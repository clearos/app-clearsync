
Name: app-clearsync
Epoch: 1
Version: 1.0.9
Release: 1%{dist}
Summary: Synchronization and Events - APIs and install
License: LGPLv3
Group: ClearOS/Libraries
Source: app-clearsync-%{version}.tar.gz
Buildarch: noarch

%description
The Synchronization and Events engine provides hooks into to operating system for creating system events and synchronizing files across multiple systems.

%package core
Summary: Synchronization and Events - APIs and install
Requires: app-base-core
Requires: clearsync

%description core
The Synchronization and Events engine provides hooks into to operating system for creating system events and synchronizing files across multiple systems.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/clearsync
cp -r * %{buildroot}/usr/clearos/apps/clearsync/

install -D -m 0644 packaging/clearsyncd.php %{buildroot}/var/clearos/base/daemon/clearsyncd.php

%post core
logger -p local6.notice -t installer 'app-clearsync-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/clearsync/deploy/install ] && /usr/clearos/apps/clearsync/deploy/install
fi

[ -x /usr/clearos/apps/clearsync/deploy/upgrade ] && /usr/clearos/apps/clearsync/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-clearsync-core - uninstalling'
    [ -x /usr/clearos/apps/clearsync/deploy/uninstall ] && /usr/clearos/apps/clearsync/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/clearsync/packaging
%exclude /usr/clearos/apps/clearsync/tests
%dir /usr/clearos/apps/clearsync
/usr/clearos/apps/clearsync/deploy
/usr/clearos/apps/clearsync/language
/usr/clearos/apps/clearsync/libraries
/var/clearos/base/daemon/clearsyncd.php
