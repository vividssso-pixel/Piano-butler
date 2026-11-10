# The Music Box on the books shelf (her 10 Nov 23:55: 'this songbook should look like this too').
# One PDF per song (with its left-hand page when it has one), a thumbnail each, and shelf.json, which books-split.py
# reads to add the book to 'The books'. Usage: python3 mbshelf.py <books-latest folder> <whole-book pdf name>
import json, os, subprocess, sys, html, shutil
O, WHOLE = sys.argv[1].rstrip('/') + '/', sys.argv[2]
slug = lambda x: ''.join(c if c.isalnum() else '-' for c in x.lower()).strip('-').replace('--', '-').replace('--', '-')
os.makedirs(O + '4 Music Box', exist_ok=True); os.makedirs(O + '_thumbs', exist_ok=True)
cards = []
for i in range(1, 40):
    if not os.path.exists(f'mb{i}.json'): break
    d = json.load(open(f'mb{i}.json')); G = d['gig']
    f = f'4 Music Box/music-box-{i:02d}-{slug(d["title"])}.pdf'; th = f'_thumbs/mb-{i:02d}.jpg'
    shutil.copy(f'lesson-mb{i}.pdf', O + f)
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=82', '-r', '60', '-f', '1', '-l', '1', '-singlefile', f'lesson-mb{i}.pdf', O + th[:-4]], check=True)
    n = int(subprocess.run(['pdfinfo', f'lesson-mb{i}.pdf'], capture_output=True, text=True).stdout.split('Pages:')[1].split()[0])
    lab = f'Song {i}' + (' · and a left-hand page' if G.get('ways') else '')
    cards.append([lab, d['title'], G['job'], f, th, '', n])
book = ['mbS', 'mb', 'Songs', 'The Piano Butler', 'Songbook', 'Music Box', 'Both hands in beat boxes, one song a page', 'Whole books (later)/' + WHOLE]
json.dump({'book': book, 'cards': cards}, open(O + '4 Music Box/shelf.json', 'w'), ensure_ascii=False, indent=1)
print(len(cards), 'songs')
