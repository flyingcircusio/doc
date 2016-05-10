.. _nixos-logrotate:

Logrotate
=========

To rotate log files that are growing in service user directories, drop custom
logrotate.conf snippets into :file:`/etc/local/logrotate/{USER}`. This service
is automatically enabled for all service users.

See :file:`/etc/local/logrotate/README.txt` for details.
