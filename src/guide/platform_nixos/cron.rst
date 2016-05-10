.. _nixos-cron:

Cron
====

NixOS generally uses `systemd` which provides "Timers" as a replacement for
cron. However, for your convenience, regular cron is available on NixOS
machines.

You can edit a user's crontab with the regular commands:

.. code-block:: console

  # Edit the current user's crontab interactively
  $ crontab -e

  # Show the current user's crontab
  $ crontab -l

  # Delete the current user's crontab
  $ crontab -r

  # Replace the current crontab with the rules in <file>
  $ crontab <file>

.. note:: User crontabs are not managed within the NixOS
    configuration model: there is no versioning and no atomic loading.
