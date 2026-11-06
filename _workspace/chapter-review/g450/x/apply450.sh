#!/bin/bash
# Phase 450 on the Mac: chapter 1's thumb in and out, one plays the others balance (app, book, guide); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g450/x/apply450.sh
set -e
X=_workspace/chapter-review/g450/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 449 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site450.py . $X
python3 tools/lessons/build.py posture-hands --final
python3 $X/claudemd450.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
