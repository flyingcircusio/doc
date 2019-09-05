.. Customers need to be notified when substantial changes occur in this document!

.. _data-protection:

Data protection measures
========================

In addition to purely technical security measures we implement additional
measures to provide a safe environment for your and your customers' data
based on the following standards and regulations:

* ISMS based on the ISO 27000 family (in progress),
* Germany's `federal data protection law (BDSG) <http://de.wikipedia.org/wiki/Bundesdatenschutzgesetz>`_, and
* the EU's `General Data Protection Regulation (GDPR) <https://de.wikipedia.org/wiki/Datenschutz-Grundverordnung>`_.

.. contents::


Data protection officer
-----------------------

The appointed data protection officer is:

| Nick Lindovsky
| DITAC GmbH
| OT Weißlandt-Gölzau · Raffineriestr. 09 · 06369 Südliches Anhalt
| https://ditac.de · datenschutz@flyingcircus.io
| `+49 34978 30186 <tel:+493497830186>`_


General
-------

This document is structured based on the BDSG's first appendix which summarizes
the law's requirements as a few “golden rules”. For the translation of German
official terms to English we made use of the EU's `InterActive Terminology for
Europe <http://iate.europa.eu>`_.

As some of the requirements of the law depend on the specific (contractual)
situation, we'd like to first outline the general situation that hosting in
the Flying Circus puts you in:

Commissioned data processing
  applies within the framework of the GDPR. We will implement a contract for
  commissioned data protection suitable to the GDPR with you.

Duty to give information
  People who are affected by processing of data have right to request
  information about what data about them is being stored as well as about the
  processes how this data is being kept secure.

Periodical check for compliance to regulations:
  The client has the responsibility to routinely check that applicable regulations
  are being conformed to by their contractor. Yearly checks appear to
  be sufficient even for highly sensitive data (e.g. medical records). The
  result needs to be documented in written form. The audit usually needs to be
  performed by a third party.


Admission control
-----------------

**Measures for admission control ensure that unauthorized persons cannot
physically access the data processing equipment.**

