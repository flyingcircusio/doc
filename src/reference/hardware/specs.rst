:Publish Date: 2013-06-13

.. _hardware-specs:

Hardware specifications
=======================

All hardware we procure for our infrastructure will comply to the following
specifications. Older hardware may have been bought adhering to former
versions of the specification and will be upgraded over time and as necessary.

Housing customers' equipment also needs to comply to the specification valid
at the time of installation.

Servers
-------

All servers, independently of their role, require:

* 4 physical gigabit network ports (Intel chips)
* OS disk: 2x256 internal SSD (e.g. via M2)
* BMC supporting IPMI 2.0 with serial console via LAN on shared port
* Redundant power supply
* Needs to be bootable from USB flash drive
* PCIe bus
* Sliding rack rails
* Support contract for at least 5 years (next business day, parts
  included)
* Bootable, built-in rescue system

Application servers
~~~~~~~~~~~~~~~~~~~

* Base: Thomas Krenn RI2208
* 256 GiB RAM
* at least 12 physical cores with good thread performance (2x Intel Xeon E5-2643v3 6-core 3.4GHz)
* CPU flags: vmx, constant_tsc
* 1 port 10GBit copper (Intel 10 Gigabit X540)
* Machine name: kyleXX

Storage servers
~~~~~~~~~~~~~~~

* Base: Thomas Krenn RI2224
* 24 slots for hard drives
* at leat 16 cores with sufficient thread performance (2x Intel Xeon E5-2640v3 8-Core)
* 128 GiB RAM
* a number of 1TB SATA 2.5" disks
* for every 7 1TB SATA disks, 1 200GiB DC S3710
* alternatively a number of Intel DC S3610 drives for SSD-based storage
* 2 10GBit copper (Intel 10 Gigabit X540)
* code name: cartmanXY

Backup servers
~~~~~~~~~~~~~~

* Base: Thomas Krenn RI1316
* No separate drives for system needed, it's OK to install on the big raid.
* High-end hardware RAID controller (Avago MegaRAID 9361-8i SAS3 8x internal) including safe controller cache
* at least 15 x 2 TB SAS 7.2k disks, depending on actual requirements.
* at least 12 GiB RAM
* at least 4 processor cores
* 1 port 10GBit copper (Intel 10 Gigabit X540)
* code name: barbradyXY

Routers
~~~~~~~

* at least 4 GiB RAM
* Power saving CPU
* code name: kennyXY

Network infrastructure
----------------------

Switches
~~~~~~~~

* Recommended models: HP ProCurve 2530-(24/48)G
* usually at least 48 10/100/1000 ports (in some cases we require fewer
  ports, so a 24 port model is acceptable in that case)
* at least 2 ports for optional fibre uplinks
* code name: stanXY

Cabling
~~~~~~~

* Use Cat6
* Respect color coding
