.. _user_profile:

User Profiles
=============

Each home directory has a so-called **user profile**, which allows to have
separate packages and versions compared to the OS. User profiles are thus a
powerful mechanism to tailor an application's runtime environment to the exact
needs of the deployment.
You can also install the tools you like in your personal user environment.

An user profile consists of a directory tree in :file:`~/.nix-profile`,
consisting of the usual subdirectories like *bin*, *include*, *lib*, etc.


Installing Packages
-------------------

Packages which are present in the standard nixpkgs distribution but are not
installed system-wide can be installed directly in the user profile with
`nix-env -iA nixos.<package attribute name>`.

See https://nixos.org/nixos/packages.html for a list of packages.
Use the "attribute name" from the list. They can differ from the package name.
For some packages, multiple versions are available.

Installing packages that are already present in the system environment is safe.
This doesn't use additional space if it's the same version.

.. warning:: Installing libraries with this approach is not recommended because
    headers and other files needed for building software may be missing.

For some packages, only files needed for running the executables in the package
are installed by default.
Use :ref:`user_env` instead. They provide more flexibility and are useful to
bundle your application's dependencies.

Example Executable: hello
^^^^^^^^^^^^^^^^^^^^^^^^^

Let's assume you want to use the :command:`hello` command in your user environment::

  $ hello
  hello: command not found

The package can be installed for the current user with::

  $ nix-env -iA nixos.hello
  installing 'hello-2.10'
  these paths will be fetched (0.04 MiB download, 0.20 MiB unpacked):
    /nix/store/83vqfmpq19g0rkgjf0sa319x919p0vvg-hello-2.10
  copying path '/nix/store/83vqfmpq19g0rkgjf0sa319x919p0vvg-hello-2.10' from 'https://cache.nixos.org'...
  building '/nix/store/mks11b15z9larfn83rmczqn76xbjssz9-user-environment.drv'...
  created 172 symlinks in user environment

In this case, Nix downloads the hello path because it's not in the local store yet.
You can run :command:`hello` now::

  $ hello
  Hello, World!

Running the install command again replaces the current `hello` package, which, in fact, changes nothing here::

  $ nix-env -iA nixos.hello
  replacing old 'hello-2.10'
  installing 'hello-2.10'

If you run the install command later, the current package may be updated to a newer version.

See :manpage:`nix-env(1)` for further options.


Updating packages
^^^^^^^^^^^^^^^^^

All packages installed using this approach above can be updated with :command:`nix-env -u`.
See :ref:`changelog` for security updates provided by the Flying Circus support team.


.. _user_env:

Custom User Environments
------------------------

This approach should be used if you want to install libraries in the user profile.

If more control needs to be exercised on an user profile, we recommend building
a custom environment with `buildEnv` that can be installed with :command:`nix-env`.
This means that packages from arbitrary sources can be mixed and pinned to
specific versions. In addition, own Nix expressions can be included.

User Environment Basics
^^^^^^^^^^^^^^^^^^^^^^^

.. highlight:: default
   :linenothreshold: 3

