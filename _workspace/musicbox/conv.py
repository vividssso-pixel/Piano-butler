# Turns an open score (ABC) into Music Box bars, so the page IS the source: nothing is typed by hand.
import re, os, sys, json
from fractions import Fraction as Fr
from music21 import converter, harmony, interval, pitch, note as m21note
SRC = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/src'
N = SRC + '/nott/ABC_cleaned/'
def find(title):
    for f in sorted(os.listdir(N)):
        t = open(N + f, encoding='latin-1').read()
        for x in re.split(r'\n(?=X:)', t):
            if re.search(r'\nT:\s*' + re.escape(title) + r'\s*\n', x): return x
    raise KeyError(title)
LET = 'CDEFGAB'
def tokname(p):   # midi+spelling -> token with octave marks around octave 4
    o = p.octave - 4; acc = {'#': '#', '-': 'b', '': ''}.get(p.accidental.modifier if p.accidental and p.accidental.alter else '', '')
    return p.step + acc + ("'" * o if o > 0 else ',' * -o)
def load(title, to=None, semis=None):
    x = find(title); s = converter.parse(x, format='abc')
    k = re.search(r'\nK:\s*([A-G][b#]?)\s*(m|min)?', x); ton = k[1].replace('b', '-'); minor = bool(k[2])
    if to:
        iv = interval.Interval(pitch.Pitch(ton), pitch.Pitch(to)); 
        if iv.semitones > 6: iv = interval.Interval(iv.semitones - 12)
        if semis is not None: iv = interval.Interval(semis)
        s = s.transpose(iv)
    bars = []
    for me in s.recurse().getElementsByClass('Measure'):
        ev = []; ch = []
        for n in me.flatten().notesAndRests:
            if isinstance(n, harmony.ChordSymbol): 
                r = n.root().name.replace('-', 'b'); q = 'm' if n.quality == 'minor' else ''
                ch.append((Fr(n.offset), r + q)); continue
            if n.quarterLength == 0: continue
            tie = bool(n.tie and n.tie.type in ('stop', 'continue')) if not n.isRest else False
            ev.append((Fr(n.offset), None if n.isRest else tokname(n.pitches[-1]), Fr(n.quarterLength), tie))
        bars.append({'ev': ev, 'ch': ch, 'len': Fr(me.duration.quarterLength), 'rep': [type(b).__name__ + ':' + str(getattr(b, 'direction', '')) + str(getattr(b, 'number', '')) for b in me.getElementsByClass(['Repeat', 'RepeatBracket'])]})
    m = re.search(r'\nM:\s*(\S+)', x)
    return bars, m[1], ton + ('m' if minor else '')
def tok(bar, meter, box):   # box = quarterLengths in one box
    ev = bar['ev']; out = ['-'] * meter; pos = {}
    for o, p, d, tie in ev: pos[o / box] = (p, d / box, tie)
    for i in range(meter):
        a = pos.get(Fr(i)); h = pos.get(Fr(i) + Fr(1, 2)); inside = [k for k in pos if i < k < i + 1 and k != Fr(i) + Fr(1, 2)]
        if inside: raise ValueError(f'note finer than half a box at {i}')
        nm = lambda t: ('r' if t[0] is None else ('~' if t[2] else '') + t[0])
        if a and h: out[i] = nm(a) + '.' + nm(h)
        elif a: out[i] = nm(a)
        elif h: out[i] = '-.' + nm(h)
    return ' '.join(out)
if __name__ == '__main__':
    for t in sys.argv[1:]:
        bars, m, k = load(t)
        ps = [pitch.Pitch(e[1].replace("'", '').replace(',', '').replace('b', '-')).midi + 12 * (e[1].count("'") - e[1].count(',')) for b in bars for e in b['ev'] if e[1]]
        ds = sorted({float(e[2]) for b in bars for e in b['ev']})
        print(f"{t}: M {m} K {k} bars {len(bars)} lens {[float(b['len']) for b in bars][:3]}.. range {min(ps)}-{max(ps)} durs {ds} reps {[(i, b['rep']) for i, b in enumerate(bars) if b['rep']]}")
