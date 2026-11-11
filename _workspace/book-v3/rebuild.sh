#!/bin/bash
# Rebuild every book draft, check, render PDFs, merge, split, landing pages; then bundle under a fresh name in outputs/ship-<ts>/
set -e
P=/tmp/claude-0/pk; H=/mnt/user-data/outputs/house-rooms; O=/mnt/user-data/outputs
cd /tmp/e2e && node /tmp/claude-0/vrv/center.js $P/wp/wpout_raw.json $P/wp/wpout.json >/dev/null && node $P/wp/crop.js $P/wp/wpout.json $P/wp/wpout_c.json >/dev/null && node $P/wp/vcrop.js $P/wp/wpout_c.json $P/wp/wpout_v.json >/dev/null
cd $P && for f in book10.py pitch.py harmony.py tips.py expr.py shape.py; do python3 $f >/dev/null 2>&1 || { echo "FAIL $f"; exit 1; }; done
(cd /tmp/e2e && node $P/heroshot.js >/dev/null) || { echo "FAIL heroshot"; exit 1; }   # her 6 Nov: the chapter pictures for the workbook Learn pages
cd $P && for f in wbtime2.py wbpitch.py wbharm.py scbook.py acc.py accsnips.py accbook.py bank.py fun.py fun2.py pgames.py wbmore.py glossary.py checkbank.py checkbook.py checkonline.py relabel.py wbref.py; do python3 $f >/dev/null 2>&1 || { echo "FAIL $f"; exit 1; }; done   # relabel last: the workbooks re-run the handbook generators
N="accompaniment-sample accompaniment-book handbook-time2 handbook-expression handbook-shape handbook-play workbook-expression workbook-shape workbook-play handbook-glossary handbook-check handbook-pitch handbook-scales handbook-harmony handbook-harmony2 handbook-tips workbook-time2 workbook-pitch workbook-scales workbook-harmony scalebook activity-bank-rhythm free-printables-rhythm rhythm-games rhythm-games2 pitch-games"
cd /tmp/e2e && node $P/check.js $(for n in $N; do echo $H/$n.html; done)
node -e "
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const H='$H/';
for (const h of '$N'.split(' ')) {const p=await b.newPage();await p.goto('file://'+H+h+'.html');await p.waitForTimeout(1500);await p.pdf({path:H+(h==='pitch-games'?'pitch-games-draft':h)+'.pdf',format:'A4',printBackground:true});await p.close();}
await b.close()})()"
cp $H/handbook-pitch.pdf $O/handbook-part1-pitch.pdf; cp $H/handbook-time2.pdf $O/handbook-part2-time.pdf; cp $H/workbook-pitch.pdf $O/workbook-pitch.pdf; cp $H/workbook-time2.pdf $O/workbook-time.pdf; cp $H/pitch-games-draft.pdf $O/pitch-games-draft.pdf; rm -f $O/handbook-part3-harmony.pdf $O/handbook-part3-scales.pdf $O/handbook-part4-chords.pdf $O/handbook-part5-harmony.pdf; cp $H/handbook-expression.pdf $O/handbook-part3-expression.pdf; cp $H/handbook-scales.pdf $O/handbook-part4-scales.pdf; cp $H/workbook-scales.pdf $O/workbook-scales.pdf; rm -f $O/handbook-part4-harmony.pdf; cp $H/handbook-harmony.pdf $O/handbook-part5-chords.pdf; cp $H/handbook-harmony2.pdf $O/handbook-part6-harmony.pdf; cp $H/handbook-shape.pdf $O/handbook-part7-shape.pdf; cp $H/handbook-play.pdf $O/handbook-part8-playing.pdf; cp $H/workbook-expression.pdf $H/workbook-shape.pdf $H/workbook-play.pdf $O/; cp $H/workbook-harmony.pdf $O/workbook-harmony.pdf
cd $H && python3 - <<'PY'
from pypdf import PdfWriter, PdfReader
def merge(out, parts):
    w=PdfWriter(); pos=0
    for f,t in parts:
        r=PdfReader(f); w.append(r); w.add_outline_item(t,pos); pos+=len(r.pages)
    w.write(out)
