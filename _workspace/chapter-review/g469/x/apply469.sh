#!/bin/bash
# Phase 469 on the Mac: chapter 13, Tempo Race, built in full; its printables card.
# Run from the repo root:   bash _workspace/chapter-review/g469/x/apply469.sh
set -e
X=_workspace/chapter-review/g469/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp printables.html CLAUDE.md "$T/"
python3 $X/printables469.py "$T/printables.html"
python3 $X/claudemd469.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/printables.html" printables.html; cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
