(antivirus-nixos)=

# Antivirus

Installs the [ClamAV] virus checker and infrastructure to update virus
signatures regularly.

## Components

- clamd - antivirus daemon
- clam(d)scan - command line virus checker
- freshclam - signature update service

## Interaction

Use {command}`clamdscan` to pass files to the scanning daemon or talk directly
to it via `libclamav`.

% vim: set spell spelllang=en:

[clamav]: http://www.clamav.net
