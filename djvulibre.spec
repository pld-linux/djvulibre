#
# Conditional build:
%bcond_without	qt	# disable qt wrapper
#
Summary:	DjVu viewers, encoders and utilities
Summary(pl):	DjVu - przegl�darki, dekodery oraz narz�dzia
Name:		djvulibre
Version:	3.5.18
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# Source0-md5:	73fd6d4f92832b85a91529b7bb3b7710
Patch0:		%{name}-opt.patch
Patch1:		%{name}-nostrip.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-link.patch
URL:		http://djvu.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
%{?with_qt:BuildRequires:	qt-devel >= 3.0.5}
BuildRequires:	rpmbuild(macros) >= 1.357
Obsoletes:	djvu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DjVu is a web-centric format and software platform for distributing
documents and images. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consume less client
resources than competing formats. DjVu was originally developed at
AT&T Labs-Research by Leon Bottou, Yann LeCun, Patrick Haffner, and
many others. In March 2000, AT&T sold DjVu to LizardTech Inc. who now
distributes Windows/Mac plug-ins, and commercial encoders (mostly on
Windows).

In an effort to promote DjVu as a Web standard, the LizardTech
management was enlightened enough to release the reference
implementation of DjVu under the GNU GPL in October 2000. DjVuLibre
(which means free DjVu), is an enhanced version of that code
maintained by the original inventors of DjVu. It is compatible with
version 3.5 of the LizardTech DjVu software suite.

This package of DjVulibre 3.5 contains:
- A full-fledged wavelet-based compressor for pictures.
- A simple compressor for bitonal (black and white) scanned pages.
- A compressor for palettized images (a la GIF/PNG).
- A set of utilities to manipulate and assemble DjVu images and
  documents.
- A set of decoders to convert DjVu to a number of other formats.
- An up-to-date version of the C++ DjVu Reference Library.

Following elements are placed in other subpackages:
- a standalone DjVu viewer based on the Qt library.
- A browser plugin that works with most Unix browsers.

%description -l pl
DjVu jest przeznaczonym g��wnie dla WWW formatem i platform�
programow� do dystrybucji dokument�w i obrazk�w. Dane w DjVu �ci�gaj�
si� szybciej, wy�wietlaj� szybciej, wygl�daj� �adniej na ekranie i
zajmuj� mniej zasob�w po stronie klienckiej ni� inne formaty. DjVu
oryginalnie zosta� stworzony w AT&T Labs-Research przez Leona Bottou,
Yanna LeCun, Patricka Haffnera i wielu innych. W marcu 2000 AT&T
sprzeda�o DjVu firmie LizardTech Inc., kt�re teraz rozpowszechnia
wtyczki dla Windows i Maca oraz komercyjne kodery (g��wnie dla
Windows).

Aby wypromowa� DjVu jako sieciowy standard, LizardTech udost�pni�
wzorcow� implementacj� DjVu na licencji GPL w pa�dzierniku 2000.
DjVuLibre (czyli wolne DjVu) jest rozszerzon� wersj� tego kodu
rozwijan� przez pomys�odawc�w DjVu. Jest kompatybilna z wersj� 3.5
oprogramowania LizardTech DjVu.

Ten pakiet zawiera: bibliotek� w C++, zestaw kompresor�w, dekoder�w i
narz�dzi do plik�w w formacie DjVu. Przegl�darka oraz wtyczki do
przegl�darek znajduj� si� w innych podpakietach.

%package devel
Summary:	Header file for DjVu library
Summary(pl):	Plik nag��wkowy biblioteki DjVu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libstdc++-devel

%description devel
Header file for DjVu library.

%description devel -l pl
Plik nag��wkowy biblioteki DjVu.

%package djview
Summary:	Qt-based DjVu viewer
Summary(pl):	Oparta o Qt przegl�darka DjVu
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	djview

%description djview
Qt-based DjVu viewer.

%description djview -l pl
Oparta o Qt przegl�darka DjVu.

%package -n browser-plugin-%{name}
Summary:	DjVu browser plugin
Summary(pl):	Wtyczka DjVu do przegl�derek WWW
Group:		X11/Libraries
Requires:	%{name}-djview = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
# for migrate purposes (greedy poldek upgrade)
Provides:	mozilla-plugin-djvulibre
Provides:	netscape-plugin-djvulibre
Obsoletes:	djview-netscape
Obsoletes:	mozilla-plugin-djvulibre
Obsoletes:	netscape-plugin-djvulibre

%description -n browser-plugin-%{name}
DjVu plugin for Mozilla and Mozilla-based browsers.

%description -n browser-plugin-%{name} -l pl
Wtyczka DjVu do przegl�darek zgodnych z Mozill�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{__sed} -e 's,@lib@,%{_lib},' %{PATCH3} | %{__patch} -p1

%build
cp -f /usr/share/automake/config.sub config
%{__aclocal} -I config
%{__autoconf}
export QT_LIBS="-L%{_libdir} -lqt-mt"
export QT_CFLAGS="-I%{_includedir}/qt"
%configure \
	PTHREAD_LIBS="-lpthread"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_browserpluginsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_browserpluginsdir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/djview.1
echo '.so djview3.1' > $RPM_BUILD_ROOT%{_mandir}/man1/djview.1
echo '.so djview3.1' > $RPM_BUILD_ROOT%{_mandir}/ja/man1/djview.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT NEWS README TODO doc/*
%attr(755,root,root) %{_bindir}/[!d]*
%attr(755,root,root) %{_bindir}/d[!j]*
%attr(755,root,root) %{_bindir}/djv[!i]*
%attr(755,root,root) %{_libdir}/libdjvulibre.so.*.*.*
%{_mandir}/man1/[!dn]*
%{_mandir}/man1/d[!j]*
%{_mandir}/man1/djv[!i]*
%lang(ja) %{_mandir}/ja/man1/[!dn]*
%lang(ja) %{_mandir}/ja/man1/d[!j]*
%lang(ja) %{_mandir}/ja/man1/djv[!i]*
%dir %{_datadir}/djvu
%dir %{_datadir}/djvu/osi
%{_datadir}/djvu/osi/languages.xml
%lang(de) %{_datadir}/djvu/osi/de
%{_datadir}/djvu/osi/en
%lang(fr) %{_datadir}/djvu/osi/fr
%lang(ja) %{_datadir}/djvu/osi/ja
%lang(zh) %{_datadir}/djvu/osi/zh
%{_datadir}/djvu/pubtext

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdjvulibre.so
%{_libdir}/libdjvulibre.la
%{_includedir}/libdjvu
%{_pkgconfigdir}/ddjvuapi.pc

%if %{with qt}
%files djview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/djview
%attr(755,root,root) %{_bindir}/djview3
%dir %{_datadir}/djvu/djview3
%lang(de) %{_datadir}/djvu/djview3/de
%lang(fr) %{_datadir}/djvu/djview3/fr
%lang(ja) %{_datadir}/djvu/djview3/ja
%{_mandir}/man1/djview.1*
%{_mandir}/man1/djview3.1*
%lang(ja) %{_mandir}/ja/man1/djview.1*
%lang(ja) %{_mandir}/ja/man1/djview3.1*
%{_desktopdir}/djvulibre-djview3.desktop
%{_iconsdir}/hicolor/*/apps/djvulibre-djview3.png
%{_iconsdir}/hicolor/*/mimetypes/mime-image-vnd.djvu.png

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/nsdejavu.so
%{_mandir}/man1/nsdejavu.1*
%lang(ja) %{_mandir}/ja/man1/nsdejavu.1*
%endif
