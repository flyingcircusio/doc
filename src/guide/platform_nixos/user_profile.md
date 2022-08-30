(user-profile)=

# User Profiles

Each home directory has a so-called **user profile**, which allows to have
separate packages and versions compared to the OS. User profiles are thus a
powerful mechanism to tailor an application's runtime environment to the exact
needs of the deployment.

A user profile consists of a directory tree in {file}`~/.nix-profile`,
consisting of the usual subdirectories like *bin*, *include*, *lib*, etc.

## Using non-standard base OS packages

Packages which are present in the standard nixpkgs distribution but not
installed system-wide can be installed in the user profile with
{command}`nix-env`. See <https://nixos.org/nixos/packages.html> for a list of
available packages.

### Example: Installing libjpeg-turbo

Consider an application needs to compile against `libjpeg-turbo`. Installing the
package via {command}`nix-env -i` makes shared libraries and include files
available in {file}`~/.nix-profile`:

```
$ nix-env -i -A nixos.libjpeg
$ ls ~/.nix-profile/lib
jpeglib.h
[...]
$ ls ~/.nix-profile/include
libjpeg.la  libjpeg.so.62 libjpeg.so  libjpeg.so.62.2.0
[...]
```

You can only install versions provided via the base OS using this method.
However, packages installed using this approach can pick up security updates
quite easily with {command}`nix-env -u`. See {ref}`changelog` for information of
security updates provided by the Flying Circus support team.

See {manpage}`nix-env(1)` for further options.

## Custom user environments

If more control needs to be excercised on a user profile, we recommend building
a custom environment with `userEnv`. This means that packages from arbitrary
sources can be mixed and pinned to specific versions. In addition, own Nix
expressions can be included.

### Basic userEnv

```{highlight} default
:linenothreshold: 3
```

Create a file like {file}`userenv.nix` which bundles required packages:

```
let
  # pinned import, see https://nixos.org/channels
  nixos_18_03 = fetchTarball https://releases.nixos.org/nixos/18.03/nixos-18.03.132915.d6c6c7fcec6/nixexprs.tar.xz;
  pkgs = import nixos_18_03 {};
in
pkgs.buildEnv {
  name = "myproject-env";
  paths = with pkgs; [
    ffmpeg
    nodejs-8_x
    electron
  ];
  extraOutputsToInstall = [ "out" "dev" "bin" "man" ];
}
```

The code shown above defines a userEnv with 3 packages installed from a specific
build of NixOS 18.03.

Dry-run this expression with:

```
nix-build userenv.nix
```

A {file}`result` symlink now points to the generated environment. It can be
inspected and used manually, but is not yet an active part of the user profile.

Run

```
nix-env -i -f userenv.nix
```

to install this userEnv in your profile. Now its binaries are available in PATH
and libraries/include files should get found by the compiler.

XXX list env vars

To update a userEnv, simply update the source and install it again via
`nix-env`.

### Mixing packages from different sources

### Custom shell initializaton

## Fitting the RPATH of 3rd-party binary objects
