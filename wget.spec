Summary:	Command-line HTTP and FTP client
Summary(pl):	Wsadowy klient HTTP/FTP 
Name:		wget
Version:	1.5.3
Release:	8
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		wget-man.patch
Patch1:		wget-pl.po.patch
Patch2:		wget-info.patch
BuildPrereq:	autoconf >= 2.13-8
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

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir}
make
tail -6 util/README >rmold.README

(cd doc; makeinfo --force %{name}.texi; touch *)

%install
rm -rf $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

install -c util/rmold.pl $RPM_BUILD_ROOT%{_bindir}/rmold

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/%{name}.info*,%{_mandir}/man1/*} \
    AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info.gz /etc/info-dir

%postun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,MAILING-LIST,NEWS,TODO,README,rmold.README}.gz

%attr(755,root,root) %{_bindir}/*

%lang(cs)    %{_datadir}/locale/cs/LC_MESSAGES/%{name}.mo
%lang(de)    %{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%lang(hr)    %{_datadir}/locale/hr/LC_MESSAGES/%{name}.mo
%lang(it)    %{_datadir}/locale/it/LC_MESSAGES/%{name}.mo
%lang(no)    %{_datadir}/locale/no/LC_MESSAGES/%{name}.mo
%lang(pl)    %{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo

%{_mandir}/man1/*
%{_infodir}/%{name}.info*

%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}rc

%changelog
* Thu May 20 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.5.3-8]
- package is FHS 2.0 compliant,
- based on spec file written by ??? <root@ricketts.stannes.ox.ac.uk>,
  rewritten for PLD use by me, Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>,
  and Micha³ Kuratczyk <kura@pld.org.pl>,
- pl translation by Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  and Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
