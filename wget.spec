Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP 
Name:		wget
Version:	1.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.gnu.org/pub/gnu/wget/%{name}-%{version}.tar.gz
Source1:	%{name}.pl.po
Patch0:		%{name}-info.patch
Patch1:		%{name}-am_ac.patch
Patch2:		http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/%{name}-1.7-ipv6-20010604.patch.gz
URL:		http://sunsite.dk/wget/
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	autoconf
BuildRequires:	texinfo
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%description -l fr
GNU Wget est un utilitaire pour récupérer des fichiers qui peut
utiliser indifféremment les protocoles HTTP ou FTP. Parmi les
caractéristiques de Wget, citons la capacité à récupérer des fichiers
en arrière-plan alors que vous n'êtes pas connecté, la récupération
récursive de répertoires, la capacité de récupérer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
récupérer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particulièrement configurable.

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do ¶ci±gania zasobów
wsadowo. Umo¿liwia ¶ci±ganie zasobów z podkatalogami, a tak¿e ma opcje
umo¿liwiaj±ce wykonanie lokalnej kopii zasobów (mirror). W razie
niemo¿no¶ci dostania siê do zasobów lub gdy po³±czenie z serwerem
FTP/HTTP zostanie zerwane, mo¿e automatycznie ponawiaæ próby
kopiowania. Jest tak¿e dobrze przystosowany do tego, ¿eby uruchamiaæ
go jako zadanie z cron'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
install %{SOURCE1} po/pl.po

%build
autoheader
autoconf
%configure \
	--with-ssl \
	--enable-ipv6
%{__make}
tail -6 util/README >rmold.README

(cd doc; makeinfo --force %{name}.texi; touch *)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

echo "y" | %{__make} install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_sysconfdir}/wgetrc.* $RPM_BUILD_ROOT%{_sysconfdir}/wgetrc
install util/rmold.pl $RPM_BUILD_ROOT%{_bindir}/rmold

gzip -9nf AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README 

%find_lang %{name}
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
%fix_info_dir

%postun
%fix_info_dir

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
