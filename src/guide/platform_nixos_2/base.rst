.. _nixos2-base:

Base environment
================

The base installation includes various tools that generally help with
application deployment. They are available on every Flying Circus NixOS VM.
The package's installation includes availability to run them manually and
to compile your own software against them.

However, those are intended for short-term convenience. Linking against them
may cause breakage of your applications in the long term.

Also, those packages are not providing running daemons (like OpenLDAP). If you
need a managed component, those need to be activated explicitly.

Packages
--------

* atop
* bc
* bind
* bundler
* curl
* cyrus_sasl
* db
* dstat
* fcmaintenance
* fio
* gcc
* gdbm
* git
* gnupg
* go
* gptfdisk
* graphviz
* imagemagick
* inetutils
* iotop
* kerberos
* libmemcached
* links
* lsof
* lynx
* mercurial
* mmv
* nano
* nc6
* ncdu
* netcat
* ngrep
* nmap
* nodejs
* openldap
* openssl
* php
* postgresql
* protobuf
* psmisc
* pv
* python27Full
* python3
* python34Packages.virtualenv
* screen
* strace
* subversion
* sysstat
* tcpdump
* telnet
* traceroute
* tree
* unzip
* utillinux
* vim
* zlib


Configuration
-------------

All tools can be configured individually with dotfiles in the user's home
directory.


Interaction
-----------

Service users may invoke :command:`sudo systemctl` to restart individual
services manually. See also :ref:`nixos2-local` for information about how to activate configuration changes.


.. vim: set spell spelllang=en:
