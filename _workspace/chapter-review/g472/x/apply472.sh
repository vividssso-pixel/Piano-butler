#!/bin/bash
# Phase 472 on the Mac: chapter 17, Accidentals, a new chapter built in full; the map renumbers chapters 18 to 27;
# printables (the new card, the numbers, 26 pages), the teacher dashboard's chapter list, CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g472/x/apply472.sh
set -e
X=_workspace/chapter-review/g472/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp printables.html CLAUDE.md teacher-dashboard.html "$T/"
python3 $X/printables472.py "$T/printables.html"
python3 $X/dash472.py "$T/teacher-dashboard.html"
python3 $X/claudemd472.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/printables.html" printables.html; cp "$T/CLAUDE.md" CLAUDE.md; cp "$T/teacher-dashboard.html" teacher-dashboard.html
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
