---
Publish Date: '2013-05-28'
---

(ldapserver)=

# OpenLDAP

Runs an OpenLDAP server for custom user management. The LDAP server listens by
default on the *srv* network for LDAP requests.

## Components

- OpenLDAP server
- {command}`ldapvi` utility to edit live LDAP records

## Configuration

The main OpenLDAP configuration is broken into parts. Some of these are left
empty by default and may be edited by service users:

- {file}`/etc/openldap/slapd.00acl-local.conf` allows to define custom ACLs
  which precede the default ACLs
- {file}`/etc/openldap/slapd.20main-local.conf` allows to add main configuration
  settings after the default configuration
- {file}`/etc/openldap/slapd.40backend-local.conf` allows to override the
  default backend configuration, e.g. to define custom indexes.
- {file}`/etc/openldap/listen_urls` contains a list of LDAP URIs to listen on,
  one per line. Listening on *srv* addresses and localhost is added
  automatically.

In addition, service users may also place custom schema files into
{file}`/etc/openldap/schema`.

The LDAP database suffix (as found in {file}`/etc/openldap/suffix`, e.g.
`cn=example,cn=com`) can only be changed by Flying Circus support staff and
requires the database to be rebuilt.

## Interaction

After configuration changes, invoke {command}`sudo /etc/init.d/slapd restart` as
service user to activate the new configuration.

To get all slapd indexes rebuilt during server restart, invoke {command}`sudo
slapd-restart-reindex`.

## Monitoring

We monitor the reachability of OpenLDAP via IPv4 and IPv6 via the *srv* network
by default. Usually these checks are sufficient, so there is no custom
monitoring configuration required.

% vim: set spell spelllang=en:
