%define oname qtstyleplugins

Summary:	Additional style plugins for Qt5
Name:		qt5-style-plugins
Version:	5.0.0
Release:	8
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://github.com/qtproject/%{oname}
Source0:	http://download.qt.io/community_releases/additional_qt_src_pkgs/%{oname}-src-%{version}.tar.gz
Patch0:		qtstyleplugins-5.0.0-float.patch
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
Suggests:	qt5-style-cleanlooks
Suggests:	qt5-style-motif
Suggests:	qt5-style-plastique

%description
Additional style plugins for Qt5 moved out of Qt5 base tree.

%files

#----------------------------------------------------------------------------

%package -n qt5-style-cleanlooks
Summary:	Cleanlooks style for Qt5

%description -n qt5-style-cleanlooks
Cleanlooks style for Qt5.

%files -n qt5-style-cleanlooks
%{_qt5_plugindir}/styles/libqcleanlooksstyle.so

#----------------------------------------------------------------------------

%package -n qt5-style-motif
Summary:	Motif style for Qt5

%description -n qt5-style-motif
Motif style for Qt5.

%files -n qt5-style-motif
%{_qt5_plugindir}/styles/libqmotifstyle.so

#----------------------------------------------------------------------------

%package -n qt5-style-plastique
Summary:	Plastique style for Qt5

%description -n qt5-style-plastique
Plastique style for Qt5.

%files -n qt5-style-plastique
%{_qt5_plugindir}/styles/libqplastiquestyle.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-src-%{version}

%conf
%qmake_qt5 %{oname}.pro

%build
%make_build

%install
make install INSTALL_ROOT=%{buildroot}

rm -rf %{buildroot}%{_libdir}/cmake
