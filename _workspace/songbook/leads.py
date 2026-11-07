# Page 3 is a lead sheet in every lesson (her 7 Nov 13:11: '3은 lead sheet으로 고정 ... 실용음악 같이 반주패턴 배우는걸로'):
# the tune with only chord names above it, and a left-hand accompaniment pattern that grows lesson by lesson.
#   L1-3  the names only: you play the tune, your teacher (or the band) plays the names
#   L4-6  tap the root: the left hand plays each name's root once, on beat 1
#   L7    pattern 1, the root held        L8  pattern 2, the root changes (C, G)
#   L9    pattern 3, the root twice       L10 pattern 4, oom-pah-pah (3/4)
# Page 1 of Lessons 7-10 shows the right hand only, big; both hands meet here, from the names.
# The chord names are a simple harmony for each tune (C, F, G, Am, E, D): for Sohyun to check.
# Usage: python3 leads.py   (rewrites the ten song files)
import json, copy

C, G, F = 'C', 'G', 'F'
LEADS = {   # per bar: [[name, beat], ...]
 'buns': [[[C]], [[C]], [[C]], [[C]], [[C]], [[G]], [[C], [G, 2]], [[C]]],
 'home': [[[C]], [[C]], [[G]], [[G]], [[C]], [[C]], [[G], [C, 4]], [[C]]],
 'mary': [[[C]], [[C]], [[G]], [[C]], [[C]], [[C]], [[G]], [[C]]],
 'ode': [[[C]], [[G]], [[C]], [[G]], [[C]], [[G]], [[C]], [[G], [C, 2]], [[G]], [[C]], [[G]], [[C], [G, 3]], [[C]], [[G]], [[C]], [[G], [C, 2]]],
 'jingle': [[[C]], [[C]], [[C]], [[C]], [[F]], [[C]], [[G]], [[G]], [[C]], [[C]], [[C]], [[C]], [[F]], [[C]], [[G]], [[C]]],
 'twinkle': [[[C]], [[F], [C, 3]], [[F], [C, 3]], [[G], [C, 3]], [[C], [F, 3]], [[C], [G, 3]], [[C], [F, 3]], [[C], [G, 3]], [[C]], [[F], [C, 3]], [[F], [C, 3]], [[G], [C, 3]]],
 'frere': [[[C]]] * 8,
 'london': [[[C]], [[C]], [[G]], [[C]], [[C]], [[C]], [[G]], [[C]]],
 'surprise': [[[C]], [[C]], [[G]], [[G]], [[C]], [[C]], [['D']], [[G]]],
 'elise': [[], [['Am']], [['Am']], [['E']], [['Am']], [['Am']], [['Am']], [['E']], [['Am']]],
}
LH = {'C': ('c3', 5), 'F': ('f3', 2), 'G': ('g3', 1), 'D': ('d3', 4)}   # the left hand's C position, an octave below middle C
n = lambda p, d, lf=None: [p, d, '', '', None, lf]
R = lambda d: ['r', d, '', '']
def tap(nm): p, f = LH[nm]; return [n(p, 'c', f), R('c'), R('m')]
PAT = {   # the pattern, shown on its own: one bar per name, on the King's staff
 'tap': {'title': 'Tap the root', 'bars': [tap('C'), tap('G')], 'chords': ['C', 'G'],
         'how': 'The root is the chord’s own letter: C for C, G for G. Play it once, on beat 1, and let it ring.'},
 'p1': {'title': 'Pattern 1 · The root, held', 'bars': [[n('c3', 's', 5)]], 'chords': ['C'],
        'how': 'Play the root on beat 1 and hold it through the bar, all four beats. Frère Jacques needs only C.'},
 'p2': {'title': 'Pattern 2 · The root changes', 'bars': [[n('c3', 's', 5)], [n('g3', 's', 1)]], 'chords': ['C', 'G'],
        'how': 'Held, as in Lesson 7; now watch the name. C: 5 on low C. G: the thumb on G.'},
 'p3': {'title': 'Pattern 3 · The root twice', 'bars': [[n('c3', 'm', 5), n('c3', 'm', 5)], [n('g3', 'm', 1), n('g3', 'm', 1)]], 'chords': ['C', 'G'],
        'how': 'The root on beats 1 and 3: two minims a bar, a slow heartbeat. D (finger 4) joins in bar 7.'},
 'p4': {'title': 'Pattern 4 · Oom-pah-pah', 'bars': [[n('a3', 'c', 5), n('e4', 'c', 1), n('e4', 'c', 1)], [n('e4', 'c', 1), n('b3', 'c', 4), n('b3', 'c', 4)]], 'chords': ['Am', 'E'],
        'how': 'The waltz pattern: the root on ONE, then a higher note on two and three. Am: A, E, E. E: E, B, B.'},
}
PAGE = {   # lesson: (pattern, how, steps, keyboard roots)
 'buns': (None, 'A lead sheet is how band players read: the tune, and above it only the chord names. You play the tune; your teacher, or the band on the listening page, plays the names.',
          ['Point to each name as the music reaches it', 'Play the tune; your teacher plays the names', 'Swap: you say the names, your teacher plays']),
 'home': (None, 'The tune, with only the chord names above it. You play the tune; your teacher, or the band, plays the names.',
          ['Find where the name changes', 'Play the tune; your teacher plays the names', 'Say the names in time while your teacher plays']),
 'mary': (None, 'The tune, with only the chord names above it. Two names in this song: C and G.',
          ['Circle every G', 'Play the tune; your teacher plays the names', 'Say the names in time while your teacher plays']),
 'ode': ('tap', 'The tune and its chord names. Now the left hand joins in: it taps each name’s root, once, on beat 1.',
         ['Tune alone, right hand', 'Left hand alone: tap the roots while your teacher plays the tune', 'Together, slowly']),
 'jingle': ('tap', 'The tune and its chord names. A new name: F. The left hand taps each root on beat 1: C, F or G.',
            ['Tune alone, right hand', 'Left hand alone: tap the roots while your teacher plays the tune', 'Together, slowly']),
 'twinkle': ('tap', 'The tune and its chord names. Some bars have two names: tap each root where its name sits, beat 1 or beat 3.',
             ['Tune alone, right hand', 'Left hand alone: tap the roots while your teacher plays the tune', 'Together, slowly']),
 'frere': ('p1', 'Your first accompaniment pattern. The whole song is one chord, C: the left hand holds low C under every bar. In bars 7 and 8 the left hand plays dang (G) instead.',
           ['Tune alone, right hand', 'Pattern alone: hold C, count four', 'Together, slowly']),
 'london': ('p2', 'The tune and its names, C and G. Your left hand plays pattern 2 from the names: hold each bar’s root.',
            ['Tune alone, right hand', 'Pattern alone, reading only the names', 'Together, slowly, then with the band']),
 'surprise': ('p3', 'The tune and its names, C, G and D. The left hand plays pattern 3. In bars 3 and 4 it plays the answer instead (the notes marked L), and in bar 8 it joins the BANG.',
              ['Tune alone, right hand', 'Pattern alone, reading only the names', 'Together, slowly, then with the band']),
 'elise': ('p4', 'The tune and its names, Am and E, in three-time. The left hand plays pattern 4 from the names: oom-pah-pah. Bar 1 has no name: the right hand starts alone.',
           ['Tune alone, right hand', 'Pattern alone, reading only the names: ONE two three', 'Together, very slowly']),
}
RIGHT_ONLY = ['frere', 'london', 'surprise', 'elise']   # page 1: the right hand only, big (both hands meet on page 3)

