:Publish Date: 2011-10-29

Release 2011-10-29
------------------

Packages
^^^^^^^^

- Security update for libxml2: GLSA 201110-26 (#9785).


Release 2011-10-26
------------------

Configuration
^^^^^^^^^^^^^

- Improved Nagios notification options to separate infrastructure and service
  notifications (#8161).
- Speed up Nagios startup to minimize monitoring "holes" (#9665).

Packages
^^^^^^^^

- Security update for ClamAV: GLSA 201110-16 (#9798).
- Security update for PostgreSQL: GLSA 201110-20 (#9714). PostgreSQL restart
  required.


Release 2011-10-13
------------------

Configuration
^^^^^^^^^^^^^

- Turn syslog-ng to back to listening on 514/udp after the developers
  misguidedly changed it to 610/udp.
- Ensure that `dstat` is installed on all physical machines.
- Fix php warning about unconfigured timezone in Nagios UI by setting timezone
  explicitly to Europe/Berlin.
- Enable HIGHMEM64 for virtual machines to allow more than 3.5GiB of memory.
  (#9531)
- Add puppet class for installing dev-lang/erlang.
- Improve GLSA notification mechanism (#8302)

Packages
^^^^^^^^

- Security fixes for phpmyadmin 3.4.4: Gentoo #383107
- Security fixes for apache 2.2.20: CVE-2011-3348
- Security fixes for dhcp: CVE-2011-{2748,2749}
- Upgrade to ghostscript 9.04 (RT 79159)


Release 2011-09-19
------------------

Configuration
^^^^^^^^^^^^^

- add fontconfig flag to gd on physical machines (in addition to virtual
  machines)

Packages
^^^^^^^^

- Security fixes for tiff 3.9.4: CVE-2009-5022,CVE-2010-{2595,3087},CVE-2011-{0192,1167}
- Security fixes for librsvg 2.34.0: CVE-2011-3146
- Security fixes for openssl 1.0.0e: CVE-2011-{3207,3210}

Release 2011-09-13
------------------

Configuration
^^^^^^^^^^^^^

- Bring wvWare tools back which disappeared accidentally during the last
  update (RT 78747).
- Remove superfluous old php configuration directories.
- Bugfix for memcached Nagios check.
- Restrict memcached to listen on SRV IPv4 only.
- Increased number of allowed postgresql IDLE processes in Nagios check.

Packages
^^^^^^^^

- Security fixes for apache 2.2.20, apache-tools 2.2.20: CVE-2011-3192 (#9539).
- Security fix for php 5.3.8: CVE-2011-2202 (#9548).
- Security fix for libpng 1.4.8: CVE-2011-2501 (#9558).
- Security fix for nagios 3.2.3: CVE-2011-2179 (#9522).
- Security fix for phpmyadmin 3.4.3.2: CVE-2011-3181 (#9521).
- Security fix for subversion 1.6.16: CVE-2011-1752 (#9523).
- Security fix for ca-certificates 20090709: Gentoo #381169 (#9542).



Release 2011-09-07
------------------

Mainly a bugfix release for the major update.

Configuration
^^^^^^^^^^^^^

- Resolve VM host race condition which impedes correct VM startup during
  booting.
- Resolve VM host init script bug which causes all iSCSI connections to die
  under certain conditions.

Documentation
^^^^^^^^^^^^^

- Expand examples in the :ref:`userinit` section.


Release 2011-08-29
------------------

Packages
^^^^^^^^

A great deal of updated packages is available with the new release. Some
highlights in no particular order (#8984):

- PostgreSQL 9.0.4 with changed configuration layout (see below).
- Python 2.5.4, 2.6.6, 2.7.1, and 3.1.3
- nginx 1.0.4
- ClamAV 0.97.1
- Emacs 23.4
- Poppler 0.16.7
- OpenSSL 1.0.0d
- NumPy 1.6.0
- setuptools 0.6.14
- virtualenv 1.6.1
- OpenSSH 5.8
- libjpeg-turbo 1.1.1
- Gentoo baselayout 2.0.3
- util-linux 2.19.1
- autoconf 2.68
- automake 1.11.1
- GCC 4.4.5
- Linux kernel version 2.6.38
- Update all packages not mentioned here to current Gentoo upstream versions.


Configuration
^^^^^^^^^^^^^

- PostgreSQL 9.0 configuration files (postgresql.conf etc.) reside now all in
  :file:`/etc/postgresql-9.0` instead of :file:`/srv/postgresql/9.0/data/`.
- Small VMs get more swap. This should avoid memory pressure from more or less
  inactive system services.
- Multi-Core VMs are available on request (#9101).
- RAM upgrades during automatically scheduled maintenance windows.
- Switch to OpenRC (#9087).
- Fix bug where a missing use flag prevented the installation of graphviz (RT
  78548).

Documentation
^^^^^^^^^^^^^

Another great deal of documentation updates, especially in the tutorials
section.


Release 2011-08-05
------------------

Configuration
^^^^^^^^^^^^^

- Automatic system maintenance scheduling. System activities that require
  downtime (kernel upgrades etc.) are automatically scheduled into the next
  available maintenance slot and e-mail notifications are sent out. System users
  may use :command:`list-maintenance` to view upcoming maintenance activities
  (#8668, #9359).
- Set default system Python version to 2.7. Scripts using a specific Python
  version (:file:`#!/usr/bin/python{X.Y}`) are not affected (#9043).
- Increase the initial TCP congestion window to 10 segments (RT 78202).


Monitoring
^^^^^^^^^^

- Fix bug with false positives in the `sysstat log freshness` check (#9269).
- Relax swap rate checks to avoid false positives. The checks should only cause
  alerts when a machine is constantly swapping.


Documentation
^^^^^^^^^^^^^

- Completely reworked :ref:`firststeps` section.
- Added tutorial ssh-keygen (#6938).


Release 2011-07-21
------------------

Configuration
^^^^^^^^^^^^^

- Support user-generated postgresql.conf Snippets in
  :file:`/etc/postgresql-{version}` (#9164)
- Service users may register user-specific init scripts to start and stop
  applications during system boot/shutdown. This feature is documented in
  :ref:`userinit` (RT 77751).


Documentation
^^^^^^^^^^^^^

- Revamped documentation, adding introductory material and better
  section overviews.


Release 2011-06-30
------------------

Configuration
^^^^^^^^^^^^^

- Increase file size limits for ClamAV (RT 77694).
- Further PostgreSQL performance tuning.
- Integration of customers-specific storage servers for high-volume customers
  (#9219).


Monitoring
^^^^^^^^^^

- Add `sysstat memory` check to provide continuous graphs of memory usage.


Documentation
^^^^^^^^^^^^^

- Improve :ref:`service-deployment-checklist` (#8371)
- Further improvements to :ref:`data-protection` (#8370)


Release 2011-06-21
------------------

Configuration
^^^^^^^^^^^^^

- Introduce facility to pin machines to fixed releases (#6820).
- Mount filesystems with `relatime` option by default.
- Tune PostgreSQL shared_buffers and wal_buffers parameter defaults (RT 77605).
- Tune kernel I/O scheduler settings.

Monitoring
^^^^^^^^^^

- Plot memory usage graph for all machines (sysstat_memory check).


Release 2011-06-09
------------------

Configuration
^^^^^^^^^^^^^

- Add xlhtml, rtf2xml and xls2csv to document processing role. (#8783)
- Add warning to auto-generated SSH :file:`authorized_keys` files that they
  should not be edited manually. (#8867)
- Reduce default greylisting time on mail gateways so that delivery of
  greylisted mails usually succeeds with the first queue re-run on
  upstream MTAs.
- Refine backup exclude lists to omit file that are easy to recreate in order to
  speed up backup and restore.

Monitoring
^^^^^^^^^^

- Relax swap activity checks to avoid false alerts when there is substantial
  swapping activity but no thrashing.
- Improve reliability of sysstat checks.

Documentation
^^^^^^^^^^^^^

- Greatly improve :ref:`data protection documentation <data-protection>` to
  provide a comprehensive overview of gocept.net data protection measures.
  (#8370)


Release 2011-05-26
------------------

Configuration
^^^^^^^^^^^^^

- Refine user access control to selectively grant rights to service users.
- Refine/debug global administrative control to selectively revoke super-admin
  rights of gocept's administrators (see :ref:`access-control`) (#8365)


Hardware
^^^^^^^^

- New monitoring server to reduce monitoring latency.
- Enhanced backup server performance.


Release 2011-05-18
------------------

Configuration
^^^^^^^^^^^^^

- Improved functionality and performance of the gocept.directory (CMDB) server.
- Fix bugs in Postfix/Mailman management code.


Release 2011-04-20
------------------

Hardware
^^^^^^^^

Add new storage and application servers for improved performance and
reliability.

Configuration
^^^^^^^^^^^^^

- Improve network routing to unnecessary roundtrips in some cases.
- Add Python 2.7 to the list of system Python installations (#8906)

Documentation
^^^^^^^^^^^^^

- Rework emergency docs in :ref:`support`.
- Add check list for service setups in :ref:`service-deployment-checklist` (#8765).


Release 2011-04-06
------------------

Configuration
^^^^^^^^^^^^^

- Introduce separate roles for PostgreSQL 8.2, 8.4, 9.0. At most one of these
  roles may be active on a node at a time.
- Improve monitoring for data links. We have seen failed auto-negotiation,
  which results in links running at 100 Mb/s and are now able to detect and fix
  these cases fast.
- Add support for TIFF graphics files to various utilities like
  :command:`convert` etc.

Documentation
^^^^^^^^^^^^^

- Describe support process.


Release 2011-02-22
------------------

Package updates
^^^^^^^^^^^^^^^

General snapshot update, upgrading most of the installed system packages. New
versions of highlighted packages are:

- python 2.6.6 and 3.1.2
- nginx 0.8.53 with IPv6 support
- haproxy 1.4.8
- postgresql 8.2.20 and 8.4.7

and many more.


Configuration
^^^^^^^^^^^^^

- Restart network services automatically after updates of the package or
  it's libraries (#8304).
- Allow different PostgreSQL versions (8.2, 8.4, or 9.0) (#7191).


Release 2011-01-28
------------------

Configuration
^^^^^^^^^^^^^

- Fix permission bug which rendered :command:`crontab` unusable for some users
  (#8392).
- Add ClamAV role to install the ClamAV virus scanner.


Documentation
^^^^^^^^^^^^^

- Add hint on how to use our mail server in mail.gocept.net.
- Document screen-multiuser (#8366).


Release 2011-01-17
------------------

Configuration
^^^^^^^^^^^^^

- Separate logging of system management changes (configuration, packages, users)
  to :file:`/var/log/sysconfig.log` from other syslog output (#8475).
- Introduce *restricted mode* machines which get system management changes only
  on explicit request (#8368).
- Send Nagios alert mails with :mailheader:`Precendence: junk` to circumvent
  auto responders.
- Introduce option for multi-page vhost list in web statistics overview (#8416)

Documentation
^^^^^^^^^^^^^

- nginx-ssl describes how to set up chained SSL certificates correctly.


.. vim: set spell spelllang=en:
