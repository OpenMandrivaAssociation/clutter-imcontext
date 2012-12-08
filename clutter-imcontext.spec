%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Name: clutter-imcontext
Summary: Port of GTK IMContext to Clutter
Group: Graphics
Version: 0.1.4
License: LGPLv2+
URL: http://www.clutter-project.org
Release: %mkrel 3
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: clutter-devel >= 1.0
BuildRequires: gobject-introspection-devel
BuildRequires: gir-repository
BuildRequires: pkgconfig(gl)

%description
Description: %{summary}

%package -n %{libname}
Summary: Port of GTK IMContext to Clutter
Group: System/Libraries

%description -n %{libname}
Description: %{summary}

%package -n %{develname}
Summary: Port of GTK IMContext to Clutter
Group: Development/C
Requires: %{name} >= %{version}
Provides: %{name}-devel

%description -n %{develname}
Description: %{summary}

%prep
%setup -q
perl -pi -e 's,^./configure.*,,' ./autogen.sh

%build
./autogen.sh
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
  if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
    mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
  fi
done

%clean
rm -rf  $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libclutter-imcontext*so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/%{name}-0.1/%{name}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libclutter-imcontext-0.1.a
%{_libdir}/libclutter-imcontext-0.1.so
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-3mdv2011.0
+ Revision: 617070
- the mass rebuild of 2010.0 packages

* Thu Oct 01 2009 Olivier Blin <oblin@mandriva.com> 0.1.4-2mdv2010.0
+ Revision: 452373
- provide clutter-imcontext-devel

* Thu Oct 01 2009 Olivier Blin <oblin@mandriva.com> 0.1.4-1mdv2010.0
+ Revision: 452285
- package gtk doc
- do not run configure twice (and fix passing gtk-doc option)
- move binary and doc outside of lib package
- initial import (from Claudio Matsuoka and Caio Begotti, based on Fedora package)
- Created package structure for clutter-imcontext.

