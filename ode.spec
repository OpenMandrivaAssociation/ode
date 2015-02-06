%define major 1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname %name -d

Summary:	The Open Dynamics Engine
Name:		ode
Version:	0.11.1
Release:	4
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
%configure2_5x \
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
%{_libdir}/lib%{name}.*a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc



%changelog
* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 1:0.11.1-2mdv2011.0
+ Revision: 633700
- drop old BRs

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sun Jul 26 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.11.1-1mdv2010.0
+ Revision: 400426
- New version 0.11.1

* Wed Feb 11 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.11-1mdv2009.1
+ Revision: 339595
- New version 0.11

* Thu Nov 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.10.1-1mdv2009.1
+ Revision: 302893
- new license policy
- obsolete old libraries
- fix file list
- new version 0.10.1
- drop patch 0, fixed by upstream
- adjust configure options
- fix file list

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1:0.9-3mdv2009.0
+ Revision: 254390
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.9-1mdv2008.1
+ Revision: 101396
- new version
- do not change compression format of source file
- fix url

* Thu Aug 23 2007 Funda Wang <fwang@mandriva.org> 1:0.8-2mdv2008.0
+ Revision: 70686
- New devel policy
- fix so link

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8-1mdv2008.0
+ Revision: 30222
- new version
- rediff P0
- spec file clean


* Sun Jan 21 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7-1mdv2007.0
+ Revision: 111579
- new release: 0.7 (closes #28339)
  fix passing of compile flags, lib64 fixes, -fPIC (P0)
- Import ode

* Sun Jul 30 2006 Guillaume Bedot <littletux@mandriva.org> 1:0.6-4mdv2007.0
- rebuilt without double-precision (maniadrive needs single)

* Wed Jul 19 2006 Guillaume Bedot <littletux@mandriva.org> 1:0.6-3mdv2007.0
- fix soname (wrongly dropped patch)

* Fri Jul 14 2006 Guillaume Bedot <littletux@mandriva.org> 1:0.6-2mdv2007.0
- fix symbolic links
- multiarch

* Thu Jul 13 2006 Guillaume Bedot <littletux@mandriva.org> 1:0.6-1mdv2007.0
- 0.6
- dropped patch
- install changes

* Sun Nov 27 2005 Oden Eriksson <oeriksson@mandriva.com> 1:0.5-7mdk
- added P0 from debain to disable OPCODE (and make the shared lib)
- added a lib64 fix

* Fri May 20 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.5-6mdk
- compile with -fPIC

* Fri May 20 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.5-5mdk
- from Jan Ciger: <jan.ciger@gmail.com> :
	o turn off the -whole-archive flag for the linker

* Fri Apr 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5-4mdk
- arg, forgot to add epoch to requires

* Thu Apr 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5-3mdk
- fix devel links
- fix devel requires
- do ldconfig

* Thu Apr 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5-2mdk
- %%mkrel
- from Jan Ciger <jan.ciger@gmail.com> :
	o 0.5 changed to build a dynamic lib a split the package

* Mon Nov 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5-1mdk
- 0.5 (add epoch as rpm takes 0.5 for less than 0.039)

