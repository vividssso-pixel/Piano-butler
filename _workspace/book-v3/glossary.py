# The Piano Butler Handbook: glossary and index, after Putting it together (her 8 Nov: A, finish the Handbook).
# Glossary: one line per word, with the chapter page. Index: built from the finished Handbook pages (headings, bold words, table entries).
import re as _gr, html as _gh
exec(open('/tmp/claude-0/pk/book10.py').read())   # helpers, css, page() (rewrites the Time draft, harmless)
H = '/mnt/user-data/outputs/house-rooms/'
G = [  # (word, definition, chapter key)
 ('a tempo', 'back to the speed before', 'E3'), ('accelerando (accel.)', 'gradually faster', 'E3'), ('accent', 'a > over a note: start it more strongly', 'E2'),
 ('acciaccatura', 'a tiny note with a slash, crushed in as fast as possible', 'E5'), ('accidental', 'a sharp, flat or natural written before a note; it lasts until the bar line', 'P6'),
 ('Adagio', 'slow, at ease', 'E3'), ('Alberti bass', 'a broken chord in the left hand: low, high, middle, high (C G E G)', 'F3'), ('Allegro', 'fast and lively', 'E3'),
 ('anacrusis', 'an upbeat: notes before the first full bar', 'T6'), ('Andante', 'at a walking pace', 'E3'), ('appoggiatura', 'a tiny note without a slash; it leans, taking half the main note’s time. Also a note outside the chord that leans on the beat (p. {{G1}})', 'E5'),
 ('articulation', 'how notes are joined or separated: slurs, staccato, tenuto, accents', 'E2'), ('augmented triad', 'a triad with 3 + 3 keys between', 'H2'),
 ('Baroque', 'music of about 1600–1750: Bach, Handel', 'F6'), ('bar', 'a group of beats between two bar lines', 'T1'), ('bass clef', 'the F clef: its two dots hug the line for bass F', 'P2'),
 ('beam', 'a thick line joining quavers or semiquavers into a beat', 'T6'), ('beat', 'the steady pulse you count', 'T1'), ('binary form', 'two sections, A B', 'F5'),
 ('broken chord', 'the notes of a chord played one after another', 'H1'), ('cadence', 'the last two chords of a phrase: musical punctuation', 'M2'),
 ('cantabile', 'in a singing style', 'E2'), ('chord', 'three or more notes played together', 'H1'), ('circle of fifths', 'the keys in a circle: go right, one more sharp; go left, one more flat', 'S5'),
 ('Classical', 'music of about 1750–1820: Haydn, Mozart', 'F6'), ('clef', 'the sign at the start of the staff that names one line', 'P2'), ('coda', 'an ending section; jump to it at “To Coda”', 'T8'),
 ('compound time', 'each beat is a dotted note and divides into three (6/8, 9/8, 12/8)', 'T5'), ('crescendo (cresc.)', 'getting louder, little by little', 'E1'),
 ('crotchet', 'a note worth one beat in 4/4', 'T2'), ('da capo (D.C.)', '“from the head”: go back to the beginning', 'T8'), ('dal segno (D.S.)', '“from the sign”: go back to the segno', 'T8'),
 ('diminished triad', 'a triad with 2 + 2 keys between', 'H2'), ('diminuendo (dim.)', 'getting softer, little by little', 'E1'), ('dolce', 'sweetly', 'E2'),
 ('dominant', 'the 5th note of the scale, and the chord built on it (V)', 'H3'), ('dot', 'adds half the note’s value', 'T3'), ('duplet', 'two notes in the time of three', 'T6'),
 ('dynamics', 'the signs for loud and soft: pp p mp mf f ff', 'E1'), ('enharmonic', 'two names for one key, such as F♯ and G♭', 'P6'), ('fermata', 'a pause: hold the note longer than written', 'E3'),
 ('Fine', '“the end”: after a D.C. or D.S., stop here', 'T8'), ('five-finger position', 'one finger on each of five keys in a row', 'L1'), ('flat (♭)', 'the very next key to the left', 'P6'),
 ('form', 'the plan of a whole piece, in letters', 'F5'), ('forte (f)', 'loud', 'E1'), ('grand staff', 'treble and bass staves joined by a brace', 'P2'),
 ('hairpin', 'a crescendo or diminuendo sign that opens or closes', 'E1'), ('hemiola', 'two bars of three felt as three bars of two', 'T7'),
 ('homophonic', 'a tune with chords underneath', 'F3'), ('imitation', 'another hand or voice copies the idea', 'F2'), ('interval', 'the distance between two notes', 'P7'),
 ('inversion', 'a chord with a note other than the root at the bottom', 'H4'), ('key', 'the scale a piece is built on, and its home note', 'S3'),
 ('key signature', 'the sharps or flats at the start of every line', 'S3'), ('Largo', 'very slow and broad', 'E3'), ('leading note', 'the 7th note of the scale, one key below home', 'S1'),
 ('ledger line', 'a short line for a note above or below the staff', 'P5'), ('8va (ottava)', 'play the notes under the dotted line an octave higher', 'P5'), ('legato', 'smoothly joined', 'E2'), ('major scale', 'tone, tone, semitone, tone, tone, tone, semitone', 'S1'),
 ('major triad', 'a triad with 3 + 2 keys between', 'H2'), ('metronome mark', '♩ = 76: 76 beats in a minute', 'E3'), ('mezzo (m)', '“half”: mp half soft, mf half loud', 'E1'),
 ('Middle C', 'the C nearest the middle of the keyboard, on a ledger line between the staves', 'P1'), ('minim', 'a note worth two crotchets', 'T2'),
 ('minor scale', 'the major scale on the same note with 3, 6 and 7 one key lower', 'S2'), ('minor triad', 'a triad with 2 + 3 keys between', 'H2'), ('Moderato', 'at a moderate speed', 'E3'),
 ('modulation', 'changing key during a piece', 'F4'), ('monophonic', 'one line alone', 'F3'), ('mordent', 'the note, its neighbour above (or below), the note', 'E5'),
 ('motif', 'a short idea of 2 to 6 notes that comes back', 'F1'), ('natural (♮)', 'cancels a sharp or flat', 'P6'), ('octave', 'from one note to the next of the same name: 11 keys between', 'P8'),
 ('ornament', 'a small sign for a quick group of notes around the main note', 'E5'), ('pedal (sustain)', 'the right pedal: notes keep ringing until you lift it', 'E4'),
 ('perfect cadence', 'V to I: a full stop', 'M2'), ('imperfect cadence', 'ending on V: a comma', 'M2'), ('interrupted cadence', 'V to vi: a surprise', 'M2'), ('phrase', 'a musical sentence, often 4 bars', 'F1'), ('pianissimo (pp)', 'very soft', 'E1'), ('piano (p)', 'soft', 'E1'),
 ('plagal cadence', 'IV to I: the “Amen”', 'M2'), ('polyphonic', 'two or more tunes at once', 'F3'), ('Presto', 'very fast', 'E3'), ('progression', 'a trip from chord to chord', 'M4'),
 ('pulse', 'the steady beat underneath the music', 'T1'), ('quaver', 'half a crotchet', 'T2'), ('rallentando (rall.)', 'gradually slower', 'E3'), ('relative minor', 'the minor key with the same key signature, a minor 3rd below', 'S3'),
 ('repeat sign', 'two dots and a double bar: play the bars again', 'T8'), ('rest', 'a silence of a set length', 'T2'), ('ritardando (rit.)', 'gradually slower', 'E3'),
 ('Romantic', 'music of about 1820–1900: Chopin, Schumann', 'F6'), ('rondo', 'A B A C A: the first idea keeps coming back', 'F5'), ('root', 'the note a chord is built on and named after', 'H1'),
 ('rubato', 'time stretched and given back, for expression', 'T7'), ('scale', 'the notes of a key in order, up or down', 'S1'), ('semibreve', 'a whole note: four crotchets', 'T2'),
 ('semiquaver', 'half a quaver', 'T2'), ('semitone', 'the very next key: no key between', 'P1'), ('sequence', 'the same shape repeated higher or lower', 'F2'),
 ('seventh chord', 'a triad with one more 3rd on top', 'H5'), ('sforzando (sfz)', 'one note made suddenly strong', 'E1'), ('sharp (♯)', 'the very next key to the right', 'P6'),
 ('sight-reading', 'playing music at first sight', 'L3'), ('simple time', 'each beat divides into two (2/4, 3/4, 4/4)', 'T4'), ('slash chord', 'C/E: the chord, then the bass note', 'H8'),
 ('slur', 'a curve over different notes: join them', 'E2'), ('staccato', 'a dot: short, detached', 'E2'), ('staff', 'the five lines and four spaces music is written on', 'P2'),
 ('subdominant', 'the 4th note of the scale, and the chord built on it (IV)', 'H3'), ('swing', 'pairs of quavers played long–short', 'T7'), ('syncopation', 'the stress falls off the beat', 'T7'),
 ('tempo', 'the speed of the beat', 'T1'), ('tenuto', 'a line: hold the note its full length', 'E2'), ('ternary form', 'A B A: out, away and back', 'F5'),
 ('texture', 'how many lines sound at once, and how they fit', 'F3'), ('theme and variations', 'one tune, changed each time it returns', 'F5'), ('tie', 'a curve joining two notes of the same pitch: one longer sound', 'T3'),
 ('time signature', 'top: how many beats; bottom: which note gets one beat', 'T4'), ('tone', 'two semitones: one key between', 'P1'), ('tonic', 'the 1st note of the scale: home', 'S1'),
 ('treble clef', 'the G clef: it curls round the line for treble G', 'P2'), ('triad', 'three notes stacked: play one, skip one, play one', 'H1'), ('trill', 'the note and its neighbour above, back and forth quickly', 'E5'),
 ('triplet', 'three notes in the time of two', 'T6'), ('turn', 'above, the note, below, the note', 'E5'), ('twelve-bar blues', 'I I I I · IV IV I I · V IV I I (or V in the last bar, to go round again)', 'M4'),
 ('una corda (u.c.)', 'the left (soft) pedal', 'E4'), ('upbeat', 'see anacrusis', 'T6')]
