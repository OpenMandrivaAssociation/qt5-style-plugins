%define snapshot 20130213
%define oname qtstyleplugins

Summary:	Additional style plugins for Qt5
Name:		qt5-style-plugins
Version:	0
Release:	0.%{snapshot}.2
License:	LGPLv2.1+
Group:		System/Libraries
URL:		https://github.com/qtproject/%{oname}
Source0:	%{oname}-%{snapshot}.tar.bz2
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
%setup -q -n %{oname}-%{snapshot}

%build
%qmake_qt5 %{oname}.pro
%make

%install
make install INSTALL_ROOT=%{buildroot}

