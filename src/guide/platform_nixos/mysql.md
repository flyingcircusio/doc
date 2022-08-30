(nixos-mysql-server)=

# MySQL (Percona)

Managed instance of the [Percona MySQL](http://percona.com) database server.

## Components

- MySQL server
- Basic database set up with initial root user creation.

## Configuration

Service users may drop config file snippets containing additional options
into {file}`/etc/local/mysql/*.cnf`.

The password for MySQL's root user can be found in
{file}`/etc/local/mysql/mysql.passwd`. This file is readable by service users.

:::{note}
Please note that there is no default permission that allows root logins from
external networks. When connecting to MySQL as root, please omit the
{command}`-h` switch:

```
test@test00 ~ $ mysql -u root -p<root password here>
```
:::

## Interaction

Service users may invoke {command}`sudo fc-manage --build` to apply
service configuration changes and trigger service restarts (if necessary).

## Monitoring

The default monitoring setup checks that the MySQL server
process is running.

% vim: set spell spelllang=en:
