#!/bin/bash
# Phase 474 on the Mac: chapter 19, Key Signatures, built in full (the first room of Level 4); every chapter's lesson
# ends with its older toolbox tools; printables (the chapter 19 card's new page and words), CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g474/x/apply474.sh
set -e
X=_workspace/chapter-review/g474/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp printables.html CLAUDE.md "$T/"
python3 $X/printables474.py "$T/printables.html"
python3 $X/claudemd474.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/printables.html" printables.html; cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
