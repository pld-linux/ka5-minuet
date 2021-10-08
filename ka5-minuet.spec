%define		kdeappsver	21.08.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		minuet
Summary:	minuet
Name:		ka5-%{kaname}
Version:	21.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4d037e3b88427e143c9c07a9f0cd8f68
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
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minuet is a free and open source software for music education. It aims
at supporting students and teachers in many aspects of music
education, such as ear training, first-sight reading, solfa, scales,
rhythm, harmony, and improvisation.

%description -l pl.UTF-8
Minuet jest wolnym i otwartoźródłowym oprogramowaniem do edukacji
muzycznej. Wspiera uczniów i nauczycieli w wielu aspektach nauki
muzyki, takich jak trening słuchu, czytania nut, solfeżu,
rytmu, harmonii i improwizacji.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications/Games
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/minuet
%attr(755,root,root) %{_libdir}/libminuetinterfaces.so.0.3.0
%dir %{_libdir}/qt5/plugins/minuet
%attr(755,root,root) %{_libdir}/qt5/plugins/minuet/minuetfluidsynthsoundcontroller.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
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
