.. _firewall:

Firewall
========

Network security at the Flying Circus is based on two key concepts:

* Traffic separation through different networks (:abbr:`VLAN (virtual local area
  network)` classes).
* Two levels of firewalling: location firewall, machine firewall.

See :ref:`virtual_networks` for a explanation of our VLAN classes.

Location firewall
-----------------

A location firewall provides perimeter security for a data center location.
This firewall cannot be influenced from individual VMs.

A location firewall ensures different access policies for different VLAN
classes:

fe
  Frontend traffic is generally not filtered. It is the duty of machine
  firewalls and application security mechanisms to prevent unauthorized access.
  However, VMs running in :ref:`strict-firewall-mode` block all incoming **fe**
  traffic on their machine firewall by default.

srv
  Outbound connections are generally allowed from srv addresses. Connections
  from private addresses are masqueraded.

  Inbound traffic gets blocked with exceptions for ports:

  * 22/tcp (SSH) for remote shell access.

  * 80/tcp (HTTP) for web statistics access. [#fn1]_

  * 123/udp (NTP) for time synchronization.

  * 443/tcp (HTTPS) for web statistics access. [#fn1]_

  * 5666/tcp (Nagios NRPE) for inter-site monitoring.

mgm
  No connectivity to the public Internet. However, we allow access for
  adminstrator from internal networks and via :abbr:`VPN (virtual private
  network)` connections.

sto, stb
  No connectivity to the public Internet.


Machine firewall
----------------

Each VM is equipped with its own firewall. The machine firewall is policing only
incoming connection attempts, outgoing connections are not restricted. The
following list describes the default configuration. Service deployments may
install additional firewall rules (see below at :ref:`custom-firewall-rules`).
Custom firewall rules may both open additional ports and reject connections to
ports which are opened by the default policy.

.. note::

   Default policy items marked as *non-overridable* cannot be altered by
   custom firewall rules.

srv
  Incoming connections are blocked except for:

  * 22/tcp (SSH) for remote shell access (*overridable*, but *non-overridable*
    from FCIO admin networks).

  * 80/tcp (HTTP) for web statistics access (*overridable*). [#fn1]_

  * 123/udp (NTP) for time synchronization (*non-overridable*).

  * 443/tcp (HTTP) for web statistics access (*overridable*). [#fn1]_

  * 5666/tcp (Nagios NRPE) for inter-site monitoring (*non-overridable*).
    [#fn1]_

  * All ports: connections originating at machines from the same resource group.
    These are generally allowed (*overridable*).

fe
  Firewall policy depends on the firewall mode: all ports are either open or
  closed by default. See below.


.. _open-firewall-mode:

"Open" firewall mode
~~~~~~~~~~~~~~~~~~~~

If a resource group is in *open* firewall mode, connections to all ports on
**fe** are allowed by default on each machine. Access to server applications
depends solely on the interface on which an application opens a port: **fe** for
public access, **srv** for intra-RG access.

.. _strict-firewall-mode:

"Strict" firewall mode
~~~~~~~~~~~~~~~~~~~~~~

If a resource group is in *strict* firewall mode, connections to ports on **fe**
are denied by default. Server applications must install a custom firewall rule
in addition to opening a port.

.. note::

   Some roles (for example, :ref:`nixos-webgateway`) pre-package firewall
   rules to allow access on their standard ports automatically. See individual
   roles documented in :ref:`platform-nixos` for details.

New resource groups have an *open* firewall mode by default. Contact our
:ref:`support` to get a resource group switched into *restricted* firewall mode.


.. _custom-firewall-rules:

Adding custom firewall rules
----------------------------

How to add custom firewall rules depends on the platform of your VM:

* :ref:`Gentoo <gentoo-firewall>`
* :ref:`NixOS <nixos-firewall>`


.. [#fn1] These rules are only necessary for Gentoo-based VMs. They are likely
   to disappear in the future.


.. vim: set spell spelllang=en:
