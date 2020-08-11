.. _nixos2-lamp:

LAMP (Apache/mod_php)
=====================

The LAMP role starts a managed instance of Apache with ``mod_php`` that can be used
to easily run a production-ready PHP application server.

.. note::

	The Apache configured by this role does not bind / open firewall ports to the
	frontend network automatically. It is not intended to serve applications
	directly to consumers but should be placed behind a :ref:`webgateway
	<nixos2-webgateway>`.

.. note::

	An alternative route for running PHP applications that we support is the
	use of nginx with PHP-FPM. However, those setups are a bit more elaborate
	and less widely used in the PHP community. They also do not support
	``.htaccess`` files.

Configuration
-------------

docroot (required)
~~~~~~~~~~~~~~~~~~

The Apache server is fully pre-configured to serve your application to the 
load balancer and you only need to point it to the docroot of your application.

Apache looks for the docroot in :file:`/etc/local/lamp/docroot` which is expected to be a symlink to the actual location where you placed you PHP code, typically in the home directory of a service user.

Assuming that you are placing your PHP code to :file:`/srv/s-myservice/code/docroot/` then you configure the PHP root by running:

.. code-block:: console

	$ sudo -i -u s-myservice
	$ cd /etc/local/lamp
	$ ln -s /srv/s-myservice/code/docroot docroot
	$ sudo fc-manage -b

apache.conf
~~~~~~~~~~~

No Apache configuration is required by default. However, you can put a file with Apache configuration in :file:`/etc/local/lamp/apache.conf` and it will be appended to the platform-generated Apache config.

php.ini
~~~~~~~

We deliver a production-tested PHP configuration that you can extend by placing additional configuration instructions in :file:`/etc/local/lamp/php.ini`.

PHP version and modules
~~~~~~~~~~~~~~~~~~~~~~~

We currently provide a single pre-selected version of PHP (7.3) with a fixed set of modules. Please contact our support if you need a different version of PHP and/or further modules.

Interaction
-----------

No special interaction is required. Changes to the configuration need to be
activated as usual using:

.. code-block:: console

	$ sudo fc-manage -b

Network
-------

The Apache server listens on the :ref:`srv interface <logical_networks>` only.

Security
--------

* Apache runs in a separate user who is a member of the ``service`` group and 
  thus can (by default) access files owned by service users.

* Access is read-only for apache by default, but you can grant write access
  for directories by running :command:``chmod g+rwsx`` on the directory.

Debugging
---------

To assist with debugging we have integrated the `Tideways application performance monitoring <https://tideways.com/>`_ daemon and PHP module by default.

To enable it, you just have to place your Tideways API key in :file:`/etc/local/lamp/php.ini`:

.. code-block:: console

   $ echo "tideways.api_key=<secretapikey>" >> /etc/local/lamp/php.ini
   $ sudo fc-manage -b

Logging
-------

Apache logs are available in :file:`/var/log/httpd`.

PHP output is accessible through the journal, running :command:`journalctl -t php -t httpd`.


Monitoring
----------

Our platform monitoring checks that Apache is running (through systemd) and verifies that the Apache statuspage (mod_status accessible via :command:`curl http://localhost:8001/server-status`) is available.
