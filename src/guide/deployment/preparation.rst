.. _preparation:

Preparation
===========

Apply appropriate roles
-----------------------

To roll out managed platform components needed to run your application ask the
support to assign the appropriate roles to your VM. For a Django hosting we will
need the following roles:

webgateway
   The webgateway role provides a nginx front-end webserver and *awstats*
   statistics.

webproxy
   The webproxy role provides a *varnish* proxy to cache static content and a
   *haproxy* load balancer, if you project to run multiple application backends.

appserver
   The appserver role provides all software you need to deploy a web application,
   like *node.js*, *zope* or various version management tools.

postgresql90
   You mostly need to install a database server. For the Django
   hosting, we will rely on *PostgreSQL*

If you are going to host your application on multiple VMs, the roles can also be
spread across various VMs.

.. note:: We ask you to introduce your application when joining the Flying
   Circus. The support team is going to roll out appropriate roles for your
   special use case.

.. _service-deployment-checklist:

Gather facts
------------

To setup your application you will need to gather the following informations:

IP addresses
~~~~~~~~~~~~

Public available services should run on FE addresses. Internal network
communication, like database access or backend application servers should run on
SRV addresses.::

   $ ip address show dev ethfe
   $ ip address show dev ethsrv

.. warning:: The Flying Circus ships with a dual stack containing full IPv6
   support. Be aware not to forget to setup IPv6 for public available services.
   This is especially important for any mail server setups.

Service User
~~~~~~~~~~~~

The service user for your application is most likely identical to the name of
the project of your project.

Running services
~~~~~~~~~~~~~~~~

Since you will have to setup your application to listen on a specific port, you
should figure out which ports are used by other services.::

   $ netstat -tulpen
