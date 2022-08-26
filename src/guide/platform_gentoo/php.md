(php)=

(lamp)=

# PHP

## Description

Installs a PHP interpreter

There are three possibilities to setup PHP:

- Apache's mod_php
- FPM
- cgi/fcgi

While Apache's mod_php is an easy and fast forward solution to set up PHP on a
single VM, we recommend the use of FPM for more complex setups. FPM offers a
clean separation of webserver and PHP processes while keeping a wide range of
configuration options regarding the PHP interpreter.

## Components

- PHP

  - Apache mod_php
  - FPM
  - cgi

## Configuration

### Apache + mod_php

The mod_php extension is already enabled for Apache. You just have to create a
virtual host configuration {file}`/etc/apache/local/{PROJECT}.conf` that points
to your PHP project:

```
Listen 127.0.0.1:8080
<VirtualHost 127.0.0.1:8080>
        DocumentRoot /srv/<serviceuser>/<project>
        <Directory srv/<serviceuser>/<project>>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
        </Directory>
</VirtualHost>
```

:::{warning}
Be aware of the user who is running the PHP process. Using Apache's
mod_php all PHP processes are spawned as subprocesses of the Apache webserver.
In consequence they are executed in the context of the user "apache". Files
created or stored by PHP are owned by "apache" and not by the service user.
:::

### FPM

To use PHP's FastCGI Process Manager (FPM) you have to create a config in your
service user directory, for example {file}`/PATH/TO/SERVICE_USER/etc/fpm.conf`:

```
[global]
error_log = /srv/<serviceuser>/<project>/var/log/fpm.log

; if you manage your FPM process with supervisord FPM should run in foreground
daemonize = false

[myapp]
listen = 127.0.0.1:9000
pm = static
pm.max_children = 4  ; adjust to your VM resources
request_slowlog_timeout = 20s
slowlog = /srv/<serviceuser>/<project>/var/log/fpm.log.slow
user =  SERVICE_USER
```

Start a FPM process using your configuration:

```
php-fpm -y /srv/<serviceuser>/<project>/etc/fpm.conf
```

:::{note}
For a reliable service setup you should install a dedicated
process manager like [supervisord] to start and monitor your FPM processes. An
example setup to start with can be found in the section
{ref}`process-management`
:::

FPM provides a FastCGI server you can connect to using any FastCGI capable
webserver, for example nginx {file}`/etc/nginx/local/{PROJECT}.conf`:

```
upstream fpm {
    server localhost:9000;
}

server {
    listen FRONTEND_IP:80 default_server;

    proxy_intercept_errors on;

    root /srv/<serviceuser>/<project>/htdocs;
    index index.php index.html index.htm;
    autoindex off;

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_pass fpm;
    }
}
```

:::{note}
We do not recommend to use Apache as a FastCGI frontend server.
:::

% vim: set spell spelllang=en:

[supervisord]: http://supervisord.org/
