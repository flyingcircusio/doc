.. _network-security:

Network security
================

Network security is handled on different levels depending on the class of
traffic. The different classes are separated by VLANs and protected from
Internet traffic by a firewall on the gateway in a Flying Circus location.

Frontend network (fe)
---------------------

Nodes providing services intended for the general public (users of
applications hosted within the Flying Circus) have one or more IPv4/IPv6 addresses in
this network.

Traffic to addresses in this network is freely allowed by the gateway
firewall.

Customers should only bind services to this IP address that are intended to be
accessed from the internet. Backend services should be bound to the server
network.

Server network (srv)
--------------------

All nodes have an address in the server network. This is used by applications
for internal communication, e.g. application servers communicating with their
database.

IPv4 and IPv6 addresses in this network are public and routed from the
internet.

Access from the internet is available into this network but limited to SSH (TCP
port 22) and select additional services like web server statistics (TCP port 80
and 443).

Storage network (sto)
---------------------

This network is used for SAN traffic (mainly for storage servers to provide
the iSCSI volumes to KVM hosts or the backup service).
It is only accessible to ring 0 machines owned by the Flying Circus but not
customer-owned equipment or virtual machines.

This network uses private IPv4 addresses that are not routed from the
internet. Traffic from outside this network is not allowed.

Management network (mgm)
------------------------

This network is used for management purposes only: access to base management
controllers (IPMI), switch consoles etc.

It uses private IPv4 addresses that are not routed from the internet. Traffic
from outside this network is not allowed.
