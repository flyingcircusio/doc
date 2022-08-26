(dovecot)=

# Dovecot

Provides the Dovecot IMAP/POP server to store and access emails.

## Components

- Dovecot

## Configuration

The managed configuration provides the following setup:

- Mails are stored in *maildir* format in {file}`/srv/vmail/<domain>/<user>`.
- Access is possible via IMAP(S) and POP(S) on all interfaces.
- The SSL certificates are self-signed by default.

## Interaction

Service users may place custom configuration directives into
{file}`/etc/dovecot/local.conf`.

Service users may reload dovecot using {command}`sudo /etc/init.d/dovecot
reload`. The init-script can be also used to restart dovcot using
{command}`sudo /etc/init.d/dovecot restart`.

A limited set of {manpage}`doveadm(1)` subcommands is available to users with
`sudo-srv` permission. Examples:

```
sudo doveadm mailbox list -u user@domain
sudo doveadm auth test user@domain password
sudo doveadm who
```

## Monitoring

- Dovecot processes running
- IMAP(S) port reachable and responsive
- POP(S) port reachable and responsive
- Log checks for {file}`/var/log/mail`

% vim: set spell spelllang=en:
