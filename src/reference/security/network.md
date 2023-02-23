% last review: 2023-02-22

% review schedule: 1 year

% ISMSControl: A.13.1.1

(network-security)=

# Network security

Network security is handled on different levels depending on the class of
traffic. The different classes are separated by VLANs and protected from
Internet traffic by a firewall on the gateways in a Flying Circus location.

## VLAN classes and gateway firewall

### Frontend network (fe)

Nodes providing services intended for the general public (users of applications
hosted within the Flying Circus) have one or more IPv4/IPv6 addresses in this
network.

Traffic to addresses in this network is forwarded by the gateway firewall
without limitations.

Customers should only bind services to those IP addresses that are intended to
be accessed from the internet. Backend services should be bound to the server
network.

### Server network (srv)

All nodes have an address in the server network. This is used by applications
for internal communication, e.g. application servers communicating with their
database.

Machines on the server network generally use private IPv4 addresses and public
IPv6 addresses. Older machines may use public IPv4 addresses for historic
reasons.  Outbound traffic is generally allowed and will be masqueraded on the
gateway firewall if necessary. If a machine needs unmasqueraded access to the
internet ensure to provision an IP address on the frontend network.

Inbound traffic will be blocked on the gateway firewall with the following
exceptions:

- 22/tcp (ssh)
- 80/tcp (http)
- 443/tcp (https)
- 5666/tcp (nrpe)
- 8140/tcp (puppet)

All those ports - except SSH - are required only for historic reasons. They are
not used by newer VMs and will be blocked at some point in the future.

### Storage network (sto and stb)

This network is used for storage traffic (Ceph RBD for KVM hosts and backup
servers as well as S3-compatible storage via the Rados Gateway). It is only
accessible to ring 0 machines owned by the Flying Circus but not customer-owned
equipment or virtual machines. Customer-owned environments implement separate
storage networks.

This network uses private IPv4 addresses that are not routed from the internet.
Traffic from outside this network is not allowed.

### Management network (mgm)

This network is used for management purposes only: access to base management
controllers (IPMI), switch consoles, machine OSes etc.

It uses private IPv4 addresses that are not routed from the internet. Traffic
from outside this network is not allowed.

## Machine firewall

Every machine is running an additional local firewall using
iptables/nftables and will by default

* block all traffic to the frontend IPs, except when explicitly opened by a
  configured service, and
* block all traffic to the server-to-server IPs, except for VMs from the same
  resource group.
