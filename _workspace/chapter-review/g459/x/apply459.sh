#!/bin/bash
# Phase 459 on the Mac: short and plain in the eight finished books and their guides; real names for the staves;
# chapter 7 renamed 'Line and Space Names'.   Run from the repo root:   bash _workspace/chapter-review/g459/x/apply459.sh
set -e
X=_workspace/chapter-review/g459/x
shasum -a 256 -c $X/expected.sha
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
node tools/precompile.js
for ch in posture-hands first-steps pulse note-names staff tones ledger-lines index; do python3 tools/lessons/build.py $ch --final; done
shasum -a 256 -c $X/new.sha | grep -v ': OK$' || true
python3 $X/dash459.py teacher-dashboard.html
python3 $X/claudemd459.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
