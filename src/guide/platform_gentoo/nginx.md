(webgateway)=

# Web gateway

## Description

Installs services needed for a public facing web server.

## Components

- {ref}`nginx`
- {ref}`modsecurity`
- {ref}`awstats`

(nginx)=

## nginx

### Interaction

Service users may invoke {command}`sudo /etc/init.d/nginx {reload,restart}` to
activate updated nginx configurations.

### Configuration

#### Virtual hosts

We provide a basic nginx configuration, but do not define virtual hosts. Service
users may create individual config files in {file}`/etc/nginx/local` that will
be included in a `http` context.

The file {file}`/etc/nginx/local/example-configuration` may serve as a start.
Copy this file to something like {file}`/etc/nginx/local/{vhost}.conf`
and edit it. You must at least:

- replace *www.example.com* with the action virtual host name
- adapt the proxy statements to match your application.

#### Anonymization

If you want IP addresses (IPv4 and IPv6) in nginx log files to be anonymized,
use the log format "anonymized" by adding the following line inside your
*server* declaration block:

```
access_log /var/log/nginx/${server_name}_access.log anonymized;
```

This way, only a /24 prefix for IPv4 addresses and a /48 prefix for IPv6
addresses will be logged.

nginx' error log in {file}`/var/log/nginx/error.log` can not be anonymized this
way. You can, however, modify it's log level (or turn off the error log
completely) by overriding the [error_log](http://nginx.org/en/docs/ngx_core_module.html#error_log) directive
`outside` your server declaration block.

### Performance logging

In addition to the normal access log files found in
{file}`/var/log/nginx/{site}.access_log` (common log format), nginx logs
performance data for each request. There is a single log file
{file}`/var/log/nginx/performance.log` which has lines consisting of the
following fields:

- request time in ISO 8601 format
- request identifier (see {ref}`nginx-req-id` below)
- HTTP method
- full URL in the form "SCHEME://HOST/URI\*"
- request status
- length (bytes) of the response sent to the client
- length (bytes) of the request received from the client
- **p** if the request was pipelined, **-** otherwise
- total request time (from receiving the first byte until sending the
  last byte)
- comma-separated list of upstream request processing times (several items may
  be logged in case of upstream retries)
- mod_gzip compression ratio or **-** if no compression took place.

Example log line:

```
2015-04-17T16:56:36+02:00 32990.1 GET "http://flyingcircus.io/@@/gocept.flyingcircus/js/jquery.min.js" 200 38667 922 . 0.8 "0.002, 0.006" 2.44
```

Example [Pandas](http://pandas.pydata.org/) data import:

```python
import pandas
performance = pandas.read_csv(
  'performance.log', sep=' ', quotechar='"', parse_dates=['timestamp'],
  na_values='-', names=('timestamp', 'id',
    'method', 'url', 'status', 'response_length', 'request_length', 'pipe',
    'request_time', 'upstream_times', 'gzip_ratio'))
```

Example [PostgreSQL](http://www.postgresql.org/) data import:

```
CREATE TABLE performance (
  timestamp          TIMESTAMP WITH TIME ZONE,
  id                 VARCHAR(24),
  method             VARCHAR(10),
  url                TEXT,
  status             INT,
  response_length    INT,
  request_length     INT,
  pipe               CHAR(1),
  request_time       FLOAT,
  upstream_times     TEXT,
  gzip_ratio         FLOAT
);

COPY performance FROM 'performance.log' (FORMAT CSV, DELIMITER ' ',
   QUOTE '"', NULL '-');
```

(nginx-req-id)=

### Request IDs

`nginx` assigns each HTTP request a unique id. In the default configuration,
the id gets logged to `performance.log` and passed to upstream servers in
the `X-Nginx-Id` request header.

See {file}`/etc/nginx/nginx.conf` for details. Users who configure their own
`proxy_set_header` directives should be aware that they have to set this header
on their own if needed.

:::{note}
Request ids are not guaranteed to be unique forever. It is reasonable to
assume that request ids will not repeat on the same host on the same day.
:::

### Monitoring

- By default, the presence of nginx processes is checked.
- To get checks for individual web pages (presence, specific content, response
  time), please notify the support.

### Testing

To test your settings, e.g. to ensure you did not introduce some syntax error,
you can use {command}`sudo /etc/init.d/nginx configtest`.

(modsecurity)=

## mod_security

The open-source web application firewall [mod_security](http://modsecurity.org/) is included on all web gateways. In the default
configuration, however, it is inactive.

### Configuration

To activate `mod_security`, enable it in a nginx configuration section
(e.g., `server` or `location`):

```
ModSecurityEnabled on;
ModSecurityConfig /etc/nginx/modsecurity/modsecurity.conf;
```

This system-wide configuration file contains some useful defaults like
activating the base rule set etc. Initially, `mod_security` runs in report-only
mode. Additional configuration like switching to policing mode or including
custom rule sets goes into {file}`/etc/nginx/modsecurity/local.conf`. Service
users can also put completely different mod_security configuration files into
the {file}`/etc/nginx/modsecurity` directory and use these in place of the
default configuration file.

### Log files

All `mod_security` events are logged into a directory hierarchy under
{file}`/var/log/nginx/modsec_audit`. Each event is written to a new file.

Log directories which are more than a day old are archived as tarballs under
{file}`/var/log/nginx/modsec_audit_{DATE}.tar.xz` and are subject to normal log
retention.

(awstats)=

## AWStats

The system generates awstats configuration files automatically for every vhost
configured in nginx. awstats configuration generally goes into
{file}`/etc/awstats/vhosts.d` and individual configuration files follow the
naming convention {file}`awstats.{VHOST}.conf`.

awstats configuration for individual vhosts can be augmented with custom
configuration. Just put it into {file}`/etc/awstats/vhosts.d/local.{VHOST}.conf`
and it will be picked up during the next awstats run.

Application deployments may install configuration files for additional vhosts or
replace the system-generated awstats configuration altogether. To do this,
remove the system-generated configuration files (which belong to the `awstats`
user) and replace them with files owned by an service user. Such files will not
be touched by the automatic configuration update.

Web statistics generated on a VM can be accessed through
the [My Flying Circus](https://my.flyingcircus.io) dashboard.

By default, a list of all configured vhosts is presented. The presentation can
be adjusted by creating {file}`/etc/awstats/pages.cfg`. See the comments in
{file}`/srv/www/localhost/cgi-bin/stats.cgi` for details.

% vim: set spell spelllang=en:
