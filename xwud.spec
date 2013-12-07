Name:		xwud
Version:	1.0.4
Release:	6
Summary:	Image displayer for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xwud is an X Window System image undumping utility. Xwud allows X
users to display in a window an image saved in a specially formatted
dump file, such as produced by xwd.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xwud
%{_mandir}/man1/xwud.*




%changelog

* Fri Jun 08 2012 tv <tv> 1.0.4-1.mga3
+ Revision: 257345
- new release

* Sun Jan 23 2011 pterjan <pterjan> 1.0.3-1.mga1
+ Revision: 35159
- imported package xwud

