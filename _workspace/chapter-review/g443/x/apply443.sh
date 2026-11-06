#!/bin/bash
# Phases 442-443 on the Mac: the rabbit in two pictures, rooms from the bottom, the door every visit; Clara without
# the title; the guide pages and printables; CLAUDE.md.   Run from the repo root:  bash _workspace/chapter-review/g443/x/apply443.sh
set -e
X=_workspace/chapter-review/g443/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 441 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site443.py . $X
for ch in posture-hands first-steps note-names staff ledger-lines index; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd443.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
