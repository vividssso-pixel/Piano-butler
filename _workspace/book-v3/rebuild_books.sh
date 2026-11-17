#!/bin/bash
# Rebuild both books from the built HTML (her 17 Nov): render every part in Chromium, then merge in book order.
# Usage: rebuild_books.sh <src dir with *-pilot.html, front.html, before.html, glossary.html, wb/*.html> <out dir> <old workbook pdf for pp. 5-6>
set -e
S=$1; O=$2; OLDWB=$3; R=$(dirname $0)/render.js; mkdir -p $O/parts
for p in front before pitch-pilot time-pilot expression-pilot scales-pilot chords-pilot harmony-pilot shape-pilot play-pilot further-pilot glossary; do node $R $S/$p.html $O/parts/hb-$p.pdf; done
for p in front pitch time expression scales chords harmony shape play; do node $R $S/wb/$p.html $O/parts/wb-$p.pdf; done
qpdf --empty --pages $(for p in front before pitch-pilot time-pilot expression-pilot scales-pilot chords-pilot harmony-pilot shape-pilot play-pilot further-pilot glossary; do echo $O/parts/hb-$p.pdf; done) -- $O/handbook-new-draft.pdf
qpdf --empty --pages $O/parts/wb-front.pdf $OLDWB 5-6 $(for p in pitch time expression scales chords harmony shape play; do echo $O/parts/wb-$p.pdf; done) -- $O/workbook-new-draft.pdf
for b in handbook workbook; do echo "$b: $(pdfinfo $O/$b-new-draft.pdf | awk '/Pages/{print $2}') pages"; done