G.sort(key=lambda x: x[0].lower().lstrip('(').replace('ö', 'o'))
# ---------- index: where each word appears in the Handbook ----------
FILES = ['handbook-pitch', 'handbook-time2', 'handbook-expression', 'handbook-scales', 'handbook-harmony', 'handbook-harmony2', 'handbook-shape', 'handbook-play']
PAGES = []   # (printed page, text of headings, bold words and table cells)
for f in FILES:
    h = open(H + f + '.html').read()
    for sec in _gr.split(r'(?=<section class="pg)', h)[1:]:
        m = _gr.search(r'<div class="foot"><span>(\d+)</span>', sec)
        if not m: continue
        keys = ' | '.join(_gr.sub(r'<[^>]+>', ' ', x) for x in _gr.findall(r'<(?:h1|h3|b|th|td)[^>]*>(.*?)</(?:h1|h3|b|th|td)>', sec, _gr.S))
        PAGES.append((int(m.group(1)), _gh.unescape(keys).lower()))
AMBIG = {'piano', 'fine', 'key', 'rest', 'bar', 'beat', 'tone', 'root', 'form', 'turn', 'tie', 'dot', 'flat', 'sharp', 'natural', 'scale', 'pulse', 'tempo', 'chord', 'interval', 'phrase', 'texture', 'staff', 'clef', 'ornament', 'accent', 'legato', 'slur', 'triad', 'motif', 'sequence', 'imitation', 'cadence', 'progression', 'dynamics', 'rubato', 'swing', 'beam', 'octave', 'semitone', 'pedal'}
def where(word, key):
    w = _gr.sub(r'\s*\(.*?\)', '', word).lower().strip()
    pat = _gr.compile(r'(?<![a-z])' + _gr.escape(w) + r'(?:s|es)?(?![a-z])')
    pg = sorted({p for p, t in PAGES if pat.search(t)})
    start = PM.PAGE[key]
    if w in AMBIG: pg = [p for p in pg if PM.PAGE[key[0] + 'O'] <= p <= PM.PAGE[key[0] + 'T']]   # common words: only within their own part
    pg = [p for p in pg if p != start]
    return [start] + sorted(set(pg))[:4]   # proofread 12 Nov: the page where it is explained always comes first
