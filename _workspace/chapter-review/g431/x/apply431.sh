#!/bin/bash
# Phase 431 on the Mac: chapter 6 after her 06:38 notes -- the lid cross, Clara's C from both lands on the opener,
# question numbers in the answer boxes (all Workbooks), the fold on the Five Cs page; guide pictures and words; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g431/x/apply431.sh
set -e
X=_workspace/chapter-review/g431/x
echo "$(cat $X/expected.sha)" | shasum -a 256 -c -          # drills.src.html is exactly what Phase 430 left
cp $X/drills.src.html drills.src.html
shasum -a 256 drills.src.html | grep -q "$(cut -c1-64 $X/new.sha)"
node tools/precompile.js
python3 $X/site431.py . $X
python3 tools/lessons/build.py ledger-lines --final
python3 $X/claudemd431.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
shasum -a 256 drills.html
echo applied
