Summary:	Command-line HTTP and FTP client
Summary(pl):	Wsadowy klient HTTP/FTP 
Name:		wget
Version:	1.5.3
Release:	8
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		wget-man.patch
Patch1:		wget-pl.po.patch
Patch2:		wget-info.patch
Patch3:		wget-1.5.3-ipv6.patch
Patch4:		wget-DESTDIR.patch
Prereq:		/sbin/install-info
URL:		http://sunsite.auc.dk/ftp/pub/infosystems/wget/
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_sysconfdir	/etc

%description
wget is a command-line program to fetch files via HTTP or FTP. It
supports recursive retrieval and mirroring options, and it automatically
retries several times before giving up, so it is well-suited to running
from cron jobs.

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do �ci�gania zasob�w wsadowo. 
Umo�liwia �ci�ganie zasob�w z podkatalogami, a tak�e ma opcje umo�liwiaj�ce 
wykonanie lokalnej kopii zasob�w (mirror). W razie niemo�no�ci dostania si� 
do zasob�w lub gdy po��czenie z serwerem FTP/HTTP zostanie zerwane, mo�e 
automatycznie ponawia� pr�by kopiowania. Jest tak�e dobrze przystosowany do 
tego, �eby uruchamia� go jako zadanie z cron'a.

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

make install \
	DESTDIR=$RPM_BUILD_ROOT

install -m755 util/rmold.pl $RPM_BUILD_ROOT%{_bindir}/rmold

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/%{name}.info*,%{_mandir}/man1/*} \
    AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README

%find_lang %{name}
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info.gz /etc/info-dir

%postun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz /etc/info-dir
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,MAILING-LIST,NEWS,TODO,README,rmold.README}.gz
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/%{name}.info*
