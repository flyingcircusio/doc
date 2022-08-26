(customerproject)=

# Base environment

The base installation includes a collection of little tools that generally help
with application deployment. They will be available on every Flying Circus
Gentoo VM.

## Packages

- [app-admin/eselect](http://packages.gentoo.org/package/app-admin/eselect) (Gentoo's multi-purpose configuration and management tool)
- [app-admin/eselect-postgresql](http://packages.gentoo.org/package/app-admin/eselect-postgresql) (Utility to select the default PostgreSQL slot)
- [app-admin/goceptnet](http://packages.gentoo.org/package/app-admin/goceptnet) (Python utilities to manage the FC infrastructure (localconfig etc.))
- [app-admin/logrotate](http://packages.gentoo.org/package/app-admin/logrotate) (Rotates, compresses, and mails system logs)
- [app-admin/rsyslog](http://packages.gentoo.org/package/app-admin/rsyslog) (An enhanced multi-threaded syslogd with database support and more)
- [app-admin/sudo](http://packages.gentoo.org/package/app-admin/sudo) (Allows users or groups to run commands as other users)
- [app-admin/sysstat](http://packages.gentoo.org/package/app-admin/sysstat) (System performance tools for Linux)
- [app-admin/tmpwatch](http://packages.gentoo.org/package/app-admin/tmpwatch) (Files which haven't been accessed in a given period of time are removed from specified directories)
- [app-admin/webapp-config](http://packages.gentoo.org/package/app-admin/webapp-config) (Gentoo's installer for web-based applications)

* [app-arch/unzip](http://packages.gentoo.org/package/app-arch/unzip) (unzipper for pkzip-compressed files)
* [app-arch/xz-utils](http://packages.gentoo.org/package/app-arch/xz-utils) (utils for managing LZMA compressed files)

- [app-crypt/aespipe](http://packages.gentoo.org/package/app-crypt/aespipe) (Encrypts data from stdin to stdout)
- [app-crypt/gnupg](http://packages.gentoo.org/package/app-crypt/gnupg) (The GNU Privacy Guard, a GPL pgp replacement)

* [app-editors/nano](http://packages.gentoo.org/package/app-editors/nano) (GNU GPL'd Pico clone with more functionality)
* [app-editors/vim](http://packages.gentoo.org/package/app-editors/vim) (Vim, an improved vi-style text editor)

- [app-misc/ca-certificates](http://packages.gentoo.org/package/app-misc/ca-certificates) (Common CA Certificates PEM files)
- [app-misc/mmv](http://packages.gentoo.org/package/app-misc/mmv) (Move/copy/append/link multiple files according to a set of wildcard patterns)
- [app-misc/screen](http://packages.gentoo.org/package/app-misc/screen) (Full-screen window manager that multiplexes physical terminals between several processes)
- [app-misc/symlinks](http://packages.gentoo.org/package/app-misc/symlinks) (Scans for and fixes broken or messy symlinks)

* [app-portage/portage-utils](http://packages.gentoo.org/package/app-portage/portage-utils) (small and fast portage helper tools written in C)

- [app-shells/bash-completion](http://packages.gentoo.org/package/app-shells/bash-completion) (Programmable Completion for bash)
- [app-shells/bash](http://packages.gentoo.org/package/app-shells/bash) (The standard GNU Bourne again shell)
- [app-shells/zsh](http://packages.gentoo.org/package/app-shells/zsh) (UNIX Shell similar to the Korn shell)

* [app-text/tree](http://packages.gentoo.org/package/app-text/tree) (Lists directories recursively, and produces an indented listing of files)

- [dev-lang/perl](http://packages.gentoo.org/package/dev-lang/perl) (Larry Wall's Practical Extraction and Report Language)
- [dev-lang/python](http://packages.gentoo.org/package/dev-lang/python) (An interpreted, interactive, object-oriented programming language)
- [dev-lang/ruby](http://packages.gentoo.org/package/dev-lang/ruby) (An object-oriented scripting language)

* [dev-libs/cyrus-sasl](http://packages.gentoo.org/package/dev-libs/cyrus-sasl) (The Cyrus SASL (Simple Authentication and Security Layer))
* [dev-libs/libaio](http://packages.gentoo.org/package/dev-libs/libaio) (Asynchronous input/output library that uses the kernels native interface)
* [dev-libs/libedit](http://packages.gentoo.org/package/dev-libs/libedit) (BSD replacement for libreadline)
* [dev-libs/openssl](http://packages.gentoo.org/package/dev-libs/openssl) (full-strength general purpose cryptography library (including SSL v2/v3 and TLS v1))
* [dev-libs/protobuf](http://packages.gentoo.org/package/dev-libs/protobuf) (Google's Protocol Buffers -- an efficient method of encoding structured data)

- [dev-perl/Nagios-Plugin](http://packages.gentoo.org/package/dev-perl/Nagios-Plugin) (A family of perl modules to streamline writing Nagios plugins)

* [dev-python/nagiosplugin](http://packages.gentoo.org/package/dev-python/nagiosplugin) (Python class library to help writing Nagios checks)
* [dev-python/netaddr](http://packages.gentoo.org/package/dev-python/netaddr) (Network address representation and manipulation library)
* [dev-python/pip](http://packages.gentoo.org/package/dev-python/pip) (Installs python packages -- replacement for easy_install)
* [dev-python/python-ldap](http://packages.gentoo.org/package/dev-python/python-ldap) (Various LDAP-related Python modules)
* [dev-python/virtualenv](http://packages.gentoo.org/package/dev-python/virtualenv) (Virtual Python Environment builder)

- [dev-ruby/bundler](http://packages.gentoo.org/package/dev-ruby/bundler) (An easy way to vendor gem dependencies)
- [dev-ruby/rubygems](http://packages.gentoo.org/package/dev-ruby/rubygems) (Centralized Ruby extension management system)

* [dev-util/ccache](http://packages.gentoo.org/package/dev-util/ccache) (fast compiler cache)
* [dev-util/strace](http://packages.gentoo.org/package/dev-util/strace) (A useful diagnostic, instructional, and debugging tool)
* [dev-util/systemtap](http://packages.gentoo.org/package/dev-util/systemtap) (A linux trace/probe tool)

- [dev-vcs/git](http://packages.gentoo.org/package/dev-vcs/git) (GIT - the stupid content tracker, the revision control system heavily used by the Linux kernel team)
- [dev-vcs/mercurial](http://packages.gentoo.org/package/dev-vcs/mercurial) (Scalable distributed SCM)
- [dev-vcs/subversion](http://packages.gentoo.org/package/dev-vcs/subversion) (Advanced version control system)

* [mail-client/mailx](http://packages.gentoo.org/package/mail-client/mailx) (The /bin/mail program, which is used to send mail via shell scripts)

- [net-analyzer/nagios-check_logfiles](http://packages.gentoo.org/package/net-analyzer/nagios-check_logfiles) (A nagios plugin for checking logfiles)
- [net-analyzer/nagios-plugins](http://packages.gentoo.org/package/net-analyzer/nagios-plugins) (Nagios 1.4.16 plugins - Pack of plugins to make Nagios work properly)
- [net-analyzer/nagios](http://packages.gentoo.org/package/net-analyzer/nagios) (The Nagios metapackage - merge this to pull install all of the nagios packages)
- [net-analyzer/netcat6](http://packages.gentoo.org/package/net-analyzer/netcat6) (netcat clone with better IPv6 support, improved code, etc...)
- [net-analyzer/net-snmp](http://packages.gentoo.org/package/net-analyzer/net-snmp) (Software for generating and retrieving SNMP data)
- [net-analyzer/nrpe](http://packages.gentoo.org/package/net-analyzer/nrpe) (Nagios Remote Plugin Executor)
- [net-analyzer/tcpdump](http://packages.gentoo.org/package/net-analyzer/tcpdump) (A Tool for network monitoring and data acquisition)
- [net-analyzer/traceroute](http://packages.gentoo.org/package/net-analyzer/traceroute) (Utility to trace the route of IP packets)

* [net-firewall/iptables](http://packages.gentoo.org/package/net-firewall/iptables) (Linux kernel (2.4+) firewall, NAT and packet mangling tools)

- [net-fs/nfs-utils](http://packages.gentoo.org/package/net-fs/nfs-utils) (NFS client and server daemons)

* [net-libs/libkeepalive](http://packages.gentoo.org/package/net-libs/libkeepalive) (Enable tcp keepalive in glibc based binary dynamic executables)

- [net-mail/mailbase](http://packages.gentoo.org/package/net-mail/mailbase) (MTA layout package)

* [net-misc/chrony](http://packages.gentoo.org/package/net-misc/chrony) (NTP client and server programs)
* [net-misc/dhcpcd](http://packages.gentoo.org/package/net-misc/dhcpcd) (A fully featured, yet light weight RFC2131 compliant DHCP client)
* [net-misc/openssh](http://packages.gentoo.org/package/net-misc/openssh) (Port of OpenBSD's free SSH release)
* [net-misc/rsync](http://packages.gentoo.org/package/net-misc/rsync) (File transfer program to keep remote files into sync)
* [net-misc/wget](http://packages.gentoo.org/package/net-misc/wget) (Network utility to retrieve files from the WWW)

- [net-nds/openldap](http://packages.gentoo.org/package/net-nds/openldap) (LDAP suite of application and development tools)

* [sec-policy/apparmor-profiles](http://packages.gentoo.org/package/sec-policy/apparmor-profiles) (A collection of profiles for the AppArmor application security system)

- [sys-apps/apparmor-utils](http://packages.gentoo.org/package/sys-apps/apparmor-utils) (Additional userspace utils to assist with AppArmor profile management)
- [sys-apps/baselayout](http://packages.gentoo.org/package/sys-apps/baselayout) (Filesystem baselayout and init scripts)
- [sys-apps/coreutils](http://packages.gentoo.org/package/sys-apps/coreutils) (Standard GNU file utilities (chmod, cp, dd, dir, ls...), text utilities (sort, tr, head, wc..), and shell utilities (whoami, who,...))
- [sys-apps/dbus](http://packages.gentoo.org/package/sys-apps/dbus) (A message bus system, a simple way for applications to talk to each other)
- [sys-apps/dstat](http://packages.gentoo.org/package/sys-apps/dstat) (Versatile replacement for vmstat, iostat and ifstat)
- [sys-apps/gptfdisk](http://packages.gentoo.org/package/sys-apps/gptfdisk) (gdisk - GPT partition table manipulator for Linux)
- [sys-apps/kmod](http://packages.gentoo.org/package/sys-apps/kmod) (library and tools for managing linux kernel modules)
- [sys-apps/man](http://packages.gentoo.org/package/sys-apps/man) (Standard commands to read man pages)
- [sys-apps/net-tools](http://packages.gentoo.org/package/sys-apps/net-tools) (Standard Linux networking tools)
- [sys-apps/openrc](http://packages.gentoo.org/package/sys-apps/openrc) (OpenRC manages the services, startup and shutdown of a host)
- [sys-apps/pciutils](http://packages.gentoo.org/package/sys-apps/pciutils) (Various utilities dealing with the PCI bus)
- [sys-apps/xinetd](http://packages.gentoo.org/package/sys-apps/xinetd) (powerful replacement for inetd)

* [sys-auth/nss_ldap](http://packages.gentoo.org/package/sys-auth/nss_ldap) (NSS LDAP Module)
* [sys-auth/pam_ldap](http://packages.gentoo.org/package/sys-auth/pam_ldap) (PAM LDAP Module)

- [sys-boot/grub](http://packages.gentoo.org/package/sys-boot/grub) (GNU GRUB boot loader)

* [sys-devel/bc](http://packages.gentoo.org/package/sys-devel/bc) (Handy console-based calculator utility)

- [sys-fs/btrfs-progs](http://packages.gentoo.org/package/sys-fs/btrfs-progs) (Btrfs filesystem utilities)
- [sys-fs/eudev](http://packages.gentoo.org/package/sys-fs/eudev) (Linux dynamic and persistent device naming support (aka userspace devfs))
- [sys-fs/ncdu](http://packages.gentoo.org/package/sys-fs/ncdu) (NCurses Disk Usage)
- [sys-fs/xfsprogs](http://packages.gentoo.org/package/sys-fs/xfsprogs) (xfs filesystem utilities)

* [sys-kernel/genkernel](http://packages.gentoo.org/package/sys-kernel/genkernel) (Gentoo automatic kernel building scripts)
* [sys-kernel/gentoo-sources](http://packages.gentoo.org/package/sys-kernel/gentoo-sources) (Full sources including the Gentoo patchset for the 2.6 kernel tree)
* [sys-kernel/linux-firmware](http://packages.gentoo.org/package/sys-kernel/linux-firmware) (Linux firmware files)

- [sys-libs/gdbm](http://packages.gentoo.org/package/sys-libs/gdbm) (Standard GNU database libraries)
- [sys-libs/glibc](http://packages.gentoo.org/package/sys-libs/glibc) (GNU libc6 (also called glibc2) C library)
- [sys-libs/pam](http://packages.gentoo.org/package/sys-libs/pam) (Linux-PAM (Pluggable Authentication Modules))

* [sys-process/acct](http://packages.gentoo.org/package/sys-process/acct) (GNU system accounting utilities)
* [sys-process/atop](http://packages.gentoo.org/package/sys-process/atop) (Resource-specific view of processes)
* [sys-process/at](http://packages.gentoo.org/package/sys-process/at) (Queues jobs for later execution)
* [sys-process/lsof](http://packages.gentoo.org/package/sys-process/lsof) (Lists open files for running Unix processes)
* [sys-process/restarter](http://packages.gentoo.org/package/sys-process/restarter) (Automatic service restart after updates)
* [sys-process/vixie-cron](http://packages.gentoo.org/package/sys-process/vixie-cron) (Paul Vixie's cron daemon, a fully featured crond implementation)

- [www-apache/mod_python](http://packages.gentoo.org/package/www-apache/mod_python) (An Apache2 module providing an embedded Python interpreter)

* [www-servers/apache](http://packages.gentoo.org/package/www-servers/apache) (The Apache Web Server)

## Configuration

All tools can be configured individually with dotfiles in the user's home
directory.

% vim: set spell spelllang=en:
