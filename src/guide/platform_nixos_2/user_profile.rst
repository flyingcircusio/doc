.. _user_profile:

User Profiles
=============

Each home directory has a so-called **user profile**, which allows to have
separate packages and versions compared to the OS. User profiles are thus a
powerful mechanism to tailor an application's runtime environment to the exact
needs of the deployment.

A user profile consists of a directory tree in :file:`~/.nix-profile`,
consisting of the usual subdirectories like *bin*, *include*, *lib*, etc.

Installing Packages
-------------------

Packages which are present in the standard nixpkgs distribution but are not
installed system-wide can be installed in the user profile with
:command:`nix-env`. It's also possible to install package versions that differ 
from the versions installed system-wide.
See https://nixos.org/nixos/packages.html for a list of available packages.


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
-----------------

All packages installed using this approach above can be updated with :command:`nix-env -u`.
See :ref:`changelog` for security updates provided by the Flying Circus support team.


Custom user environments
------------------------

If more control needs to be excercised on a user profile, we recommend building
a custom environment with `userEnv`. This means that packages from arbitrary
sources can be mixed and pinned to specific versions. In addition, own Nix
expressions can be included. This approach should be used if you want to install
libraries in the user profile.

Basic userEnv
^^^^^^^^^^^^^

.. highlight:: default
   :linenothreshold: 3

Create a file like :file:`userenv.nix` which bundles required packages::

   let
     # pinned import, see https://nixos.org/channels
     nixos_18_03 = fetchTarball https://releases.nixos.org/nixos/18.03/nixos-18.03.132915.d6c6c7fcec6/nixexprs.tar.xz;
     pkgs = import nixos_18_03 {};
   in
   pkgs.buildEnv {
     name = "myproject-env";
     paths = with pkgs; [
       libjpeg
       ffmpeg
       nodejs-8_x
       electron
     ];
     extraOutputsToInstall = [ "out" "dev" "bin" "man" ];
   }

The code shown above defines a userEnv with 3 packages installed from a specific
build of NixOS 18.03. The pinned NixOS version can be newer or older than the 
installed system version.

Dry-run this expression with::

   nix-build userenv.nix

A :file:`result` symlink now points to the generated environment. It can be
inspected and used manually, but is not yet an active part of the user profile.

Run ::

   nix-env -i -f userenv.nix

to install this userEnv in your profile. Now its binaries are available in PATH
and libraries/include files should get found by the compiler.

XXX list env vars

To update a userEnv, simply update the source and install it again via
`nix-env`.

Mixing packages from different sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custom shell initializaton
^^^^^^^^^^^^^^^^^^^^^^^^^^


Fitting the RPATH of 3rd-party binary objects
---------------------------------------------
