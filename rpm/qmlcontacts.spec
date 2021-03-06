# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       qmlcontacts

# >> macros
# << macros

Summary:    Contacts application for nemo
Version:    0.4.2
Release:    1
Group:      Applications/System
License:    GPLv2
URL:        https://github.com/nemomobile/qmlcontacts
Source0:    %{name}-%{version}.tar.bz2
Source100:  qmlcontacts.yaml
Requires:   qt-components >= 1.4.8
Requires:   mapplauncherd-booster-qtcomponents
Requires:   nemo-qml-plugin-thumbnailer
Requires:   nemo-qml-plugin-contacts
Requires:   nemo-qml-plugin-folderlistmodel
Requires:   qmlgallery
Requires:   qmlfilemuncher
Requires:   contactsd
Requires:   nemo-qml-plugin-dbus
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtContacts)
BuildRequires:  pkgconfig(qdeclarative-boostable)
BuildRequires:  desktop-file-utils
Provides:   meego-handset-people > 0.2.32
Provides:   meego-handset-people-branding-upstream > 0.2.32
Obsoletes:   meego-handset-people <= 0.2.32
Obsoletes:   meego-handset-people-branding-upstream <= 0.2.32

%description
Contacts application using Qt Quick for Nemo Mobile.

%package tools
Summary:    Development tools for qmlcontacts
License:    BSD
Group:      Applications/System

%description tools
Tools to help development of contacts application/framework/etc.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/qmlcontacts
%{_datadir}/applications/qmlcontacts.desktop
%{_libdir}/qt4/imports/org/nemomobile/qmlcontacts/*
# >> files
# << files

%files tools
%defattr(-,root,root,-)
%{_bindir}/vcardconverter
# >> files tools
# << files tools
