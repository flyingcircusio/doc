.. _apparmor:

AppArmor
========

This role installs and pre-configures AppArmor, a Linux application security
system. Information about AppArmor can be found in the `official documentation
<http://wiki.apparmor.net/index.php/Documentation>`_.

Components
----------

* apparmor-profiles (A collection of profiles for the AppArmor application
  security system)
* apparmor-utils (Additional userspace utils to assist with AppArmor profile
  management)

Configuration
-------------

The pre-configured AppArmor profiles are stored in :file:`/etc/apparmor.d/`.

By default, all these profiles are loaded in `complain` mode, which represents a
learning mode. Actions that violate profile rules are only logged, not
prohibited. Technically, the `complain` mode is realized by having symlinks in
:file:`/etc/apparmor.d/force-complain/` that point to the respective profile in
:file:`/etc/apparmor.d/`.

To enable a profile, simply remove the corresponding symlink in
:file:`/etc/apparmor.d/force-complain/` as a service user.

Service users may put own AppArmor profiles in :file:`/etc/apparmor.d/local/`.
For information about how to create AppArmor profiles, the official `quick
language guide <http://wiki.apparmor.net/index.php/QuickProfileLanguage>`_ is a
good place to start.

.. note::

   Please note that profiles created in :file:`/etc/apparmor.d/local/` are
   enabled by default as long as you put a corresponding symlink in
   :file:`/etc/apparmor.d/force-complain/`.

Interaction
-----------

Service users may restart AppArmor by executing :command:`/etc/init.d/apparmor
restart`.

They may also inquire information about AppArmors's currently loaded policy
be executing :command:`sudo aa-status`.

Further, service users may list processes that have network access and have no
AppArmor profile assigned by executing :command:`sudo aa-unconfined`.


Monitoring
----------

Log messages from AppArmor will appear in our general logcheck which customers
do also receive notifications about.

You can manually inspect the log files on a machine for entries by grepping this way::

    $ zgrep -i /var/log/messages*