O='/mnt/user-data/outputs/'
merge(O+'rhythm-activities-games.pdf',[('/tmp/claude-0/pk/col/cover.pdf','Cover and contents'),('activity-bank-rhythm.pdf','Activity bank · Rhythm 1–3'),('free-printables-rhythm.pdf','Free printables · Rhythm'),('rhythm-games.pdf','Rhythm games 1–4'),('rhythm-games2.pdf','Rhythm games 5–13')])
merge(O+'books/handbook-draft.pdf',[(O+'handbook-part1-pitch.pdf','Part I · Pitch'),(O+'handbook-part2-time.pdf','Part II · Time'),(O+'handbook-part3-expression.pdf','Part III · Expression'),(O+'handbook-part4-scales.pdf','Part IV · Scales and keys'),(O+'handbook-part5-chords.pdf','Part V · Chords'),(O+'handbook-part6-harmony.pdf','Part VI · Harmony in music'),(O+'handbook-part7-shape.pdf','Part VII · Shape and style'),(O+'handbook-part8-playing.pdf','Part VIII · Playing and listening'),(O+'house-rooms/handbook-tips.pdf','Putting it together'),(O+'house-rooms/handbook-glossary.pdf','Glossary and index')])
merge(O+'books/workbook-draft.pdf',[(O+'workbook-pitch.pdf','Pitch'),(O+'workbook-time.pdf','Time'),(O+'workbook-expression.pdf','Expression'),(O+'workbook-scales.pdf','Scales and keys'),(O+'workbook-harmony.pdf','Chords and harmony'),(O+'workbook-shape.pdf','Shape and style'),(O+'workbook-play.pdf','Playing and listening')])
PY
cp $O/rhythm-activities-games.pdf $O/books/; cp $O/pitch-games-draft.pdf $O/books/pitch-games.pdf
rm -rf $O/books-latest && python3 $P/split/split.py >/dev/null
mkdir -p "$O/books-latest/3 Activities and games" "$O/books-latest/Whole books (later)"
cp $O/rhythm-activities-games.pdf "$O/books-latest/3 Activities and games/"; cp $H/scalebook.pdf "$O/books-latest/Whole books (later)/scale-and-chord-book-draft.pdf"; cp $H/accompaniment-book.pdf "$O/books-latest/Whole books (later)/accompaniment-book-levels-1-3.pdf"; cp $O/pitch-games-draft.pdf "$O/books-latest/3 Activities and games/pitch-games.pdf"
cp $O/handbook-part1-pitch.pdf $O/handbook-part2-time.pdf $O/handbook-part3-expression.pdf $O/handbook-part4-scales.pdf $O/handbook-part5-chords.pdf $O/handbook-part6-harmony.pdf $O/handbook-part7-shape.pdf $O/handbook-part8-playing.pdf $H/handbook-tips.pdf $H/handbook-glossary.pdf $O/workbook-pitch.pdf $O/workbook-time.pdf $O/workbook-scales.pdf $O/workbook-harmony.pdf $O/workbook-expression.pdf $O/workbook-shape.pdf $O/workbook-play.pdf "$O/books-latest/Whole books (later)/"
cp $H/handbook-check.pdf "$O/books-latest/Where do I start - the Handbook check.pdf"
(cd /tmp/e2e && node $P/regions.js $P/regions.json $H/handbook-pitch.html $H/handbook-time2.html $H/handbook-expression.html $H/handbook-scales.html $H/handbook-harmony.html $H/handbook-harmony2.html $H/handbook-shape.html $H/handbook-play.html >/dev/null)
python3 $P/readpage.py --pages >/dev/null   # her 8 Nov: Read and listen, the Handbook online with the audio; cp $P/handbook-check-online.html $O/books/handbook-check.html; cp $H/handbook-check.pdf $O/books/handbook-check.pdf
python3 $P/pp/gen.py all >/dev/null
TS=$(date +%s); S=$O/ship-$TS; mkdir -p $S/src
(cd $O/books-latest && tar czf $S/books-latest.tgz .); (cd $O/printables-site && tar czf $S/printables.tgz printables); (cd $O && tar czf $S/books-dir.tgz --exclude=books/read books); (cd $O/books && tar czf $S/read.tgz read)
cp $P/book10.py $P/pitch.py $P/harmony.py $P/wbharm.py $P/mock_h7.py $P/tips.py $P/wp/wpsnips.json $P/wp/wpout_raw.json $P/tips/six_num.svg $P/wbtime2.py $P/wbpitch.py $P/bank.py $P/fun.py $P/fun2.py $P/pgames.py $P/check.js $P/heroshot.js $P/scbook.py $P/mock/secret.py $P/openart.py $P/split/split.py $P/rebuild.sh $P/mock/secret.py $P/mock/scales.py $P/pagemap.py $P/pitch_new.py $P/pitch_scales.py $P/acc.py $P/accsnips.py $P/accbook.py $P/ex/accsnips.json $P/ex/accout.json $P/time_t8.py $P/expr.py $P/shape.py $P/wbmore.py $P/glossary.py $P/readpage.py $P/regions.js /tmp/claude-0/tts/scripts.py /tmp/claude-0/tts/story.py /tmp/claude-0/tts/audio.py $P/checkbank.py $P/checkbook.py $P/checkonline.py $P/handbook-check-online.html $P/relabel.py $P/wbref.py $P/clock5.svg $P/ex/esnips.json $P/ex/eout.json /tmp/claude-0/vrv/vrve.mjs $P/kb.py $P/pp/gen.py $P/pp/items.py /tmp/claude-0/vrv/vrvp.mjs /tmp/claude-0/vrv/center.js /tmp/claude-0/vrv/psnips.json /tmp/claude-0/vrv/pout.json /tmp/claude-0/vrv/snips.json /tmp/claude-0/vrv/out.json /tmp/claude-0/vrv/wsnips.json /tmp/claude-0/vrv/wout.json /tmp/claude-0/vrv/vrv2.mjs /tmp/claude-0/vrv/tight.js $P/firstdone.py $P/wp/vcrop.js $P/wp/crop.js $S/src/
(cd $S && sleep 1 && { tar czf src.tgz --warning=no-file-changed src || true; } && rm -rf src)
echo "SHIP $S"
