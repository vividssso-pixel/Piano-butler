# The opening pages of Music Box 3 -> md0.json
import json, copy
base = json.load(open('md1.json')); S = [json.load(open(f'md{i}.json')) for i in range(1, 10)]; src = json.load(open('md-sources.json'))
EY = {1: 'No letters: notes on five lines', 2: 'Quick pairs and dotted notes', 3: 'A sharp; a tune that falls and climbs', 4: 'The bass clef: chords as stacked notes', 5: 'Six counts; a minor home', 6: 'Two shapes in every left-hand bar', 7: 'A lead sheet: tune and chord names', 8: 'A lead sheet in swinging six', 9: 'Nothing but the tune and three names'}
LH = {1: 'Whole chords, in letters', 2: 'A chord on beats 1 and 3', 3: 'Bottom key, then the top two', 4: 'Whole chords, read from notes', 5: 'Two chords in a bar, read from notes', 6: 'Low note, then two notes, read from notes', 7: 'Yours to choose', 8: 'Yours to choose', 9: 'Yours to invent'}
U = {1: 'Unit 1 · Real notes for the right hand', 4: 'Unit 2 · Real notes for the left hand too', 7: 'Unit 3 · Only the tune and the chord names', 9: 'The last page'}
rows = ''
for i, s in enumerate(S, 1):
    if i in U: rows += f'<tr class="u"><td colspan="4">{U[i]}</td></tr>'
    rows += f'<tr><td class="n">{i if i < 9 else ""}</td><td><b>{s["title"]}</b></td><td>{EY[i]}</td><td>{LH[i]}</td></tr>'
p1 = f'''<div class="kick">Start here</div><h1>Music Box 3</h1><p class="byl">Eight songs and one old friend</p>
<div class="mb-intro"><p>Music Box 2 ended with one letter on the page. This book takes the last step, and then one more. First the notes stand <b>with no letters at all</b>, for both hands. Then the left hand disappears from the page, and <b>you decide what it plays</b>. That is the whole point of these three books.</p></div>
<div class="sp"></div><table class="ftb"><tr><th style="width:4%"></th><th style="width:36%">Song</th><th style="width:32%">What the eyes learn</th><th style="width:28%">What the left hand does</th></tr>{rows}</table>
<div class="sp"></div><p class="fp">The last page is <b>Twinkle</b> once more: the tune, three chord names, and nothing else. By then you will not need more.</p>'''
p2 = '''<div class="kick">Start here</div><h1>How to use this book</h1><p class="byl">For anyone learning without a teacher, and for teachers too</p>
<div class="say"><div class="ah">Finding a note without a letter</div><ul class="fl">
<li><b>Right hand, the treble clef (the Queen).</b> Her curl wraps round the second line from the bottom: that line is <b>G</b>.</li><li><b>Left hand, the bass clef (the King).</b> His two dots sit either side of the second line from the top: that line is <b>F</b>.</li>
<li><b>Middle C</b> sits on its own short line, just below the right-hand lines and just above the left-hand lines.</li><li><b>From any note you know</b>, count: line, space, line, space. Each step is the next white key.</li>
<li><b>Do not count every note.</b> Find the first one, then read the shape: up, down, step or jump.</li><li><b>♯ and ♭</b> are written in front of every note they change, every time.</li></ul></div>
<div class="sp"></div><div class="say"><div class="ah">Fingers</div><p>This book prints no finger numbers. Choose your own and <b>write them in pencil</b>. Three rules cover almost everything: keep the hand in one place for as long as the tune allows; when it must move, move on a long note; going up, the thumb can tuck under, and going down, a finger can step over.</p></div>
<div class="sp"></div><div class="say"><div class="ah">Two or three pages for every song</div><p>The <b>first page</b> gets you ready: the one new thing, the chords in the song with their keys, and five steps to practise in order. Then comes the song. Long songs run over two or three pages; the line that begins <i>Ready for the next song when</i> is always at the very end.</p></div>
<div class="sp"></div><div class="say"><div class="ah">If you get stuck</div><ol class="stp"><li>Play at <b>half the speed</b>. Then half of that.</li><li>Take <b>one line a day</b>.</li><li>In Unit 2, write the chord name over any left-hand shape you cannot read yet. Rub it out next week.</li></ol></div>
<div class="sp"></div><div class="say"><div class="ah">For teachers</div><p>Unit 3 is the destination of the series: a lead sheet, a table of chords and a menu of accompaniment patterns. The patterns are the ones taught, one at a time, across Music Box 1 and 2. Key signatures are not used yet; every accidental is written out.</p></div>'''
NOTE = {2: 'The first part only, played twice.', 3: 'The source gives no chords: they are this book’s own.', 4: 'The chorus.', 9: 'The tune as in Music Box 1 and 2. The chords are the usual three.'}
rows = ''.join(f'<tr><td class="n">{i if i < 9 else ""}</td><td><b>{t}</b><br>{c}</td><td>{s}</td><td>{NOTE.get(i, "Tune and chord names as in the source.")}</td></tr>' for i, (t, c, s) in enumerate(src, 1))
p3 = f'''<div class="kick">Start here</div><h1>Where the tunes come from</h1><p class="byl">Every melody in this book is taken straight from an open score</p>
<div class="mb-intro"><p style="font-size:16px">In this book nothing was typed in by hand. Each tune, and the chord names above it, was converted by a program from a published open score, then checked back against that score note by note.</p></div>
<div class="sp"></div><table class="ftb sm"><tr><th></th><th>Song</th><th>Taken from</th><th>What is different here</th></tr>{rows}</table>
<div class="sp"></div><p class="fp" style="font-size:13px">Some tunes are moved to a key with fewer black keys; the notes keep their distances. Where a source names a seventh chord, this book prints the plain chord. The left-hand shapes are this book’s own. Open scores: Nottingham Music Database.</p>'''
d = copy.deepcopy(base); d.update(id='md0', title='How this book works', lesson=0, label='Start here', page0=0)
for k in ('nokb', 'extra', 'split', 'steps', 'song_note'): d['gig'].pop(k, None)
d['gig']['front'] = [p1, p2, p3]
json.dump(d, open('md0.json', 'w'), ensure_ascii=False); print('front ok')
