{ pkgs ? import <nixpkgs> {}
, revCount ? 0
, shortRev ? "0000000"
, gitTag ? ""
}:

let
  buildEnv = pkgs.python3.withPackages (ps: [ ps.sphinx ps.sphinx_rtd_theme ]);
  version = "${toString revCount}.${shortRev}";

in pkgs.stdenv.mkDerivation {
  name = "flyingcircus-docs";
  configurePhase = ":";
  buildInputs = [ buildEnv ] ++ (with pkgs; [ python3 git ]);
  doCheck = false;
  buildPhase = ''
    cd $src
    sphinx-build -j 10 -a -b html src $out
  '';
  installPhase = ":";
  src = ./.;
  dontStrip = true;
  dontPatchELF = true;
  inherit revCount shortRev gitTag version;
}
