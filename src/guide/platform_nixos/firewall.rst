.. _nixos-firewall:

Firewall
========

On NixOS, our general firewall rules apply with a slight deviation:
access is limited by default and can be enabled on a per-case basis.

You are free to open any port you like on the frontend network (``ethfe``) which
will be accessible to the outside world. The server-to-server network is only
accessible in a limited way from the outside and freely to the machines
in the same project.

Adding custom configuration
---------------------------

To add firewall rules, you can place configuration files in
:file:`/etc/local/firewall/*`. Upon the next config activation all files placed
there will be concatenated and placed in a late stage of the firewall
configuration.

The files are shell scripts and are intended to be very simple. We check
that all lines are either:

* comments (starting with #)
* invocations of an iptables command (iptables, ip6tables, ip46tables)

After making changes to the firewall configuration, either wait for the
agent to apply it or run ``sudo fc-manage -b``.

.. note::

    You should definitely use the ``nixos-fw`` chain instead of the regular
    ``INPUT`` chain to avoid unpredictable behaviour.

How to verify
-------------

Service users may list currently active firewall rules with :command:`sudo
iptables -L`, e.g.:

.. code-block:: bash

    iptables -L -nv    # show IPv4 firewall rules w/o DNS resolution
    ip6tables -L -nv   # show IPv6 firewall rules w/o DNS resolution

If the intended rules do not show up, check the system journal for possible
syntax errors in :file:`/etc/local/firewall` and re-run
:command:`fc-manage --build`.
