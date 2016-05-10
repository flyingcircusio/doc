.. _mailserver:

Mail server
===========

Provides an MTA (Mail Transfer Agent) to process incoming and outgoing
customer emails.

Components
----------

* Postfix
* policyd-weight
* postgrey
* AMaViS
* SpamAssassin

Configuration
-------------

* Overrule/extend standard system aliases in :file:`/etc/mail/local-aliases`.
* There are various maps in :file:`/etc/mail` that allow customizing mail
  delivery and access control. User-customizable maps include:

  * access-client
  * access-helo
  * access-recipient
  * access-sender
  * canonical
  * canonical.pcre
  * external-networks
  * local-aliases
  * relay-domains
  * transport
  * virtual-aliases

* The host name announced in HELO can be set in :file:`/etc/postfix/myhostname`.
  Please note that DNS records (forward/reverse) must be in place before
  changing this file.
* Customizations to main.cf parameters can be written into
  :file:`/etc/postfix/main.d/40_local.cf`. It is also OK to create new files in
  the form :file:`/etc/postfix/main.d/{NN_NAME}.cf`.


Sending mail from applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mails should generally be injected via the *submission* port (587). Port 25 is
reserved for incoming mail delivery. Specifically, delivery to port 25 may
result in a temporary failure (4xx response codes) and must be retried. Mails
submitted via port 587 are always spooled by the mail server.

By default, mails from localhost are accepted without authentication. To
submit mails from other hosts, choose one of two options:

#. Set SMTP AUTH credentials on the mail server using :command:`sudo
   saslpasswd2 {USERNAME}` and let submission clients authenticate against the
   mail server (preferred).
#. List IP addresses or CIDR networks in :file:`/etc/mail/external-networks`.
   Mail submission from one of the listed addresses will proceed  without
   authentication.


Forwarding mail to applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custom pipe transports are generated automatically for each service user
following the naming scheme "user-*username*". For
example, if the service user *webapp* is defined, there is a pipe transport
named `user-webapp`. It delivers mails by calling :file:`{HOME}/bin/deliver` in
the respective service users' home directory.

Use :file:`/etc/mail/transport` rules to forward mails to user-specific
transports. For example, a transport line ::

   @virtual.do.main  user-webapp:

causes all mails sent to a virtual domain being piped into the executable
:file:`~webapp/bin/deliver`. The local delivery script is called for every
incoming mail with the parameters::

   $HOME/bin/deliver -f $sender $nexthop $recipient [$recipient ...]

.. note::

   Set `user-USER_destination_recipient_limit = 1` in
   :file:`/etc/postfix/main.d/40_local.cf` to avoid delivery to multiple
   recipients.

All other aspects like local mail server names etc. must be configured by an
administrator.


DNS Setup
---------

Mail servers require a special DNS setup. Please check with our :ref:`support`
that the following conditions hold. Unclean DNS setups may cause bad
anti-spam scorings on remote mail servers.

Mail server name (HELO name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each mail server must have a distinguished own name (HELO name) which configured
as MX of the server's virtual domains and known internally as `myhostname`. In
the following examples, the mail server's name is `mail.test.fcio.net`.

DNS configuration::

  maildomain1.test.fcio.net.     MX 10 mail.test.fcio.net.

Local configuration::

  $ cat /etc/postfix/myhostname
  mail.test.fcio.net

IP addresses
^^^^^^^^^^^^

The forward and reverse resolution of the mail server's frontend addresses must
match exactly its HELO name.

DNS configuration::

  mail.test.fcio.net.   AAAA    2a02:238:f030:1c2::10
  mail.test.fcio.net.   A       172.20.2.10

  2a02:238:f030:1c2::10 PTR     mail.test.fcio.net.
  172.20.2.10           PTR     mail.test.fcio.net.

Postfix configuration::

  smtp_bind_address = 172.20.2.10
  smtp_bind_address6 = 2a02:238:f030:1c2::10

Greylisting
^^^^^^^^^^^

By default external mail servers have to pass `greylisting`_ when delivering 
mail for the first time. Service users may whitelist specific clients or
recipients by setting a whiteliste rule in
:file:`/etc/postfix/postgrey_whitelist_clients.local` or
:file:`/etc/postfix/postgrey_whitelist_recipients.local` as described on the
`postgrey man page`_.

To put changes into effect, invoke :command:`sudo /etc/init.d/postgrey restart`
as service user.

.. _greylisting: http://projects.puremagic.com/greylisting/ 
.. _postgrey man page: http://linux.die.net/man/8/postgrey

Interaction
-----------

* To put changed postfix maps and aliases into effect, invoke :command:`sudo
  /etc/init.d/postfix reload` as service user.
* Use :command:`sudo saslpasswd2` to edit the Postfix authentication database
  as service user. (see :manpage:`saslpasswd2(8)`). Note that the :option:`-f`
  option is not allowed. Use :command:`sudo sasldblistusers2` to inspect the
  SASL authentication database.

If the :ref:`antivirus` role is also present on the same VM, all mails are
automatically scanned for viruses. If the antivirus role is not present, mails
are only scanned for spam.

Monitoring
----------

An extensive range on checks is provided by default, including:

* process checks
* port checks for SMTP
* rejection checks for spam and virus mails
* stale postfix maps

.. vim: set spell spelllang=en:
