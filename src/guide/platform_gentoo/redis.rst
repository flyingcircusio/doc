:Publish Date: 2012-06-04

.. _redis-server:

Redis
=====

Runs a `Redis <http://redis.io>`_ database server. The server listens on the
*srv* interface on port 6379.


Components
----------

* Redis


Configuration
-------------

The Redis configuration is fully managed and located in
:file:`/etc/redis.conf` and :file:`/etc/conf.d/redis`. Currently, the
configuration is mostly as provided by the upstream defaults.

The authentication password is automatically generated upon installation
and can be read by service users. It can be found in :file:`/etc/redis.conf` by
searching for :command:`requirepass`.


Interaction
-----------

Interaction with the server happens only in-band using the Redis commands.
Please make sure to authenticate yourself by sending the :command:`AUTH` command
followed by the authentication password before sending any other commands.


Monitoring
----------

We monitor by default:

* whether exactly 1 :command:`redis-server` process is running
* whether the TCP port is reachable

.. vim: set spell spelllang=en:
