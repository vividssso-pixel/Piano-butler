# Engraved examples for the Accompaniment Book: tunes with chord symbols above, left-hand patterns below (vrve.mjs).
import json, subprocess
def count(tok):
    if tok in ('[', ']'): return 0
    t = tok.split('/')[0]
    return t.count('.') + 1 if t.startswith('(') and ')' in t else 1
def tune(tre, chords=None, bass=None, meter='4/4', key=None, sp=0.35, dur='4', extra=(), clef=None):
    """tre/bass: lists of bars (token strings). chords: per bar, a symbol or a list of (token index, symbol)."""
    nid = 0; ctl = []; first = {}
    for b in range(len(tre)):
        ids = []
        for tok in tre[b].split():
            c = count(tok)
            if c: ids.append(nid + 1)
            nid += c
        first[b] = ids
        if bass:
            for tok in bass[b].split(): nid += count(tok)
        if chords and b < len(chords) and chords[b]:
            ch = chords[b] if isinstance(chords[b], list) else [(0, chords[b])]
            for i, sym in ch: ctl.append(f'harm {ids[i]} {sym}')
    v = {'clef': clef or ('GF' if bass else 'G'), 'src': ' | '.join(tre), 'dur': dur, 'meter': meter, 'sp': sp, 'ctl': ctl + list(extra)}
    if bass: v['src2'] = ' | '.join(bass)
    if key: v['key'] = key
    return v
