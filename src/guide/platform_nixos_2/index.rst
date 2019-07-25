.. _platform-nixos2:

Platform: NixOS 19.03
=====================

Our second-generation platform is based upon `NixOS 19.03 <http://nixos.org/>`_.
We are currently providing a subset of the features and components that
are available on our older platforms.

NixOS provides new approaches for installing and managing software. Also,
VMs on our NixOS platform are run in 64-bit and thus allow you to use much
more memory for larger applications.

.. toctree::
   :titlesonly:

   base
   local
   systemd
   cron
   logrotate
   firewall
   user_profile


Roles and packages
------------------

.. toctree::
   :titlesonly:

   external_net
   memcached
   postgresql
   redis
   statshost
   webgateway
   webproxy
