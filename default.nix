{ pkgs ? import <nixpkgs> {}
, revCount ? 0
, shortRev ? "0000000"
, gitTag ? ""
, platformDocObjectsInventory ? null # path to objects.inv of flyingcircusio/fc-nixos/doc
}:

let
  myst-docutils = pkgs.python3Packages.callPackage ./myst-docutils.nix {};
  buildEnv = pkgs.python3.withPackages (ps: with ps; [
    linkify-it-py
    myst-docutils
    sphinx
    sphinx_rtd_theme
  ]);
  version = "${toString revCount}.${shortRev}";

in pkgs.stdenv.mkDerivation {
  name = "flyingcircus-docs";
  configurePhase = ":";
  buildInputs = [ buildEnv ] ++ (with pkgs; [ python3 git ]);
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
