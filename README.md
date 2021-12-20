waco_master
===========

![test](https://github.com/waco-org/waco-master/actions/workflows/test.yml/badge.svg)

An Ansible role that orchestrates the installation of several developer oriented tools by driving
other roles. Currently only Red Hat open distributions are supported, i.e. CentOS 8, CentOS 7 and
Fedora 35. Neither RHEL 8 and 7 nor other derivatives were tested, but they should work without
problems. Centos Stream variants are not supported.

The currently supported tools and applications are:

- Docker Community Edition
- Python, from either source or system packages, and within virtualenv's:

    + Ansible
    + Mercurial
    + Sphinx

- Flatpak and flatpak applications, both system and user level
- Grsync
- Apache Maven
- Hashicorp Packer
- Hashicorp Vagrant
- Oracle VirtualBox
- Visual Studio Code
- Rust, per user

Requirements
------------

None.

Role Variables
--------------

There are many variables that control the operation of this role, they are documented in the
[defaults/main.yml](https:defaults/main.yml) file.

Dependencies
------------

The `nmusatti.docker_ce` role is used to install Docker Community Edition.

The `nmusatti.source_python` role is used to install Python from source.

The `nmusatti.waco_python` is used to customize Python installations. Note that the
`waco_python` role is not currently available from Ansible Galaxy and must be downloaded from its
[GitHub repository](https://github.com/waco-org/waco-python.git).

The `geerlingguy.repo-epel` role is used to enable the EPEL repository on CentOS.

The `bobbyrenwick.pip` role is used to install pip.

Example Playbook
----------------

Consider using the [waco-bootstrap](https://github.com/waco-org/waco-bootstrap.git) project to apply
the `waco-master` role to newly installed computers. Otherwise you can invoke it directly, in
which case you might want to copy and customize the `defaults/main.yml` file, and pass it as a
variable file:

    - hosts: servers
      roles:
         - role: nmusatti.waco_master
           vars_file: my_defaults.yml

> Note: Currently I cannot upload this role to Ansible Galaxy, so you need to download it from
> GitHub.

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - <https://github.com/nmusatti>

WACO - Workstation as Code - <https://github.com/waco-org>
