#!/bin/bash
# Phase 446 on the Mac: chapter 3 draft v1 + review pack -- a draft only (drills.src.html unchanged); CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g446/x/apply446.sh
set -e
X=_workspace/chapter-review/g446/x
python3 $X/claudemd446.py CLAUDE.md
mkdir -p "Claude outputs" && cp $X/Chapter-03-Pulse-review-v1.pdf "Claude outputs/"
mkdir -p _workspace/chapter-review/kit && cp $X/kit/*.js _workspace/chapter-review/kit/
git status --short | grep -v '^??' || true
echo applied
