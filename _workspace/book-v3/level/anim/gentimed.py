# timed story track for one room: the story, its piano cue, the hook to the next door; writes anim/rooms/<rid>.mp3 and .json
import sys, json
rid = sys.argv[1]; cue = sys.argv[2] if len(sys.argv) > 2 else None
sys.argv = [sys.argv[0]]; sys.path.insert(0, '/tmp/claude-0/tts')
import storyaudio as S, audio as A
G = {}; exec(open('/tmp/claude-0/lvl/tease.py').read(), G)
L = S.lines_for(rid)
if cue: L = [('piano', cue) if l[0] == 'piano' else l for l in L]
L = L + [('pause', 0.6), ('N', 'Behind the next door.'), ('N', G['TEASE'][rid]), ('piano', 'pp:G4 pp:C5*2')]
tl = []; w = A.render(L, tl, first=True); A.mp3(w, f'/tmp/claude-0/anim/rooms/{rid}.mp3')
json.dump({'dur': round(len(w) / A.SR, 2), 'lines': tl}, open(f'/tmp/claude-0/anim/rooms/{rid}.json', 'w'), indent=1)
print(rid, round(len(w) / A.SR, 1), flush=True)
