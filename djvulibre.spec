# TODO
# - test and add other browsers
#
# Conditional build:
%bcond_without	qt	# disable qt wrapper
#
Summary:	DjVu viewers, encoders and utilities
Summary(pl):	DjVu - przegl±darki, dekodery oraz narzêdzia
Name:		djvulibre
Version:	3.5.16
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# Source0-md5:	5591c99a50aed1613a796a5aa4978fc0
Patch0:		%{name}-opt.patch
Patch1:		%{name}-nostrip.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-c++.patch
URL:		http://djvu.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
%{?with_qt:BuildRequires:	qt-devel >= 3.0.5}
BuildRequires:	rpmbuild(macros) >= 1.236
Obsoletes:	djvu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/browser-plugins

# list of supported browsers, in free form text
%define		browsers mozilla, netscape

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
DjVu jest przeznaczonym g³ównie dla WWW formatem i platform±
programow± do dystrybucji dokumentów i obrazków. Dane w DjVu ¶ci±gaj±
siê szybciej, wy¶wietlaj± szybciej, wygl±daj± ³adniej na ekranie i
zajmuj± mniej zasobów po stronie klienckiej ni¿ inne formaty. DjVu
oryginalnie zosta³ stworzony w AT&T Labs-Research przez Leona Bottou,
Yanna LeCun, Patricka Haffnera i wielu innych. W marcu 2000 AT&T
sprzeda³o DjVu firmie LizardTech Inc., które teraz rozpowszechnia
wtyczki dla Windows i Maca oraz komercyjne kodery (g³ównie dla
Windows).

Aby wypromowaæ DjVu jako sieciowy standard, LizardTech udostêpni³
wzorcow± implementacjê DjVu na licencji GPL w pa¼dzierniku 2000.
DjVuLibre (czyli wolne DjVu) jest rozszerzon± wersj± tego kodu
rozwijan± przez pomys³odawców DjVu. Jest kompatybilna z wersj± 3.5
oprogramowania LizardTech DjVu.

Ten pakiet zawiera: bibliotekê w C++, zestaw kompresorów, dekoderów i
narzêdzi do plików w formacie DjVu. Przegl±darka oraz wtyczki do
przegl±darek znajduj± siê w innych podpakietach.

%package devel
Summary:	Header file for DjVu library
Summary(pl):	Plik nag³ówkowy biblioteki DjVu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libstdc++-devel

%description devel
Header file for DjVu library.

%description devel -l pl
Plik nag³ówkowy biblioteki DjVu.

%package djview
Summary:	Qt-based DjVu viewer
Summary(pl):	Oparta o Qt przegl±darka DjVu
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	djview

%description djview
Qt-based DjVu viewer.

%description djview -l pl
Oparta o Qt przegl±darka DjVu.

%package -n browser-plugin-%{name}
Summary:	DjVu browser plugin
Summary(pl):	Wtyczka DjVu do przegl±derek WWW
Group:		X11/Libraries
Requires:	%{name}-djview = %{version}-%{release}
Requires:	browser-plugins(%{_target_cpu})
Obsoletes:	mozilla-plugin-djvulibre
Obsoletes:	netscape-plugin-djvulibre
Obsoletes:	djview-netscape
# for migrate purposes (greedy poldek upgrade)
Provides:	mozilla-plugin-djvulibre
Provides:	netscape-plugin-djvulibre

%description -n browser-plugin-%{name}
DjVu plugin for Mozilla and Mozilla-based browsers.

Supported browsers: %{browsers}.

%description -n browser-plugin-%{name} -l pl
Wtyczka DjVu do przegl±darek zgodnych z Mozill±.

Obs³ugiwane przegl±darki: %{browsers}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub config
%{__aclocal} -I config -I gui/desktop
%{__autoconf}
QT_LIBS="-L%{_libdir} -lqt-mt"; export QT_LIBS
QT_CFLAGS="-I%{_includedir}/qt"; export QT_CFLAGS
%configure \
	PTHREAD_LIBS="-lpthread"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

# pass dtop_* to allow build w/o gnome/kde/etc. installed
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_plugindir} \
	dtop_applications=%{_desktopdir} \
	dtop_icons=%{_iconsdir} \
	dtop_mimelnk=%{_datadir}/mimelnk \
	dtop_applnk= \
	dtop_pixmaps=%{_pixmapsdir} \
	dtop_mime_info= \
	dtop_application_registry=

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%triggerin -n browser-plugin-%{name} -- mozilla
%nsplugin_install -d %{_libdir}/mozilla/plugins nsdejavu.so

%triggerun -n browser-plugin-%{name} -- mozilla
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins nsdejavu.so

%triggerin -n browser-plugin-%{name} -- mozilla-firefox
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins nsdejavu.so

%triggerun -n browser-plugin-%{name} -- mozilla-forefox
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins nsdejavu.so

%triggerin -n browser-plugin-%{name} -- netscape-common
%nsplugin_install -d %{_libdir}/netscape/plugins nsdejavu.so

%triggerun -n browser-plugin-%{name} -- netscape-common
%nsplugin_uninstall -d %{_libdir}/netscape/plugins nsdejavu.so

# as rpm removes the old obsoleted package files after the triggers
# are ran, add another trigger to make the links there.
%triggerpostun -n browser-plugin-%{name} -- mozilla-plugin-%{name}
%nsplugin_install -f -d %{_libdir}/mozilla/plugins nsdejavu.so

%triggerpostun -n browser-plugin-%{name} -- netscape-plugin-%{name}
%nsplugin_install -f -d %{_libdir}/netscape/plugins nsdejavu.so

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
%{_datadir}/djvu/languages.xml
%dir %{_datadir}/djvu/osi
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

%if %{with qt}
%files djview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/djview
%{_mandir}/man1/djview.1*
%lang(ja) %{_mandir}/ja/man1/djview.1*
%{_datadir}/mimelnk/image/x-djvu.desktop
%{_desktopdir}/djview.desktop
%{_iconsdir}/hicolor/*/mimetypes/djvu.png
%{_pixmapsdir}/djvu.png

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*.so
%{_mandir}/man1/nsdejavu.1*
%lang(ja) %{_mandir}/ja/man1/nsdejavu.1*
%endif
