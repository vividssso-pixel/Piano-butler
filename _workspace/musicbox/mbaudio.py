# The Music Box's listening page (her 10 Nov 22:59: 'the audio is the old version; change what is here and reuse it').
# musicbox.html is listen.html with the Music Box's own versions of the songs: the same tune, words and chords as the
# book's boxes. The Lesson Book's listen.html is left as it is. Piano = exactly what the student's left hand plays.
# Usage: python3 mbaudio.py <listen.html> <out musicbox.html>
import json, re, sys
src = open(sys.argv[1]).read()
OLD = {s['id']: s for s in json.loads(re.search(r'const SONGS\s*=\s*(\[.*?\]);\s*\n', src, re.S).group(1))}
PIT = {'C': 'c4', 'D': 'd4', 'E': 'e4', 'F': 'f4', 'G': 'g4', 'A': 'a4'}
DUR = {1: 'c', 2: 'm', 3: 'd', 4: 's'}
BAND = {'C': 'C6', 'F': 'Fmaj7', 'G': 'G7'}
JAZZ = OLD['mary']['band']['voicing']; TRI = OLD['mary']['piano']['voicing']
BPM = {'buns': 92, 'mary': 96, 'auclair': 84, 'lightly': 92, 'ode': 96, 'jingle': 112, 'twinkle': 88, 'london': 100, 'saints': 104}
STY = {'auclair': ('moon', 'popballad', 'lullaby'), 'lightly': ('winds', 'bossa', 'lullaby'), 'saints': ('brass', 'gospel', 'march')}
songs = []
for i in range(1, 20):
    try: d = json.load(open(f'mb{i}.json'))
    except FileNotFoundError: break
    G, sid = d['gig'], d['id']; bars, chords = [], []
    for line in G['song_grid']:
        for b in line:
            rt, wt, out = b['r'].split(), (b.get('w') or '').split(), []
            for k, t in enumerate(rt):
                w = wt[k] if k < len(wt) else ''
                if t == '-': continue
                n = 1
                while k + n < len(rt) and rt[k + n] == '-': n += 1
                if t == 'r': out.append(['r', 'c', '', '']); continue
                if '.' in t:
                    for x, y in zip(t.split('.'), (w.split('.') + [''])[:2]): out.append([PIT[x], 'q', y.rstrip('-'), 'i' if y.endswith('-') else ''])
                    continue
                out.append([PIT[t], DUR[n], '' if w == '-' else w.rstrip('-'), 'i' if w.endswith('-') else ''])
            bars.append(out); chords.append(b['l'])
    o = OLD.get(sid, {})
    ens, band = dict(o.get('ens') or {'style': STY.get(sid, ('winds',))[0], 'voicing': TRI}), dict(o.get('band') or {'swing': 0, 'style': STY.get(sid, (0, 'bossa'))[1], 'voicing': JAZZ})
    ens.update({'bpm': BPM[sid], 'chords': [[[c, 4]] for c in chords]}); band.update({'bpm': BPM[sid] + 4, 'chords': [[[BAND[c], 4]] for c in chords]})
    piano = {'bpm': BPM[sid], 'style': 'lh', 'voicing': TRI, 'chords': [[[c, 4]] for c in chords]}
    songs.append({'id': sid, 'n': i, 'title': d['title'], 'meter': '4/4', 'bpm': BPM[sid], 'tunes': [{'t': 'The song', 'b': bars}], 'piano': piano, 'band': band, 'ens': ens})
out = re.sub(r'const SONGS\s*=\s*\[.*?\];\s*\n', lambda m: 'const SONGS = ' + json.dumps(songs, ensure_ascii=False, separators=(',', ':')) + ';\n', src, count=1, flags=re.S)
R = [("<title>Listen · The Piano Butler Lesson Book</title>", "<title>Listen · The Butler's Music Box</title>"),
     ('<div class="kick">The Piano Butler · Lesson Book · Level 0</div>', '<div class="kick">The Piano Butler · The Music Box</div>'),
     ("$('lno').textContent = 'Lesson ' + song.n;", "$('lno').textContent = 'Song ' + song.n;"),
     # the student's own left hand: the root, once a bar, held (Music Box)
     ("    waltz: (r, v, s, len) =>", "    lh: (r, v, s, len) => { pianoNote(r * 2, at(s), len * beat * 0.96, 0.34); },   // the Music Box: your left hand, one key a bar\n    waltz: (r, v, s, len) =>"),
     ("if (last) { v.forEach(f =>", "if (last && A.style === 'lh') { pianoNote(r * 2, at(s), Math.max(len, 3) * beat, 0.34); return; }\n      if (last) { v.forEach(f =>"),
     ("const LBL = { waltz: 'Waltz',", "const LBL = { lh: 'Your left hand', waltz: 'Waltz',"),
     ("Then pick <b>Piano</b> or <b>Band</b>, tick <b>I play the tune</b>, and play your part with them.", "<b>Piano</b> plays your left hand. Tick <b>I play the tune</b> and play the right hand with it; or pick <b>Band</b> and play both hands with them.")]
for a, b in R:
    assert out.count(a) == 1, a; out = out.replace(a, b)
open(sys.argv[2], 'w').write(out); print(len(songs), 'songs', [s['id'] for s in songs])
