{ pkgs ? import <nixpkgs> {}
, platformDocObjectsInventory
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
        inherit pkgs platformDocObjectsInventory;
        inherit (src) revCount shortRev gitTag;
      });
      builder = pkgs.stdenv.shell;
      PATH = with pkgs; lib.makeBinPath [ coreutils gnutar gzip ];
      args = [ "-ec" ''
        mkdir -p $out/nix-support
        cd $src
        tar cf $out/platform-doc.tar --mode +w -C en .
        tar uf $out/platform-doc.tar --mode +w de
        gzip $out/platform-doc.tar
        echo "file tarball $out/platform-doc.tar.gz" >> $out/nix-support/hydra-build-products
        cp $src/en/objects.inv $out
        echo "file inventory $out/objects.inv" >> $out/nix-support/hydra-build-products
      ''];
    }
  );
}