EXTRA = [('arpeggio', 'H1'), ('block chords', 'F3'), ('borrowed chord', 'M1'), ('C clef', 'P2'), ('common time', 'T4'), ('cut common time', 'T4'), ('degree names', 'S1'),
         ('first and second time bars', 'T8'), ('half pedal', 'E4'), ('harmonic minor', 'S2'), ('irregular time', 'T5'),
         ('melodic minor', 'S2'), ('power chord', 'H6'), ('sonata form', 'F5'), ('strophic', 'F5'), ('sus chord', 'H6'), ('metronome', 'L2'), ('mood words', 'E2'), ('performing', 'L5'), ('phrase mark', 'E2'), ('practising', 'L2'),
         ('Roman numerals', 'H3'), ('sostenuto', 'E4'), ('thumb under', 'L1'), ('two-note slur', 'E2'), ('verse and chorus', 'F5')]
IDX = sorted([(w, where(w, k)) for w, d, k in G if not d.startswith('see ')] + [(w, where(w, k)) for w, k in EXTRA], key=lambda x: x[0].lower())
# ---------- pages ----------
def gpage(inner, n, end=False): return page(inner, n, 'GLOSSARY AND INDEX').replace('<section class="pg">', '<section class="pg" data-end="1">' if end else '<section class="pg">', 1)
def gl(rows): return '<div class="gls">' + ''.join(f'<p><b>{w}</b> {d} <i>p.&#8202;{PM.PAGE[k]}</i></p>' for w, d, k in rows) + '</div>'
def ix(rows): return '<div class="idx">' + ''.join(f'<p><b>{w}</b> {", ".join(str(x) for x in pg)}</p>' for w, pg in rows) + '</div>'
GPP, IPP = 50, 96   # entries per page (tuned to fill each page)
def cut(L, sizes):
    out, i = [], 0
    for n in sizes:
        if i >= len(L): break
        out.append(L[i:i + n]); i += n
    while i < len(L): out.append(L[i:i + sizes[-1]]); i += sizes[-1]
    return out
