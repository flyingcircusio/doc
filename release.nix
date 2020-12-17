{ pkgs ? import <nixpkgs> {}
, src ? {
    outPath = ./.;
    revCount = 0;
    shortRev = "0000000";
    gitTag = "master";
  }
}:
let
  lib = pkgs.lib;

in {
  platformDoc = lib.hydraJob (
    pkgs.stdenv.mkDerivation {
      name = "platform-doc";
      src = (import src.outPath {
        inherit pkgs;
        inherit (src) revCount shortRev gitTag;
      });
      builder = pkgs.stdenv.shell;
      PATH = with pkgs; lib.makeBinPath [ coreutils gnutar gzip ];
      args = [ "-ec" ''
        mkdir -p $out/nix-support
        tar czf $out/platform-doc.tar.gz --mode +w -C $src .
        echo "file tarball $out/platform-doc.tar.gz" >> $out/nix-support/hydra-build-products
        cp $src/objects.inv $out
        echo "file inventory $out/objects.inv" >> $out/nix-support/hydra-build-products
      ''];
    }
  );
}
