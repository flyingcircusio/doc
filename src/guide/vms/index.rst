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

For every resource group maintenance is by default configured between 22:00 and
5:00 with a pre-announcement period of 24 hours. When our tools notice that
maintenance is required they will automatically pick a window matching the
configured limits and notify the technical contacts.

Reboot
------

Automated reboots are announced according the maintenance guidlines. Users
granted with sudo-srv permissions are able to reboot a VM by calling::

  sudo shutdown -r now

