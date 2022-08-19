.. _antivirus:

Antivirus
=========

Installs the `ClamAV`_ virus checker and infrastructure to update virus
signatures regularly.

.. _ClamAV: http://www.clamav.net

Components
----------

* clamd - antivirus daemon
* clamscan - stand-alone virus checker
* freshclam - signature update service

Interaction
-----------

Use :command:`clamdscan` to pass files to the scanning daemon.

If the :ref:`mailserver` role is also present on the same VM, all mails are
automatically scanned for viruses and discarded if they contain a known virus.

.. vim: set spell spelllang=en:
