%define appname SMHI-osgQt
%define name SMHI-osgQt
%define version 3.5.6
%define release 1.3.1
%define vendor	smhi.se

Summary: Systemd unit file for %{appname}
Name: %{appname}
Version: %{version}
Release: %{release}
License: SMHI
Group: Utilities
URL: http://www.smhi.se/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
osgQt lib and executables %{appname}

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
cd $RPM_BUILD_ROOT/usr
tar xvzf $RPM_SOURCE_DIR/SMHI-osgQt.tar.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%files
%defattr(-,root,root,-)
/usr/bin/select_gpu.sh
/usr/bin/startViewer.sh
/usr/bin/osgQtWidget
/usr/bin/osgqfont
/usr/include/osgQt/Export
/usr/include/osgQt/GraphicsWindowQt
/usr/include/osgQt/QFontImplementation
/usr/include/osgQt/QGraphicsViewAdapter
/usr/include/osgQt/QWebViewImage
/usr/include/osgQt/QWidgetImage
/usr/include/osgQt/Version
/usr/lib64/libosgQt.so
/usr/lib64/libosgQt.so.146
/usr/lib64/libosgQt.so.3.5.6
/usr/lib64/osgdb_qfont.so
/usr/lib64/libcoserver.so
/usr/lib64/libcoserver.so.2
/usr/lib64/libcoserver.so.2.0.0
/usr/lib64/libmiLogger.so
/usr/lib64/libmiLogger.so.6
/usr/lib64/libmiLogger.so.6.0.0
/usr/lib64/libqUtilities.so
/usr/lib64/libqUtilities.so.7
/usr/lib64/libqUtilities.so.7.0.0
/usr/lib64/pkgconfig/openscenegraph-osgQt.pc


%changelog
* Mon Dec 19 2016 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Initial build.
- Step, sequence, drag and drop and help.
* Tue Feb 28 2016 Yngve Einarsson <Yngve.Einarsson@smhi.se>
- Automatic updates implemented, using the metlibs coserver library.