for s, lead in LEADS.items():
    d = json.load(open(s + '.json'))
    assert len(lead) == len(d['bars']), s
    d['leadch'] = [[[x[0], x[1] if len(x) > 1 else 1] for x in bar] for bar in lead]
    pat, how, steps = PAGE[s]
    # the pattern as a tune of its own, kept at the end of 'more' (and replaced on a re-run)
    d['more'] = [m for m in d.get('more', []) if not m.get('_pattern')]
    J = d['jobs']
    for k in [k for k in J if k.startswith(('lead', 'patt'))]: J.pop(k)
    if pat:
        P = copy.deepcopy(PAT[pat]); P['_pattern'] = 1; d['more'].append(P); src = len(d['more']) - 1
        P['leadch'] = [[[c, 1]] for c in P['chords']]
        J['patt1'] = [0, len(P['bars']), {'src': src, 'bass': 1, 'meter': 1, 'lead': 1, 'lhfing': 1, 'sl': 0.12}]
    # Lessons 7-9 (8 bars): page 1 at two bars a line, so the right hand's notes are big (her 7 Nov: the page had room)
    if False and s in ('frere', 'london', 'surprise'):
        base = dict(J['sing1'][2]); base.pop('meter', None)
        for k in [k for k in J if k.startswith('sing')]: J.pop(k)
        for i in range(4): J[f'sing{i + 1}'] = [2 * i, 2 * i + 2, dict(base, **({'meter': 1} if i == 0 else {}))]
    # the lead sheet: the page-1 lines without words, chord names above, a finger on each line's first note
    sing = sorted([k for k in J if k.startswith('sing')], key=lambda k: int(k[4:]))
    TWO = s in ('buns', 'frere')   # two bars a line where that comes out bigger (measured: Hot Cross Buns 1.34x, Frère 1.19x; the others smaller)
    if TWO:
        src = J[sing[0]][2]; rest = dict(J[sing[1]][2]) if len(sing) > 1 else dict(src)
        sing = [f'_l{i}' for i in range(4)]
        for i in range(4): J[sing[i]] = [2 * i, 2 * i + 2, dict(src) if i == 0 else dict(rest, **{'meter': 0})]
    for i, k in enumerate(sing):
        b0, b1, o = J[k]; o2 = {kk: v for kk, v in o.items() if kk not in ('words', 'lys', 'lws', 'lh', 'dyn', 'ltm', 'vdown', 'snl')}
        o2.update({'lead': 1, 'fing': 1, 'fing1': 1})
        o2.pop('meter', None) if not o2.get('meter') else None
        J[f'lead{i + 1}'] = [b0, b1, o2]
    for k in [k for k in J if k.startswith('_l')]: J.pop(k)
    sing = sorted([k for k in J if k.startswith('sing')], key=lambda k: int(k[4:]))
    hasL = lambda b0, b1: any((d.get('hand') or {}).get(x[0]) == 'L' or (len(x) > 6 and x[6] == 'L') for bar in d['bars'][b0:b1] for x in bar)
    if s in RIGHT_ONLY:   # page 1: the right hand alone; a line with a left-hand note keeps its words lower (mix)
        for k in sing:
            J[k][2].pop('lh', None); J[k][2].pop('mix', None)
            if hasL(J[k][0], J[k][1]): J[k][2]['mix'] = 1
    for k in [k for k in J if k.startswith('lead')]:
        J[k][2].pop('mix', None)
        if hasL(J[k][0], J[k][1]): J[k][2]['mix'] = 1
    d['lead_page'] = {'pattern': PAT[pat] if pat else None, 'how': how, 'steps': steps, 'jobs': sorted([k for k in J if k.startswith('lead')], key=lambda k: int(k[4:])), 'pjob': 'patt1' if pat else None}
    d.pop('chord_page', None)
    json.dump(d, open(s + '.json', 'w'), ensure_ascii=False, indent=0)
    print(s, 'ok', len(sing), 'lines', pat)
