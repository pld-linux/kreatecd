Summary:	KreateCD - Frontend for CD writers using the K Desktop Environment
Summary(pl):	KreateCD - Frontend do nagrywarek CD do KDE
Name:		kreatecd
Version:	1.0.0
Release:	1
Group:		X11/KDE/Applications
Copyright:	GPL
Vendor:		Alexander Feigl <Alexander.Feigl@gmx.de>
Source:		%{name}-%{version}.tar.bz2
URL:		http://members.tripod.com/~lonely_dreamer/
BuildRequires:	qt-devel >= 2.2
BuildRequires:	kdelibs-devel >= 2.1
Requires:	kdelibs >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
KreateCD is a frontend for CD writers using the K Desktop Environment, cdrecord
cdparanoia and mkisofs.

%description -l pl
KreateCD jest frontend'em dla nagrywarek CD pod KDE, używającym  cdrecord
cdparanoia oraz mkisofs.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} transform="" DESTDIR="$RPM_BUILD_ROOT" install

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/CD-RW
mv $RPM_BUILD_ROOT/%{_applnkdir}/Applications/kreatecd.desktop \
    $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/CD-RW/kreatecd.desktop

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
