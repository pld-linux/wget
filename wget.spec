Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(es):	Cliente en lМnea de comando para bajar archivos WWW/FTP con recursiСn opcional
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP
Summary(pt_BR):	Cliente na linha de comando para baixar arquivos WWW/FTP com recursЦo opcional
Summary(ru):	Утилита для получения файлов по протоколам HTTP и FTP
Summary(uk):	Утил╕та для отримання файл╕в по протоколам HTTP та FTP
Summary(zh_CN):	[м╗я╤]╧╕дэг©╢С╣добтьЁлпР,ж╖Ёж╤о╣ЦпЬ╢╚
Name:		wget
Version:	1.8.2
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.gnu.org/pub/gnu/wget/%{name}-%{version}.tar.gz
# Source0-md5:	a2473d7a53ebaf0a1bdb06f17059e8f1
Source2:	%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	bad85be11d26aeab8158cdfcf7e7483e
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac.patch
# based on http://www14.u-page.so-net.ne.jp/db3/h-yamamo/ipv6/patches/%{name}-1.8.1-v6-20219.patch.gz
Patch2:		%{name}-ipv6.patch
Patch3:		%{name}-ht.patch
Patch4:		%{name}-filename.patch
Patch5:		%{name}-terminate_filename.patch
URL:		http://sunsite.dk/wget/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel < 0.11
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	texinfo
BuildRequires:	perl-devel
Provides:	webclient
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

%description -l es
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

%description -l fr
GNU Wget est un utilitaire pour rИcupИrer des fichiers qui peut
utiliser indiffИremment les protocoles HTTP ou FTP. Parmi les
caractИristiques de Wget, citons la capacitИ Ю rИcupИrer des fichiers
en arriХre-plan alors que vous n'Йtes pas connectИ, la rИcupИration
rИcursive de rИpertoires, la capacitИ de rИcupИrer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
rИcupИrer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particuliХrement configurable.

%description -l ja
GNU wget ╓о HTTP ╓╚ FTP ╔в╔М╔х╔Ё╔К╓н╓и╓а╓И╓╚╓Р╩хмя╓╧╓К╓Ё╓х╓╛╓г╓╜╓К
╔у╔║╔╓╔К╓Р╪Хфю╓╧╓К╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓г╓╧║ёwget ╓о╔М╔╟╔╒╔╕╔х╓╥╓ф╓╓╓К
╢ж╓к╔п╔ц╔╞╔╟╔И╔╕╔С╔и╓гф╞╓╞фцд╖╓Р╓Б╓ц╓ф╓╓╓К╓Ё╓х║╒╔г╔ё╔Л╔╞╔х╔Й╓н╨ф╣╒е╙
╪Хфю║╒╔у╔║╔╓╔К╔м║╪╔Ю╓н╔О╔╓╔К╔и╔╚║╪╔и╔ч╔ц╔а╔С╔╟║╒╔у╔║╔╓╔К╓н╔©╔╓╔Ю╔╧╔©╔С╔в╓н
йщб╦╓ххФЁс║╒цы╓╞ит╟бдЙ╓йюэбЁ╓г FTP ╔╣║╪╔п╓н Rest ╓х HTTP ╔╣║╪╔п╓н
Range ╓н╩хмя║╒╔в╔М╔╜╔╥║╪╔╣║╪╔п╓н╔╣╔щ║╪╔х╓хюъдЙ╓нмф╟в╓╣╓Р╢ч╓С╓юфцд╖╓Р
╓Б╓ц╓ф╓╓╓ч╓╧║ё

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do ╤ci╠gania zasobСw
wsadowo. Umo©liwia ╤ci╠ganie zasobСw z podkatalogami, a tak©e ma opcje
umo©liwiaj╠ce wykonanie lokalnej kopii zasobСw (mirror). W razie
niemo©no╤ci dostania siЙ do zasobСw lub gdy poЁ╠czenie z serwerem
FTP/HTTP zostanie zerwane, mo©e automatycznie ponawiaФ prСby
kopiowania. Jest tak©e dobrze przystosowany do tego, ©eby uruchamiaФ
go jako zadanie z crona.

%description -l pt_BR
O GNU wget И uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo nЦo interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conexУes lentas ou instАveis,
baixando o arquivo atИ que ele seja completamente recebido.

%description -l ru
GNU Wget - это утилита командной строки для получения файлов по
протоколам FTP и HTTP. Среди возможностей Wget - работа в фоновом
режиме когда вы выходите из системы, рекурсивное извлечение каталогов,
выбор файлов по шаблону, сравнение времени удаленных и локальных
файлов, сохранение времени удаленных файлов при загрузке,
использование REST с FTP серверами и Range с HTTP серверами для
загрузки файлов по медленным или нестабильным каналам, поддержка Proxy
серверов, конфигурируемость.

%description -l uk
GNU Wget - це утил╕та командного рядка для отримання файл╕в по
протоколам FTP та HTTP. Серед можливостей Wget - робота в фоновому
режим╕ коли ви виходите ╕з системи, рекурсивне отримання каталог╕в,
виб╕р файл╕в по шаблону, пор╕вняння часу в╕ддалених та локальних
файл╕в, збереження часу в╕ддалених файл╕в при завантаженн╕,
використання REST з FTP серверами та Range з HTTP серверами для
завантаження файл╕в по пов╕льним чи нестаб╕льним каналам, п╕дтримка
Proxy сервер╕в, настроюван╕сть.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--with-ssl \
	--enable-ipv6
%{__make}
tail -6 util/README >rmold.README

cd doc
makeinfo --force %{name}.texi; touch *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

echo "y" | \
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

install util/rmold.pl		$RPM_BUILD_ROOT%{_bindir}/rmold
install doc/sample.wgetrc	$RPM_BUILD_ROOT%{_sysconfdir}/wgetrc

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
