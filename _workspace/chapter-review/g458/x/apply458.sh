#!/bin/bash
# Phase 458 on the Mac: 'its other name is ...' in chapter 11 (book, tips, Teacher copy, guide page); CLAUDE.md rules.
# Run from the repo root:   bash _workspace/chapter-review/g458/x/apply458.sh
set -e
X=_workspace/chapter-review/g458/x
shasum -a 256 -c $X/expected.sha
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha >/dev/null
node tools/precompile.js
python3 tools/lessons/build.py tones --final
shasum -a 256 -c $X/new.sha | grep -v ': OK$' || true
python3 $X/claudemd458.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
