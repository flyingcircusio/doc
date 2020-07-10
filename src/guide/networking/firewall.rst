.. _firewall:

Firewall
========

Concept
-------

We rely mainly on the separation of different VLANs. Firewalls provide
exceptions to the rules. This results in a rather small firewall ruleset which
is easy to understand.

The main decision about access control is expressed by the choice of the
interface(s) application bind to. If an application opens a port on the *fe*
interface, public access is assumed. If an application opens a port on the *srv*
interface, restricted access is assumed.


Restrictions on the *srv* network
---------------------------------

Only few connections from the public internet to ports on the *srv* network
can be opened by default. Machines inside the same project may access the
*srv* ports of their RG peers freely.

Currently we allow public access for:

* SSH (22) - to provide login access to VMs
* HTTP/HTTPS (80/443) - providing access to managed component features, like awstats
* NTP (123) - to synchronize clocks with outside hosts

Managed components that are installed on a machine may provide additional
firewall exceptions (either for public or data center-internal traffic), for
example:

* Grafana (statshost) opens ports 2003 and 2004.
* VxLAN/OpenVPN servers open several ports depending on their configuration.


.. _custom-firewall-rules:

Adding custom firewall rules
----------------------------

How to add custom firewall rules depends on the platform of your VM:

* :ref:`NixOS <nixos2-firewall>`
* :ref:`Gentoo <gentoo-firewall>`


.. vim: set spell spelllang=en:
