import json
S = {}
def w(k, clef, src): S[k] = dict(clef=clef, src=src, nobar=True, sp=0.3)
w('x_CABBAGE', 'G', 'c5 a4 b4 b4 a4 g4 e4'); w('x_CAFE', 'F', 'c3 a2 f3 e3'); w('x_BADGE', 'G', 'b4 a4 d5 g4 e5')
w('x_EGG', 'F', 'e3 g2 g2'); w('x_FADE', 'G', 'f4 a4 d5 e5'); w('x_EDGE', 'F', 'e3 d3 g3 e2')
S['sd_a'] = dict(clef='G', src='e4 f4 g4 a4 | g4 f4 e4 d4 | c4 d4 e4 f4 | g4:2 g4:2', dur='4', meter='4/4', sp=0.35)
S['sd_b'] = dict(clef='G', src='e4 f4 g4 b4 | g4 f#4 e4 d4 | c4 e4 e4 a4 | g4:2 e4:2', dur='4', meter='4/4', sp=0.35)
json.dump(S, open('gsnips.json', 'w')); print(len(S))
