#!/bin/bash
# Phase 482 on the Mac: chapter 26, Composers through Time, built in full on the timeline of music (Lesson Book, screen
# lesson, drill, Workbook, Teacher copy); printables.html (the chapter 26 card's words); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g482/x/apply482.sh
set -e
X=_workspace/chapter-review/g482/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp CLAUDE.md "$T/"
python3 $X/claudemd482.py "$T/CLAUDE.md"
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
cp "$T/CLAUDE.md" CLAUDE.md
shasum -a 256 -c $X/new.sha >/dev/null
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
