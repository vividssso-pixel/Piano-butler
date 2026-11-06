#!/bin/bash
# Phase 462 on the Mac: 'Whose house is this?' colours; the openers' diamond; Book rules 13-15.
# Run from the repo root:   bash _workspace/chapter-review/g462/x/apply462.sh
set -e
X=_workspace/chapter-review/g462/x
shasum -a 256 -c $X/expected.sha
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/claudemd462.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
