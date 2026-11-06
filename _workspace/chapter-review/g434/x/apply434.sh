#!/bin/bash
# Phase 434 on the Mac: chapter 7 draft v2 (half step / whole step) -- a draft only (drills.src.html unchanged); CLAUDE.md row.
# Run from the repo root:   bash _workspace/chapter-review/g434/x/apply434.sh
set -e
X=_workspace/chapter-review/g434/x
python3 $X/claudemd434.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo applied
