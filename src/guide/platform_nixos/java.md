(nixos-java)=

# Java

The Java role installs installs [OpenJDK 8](http://openjdk.java.net).

Note that on the NixOS platform it is not strictly necessary to activate a role to install software. You can install Java into the service-user:

```
ssh your-vm
sudo -iu s-youserservice
nix-env -iA nixos.jdk
```

To find out about which java packages are available, see the [NixOS packages index](https://nixos.org/nixos/packages.html). We also have some guidance for [automatically installing Oracle Java](https://blog.flyingcircus.io/2016/05/12/automatic-installation-of-oracle-java/).

% vim: set spell spelllang=en:
