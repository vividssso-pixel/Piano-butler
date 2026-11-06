#!/bin/bash
# Phase 465 on the Mac: a More Scales room on Level 5 (off the map until its chapter exists); Korean bar line 세로줄 everywhere.
# Run from the repo root:   bash _workspace/chapter-review/g465/x/apply465.sh
set -e
X=_workspace/chapter-review/g465/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp CLAUDE.md "$T/"; python3 $X/claudemd465.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