Create a file like :file:`userenv.nix` which bundles required packages::

   let
     # pinned NixOS version, see https://nixos.org/channels
     pkgs = import (fetchTarball https://releases.nixos.org/nixos/19.09/nixos-19.09.2149.58a9acf75a3/nixexprs.tar.xz) {};
     # or just use the current NixOS version of the platform, currently 19.03
     # pkgs = import <nixpkgs> {};
   in
   pkgs.buildEnv {
     name = "myproject-env";
     paths = with pkgs; [
       libjpeg
       zlib
       ffmpeg
       nodejs-10_x
       electron
     ];
     extraOutputsToInstall = [ "dev" ];
   }

The code shown above defines an user env with 5 packages installed from a specific
build of NixOS 19.09. The pinned NixOS version can be newer or older than the
installed system version.

See https://nixos.org/nixos/packages.html for a list of packages.
Look for the "attribute name" of the package and include it in `paths`.

Dry-run this expression with::

   nix-build userenv.nix

A :file:`result` symlink now points to the generated environment. It can be
inspected and used manually, but is not yet an active part of the user profile.

Run ::

   nix-env -i -f userenv.nix

to install the env in your profile. Now its binaries are available in PATH
and libraries/include files should get found by the compiler.

To update an user env, install it again with the same command.
This picks up changes in :file:`userenv.nix` and package updates
(if the imports are not pinned to a specific version).

Collisions With Existing Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Packages included in an user environment can collide with separately installed packages.

You may encounter an error like this::

  $ nix-env -if userenv.nix
  installing 'myproject-env'
  building '/nix/store/c3qwfxvdhjgirvzxdhc2h0wpa59fplvk-user-environment.drv'...
  error: packages '/nix/store/s1vqsx5jd7xxq3ihwxz4sc6h1fwnh3v1-myproject-env/lib/libz.so' and '/nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/lib/libz.so' have the same priority 5; use 'nix-env --set-flag priority NUMBER INSTALLED_PKGNAME' to change the priority of one of the conflicting packages (0 being the highest priority)
  builder for '/nix/store/c3qwfxvdhjgirvzxdhc2h0wpa59fplvk-user-environment.drv' failed with exit code 1
  error: build of '/nix/store/c3qwfxvdhjgirvzxdhc2h0wpa59fplvk-user-environment.drv' failed

You can check for potential collisions by viewing the list of packages in the user profile::

  nix-env -q --installed

To avoid/resolve conflicts, remove the package and install the user env afterwards::

  nix-env -e zlib-1.2.11
  nix-env -if userenv.nix

Multiple Package Outputs
^^^^^^^^^^^^^^^^^^^^^^^^

Packages can have multiple "outputs" which means that not all files are
installed by default. If you want to install libraries to build against,
including `dev` in `extraOutputsToInstall` should be sufficient.
You can check which outputs are available with the following command::

   nix show-derivation -f '<nixpkgs>' zlib | jq '.[].env.outputs'

This shows the outputs for `zlib`: `out`, `dev` and `static`. `-f` sets
the inspected NixOS version, which can be an URL like in :file:`userenv.nix`.

Assume we have an user env with just `zlib`. If `extraOutputsToInstall`
is empty, these files would be installed::

  $ nix-build userenv.nix && tree -l result
  /nix/store/s1vqsx5jd7xxq3ihwxz4sc6h1fwnh3v1-myproject-env
  result
  ├── lib -> /nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/lib
  │   ├── libz.so -> libz.so.1.2.11
  │   ├── libz.so.1 -> libz.so.1.2.11
  │   └── libz.so.1.2.11
  └── share -> /nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/share
      └── man
          └── man3
              └── zlib.3.gz


If you add `dev` to `extraOutputsToInstall`, `include` and `lib/pkgconfig`
would be installed, too::

  $ nix-build userenv.nix && tree -l result
  /nix/store/a078dzvn7w7pp3mn0gxig8mpc14p2g4s-myproject-env
  result
  ├── include -> /nix/store/ww7601vx7qrcwwfnwzs1cwwx6zcqdjz3-zlib-1.2.11-dev/include
  │   ├── zconf.h
  │   └── zlib.h
  ├── lib
  │   ├── libz.so -> /nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/lib/libz.so
  │   ├── libz.so.1 -> /nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/lib/libz.so.1
  │   ├── libz.so.1.2.11 -> /nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/lib/libz.so.1.2.11
  │   └── pkgconfig -> /nix/store/ww7601vx7qrcwwfnwzs1cwwx6zcqdjz3-zlib-1.2.11-dev/lib/pkgconfig
  │       └── zlib.pc
  └── share -> /nix/store/iiymx8j7nlar3gc23lfkcscvr61fng8s-zlib-1.2.11/share
      └── man
          └── man3
              └── zlib.3.gz


Mixing Packages From Different Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can import packages from different NixOS versions or other sources::

   let
     pkgs = import <nixpkgs> {};
     pkgs_19_09 = import (fetchTarball https://releases.nixos.org/nixos/19.09/nixos-19.09.2149.58a9acf75a3/nixexprs.tar.xz) {};
   in
   pkgs.buildEnv {
     name = "myproject-env";
     paths = with pkgs; [
       pkgs_19_09.libjpeg
       zlib
     ];
     extraOutputsToInstall = [ "dev" ];
   }

This installs the `zlib` from the platform NixOS version but `libjpeg` from NixOS 19.09.


.. XXX list env vars
.. XXX Custom shell initializaton
.. XXX Fitting the RPATH of 3rd-party binary objects
