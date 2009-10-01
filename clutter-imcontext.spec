%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Name: clutter-imcontext
Summary: Port of GTK IMContext to Clutter
Group: Graphics
Version: 0.1.4
License: LGPLv2+
URL: http://www.clutter-project.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: clutter-devel >= 1.0
BuildRequires: gobject-introspection-devel
BuildRequires: gir-repository

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

%description -n %{develname}
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh --enable-gtk-doc
%configure2_5x
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
%{_libdir}/libclutter-imcontext-0.1.la
%{_libdir}/libclutter-imcontext-0.1.so
