# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-calcit

# >> macros
# << macros

Summary:    Calcit Math Game
Version:    0.1.1
Release:    1
Group:      Qt/Qt
License:    GPLv3
BuildArch:  noarch
URL:        http://github.com/poetaster/calcit
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   libsailfishapp-launcher
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.3
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
A math game resembling wordle.

%if "%{?vendor}" == "chum"
PackageName: harbour-calcit
Type: desktop-application
Categories:
 - Game
DeveloperName: Mark Washeim (poetaster)
Custom:
 - Repo: https://github.com/poetaster/calcit
Icon: https://github.com/poetaster/calcit/raw/main/icons/108x108/harbour-calcit.png
Screenshots:
 - https://raw.githubusercontent.com/poetaster/calcit/main/screenshot-2.png
 - https://raw.githubusercontent.com/poetaster/calcit/main/screenshot-3.png
%endif

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%defattr(0644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
