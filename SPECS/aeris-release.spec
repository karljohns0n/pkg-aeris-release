Name:			aeris-release       
Version:		1.0 
Release:		6%{?dist}

Summary:		Aeris Network Packages repository configuration

Group:			System Environment/Base 
License:		Aeris Network Packages End User Agreement 
Vendor:			Aeris Network Packages
URL:			https://repo.aerisnetwork.com

Source0:		RPM-GPG-KEY-AERIS
Source1:		aeris.repo.centos
Source2:		AERIS-PACKAGES-EUA

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:		noarch
Provides:		aeris

%description
This package contains the Aeris Network Packages repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
%{__cp} -p %{SOURCE0} .
%{__cp} %{SOURCE1} aeris.repo
%{__cp} -p %{SOURCE2} .

%{?el6:%{__sed} -i 's_@RELEASE@_6_' *.repo}
%{?el7:%{__sed} -i 's_@RELEASE@_7_' *.repo}
%{?el8:%{__sed} -i 's_@RELEASE@_8_' *.repo}
%{?el8:%{__sed} -i '/priority/a module_hotfixes=1' *.repo}

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -Dpm644 RPM-GPG-KEY-AERIS %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-AERIS
%{__install} -Dpm644 aeris.repo %{buildroot}/%{_sysconfdir}/yum.repos.d/aeris.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AERIS-PACKAGES-EUA
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-AERIS


%changelog
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
