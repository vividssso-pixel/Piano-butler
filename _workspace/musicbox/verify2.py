# Checks every Music Box 2 melody, note by note, against the open score it was taken from.
# Pitches are compared as steps between neighbouring notes (so the key does not matter); lengths as ratios.
import json, re, os, sys, subprocess
from fractions import Fraction as Fr
from music21 import converter, corpus
SRC = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/src'
P = os.path.dirname(corpus.__file__)
SEMI = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
def mine(i, bars=None):
    d = json.load(open(f'mc{i}.json')); g = d['gig']; out = []
    flat = [b for ln in g['song_grid'] for b in ln]
    if bars: flat = [flat[k] for k in bars]
    for b in flat:
        for t in (b['r'].split() + ['-'] * d['beats'])[:d['beats']]:
            parts = t.split('.') if '.' in t else [t]; ln = Fr(1, len(parts))
            for x in parts:
                tie = x.startswith('~'); x = x.lstrip('~')
                m = re.match(r"^([A-G])([#b]?)([',]*)$", x)
                if m and not tie: out.append([SEMI[m[1]] + {'#': 1, 'b': -1, '': 0}[m[2]] + 12 * m[3].count("'") - 12 * m[3].count(','), ln])
                elif out: out[-1][1] += ln      # hold, tie or rest: the note before it lasts longer
    return out
def abc(path, title, nth=0):
    t = open(path if os.path.exists(path) else os.path.join(P, path), encoding='latin-1').read()
    tunes = [x for x in re.split(r'\n(?=X:)', t) if re.search(r'\nT:\s*' + re.escape(title), x)]
    s = converter.parse(tunes[nth], format='abc'); out = []
    for n in s.flatten().notesAndRests:
        if n.quarterLength == 0: continue
        if 'Harmony' in n.classes or 'ChordSymbol' in n.classes: continue
        if n.isRest:
            if out: out[-1][1] += Fr(n.quarterLength)
        else: out.append([n.pitches[-1].midi, Fr(n.quarterLength)])
    return out
def ly(text, relative=None):
    text = re.sub(r'%.*', '', text); text = re.sub(r'\\[a-zA-Z]+|[\[\]()~_^\-.>!|]|"[^"]*"|\{|\}', lambda m: ' ' if m[0] != '.' else '.', text)
    out = []; last = None; dur = Fr(1)
    STEP = 'cdefgab'
    for tok in text.split():
        m = re.match(r"^([a-g])(is|es|s)?([',]*)(\d+)?(\.*)$", tok) or (re.match(r"^(r|R|s)()()(\d+)?(\.*)$", tok))
        if not m: continue
        if m[4]: dur = Fr(4, int(m[4])); 
        d = dur * (Fr(3, 2) if m[5] == '.' else 1) if m[4] or m[5] else dur
        if m[4]: dur = Fr(4, int(m[4])); dlast = d
        if m[1] in 'rRs':
            if out: out[-1][1] += d
            continue
        pc = SEMI[m[1].upper()] + (1 if m[2] == 'is' else -1 if m[2] in ('es', 's') else 0); st = STEP.index(m[1])
        if relative is None: midi = 48 + pc + 12 * m[3].count("'") - 12 * m[3].count(',')
        else:
            if last is None: lo, lst = relative
            else: lo, lst = last
            # nearest octave so that the step distance is at most a fourth
            cands = [(o, abs((o * 7 + st) - lst)) for o in range(0, 9)]; o = min(cands, key=lambda c: c[1])[0] + m[3].count("'") - m[3].count(',')
            midi = 12 * o + pc; last = (midi, o * 7 + st)
        out.append([midi, d])
    return out
def git(path):
    return subprocess.run(['git', 'show', 'HEAD:' + path], cwd=SRC + '/mut', capture_output=True, text=True).stdout
import difflib
NM = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
def cmp(name, a, b, n=None, lens=True):
    if n: a, b = a[:n], b[:n]
    sh = a[0][0] - b[0][0]; pa = [x[0] for x in a]; pb = [x[0] + sh for x in b]
    ops = [o for o in difflib.SequenceMatcher(None, pa, pb, autojunk=False).get_opcodes() if o[0] != 'equal']
    same = sum(o[2] - o[1] for o in difflib.SequenceMatcher(None, pa, pb, autojunk=False).get_opcodes() if o[0] == 'equal')
    desc = '; '.join(f"{o[0]} mine[{o[1] + 1}:{o[2]}]={[NM[p % 12] for p in pa[o[1]:o[2]]]} source[{o[3] + 1}:{o[4]}]={[NM[p % 12] for p in pb[o[3]:o[4]]]}" for o in ops)
    # lengths: walk the matching stretches and compare each note's length as a ratio to the first matched note
    lb = []; ua = ub = None
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, pa, pb, autojunk=False).get_opcodes():
        if tag != 'equal': continue
        for k in range(i2 - i1 - 1):   # the last note of a stretch may be cut short by a pick-up or a tie in one version
            x, y = a[i1 + k][1], b[j1 + k][1]
            if ua is None: ua, ub = x, y
            if x / ua != y / ub: lb.append(f'note {i1 + k + 1}: {x / ua} vs {y / ub}')
    print(f'{name:32s} mine {len(a):3d} notes, source {len(b):3d} | same in order {same:3d} | {desc or "identical pitches"} | length differences {len(lb)}: {"; ".join(lb[:5])}')
