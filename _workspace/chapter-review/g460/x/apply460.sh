#!/bin/bash
# Phase 460 on the Mac: chapter 5, Notes & Rests, as a Lesson Book, its screen lesson, drill, Workbook and Teacher copy.
# Run from the repo root:   bash _workspace/chapter-review/g460/x/apply460.sh
set -e
X=_workspace/chapter-review/g460/x
shasum -a 256 -c $X/expected.sha
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/printables460.py printables.html
python3 $X/claudemd460.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
