.. _service_setup:

Service setup
=============

Finally, you have to setup the platfom services to serve your Django
application.



nginx
-----

As a service user create a nginx config
:file:`/etc/nginx/local/django-mysite.conf` to serve the Django application::

   upstream @django {
       server localhost:8000;
       keepalive 10;
   }

   server {
       listen IPv4_FE_ADDRESS:80 default_server;
       listen [IPv6_FE_ADDRESS]:80;
       server_name www.example.com example.com;

       # Redirect to canonical host name (makes URLs unique).
       if ($host != $server_name) {
           rewrite . $scheme://$server_name$request_uri redirect;
       }

       location / {
           proxy_pass http://@django;
       }
   }

Further common configuration options can be found in
:file:`/etc/nginx/local/example-configuration`. Please note that an nginx
configuration file must end with `.conf` to get included.

Reload nginx::

   sudo /etc/init.d/nginx reload

See the :ref:`webgateway` role documentation for further details.


Log rotation
------------

Create a snippet :file:`/var/spool/logrotate/SERVICE_USER` with
:program:`logrotate` configuration like the following example::

   /srv/SERVICE_USER/myproject/log/*.log {
      postrotate
         /srv/SERVICE_USER/myproject/bin/supervisorctl restart all
      endscript
   }

The log rotation will be invoked every night. The :manpage:`logrotate(8)`
man page documents available options. A set of standard options (like *compress*
and *dateext*) will get applied automatically; see
:file:`/etc/logrotate.options` for reference.

.. vim: set ft=rst:
