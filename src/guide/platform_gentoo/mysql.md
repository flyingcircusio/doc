---
Publish Date: '2013-03-28'
---

(mysql-server)=

# MySQL

Managed instance of the [MySQL] database server.

## Components

- MySQL server
- Basic database set up like initial root user creation.

## Configuration

A my.cnf file containing basic settings is put to {file}`/etc/mysql/my.cnf`.
Service users may drop config file snippets containing additional options
into {file}`/etc/mysql/local`.

The password for MySQL's root user can be found in
{file}`/etc/mysql/mysql.passwd`. This file is readable by service users.

:::{note}
Please note that there is no default permission that allows root logins from
external. When connecting to MySQL as root, please omit the {command}`-h`
switch:

```
test@test00 ~ $ mysql -u root -p<root password here>
```
:::

## Interaction

Service users may invoke {command}`sudo /etc/init.d/mysql restart` to restart
the MySQL server after configuration changes.

## Monitoring

The default monitoring setup checks that the MySQL server
process is running and that it responds to connection attempts to the standard
MySQL port.

% vim: set spell spelllang=en:

[mysql]: http://dev.mysql.com/
