.. _infrastructure-storage:

Storage
=======

VM storage is provided by a Ceph cluster. Each block device visible in VMs
(e.g., :file:`/dev/vda` or :file:`/dev/sda`) reflects an underlying Ceph `RBD
volume`_.

.. _RBD volume: http://docs.ceph.com/docs/master/architecture/

Disk Layout
-----------

Each RBD volume contains a complete virtual disk image consisting of a partition
table and one or more filesystems. We use both XFS and ext4 filesystems in VMs.


Growing and shrinking disks
---------------------------

Such a virtual disk is quite easy to grow but not so easy to shrink.

When *growing* a virtual disk, we enlarge the underlying RBD volume, adapt the
partition table and resize the main filesystem. This procedure is fully
transpart and can be performed without downtime.

*Shrinking* a virtual disk is not directly supported. On customer request, we
install a filesystem quota to ensure that no more space is used than booked. On
newer NixOS VMs with XFS filesystems, tools like
:command:`df` report that reduced size correctly. Older Gentoo-based VMs
with ext4 filesystems are not so smart; :command:`df` still
reports the old size even when a quota is installed.  Nonetheless, we will
monitor disk usage on basis of the reduced disk size.
