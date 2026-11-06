#!/bin/bash
# Phase 444 on the Mac: the hidden attic (chapter 11) and no '--' anywhere a reader looks; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g444/x/apply444.sh
set -e
X=_workspace/chapter-review/g444/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 443 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/claudemd444.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
