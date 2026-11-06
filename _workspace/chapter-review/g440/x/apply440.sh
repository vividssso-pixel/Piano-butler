#!/bin/bash
# Phase 440 on the Mac: Tones & Semitones, the steps dotted on the keys (drills.src.html -> drills.html); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g440/x/apply440.sh
set -e
X=_workspace/chapter-review/g440/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 439 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/claudemd440.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
