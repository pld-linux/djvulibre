Summary:	DjVu viewers, encoders and utilities
Summary(pl):	DjVu - przegl±darki, dekodery oraz narzêdzia
Name:		djvulibre
Version:	3.5.14
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# Source0-md5:	4a3f17603468b2e6969190be18bf00d0
Patch0:		%{name}-opt.patch
Patch1:		%{name}-nostrip.patch
Patch2:		%{name}-desktop.patch
URL:		http://djvu.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 3.0.5
Obsoletes:	djvu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mozdir		/usr/%{_lib}/mozilla/plugins
%define		nsdir		/usr/%{_lib}/netscape/plugins

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
rozwijan± przez pomys³odawców DjVu. Jest kompatybilna z wersj±
3.5 oprogramowania LizardTech DjVu.

Ten pakiet zawiera: bibliotekê w C++, zestaw kompresorów, dekoderów
i narzêdzi do plików w formacie DjVu. Przegl±darka oraz wtyczki do
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

%package -n mozilla-plugin-%{name}
Summary:	DjVu plugin for Mozilla
Summary(pl):	Wtyczka DjVu do Mozilli
Group:		X11/Libraries
Requires:	%{name}-djview = %{version}-%{release}
Requires:	mozilla-embedded

%description -n mozilla-plugin-%{name}
DjVu plugin for Mozilla and Mozilla-based browsers.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka DjVu do Mozilli i przegl±darek na niej bazuj±cych.

%package -n netscape-plugin-%{name}
Summary:	DjVu plugin for Netscape
Summary(pl):	Wtyczka DjVu do Netscape
Group:		X11/Libraries
Requires:	%{name}-djview = %{version}-%{release}
Requires:	netscape-common
Obsoletes:	djview-netscape

%description -n netscape-plugin-%{name}
DjVu plugin for Netscape.

%description -n netscape-plugin-%{name} -l pl
Wtyczka DjVu do Netscape.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
install -d $RPM_BUILD_ROOT{%{mozdir},%{nsdir}}

# pass dtop_* to allow build w/o gnome/kde/etc. installed
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{mozdir} \
	dtop_applications=%{_desktopdir} \
	dtop_icons=%{_iconsdir} \
	dtop_mimelnk=%{_datadir}/mimelnk \
	dtop_applnk= \
	dtop_pixmaps=%{_pixmapsdir} \
	dtop_mime_info=%{_datadir}/mime-info \
	dtop_application_registry=%{_datadir}/application-registry

cp -f $RPM_BUILD_ROOT%{mozdir}/nsdejavu.so $RPM_BUILD_ROOT%{nsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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

%files djview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/djview
%{_mandir}/man1/djview.1*
%lang(ja) %{_mandir}/ja/man1/djview.1*
%{_desktopdir}/djview.desktop
%{_pixmapsdir}/djvu.png
# KDE-specific
%{_iconsdir}/hicolor/*/mimetypes/djvu.png
%{_datadir}/mimelnk/image/x-djvu.desktop
# GNOME-specific
%{_datadir}/mime-info/djvu.*
%{_datadir}/application-registry/djvu.applications

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{mozdir}/*.so
%{_mandir}/man1/nsdejavu.1*
%lang(ja) %{_mandir}/ja/man1/nsdejavu.1*

%files -n netscape-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{nsdir}/*.so
