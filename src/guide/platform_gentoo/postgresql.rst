.. _postgresql-server:

PostgreSQL
==========

Managed instance of the `PostgreSQL <http://postgresql.org>`_ database server.


Components
----------

* PostgreSQL server

Configuration
-------------

Managed PostgreSQL instances already have a good basis configuration with
reasonable sized memory parameters (for example, `shared_buffers`, `work_mem`).
Project-specific configuration goes into
:file:`/etc/postgresql-{VERSION}/postgresql-local.conf`.


Interaction
-----------

Service users can use :command:`sudo -u postgres -i` to access the
PostgreSQL super user account to perform administrative commands like
:command:`createdb` and :command:`createuser`.

Both service users and the `postgres` DB super user may invoke ::

   sudo /etc/init.d/postgresql-${VERSION} restart

to restart the PostgreSQL server after configuration changes (replace $VERSION
with the installed PostgreSQL version).


Monitoring
----------

The default monitoring setup checks that the PostgreSQL server
process is running and that it responds to connection attempts to the standard
PostgreSQL port.


Miscellaneous
-------------

Our PostgreSQL installations have the autoexplain feature enabled by default.

.. vim: set spell spelllang=en:
