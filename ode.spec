%define major 0
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %name

Summary:	The Open Dynamics Engine
Name:		ode
Version:	0.8
Release:	%mkrel 2
Epoch:		1
License:	BSD LGPL
Group:		System/Libraries
URL:		http://ode.org
Source0:	http://downloads.sourceforge.net/opende/%{name}-src-%{version}.tar.bz2
Patch0:		ode-0.8-library-fixes.patch
BuildRequires:	X11-devel
BuildRequires:	libmesaglu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. It is has been primarily written
by Russell Smith. ODE builds under a variety of different Windows
and Unix platforms. 

ODE is useful for simulating things like vehicles, objects in virtual
reality environments, and virtual creatures. 

%package -n	%{libname}
Summary:	Physics simulation library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with ODE.

%package -n	%{develname}
Summary:	Headers and libraries to develop ODE applications
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%libname-devel
Requires:	%{libname} = %{epoch}:%{version}

%description -n	%{develname}
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. It is has been primarily written
by Russell Smith. ODE builds under a variety of different Windows
and Unix platforms.

ODE is useful for simulating things like vehicles, objects in virtual
reality environments, and virtual creatures.

%prep
%setup -q
%patch0 -p0 -b .library_fixes

%build
./autogen.sh
%configure2_5x \
	--enable-soname \
	--enable-release \
	--with-trimesh=opcode

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/ode-config
%multiarch_includes %{buildroot}%{_includedir}/ode/config.h

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libode.so.%{major}*

%files -n %{develname}
%defattr(644,root,root,755)
%doc CHANGELOG.txt LICENSE-BSD.TXT README.txt
%dir %{_includedir}/ode
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %multiarch %{multiarch_bindir}/%{name}-config
%multiarch %{multiarch_includedir}/ode/config.h
%{_includedir}/ode/*.h
%{_libdir}/libode.a
%{_libdir}/libode.so
