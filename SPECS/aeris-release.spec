Name:			aeris-release       
Version:		1.0 
Release:		10%{?dist}

Summary:		Aeris Network Packages repository configuration

Group:			System Environment/Base 
License:		Aeris Network Packages End User Agreement 
Vendor:			Aeris Network Packages
URL:			https://repo.aerisnetwork.com

Source0:		RPM-GPG-KEY-AERIS
Source1:		aeris.repo.el
Source2:		AERIS-PACKAGES-EUA
Source3:		RPM-GPG-KEY-AERIS-2022

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:		noarch
Provides:		aeris

%{?el6:Requires: epel-release = 6}
%{?el7:Requires: epel-release = 7}
%{?el8:Requires: epel-release = 8}
%{?el9:Requires: epel-release = 9}

%description
This package contains the Aeris Network Packages repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
%{__cp} %{SOURCE1} aeris.repo
%{__cp} -p %{SOURCE2} .

%{?el6:%{__sed} -i 's_@RELEASE@_6_' *.repo}
%{?el7:%{__sed} -i 's_@RELEASE@_7_' *.repo}
%{?el8:%{__sed} -i 's_@RELEASE@_8_' *.repo}
%{?el9:%{__sed} -i 's_@RELEASE@_9_' *.repo}

%{?el8:%{__sed} -i '/priority/c module_hotfixes=1' *.repo}
%{?el9:%{__sed} -i '/priority/d' *.repo}

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -Dpm644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-AERIS
%{__install} -Dpm644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-AERIS-2022

%{__install} -Dpm644 aeris.repo %{buildroot}/%{_sysconfdir}/yum.repos.d/aeris.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AERIS-PACKAGES-EUA
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-AERIS
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-AERIS-2022

%changelog
* Sun Dec 31 2023 Karl Johnson <karljohnson.it@gmail.com> - 1.0-10
- SHA512 pub key (2022) now for EL6 to EL9

* Fri Jul 15 2022 Karl Johnson <karljohnson.it@gmail.com> - 1.0-9
- Add EL9 support
- New SHA512 pub key for EL9 and up

* Fri Nov 12 2021 Karl Johnson <karljohnson.it@gmail.com> - 1.0-8
- Rename CentOS to EL
- Remove failovermethod for EL8

* Thu Mar 19 2020 Karl Johnson <karljohnson.it@gmail.com> - 1.0-7
- Require EPEL for all CentOS version

* Wed Jan 8 2020 Karl Johnson <karljohnson.it@gmail.com> - 1.0-6
- Add CentOS 8 support

* Tue Jan 15 2019 Karl Johnson <kjohnson@aerisnetwork.com> - 1.0-5
- Switch repo URL to HTTPS

* Mon May 16 2016 Karl Johnson <kjohnson@aerisnetwork.com> - 1.0-4
- EUA added

* Mon May 16 2016 Karl Johnson <kjohnson@aerisnetwork.com> - 1.0-3
- Testing repo added

* Wed Sep 24 2014 Karl Johnson <kjohnson@aerisnetwork.com> - 1.0-2
- CentOS 7 repo added

* Wed Aug 06 2014 Karl Johnson <kjohnson@aerisnetwork.com> - 1.0-1
- Initial package based on epel-release
