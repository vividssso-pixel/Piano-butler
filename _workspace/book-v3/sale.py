# Her 15 Nov ("작게 작게 가는 게 나을 듯", "어느 정도 반응이 오기 전까진"): the sale files. Small products, one per part,
# each = the Handbook part (with the cover, copyright page and "How to read this book") + its Workbook pages (with the
# Workbook's front matter). Plus the complete set (both whole books + Going further as a bonus) and a free sampler.
import json, os, sys, zipfile
sys.path.insert(0, '/tmp/claude-0/pk'); import pagemap as PM
from pypdf import PdfReader, PdfWriter
O = '/mnt/user-data/outputs/'; H = O + 'house-rooms/'
HB, WB = PdfReader(O + 'books/handbook-draft.pdf'), PdfReader(O + 'books/workbook-draft.pdf')
J = json.load(open(H + 'workbook-pages.json')); OFF, TOTAL = J['off'], J['total']
ORDER = list(OFF)
def wb_range(f):
    i = ORDER.index(f); end = OFF[ORDER[i + 1]] if i + 1 < len(ORDER) else TOTAL
    return list(range(OFF[f] + 1, end + 1))
def hb_range(*parts):
    keys = ['P', 'T', 'E', 'S', 'H', 'M', 'F', 'L', 'G']; out = []
    for p in parts:
        a = PM.PAGE[p + 'O']; nxt = keys[keys.index(p) + 1] if p != 'G' else None
        b = PM.PAGE[nxt + 'O'] - 1 if nxt else PM.PAGE['X'] - 1
        out += list(range(a, b + 1))
    return out
HB_FRONT = [1, 3, 4, 17]; WB_FRONT = [1, 2, 3, 4]
def write(path, reader, pages, title):
    w = PdfWriter()
    for n in pages: w.add_page(reader.pages[n - 1])
    w.add_metadata({'/Title': title, '/Author': 'Sohyun Park', '/Subject': 'The Piano Butler · thepianobutler.com'})
    with open(path, 'wb') as f: w.write(f)
PRODUCTS = [
 ('01-pitch', 'Pitch', ['P'], 'workbook-pitch', 'Reading notes: the keyboard, the staff and clefs, ledger lines, sharps and flats, intervals'),
 ('02-time', 'Time', ['T'], 'workbook-time2', 'Rhythm: the beat, notes and rests, dots and ties, time signatures, upbeats, syncopation, repeats'),
 ('03-expression', 'Expression', ['E'], 'workbook-expression', 'Loud and soft, touch, speed words, the pedals, ornaments'),
 ('04-scales-and-keys', 'Scales and keys', ['S'], 'workbook-scales', 'Major and minor scales, key signatures, finding the key, the circle of fifths'),
 ('05-chords-and-harmony', 'Chords and harmony', ['H', 'M'], 'workbook-harmony', 'Triads, chords in a key, inversions, sevenths, colour chords, slash chords, cadences, progressions'),
 ('06-shape-and-style', 'Shape and style', ['F'], 'workbook-shape', 'Motifs and phrases, sequence, texture, changing key, form, styles through time'),
 ('07-playing-and-listening', 'Playing and listening', ['L'], 'workbook-play', 'Fingering, practising well, sight-reading, listening, performing'),
]
S = O + 'sale/'; os.makedirs(S, exist_ok=True); info = []
for slug, name, parts, wf, blurb in PRODUCTS:
    d = S + slug + '/'; os.makedirs(d, exist_ok=True)
    hp = HB_FRONT + hb_range(*parts); wp = WB_FRONT + wb_range(wf)
    write(d + f'Piano Butler Handbook - {name}.pdf', HB, hp, f'The Piano Butler Handbook · {name}')
    write(d + f'Piano Butler Workbook - {name}.pdf', WB, wp, f'The Piano Butler Workbook · {name}')
    info.append((slug, name, blurb, len(hp), len(wp)))
# the complete set: both whole books, Going further as a bonus
d = S + '00-complete-set/'; os.makedirs(d, exist_ok=True)
write(d + 'Piano Butler Handbook - complete.pdf', HB, list(range(1, len(HB.pages) + 1)), 'The Piano Butler Handbook')
write(d + 'Piano Butler Workbook - complete.pdf', WB, list(range(1, len(WB.pages) + 1)), 'The Piano Butler Workbook')
if os.path.exists(O + 'workbook-further.pdf'):
    r = PdfReader(O + 'workbook-further.pdf'); write(d + 'Bonus - Going further workbook pages.pdf', r, list(range(1, len(r.pages) + 1)), 'Bonus · Going further')
info.append(('00-complete-set', 'Complete set', 'Both whole books, every part, the glossary and index, plus the Going further bonus', len(HB.pages), len(WB.pages)))
# the free sampler: Before you play, and the first chapter of every part
d = S + '99-free-sampler/'; os.makedirs(d, exist_ok=True)
hp = HB_FRONT + [18, 19, 20] + [PM.PAGE[p + '1'] for p in 'PTESHFL']
wp = WB_FRONT + wb_range('workbook-before')
for f in ORDER[1:]: wp += wb_range(f)[:1 if f == 'workbook-scales' else 2]
write(d + 'Piano Butler - free sampler (Handbook).pdf', HB, hp, 'The Piano Butler · free sampler (Handbook)')
write(d + 'Piano Butler - free sampler (Workbook).pdf', WB, wp, 'The Piano Butler · free sampler (Workbook)')
info.append(('99-free-sampler', 'Free sampler', 'Before you play, and the first page of each Handbook part and the first chapter of each Workbook part', len(hp), len(wp)))
for slug, *_ in info:
    z = S + slug + '.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for fn in sorted(os.listdir(S + slug)): zf.write(S + slug + '/' + fn, fn)
json.dump(info, open(S + 'products.json', 'w'), indent=1)
for i in info: print(i[0], i[1], 'HB', i[3], 'WB', i[4], round(os.path.getsize(S + i[0] + '.zip') / 1e6, 1), 'MB')
