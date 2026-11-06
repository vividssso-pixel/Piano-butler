#!/bin/bash
# Phase 479 on the Mac: chapter 23, Musical Terms, built in full (Lesson Book, screen lesson, drill, Workbook, Teacher copy);
# the map's new order (Level 4 ends with terms and form; Level 5 melody, composers, styles); printables.html (topic numbers, the chapter 23 card); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g479/x/apply479.sh
set -e
X=_workspace/chapter-review/g479/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp CLAUDE.md "$T/"
python3 $X/claudemd479.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
