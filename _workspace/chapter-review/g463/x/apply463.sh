#!/bin/bash
# Phase 463 on the Mac: walk / run-ning (타 / 티-티) in chapter 3; held taps; the King's cross; chapter 6's skips.
# Run from the repo root:   bash _workspace/chapter-review/g463/x/apply463.sh
set -e
X=_workspace/chapter-review/g463/x
shasum -a 256 -c $X/expected.sha
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
node tools/precompile.js
for ch in pulse staff; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd463.py CLAUDE.md
grep -c "tur-tle\|light-house" lessons/pulse-and-counting.html || true
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
