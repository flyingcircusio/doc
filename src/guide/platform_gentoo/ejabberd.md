:Publish Date: 2012-12-13

.. _jabber:

ejabberd
========

Description
-----------

Installs ejabberd, a XMPP (Jabber) server.

Components
----------

- `ejabberd`_

.. _ejabberd: http://www.process-one.net/en/ejabberd

Configuration
-------------

A default configuration that enabled the most common modules (including mod_muc)
is provided with the role. Please note that the default configuration opens
sockets on localhost only, so the XMPP server will not be very useful without
customization.

Service users may modify :file:`/etc/jabber/ejabberd-local.cfg`, which is read
in addition to the default configuration. Most likely custom port definitions
go in here.

Interaction
-----------

Service users may call :command:`sudo /etc/init.d/ejabberd restart` to restart
the XMPP server instance. They may also call :command:`sudo
/etc/init.d/ejabberctl` to invoke administrative functions.

The XMPP server logs to :file:`/var/log/jabber` which is world-readable.


Monitoring
----------

- The existence of an ejabberd process is checked.
- The monitoring system tries to connect to localhost port 5222 and expects a
  XMPP handshake. When you configure custom ports in
  :file:`/etc/jabber/ejabberd-local.cfg`, make sure to leave a port open on
  localhost:5222 to keep the check running.

.. vim: set spell spelllang=en:
