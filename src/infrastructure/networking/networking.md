% last review: 2023-02-22

% review schedule: 1 year

% ISMSControl: A.13.1.3


(networking-overview)=

# Overview

## Physical networks

The physical network in our public datacenter RZOB is implemented using
physically separated switches per layer 2 segment (VLAN) with a hot-spare for
each switch type. In WHQ, we operate multiple layer 2 segments using the same
physical switches, using VLANs within the switches for logical separation, but
with cold-spares instead of hot-spares.

The frontend (FE) and server-to-server (SRV) networks run on 1G infrastructure,
whereas the storage networks are connected with 10G links. In RZOB our routers
have redundant 2x10G connectivity to our uplink provider. In WHQ our routers
have a redundant 2x1G link to our uplink provider, however this provider only
has *non-redundant* 2.5G connectivity itself.

In all locations, routers are connected to the datacenter uplink, the frontend
network, the server-to-server network, and the management network. In RZOB a
dedicated physical interface is used for each of these networks. In WHQ, all of
these networks are delivered over a single physical interface using tagged
VLANs.

(logical-networks)=

## Logical networks

```{image} logical.png
```

The following VLANs and logical networks are in use:

**MGM** - Management, purely for administrative purposes. This VLAN connects
switch management ports, Remote Access Controllers, and additional access to
server OSes via SSH. Not accessible from the outside world, private IPv4
address space.

**FE** - Frontend, for customer application traffic. This VLAN connects to
machines that provide customers' applications to the public. This network is
switched to the virtual machines and leverages completely public traffic. The
DC firewalls do not filter this. Customer applications are free to use any
ports they like but must be careful opening them. VMs can filter this network
locally. All VMs receive a NIC on this VLAN but not necessarily IPv4 or IPv6
addresses if they do not provide public traffic. DNS
example: *vm00.fe.rzob.gocept.net*.

**SRV** - Server to server communication. Used for customer application
components to talk to each other, e.g. database traffic and for management
purposes on the application level. This network is firewalled from the internet
at our DC edge firewalls and allows only HTTP/S and SSH traffic. Additionally
VMs can filter this traffic locally and only allow arbitrary traffic from VMs
belonging to the same project by default. This network is used on all VMs and
has IPv4 (usually private) and IPv6 addresses allocated automatically.
DNS example: *vm00.srv.rzob.fcio.net* or simply
*vm00.fcio.net*.

**STO** - Storage communication. Used by the virtualization and backup servers
to access the network storages where the VM disk images as well as object
storage gateways (RadosGW) are located. DNS example: *filer.sto.rzob.gocept.net*.

**STB** - Storage backend communication. Used by the storage layer for
replication and self-management. DNS example: *filer.stb.rzob.gocept.net*.

Individual VMs that run management services, like monitoring, may get bridged
into the additional VLANs or granted firewall exceptions as necessary.

The routers suppress routing of traffic on VLANs that are "martian", e.g.
frontend traffic injected on the server-to-server network or private addresses
from the internet.

Services that require tight control are bound to listening IP addresses on only
those networks but then can get relaxed ACL rules making configuration simpler
and easier to understand.

## Local ports

Your application is generally free to use any open port on a machine above 1024.
Especially if you run a component that has a registered, well-known port, please
use that.

However, custom applications may run into the trouble of colliding with other
components. For that we guarantee that the ports 61000-61999 will never be used
by our managed components, nor by the kernel when assigning dynamic ports.
