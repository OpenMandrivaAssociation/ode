%define major 3
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %name -d

Summary:	The Open Dynamics Engine
Name:		ode
Version:	0.13
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ode.org
Source0:	http://downloads.sourceforge.net/opende/%{name}-%{version}.tar.bz2

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
Obsoletes:	%{mklibname %{name} 0} < 0.10.1

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with ODE.

%package -n	%{develname}
Summary:	Headers and libraries to develop ODE applications
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{mklibname %{name} 0 -d}
Obsoletes:	%{mklibname %{name} 0 -d} < 0.10.1
Requires:	%{libname} = %{epoch}:%{version}-%{release}

%description -n	%{develname}
The Open Dynamics Engine (ODE) is a free software library for the
simulation of Rigid Body Dynamics. It is has been primarily written
by Russell Smith. ODE builds under a variety of different Windows
and Unix platforms.

ODE is useful for simulating things like vehicles, objects in virtual
reality environments, and virtual creatures.

%prep
%setup -q

%build
%configure \
	--with-trimesh=opcode \
	--with-drawstuff=X11 \
	--enable-new-trimesh \
	--enable-demos \
	--enable-shared

%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/%{name}-config

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libode.so.%{major}*

%files -n %{develname}
%doc CHANGELOG.txt README.txt
%dir %{_includedir}/%{name}
%{_bindir}/%{name}-config
%{multiarch_bindir}/%{name}-config
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

