Summary:	KreateCD - Frontend for CD writers using the K Desktop Environment
Summary(pl):	KreateCD - Frontend do nagrywarek CD do KDE
Name:		kreatecd
Version:	0.2.2
Release:	1
Group:		X11/KDE/Applications
Copyright:	GPL
Vendor:		Alexander Feigl <Alexander.Feigl@gmx.de>
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}.patch
URL:		http://members.tripod.com/~lonely_dreamer/
BuildRequires:	qt-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KreateCD is a frontend for CD writers using the K Desktop Environment, cdrecord
cdparanoia and mkisofs.

%description -l pl
KreateCD jest frontend'em dla nagrywarek CD pod KDE, u¿ywaj±cym  cdrecord
cdparanoia oraz mkisofs.

%prep
%setup -q
%patch -p1

%build
mv %{builddir}/doc/default %{builddir}/doc/de
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
        --prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
