# TODO
# - add --delete-remote patches:
#  - http://wget-bugs.ferrara.linux.it/issue9
#  - or http://osdir.com/ml/web.wget.patches/2005-09/msg00006.html
# - add http://article.gmane.org/gmane.comp.web.wget.patches/2333
#
# Conditional build:
%bcond_without	tests
%bcond_with	gnutls	# use GnuTLS (wget default) instead of OpenSSL

Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(es.UTF-8):	Cliente en línea de comando para bajar archivos WWW/FTP con recursión opcional
Summary(fr.UTF-8):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl.UTF-8):	Wsadowy klient HTTP/FTP
Summary(pt_BR.UTF-8):	Cliente na linha de comando para baixar arquivos WWW/FTP com recursão opcional
Summary(ru.UTF-8):	Утилита для получения файлов по протоколам HTTP и FTP
Summary(uk.UTF-8):	Утиліта для отримання файлів по протоколам HTTP та FTP
Summary(zh_CN.UTF-8):	[通讯]功能强大的下载程序,支持断点续传
Name:		wget
Version:	1.17.1
Release:	1
License:	GPL v3+ with OpenSSL exception
Group:		Networking/Utilities
Source0:	http://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.xz
# Source0-md5:	b0d58ef4963690e71effba24c105ed52
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d8b2b56ec7461606c22edbafaf8a418f
Patch0:		%{name}-info.patch
Patch1:		%{name}-wgetrc_path.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-ssl-certs.patch
Patch4:		user.xdg.origin.url.patch
URL:		http://www.gnu.org/software/wget/
BuildRequires:	attr-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.17
%{?with_gnutls:BuildRequires:	gnutls-devel}
BuildRequires:	gpgme-devel >= 0.4.2
BuildRequires:	libidn-devel
BuildRequires:	libmetalink-devel
BuildRequires:	libpsl-devel
BuildRequires:	libuuid-devel
%{!?with_gnutls:BuildRequires:	openssl-devel >= 0.9.7m}
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
BuildRequires:	zlib-devel
%if %{with tests}
BuildRequires:	perl-HTTP-Daemon
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	python3-modules >= 1:3.0
%endif
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles		%{_bindir}/rmold

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%description -l es.UTF-8
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

%description -l fr.UTF-8
GNU Wget est un utilitaire pour récupérer des fichiers qui peut
utiliser indifféremment les protocoles HTTP ou FTP. Parmi les
caractéristiques de Wget, citons la capacité à récupérer des fichiers
en arrière-plan alors que vous n'êtes pas connecté, la récupération
récursive de répertoires, la capacité de récupérer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
récupérer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particulièrement configurable.

%description -l ja.UTF-8
GNU wget は HTTP か FTP プロトコルのどちらかを使用することができる
ファイルを取得するユーティリティです。wget はログアウトしている
間にバックグラウンドで働く特徴をもっていること、ディレクトリの再帰的
取得、ファイルネームのワイルドカードマッチング、ファイルのタイムスタンプの
保存と比較、遅く不安定な接続で FTP サーバの Rest と HTTP サーバの
Range の使用、プロキシーサーバのサポートと設定の容易さを含んだ特徴を
もっています。

%description -l pl.UTF-8
Wget jest klientem FTP/HTTP przeznaczonym do ściągania zasobów
wsadowo. Umożliwia ściąganie zasobów z podkatalogami, a także ma opcje
umożliwiające wykonanie lokalnej kopii zasobów (mirror). W razie
niemożności dostania się do zasobów lub gdy połączenie z serwerem
FTP/HTTP zostanie zerwane, może automatycznie ponawiać próby
kopiowania. Jest także dobrze przystosowany do tego, żeby uruchamiać
go jako zadanie z crona.

%description -l pt_BR.UTF-8
O GNU wget é uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo não interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conexões lentas ou instáveis,
baixando o arquivo até que ele seja completamente recebido.

%description -l ru.UTF-8
GNU Wget - это утилита командной строки для получения файлов по
протоколам FTP и HTTP. Среди возможностей Wget - работа в фоновом
режиме когда вы выходите из системы, рекурсивное извлечение каталогов,
выбор файлов по шаблону, сравнение времени удаленных и локальных
файлов, сохранение времени удаленных файлов при загрузке,
использование REST с FTP серверами и Range с HTTP серверами для
загрузки файлов по медленным или нестабильным каналам, поддержка Proxy
серверов, конфигурируемость.

%description -l uk.UTF-8
GNU Wget - це утиліта командного рядка для отримання файлів по
протоколам FTP та HTTP. Серед можливостей Wget - робота в фоновому
режимі коли ви виходите із системи, рекурсивне отримання каталогів,
вибір файлів по шаблону, порівняння часу віддалених та локальних
файлів, збереження часу віддалених файлів при завантаженні,
використання REST з FTP серверами та Range з HTTP серверами для
завантаження файлів по повільним чи нестабільним каналам, підтримка
Proxy серверів, настроюваність.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%{__rm} doc/wget.info doc/sample.wgetrc.munged_for_texi_inclusion po/stamp-po

# temp hack for 1.13.4
test -e build-aux/bzr-version-gen || cat <<EOF > build-aux/bzr-version-gen
#!/bin/sh
echo -n %{version}
EOF
chmod +x build-aux/bzr-version-gen

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-digest \
	--enable-ipv6 \
	--enable-iri \
	--enable-largefile \
	--enable-nls \
	--enable-ntlm \
	--enable-opie \
	--enable-pcre \
	--with-libpsl \
	--with-ssl%{!?with_gnutls:=openssl} \
	--with-zlib \
	%{nil}
%{__make}
tail -n 6 util/README >rmold.README

# 1.13.4 tarball was buggy and produced empty version.
grep %{version} src/version.c

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GETTEXT_PACKAGE=wget

install -p util/rmold.pl $RPM_BUILD_ROOT%{_bindir}/rmold
cp -a doc/sample.wgetrc	$RPM_BUILD_ROOT%{_sysconfdir}/wgetrc

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README MAILING-LIST rmold.README
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/rmold
%attr(755,root,root) %{_bindir}/wget
%{_mandir}/man1/wget.1*
%{_mandir}/hu/man1/wget.1*
%{_mandir}/pl/man1/wget.1*
%{_infodir}/wget.info*
