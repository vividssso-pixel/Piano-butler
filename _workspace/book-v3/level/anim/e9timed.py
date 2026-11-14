import sys, json
sys.argv = [sys.argv[0]]; sys.path.insert(0, '/tmp/claude-0/tts')
import storyaudio as S, audio as A
G = {}; exec(open('/tmp/claude-0/lvl/tease.py').read(), G)
rid = 'hbr-ear-beginner'; L = S.lines_for(rid)
# someone plays behind the door; then the listening game, then how it ended
k = [i for i, l in enumerate(L) if l[0] == 'piano'][0]
L = L[:1] + [('piano', 'pp:C5 pp:E5 pp:G5 pp:E5 pp:C5*2')] + L[1:k] + [
    ('B', 'Shall we listen with her? Is this note high, or low?'), ('piano', 'C6*2'), ('pause', 2.2), ('N', 'High.'),
    ('B', 'And this one?'), ('piano', 'C2*2'), ('pause', 2.2), ('N', 'Low.'),
    ('B', 'Now two little tunes. The same, or different?'), ('piano', 'C4 E4 G4'), ('pause', .8), ('piano', 'C4 E4 G4'), ('pause', 2.2), ('N', 'The same tune, twice.')] + L[k + 1:]
L = L + [('pause', 0.6), ('B', 'The Butler’s note.'), ('B', G['TEASE'][rid]), ('piano', 'pp:G4 pp:C5*2')]
tl = []; w = A.render(L, tl, first=True); A.mp3(w, '/tmp/claude-0/anim/e9.mp3')
json.dump({'dur': round(len(w) / A.SR, 2), 'lines': tl}, open('/tmp/claude-0/anim/e9.json', 'w'), indent=1)
print(round(len(w) / A.SR, 1))
