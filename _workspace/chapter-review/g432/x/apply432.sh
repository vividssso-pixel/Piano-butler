#!/bin/bash
# Phase 432 on the Mac: chapter 7 draft v1 + review pack -- a draft only (drills.src.html unchanged); CLAUDE.md row.
# Run from the repo root:   bash _workspace/chapter-review/g432/x/apply432.sh
set -e
X=_workspace/chapter-review/g432/x
python3 $X/claudemd432.py CLAUDE.md
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
echo applied
