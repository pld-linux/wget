Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(es):	Cliente en línea de comando para bajar archivos WWW/FTP con recursión opcional
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP
Summary(pt_BR):	Cliente na linha de comando para baixar arquivos WWW/FTP com recursão opcional
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ÐÏÌÕÞÅÎÉÑ ÆÁÊÌÏ× ÐÏ ÐÒÏÔÏËÏÌÁÍ HTTP É FTP
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ÏÔÒÉÍÁÎÎÑ ÆÁÊÌ¦× ÐÏ ÐÒÏÔÏËÏÌÁÍ HTTP ÔÁ FTP
Summary(zh_CN):	[Í¨Ñ¶]¹¦ÄÜÇ¿´óµÄÏÂÔØ³ÌÐò,Ö§³Ö¶ÏµãÐø´«
Name:		wget
Version:	1.9.1
Release:	5
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz
# Source0-md5:	e6051f1e1487ec0ebfdbda72bedc70ad
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d8b2b56ec7461606c22edbafaf8a418f
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-m4.patch
Patch3:		%{name}-lame_fs.patch
Patch4:		%{name}-pl.patch
Patch5:		%{name}-wgetrc_path.patch
Patch6:		%{name}-back-to-ipv4.patch
Patch7:		%{name}-home_etc.patch
Patch8:		%{name}-strptime.patch
Patch9:		%{name}-porn.patch
Patch10:	%{name}-nonperm.patch
URL:		http://sunsite.dk/wget/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	texinfo
BuildRequires:	perl-devel
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

%description -l es
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

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

%description -l ja
GNU wget ¤Ï HTTP ¤« FTP ¥×¥í¥È¥³¥ë¤Î¤É¤Á¤é¤«¤ò»ÈÍÑ¤¹¤ë¤³¤È¤¬¤Ç¤­¤ë
¥Õ¥¡¥¤¥ë¤ò¼èÆÀ¤¹¤ë¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ç¤¹¡£wget ¤Ï¥í¥°¥¢¥¦¥È¤·¤Æ¤¤¤ë
´Ö¤Ë¥Ð¥Ã¥¯¥°¥é¥¦¥ó¥É¤ÇÆ¯¤¯ÆÃÄ§¤ò¤â¤Ã¤Æ¤¤¤ë¤³¤È¡¢¥Ç¥£¥ì¥¯¥È¥ê¤ÎºÆµ¢Åª
¼èÆÀ¡¢¥Õ¥¡¥¤¥ë¥Í¡¼¥à¤Î¥ï¥¤¥ë¥É¥«¡¼¥É¥Þ¥Ã¥Á¥ó¥°¡¢¥Õ¥¡¥¤¥ë¤Î¥¿¥¤¥à¥¹¥¿¥ó¥×¤Î
ÊÝÂ¸¤ÈÈæ³Ó¡¢ÃÙ¤¯ÉÔ°ÂÄê¤ÊÀÜÂ³¤Ç FTP ¥µ¡¼¥Ð¤Î Rest ¤È HTTP ¥µ¡¼¥Ð¤Î
Range ¤Î»ÈÍÑ¡¢¥×¥í¥­¥·¡¼¥µ¡¼¥Ð¤Î¥µ¥Ý¡¼¥È¤ÈÀßÄê¤ÎÍÆ°×¤µ¤ò´Þ¤ó¤ÀÆÃÄ§¤ò
¤â¤Ã¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do ¶ci±gania zasobów
wsadowo. Umo¿liwia ¶ci±ganie zasobów z podkatalogami, a tak¿e ma opcje
umo¿liwiaj±ce wykonanie lokalnej kopii zasobów (mirror). W razie
niemo¿no¶ci dostania siê do zasobów lub gdy po³±czenie z serwerem
FTP/HTTP zostanie zerwane, mo¿e automatycznie ponawiaæ próby
kopiowania. Jest tak¿e dobrze przystosowany do tego, ¿eby uruchamiaæ
go jako zadanie z crona.

%description -l pt_BR
O GNU wget é uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo não interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conexões lentas ou instáveis,
baixando o arquivo até que ele seja completamente recebido.

