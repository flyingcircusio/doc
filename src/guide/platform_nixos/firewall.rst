.. _nixos-firewall:

Firewall
========

On NixOS, our general firewall rules apply with a slight deviation:
access is limited by default and can be enabled on a per-case basis.

You are free to open any port you like on the frontend network (``ethfe``) which
will be accessible to the outside world. The server-to-server network is only
accessible in a limited way from the outside and freely to the machines
in the same project.

To add custom rules, you can place configuration files in
:file:`/etc/local/firewall/*`. Upon the next config activation all files placed
there will be concatenated and placed in a late stage of the firewall
configuration.

The files are shell scripts and are intended to be very simple. We check
that all lines are either:

* comments (starting with #)
* invocations of an iptables command (iptables, ip6tables, ip46tables)

Here's an example:

.. code-block:: bash

    # Enable port 1234 to be accessed on the frontend network via
    # IPv4 and IPv6
    ip46tables -A nixos-fw -i ethfe -p tcp --dport 1234 -j nixos-fw-accept


.. note:: NixOS has a few special firewall chains that support good re-use
    of reject/logging and others. You should definitely use the ``nixos-fw``
    chain instead of the regular ``INPUT`` chain to avoid unpredictable
    behaviour.

After making changes to the firewall configuration, either wait for the
agent to apply it or run ``sudo fc-manage --build``.
