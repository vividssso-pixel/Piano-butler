#!/bin/bash
# Phase 430 on the Mac: no cut-in-corner frame in the picture boxes online (it spilled out of every box on wide screens);
# the printed books keep it, measured zoom-proof. CLAUDE.md row.
# Run from the repo root:   bash _workspace/chapter-review/g430/x/apply430.sh
set -e
X=_workspace/chapter-review/g430/x
echo "$(cat $X/expected.sha)" | shasum -a 256 -c -          # drills.src.html is exactly what Phase 429 left
cp $X/drills.src.html drills.src.html
shasum -a 256 drills.src.html | grep -q "$(cut -c1-64 $X/new.sha)"
node tools/precompile.js
python3 $X/claudemd430.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
shasum -a 256 drills.html
echo applied
