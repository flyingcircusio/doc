{ pkgs ? import <nixpkgs> {} }:
let
  lib = pkgs.lib;
  doc = import ./. { inherit pkgs; };
in {
  platformDoc = lib.hydraJob (
    pkgs.runCommandLocal "platform-doc" { inherit doc; } ''
      mkdir -p $out/nix-support
      tar czf $out/platform-doc.tar.gz -C $doc .
      cp $doc/objects.inv $out
      echo "file objects $out/objects.inv" > $out/nix-support/hydra-build-products
    '');
}
