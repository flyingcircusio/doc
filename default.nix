{
  pkgs ? import (fetchTarball "https://hydra.flyingcircus.io/build/457353/download/1/nixexprs.tar.xz") {}
, revCount ? 0
, shortRev ? "0000000"
, gitTag ? ""
, platformDocObjectsInventory ? null # path to objects.inv of flyingcircusio/fc-nixos/doc
}:

let
  sphinx-intl = pkgs.python3Packages.callPackage ./sphinx-intl.nix {};

  buildEnv = pkgs.python3.withPackages (ps: with ps; [
    linkify-it-py
    myst-docutils
    sphinx
    sphinx-copybutton
    sphinx-intl
    sphinx_rtd_theme
    furo
  ]);

  version = "${toString revCount}.${shortRev}";

in pkgs.stdenv.mkDerivation {
  name = "flyingcircus-docs";
  configurePhase = ":";
  buildInputs = [ buildEnv ] ++ (with pkgs; [ python3 git gnumake ]);
  doCheck = false;
  buildPhase = ''
    make html
    make html-de
  '';
  installPhase = ''
    mkdir $out
    mv _build/en/html $out/en
    mv _build/de/html $out/de
  '';
  src = ./.;
  dontStrip = true;
  dontPatchELF = true;
  inherit revCount shortRev gitTag version platformDocObjectsInventory;
}
