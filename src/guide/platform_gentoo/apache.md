(apache)=

# Apache

## Description

Installs the Apache webserver

## Components

- Apache

  - mod_cgi

  - mod_dav

  - mod_php

  - mod_proxy

  - mod_rewrite

  - ...

## Apache

:::{note}
The Apache web server is set up to listen on loopback and SRV
interfaces only and is not designed to run as the frontend webserver. You will
need to setup {ref}`webgateway` to make the LAMP stack public available.
:::

### Configuration

We provide a basic Apache configuration including a setup for AWstats, but do
not define any virtual hosts. Service users may create individual config files
in {file}`/etc/apache2/local` that will be included in Apache's global config
context.

### Interaction

To activate updated Apache configurations *without downtime* service users may
restart apache2 *gracefully*. There is one caveat though. If the config file is
incorrect apache2 may stop silently, which is why you should check the
correctness before.

```console
# check config
$ sudo /etc/init.d/apache2 configtest
# restart gracefully
$ sudo /etc/init.d/apache2 graceful
```

If you don't mind the downtime, service users may invoke

```console
$ sudo /etc/init.d/apache2 restart
```

### Logging

If not re-defined in a custom configuration log files can be found in
{file}`/var/log/apache2`. The log files are readable by the service users as
well as by human users.

### Monitoring

- By default, the presence of Apache processes is checked.
- To get checks for individual web pages (presence, specific content, response
  time), please notify the support.
