#!/bin/bash
# Phase 438 on the Mac: the house -- no frames, no lamps, the glass dome in your room; the guides' front page; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g438/x/apply438.sh
set -e
X=_workspace/chapter-review/g438/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 437 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site438.py . $X
python3 tools/lessons/build.py index --final
python3 $X/claudemd438.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
