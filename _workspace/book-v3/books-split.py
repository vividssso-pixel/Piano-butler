# Split the Handbook and Workbook into one PDF per chapter, plus a card gallery like printables.html
import os, subprocess, html
from pypdf import PdfReader, PdfWriter
O = '/mnt/user-data/outputs/books-latest/'
SRC = {'hbP': '/mnt/user-data/outputs/handbook-part1-pitch.pdf', 'hbT': '/mnt/user-data/outputs/handbook-part2-time.pdf', 'wbP': '/mnt/user-data/outputs/workbook-pitch.pdf', 'wbT': '/mnt/user-data/outputs/workbook-time.pdf', 'hbX': '/mnt/user-data/outputs/house-rooms/handbook-tips.pdf', 'hbH': '/mnt/user-data/outputs/handbook-part5-chords.pdf', 'hbM': '/mnt/user-data/outputs/handbook-part6-harmony.pdf', 'hbS': '/mnt/user-data/outputs/handbook-part4-scales.pdf', 'hbE': '/mnt/user-data/outputs/handbook-part3-expression.pdf', 'wbE': '/mnt/user-data/outputs/workbook-expression.pdf', 'wbF': '/mnt/user-data/outputs/workbook-shape.pdf', 'wbL': '/mnt/user-data/outputs/workbook-play.pdf', 'hbF': '/mnt/user-data/outputs/handbook-part7-shape.pdf', 'hbL': '/mnt/user-data/outputs/handbook-part8-playing.pdf', 'wbS': '/mnt/user-data/outputs/workbook-scales.pdf', 'wbH': '/mnt/user-data/outputs/workbook-harmony.pdf'}
# chapter: (part, n, title, blurb, handbook pages in its PDF (1-based), printed pp, workbook pages, workbook printed pp)
import sys as _sy; _sy.path.insert(0, '/tmp/claude-0/pk'); import pagemap as PM
def HB(keys):   # pdf pages (1-based, opener = 1) and printed pages of a run of topics, from the page map
    o = PM.PAGE[keys[0][0] + 'O']; pg = []
    for k in keys:
        a, n = PM.pages_of(k); pg += list(range(a, a + n))
    return [x - o + 1 for x in pg], (f'{pg[0]}–{pg[-1]}' if len(pg) > 1 else str(pg[0]))
