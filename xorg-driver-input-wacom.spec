Summary:	X.org Wacom input driver
Name:		xorg-driver-input-wacom
Version:	0.26.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/linuxwacom/xf86-input-wacom-%{version}.tar.bz2
# Source0-md5:	707b14021b87622042d4c1533a41b97f
URL:		http://sourceforge.net/apps/mediawiki/linuxwacom/index.php?title=Main_Page
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-proto >= 7.7-3
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org Wacom input driver.

%package devel
Group:          Development/Libraries
Summary:        Header file for wacom driver

%description devel
Header file for wacom driver

%prep
%setup -qn xf86-input-wacom-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xsetwacom
%attr(755,root,root) %{_libdir}/xorg/modules/input/wacom_drv.so
%{_datadir}/X11/xorg.conf.d/50-wacom.conf
%{_mandir}/man4/wacom.4*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isdv4-serial-debugger
%{_includedir}/xorg/Xwacom.h
%{_includedir}/xorg/wacom-properties.h
%{_includedir}/xorg/wacom-util.h
%{_includedir}/xorg/isdv4.h
%{_pkgconfigdir}/xorg-wacom.pc

