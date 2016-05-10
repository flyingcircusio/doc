.. _box:

=======
The Box
=======

The box is a special temporary disk space in the Flying Circus that can be used
to perform administrative tasks that require a lot of disk space temporarily
and to move data between VMs and resource groups securely and conveniently.

.. contents::
    :local:
    :depth: 2

Meet your box
=============

Every user sees the box in his home directory on every VM that he has access to::

    $ ssh bob@myapp00.gocept.net
    bob@myapp00 ~ $ ls
    box

The box is a shared network filesystem and any changes become visible on all
other VMs immediately: put a file in it, change it, or delete it, and all other
clients will be able to see the change right away.

Use your box securely
=====================

The ``box grant`` command allows you to perform certain ownership and mode
operations that would otherwise be accessible to root users only.

.. warning::

  Using the box without the box command will make no special adjustments to
  file permissions. Your files may be readable by all users on all machines
  that you have access to.


Private access
--------------

Run ``box grant private`` to make a directory only accessible to your user (no
other group and not world-readable)::

    bob@myapp00 ~ $ ls box
    bob@myapp00 ~ $ box grant private my-private-dir
    bob@myapp00 ~ $ ls -lah ~/box
    drwx------   2 bob  users    68B May  8 12:53 my-private-dir

Public access
-------------

If you want a directory to be available to any user on any of the VMs you have
access to, then you can run the ``box grant public`` command::

    bob@myapp00 ~ $ ls box
    bob@myapp00 ~ $ box grant public my-public-dir
    bob@myapp00 ~ $ ls -lah ~/box
    drwxr-xr-x   2 bob  users    68B May  8 12:53 my-public-dir

Bouncing between service users and machines
-------------------------------------------

Service users do not have their own box and in some cases you will need to move
data between different service users and different resource groups.

For that you can use your own box and the ``box grant`` command to "bounce"
data around. Lets say we want to make a database dump and move it from myapp01
to yourapp02 and switch service users from "myapp" to "yourapp" at the same
time.

Lets create a directory for the service user that creates the dump first::

    $ ssh bob@myapp00
    bob@myapp00 ~ $ box grant myapp db-dump
    bob@myapp00 ~ $ ls -lah ~/box
    drwx------   2 myapp  service    68B May  8 12:53 db-dump

Now dump the data::

    bob@myapp00 ~ $ sudo -u myapp -i
    myapp@myapp00 ~ $ pg_dump myapp-db > /home/bob/box/db-dump/dump.sql

And log in to the other machine::

    myapp@myapp00 ~ $ ^D
    bob@myapp00 ~ $ ^D
    $ ssh bob@yourapp00

Grant permissions to the service user that will load the database::

    bob@yourapp00 ~ $ ls ~/box
    drwx------   2 1382  service    68B May  8 12:53 db-dump
    bob@yourapp00 ~ $ box grant yourapp db-dump
    bob@yourapp00 ~ $ sudo -u yourapp -i
    yourapp@yourapp00 ~ $ psql yourapp < /home/bob/box/db-dump/dump.sql

And finally assume ownership yourself and delete the data::

    yourapp@yourapp00 ~ $ ^D
    bob@yourapp00 ~ $ box grant private db-dump
    bob@yourapp00 ~ $ rm -rf ~/box/db-dump

Instead of deleting the data you could also leave it there and wait for the
automatic cleanup to delete it after a day. However, it is good behaviour
to clean up after yourself to allow other users to use the unneeded space.

For more information on the ``box`` command check the manpage with ``man box``
on your VM.

Rules
=====

* The Box is provided free of charge.

* A fair-use policy applies.

* We provide a certain amount of disk space that may be
  used by everyone that we will adjust over time to keep
  the box useful.

* We do not guarantee a given amount for free space for
  anyone at any given time.

* We do not perform backups of the box.

* Files are kept for 24 hours and then deleted on the
  server side.

* Do not build applications that rely on the box at runtime. It is intended
  for temporary, ad-hoc administrative tasks only.
