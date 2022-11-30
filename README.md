# Flying Circus Documentation

This is the manual for the Flying Circus. It explains how the platform works
and how to run applications.

The rendered HTML is hosted on https://doc.flyingcircus.io which is usually
built from the default branch of this repo.

## Tech

- Documentation generator [Sphinx](https://www.sphinx-doc.org/en/master/)
- Markup languange/Sphinx extension [MyST Markdown](https://myst-parser.readthedocs.io/en/latest/)
- Translation utility [sphinx-doc/sphinx-intl](https://github.com/sphinx-doc/sphinx-intl)
- Read the Docs Sphinx theme [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html)

## Development

- Build full documentation locally with pinned nixpkgs: `nix-build`
  - Building with pinned nixpkgs may take some time and download a lot of
    stuff if you don't already have the needed packages installed and your
    local channel differs greatly from the pinned version.
  - or: build with nixpkgs flake: `nix-build --arg pkgs 'import (builtins.getFlake "nixpkgs") {}'`
  - or: build with local nixpkgs from NIX_PATH: `nix-build --arg pkgs 'import <nixpkgs> {}'`
  - At least nixpkgs version 22.11 is required.

- Start Nix development environment which has the tools needed to build the
  documentation and do other maintenance tasks like regenerating the
  translation files: `nix-shell`.
  The following commands will work in this env:

    - Update POT/PO files from source: `make update-translations`
    - Build english (source language) documentation: `make html`
    - Build translated documentation in German: `make html-de`
    - Check all links (slow!): `sphinx-build  src _build -b linkcheck`
    - Show contents of the objects inventory: 
      `python -m sphinx.ext.intersphinx https://doc.flyingcircus.io/platform/objects.inv`

  - Update nixpkgs version: change URL in `default.nix` for the `pkgs` argument, right at the top.

## External References (intersphinx)

We need to link to platform/role docs which are version-specific and live in the
[flyingcircusio/fc-nixos](https://github.com/flyingcircusio/fc-nixos) repository
under `doc`. The current default version of the platform/role docs is configured
in `src/conf.py` as `platform-current`. When building locally, the object
inventory file (objects.inv) is pulled from the URL specified there.

To link from this repo here to the platform/role docs, use
`{external+platform-current:ref}` like:

~~~
Refer to the {external+platform-current:ref}`nixos-postgresql-server` role documentation.
~~~

Available symbols can be checked with, for example:

~~~
python -m sphinx.ext.intersphinx https://doc.flyingcircus.io/roles/fc-21.11-production/objects.inv`
~~~

## Translations

For now, only one file, the data protection rules, is translated to German. The
rendered German version can be found here:

https://doc.flyingcircus.io/platform/de/reference/security/data-protection.html

After changes to this file, `make update-translations` should be run.

Note that there is currently a bug in MyST which incorrectly renders footnote references
in translated strings. If you need footnotes + translation in a file, just keep it as RestructuredText with the ending `.rst`.

Bug report:

https://github.com/executablebooks/MyST-Parser/issues/445