gch = cut(G, [40, 47, 47]); ich = cut(IDX, [100, 130])
start = PM.PAGE['X'] + 2
out = []
for i, ch in enumerate(gch):
    out.append(gpage((head('Glossary', 'Glossary', 'Every musical word in the Handbook, in one line, with the page where it is explained.') if i == 0 else '<div class="kick">Glossary · continued</div>') + gl(ch), start + len(out)))
for i, ch in enumerate(ich):
    out.append(gpage((head('Index', 'Index', 'Where each word appears. The first page is where it is explained.') if i == 0 else '<div class="kick">Index · continued</div>') + ix(ch), start + len(out), i == len(ich) - 1))
GCSS = '.gls{column-count:2;column-gap:28px;font-size:13.5px;line-height:1.38} .gls p{margin:0 0 5px;break-inside:avoid} .gls b{color:#26296b} .gls i{font-style:normal;color:#e4572e;font-weight:700;font-size:12.5px;white-space:nowrap}' \
       ' .idx{column-count:3;column-gap:24px;font-size:13.5px;line-height:1.45} .idx p{margin:0 0 3px;break-inside:avoid} .idx b{color:#26296b;font-weight:700}'
open(H + 'handbook-glossary.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{GCSS}</style></head><body>{"".join(out)}</body></html>')
print('ok glossary', len(G), 'words,', len(IDX), 'index entries,', len(out), 'pages from p.', start)
