{ pkgs ? import <nixpkgs> {} }:

let
  buildEnv = pkgs.python3.withPackages (ps: [ ps.sphinx ps.sphinx_rtd_theme ]);

in pkgs.stdenv.mkDerivation {
  name = "flyingcircus-docs";
  configurePhase = ":";
  buildInputs = [ buildEnv ] ++ (with pkgs; [ python3 git ]);
  doCheck = false;
  buildPhase = "sphinx-build -j 10 -a -b html $src/src $out";
  installPhase = ":";
  src = ./.;
  dontStrip = true;
  dontPatchELF = true;
}
