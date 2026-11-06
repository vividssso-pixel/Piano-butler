#!/bin/bash
# Phase 453 on the Mac: the guide pages without long dashes, in short paragraphs; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g453/x/apply453.sh
set -e
X=_workspace/chapter-review/g453/x
shasum -a 256 -c $X/expected.sha            # the guide sources are exactly what Phase 449/450 left
cp $X/src/*.html tools/lessons/src/
for ch in index first-steps posture-hands note-names staff ledger-lines tones; do python3 tools/lessons/build.py $ch --final; done
python3 $X/claudemd453.py CLAUDE.md
git status --short | grep -v '^??' || true
echo applied
