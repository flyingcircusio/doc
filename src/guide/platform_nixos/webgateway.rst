.. _nixos-webgateway:

Webgateway
==========

This role provides a stack of components that enables you to serve a web
application via HTTP. In addition, you can do load balancing and configure
failover support.

Role architecture
-----------------

The role includes of two software packages:

* the `nginx <http://nginx.org/>`_ web server
* the `HAProxy <http://www.haproxy.org/>`_ load balancer and proxy server

Both packages get a basic configuration, which can be found `here for nginx <https://github.com/flyingcircusio/nixpkgs/blob/fc-15.09-dev/nixos/modules/flyingcircus/roles/nginx.nix>`_ and `here for HAProxy <https://github.com/flyingcircusio/nixpkgs/blob/fc-15.09-dev/nixos/modules/flyingcircus/roles/haproxy.nix>`_.

In any way, you will have to add custom configuration to serve your site.

.. note:: Although we install nginx and HAProxy, there is no need to use them
   both. Since there is no connection between them w.r.t configuration, you can
   still use only one of them and leave the other one as is.

How we differ from what you are used to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is how we differ from what you already know from common Linux distributions
and how you are used to configure, start, stop and maintain these packages.

* **configuration file locations:**

  We do not edit files in `/etc/nginx/*` or `/etc/haproxy/*`, respectively.
  Since we use NixOS, files have to be edited in `/etc/local/nginx` and
  `/etc/local/haproxy/`, followed by a NixOS rebuild which copies them into the
  Nix store and activates the new configuration. To do so, run the command
  :command:`sudo systemctl start fc-manage`

* **service control:**

  We use :command:`systemd` to control processes. You can use familiar commands
  like :command:`sudo systemctl restart nginx.service` to control services.
  However, remember that invoking :command:`sudo systemctl start fc-manage` is
  necessary to put configuration changes into effect. A simple restart is not
  sufficient. For further information, also see :ref:`nixos-local`.

Role configuration
------------------

Your custom configuration goes to
:file:`/etc/local/nginx/<your_config_name>.conf` for nginx and to
:file:`/etc/local/haproxy/haproxy.cfg` for HAProxy. Please note that all
configuration has to be performed as a service user.

HAProxy
~~~~~~~

For HAProxy, you will already find a configuration file which you can change to
fit your needs. For reference, please refer to the `official documentation <http://cbonte.github.io/haproxy-dconv/configuration-1.5.html>`_.

nginx
~~~~~

For nginx, you will have to add a file yourself that contains at least one
:command:`server` block declaration as described in `the official documentation
<https://www.nginx.com/resources/admin-guide/nginx-web-server/>`_. Your files
will then be integrated with nginx' default config. Therefore, please omit
the http clause. It is already set by the default config. A structure like the
following is sufficient:

.. code-block:: console

   server {
       listen 127.0.0.1:8080;
       # The rest of server configuration
   }

.. note::

   If you configure SSL, please place your certificate files next to the config
   in :file:`/etc/local/nginx/` and use **absolute** paths to these files inside
   your configuration, e.g.:

   .. code-block:: console

      ssl_certificate /etc/local/nginx/mydomain.crt;
      ssl_certificate_key /etc/local/nginx/mydomain.key;


Debugging
---------

nginx' access logs are stored in:

.. code-block:: console

   $ ls /var/log/nginx/*.log

nginx' error logs go to systemd's journal by default. To view them, use
:manpage:`journalctl(1)` as usual, e.g.:

.. code-block:: console

   $ journalctl --since -1h --unit nginx.service
