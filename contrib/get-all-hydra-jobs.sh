#!/usr/bin/env bash
NIXPKGS_ARGS="{ config = { allowUnfree = true; inHydra = false; allowInsecurePredicate = (_: true); scrubJobs = false; }; };"
nix-eval-jobs --force-recurse --meta --repair --quiet --gc-roots-dir /tmp/gcroots --expr "(import <nixpkgs/pkgs/top-level/release.nix> { nixpkgsArgs = $NIXPKGS_ARGS })" --include nixpkgs=$LOCAL_NIXPKGS_CHECKOUT "$@" > evaluation.jsonl