CH = [
 ('Pitch', 1, 'The keyboard', 'High and low, the groups of two and three black keys, the letters going round, the eight Cs.', 'hbP', *HB(['P1']), 'wbP', [1, 2], '1–2'),
 ('Pitch', 2, 'The staff and the clefs', 'Lines and spaces, the treble and bass clefs, the grand staff, Middle C between the staves.', 'hbP', *HB(['P2']), 'wbP', [3, 4], '3–4'),
 ('Pitch', 3, 'The staff and the keyboard', 'Every line and space is one white key: from the page to the key and back.', 'hbP', *HB(['P3']), 'wbP', [5, 6], '5–6'),
 ('Pitch', 4, 'Reading the notes', 'Read any note from treble G, bass F or Middle C: step or skip; the sentences for lines and spaces.', 'hbP', *HB(['P4']), 'wbP', [7, 8], '7–8'),
 ('Pitch', 5, 'Ledger lines', 'Notes above and below the staff; Middle C written two ways; 8va.', 'hbP', *HB(['P5']), 'wbP', [9, 10], '9–10'),
 ('Pitch', 6, 'Sharps, flats and naturals', 'A semitone right or left, how long a sign lasts, two names for one key.', 'hbP', *HB(['P6']), 'wbP', [11, 12], '11–12'),
 ('Pitch', 7, 'Counting intervals', 'Count the notes for the number; tones and semitones.', 'hbP', *HB(['P7']), 'wbP', [13, 14], '13–14'),
 ('Pitch', 8, 'Major, minor and perfect', 'Count the keys between for the size.', 'hbP', *HB(['P8']), 'wbP', [15, 16], '15–16'),
 ('Time', 1, 'Pulse and the bar', 'The steady beat, tempo, strong beats and bar lines.', 'hbT', *HB(['T1']), 'wbT', [1, 2], '1–2'),
 ('Time', 2, 'Notes and rests', 'Every note value and its rest, and their other names.', 'hbT', *HB(['T2']), 'wbT', [3, 4], '3–4'),
 ('Time', 3, 'How long is a note?', 'Adding values, dots and ties.', 'hbT', *HB(['T3']), 'wbT', [5, 6], '5–6'),
 ('Time', 4, 'Time signatures', 'Simple time: the top and bottom numbers, changing time.', 'hbT', *HB(['T4']), 'wbT', [7, 8], '7–8'),
 ('Time', 5, 'Compound and irregular time', '6/8, 9/8, 12/8; 5/4, 7/8 and 3 + 3 + 2.', 'hbT', *HB(['T5']), 'wbT', [9, 10], '9–10'),
 ('Time', 6, 'Groups and upbeats', 'Beams, upbeats, triplets, duplets and semiquavers.', 'hbT', *HB(['T6']), 'wbT', [11, 12], '11–12'),
 ('Time', 7, 'Off the beat', 'Syncopation, swing, hemiola, polyrhythm and rubato.', 'hbT', *HB(['T7']), 'wbT', [13, 14], '13–14'),
 ('Time', 8, 'Repeats and road signs', 'Repeat signs, 1st and 2nd time bars, D.C., D.S., Fine and Coda.', 'hbT', *HB(['T8']), 'wbT', [15], '15'),
 ('Expr', 1, 'Loud and soft', 'Dynamics from pp to ff, hairpins, cresc. and dim., sfz and fp.', 'hbE', *HB(['E1']), 'wbE', [1, 2], '1–2'),
 ('Expr', 2, 'Touch: smooth, short, strong', 'Slurs and phrases, staccato, tenuto, accents, two-note slurs, mood words.', 'hbE', *HB(['E2']), 'wbE', [3, 4], '3–4'),
 ('Expr', 3, 'Speed words', 'Tempo words from Largo to Presto, the metronome mark, rit., accel., a tempo and the fermata.', 'hbE', *HB(['E3']), 'wbE', [5, 6], '5–6'),
 ('Expr', 4, 'The pedals', 'The sustain pedal, Ped. and *, changing the pedal, the soft pedal.', 'hbE', *HB(['E4']), 'wbE', [7, 8], '7–8'),
 ('Expr', 5, 'Ornaments', 'Trills, mordents, turns, acciaccaturas and appoggiaturas, written and played.', 'hbE', *HB(['E5']), 'wbE', [9, 10], '9–10'),
 ('Scales', 1, 'Scales and keys', 'Major and minor scales, key signatures, finding the key, the circle of fifths.', 'hbS', *HB(['S1', 'S2', 'S3', 'S4', 'S5']), 'wbS', [1, 2], '1–2'),
 ('Harmony', 1, 'Chords and triads', 'Root, 3rd and 5th; play one, skip one; solid and broken chords.', 'hbH', *HB(['H1']), 'wbH', [1, 2], '1–2'),
 ('Harmony', 2, 'Four kinds of triad', 'Major, minor, diminished and augmented: counting the keys in between.', 'hbH', *HB(['H2']), 'wbH', [3, 4], '3–4'),
 ('Harmony', 3, 'Chords in a key', 'Roman numerals, the primary chords I, IV and V, chords in a minor key, the twelve-bar blues.', 'hbH', *HB(['H3']), 'wbH', [5, 6], '5–6'),
 ('Harmony', 4, 'Inversions', 'Root position, 1st and 2nd inversion, slash chords, smooth chord changes.', 'hbH', *HB(['H4']), 'wbH', [7, 8], '7–8'),
 ('Harmony', 5, 'Seventh chords', 'One more floor: maj7, 7, m7, ø7 and °7; sevenths in a key; why G7 pulls home.', 'hbH', *HB(['H5']), 'wbH', [9, 10], '9–10'),
 ('Harmony', 6, 'Colour chords', 'sus2, sus4, power chords, 6 and add9: move the 3rd, drop it, or add one note.', 'hbH', *HB(['H6']), 'wbH', [11, 12], '11–12'),
 ('Harmony', 7, 'The tower: 9, 11, 13', 'Keep stacking 3rds: ninths, elevenths and thirteenths, and which notes to leave out.', 'hbH', *HB(['H7']), 'wbH', [13, 14], '13–14'),
 ('Harmony', 8, 'Slash chords', 'C/E and its four jobs: inversions, walk-downs, pedals and colour basses.', 'hbH', *HB(['H8']), 'wbH', [15, 16], '15–16'),
 ('Music', 1, 'Chords from outside the key', 'Guest chords: V of V, borrowed chords, ♭VII, ♭VI, the Neapolitan and the augmented 6th.', 'hbM', *HB(['M1']), 'wbH', [17, 18], '17–18'),
 ('Music', 2, 'Cadences', 'Musical punctuation: perfect, plagal, imperfect and interrupted cadences.', 'hbM', *HB(['M2']), 'wbH', [19, 20], '19–20'),
 ('Music', 3, 'Chords under a melody', 'Which snowman holds the note; Twinkle with its chords; block, broken and Alberti bass.', 'hbM', *HB(['M3']), 'wbH', [21, 22], '21–22'),
 ('Music', 4, 'Progressions everywhere', 'The famous chord trips by number: the pop four, the fifties, the jazz three-step, the canon; same trip in any key.', 'hbM', *HB(['M4']), 'wbH', [23, 24], '23–24'),
 ('Shape', 1, 'Motifs and phrases', 'Motifs, 4-bar phrases, question and answer.', 'hbF', *HB(['F1']), 'wbF', [1, 2], '1–2'),
 ('Shape', 2, 'Repetition and sequence', 'Repetition, sequences, imitation and contrast.', 'hbF', *HB(['F2']), 'wbF', [3, 4], '3–4'),
 ('Shape', 3, 'Texture', 'One line, melody and accompaniment, Alberti bass, polyphony.', 'hbF', *HB(['F3']), 'wbF', [5, 6], '5–6'),
 ('Shape', 4, 'Changing key', 'Modulation to the nearest keys and how to spot it.', 'hbF', *HB(['F4']), 'wbF', [7, 8], '7–8'),
 ('Shape', 5, 'Form', 'Binary, ternary, rondo, variations, strophic, verse and chorus.', 'hbF', *HB(['F5']), 'wbF', [9, 10], '9–10'),
 ('Shape', 6, 'Styles through time', 'Baroque, Classical, Romantic and Modern, and how to play each.', 'hbF', *HB(['F6']), 'wbF', [11, 12], '11–12'),
 ('Play', 1, 'Fingering', 'Finger numbers, five-finger position, thumb under and finger over.', 'hbL', *HB(['L1']), 'wbL', [1, 2], '1–2'),
 ('Play', 2, 'Practising well', 'A fifteen-minute plan, chunks, the metronome ladder.', 'hbL', *HB(['L2']), 'wbL', [3, 4], '3–4'),
 ('Play', 3, 'Sight-reading', 'The thirty-second scan, patterns, keeping going.', 'hbL', *HB(['L3']), 'wbL', [5, 6], '5–6'),
 ('Play', 4, 'Listening', 'Major or minor, intervals by song, finished or not, clapping back.', 'hbL', *HB(['L4']), 'wbL', [7, 8], '7–8'),
 ('Play', 5, 'Performing', 'A routine, recovering from slips, playing from memory.', 'hbL', *HB(['L5']), 'wbL', [9, 10], '9–10'),
]
EXTRA = [('hb', 'Pitch', 'Part I opener', 'hbP', [1], 'The map of Part I and its contents.'), ('hb', 'Time', 'Part II opener', 'hbT', [1], 'The map of Part II and its contents.'), ('hb', 'Expr', 'Part III opener', 'hbE', [1], 'The map of Part III and its contents.'), ('hb', 'Scales', 'Part IV opener', 'hbS', [1], 'The map of Part IV and its contents.'), ('hb', 'Harmony', 'Part V opener', 'hbH', [1], 'The map of Part V and its contents.'), ('hb', 'Music', 'Part VI opener', 'hbM', [1], 'The map of Part VI and its contents.'), ('hb', 'Shape', 'Part VII opener', 'hbF', [1], 'The map of Part VII and its contents.'), ('hb', 'Play', 'Part VIII opener', 'hbL', [1], 'The map of Part VIII and its contents.'), ('hb', 'Shape', 'Tips: when a piece goes nowhere', 'hbF', HB(['FT'])[0], f'The end of Part VII (p. {PM.PAGE["FT"]}).'), ('hb', 'Play', 'Tips: when practice isn’t working', 'hbL', HB(['LT'])[0], f'The end of Part VIII (p. {PM.PAGE["LT"]}).'),
         ('hb', 'Pitch', 'Tips: when a note reads wrong', 'hbP', HB(['PT'])[0], f'The end of Part I: the usual reading slips, what to check, and where to turn (p. {PM.PAGE["PT"]}).'), ('hb', 'Time', 'Tips: when the rhythm slips', 'hbT', HB(['TT'])[0], f'The end of Part II: what to check when the rhythm slips, and four ways to steady it (p. {PM.PAGE["TT"]}).'), ('hb', 'Expr', 'Tips: when your playing sounds flat', 'hbE', HB(['ET'])[0], f'The end of Part III: what to check when every note is right but the music sounds flat (p. {PM.PAGE["ET"]}).'), ('hb', 'Scales', 'Tips: when a note sounds wrong', 'hbS', HB(['ST'])[0], f'The end of Part IV: the usual key slips, what to check, and where to turn (p. {PM.PAGE["ST"]}).'), ('hb', 'Harmony', 'Tips: when a chord sounds wrong', 'hbH', HB(['HT'])[0], f'The end of Part V: the usual chord slips, what to check, and where to turn (p. {PM.PAGE["HT"]}).'), ('hb', 'Music', 'Tips: when the harmony goes wrong', 'hbM', HB(['MT'])[0], f'The end of Part VI: endings, guests, the left hand against the tune, and four ways to hear the harmony (p. {PM.PAGE["MT"]}).'),
         ('hb', 'Harmony', 'Putting it together', 'hbX', [1, 2], 'The closing pages of the Handbook: everything one note tells you; when a passage won’t come right (pp. ' + f'{PM.PAGE["X"]}–{PM.PAGE["X"] + 1}' + ').'), ('wb', 'Harmony', 'Answers', 'wbH', [25, 26], 'Every answer, Harmony 1–12.'),
         ('wb', 'Pitch', 'Review, progress and answers', 'wbP', [17, 18, 19], 'A ten-minute review, the progress chart and every answer.'), ('wb', 'Time', 'Review, progress and answers', 'wbT', [15, 16, 17], 'A ten-minute review, the progress chart and every answer.'), ('wb', 'Scales', 'Review, progress and answers', 'wbS', [3, 4, 5], 'A ten-minute review, the progress chart and every answer.'), ('wb', 'Expr', 'Review, progress and answers', 'wbE', [11, 12, 13], 'A ten-minute review, the progress chart and every answer.'), ('wb', 'Shape', 'Review, progress and answers', 'wbF', [13, 14, 15], 'A ten-minute review, the progress chart and every answer.'), ('wb', 'Play', 'Review, progress and answers', 'wbL', [11, 12, 13], 'A ten-minute review, the progress chart and every answer.')]
