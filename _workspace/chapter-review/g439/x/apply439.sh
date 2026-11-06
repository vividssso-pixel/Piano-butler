#!/bin/bash
# Phase 439 on the Mac: the double dash and Korean words never split (drills.src.html -> drills.html); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g439/x/apply439.sh
set -e
X=_workspace/chapter-review/g439/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 438 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/claudemd439.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
