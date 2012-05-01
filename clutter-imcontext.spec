# Tarfile created using git
# git clone git://git.moblin.org/clutter-imcontext
# git archive --format=tar --prefix=%{name}-%{version}/ %{git_version} | bzip2 > ~/%{name}-%{version}-%{gitdate}.tar.bz2
%define git_version 9043ff1

%define major	0
%define api	0.1
%define libname		%mklibname %{name} %{api} %{major}
%define develname	%mklibname -d %{name} %{api}

Name:		clutter-imcontext
Version:	0.1.6
Release:	2
Summary:	IMContext Framework Library for Clutter
Group:		System/Libraries
License:	LGPLv2
URL:		http://maemo.org/packages/view/clutter-imcontext
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(clutter-x11-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)

%description
IMContext Framework Library for Clutter.

%package -n %{libname}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%mklibname  %{name} 0

%description -n %{libname}
Runtime library for %{name}.

%package -n %{develname}
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel
Obsoletes:	%mklibname  %{name} -d

%description -n %{develname}
Files for development with %{name}.

%prep
%setup -q

%build
# Don't run configure from autogen.sh
sed -i -e '/configure/d' autogen.sh
./autogen.sh

%configure2_5x \
	--disable-static

%make V=1

%install
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog
%dir %{_sysconfdir}/clutter-imcontext
%config %{_sysconfdir}/clutter-imcontext/enable_autoshow
%{_bindir}/clutter-scan-immodules

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}-%{api}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so