PNUM = {'Pitch': '1', 'Time': '2', 'Expr': '3', 'Scales': '4', 'Harmony': '5', 'Music': '6', 'Shape': '7', 'Play': '8'}
R = {k: PdfReader(v) for k, v in SRC.items()}
def slug(x): return ''.join(c if c.isalnum() else '-' for c in x.lower()).strip('-').replace('--', '-')
def cut(src, pages, path):
    os.makedirs(os.path.dirname(path), exist_ok=True); w = PdfWriter()
    for p in pages: w.add_page(R[src].pages[p - 1])
    w.write(path)
def thumb(src, page, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=82', '-r', '60', '-f', str(page), '-l', str(page), '-singlefile', SRC[src], path[:-4]], check=True)
cards = {'hb': {'Pitch': [], 'Time': [], 'Expr': [], 'Scales': [], 'Harmony': [], 'Music': [], 'Shape': [], 'Play': [], 'Tips': []}, 'wb': {'Pitch': [], 'Time': [], 'Expr': [], 'Scales': [], 'Harmony': [], 'Shape': [], 'Play': []}}
PARTN = {'Pitch': 'Part I · Pitch', 'Time': 'Part II · Time', 'Expr': 'Part III · Expression', 'Scales': 'Part IV · Scales and keys', 'Harmony': 'Part V · Chords', 'Music': 'Part VI · Harmony in music', 'Shape': 'Part VII · Shape and style', 'Play': 'Part VIII · Playing and listening', 'Tips': 'Tips'}
WBN = {'Expr': 'Expression', 'Shape': 'Shape and style', 'Play': 'Playing and listening', 'Pitch': 'Pitch', 'Time': 'Time', 'Scales': 'Scales and keys', 'Harmony': 'Chords and harmony', 'Music': 'Chords and harmony'}
WBP = lambda p: 'Harmony' if p == 'Music' else p   # one workbook for Parts V and VI (Expression has none yet)
for part, n, title, blurb, hs, hp, hpp, ws, wp, wpp in CH:
    base = f'{PNUM[part]}-{n}-{slug(title)}'
    hf = f'1 Handbook/{PARTN[part].replace(" · ", " ")}/handbook-{base}.pdf'; wf = f'2 Workbook/{WBN.get(part, part)}/workbook-{base}.pdf'
    cut(hs, hp, O + hf); thumb(hs, hp[0], O + f'_thumbs/hb-{base}.jpg')
    if ws: cut(ws, wp, O + wf); thumb(ws, wp[0], O + f'_thumbs/wb-{base}.jpg')
    cards['hb'][part].append((f'Chapter {n} · {PARTN[part].split(" · ")[1]}', title, blurb, hf, f'_thumbs/hb-{base}.jpg', f'p. {hpp}' if '–' not in hpp else f'pp. {hpp}', len(hp)))
    if ws: cards['wb'][WBP(part)].append((f'Chapter {n + (8 if part == "Music" else 0)} · {WBN[part]}', title, blurb, wf, f'_thumbs/wb-{base}.jpg', f'pp. {wpp}', len(wp)))
for kind, part, title, src, pages, blurb in EXTRA:
    base = f'{PNUM[part]}-0-{slug(title)}' if kind == 'hb' else f'{PNUM[part]}-9-{slug(title)}'
    f = (f'1 Handbook/{PARTN[part].replace(" · ", " ")}/handbook-{base}.pdf' if kind == 'hb' else f'2 Workbook/{WBN.get(part, part)}/workbook-{base}.pdf')
    cut(src, pages, O + f); thumb(src, pages[0], O + f'_thumbs/{kind}-{base}.jpg')
    c = (WBN.get(part, 'Expression'), title, blurb, f, f'_thumbs/{kind}-{base}.jpg', '', len(pages))
    (cards[kind][part if kind == 'hb' else WBP(part)].insert(0, c) if kind == 'hb' and 'opener' in title else cards[kind][part if kind == 'hb' else WBP(part)].append(c))
E = lambda x: html.escape(x, quote=True)
def card(c):
    lab, title, blurb, f, th, pp, n = c
    return f'''<div class="card"><a class="sheet" href="{E(f)}" target="_blank"><img src="{E(th)}" alt="" loading="lazy"></a><div class="txt"><div class="topic">{E(lab)}</div><h3>{E(title)}</h3><p>{E(blurb)}</p>
<div class="foot"><span class="meta">{n} {"page" if n == 1 else "pages"}{" · " + E(pp) if pp else ""}</span><a class="btn" href="{E(f)}" target="_blank">Open</a></div></div></div>'''
BOOKS = [('hbP', 'hb', 'Pitch', 'The Piano Butler Handbook', 'Part I', 'Pitch', 'The keyboard, the staff, reading the notes, sharps and flats, intervals', 'Whole books (later)/handbook-part1-pitch.pdf'),
         ('wbP', 'wb', 'Pitch', 'The Piano Butler Workbook', 'Workbook', 'Pitch', 'Learn and Use pages for every Pitch chapter, review and answers', 'Whole books (later)/workbook-pitch.pdf'),
         ('hbT', 'hb', 'Time', 'The Piano Butler Handbook', 'Part II', 'Time', 'Pulse, note values, time signatures and rhythm', 'Whole books (later)/handbook-part2-time.pdf'),
         ('wbT', 'wb', 'Time', 'The Piano Butler Workbook', 'Workbook', 'Time', 'Learn and Use pages for every Time chapter, review and answers', 'Whole books (later)/workbook-time.pdf'),
         ('hbE', 'hb', 'Expr', 'The Piano Butler Handbook', 'Part III', 'Expression', 'Dynamics, touch, speed words, the pedals and ornaments', 'Whole books (later)/handbook-part3-expression.pdf'),
         ('wbE', 'wb', 'Expr', 'The Piano Butler Workbook', 'Workbook', 'Expression', 'Learn and Use pages for every Expression chapter, review and answers', 'Whole books (later)/workbook-expression.pdf'),
         ('hbS', 'hb', 'Scales', 'The Piano Butler Handbook', 'Part IV', 'Scales and keys', 'Major and minor scales, key signatures, the circle of fifths', 'Whole books (later)/handbook-part4-scales.pdf'),
         ('wbS', 'wb', 'Scales', 'The Piano Butler Workbook', 'Workbook', 'Scales and keys', 'Learn and Use pages for scales and keys, review and answers', 'Whole books (later)/workbook-scales.pdf'),
         ('hbH', 'hb', 'Harmony', 'The Piano Butler Handbook', 'Part V', 'Chords', 'Triads, the four kinds, chords in a key, inversions, sevenths, colour chords, 9 11 13, slash chords', 'Whole books (later)/handbook-part5-chords.pdf'),
         ('hbM', 'hb', 'Music', 'The Piano Butler Handbook', 'Part VI', 'Harmony in music', 'Guest chords, cadences, chords under a melody, famous progressions', 'Whole books (later)/handbook-part6-harmony.pdf'),
         ('wbH', 'wb', 'Harmony', 'The Piano Butler Workbook', 'Workbook', 'Chords and harmony', 'Learn and Use pages for Chords and for Harmony in music', 'Whole books (later)/workbook-harmony.pdf'),
         ('hbF', 'hb', 'Shape', 'The Piano Butler Handbook', 'Part VII', 'Shape and style', 'Motifs, phrases, texture, changing key, form and styles', 'Whole books (later)/handbook-part7-shape.pdf'),
         ('wbF', 'wb', 'Shape', 'The Piano Butler Workbook', 'Workbook', 'Shape and style', 'Learn and Use pages for every Shape and style chapter, review and answers', 'Whole books (later)/workbook-shape.pdf'),
         ('hbL', 'hb', 'Play', 'The Piano Butler Handbook', 'Part VIII', 'Playing and listening', 'Fingering, practising, sight-reading, listening and performing', 'Whole books (later)/handbook-part8-playing.pdf'),
         ('wbL', 'wb', 'Play', 'The Piano Butler Workbook', 'Workbook', 'Playing and listening', 'Learn and Use pages for every Playing and listening chapter, review and answers', 'Whole books (later)/workbook-play.pdf')]
# the Music Box songbook (her 10 Nov 23:55), when its shelf.json is there: made by _workspace/musicbox/mbshelf.py
if os.path.exists(O + '4 Music Box/shelf.json'):
    import json as _json; _MB = _json.load(open(O + '4 Music Box/shelf.json'))
    cards['mb'] = {'Songs': [tuple(c) for c in _MB['cards']]}; BOOKS.append(tuple(_MB['book']))
TS = lambda t: (' style="font-size:10cqw;line-height:11.5cqw;white-space:normal"' if len(t) > 15 else ' style="font-size:10cqw;line-height:12.5cqw"') if len(t) > 10 else ''   # her 5 Nov: long titles (Scales and keys) stay inside the frame
def cover(b):
    k, kind, part, series, kick, title, blurb, whole = b
    n = len(cards[kind][part]); acc = '#e4572e' if kind in ('wb', 'mb') else '#f4a9bb'; ink = '#26296b' if kind in ('wb', 'mb') else '#fffdf7'
    return f"""<button type="button" class="book" data-book="{k}" aria-expanded="false"><span class="cv {'wb mb' if kind == 'mb' else kind}"><span class="fr"><span class="se">{E(series)}</span><span class="ki" style="color:{acc}">{E(kick)}</span><span class="ti"{TS(title)}>{E(title)}</span><span class="dv"></span><span class="bl">{E(blurb)}</span><span class="bw"><svg viewBox="0 0 40 24" width="34" height="20"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{ink}" stroke-width="2" stroke-linejoin="round"/><path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{ink}" stroke-width="2" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.6" fill="{acc}"/></svg></span></span></span>
<span class="cap"><b>{E(kick if kind != 'wb' else 'Workbook')} · {E(title)}</b><span>{n} {("section" if n == 1 else "sections") if kind == "hb" else "songs" if kind == "mb" else "parts"} · tap to open</span></span></button>"""
def panel(b):
    k, kind, part, series, kick, title, blurb, whole = b
    return f"""<section class="panel" id="p-{k}" hidden><div class="ph"><h2>{E(series)} · {E(kick + ' · ' if kind == 'hb' else '')}{E(title)}</h2><a class="whole" href="{E(whole)}" target="_blank">The whole draft as one PDF</a></div>
<div class="grid">{''.join(card(c) for c in cards[kind][part])}</div></section>"""
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>The books</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap" rel="stylesheet">
<style>:root{{--cream:#faf6ec;--navy:#26296b;--dk:#1c1e4f;--navy-soft:#4a4d86;--muted:#6d6f9c;--line:#e8e1d0;--coral:#e4572e}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--cream);color:var(--navy);font-family:Inter,-apple-system,sans-serif;line-height:1.55}}
.wrap{{max-width:1100px;margin:0 auto;padding:28px 20px 72px}} h1,h2,h3{{font-family:'Playfair Display',Georgia,serif;margin:0}}
h1{{font-size:clamp(38px,6vw,60px);font-weight:900;line-height:1.02}} .lead{{font-size:17px;color:var(--navy-soft);margin:12px 0 0;max-width:40em}}
.shelf{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin-top:30px;padding-bottom:16px;border-bottom:8px solid #b59a68;box-shadow:0 4px 0 rgba(38,41,107,.12)}}
.book{{all:unset;cursor:pointer;display:flex;flex-direction:column;gap:10px}} .book:focus-visible .cv{{outline:3px solid var(--coral);outline-offset:4px}}
.cv{{display:block;aspect-ratio:210/297;background:var(--dk);border-radius:2px 6px 6px 2px;box-shadow:inset 6px 0 0 rgba(0,0,0,.25),0 8px 18px rgba(28,30,79,.25);transition:transform .2s;padding:9%;container-type:inline-size}}
.cv.wb{{background:linear-gradient(90deg,#efe6cf,#f8f1de 18%,#f3ead3);box-shadow:inset 6px 0 0 rgba(120,90,40,.18),0 8px 18px rgba(28,30,79,.18)}} .cv.wb .fr{{color:#26296b;border-color:rgba(38,41,107,.55);outline-color:rgba(38,41,107,.3)}} .cv.wb .dv{{border-color:#26296b}} .book:hover .cv,.book[aria-expanded=true] .cv{{transform:translateY(-8px)}} .book[aria-expanded=true] .cv{{outline:3px solid var(--coral);outline-offset:4px}}
.fr{{display:flex;flex-direction:column;height:100%;border:1.5px solid rgba(255,253,247,.7);outline:.6px solid rgba(255,253,247,.4);outline-offset:-6px;padding:14% 10% 10%;color:#fffdf7}}
.se{{font-size:4.4cqw;letter-spacing:.14em;text-transform:uppercase;opacity:.85}} .ki{{font-size:4.8cqw;font-weight:800;letter-spacing:.3em;text-transform:uppercase;margin-top:16%}}
.ti{{font-family:'Playfair Display',serif;font-weight:800;font-size:12.5cqw;line-height:1;margin-top:4px;white-space:nowrap}} .dv{{width:40%;height:4px;border-top:1px solid #fffdf7;border-bottom:1px solid #fffdf7;opacity:.7;margin:10% 0}}
.bl{{font-size:5.4cqw;line-height:1.45;opacity:.9;min-height:4.35em}} .bw{{margin-top:auto}}
.cap{{display:flex;flex-direction:column}} .cap b{{font-size:15px}} .cap span{{font-size:12.5px;color:var(--muted);font-weight:600}}
.panel{{margin-top:34px}} .ph{{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:1.5px solid var(--navy);padding-bottom:8px;margin-bottom:22px}} .ph h2{{font-size:clamp(24px,3.4vw,32px);font-weight:900}} .whole{{font-size:14px;font-weight:700;color:var(--navy-soft)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,210px),1fr));gap:24px 20px}} .card{{display:flex;flex-direction:column}}
.sheet{{display:block;background:#fff;border:1px solid var(--line);border-radius:4px;overflow:hidden;transition:transform .15s}} .sheet:hover{{transform:translateY(-3px)}} .sheet img{{display:block;width:100%;height:auto}}
.txt{{padding:12px 2px 0;display:flex;flex-direction:column;flex:1}} .topic{{font-size:12.5px;font-weight:700;color:var(--coral)}} h3{{font-size:19px;font-weight:800;margin:2px 0 6px;line-height:1.2}} .card p{{font-size:14px;color:var(--navy-soft);margin:0 0 8px}}
.foot{{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:10px}} .meta{{font-size:12.5px;color:var(--muted);font-weight:600}} .btn{{text-decoration:none;background:var(--coral);color:#fff;font-weight:700;font-size:14px;border-radius:999px;padding:7px 15px}}
.more{{margin-top:40px;display:flex;gap:10px;flex-wrap:wrap;align-items:center}} .more b{{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-right:4px}} .more a{{text-decoration:none;font-weight:700;font-size:14px;border:1.5px solid var(--navy);border-radius:999px;padding:7px 14px;background:#fffefa;color:var(--navy)}}
@media(max-width:700px){{.shelf{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
</style></head><body><div class="wrap"><h1>The books</h1><p class="lead">Drafts. Tap a book to see its chapters; every chapter opens as its own PDF.</p>
<div class="shelf">{''.join(cover(b) for b in BOOKS)}</div>
{''.join(panel(b) for b in BOOKS)}
<div class="more"><b>Where do I start?</b><a href="Where do I start - the Handbook check.pdf" target="_blank">The Handbook check (printable)</a></div>
<div class="more"><b>New books</b><a href="Whole books (later)/accompaniment-book-levels-1-3.pdf" target="_blank">The Butler’s Accompaniment Book, Levels 1–3</a></div>
<div class="more"><b>Activities and games</b><a href="3 Activities and games/rhythm-activities-games.pdf" target="_blank">Rhythm activities and games</a><a href="3 Activities and games/pitch-games.pdf" target="_blank">Pitch games</a></div>
</div><script>
document.querySelectorAll('.book').forEach(b => b.addEventListener('click', () => {{
  const k = b.dataset.book, on = b.getAttribute('aria-expanded') === 'true';
  document.querySelectorAll('.book').forEach(x => x.setAttribute('aria-expanded', 'false'));
  document.querySelectorAll('.panel').forEach(p => p.hidden = true);
  if (!on) {{ b.setAttribute('aria-expanded', 'true'); const p = document.getElementById('p-' + k); p.hidden = false; p.scrollIntoView({{behavior: 'smooth', block: 'start'}}); }}
}}));
</script></body></html>"""
open(O + 'index.html', 'w').write(page)
print(sum(len(v) for k in cards.values() for v in k.values()), 'cards')
