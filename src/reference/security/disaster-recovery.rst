.. _disaster-recovery:

Disaster recovery
=================

This disaster recovery plan provides an overview of the expected disasters and
how Flying Circus systems and personnel is prepared to deal with them.

For each scenario we give:

* a preventive action
* the recovery action
* the recovery time and recovery point objective
* measures we take to prevent the scenario

Terminology
-----------

RTO
    Recovery time objective. The planned time needed between discovering a
    disaster and restoring the service.
RPO
    Recovery point objective. The point in time to which data will be
    available after recovery. Given as in "time before the disaster".

.. note::
    If recovery actions are neither self-service nor automatic then a 1 hour
    response time is included to notify the standby support technician.


Hardware errors
---------------

Loss of active network component
````````````````````````````````

Disaster prevention
    We deploy hot-standby routers, active-active redundant core switches
    and keep warm standby ports on neighbouring switches.

Disaster recovery
    Swap faulty component with standby component. This happens automatically
    for routers and manually for switches.

    Depending on the affected services higher level components' redundancies (
    storage, virtualisation) may allow faster recovery times.

    RTO for hot-standby routers: less than 15 seconds

    RTO for core switches: 0 seconds (active-active)

    RTO for access switch port failures: 1 hour

    RTO for access switch complete failures: 4 hours

    RPO: n/a

Loss of VM server
`````````````````

Disaster prevention
    We buy professional hardware with those components that are most likely to
    fail built in redundantly: multiple disks in RAID and a redundant power
    supply.

Disaster recovery
    Restart virtual machines from the failed host on spare hosts.

    RTO: within customer-specific SLA + 15 minutes

    RPO: 0

Loss of storage servers covered by redundancy
`````````````````````````````````````````````

Disaster prevention
    We store all virtual machine images on a distributed storage system (Ceph)
    with n+2 redundancy. Loss of a single server can be masked transparently.

    We can loose multiple storage servers, depending on the capacity of our
    cluster. We expect to be able to loose at least 2 servers without impacting
    service or data availability.

Disaster recovery
    Ceph performs automatic recovery. Reduced I/O performance may be experienced
    during this period on virtual machines.

    RTO: 5 minutes

    RPO: 0

Loss of storage servers exceeding redundancy
````````````````````````````````````````````

Disaster prevention
    This is a multi-layered issue. In the case of loss of redundancy beyond
    automatic repair abilities requires specific diagnostics and

Disaster recovery
    Restore virtual machines from backup.

    RTO: 4 hours

    RPO: 24 hours / 1 hour [#fn1]_

Loss of server rack
```````````````````

Disaster prevention
    The most likely scenario to loose a server rack is due to overheating and
    fire. We thus pack racks loosely to allow for optimal air-flow and density
    without over-heating. Also, the data center operator employs a smoke
    detection system that allows for early detection and fire prevention.

Disaster recovery
    Buy and install new hardware, provision to new rack in data center.

    RTO: 2 weeks

    RPO: not available


Force majeure
-------------

Loss of power in the data center
````````````````````````````````

Disaster prevention
    Require redundant power lines, UPS backup, and diesel generators in the
    data center.

Disaster recovery
    Data center personnel restores power.

    RTO: n/a, covered by 3rd party 99.99% SLA

    RPO: n/a

Loss of uplink connectivity in the data center
```````````````````````````````````````````````

Disaster prevention
    The data center provides redundant uplinks to the internet together with
    separate underground cables from different directions. The data center
    also uses a highly-available routers and network.

    The Flying Circus has a service level agreement on the availability of the
    network with the data center provider.

Disaster recovery
    Data center restores connectivity

    RTO: n/a, covered by 3rd party 99.99% SLA

    RPO: n/a

Loss of data center
```````````````````

Disaster prevention
    Our data center implements a variety of security measures certified through
    the ISO 27000 family.

    RZOB: http://www.kamp.de/kamp-rechenzentrum/sicherheit.html

Disaster recovery
    Evaluate recovery of data center, if possible together with the data
    center operator.

    Alternatively find new data center and rebuild infrastructure.

    RTO: n/a

    RPO: n/a


Software errors
---------------

Filesystem corruption
`````````````````````

Disaster prevention
    We use mature file systems in our storage cluster, backup solutions and
    with the VMs which can cause inconsistencies under failure scenarios.

Disaster recovery
    Restore filesystem or missing files from backups, recreate backups in case
    of file system errors on backup systems.

    RTO: 4 hours

    RPO: 1 day/1 hour [#fn1]_

Configuration errors
````````````````````

Disaster prevention
    Leverage automated, repeatable, and version-controlled configuration systems.

Disaster recovery
    Roll back configuration changes and restore backups if data is lost.

    RTO: depends on SLA [#fn2]_

    RPO for reversible configuration changes: 4 hours

    RPO for restore: 1 day/1 hour [#fn1]_

Application errors
``````````````````

Disaster prevention
    Leverage automated, repeatable, and version-controlled application
    deployment. Leverage fully separated test/staging/production environments.

Disaster recovery
    Re-install application and restore backups if data is lost.

    RTO: depends on SLA [#fn2]_

    RPO for reinstallation: 4 hours

    RPO for restore: 1 day/1 hour [#fn1]_


User errors
-----------

Accidental single file deletion
```````````````````````````````

Disaster prevention
    Performing backups.

Disaster recovery
    Restore deleteed file from backup.

    RTO: depends on SLA [#fn2]_

    RPO: 1 day/1 hour [#fn1]_


Accidental database/directory tree deletion
```````````````````````````````````````````

Disaster prevention
    Restricting root access and performing backups.

Disaster recovery
    Restore deleted files from backup.

    RTO: depends on SLA [#fn2]_

    RPO: 1 day/1 hour [#fn1]_

.. [#fn1] RPO is 1 day for all virtual machines covered by the default backup
   schedule.  Customers can opt for a more frequent backup schedule with hourly
   backups.
.. [#fn2] Standard support reaction time is 4 hours during office hours.
   Customers may book SLAs with shorter guaranteed reaction times.
