(outbound)=

# Outbound connectivity from VMs

How outbound connectivity from a VM to external hosts outside of the
Flying Circus works depends on the network configuration for that VM:

- VMs can always connect to remote IPv6 destinations directly, as all
  VMs are assigned public IPv6 addresses.

- If a VM has a public IPv4 address, then it can connect to remote
  IPv4 destinations directly.

- If a VM does *not* have a public IPv4 address available, then we
  perform network address translation (NAT) on our site border
  routers, to ensure that a public address is used as the source
  address of connections outside of our network.

We use a fixed set of addresses as NAT source addresses for outbound
IPv4 connections in each location.

- **RZOB** (Production datacenter):
  - 195.62.112.82
  - 195.62.112.83
  - 195.62.112.90
  - 195.62.112.91
- **WHQ** (Backup and staging datacenter):
  - 213.187.81.2
