Name:		xwud
Version:	1.0.6
Release:	1
Summary:	Image displayer for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
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
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

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

