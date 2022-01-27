#
# spec file for cardano-release.spec
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2022 PERLUR Group
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the AGPL License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/CardanoOS/CardanoOS
#

Name:           cardano-release
Version:        1
Release:        1
Summary:        Extra Packages for openSUSE repository configuration
Group:          System Environment/Base
License:        AGPL
	
URL:            https://github.com/CardanoOS/
Source0:        http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
Source1:        AGPL-3.0-only
Source2:        cardano-leap.repo
Source3:        cardano-tumbleweed.repo
Source4:        cardano-microos.repo
Source5:        cardano-kubic.repo
Source6:        cardano-factory.repo
BuildArch:      noarch
Requires:       redhat-release >=  %{version}
Conflicts:      fedora-release
%description
	
This package contains the Extra Packages for openSUSE distributions GPG key as well as configuration for zypper.
	
%prep

%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build
	
%install
rm -rf $RPM_BUILD_ROOT

#GPG Key	
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
	
 
	
# yum
	
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
	
install -pm 644 %{SOURCE2} %{SOURCE3}  \
	
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
	
install -pm 644 -D %{SOURCE4} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/90-epel.preset
	
 
	
%clean
	
rm -rf $RPM_BUILD_ROOT
	
 
	
%files
	
%defattr(-,root,root,-)
	
%doc GPL
	
%config(noreplace) /etc/yum.repos.d/*
	
/etc/pki/rpm-gpg/*
	
%{_prefix}/lib/systemd/system-preset/90-epel.preset
	
 
	
%changelog
