.. _platform-nixos2:

Platform: NixOS 19.03
=====================

Our third-generation platform is based upon `NixOS 19.03 <http://nixos.org/>`_.

NixOS provides new approaches for installing and managing software. Also,
VMs on our NixOS platform are run in 64-bit and thus allow you to use much
more memory for larger applications.

.. toctree::
   :titlesonly:

   base
   user_profile
   local
   systemd
   cron
   logging
   logrotate
   firewall
   monitoring

.. _nixos2-components:

Components/Roles
----------------

.. toctree::
   :titlesonly:

   docker
   elasticsearch
   external_net
   kibana
   kubernetes
   loghost
   mailserver
   memcached
   mongodb
   nfs
   postgresql
   rabbitmq
   redis
   statshost
   webgateway
   webproxy
