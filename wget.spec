Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP 
Name:		wget
Version:	1.5.3
Release:	10
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		wget-man.patch
Patch1:		wget-pl.po.patch
Patch2:		wget-info.patch
Patch3:		wget-1.5.3-ipv6.patch
Patch4:		wget-DESTDIR.patch
Prereq:		/usr/sbin/fix-info-dir
URL:		http://sunsite.auc.dk/ftp/pub/infosystems/wget/
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_sysconfdir	/etc

%description
wget is a command-line program to fetch files via HTTP or FTP. It
supports recursive retrieval and mirroring options, and it automatically
retries several times before giving up, so it is well-suited to running
from cron jobs.

%description -l fr
GNU Wget est un utilitaire pour récupérer des fichiers qui peut utiliser
indifféremment les protocoles HTTP ou FTP. Parmi les caractéristiques de
Wget, citons la capacité à récupérer des fichiers en arrière-plan alors que
vous n'êtes pas connecté, la récupération récursive de répertoires, la
capacité de récupérer des fichiers en appliquant un filtre sur le nom ou sur
la date, la gestion de Rest avec les serveurs FTP et de Range avec les
serveurs HTTP pour récupérer des fichiers avec une connexion lente ou
instable, le support des serveurs Proxy... Wget est particulièrement
configurable.

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do ¶ci±gania zasobów wsadowo. 
Umo¿liwia ¶ci±ganie zasobów z podkatalogami, a tak¿e ma opcje umo¿liwiaj±ce 
wykonanie lokalnej kopii zasobów (mirror). W razie niemo¿no¶ci dostania siê 
do zasobów lub gdy po³±czenie z serwerem FTP/HTTP zostanie zerwane, mo¿e 
automatycznie ponawiaæ próby kopiowania. Jest tak¿e dobrze przystosowany do 
tego, ¿eby uruchamiaæ go jako zadanie z cron'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure 
make
tail -6 util/README >rmold.README

(cd doc; makeinfo --force %{name}.texi; touch *)

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install util/rmold.pl $RPM_BUILD_ROOT%{_bindir}/rmold

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/%{name}.info*,%{_mandir}/man1/*} \
	AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README

%find_lang %{name}
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,MAILING-LIST,NEWS,TODO,README,rmold.README}.gz
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/%{name}.info*
