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
# case the license is the MIT License). An "Open Source License" is a
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
# This is a EPEL maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
	
URL:            https://github.com/CardanoOS/
Source0:        http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
Source1:        GPL
Source2:        epel.repo
Source3:        epel-testing.repo
# EPEL default preset policy (borrowed from fedora's 90-default.preset)
Source4:        90-epel.preset
BuildArch:     noarch
Requires:      redhat-release >=  %{version}
Conflicts:     fedora-release
%description
	
This package contains the Extra Packages for openSUSE Leap repository
	
GPG key as well as configuration for zypper.
	
 
	
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
