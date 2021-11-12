# Aeris Enterprise Linux RPMs

[![ProjectStatus](https://img.shields.io/badge/status-active-brightgreen.svg)](#)
[![Build](https://img.shields.io/travis/com/karljohns0n/pkg-aeris-release/master.svg)](#)
[![Release 1.0-8](https://img.shields.io/badge/release-1.0--8-success.svg)](#)
[![Change Log](https://img.shields.io/badge/change-log-blue.svg?style=flat)](https://repo.aerisnetwork.com/stable/el/7/x86_64/repoview/aeris-release.html)

## Synopsis

Get started with Aeris Network packages by installing the repository, compatible with RHEL, CentOS, Rocky Linux, AlmaLinux.

El6 and EL7 packages are built using CentOS, EL8 are built using AlmaLinux.

```bash
EL6 > yum -y install https://repo.aerisnetwork.com/pub/aeris-release-6.rpm
EL7 > yum -y install https://repo.aerisnetwork.com/pub/aeris-release-7.rpm
EL8 > dnf -y install https://repo.aerisnetwork.com/pub/aeris-release-8.rpm
```

To install a package which is still in the testing repo:

```bash
> yum --enablerepo=aeris-testing install nginx-more
```

Browse [EL6](https://repo.aerisnetwork.com/stable/el/6/x86_64/repoview/), [EL7](https://repo.aerisnetwork.com/stable/el/7/x86_64/repoview/) and [EL8](https://repo.aerisnetwork.com/stable/el/8/x86_64/repoview/) repoview to find more information about available packages.
