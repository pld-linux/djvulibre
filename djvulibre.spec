# TODO: use system qt qt.qm files instead of included copies
#
# Conditional build:
%define		base_ver	3.5.25
%define		minor_ver	.3
#
Summary:	DjVu viewers, encoders and utilities
Summary(pl.UTF-8):	DjVu - przeglądarki, dekodery oraz narzędzia
Name:		djvulibre
Version:	%{base_ver}%{minor_ver}
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# Source0-md5:	5f45d6cd5700b4dd31b1eb963482089b
Patch0:		%{name}-opt.patch
Patch1:		djvulibre-3.5.22-cdefs.patch
URL:		http://djvu.sourceforge.net/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
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

%description -l pl.UTF-8
DjVu jest przeznaczonym głównie dla WWW formatem i platformą
programową do dystrybucji dokumentów i obrazków. Dane w DjVu ściągają
się szybciej, wyświetlają szybciej, wyglądają ładniej na ekranie i
zajmują mniej zasobów po stronie klienckiej niż inne formaty. DjVu
oryginalnie został stworzony w AT&T Labs-Research przez Leona Bottou,
Yanna LeCun, Patricka Haffnera i wielu innych. W marcu 2000 AT&T
sprzedało DjVu firmie LizardTech Inc., które teraz rozpowszechnia
wtyczki dla Windows i Maca oraz komercyjne kodery (głównie dla
Windows).

Aby wypromować DjVu jako sieciowy standard, LizardTech udostępnił
wzorcową implementację DjVu na licencji GPL w październiku 2000.
DjVuLibre (czyli wolne DjVu) jest rozszerzoną wersją tego kodu
rozwijaną przez pomysłodawców DjVu. Jest kompatybilna z wersją 3.5
oprogramowania LizardTech DjVu.

Ten pakiet zawiera: bibliotekę w C++, zestaw kompresorów, dekoderów i
narzędzi do plików w formacie DjVu.

%package devel
Summary:	Header files for DjVu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki DjVu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libstdc++-devel

%description devel
Header files for DjVu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DjVu.

%prep
%setup -q -n %{name}-%{base_ver}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%configure \
	PTHREAD_LIBS="-lpthread" \
	--disable-desktopfiles

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT NEWS README doc/*
%attr(755,root,root) %{_bindir}/any2djvu
%attr(755,root,root) %{_bindir}/bzz
%attr(755,root,root) %{_bindir}/c44
%attr(755,root,root) %{_bindir}/cjb2
%attr(755,root,root) %{_bindir}/cpaldjvu
%attr(755,root,root) %{_bindir}/csepdjvu
%attr(755,root,root) %{_bindir}/ddjvu
%attr(755,root,root) %{_bindir}/djvm
%attr(755,root,root) %{_bindir}/djvmcvt
%attr(755,root,root) %{_bindir}/djvu*
%attr(755,root,root) %{_libdir}/libdjvulibre.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdjvulibre.so.21
%{_mandir}/man1/any2djvu.1*
%{_mandir}/man1/bzz.1*
%{_mandir}/man1/c44.1*
%{_mandir}/man1/cjb2.1*
%{_mandir}/man1/cpaldjvu.1*
%{_mandir}/man1/csepdjvu.1*
%{_mandir}/man1/ddjvu.1*
%{_mandir}/man1/djvm.1*
%{_mandir}/man1/djvmcvt.1*
%{_mandir}/man1/djvu*.1*
%dir %{_datadir}/djvu
%dir %{_datadir}/djvu/osi
%{_datadir}/djvu/osi/languages.xml
%lang(cs) %{_datadir}/djvu/osi/cs
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
