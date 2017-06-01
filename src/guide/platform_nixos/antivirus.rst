.. _antivirus_nixos:

Antivirus
=========

Installs the `ClamAV`_ virus checker and infrastructure to update virus
signatures regularly.

.. _ClamAV: http://www.clamav.net

Components
----------

* clamd - antivirus daemon
* clam(d)scan - command line virus checker
* freshclam - signature update service

Interaction
-----------

Use :command:`clamdscan` to pass files to the scanning daemon or talk directly
to it via `libclamav`.

.. vim: set spell spelllang=en:
