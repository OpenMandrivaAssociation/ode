%define	name		ode
%define	version		0.7
%define	rel		1
%define	release		%mkrel %{rel}
%define	lib_name_orig	lib%{name}
%define lib_major	0
%define lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} %{lib_major} -d


Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Source0:	%{name}-src-%{version}.tar.bz2
Patch0:		ode-0.7-library-fixes.patch
License:	BSD LGPL
Group:		System/Libraries
URL:		http://opende.sourceforge.net/
Summary:	The Open Dynamics Engine
BuildRequires:	X11-devel MesaGLU-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. It is has been primarily written
by Russell Smith. ODE builds under a variety of different Windows
and Unix platforms. 

ODE is useful for simulating things like vehicles, objects in virtual
reality environments, and virtual creatures. 

%package -n	%{lib_name}
Summary:	Physics simulation library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with ODE.

%package -n	%{lib_name_devel}
Summary:	Headers and libraries to develop ODE applications
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{epoch}:%{version}

%description -n	%{lib_name_devel}
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. It is has been primarily written
by Russell Smith. ODE builds under a variety of different Windows
and Unix platforms.

ODE is useful for simulating things like vehicles, objects in virtual
reality environments, and virtual creatures.

%prep
%setup -q
%patch0 -p1 -b .library_fixes

%build
./autogen.sh
%configure	--enable-release \
		--enable-soname
%make

%install
rm -rf %{buildroot}

%makeinstall

%multiarch_binaries %{buildroot}%{_bindir}/ode-config
%multiarch_includes %{buildroot}%{_includedir}/ode/config.h

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root,0755)
%{_libdir}/%{lib_name_orig}.so.%{lib_major}*

%files -n %{lib_name_devel}
%defattr(-,root,root)
%doc CHANGELOG.txt LICENSE-BSD.TXT README.txt
%{_bindir}/%{name}-config
%multiarch %{multiarch_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.so


