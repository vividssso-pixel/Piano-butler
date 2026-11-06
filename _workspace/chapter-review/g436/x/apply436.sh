#!/bin/bash
# Phase 436 on the Mac: the path in five levels and every box centred -- the app and its books (drills.src.html ->
# drills.html), the guides' pages and front page (kickers, numbers, the house, its sharing picture), CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g436/x/apply436.sh
set -e
X=_workspace/chapter-review/g436/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 433 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site436.py . $X
for c in posture-hands first-steps note-names staff ledger-lines index; do python3 tools/lessons/build.py $c --final; done
python3 $X/claudemd436.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
