.. _storage:

Storage
=======

Terminology
-----------

Disk quota
	Restriction of usable disk space. The function of using disk quotas is to allocate limited disk space.
Nagios
	A monitoring and alerting service for servers


:ref:`platform-gentoo`
``````````````````````

It's possible to grow the disk to the desired size. Unfortunately this isn't the case for shrinking the disk. After resizing the disk to a smaller size we don't change anything about the machine configuration itself but inform the nagios checks about the new disk size. Using tools like **df** or **lsblk** won't reflect those changes.

:ref:`platform-nixos`
`````````````````````

Growing the disk works the same as on our Gentoo based plattform. Shrinking is realized by changing the allowed disk quota. Changes in the quota rules are reflected by command line tools and hence should no longer lead to confusion by the user.


Hands-On
--------

Showing the size of the root-partition. *Hint: Currently only useful on NixOS*

.. code-block:: console

   $ lsblk -n --output SIZE /dev/disk-by-label/root