.. _antivirus:

Antivirus
=========

Installs the `ClamAV`_ virus checker and infrastructure to update virus
signatures regularly.

.. note::

   ClamAV is a bit heavy on resources. It requires 256 to 512 MiB RAM depending
   on usage.

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
