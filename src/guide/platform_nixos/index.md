(platform-nixos)=

# NixOS 15.09 (outdated)

Our second-generation platform is based upon [NixOS 15.09](http://nixos.org/).
We are providing a subset of the features and components that
are available on our first-generation Gentoo-based platform.

It is outdated and replaced by current [NixOS platforms](/roles/current).
Updates and changes are provided to assist migration to the new platform.

NixOS provides new approaches for installing and managing software. Also,
VMs on our NixOS platform are run in 64-bit and thus allow you to use much
more memory for larger applications.

```{toctree}
:titlesonly: true

base
local
systemd
cron
logging
logrotate
firewall
user_profile
```

(nixos-components)=

## Components/Roles

```{toctree}
:titlesonly: true

antivirus
datadog
docker
elasticsearch
external_net
java
loghost
memcached
mysql
nfs
php
postgresql
redis
statshost
webgateway
webproxy
```
