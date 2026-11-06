#!/bin/bash
# Phase 455 on the Mac: chapter 3 (Pulse & Counting) as a Lesson Book, its online lesson, drill, Workbook and Teacher copy; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g455/x/apply455.sh
set -e
X=_workspace/chapter-review/g455/x
shasum -a 256 -c $X/expected.sha            # drills.src.html is exactly what Phases 453/454 left
cp $X/drills.src.html drills.src.html
shasum -a 256 -c $X/new.sha
node tools/precompile.js
python3 $X/claudemd455.py CLAUDE.md
echo "drills.html $(shasum -a 256 drills.html | cut -c1-64)"
echo "container   $(cat $X/build.sha)"
git status --short | grep -v '^??' || true
echo applied
