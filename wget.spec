Summary:     Command-line HTTP and FTP client
Summary(pl): Wsadowy klient HTTP/FTP 
Name:        wget
Version:     1.5.2
Release:     2
Copyright:   GPL
Group:       Networking/Utilities
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:      wget-man.patch
Patch1:      wget-pl.po.patch
Prereq:      /sbin/install-info
BuildRoot:   /tmp/%{name}-%{version}-root

%description
wget is a command-line program to fetch files via HTTP or FTP.  It
supports recursive retrieval and mirroring options, and it automatically
retries several times before giving up, so it is well-suited to running
from cron jobs.

%description -l pl
wget jest klientem FTP/HTTP przeznaczonym do �ci�gania zasob�w zasob�w
wsadowo. Umo�liwia �ci�ganie zasob�w z podkatalogami, a tak�e opcje
umo�liwiaj�ce wykonanie lokalnej kopi zasob�w (mirror). W razie nie mo�no�ci
dostania si� do zasob�w mo�e automatycznie ponawia� pr�by kopiowania
zasob�w. Jest tak�e dobrze przystosowany do tego �eby uruchamia� go jako
zadanie z cron'a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS=-s \
	./configure --prefix=/usr --sysconfdir=/etc
make
tail -6 util/README >rmold.README

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc install
gzip -9nf $RPM_BUILD_ROOT/usr/info/wget.info*
install -c util/rmold.pl $RPM_BUILD_ROOT/usr/bin/rmold

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/wget.info.gz /usr/info/dir

%postun
/sbin/install-info --delete /usr/info/wget.info.gz /usr/info/dir

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog MAILING-LIST NEWS README TODO rmold.README
%verify(not md5 size mtime) %config(noreplace) /etc/wgetrc
%attr(711, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/info/wget.info*
%lang(cs) /usr/share/locale/cs/LC_MESSAGES/wget.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/wget.mo
%lang(hr) /usr/share/locale/hr/LC_MESSAGES/wget.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/wget.mo
%lang(no) /usr/share/locale/no/LC_MESSAGES/wget.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/wget.mo
%lang(pt) /usr/share/locale/pt_BR/LC_MESSAGES/wget.mo

%changelog
* Mon Sep  7 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-2]
- added wget-pl.po.patch patch with polish translation 
  (Adam Kozubowicz <tapir@interdata.com.pl>,
- added wget-man.patch patch with wget man page,
- changed permission on binaries to 711.

* Sat Aug  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.2-1]
- added pl translation.

* Sun May 17 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.1-2]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot and Source,
- added %verify(not md5 size mtime) and noreplace parameter for %config,
- removed COPYING from %doc (copyright statment is in Copyright
  field),
- added %postun, %post sections with {de}instaling wget info pages,
- spec file rewrited for using Buildroot,
- added %clean section,
- added URL,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- Buildroot changed to /tmp/lftp-%%{PACKAGE_VERSION}-root,
- added %%{PACKAGE_VERSION} to Source url,
- replaced "mkdir -p" with "install -d" in %install,
- base datadir changed to /usr/share,
- added %lang macros for /usr/share/locale/*/LC_MESSAGES/wget.mo files,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Thu May  7 1998 ??? <root@ricketts.stannes.ox.ac.uk>
  [1.5.1-1]
- previous release in rpm package.