N = SRC + '/nott/ABC_cleaned/'
cmp('1 Ducklings', mine(1), abc('essenFolksong/kinder0.abc', 'ALLE MEINE ENTCHEN'))
cmp('2 Oh! Susanna', mine(2), abc(N + 'reelsr-t.abc', 'Oh Susanna'))
f = [x for x in os.listdir(N) if 'Little Brown Jug' in open(N + x, encoding='latin-1').read()][0]
cmp('3 Little Brown Jug', mine(3), abc(N + f, 'Little Brown Jug')[2:])
cmp('4 Deck the Halls (lines 1, 3)', mine(4, [0, 1, 2, 3, 8, 9, 10, 11]), abc(N + 'xmas.abc', 'Nos Galan'))
fn = re.search(r'Soprano = \{(.*)', git('ftp/Traditional/first_noel/first_noel.ly'))[1]
cmp('5 The First Noel', mine(5), ly(re.sub(r'\\time 3/4|\\key d \\major|\\bar "\|\."', '', fn)))
cmp('6 Good King Wenceslas', mine(6), abc(N + 'xmas.abc', 'GKW'))
sn = re.search(r'Soprano = \{(.*)', git('ftp/GruberFX/stille_nacht/stille_nacht.ly'))[1]
cmp('7 Silent Night', mine(7), ly(re.sub(r'\\time 6/8|\\key bes \\major|\\bar "\|\."', '', sn)))
cmp('8 Daisy Bell', mine(8), abc(N + [x for x in os.listdir(N) if 'Daisy Daisy' in open(N + x, encoding='latin-1').read()][0], 'Daisy Daisy')[2:], n=24)
mi = git('ftp/BachJS/BWVAnh114/anna-magdalena-04/anna-magdalena-04.ly'); v1 = mi[mi.index('voiceone'):]; v1 = v1[v1.index('\\key g \\major') + 13:]
v1 = re.sub(r'\\grace\s+[a-g]\d*', '', v1.split('\\repeat')[1] if False else v1); v1 = re.sub(r'\\(mordent|break|prall|trill)', '', v1)
cmp('9 Minuet in G (right hand)', mine(9), ly(v1, relative=(72, 5 * 7)), n=len(mine(9)))
gs = re.search(r'Soprano = \{(.*)', git('ftp/Traditional/greensleeves/greensleeves.ly'))[1]
cmp('10 Greensleeves', mine(10), ly(re.sub(r'\\time 6/8|\\partial 8|\\key g \\major', '', gs)), n=len(mine(10)))
cn = git('ftp/PachelbelJ/Canon_per_3_Violini_e_Basso/Canon_per_3_Violini_e_Basso-lys/violin_common.ily'); cn = cn[cn.index('{') + 1:]
cmp('11 Canon', mine(11), ly(cn, relative=(72, 5 * 7)), n=len(mine(11)) - 1)
gr = git('ftp/GriegE/O46/Dans_l_antre_du_roi_de_la_montagne/Dans_l_antre_du_roi_de_la_montagne.ly'); gr = gr[gr.index('rightOne'):]; gr = gr[gr.index('b,,8'):]
gr = re.sub(r'_\\markup\s*\{[^}]*\{[^}]*\}\s*\}|\\pp|<a, a\'>', lambda m: 'a' if m[0].startswith('<') else '', gr)
cmp('12 Mountain King', mine(12), ly(gr, relative=(72, 5 * 7)), n=len(mine(12)))
fe = git('ftp/BeethovenLv/WoO59/fur_Elise_WoO59/fur_Elise_WoO59.ly'); fe = fe[fe.index('\\partial 8 e'):]; fe = re.sub(r'\^\\markup\s*\{[^}]*\}|\\pp', '', fe); fe = fe[:fe.index('\\alternative')] + ' a4'
cmp('13 Für Elise (right hand)', mine(13), ly(fe.replace('\\partial 8', '')), n=len(mine(13)))
E = [x for x in os.listdir(P + '/essenFolksong') if x.endswith('.abc') and 'MORGEN KOMMT DER WEIHNACHTSMANN' in open(P + '/essenFolksong/' + x, encoding='latin-1').read()]