MARY = ['e4 d4 c4 d4', 'e4 e4 e4:2', 'd4 d4 d4:2', 'e4 g4 g4:2', 'e4 d4 c4 d4', 'e4 e4 e4 e4', 'd4 d4 e4 d4', 'c4:1']
MARY_G = ['b4 a4 g4 a4', 'b4 b4 b4:2', 'a4 a4 a4:2', 'b4 d5 d5:2', 'b4 a4 g4 a4', 'b4 b4 b4 b4', 'a4 a4 b4 a4', 'g4:1']
MARY_F = ['a4 g4 f4 g4', 'a4 a4 a4:2', 'g4 g4 g4:2', 'a4 c5 c5:2', 'a4 g4 f4 g4', 'a4 a4 a4 a4', 'g4 g4 a4 g4', 'f4:1']
TW = ['c4 c4 g4 g4', 'a4 a4 g4:2', 'f4 f4 e4 e4', 'd4 d4 c4:2']
TWC = ['C', [(0, 'F'), (2, 'C')], [(0, 'F'), (2, 'C')], [(0, 'G'), (2, 'C')]]
ODE = ['e4 e4 f4 g4', 'g4 f4 e4 d4', 'c4 c4 d4 e4', 'e4:4. d4:8 d4:2']
GRACE = ['g4', 'c5:2 [ e5:8 c5:8 ]', 'e5:2 d5', 'c5:2 a4', 'g4:2 g4']   # Amazing Grace in C, 3/4, with its upbeat
S = {
 'k_tw_lead': tune(TW, TWC),
 'k_mary_lead': tune(MARY, ['C', 'C', 'G', 'C', 'C', 'C', 'G', 'C'], sp=0.28),
 'k_mary_q4': tune(MARY[:4], ['C', 'C', '?', '?']),
 'k_mary_g': tune(MARY_G[:4], ['?', '?', '?', '?'], key='1s'),
 'k_mary_f': tune(MARY_F[:4], ['?', '?', '?', '?'], key='1f'),
 'k_mary_g_a': tune(MARY_G[:4], ['G', 'G', 'D', 'G'], key='1s'),
 'k_sym': tune(['(c4.e4.g4):1', '(a3.c4.e4):1', '(g3.b3.d4.f4):1', '(f3.a3.c4):1'], ['C', 'Am', 'G7', 'F'], sp=0.5),
 'k_pat3': tune(['s:1', 's:1', 's:1'], None, ['(c3.g3):1', '(c3.g3):2 (c3.g3):2', 'c3 g3 c3 g3'], sp=0.4),
 'k_mary_min': tune(MARY[:4], ['C', 'C', 'G', 'C'], ['c3:2 c3:2', 'c3:2 c3:2', 'g2:2 g2:2', 'c3:2 c3:2']),
 'k_rf': tune(MARY[:4], ['C', 'C', 'G', 'C'], ['c3 g3 c3 g3', 'c3 g3 c3 g3', 'g2 d3 g2 d3', 'c3 g3 c3 g3'], sp=0.3),
 'k_mary_root': tune(MARY[:4], ['C', 'C', 'G', 'C'], ['c3:1', 'c3:1', 'g2:1', 'c3:1']),
 'k_moves': tune(['s:1', 's:1', 's:1'], None, ['c3:1', 'f3:1', 'g2:1'], sp=0.5),
 'k_broken': tune(TW, TWC, ['c3 e3 g3 e3', 'f2 a2 c3 e3', 'f2 a2 c3 e3', 'g2 b2 c3 e3'], sp=0.3),
 'k_brk_q': tune(['s:1'], None, ['g2 b2 d3 b2'], sp=0.6),
 'k_brk_pats': tune(['s:1', 's:1', 's:1'], None, ['c3 e3 g3 e3', 'c3 e3 g3:2', 'c3 g3 e4 g3'], sp=0.4),
 'k_waltz': tune(GRACE, [None, 'C', 'C', 'F', 'C'], ['r', 'c3 (e3.g3) (e3.g3)', 'c3 (e3.g3) (e3.g3)', 'f2 (a2.c3) (a2.c3)', 'c3 (e3.g3) (e3.g3)'], meter='3/4', sp=0.3),
 'k_waltz_lead': tune(GRACE, [None, 'C', 'C', '?', 'C'], meter='3/4', sp=0.35),
 'k_oompah': tune(['s:2.', 's:2.', 's:2.'], None, ['c3 (e3.g3) (e3.g3)', 'f2 (a2.c3) (a2.c3)', 'g2 (b2.d3) (b2.d3)'], meter='3/4', sp=0.45),
 'k_alb': tune(ODE, ['C', 'G', 'C', [(0, 'C'), (2, 'G')]], ['[ c3:8 g3:8 e3:8 g3:8 ] [ c3:8 g3:8 e3:8 g3:8 ]', '[ g2:8 d3:8 b2:8 d3:8 ] [ g2:8 d3:8 b2:8 d3:8 ]', '[ c3:8 g3:8 e3:8 g3:8 ] [ c3:8 g3:8 e3:8 g3:8 ]', '[ c3:8 g3:8 e3:8 g3:8 ] [ g2:8 d3:8 b2:8 d3:8 ]'], sp=0.3),
 'k_alb_pats': tune(['s:1', 's:1', 's:1'], None, ['[ c3:8 g3:8 e3:8 g3:8 ] [ c3:8 g3:8 e3:8 g3:8 ]', '[ f2:8 c3:8 a2:8 c3:8 ] [ f2:8 c3:8 a2:8 c3:8 ]', '[ g2:8 d3:8 b2:8 d3:8 ] [ g2:8 d3:8 b2:8 d3:8 ]'], sp=0.35),
}
S.update({
 'k_mary_q1': tune(MARY[:4], ['?', '?', '?', '?']),
 'k_mary_a': tune(MARY[:4], ['C', 'C', 'G', 'C']), 'k_mary_b': tune(MARY[4:], ['C', 'C', 'G', 'C']),
 'k_two': tune(MARY[2:4], ['G', '?']),
 'k_step1': tune(MARY[:2], ['C', 'C'], ['c3:1', 'c3:1']), 'k_step2': tune(MARY[:2], ['C', 'C'], ['(c3.g3):1', '(c3.g3):1']), 'k_step3': tune(MARY[:2], ['C', 'C'], ['(c3.e3.g3):1', '(c3.e3.g3):1']),
 'k_pulse_q': tune(MARY[:4], ['C', '?', '?', '?'], ['c3 c3 c3 c3', 'r:1', 'r:1', 'r:1']),
 'k_pat3': tune(['(c3.g3):1', '(c3.g3):2 (c3.g3):2', 'c3 c3 c3 c3'], ['C', 'C', 'C'], clef='F', sp=0.4),
 'k_moves': tune(['c3:1', 'f3:1', 'g2:1'], ['C', 'F', 'G'], clef='F', sp=0.5),
 'k_brk_q': tune(['g2 b2 d3 b2'], None, clef='F', sp=0.6),
 'k_brk_pats': tune(['c3 e3 g3 e3', 'c3 e3 g3:2', 'c3 g3 c4 g3'], ['C', 'C', 'C'], clef='F', sp=0.4),
 'k_oompah': tune(['c3 (e3.g3) (e3.g3)', 'f2 (a2.c3) (a2.c3)', 'g2 (b2.d3) (b2.d3)'], ['C', 'F', 'G'], meter='3/4', clef='F', sp=0.45),
 'k_alb_pats': tune(['[ c3:8 g3:8 e3:8 g3:8 ] [ c3:8 g3:8 e3:8 g3:8 ]', '[ f2:8 c3:8 a2:8 c3:8 ] [ f2:8 c3:8 a2:8 c3:8 ]', '[ g2:8 d3:8 b2:8 d3:8 ] [ g2:8 d3:8 b2:8 d3:8 ]'], ['C', 'F', 'G'], clef='F', sp=0.35),
 'k_broken': tune(TW, TWC, ['c3 e3 g3 e3', 'f2 c3 c3 g3', 'f2 c3 c3 g3', 'g2 d3 c3 g3'], sp=0.3),
 'k_sym': tune(['(c4.e4.g4):1', '(a4.c5.e5):1', '(g4.b4.d5.f5):1', '(f4.a4.c5):1'], ['C', 'Am', 'G7', 'F'], sp=0.5),
})
json.dump(S, open('/tmp/claude-0/pk/ex/accsnips.json', 'w'), indent=0)
subprocess.run(['node', '/tmp/claude-0/vrv/vrve.mjs', '/tmp/claude-0/pk/ex/accsnips.json', '/tmp/claude-0/pk/ex/accout_raw.json'], check=True, capture_output=True)
subprocess.run(['node', '/tmp/claude-0/vrv/center.js', '/tmp/claude-0/pk/ex/accout_raw.json', '/tmp/claude-0/pk/ex/accout.json'], check=True, capture_output=True, cwd='/tmp/e2e')
print('ok acc snippets', len(S))
