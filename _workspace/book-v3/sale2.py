# The sale files for the restructured books (her 16 Nov, option A): same products as sale.py (her 15 Nov), cut from the new
# Handbook (145 pp.) and Workbook (142 pp.). Each part = the Handbook part (cover, title, copyright, How to read this book)
# + its Workbook part (Workbook front matter). Plus the complete set (with the Going further bonus) and the free sampler.
import json, os, zipfile
from pypdf import PdfReader, PdfWriter
O = '/mnt/user-data/outputs/'; S = O + 'sale2/'; os.makedirs(S, exist_ok=True)
HB = PdfReader(O + 'pilot/full/handbook-new-draft.pdf'); WB = PdfReader(O + 'pilot/full/workbook-new-draft.pdf')
NM = json.load(open('/tmp/claude-0/pk/newmap.json'))
def hb_pages(*parts): return sorted({x['pg'] for p in parts for x in NM[p]})
def wb_pages(*parts): return sorted({x['pg'] for p in parts for x in json.load(open(f'{O}pilot/wb/{p}.map.json'))['pages']})
def first(part, k): return [x['pg'] for x in NM[part] if x['k'] == k]
def wb_first(part, k): return [x['pg'] for x in json.load(open(f'{O}pilot/wb/{part}.map.json'))['pages'] if x.get('k') == k]
HB_FRONT = [1, 3, 4, 17]; WB_FRONT = [1, 2, 3, 4]; AUTHOR = 'Clara Sohyun Park'
def write(path, reader, pages, title):
    w = PdfWriter()
    for n in pages: w.add_page(reader.pages[n - 1])
    w.add_metadata({'/Title': title, '/Author': AUTHOR, '/Subject': 'The Piano Butler · music theory for pianists · thepianobutler.com'})
    with open(path, 'wb') as f: w.write(f)
PRODUCTS = [  # slug, name, Handbook parts, Workbook parts, listing blurb (search words welcome here, her 16 Nov)
 ('01-pitch', 'Pitch', ['pitch'], ['pitch'], 'Reading notes on the piano: the keyboard and Middle C, treble and bass clef, ledger lines, sharps and flats, tones and semitones, intervals. Beginner to Grade 2.'),
 ('02-time', 'Time', ['time'], ['time'], 'Rhythm for pianists: note values and rests, dotted notes and ties, pulse and tempo, time signatures, compound and irregular time, upbeats, triplets, syncopation, bar lines, repeats and road signs. Beginner to Grade 5.'),
 ('03-expression', 'Expression', ['expression'], ['expression'], 'Dynamics, crescendo and accents, staccato and legato, slurs and phrases, Italian speed and mood words, rit. and a tempo, the pedals, ornaments and grace notes. Beginner to Grade 3.'),
 ('04-scales-and-keys', 'Scales and keys', ['scales'], ['scales'], 'Major and minor scales, key signatures, relative minor, finding the key of a piece, the circle of fifths. Prelim to Grade 3.'),
 ('05-chords-and-harmony', 'Chords and harmony', ['chords', 'harmony'], ['chords', 'harmony'], 'Triads, chords in a key, primary chords I IV V, inversions, seventh, sus and added-note chords, slash chords, secondary dominants, borrowed chords, cadences, harmonising a melody, accompaniment patterns, chord progressions, the twelve-bar blues. Prelim to Grade 8.'),
 ('06-shape-and-style', 'Shape and style', ['shape'], ['shape'], 'Motifs, phrases, sequence and imitation, texture, modulation, binary, ternary and rondo form, musical periods from Baroque to Modern. Grade 2 to Grade 5.'),
 ('07-playing-and-listening', 'Playing and listening', ['play'], ['play'], 'Piano fingering, how to practise, sight-reading, ear training (major or minor, intervals by song), performing and stage nerves, common piano mistakes and how to fix them.'),
]
info = []
for slug, name, hp_, wp_, blurb in PRODUCTS:
    d = S + slug + '/'; os.makedirs(d, exist_ok=True)
    hp = HB_FRONT + hb_pages(*hp_); wp = WB_FRONT + wb_pages(*wp_)
    write(d + f'Piano Butler Handbook - {name}.pdf', HB, hp, f'The Piano Butler Handbook · {name}')
    write(d + f'Piano Butler Workbook - {name}.pdf', WB, wp, f'The Piano Butler Workbook · {name}')
    info.append((slug, name, blurb, len(hp), len(wp)))
d = S + '00-complete-set/'; os.makedirs(d, exist_ok=True)
write(d + 'Piano Butler Handbook - complete.pdf', HB, list(range(1, len(HB.pages) + 1)), 'The Piano Butler Handbook')
write(d + 'Piano Butler Workbook - complete.pdf', WB, list(range(1, len(WB.pages) + 1)), 'The Piano Butler Workbook')
if os.path.exists(O + 'workbook-further.pdf'):
    r = PdfReader(O + 'workbook-further.pdf'); write(d + 'Bonus - Going further workbook pages.pdf', r, list(range(1, len(r.pages) + 1)), 'Bonus · Going further')
info.append(('00-complete-set', 'Complete set', 'Both whole books: every part, the glossary and index, and the Going further bonus (non-chord notes). Music theory for pianists from the first lesson to Grade 8.', len(HB.pages), len(WB.pages)))
d = S + '99-free-sampler/'; os.makedirs(d, exist_ok=True)
FIRST = [('pitch', 'P1'), ('time', 'T1'), ('expression', 'E1'), ('scales', 'S1'), ('chords', 'H1'), ('shape', 'F1'), ('play', 'L1')]
hp = HB_FRONT + [18, 19, 20] + [first(p, k)[0] for p, k in FIRST]
wp = WB_FRONT + [5, 6] + [n for p, k in FIRST for n in wb_first(p, k)]
write(d + 'Piano Butler - free sampler (Handbook).pdf', HB, hp, 'The Piano Butler · free sampler (Handbook)')
write(d + 'Piano Butler - free sampler (Workbook).pdf', WB, wp, 'The Piano Butler · free sampler (Workbook)')
info.append(('99-free-sampler', 'Free sampler', 'Before you play, and the first chapter of every part, in both books.', len(hp), len(wp)))
for slug, *_ in info:
    with zipfile.ZipFile(S + slug + '.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for fn in sorted(os.listdir(S + slug)): zf.write(S + slug + '/' + fn, fn)
json.dump(info, open(S + 'products.json', 'w'), indent=1)
for i in info: print(i[0], 'HB', i[3], 'WB', i[4], round(os.path.getsize(S + i[0] + '.zip') / 1e6, 1), 'MB')
