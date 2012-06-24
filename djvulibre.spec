Summary:	DjVu viewers, encoders and utilities.
Summary(pl):	DjVu - przegl�darki, dekodery oraz narz�dzia.
Name:		djvulibre
Version:	3.5.5
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	qt-devel >= 2.2.0
URL:		http://djvu.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_prefix		/usr/X11R6

%description

DjVu is a web-centric format and software platform for distributing
documents and images. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consume less client
resources than competing formats. DjVu was originally developped at
AT&T Labs-Research by Leon Bottou, Yann LeCun, Patrick Haffner, and
many others. In March 2000, AT&T sold DjVu to LizardTech Inc. who now
distributes Windows/Mac plug-ins, and commercial encoders (mostly on
Windows)

In an effort to promote DjVu as a Web standard, the LizardTech
management was enlightened enough to release the reference
implementation of DjVu under the GNU GPL in October 2000. DjVuLibre
(which means free DjVu), is an enhanced version of that code
maintained by the original inventors of DjVu. It is compatible with
version 3.5 of the LizardTech DjVu software suite.

DjVulibre-3.5 contains:
- a standalone DjVu viewer based on the Qt library.
- A browser plugin that works with most Unix browsers.
- A full-fledged wavelet-based compressor for pictures.
- A simple compressor for bitonal (black and white) scanned pages.
- A compressor for palettized images (a la GIF/PNG).
- A set of utilities to manipulate and assemble DjVu images and
  documents.
- A set of decoders to convert DjVu to a number of other formats.
- An up-to-date version of the C++ DjVu Reference Library.

%prep -q
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure
make depend
make

gzip -9nf README INSTALL NEWS TODO

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins

%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins && ln -sf ../../netscape/plugins/nsdejavu.so .

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}
%{_datadir}/djvu
%{_mandir}
