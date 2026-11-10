#!/bin/bash
# Build one lesson: bash build.sh <song>   (engrave, crop, page, pdf, clashes)
set -e; s=$1; cd "$(dirname "$0")"
node engrave.mjs $s.json $s-svg.json >/dev/null
node crop.js $s-svg.json $s-crop.json >/dev/null
python3 lesson.py $s.json $s-crop.json lesson-$s.html >/dev/null
o=$(node pdf.js "$PWD/lesson-$s.html" "$PWD/lesson-$s.pdf" | grep over)
c=$(node check.js "$PWD/lesson-$s.html" | tail -1)
echo "$s $o $c"
