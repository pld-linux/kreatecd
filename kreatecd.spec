Summary:	KreateCD - Frontend for CD writers using the K Desktop Environment
Name:		kreatecd
Version:	0.2.2
Release:	1
Group:		X11/KDE/Apps
Copyright:	GPL
Vendor:		Alexander Feigl <Alexander.Feigl@gmx.de>
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}.patch
URL:		http://members.tripod.com/~lonely_dreamer/
BuildPrereq:	qt-devel
BuildPrereq:	kdelibs-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
KreateCD is a frontend for CD writers using the K Desktop Environment, cdrecord
cdparanoia andmkisofs.

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
make

%install
rm -rf $RPM_BUILD_ROOT
make install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}

%changelog                                               
* Sat Jul 10 1999
  []
- based on spec written by Troy Engel <tengel@sonic.net>.
