.. _setup_database:

Setup database
==============

Change to your service user context.::

   $ sudo -iu SERVICE_USER

Service users are allowed to change into the postgres user context.::

   $ sudo -iu postgres

Create PostgreSQL role
----------------------

To access a database from the application we need to create a PostgreSQL role.::

   $ createuser -DRSEP django

Create PostgreSQL database
--------------------------

Afterwards we create a database for the application.::

  $ createdb -O django django

Test database connection
------------------------

Exit the postgres user context and test the database connection.::

  $ exit
  $ psql -h localhost -U django -d django
