#!/bin/bash
# Phase 429 on the Mac: 'ladder' for 'rung', guide lines and the lid in chapter 6, the two guide pages rebuilt, CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g429/x/apply429.sh
set -e
X=_workspace/chapter-review/g429/x
echo "$(cat $X/expected.sha)" | shasum -a 256 -c -          # drills.src.html is exactly what Phase 428 left
cp $X/drills.src.html drills.src.html
shasum -a 256 drills.src.html | grep -q "$(cut -c1-64 $X/new.sha)"
node tools/precompile.js
python3 $X/site429.py . $X
for ch in ledger-lines staff; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd429.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo applied
