#!/bin/bash
# Phase 426 on the Mac: the townhouse map in drills, the guides' front page, CLAUDE.md. Run from the repo root:
#   bash _workspace/chapter-review/g426/x/apply426.sh
set -e
X=_workspace/chapter-review/g426/x
echo "$(cat $X/expected.sha)" | shasum -a 256 -c -          # drills.src.html is exactly what Phase 425 left
cp $X/drills.src.html drills.src.html
(cd $X && shasum -a 256 -c new.sha) && shasum -a 256 drills.src.html | grep -q "$(cut -c1-64 $X/new.sha)"
node tools/precompile.js
python3 $X/site426.py . $X
for ch in index posture-hands first-steps note-names staff; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd426.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo applied
