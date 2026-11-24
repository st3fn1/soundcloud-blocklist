#!/usr/bin/env python3
"""Checks the lists are well formed and that no blocked domain would break SoundCloud."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = ["soundcloud-ads.txt", "soundcloud-trackers.txt"]
DOMAIN = re.compile(r"^(?=.{1,253}$)([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$")

def load(name):
    out = []
    for n, line in enumerate((ROOT / name).read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if not DOMAIN.match(line):
            sys.exit(f"{name}:{n}: invalid domain '{line}'")
        out.append(line)
    if len(out) != len(set(out)):
        sys.exit(f"{name}: duplicate entries")
    return out

allow = load("allowlist.txt")
protected = {"soundcloud.com", "sndcdn.com", "soundcloud.cloud"} | set(allow)
errors = 0
for name in BLOCK:
    for d in load(name):
        for p in protected:
            # a blocked domain must not equal, or be a parent of, anything SoundCloud needs
            if d == p or p.endswith("." + d) or d.endswith("." + p):
                print(f"{name}: '{d}' would block SoundCloud domain '{p}'"); errors += 1
    print(f"{name}: OK")
sys.exit(1 if errors else 0)
