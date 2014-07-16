Summary:	Google's HTML5 parser library for C99
Name:		gumbo-parser
Version:	0.1
Release:	0.20140716
License:	Apache-2.0
Group:		Development/Libraries
URL:		http://github.com/google/gumbo-parser
#Snapshot:	d90ea2b2d01b27a7adf0501f644a7782e50362fe
Source0:	https://codeload.github.com/google/gumbo-parser/zip/master
# Source0-md5:	5c9eea65641b9df3bc57301b6ed74808
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
%setup -qn %{name}-master

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgumbo.so.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gumbo.h
%attr(755,root,root) %{_libdir}/libgumbo.so
%{_pkgconfigdir}/gumbo.pc
