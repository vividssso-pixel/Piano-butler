#!/bin/bash
# Phase 476 on the Mac: the twelve keys, macro first (chapters 16 and 19: the keyboard clock and the circle of fifths,
# the student's keys from the dashboard, level 10, Workbook page 7); teacher-dashboard.html (the keys picker); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g476/x/apply476.sh
set -e
X=_workspace/chapter-review/g476/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp CLAUDE.md "$T/"
python3 $X/claudemd476.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
cp "$T/CLAUDE.md" CLAUDE.md
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
