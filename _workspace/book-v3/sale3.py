# The sale files rebuilt from the proofread books (her 17 Nov). Same products as sale2.py (her 15-16 Nov): each part =
# the Handbook part (with cover, copyright page, How to read this book) + its Workbook pages (with the Workbook front
# matter); the complete set with the Going further bonus; the free sampler. Page ranges come from the rendered parts
# (sale2.py read them from newmap.json, which was lost with the old workspace).
import json, os, zipfile, shutil
from pypdf import PdfReader, PdfWriter
P = '/mnt/user-data/outputs/pilot'; S = '/mnt/user-data/outputs/sale3/'
shutil.rmtree(S, ignore_errors=True); os.makedirs(S)
HB = PdfReader(f'{P}/full/handbook-new-draft.pdf'); WB = PdfReader(f'{P}/full/workbook-new-draft.pdf')
assert len(HB.pages) == 145 and len(WB.pages) == 142
R = lambda a, b: list(range(a, b + 1))
HBP = {'pitch': R(21, 37), 'time': R(38, 57), 'expression': R(58, 73), 'scales': R(74, 83), 'chords': R(84, 102), 'harmony': R(103, 113),
       'shape': R(114, 125), 'play': R(126, 137)}
def wbp(part): return sorted({x['pg'] for x in json.load(open(f'{P}/wb/{part}.map.json'))['pages']})
def wb_first(part, k): return [x['pg'] for x in json.load(open(f'{P}/wb/{part}.map.json'))['pages'] if x.get('k') == k]
HB_FRONT = [1, 3, 4, 17]; WB_FRONT = [1, 2, 3, 4]; AUTHOR = 'Piano Butler'
def write(path, reader, pages, title):
    w = PdfWriter()
    for n in pages: w.add_page(reader.pages[n - 1])
    w.add_metadata({'/Title': title, '/Author': AUTHOR, '/Subject': 'The Piano Butler · music theory for pianists · thepianobutler.com'})
    with open(path, 'wb') as f: w.write(f)
PRODUCTS = [  # slug, name, parts, listing blurb (search words welcome here, her 16 Nov)
 ('01-pitch', 'Pitch', ['pitch'], 'Reading notes on the piano: the keyboard and Middle C, treble and bass clef, ledger lines, sharps and flats, tones and semitones, intervals. Beginner to Grade 2.'),
 ('02-time', 'Time', ['time'], 'Rhythm for pianists: note values and rests, dotted notes and ties, pulse and tempo, time signatures, compound and irregular time, upbeats, triplets, syncopation, bar lines, repeats and road signs. Beginner to Grade 5.'),
 ('03-expression', 'Expression', ['expression'], 'Dynamics, crescendo and accents, staccato and legato, slurs and phrases, Italian speed and mood words, rit. and a tempo, the pedals, ornaments and grace notes. Beginner to Grade 3.'),
 ('04-scales-and-keys', 'Scales and keys', ['scales'], 'Major and minor scales, key signatures, relative minor, finding the key of a piece, the circle of fifths. Prelim to Grade 3.'),
 ('05-chords-and-harmony', 'Chords and harmony', ['chords', 'harmony'], 'Triads, chords in a key, primary chords I IV V, inversions, seventh, sus and added-note chords, slash chords, secondary dominants, borrowed chords, cadences, harmonising a melody, accompaniment patterns, chord progressions, the twelve-bar blues. Prelim to Grade 8.'),
 ('06-shape-and-style', 'Shape and style', ['shape'], 'Motifs, phrases, sequence and imitation, texture, modulation, binary, ternary and rondo form, musical periods from Baroque to Modern. Grade 2 to Grade 5.'),
 ('07-playing-and-listening', 'Playing and listening', ['play'], 'Piano fingering, how to practise, sight-reading, ear training (major or minor, intervals by song), performing and stage nerves, common piano mistakes and how to fix them.'),
]
info = []
for slug, name, parts, blurb in PRODUCTS:
    d = S + slug + '/'; os.makedirs(d)
    hp = HB_FRONT + [n for p in parts for n in HBP[p]]; wp = WB_FRONT + [n for p in parts for n in wbp(p)]
    write(d + f'Piano Butler Handbook - {name}.pdf', HB, hp, f'The Piano Butler Handbook · {name}')
    write(d + f'Piano Butler Workbook - {name}.pdf', WB, wp, f'The Piano Butler Workbook · {name}')
    info.append((slug, name, blurb, len(hp), len(wp)))
d = S + '00-complete-set/'; os.makedirs(d)
write(d + 'Piano Butler Handbook - complete.pdf', HB, R(1, 145), 'The Piano Butler Handbook')
write(d + 'Piano Butler Workbook - complete.pdf', WB, R(1, 142), 'The Piano Butler Workbook')
if os.path.exists('/mnt/user-data/outputs/workbook-further.pdf'):
    r = PdfReader('/mnt/user-data/outputs/workbook-further.pdf'); write(d + 'Bonus - Going further workbook pages.pdf', r, R(1, len(r.pages)), 'Bonus · Going further')
info.append(('00-complete-set', 'Complete set', 'Both whole books: every part, the glossary and index, and the Going further bonus (non-chord notes). Music theory for pianists from the first lesson to Grade 8.', 145, 142))
d = S + '99-free-sampler/'; os.makedirs(d)
FIRST = [('pitch', 'P1', 22), ('time', 'T1', 39), ('expression', 'E1', 59), ('scales', 'S1', 75), ('chords', 'H1', 85), ('shape', 'F1', 115), ('play', 'L1', 127)]
hp = HB_FRONT + [18, 19, 20] + [pg for _, _, pg in FIRST]
wp = WB_FRONT + [5, 6] + [n for p, k, _ in FIRST for n in wb_first(p, k)]
write(d + 'Piano Butler - free sampler (Handbook).pdf', HB, hp, 'The Piano Butler · free sampler (Handbook)')
write(d + 'Piano Butler - free sampler (Workbook).pdf', WB, wp, 'The Piano Butler · free sampler (Workbook)')
info.append(('99-free-sampler', 'Free sampler', 'Before you play, and the first chapter of every part, in both books.', len(hp), len(wp)))
for slug, *_ in info:
    with zipfile.ZipFile(S + slug + '.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for fn in sorted(os.listdir(S + slug)): zf.write(S + slug + '/' + fn, fn)
json.dump(info, open(S + 'products.json', 'w'), indent=1)
for i in info: print(i[0], 'HB', i[3], 'WB', i[4], round(os.path.getsize(S + i[0] + '.zip') / 1e6, 1), 'MB')
