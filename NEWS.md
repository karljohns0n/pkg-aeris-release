# NEWS

## 2024-01-02

### Important: Transition to a new GPG key

Effective January 2, 2024, Aeris Network is enhancing security by signing all packages with a [new GPG key](https://repo.aerisnetwork.com/pub/RPM-GPG-KEY-AERIS) that utilizes SHA2 digest algorithms, replacing the older SHA1. This update applies to all future and existing packages across all linux enterprise distributions.

The full fingerprint of the key is: `0821 3E13 DC42 AF06 DA60  FBBD 3546 F874 9B4E F1C1`

To facilitate a smooth transition, we've provided two straightforward methods for importing the new key: either directly through a rpm command or by using our Ansible playbook. Please update promptly to ensure continued packages updates from our repository.

```bash
rpm --import https://repo.aerisnetwork.com/pub/RPM-GPG-KEY-AERIS
```

```yaml
- name: Ensure latest Aeris RPM GPG key is installed
  hosts: all
  tasks:

    - name: Fetch latest Aeris RPM GPG key
      become: true
      ansible.builtin.rpm_key:
        state: present
        key: "https://repo.aerisnetwork.com/pub/RPM-GPG-KEY-AERIS"
        fingerprint: 0821 3E13 DC42 AF06 DA60  FBBD 3546 F874 9B4E F1C1
      when:
        - ansible_distribution in [ "CentOS", "EL", "Rocky", "AlmaLinux" ]

    - name: Update gpgkey configuration for Aeris repository
      become: true
      community.general.ini_file:
        path: /etc/yum.repos.d/aeris.repo
        section: "{{ item }}"
        option: gpgkey
        value: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-AERIS
        mode: '0644'
        owner: root
        group: root
        backup: false
        ignore_spaces: true
        no_extra_spaces: true
      loop:
        - aeris
        - aeris-testing
      when:
        - ansible_distribution in [ "CentOS", "EL", "Rocky", "AlmaLinux" ]
```
