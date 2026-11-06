#!/bin/bash
# Phase 484 on the Mac: the foundation, step 1: the Toolbox in five areas and 13 concepts (rule 16); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g484/x/apply484.sh
set -e
X=_workspace/chapter-review/g484/x
shasum -a 256 -c $X/expected.sha
T=$(mktemp -d); cp CLAUDE.md "$T/"
python3 $X/claudemd484.py "$T/CLAUDE.md" $X/row484.md
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done
cp "$T/CLAUDE.md" CLAUDE.md
shasum -a 256 -c $X/new.sha >/dev/null
node tools/precompile.js
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
