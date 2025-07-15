Summary:	Window Manager Icons - themable icon distribution
Summary(pl.UTF-8):	Window Manager Icons - konfigurowalny zbiór ikon
Name:		wm-icons
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/wm-icons/%{name}-%{version}.tar.bz2
# Source0-md5:	5fc5a23dcc048b8bc3e5baf6923fa9c3
Patch0:		%{name}-ac_am_fixes.patch
URL:		http://wm-icons.sourceforge.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Window Manager Icons is an efficient icon distribution designed to
be standardized and configurable. Includes several themed icon sets,
scripts and configurations for several window managers.

%description -l pl.UTF-8
Window Manager Icons to wydajna dystrybucja ikon zaprojektowana do
standaryzacji i konfigurowania. Posiada parę tematycznych zestawów
ikon, skrypty i konfigurację dla kilku menadżerów okien.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-all-sets
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc doc/FAQ doc/README.3dpixmaps doc/README.martys doc/README.penguins
%doc doc/icons.lst doc/wm-icons.lsm
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_iconsdir}/%{name}
