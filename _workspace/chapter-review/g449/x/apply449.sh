#!/bin/bash
# Phase 449 on the Mac: the five Cs by their real names (app, books, ledger-lines guide); CLAUDE.md rules 8 and 11.
# Run from the repo root:   bash _workspace/chapter-review/g449/x/apply449.sh
set -e
X=_workspace/chapter-review/g449/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phase 448 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/site449.py . $X
python3 tools/lessons/build.py ledger-lines --final
python3 $X/claudemd449.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
