Summary:	KreateCD - Frontend for CD writers using the K Desktop Environment
Summary(pl):	KreateCD - Frontend do nagrywarek CD do KDE
Name:		kreatecd
Version:	1.0.0
Release:	1
License:	GPL
Vendor:		Alexander Feigl <Alexander.Feigl@gmx.de>
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://download.sourceforge.net/pub/sourceforge/kreatecd/%{name}-%{version}.tar.bz2
URL:		http://www.kreatecd.de/
BuildRequires:	cdrecord
BuildRequires:	kdelibs-devel >= 2.1
Requires:	kdelibs >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
KreateCD is a frontend for CD writers using the K Desktop Environment,
cdrecord cdparanoia and mkisofs.

%description -l pl
KreateCD jest frontend'em dla nagrywarek CD pod KDE, używającym
cdrecord cdparanoia oraz mkisofs.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} %{!?debug:-fno-rtti -fno-exceptions}"
%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/CD-RW

%{__make} install \
	transform="" \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_applnkdir}/Utilities/CD-RW

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreatecd
%{_applnkdir}/Utilities/CD-RW/kreatecd.desktop
%{_datadir}/apps/kreatecd
%{_datadir}/mimelnk/application/x-kreatecd.desktop
%{_pixmapsdir}/*/*/apps/kreatecd.png
