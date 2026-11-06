#!/bin/bash
# Phase 473 on the Mac: chapter 18, The Piano's Story, built in full (the last room of Level 3); the Styles Workbook's page 5
# goes with the toolbox's eras; printables (the chapter 18 card's new page and words), CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g473/x/apply473.sh
set -e
X=_workspace/chapter-review/g473/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp printables.html CLAUDE.md "$T/"
python3 $X/printables473.py "$T/printables.html"
python3 $X/claudemd473.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/printables.html" printables.html; cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
