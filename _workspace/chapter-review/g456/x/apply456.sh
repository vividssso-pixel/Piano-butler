#!/bin/bash
# Phase 456 on the Mac: chapter 3's guide page (lessons/pulse-and-counting.html), room 3 open on the guides' house,
# the neighbours' links, sitemap, the printables card; CLAUDE.md.
# Run from the repo root:   bash _workspace/chapter-review/g456/x/apply456.sh
set -e
X=_workspace/chapter-review/g456/x
shasum -a 256 -c $X/expected.sha            # the files are exactly what Phase 455 left
mkdir -p tools/lessons/svg/pulse
(cd $X/files && find . -type f) | while read -r f; do mkdir -p "$(dirname "$f")"; cp "$X/files/$f" "$f"; done   # cp writes in place (no delete needed)
shasum -a 256 -c $X/new.sha | grep -v ': OK$' || true
shasum -a 256 -c $X/new.sha >/dev/null
python3 $X/claudemd456.py CLAUDE.md
git status --short | grep -v '^??' || true
git status --short | grep '^??' | grep -v '_workspace\|Claude outputs' || true
echo applied
