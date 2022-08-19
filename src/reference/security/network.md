.. _network-security:

Network security
================

Network security is handled on different levels depending on the class of
traffic. The different classes are separated by VLANs and protected from
Internet traffic by a firewall on the gateway in a Flying Circus location.

VLAN classes and gateway firewall
---------------------------------

Frontend network (fe)
~~~~~~~~~~~~~~~~~~~~~

Nodes providing services intended for the general public (users of applications
hosted within the Flying Circus) have one or more IPv4/IPv6 addresses in this
network.

Traffic to addresses in this network is freely allowed by the gateway
firewall.

Customers should only bind services to this IP address that are intended to be
accessed from the internet. Backend services should be bound to the server
network.

Server network (srv)
~~~~~~~~~~~~~~~~~~~~

All nodes have an address in the server network. This is used by applications
for internal communication, e.g. application servers communicating with their
database.

Server networks use a mixture of public and private IP addresses. Outbound
traffic is generally possible and will be masqueraded on the gateway firewall if
necessary.

Inbound traffic will be blocked on the gateway firewall with the following
exceptions:

* 22/tcp (ssh)
* 80/tcp (http)
* 443/tcp (https)
* 5666/tcp (nrpe)
* 8140/tcp (puppet)

Ports 80 and 443 are for backend web services like access statistics and are
expected to be turned off in the future.

Storage network (sto)
~~~~~~~~~~~~~~~~~~~~~

This network is used for SAN traffic (mainly for storage servers to provide
the iSCSI volumes to KVM hosts or the backup service).
It is only accessible to ring 0 machines owned by the Flying Circus but not
customer-owned equipment or virtual machines.

This network uses private IPv4 addresses that are not routed from the
internet. Traffic from outside this network is not allowed.

Management network (mgm)
~~~~~~~~~~~~~~~~~~~~~~~~

This network is used for management purposes only: access to base management
controllers (IPMI), switch consoles etc.

It uses private IPv4 addresses that are not routed from the internet. Traffic
from outside this network is not allowed.


Machine firewall
----------------

