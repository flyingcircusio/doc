.. image:: ../../images/vms250.png
   :class: logo
   :width: 250px



****************
Virtual machines
****************


.. toctree::
    :hidden:

    box


* VMs are run on Linux KVM hypervisors.
* The guest operating system is a 32-bit Gentoo Linux managed by the Flying Circus.

    * Packages are installed through the managed components. If you require something special you are free to compile it in your service users' home.
    * We are always looking for more components to manage for you but as a general rule new managed components take their time to develop them. Contact our support if you would like to make a wish.
* VMs can be assigned resources:

    * 1-8 CPUs
    * 256MiB-60GiB RAM (note the 32-bit per process memory limit of 3GiB)
    * 5GiB-10+TiB disk (note that filesystems become unwieldy at a certain size)
* Resources can be resized:

    * CPU and RAM changes currently require a reboot of the VM.
    * Disks can be increased on the fly without a reboot. Disk decreases require a reboot.

* Virtual disks are stored in CEPH RBD volumes.


Maintenance
-----------

For every project maintenance is by default configured between 22:00 and
5:00 with a pre-announcement period of 24 hours. When our tools notice that
maintenance is required they will automatically pick a window matching the
configured limits and notify the technical contacts.

Reboot
------

Automated reboots are announced according the maintenance guidlines. Users
granted with sudo-srv permissions are able to reboot a VM by calling::

  sudo shutdown -r now

Deletion
--------

VMs are deleted in a multi-stage process that takes around 38 days. You can
schedule the deletion of a VM at earliest for the next day (midnight
Europe/Berlin).

The stages of deletion are:

Prepare
  (t-5 days)

  Create a maintenance period to let technical contacts know that a VM
  is due for deletion soon.

  Also, add downtimes in our monitoring systems to stop any alerts related
  to the VM starting from their deletion date.

Soft
  (at t=0)

  Shutdown the VM but keep all existing records, IPs, disks, etc.

  At this point you can still cancel the deletion and start up the VM as it was
  including all persistent data.

Hard
  (t+3 days)

  Delete the VMs hard disk from activate storage.

  Also delete all records from our directory and allow the IPs to be reused.

Purge
  (t+8 days)

  Delete the VMs backups.

Recycle
  (t+38 days)

  Delete the VM deletion notice which will in turn allow the VMs name to
  be used again.
