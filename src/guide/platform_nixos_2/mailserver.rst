.. _nixos2-mailserver:

Mail server
===========

This role installs a complete mail server for incoming and outgoing mail.
Incoming mail is either delivered to IMAP mailboxes via dovecot, or forwarded to
an application via alias/transport configs. Outgoing mail is accepted on the
submission port or via a *sendmail* executable.

An optional web mail UI is included. This role also includes state-of-the-art
spam control.

User accounts can be created/modified dynamically. There is, however, no default
mechanism for user management besides text files.

Components
----------

* `Postfix <http://www.postfix.org/>`_
* `Dovecot <https://dovecot.org/>`_
* `Roundcube <https://roundcube.net/>`_
* `rspamd <https://rspamd.com/>`_
* `OpenDKIM <http://www.opendkim.org/>`_
* `SPF/PostSRSd <https://github.com/roehling/postsrsd>`_
* Mail client `autoconfiguration
  <https://wiki.mozilla.org/Thunderbird:Autoconfiguration>`_
* `Knot DNS <https://www.knot-dns.cz/>`_ as local cache


Configuration
-------------

General
~~~~~~~

Mail servers need proper DNS configuration. DNS configuration errors will likely
result in mail being rejected by remote mail servers. Some important
terminology:

HELO name
  The canonical name of the mail server. The HELO name is the same as the value
  of the **mailHost** option and the **myhostname** Postfix configuration
  variable. The HELO name must be listed in the **MX** records of
  all served *mail domains*.

  Example: mail.test.fcio.net

Frontend IP addresses
  Public IPv4 and/or IPv6 adresses. **A** and **AAAA** queries of the HELO name
  must resolve to the frontend IP addresses. Each address must have a **PTR**
  record which must resolve exactly to the HELO name.

  Example: 195.62.126.119, 2a02:248:101:62::1191

Mail domain
  List of DNS domains that serve as domain part in mail addresses hosted by a
  mail server. Not to be confused with the domain part of the server's FQDN
  which may be the same or may not.  Each *domain* must have a **MX** record
  which points to the mail server's *HELO name*.

  Example: test.fcio.net, test2.fcio.net


Nix options
~~~~~~~~~~~

Options can be set in either :file:`/etc/nixos/local.nix` or
:file:`/etc/local/nixos/`.

Frequently used options:

domains
  List of *mail domains* which should be served by this mail server.

mailHost
  *HELO name*, see above.

webmailHost
  Virtual server name for the Roundcube web mail service. Appropriate DNS
  entries are expected to point to the VM's frontend address. If this option is
  set, the Roundcube service will be enabled.

rootAlias
  E-mail address to receive all mails to the local root account.

Specialist options:

redisDatabase
  Database number (0-15) for rspamd. Defaults to 5. The database number can
  be adjusted if any another local application happens to use DB 5.

smtpBind4 and smtpBind6
  Which frontend address to use in case ethfe has several of them.

explicitSmtpBind
  Whether to include explicit smtp_bind_address in the Postfix main.cf file.
  Defaults to true if ethfe has more than one IPv4 or IPv6 address. Needs
  to be overridden only in very special cases.

passwdFile
  Virtual mail users listing in :manpage:`passwd(7)` format. Set this if an
  application generates this file automatically and puts it into an
  application-specific location.

.. admonition:: Example: :file:`/etc/local/nixos/mail.nix`

  ::

    flyingcircus.roles.mailserver = {
      enable = true;
      mailHost = "mail.test.fcio.net";
      webmailHost = "webmail.test.fcio.net";
      domains = ["test.fcio.net", "anothertest.fcio.net"];
    };


Integration points
~~~~~~~~~~~~~~~~~~

/etc/local/mail/users.json
  Statically configured virtual mail users. Must contain a dict keyed by virtual
  mail address and may have the following fields:

  * hashedPassword: SHA-256 hash of the mail user's SMTP and IMAP password. Use
    :command:`mkpasswd -m sha-256` to create a suitable hash.
  * aliases: list of additional e-mail addresses for this user.
  * catchAll: list of additional subdomain for which this user received all
    mails regardless of the local part.
  * quota: byte size like "4G".
  * sieveScript: string which includes a statically configured sieve script or
    *null* to allow dynamic sieve scripts via managesieve.

  All domain parts (key and aliases) must be listed in the *domains* option.

/etc/local/mail/local_valiases.json
  Additional aliases which are not mentioned in users.json. Expected to be a
  dict with the alias as key and the receiving address as value.

/etc/local/mail/main.cf
  Additional Postfix :manpage:`postconf(5)` settings.

/etc/local/mail/dns.zone
  Copy-and-paste DNS records for inclusion in zone files. Adapt if necessary.


Interaction
-----------

Open ports
~~~~~~~~~~

* 25: Postfix SMTP incoming. Public access, anti-spam measures apply.
* 80: `http://autoconfig.${domain}` - mail client settings autoconfiguration.
  Everything else will be directed to HTTPS.
* 143: Dovecot IMAP. STARTTLS and authentication required.
* 443: Roundcube web mail.
* 587: Postfix SMTP submission. STARTTLS and authentication required.
* 993: Dovecot IMAPS. Authentication required.
* 4190: Dovecot managesieve

Dynamic account creation
~~~~~~~~~~~~~~~~~~~~~~~~

Applications may modify the file specified in the *passwdFile* option (default:
:file:`/var/lib/dovecot/passwd`) to create mail accounts dynamically. Note that
this file must comply to the :manpage:`passwd(5)` file format. This means that
all 7 fields must be present, although only the first two (username=mail address
and SHA-256 crypted password) are actually used.

Dynamic accounts exist in addition to statically created accounts from
:file:`users.json`.

If there is both a statically configured password and an appropriate entry in
the passwrd file, a user may authenticate successfully with either one. So make
sure that the `hashedPassword` entry is empty if users are expected to change
their password dynamically.


Roundcube password change and vacation message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Roundcube web UI allows to change the password and to install a vacation
message via a preconfigured sieve script. Both functions can be accessed via the
"Options" menu.


Monitoring
----------

Monitoring checks/metrics created by this role:

* Port checks for SMTP, submission, IMAP, and IMAPs.
* Postfix excessive queue length check.
* Postfix queue length, size, and age metrics.

.. vim: set spell spelllang=en:
