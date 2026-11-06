#!/bin/bash
# Phase 445 on the Mac: chapter 11's guide page and its room; one colon a sentence; guides' previous/next; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g445/x/apply445.sh
set -e
X=_workspace/chapter-review/g445/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 444 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site445.py . $X
for ch in tones first-steps note-names staff ledger-lines index; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd445.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
