#!/bin/bash
# Phase 447 on the Mac: the clefs sit on their lines (app, books, guide drawings); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g447/x/apply447.sh
set -e
X=_workspace/chapter-review/g447/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 445 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site447.py . $X
for ch in staff ledger-lines tones; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd447.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
