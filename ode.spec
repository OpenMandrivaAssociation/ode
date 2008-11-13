%define major 1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %name -d

Summary:	The Open Dynamics Engine
Name:		ode
Version:	0.10.1
Release:	%mkrel 1
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.ode.org
Source0:	http://downloads.sourceforge.net/opende/%{name}-%{version}.tar.lzma
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
%configure2_5x \
	--with-trimesh=opcode \
	--with-drawstuff=X11 \
	--enable-new-trimesh \
	--enable-demos \
	--enable-shared

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/ode-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libode.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc CHANGELOG.txt README.txt
%dir %{_includedir}/ode
%{_bindir}/%{name}-config
%multiarch %{multiarch_bindir}/%{name}-config
%{_includedir}/ode/*.h
%{_libdir}/libode.*a
%{_libdir}/libode.so