The physical assets (servers, switches, hard drives, ...) are located in EU
data centers operated by third parties. The ownership of the physical equipment
is with the Flying Circus, or, in special cases by our customers
[#customer-owned]_.

For each data center used by us we require the following measures:

* video surveillance (outside facilities, in-doors and rack corridors)
* two-factor security for granting access (e.g. personal password and
  transponder card) with logging
* physical access must be documented
* 24 hour guard services with linked alarm system
* separate physical security zones for general areas, data center
  infrastructure and customer-accessible areas
* separately locked racks with the possibility to use custom locks and keys.

We maintain a separate :ref:`data-centers`.

Physical access to data processing equipment may be performed only by the
Flying Circus' :ref:`administrators <administrators>`. Administrators may
delegate physical access to other persons (e.g., data center staff).


.. _entry-control:

Entry control
-------------

**Measures for entry control ensure that unauthorized third parties can not make use
of the data processing systems.**

Machines managed within the Flying Circus can be accessed by a variety of ways for
management purposes: SSH, web interfaces, and others. For those we employ
a homogenous scheme to identify and authorize users within the Flying Circus.
Management access to systems must use encrypted communication channels.

Identification and authorization of customer applications not managed by the Flying Circus infrastructure are not covered by our security responsibility. Our
customers are required to ensure the security of their applications themselves.

User identification must be performed using *personal* credentials, so that
actions can be traced back to an individual originator. Thus, sharing one's
credentials with another person is prohibited.  Credentials can be either a
username and a cryptographic measure (e.g. a private/public key scheme) or a
password, depending on the applicability.

Users with a Flying Circus account are required to manage their password securely:
unauthorized physical or logical access to objects that can potentially store
passwords may not result in a compromised passwords. Examples are: Home
directory on a laptop, keychain or password manager software, backups, USB
sticks, smartphones. Strongly encrypted storage of passwords is permissible.

All machines have emergency root logins which may only be used by
:ref:`Flying Circus administrators <administrators>` if regular user
authentication is not working correctly. Such uses must be documented.

All privileged actions need to be securely logged. [#secure-logging]_ SSH logins
must be performed using SSH keys.  Successful SSH logins to machines are
logged---unsuccessful SSH login attempts are not. [#log-unsuccessful-attempts]_


.. _access-control:

Access control
--------------

**Measures for access control protect against access by unauthorized
personnel.**

Flying Circus implements a permission-based concept to separate application
maintenance tasks from privileged administrative tasks: for example, customer
software updates or database access versus OS updates or OS configuration.

Privileged administrative access is generally not granted to customers.
In cases where another person who is not an
administrator is needed to solve a problem, a shared session between an
administrator and the other person must be established
(e.g. with :command:`screen`).

Technically, there are three access variants to perform privileged
administrative operations:

#. Using a user account which has been granted the 'login' and
   'wheel' :ref:`permissions <permissions>` for a certain project. This
   requires the user to log into a regular account using his SSH key and
   additionally provide his password to access privileged operations.

#. Using a user account which is member of the global
   group of administrators (see :ref:`administrators`) which grants access to
   all machines within the Flying Circus infrastructure.

#. Emergency root logins (see above in :ref:`entry-control`).

Authorized and unauthorized access to privileged operations is logged.
[#trace-tty]_

Flying Circus maintains a set of permissions which enable users to perform
application maintenance and other semi-privileged tasks, e.g. access to
service user accounts or database administration rights. Permissions are granted
to individual users upon customer request.

All permission assignments are traceable and explicitly documented: their
effects are documented in the configuration code and their assignments
are documented in the configuration database. A comprehensive list of users and
their permissions may be produced automatically on request. [#admin-revocation]_

Group accounts are generally not allowed to perform privileged administrative
operations to ensure traceability of actions.

Passwords for physical machines granting access to root accounts and IPMI
controllers are stored as copies in a strongly encrypted password manager.


Transfer control
----------------

**Measures for transfer control ensure that data that is being saved or
transferred is protected against unauthorized reading, copying, modification, or
deletion. It also requires that the points for intentional transfer are
documented.**

All private data transferred past the boundary of a machine must use an
authenticated and encrypted communication channel (exceptions see below).
Data paths where sensitive information may be transferred include:

* Application data (e.g., database contents) is transferred from or to the
  customer using the standard SCP/SFTP protocol.

* Persistent data is saved on storage servers. Storage traffic is not encrypted
  due to performance reasons, but storage servers are connected to application
  servers using a private network. Machines on which administrative privileges
  are granted to customers are not allowed to connect directly to the storage
  network (see also :ref:`network-security`).

* Backups are transferred to backup servers at the same site using an encrypted
  communication channel or the private storage network. Backup data may also be
  transferred to off-site backup servers to improve disaster recovery abilities.

* In addition to application data, a system can generate data at runtime that
  contains sensitive information, for example log files. Log files usually do
  not leave the machine on which they were generated, but may be transferred to
  a central log server via an encrypted channel. Only Flying Circus
  administrators have access to the central log server.


Input control
-------------

**Measures for input control ensure that input, change, and deletion of data are
documented showing at least who worked when on what data.**

The security of data entry, change and deletion is generally part of the
customer's application. Customers must ensure that data entry,
deletion and removal are handled appropriately according to their applicable
data protection laws.

However, within the performance of maintenance work it may be necessary that
administrators need to enter, change, or delete data records on a low technical
level to ensure the continued operation of the overall system. This will only
happen after having informed the affected customers and having documented this
in our issue tracking system.

Managed log files are rotated by the Flying Circus infrastructure automatically
with sensible retention times.

Changes in the Flying Circus user directory (e.g., SSH keys) can be performed by
the customer themselves or through our support. If the change happens through
our support hen it  must be documented beforehand and confirmed by the customer
after the change has been performed.


Order control
-------------

**Measures for order control ensure that data is only processed according to the
orders of the client.**

The Flying Circus ensures that all actions taken by system administrators are
covered by a contract or order with the customers affected by the action. This
can be due to broad maintenance contracts or due to specific support requests.

Individual change requests must have an associated ticket in the Flying Circus
request tracking system.

Specific actions performed will be reported to the customer if required.


Availability
------------

**Measures for availability ensure that data is not accidentally destroyed or
lost.**

The availability of resources depending on the data center facilities is
delegated to the operator of the data center. The Flying Circus facilitates
service level agreements to make expectations about availability explicit.

The selection of hardware is performed by the Flying Circus using professional
equipment and vendors. The Flying Circus facilitates standard procedures for
increased availability of single components (e.g., RAID storages, redundant
power supplies, spare components).

Customer data is regularly backed up according to the Flying Circus'
:ref:`backup schedule <backup>`. Restoration of past states may be performed
by administrators on request. Additionally, a
:ref:`disaster recovery plan <disaster-recovery>` details failure scenarios,
our preventative and recovery measures.


Separation
----------

**Measures for separation ensure that data that is collected for separate
purposes must be processed separately.**

To separate data from different customers the Flying Circus facilitates virtualization:
both virtual machines (to separate execution context) and SAN (to separate
storage) ensure that customers can only access data belonging to them. Within a
single machine access to different files and processes is available using
standard UNIX permissions.

Machines (both virtual and physical) live in a specific *access ring* (short:
ring):

* *Ring 0* machines perform infrastructure tasks. Thus, they need to process
  data belonging to several customers.  Only administrator access is allowed on
  such machines.  Examples include VM hosts and storage servers.
* *Ring 1* machines process data for a specific customer and are accessible to
  users associated to that customer. Examples include customer VMs.

All resources that belong logically together (e.g., VMs, storage
volumes) are bundled into *projects*. projects share that same set
of user accounts and permissions.


.. rubric:: Footnotes

.. [#customer-owned] If a customer owns equipment managed within the Flying Circus we
    require that this customer uses a separate rack with separate access control.

.. [#secure-logging] This requirement was added recently and has not been
    implemented yet.

.. [#log-unsuccessful-attempts] We consider not logging unsuccessful logins
   acceptable, as SSH logins are only valid using cryptographic private/public
   key authentication. Password logins are always rejected. Potential attack
   vectors are thus limited to stolen or cracked private keys or vulnerabilities
   in the SSH server software. Cracked keys are practically impossible using
   current technology. Known broken key formats are revoked/rejected regularly.
   Stolen keys or errors in the server software will not be
   traceable using unsuccessful login records either.  On the opposite: the
   amount of password login tries performed nowadays (due to bot nets etc.)
   would cause spamming of the logging infrastructure which in turn can be a
   vector for DOS attacks.

.. [#admin-revocation] Revoking administrator privileges is currently not a
    standardized process but will be added to the list of business processes
    soon.

.. [#trace-tty] Individual actions performed with administrative privileges are
   only partially logged.

.. [#restricted-exception] An exception to this rule are restricted machines,
   which are used in exceptional cases only and operate in a separated network
   evironment.
