#!/bin/bash
# Phase 464 on the Mac: chapter 8, Time Signatures, built in full; chapters 6 and 22 renamed; printables numbered by the map.
# Run from the repo root:   bash _workspace/chapter-review/g464/x/apply464.sh
set -e
X=_workspace/chapter-review/g464/x
shasum -a 256 -c $X/expected.sha
# test the three patchers on copies first, so a mismatch stops before anything changes
T=$(mktemp -d)
cp printables.html teacher-dashboard.html CLAUDE.md "$T/"
python3 $X/printables464.py "$T/printables.html"
python3 $X/dash464.py "$T/teacher-dashboard.html"
python3 $X/claudemd464.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/printables.html" printables.html; cp "$T/teacher-dashboard.html" teacher-dashboard.html; cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
grep -c "Reading the Staff\|Famous Composers" printables.html teacher-dashboard.html || true
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
