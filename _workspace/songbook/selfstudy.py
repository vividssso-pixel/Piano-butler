# The book works without a teacher too (her 7 Nov 14:02: '독학하는 사람들 기준에서도 괜찮아야하니 선생님이 뭐 어쩌겠다 이런건 빼자'):
# every 'your teacher ...' goes. Spot the mistake becomes a printed line with one wrong note, to play and compare with
# page 1; guessing games become 'record it and listen back'; the band on the listening page plays what a teacher played.
# Usage: python3 selfstudy.py   (run after leads.py)
import json, copy
SONGS = ['buns', 'home', 'mary', 'ode', 'jingle', 'twinkle', 'frere', 'london', 'surprise', 'elise']
WRONG = {   # the excerpt's first bar, the bar and note to change, the wrong pitch
 'buns': (0, 0, 1, 'e4'), 'home': (0, 1, 1, 'e4'), 'mary': (0, 0, 2, 'e4'), 'ode': (0, 1, 2, 'd4'), 'jingle': (0, 1, 1, 'f4'),
 'twinkle': (0, 0, 2, 'f4'), 'frere': (0, 1, 2, 'f4'), 'london': (0, 0, 1, 'g4'), 'surprise': (6, 0, 2, 'f4'), 'elise': (0, 1, 1, 'd5')}
YOURS_HOW = 'Pick one and play the whole song that way. Record it on a phone and listen back: does it sound the way you meant?'
TRICK = 'One note here is wrong. Play it, then the same bars on page 1: which note sounds wrong? Circle it.'
REPL = [
 ('Play the tune; your teacher plays the names', 'Play the tune with the band (the listening page): the band plays the names'),
 ('Swap: you say the names, your teacher plays', 'Say the names out loud in time while the band plays'),
 ('Say the names in time while your teacher plays', 'Say the names out loud in time while the band plays'),
 ('Left hand alone: tap the roots while your teacher plays the tune', 'Left hand alone: tap the roots while the recording plays the tune'),
 ('You play the tune; your teacher, or the band on the listening page, plays the names.', 'You play the tune; the band on the listening page plays the names.'),
 ('You play the tune; your teacher, or the band, plays the names.', 'You play the tune; the band on the listening page plays the names.'),
 ('then as a round with your teacher.', 'then as a round with a friend: the second player starts two bars later.'),
 ('Then play it as a <b>round</b> with your teacher: two tunes at once make harmony.', 'Then play it as a <b>round</b> with a friend: two tunes at once make harmony.'),
 ('From the names: your teacher plays the tune, you play the roots A and E', 'From the names: the band plays the tune, you play the roots A and E'),
]
def walk(v):
    if isinstance(v, str):
        for a, b in REPL: v = v.replace(a, b)
        return v
    if isinstance(v, list): return [walk(x) for x in v]
    if isinstance(v, dict): return {k: walk(x) for k, x in v.items()}
    return v
for s in SONGS:
    d = json.load(open(s + '.json'))
    d = walk(d)
    if 'yours' in d: d['yours']['how'] = YOURS_HOW
    d.pop('duet', None)
    # the printed mistake: two bars of the song, one note changed, drawn like page 1 (no words)
    b0, bi, ni, wp = WRONG[s]
    bars = copy.deepcopy(d['bars'][b0:b0 + 2]); right = bars[bi][ni][0]; bars[bi][ni][0] = wp
    d['more'] = [m for m in d.get('more', []) if not m.get('_oops')]
    for k, m in enumerate(d['more']):   # the pattern may have moved down when the old mistake went
        if m.get('_pattern') and 'patt1' in d['jobs']: d['jobs']['patt1'][2]['src'] = k
    tune = {'title': 'Spot the mistake', '_oops': 1, 'bars': bars, 'answer': [b0 + bi + 1, right, wp]}
    if 'leadch' in d: tune['leadch'] = []
    d['more'].append(tune); src = len(d['more']) - 1
    J = d['jobs']; base = dict(J['sing1'][2])
    for k in ('words', 'lys', 'lws', 'lh', 'dyn', 'ltm', 'vdown', 'snl', 'fing1', 'mix', 'meter'): base.pop(k, None)
    base.update({'src': src, 'fing': 0})
    if (d.get('hand') or {}).get(wp) == 'L': base['mix'] = 1
    J['oops1'] = [0, 2, base]
    d['trick'] = TRICK
    # the patterns' text with the band, not a teacher
    json.dump(d, open(s + '.json', 'w'), ensure_ascii=False, indent=0)
    print(s, 'mistake in bar', b0 + bi + 1, right, '->', wp)
