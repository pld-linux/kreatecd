Summary:	KreateCD - Frontend for CD writers using the K Desktop Environment
Summary(pl):	KreateCD - Frontend do nagrywarek CD do KDE
Name:		kreatecd
Version:	1.1.0
Release:	3
License:	GPL v2
Vendor:		Alexander Feigl <Alexander.Feigl@gmx.de>
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kreatecd/%{name}-%{version}.tar.bz2
# Source0-md5:	e79913878fc2818ee96ff77be0e7e138
URL:		http://www.kreatecd.de/
BuildRequires:	cdrtools-cdda2wav
BuildRequires:	cdparanoia-III
BuildRequires:	cdrtools
BuildRequires:	cdrtools-mkisofs
BuildRequires:	mpg123
BuildRequires:	kdelibs-devel >= 2.1
BuildRequires:	libvorbis-devel >= 1:1.0
Requires:	cdrtools-cdda2wav
Requires:	cdparanoia-III
Requires:	cdrtools
Requires:	cdrtools-mkisofs
Requires:	mpg123
Requires:	kdelibs >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KreateCD is a frontend for CD writers using the K Desktop Environment,
cdrecord cdparanoia and mkisofs.

%description -l pl
KreateCD jest frontend'em dla nagrywarek CD pod KDE, u¿ywaj±cym
cdrecord cdparanoia oraz mkisofs.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} %{!?debug:-fno-rtti -fno-exceptions}"

%configure2_13 \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW

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
