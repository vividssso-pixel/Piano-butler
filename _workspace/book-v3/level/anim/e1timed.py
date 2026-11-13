import sys, json
sys.argv = [sys.argv[0]]; sys.path.insert(0, '/tmp/claude-0/tts')
import storyaudio as S, audio as A
G = {}; exec(open('/tmp/claude-0/lvl/tease.py').read(), G)
rid = 'hbr-E1'; L = S.lines_for(rid)
# her 14 Nov: more time with piano. The opening plays the chord forte, then piano; the ending lets a soft tune ring after Clara plays again
L = [('piano', '[f C4 E4 G4] [f C4 E4 G4] [pp C4 E4 G4]') if l[0] == 'piano' else l for l in L]
k = [i for i, l in enumerate(L) if l[0] == 'N' and l[1].startswith('So Clara plays it again')][0]
L = L[:k + 1] + [('piano', 'pp:E4 pp:G4 pp:C5 pp:G4 pp:E4 pp:C4*2'), ('pause', .6)] + L[k + 1:]
L = L + [('pause', 0.6), ('N', 'Behind the next door.'), ('N', G['TEASE'][rid]), ('piano', 'pp:G4 pp:C5*2')]
tl = []; w = A.render(L, tl, first=True); A.mp3(w, '/tmp/claude-0/anim/e1.mp3')
json.dump({'dur': round(len(w) / A.SR, 2), 'lines': tl}, open('/tmp/claude-0/anim/e1.json', 'w'), indent=1)
print(round(len(w) / A.SR, 1))
