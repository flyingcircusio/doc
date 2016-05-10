.. _install-application:

Install application
===================

Change to your service user context.::

   $ sudo -iu SERVICE_USER

Virtualenv
----------

To install Python applications in a controlled environment, you can use
:program:`virtualenv`. :program:`virtualenv` is already installed system-wide
on VMs.::

   $ cd myproject
   $ virtualenv --python=python2.7 .
   New python executable in myproject/bin/python2.7
   Also creating executable in myproject/bin/python
   Installing setuptools............done.
   Installing pip...............done.


Buildout
--------

We recommend to ship your application using `buildout`_. To do so, first
download Buildout's :file:`bootstrap.py`::

   $ wget http://downloads.buildout.org/2/bootstrap.py

Create a :file:`buildout.cfg`::

   [buildout]
   parts = django
   versions = versions

   [versions]
   Django = 1.5.5

   [django]
   recipe = djangorecipe
   eggs = psycopg2
   settings = production
   project = mysite


Install
-------

Use *Buildout* to install Django.::

   $ ./bin/python bootstrap.py
   $ ./bin/buildout


Setup application
-----------------

The follwing steps are Django related and may differ depending on your
application.

Adjust :file:`mysite/settings.py`::

   [...]
   DATABASES = {
       'default': {
           'ENGINE': 'postgresql',          # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
           'NAME': 'django',                # Or path to database file if using sqlite3.
           'USER': 'django',                # Not used with sqlite3.
           'PASSWORD': 'YOUR_PG_PASSWORD',  # Not used with sqlite3.
           'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
           'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
       }
   }
   [...]
   ALLOWED_HOSTS = ['your.domain.example.com']

Initialize the database::

   $ ./bin/django syncdb

Test the app to start successfully.::

  $ ./bin/django runserver 8000

.. _buildout: http://www.buildout.org
