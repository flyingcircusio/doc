.. _nixos2-mongodb:

MongoDB
=======

Managed instance of `MongoDB <https://www.mongodb.com>`_.
There's a role for each supported major version, currently:

* mongodb32
* mongodb34
* mongodb36
* mongodb40


3.2 and 3.4 are end-of-life and should be upgraded.


Configuration
-------------

MongoDB works out-of-the box without configuration.
You can put additional configuration in :file:`/etc/local/mongodb/mongodb.yaml`.
It will be joined with the basic config.

Command Line Interface
----------------------

You can use the :command:`mongo` Shell to query and update data as well
as perform administrative operations.

Upgrade
-------

Upgrade paths must include all major versions: 3.2 -> 3.4 -> 3.6 -> 4.0.

Before each upgrade step, the feature compatibililty version must be set to the
current version in the :command:`mongo` Shell, for example::

    db.adminCommand( { setFeatureCompatibilityVersion: "3.6" } )

Upgrades can be done by disabling the current role and enabling the role
for the next major version.
MongoDB will be upgraded and restarted on the next management task run.
This happens automatically or you can trigger a rebuild with
:code:`sudo fc-manage --build --directory` immediately.


Monitoring
----------

Our monitoring checks that the mongodb daemon is running.
