# The opening pages of Music Box 2 -> mc0.json
import json, copy
base = json.load(open('mc1.json')); S = [json.load(open(f'mc{i}.json')) for i in range(1, 15)]; src = json.load(open('mc-sources.json'))
RH = {1: 'Letters inside the notes', 2: 'A start before bar 1; beamed pairs', 3: 'A hand that jumps; arrows ↑ ↓', 4: 'Finger 2 over the thumb', 5: 'Three beats; the scale fingering',
      6: 'Five lines, letters still inside; F♯', 7: 'Dotted notes on the lines', 8: 'Long notes; two hand places', 9: 'Quick beamed notes',
      10: 'A letter at the start of each bar only', 11: 'A letter at the start of each line only', 12: 'Sharps and flats without help', 13: 'Very quick notes', 14: 'One letter on the whole page'}
LH = {1: 'The C chord: three keys at once', 2: 'The G chord', 3: 'The F chord: C, F, G in a row', 4: 'Two chords in one bar', 5: 'Waltz: low, high, high',
      6: 'A new home, G: three chords there', 7: 'The fan: one key on each beat', 8: 'The fan in G; a first minor chord', 9: 'A tune of its own',
      10: 'A minor home: Am, G, F, E', 11: 'A bass that goes round and round', 12: 'Two keys rocking: bottom and top', 13: 'Hands pass the music to each other', 14: 'Six chords, with minor colours'}
U = {1: 'Unit 1 · The letters move inside the notes', 6: 'Unit 2 · The notes climb onto five lines', 10: 'Unit 3 · The letters fade away', 14: 'The last page'}
rows = ''
for i, s in enumerate(S, 1):
    if i in U: rows += f'<tr class="u"><td colspan="4">{U[i]}</td></tr>'
    rows += f'<tr><td class="n">{i if i < 14 else ""}</td><td><b>{s["title"]}</b></td><td>{RH[i]}</td><td>{LH[i]}</td></tr>'
p1 = f'''<div class="kick">Start here</div><h1>Music Box 2</h1><p class="byl">Thirteen songs and one old friend</p>
<div class="mb-intro"><p>In Music Box 1 you played from letters in boxes. In this book the letters slowly turn into <b>real notes</b>, and the left hand grows from one key into <b>whole chords that move</b>. One new thing in each song, never two. The last page is <b>Twinkle</b> again: same tune, new left hand, so you can hear how far you have come.</p></div>
<div class="sp"></div><table class="ftb"><tr><th style="width:4%"></th><th style="width:36%">Song</th><th style="width:32%">What the eyes learn</th><th style="width:28%">What the left hand learns</th></tr>{rows}</table>'''
p2 = '''<div class="kick">Start here</div><h1>How to use this book</h1><p class="byl">For anyone learning without a teacher, and for teachers too</p>
<div class="say"><div class="ah">Two pages for every song</div><p>The <b>left page</b> gets you ready: the one new thing, where each hand sits, how to read the page, and five steps to practise in order. The <b>right page</b> is the song. Do not skip the left page.</p></div>
<div class="sp"></div><div class="say"><div class="ah">How fast to go</div><p>About <b>one song a week</b>. Ten minutes every day is worth more than an hour on Sunday. Each right page ends with <i>Ready for the next song when</i>. When that line is true and the four boxes are ticked, turn the page. If not, stay: nothing is lost by staying.</p></div>
<div class="sp"></div><div class="say"><div class="ah">If you get stuck</div><ol class="stp"><li>Play at <b>half the speed</b>. Then half of that.</li><li>Take <b>one line a day</b>, not the whole song.</li><li>Go back one song and play it once for pleasure. It will feel easy now: that is what progress feels like.</li></ol></div>
<div class="sp"></div><div class="say"><div class="ah">What the signs mean</div><ul class="fl">
<li><b>Numbers above the notes</b>: fingers. 1 is the thumb, 5 the little finger, in both hands.</li><li><b>Numbers below the notes</b>: the count. Say it out loud.</li>
<li><b>A black note</b> lasts one box. <b>A white note with a stem</b> lasts two. <b>A white note with no stem</b> fills a bar of four.</li><li><b>A dot</b> after a note makes it half as long again. The short note after it comes late, on <i>and</i>.</li>
<li><b>Notes joined by a beam</b> are quick: two of them share one box.</li><li><b>♯</b> before a note: the black key just to its right. <b>♭</b>: the black key just to its left.</li>
<li><b>An arrow ↑ or ↓</b>: the higher or the lower key of that name.</li><li><b>Coral letters over the left hand</b>: the name of the chord. <b>m</b> means minor, the darker kind.</li>
<li><b>Letters stacked in a box</b>: play those keys together.</li><li><b>A ♯ just after the clef</b>: the key signature. It changes that note in every bar.</li><li><b>Two numbers after the clef</b>: the time signature. The top one is the beats in a bar.</li><li><b>A long line</b> after a note or chord: keep holding.</li></ul></div>
<div class="sp"></div><div class="say"><div class="ah">For teachers</div><p>Each song adds exactly one thing; the table on the first page names it. The left-hand patterns are the standard ways to accompany a melody, in order: whole chord, changing chord, split chord, broken chord, an independent line, a ground bass. The last box on each left page turns the song into a small arranging exercise.</p></div>'''
NOTE = {7: 'As in the Mutopia score.', 6: 'As in the sources. Line 1 is played twice.', 2: 'In the chorus the long A is as sung; the source repeats it.', 3: 'Two lead-in notes that fiddlers add between the halves are left out.', 4: 'Line 4 is the ending as sung; the source writes out lines 1 to 3.',
        5: 'Verse once, then the refrain.', 8: 'The whole chorus. One lead-in note that is not sung is left out.', 9: 'Complete. Three left-hand bars with two voices are written as one line.', 10: 'Verse and chorus. The source prints one F in the chorus without its ♯; here it has it.', 11: 'Four phrases of the first violin, then a closing C. The last beat of bar 8 is one note here.', 12: 'Theme, answer, theme, with the bass; repeats not written out.', 13: 'The whole first section, both hands as written, played once through.', 14: 'The tune as in Music Box 1; the chords are ours.'}
rows = ''.join(f'<tr><td class="n">{i if i < 14 else ""}</td><td><b>{t}</b><br>{c}</td><td>{s}</td><td>{NOTE.get(i, "As in the source.")}</td></tr>' for i, (t, c, s) in enumerate(src, 1))
p3 = f'''<div class="kick">Start here</div><h1>Where the tunes come from</h1><p class="byl">Every melody in this book was checked note by note against an open score</p>
<div class="mb-intro"><p style="font-size:16px">All fourteen tunes are old enough to belong to everyone. Each was compared, pitch by pitch and length by length, with a published open edition. Where this book differs, the last column says how.</p></div>
<div class="sp"></div><table class="ftb sm"><tr><th></th><th>Song</th><th>Checked against</th><th>What is different here</th></tr>{rows}</table>
<div class="sp"></div><p class="fp" style="font-size:13px">Some tunes are moved to a key that sits under the hand; the notes keep their distances. The left-hand chords and all the fingerings are this book’s own. Open scores: Mutopia Project (mutopiaproject.org), Nottingham Music Database, Essen Folksong Collection.</p>'''
d = copy.deepcopy(base); d.update(id='mc0', title='How this book works', lesson=0, label='Start here')
d['gig']['front'] = [p1, p2, p3]
json.dump(d, open('mc0.json', 'w'), ensure_ascii=False); print('front ok')
