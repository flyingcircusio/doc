.. _nixos2-local:

Local configuration
===================

You can customize the system's configuration for managed components with
config files that are located in  :file:`/etc/local/*`.

Every component that supports customizing its configuration creates a directory
such as :file:`/etc/local/firewall`. The specific format and allowed filenames
depend on the specifics of each component and are documented separately.

Changes to the files in the local configuration directory are picked up
automatically upon the next run of our configuration agent (generally every
10 minutes) but you can also explicitly trigger it by running:

.. code-block:: console

  $ sudo fc-manage --build

This will update the machine's system configuration, which includes copying the
local configuration files into the Nix store. Your custom config is thus
versioned along the general system config (in case we have to revert to an
older configuration version) and is atomically loaded and activated.

To inspect the result of this call, you can check the journal:

.. code-block:: console

  $ journalctl --since -1h --unit fc-manage
