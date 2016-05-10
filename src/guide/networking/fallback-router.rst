Redundant router
================

Routers are an important resource within a location because they provide all
external connectivity for all machines to the internet.

To improve the availability of routers without expensive high-availability
hardware or rigid SLAs from our vendors we use a redundant setup where the
router role is provided by two (mostly) identical machines together with
software and configuration.

Our goal is to be able to guarantee a recovery of connectivity within
less than 4 hours.

Configuration details
---------------------

Two routers are configured with regularly allocated IP addresses for all their
VLANs (mgm, srv, fe, sto, tr).

The actual gateway addresses of the IP networks in this location are assigned
to a physical host in the directory that is not directly a puppet client. It
is usually called <location-router> (e.g. "whq-router" for the router in our
WHQ network).

The two routers use CARP
(http://en.wikipedia.org/wiki/Common_Address_Redundancy_Protocol) together
with soem handy configuration to decide which of the routers should actually
assign itself the gateway addresses.

The basic configuration is provided by the router role, with specific
configuration (IP addresses, shared passwords) being manually managed in
/etc/conf.d/ucarp.* as well as the service configuration.

When a ucarp daemon switches to backup mode it also disables the dhcpd and
radvd services. When switching to master mode it enables the dhcpd and radvd
services.

The nagios checks for the ucarp daemons and the virtual gateway addresses are
managed in the per-location monitoring code.

Manually switching master/backup routers
----------------------------------------

The master/backup role is normally automatically determined by an election
process between all possible routers.

If for some reason, this should be manually changed, then the following steps
need ot be performed:

* locate the current master and log in per SSH
* force all ucarp daemons to switch to backup state by calling `killall
  -SIGUSR2 ucarp`

Known issues
------------

Inertia
-------

Switching between routers back and forth quickly can produce somewhat
counterintuitive results: machines that are being switched to backup can
quickly assume the master back because the election process may decide that
another machine that was also recently switched to backup manually isn't a
preferred master anymore.

Uplink router ARP caching
-------------------------

In one case of switching after pulling the cable out of the master's transfer
interface we have seen the master and backup switching their role but the
remote router not giving up its ARP caching.

In this case there is the chance that pinging the remote router at the
transfer network address may force its ARP cache to be flushed for our IP but
this hasn't been verified as the situation could not be reconstructed.
