#
# Conditional build:
%bcond_without	python		# any Python
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module
%bcond_without	static_libs	# static library

%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif
Summary:	Google's HTML5 parser library for C99
Summary(pl.UTF-8):	Biblioteka Google'a do analizy HTML5 dla C99
Name:		gumbo-parser
Version:	0.10.1
Release:	3
Epoch:		1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/google/gumbo-parser/releases
# TODO:		https://github.com/google/gumbo-parser/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/google/gumbo-parser/archive/v%{version}.tar.gz
# Source0-md5:	c6f75c9eda65e897c242f8958a34aed0
URL:		http://github.com/google/gumbo-parser
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented
as a C99 library. It is fully conformant with the HTML5 specification,
robust and resilient to bad input, supports source locations and
pointers back to the original text.

%description -l pl.UTF-8
Gumbo to implementacja algorytmu analizy HTML5 jako biblioteka C99.
Jest w pełni zgodna ze specyfikacją HTML5, potężna i odporna na błędne
wejście; obsługuje położenia źródłowe i wskaźniki powrotne do
pierwotnego tekstu.

%package devel
Summary:	Development files for Google's C99 HTML5 parser
Summary(pl.UTF-8):	Pliki programistyczne C99 analizatora HTML5 Google'a
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This subpackage contains the header files for developing applications
that want to make use of gumbo-parser.

%description devel -l pl.UTF-8
Ten podpakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących gumbo-parser.

%package static
Summary:	Static Gumbo parser library
Summary(pl.UTF-8):	Statyczna biblioteka analizatora Gumbo
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Gumbo parser library.

%description static -l pl.UTF-8
Statyczna biblioteka analizatora Gumbo.

%package -n python-gumbo
Summary:	Python 2 interface to Gumbo HTML5 parser
Summary(pl.UTF-8):	Interfejs Pythona 2 do analizatora HTML5 Gumbo
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n python-gumbo
Python 2 interface to Gumbo HTML5 parser.

%description -n python-gumbo -l pl.UTF-8
Interfejs Pythona 2 do analizatora HTML5 Gumbo.

%package -n python3-gumbo
Summary:	Python 3 interface to Gumbo HTML5 parser
Summary(pl.UTF-8):	Interfejs Pythona 3 do analizatora HTML5 Gumbo
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n python3-gumbo
Python 3 interface to Gumbo HTML5 parser.

%description -n python3-gumbo -l pl.UTF-8
Interfejs Pythona 3 do analizatora HTML5 Gumbo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgumbo.la

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgumbo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgumbo.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgumbo.so
%{_includedir}/gumbo.h
%{_includedir}/tag_enum.h
%{_pkgconfigdir}/gumbo.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgumbo.a
%endif

%if %{with python2}
%files -n python-gumbo
%defattr(644,root,root,755)
%{py_sitescriptdir}/gumbo-%{version}-py*.egg-info
%{py_sitescriptdir}/gumbo
%endif

%if %{with python3}
%files -n python3-gumbo
%defattr(644,root,root,755)
%{py3_sitescriptdir}/gumbo-%{version}-py*.egg-info
%{py3_sitescriptdir}/gumbo
%endif
