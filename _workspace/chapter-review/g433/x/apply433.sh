#!/bin/bash
# Phase 433 on the Mac: the butler is the rabbit again (centred) -- every book's REMEMBER band, the map's hall, the
# welcomes; the guides' front-page house and its sharing picture; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g433/x/apply433.sh
set -e
X=_workspace/chapter-review/g433/x
echo "$(cat $X/expected.sha)" | shasum -a 256 -c -          # drills.src.html is exactly what Phase 431 left
cp $X/drills.src.html drills.src.html
shasum -a 256 drills.src.html | grep -q "$(cut -c1-64 $X/new.sha)"
node tools/precompile.js
python3 $X/site433.py . $X
python3 tools/lessons/build.py index --final
python3 $X/claudemd433.py CLAUDE.md
shasum -a 256 drills.html
echo applied
