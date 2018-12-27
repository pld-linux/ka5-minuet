%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		minuet
Summary:	minuet
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a6a4b037e75c1e601921c89f05ebb3d5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.11.1
BuildRequires:	fluidsynth-devel >= 1.1.6
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minuet is a free and open source software for music education. It aims
at supporting students and teachers in many aspects of music
education, such as ear training, first-sight reading, solfa, scales,
rhythm, harmony, and improvisation.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/minuet
%attr(755,root,root) %{_libdir}/libminuetinterfaces.so.0.3.0
%dir %{_libdir}/qt5/plugins/minuet
%attr(755,root,root) %{_libdir}/qt5/plugins/minuet/minuetfluidsynthsoundcontroller.so
%{_desktopdir}/org.kde.minuet.desktop
%{_iconsdir}/hicolor/128x128/apps/minuet.png
%{_iconsdir}/hicolor/128x128/apps/minuet.svg
%{_iconsdir}/hicolor/16x16/actions/minuet-chords.svg
%{_iconsdir}/hicolor/16x16/actions/minuet-intervals.svg
%{_iconsdir}/hicolor/16x16/actions/minuet-rhythms.svg
%{_iconsdir}/hicolor/16x16/actions/minuet-scales.svg
%{_iconsdir}/hicolor/16x16/apps/minuet.png
%{_iconsdir}/hicolor/16x16/apps/minuet.svg
%{_iconsdir}/hicolor/22x22/actions/minuet-chords.svg
%{_iconsdir}/hicolor/22x22/actions/minuet-intervals.svg
%{_iconsdir}/hicolor/22x22/actions/minuet-rhythms.svg
%{_iconsdir}/hicolor/22x22/actions/minuet-scales.svg
%{_iconsdir}/hicolor/22x22/apps/minuet.png
%{_iconsdir}/hicolor/22x22/apps/minuet.svg
%{_iconsdir}/hicolor/32x32/apps/minuet.png
%{_iconsdir}/hicolor/32x32/apps/minuet.svg
%{_iconsdir}/hicolor/48x48/apps/minuet.png
%{_iconsdir}/hicolor/48x48/apps/minuet.svg
%{_iconsdir}/hicolor/64x64/apps/minuet.png
%{_iconsdir}/hicolor/64x64/apps/minuet.svg
%{_iconsdir}/hicolor/scalable/apps/minuet.svgz
%{_datadir}/metainfo/org.kde.minuet.appdata.xml
%{_datadir}/minuet

%files devel
%defattr(644,root,root,755)
%{_includedir}/minuet
%{_libdir}/libminuetinterfaces.so
