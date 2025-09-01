# Aeris Enterprise Linux RPMs

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](#)
[![Release](https://img.shields.io/badge/release-1.0--11-success.svg)](#)

## Synopsis

Get started with Aeris Network packages by installing the repository, compatible with RHEL, CentOS, Rocky Linux, AlmaLinux.

El6 and EL7 packages are built using CentOS while EL8, EL9 and EL10 are built using Rocky Linux.

```bash
EL6 > yum -y install https://repo.aerisnetwork.com/pub/aeris-release-6.rpm
EL7 > yum -y install https://repo.aerisnetwork.com/pub/aeris-release-7.rpm
EL8 > dnf -y install https://repo.aerisnetwork.com/pub/aeris-release-8.rpm
EL9 > dnf -y install https://repo.aerisnetwork.com/pub/aeris-release-9.rpm
EL10 > dnf -y install https://repo.aerisnetwork.com/pub/aeris-release-10.rpm
```

To install a package which is still in the testing repo:

```bash
> yum --enablerepo=aeris-testing install nginx-more
```

Browse [Aeris Network Repository](https://repo.aerisnetwork.com/) to find more information about available packages.
