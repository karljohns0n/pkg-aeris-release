[aeris]
name=Aeris Packages for Enterprise Linux @RELEASE@ - stable - $basearch
baseurl=https://repo.aerisnetwork.com/stable/el/@RELEASE@/$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-AERIS

[aeris-testing]
name=Aeris Packages for Enterprise Linux @RELEASE@ - testing - $basearch
baseurl=https://repo.aerisnetwork.com/testing/el/@RELEASE@/$basearch
failovermethod=priority
enabled=0
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-AERIS
