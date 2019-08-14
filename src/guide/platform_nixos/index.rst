.. _platform-nixos:

Platform: NixOS 15.09
=====================

Our second-generation platform is based upon `NixOS 15.09 <http://nixos.org/>`_.
We are providing a subset of the features and components that
are available on our first-generation Gentoo-based platform.
It is maintained but not developed much further and will be replaced by :ref:`platform-nixos2`.

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


Components/Roles
----------------

.. toctree::
   :titlesonly:

   antivirus
   datadog
   docker
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
