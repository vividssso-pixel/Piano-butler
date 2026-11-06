#!/bin/bash
# Phase 428 on the Mac: chapter 6 (Ledger Lines) applied -- drills, the guide page and its room, printables, CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g428/x/apply428.sh
set -e
X=_workspace/chapter-review/g428/x
echo "$(cat $X/expected.sha)" | shasum -a 256 -c -          # drills.src.html is exactly what Phase 426 left
cp $X/drills.src.html drills.src.html
shasum -a 256 drills.src.html | grep -q "$(cut -c1-64 $X/new.sha)"
node tools/precompile.js
python3 $X/site428.py . $X
for ch in ledger-lines index; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd428.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo applied