%description -l ru
GNU Wget - ÜÔÏ ÕÔÉÌÉÔÁ ËÏÍÁÎÄÎÏÊ ÓÔÒÏËÉ ÄÌÑ ÐÏÌÕÞÅÎÉÑ ÆÁÊÌÏ× ÐÏ
ÐÒÏÔÏËÏÌÁÍ FTP É HTTP. óÒÅÄÉ ×ÏÚÍÏÖÎÏÓÔÅÊ Wget - ÒÁÂÏÔÁ × ÆÏÎÏ×ÏÍ
ÒÅÖÉÍÅ ËÏÇÄÁ ×Ù ×ÙÈÏÄÉÔÅ ÉÚ ÓÉÓÔÅÍÙ, ÒÅËÕÒÓÉ×ÎÏÅ ÉÚ×ÌÅÞÅÎÉÅ ËÁÔÁÌÏÇÏ×,
×ÙÂÏÒ ÆÁÊÌÏ× ÐÏ ÛÁÂÌÏÎÕ, ÓÒÁ×ÎÅÎÉÅ ×ÒÅÍÅÎÉ ÕÄÁÌÅÎÎÙÈ É ÌÏËÁÌØÎÙÈ
ÆÁÊÌÏ×, ÓÏÈÒÁÎÅÎÉÅ ×ÒÅÍÅÎÉ ÕÄÁÌÅÎÎÙÈ ÆÁÊÌÏ× ÐÒÉ ÚÁÇÒÕÚËÅ,
ÉÓÐÏÌØÚÏ×ÁÎÉÅ REST Ó FTP ÓÅÒ×ÅÒÁÍÉ É Range Ó HTTP ÓÅÒ×ÅÒÁÍÉ ÄÌÑ
ÚÁÇÒÕÚËÉ ÆÁÊÌÏ× ÐÏ ÍÅÄÌÅÎÎÙÍ ÉÌÉ ÎÅÓÔÁÂÉÌØÎÙÍ ËÁÎÁÌÁÍ, ÐÏÄÄÅÒÖËÁ Proxy
ÓÅÒ×ÅÒÏ×, ËÏÎÆÉÇÕÒÉÒÕÅÍÏÓÔØ.

%description -l uk
GNU Wget - ÃÅ ÕÔÉÌ¦ÔÁ ËÏÍÁÎÄÎÏÇÏ ÒÑÄËÁ ÄÌÑ ÏÔÒÉÍÁÎÎÑ ÆÁÊÌ¦× ÐÏ
ÐÒÏÔÏËÏÌÁÍ FTP ÔÁ HTTP. óÅÒÅÄ ÍÏÖÌÉ×ÏÓÔÅÊ Wget - ÒÏÂÏÔÁ × ÆÏÎÏ×ÏÍÕ
ÒÅÖÉÍ¦ ËÏÌÉ ×É ×ÉÈÏÄÉÔÅ ¦Ú ÓÉÓÔÅÍÉ, ÒÅËÕÒÓÉ×ÎÅ ÏÔÒÉÍÁÎÎÑ ËÁÔÁÌÏÇ¦×,
×ÉÂ¦Ò ÆÁÊÌ¦× ÐÏ ÛÁÂÌÏÎÕ, ÐÏÒ¦×ÎÑÎÎÑ ÞÁÓÕ ×¦ÄÄÁÌÅÎÉÈ ÔÁ ÌÏËÁÌØÎÉÈ
ÆÁÊÌ¦×, ÚÂÅÒÅÖÅÎÎÑ ÞÁÓÕ ×¦ÄÄÁÌÅÎÉÈ ÆÁÊÌ¦× ÐÒÉ ÚÁ×ÁÎÔÁÖÅÎÎ¦,
×ÉËÏÒÉÓÔÁÎÎÑ REST Ú FTP ÓÅÒ×ÅÒÁÍÉ ÔÁ Range Ú HTTP ÓÅÒ×ÅÒÁÍÉ ÄÌÑ
ÚÁ×ÁÎÔÁÖÅÎÎÑ ÆÁÊÌ¦× ÐÏ ÐÏ×¦ÌØÎÉÍ ÞÉ ÎÅÓÔÁÂ¦ÌØÎÉÍ ËÁÎÁÌÁÍ, Ð¦ÄÔÒÉÍËÁ
Proxy ÓÅÒ×ÅÒ¦×, ÎÁÓÔÒÏÀ×ÁÎ¦ÓÔØ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
rm -f doc/wget.info*

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--with-ssl \
	--enable-ipv6
%{__make}
tail -n 6 util/README >rmold.README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install util/rmold.pl		$RPM_BUILD_ROOT%{_bindir}/rmold
install doc/sample.wgetrc	$RPM_BUILD_ROOT%{_sysconfdir}/wgetrc

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO README MAILING-LIST rmold.README
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}rc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*.info*
