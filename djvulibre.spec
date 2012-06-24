Summary:	DjVu viewers, encoders and utilities
Summary(pl):	DjVu - przegl�darki, dekodery oraz narz�dzia
Name:		djvulibre
Version:	3.5.12
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# Source0-md5:	510e834a0e733a5b91e8c14db76fa849
Patch0:		%{name}-opt.patch
Patch1:		%{name}-nostrip.patch
URL:		http://djvu.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 3.0.5
Obsoletes:	djvu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mozdir		/usr/lib/mozilla/plugins
%define		nsdir		/usr/lib/netscape/plugins

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
rozwijan� przez pomys�odawc�w DjVu. Jest kompatybilna z wersj�
3.5 oprogramowania LizardTech DjVu.

Ten pakiet zawiera: bibliotek� w C++, zestaw kompresor�w, dekoder�w
i narz�dzi do plik�w w formacie DjVu. Przegl�darka oraz wtyczki do
przegl�darek znajduj� si� w innych podpakietach.

%package djview
Summary:	Qt-based DjVu viewer
Summary(pl):	Oparta o Qt przegl�darka DjVu
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	djview

%description djview
Qt-based DjVu viewer.

%description djview -l pl
Oparta o Qt przegl�darka DjVu.

%package -n mozilla-plugin-%{name}
Summary:	DjVu plugin for Mozilla
Summary(pl):	Wtyczka DjVu do Mozilli
Group:		X11/Libraries
Requires:	%{name}-djview = %{version}
Requires:	mozilla-embedded

%description -n mozilla-plugin-%{name}
DjVu plugin for Mozilla and Mozilla-based browsers.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka DjVu do Mozilli i przegl�darek na niej bazuj�cych.

%package -n netscape-plugin-%{name}
Summary:	DjVu plugin for Netscape
Summary(pl):	Wtyczka DjVu do Netscape
Group:		X11/Libraries
Requires:	%{name}-djview = %{version}
Requires:	netscape-common
Obsoletes:	djview-netscape

%description -n netscape-plugin-%{name}
DjVu plugin for Netscape.

%description -n netscape-plugin-%{name} -l pl
Wtyczka DjVu do Netscape.

%prep -q
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{mozdir},%{nsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/netscape/plugins/nsdejavu.so \
	$RPM_BUILD_ROOT%{mozdir}
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
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/[!d]*
%{_mandir}/man1/d[!j]*
%{_mandir}/man1/djv[!i]*
%dir %{_datadir}/djvu
%{_datadir}/djvu/languages.xml
%dir %{_datadir}/djvu/osi
%lang(zh) %{_datadir}/djvu/osi/Chinese_PRC
%lang(de) %{_datadir}/djvu/osi/de_DE
%{_datadir}/djvu/osi/en
%lang(fr) %{_datadir}/djvu/osi/fr_FR
%lang(ja) %{_datadir}/djvu/osi/ja_JP

%files djview
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/djview
%{_mandir}/man1/djview.1*

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{mozdir}/*.so

%files -n netscape-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{nsdir}/*.so
