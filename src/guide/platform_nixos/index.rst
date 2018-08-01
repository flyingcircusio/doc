.. _platform-nixos:

Platform: NixOS
===============

Our second-generation platform is based upon `NixOS <http://nixos.org/>`_.
We are currently providing a subset of the features and components that
are available on our first-generation Gentoo-based platform.

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

   antivirus
   datadog
   elasticsearch
   external_net
   java
   loghost
   memcached
   mysql
   php
   postgresql
   redis
   statshost
   webgateway
   webproxy
