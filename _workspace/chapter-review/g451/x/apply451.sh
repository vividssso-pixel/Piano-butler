#!/bin/bash
# Phase 451 on the Mac: the cut-outs' fixes; two printables pictures; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g451/x/apply451.sh
set -e
X=_workspace/chapter-review/g451/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 450 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site451.py . $X
python3 $X/claudemd451.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
