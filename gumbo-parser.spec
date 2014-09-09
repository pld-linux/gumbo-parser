Summary:	Google's HTML5 parser library for C99
Name:		gumbo-parser
Version:	0.1
Release:	0.20140908
License:	Apache v2.0
Group:		Development/Libraries
# use this url as next snapshot url: https://github.com/google/gumbo-parser/archive/master/%{name}-%{version}-%{release}.tar.gz
Source0:	https://codeload.github.com/google/gumbo-parser/zip/master
# Source0-md5:	7c6af930a4132ff5bf3e0f07bdae529c
URL:		http://github.com/google/gumbo-parser
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a C99 library. It is fully conformant with the HTML5 specification,
robust and resilient to bad input, supports source locations and
pointers back to the original text.

%package devel
Summary:	Development files for Google's C99 HTML5 parser
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a C99 library. It is fully conformant with the HTML5 specification,
robust and resilient to bad input, supports source locations and
pointers back to the original text.

This subpackage contains libraries and header files for developing
applications that want to make use of gumbo-parser.

%prep
%setup -qc
mv %{name}-master/* .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgumbo.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgumbo.so.*.*.*
%ghost %{_libdir}/libgumbo.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/gumbo.h
%attr(755,root,root) %{_libdir}/libgumbo.so
%{_pkgconfigdir}/gumbo.pc
