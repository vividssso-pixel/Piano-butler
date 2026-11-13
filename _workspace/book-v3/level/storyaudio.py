# Her 14 Nov ("오디오랑 같이 가야 연결점 찾기가 쉽더라"): one audio track per room story: the scene, a pause to try it, how it ended.
# The Butler narrates; quoted lines go to the speaker named beside them (King, Queen, Doorkeeper, Stationmaster).
import sys, re, json, os
sys.argv = [sys.argv[0]]
sys.path.insert(0, '/tmp/claude-0/tts')
import numpy as np
import audio as A
A.VOICE['N'] = ('bf_alice', 0.95)   # the storyteller: a warm, unhurried voice; the residents speak in their own voices
src = open('/tmp/claude-0/lvl/levelstory.py').read().split("def build_story")[0]
G = {}; exec(src, G)
STORY = G['STORY']
CUE = {'hbr-B1': 'C4 E4 G4 C5', 'hbr-P1': 'C2*2 C6*2', 'hbr-L1': 'C4 D4 E4 F4 G4', 'hbr-P2': 'G4*2 F3*2', 'hbr-T1': 'C4 C4 C4 C4', 'hbr-T2': 'C4 C4*2',
       'hbr-T2-s2': 'C4*4', 'hbr-E1': '[ff C4 E4 G4] [pp C4 E4 G4]', 'hbr-ear-beginner': 'G4 E5', 'hbr-L2': 'C4 D4 E4 F4 G4', 'x-dyn': '[pp C4 E4 G4] [p C4 E4 G4] [ff C4 E4 G4]',
       'hbr-P3': 'C4*2', 'hbr-P4': 'E4 G4 B4 D5 F5', 'hbr-T3': 'C4 C4/2 C4/2 C4/4 C4/4 C4/4 C4/4', 'hbr-T4': 'C4 E4 G4 C4 E4 G4', 'hbr-T8': 'C4 C4 G4 G4 A4 A4 G4*2',
       'hbr-E2': 'C4 D4 E4 F4 G4', 'hbr-S1': 'G4 A4 B4 C5 D5 E5 F#5 G5', 'hbr-S2': 'A3 B3 C4 D4 E4 F4 G4 A4', 'hbr-H1': 'C4 E4 G4 [C4 E4 G4]', 'hbr-ear-prelim': 'C5 E5 G5'}
NAMES = [('King', 'K'), ('Queen', 'Q'), ('Doorkeeper', 'D'), ('Stationmaster', 'S'), ('Butler', 'B')]
def plain(h): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', re.sub(r'<i>(col piano e forte|forte|piano)</i>', r'⟨\1⟩', h)).replace('&nbsp;', ' ')).strip()
def voiced(text):   # the storyteller narrates; a quote is spoken only when a speaker is named next to it ("says the King")
    out = []; pos = 0
    for m in re.finditer(r'“(.*?)”', text):
        after = text[m.end():m.end() + 30]; before = text[max(0, m.start() - 70):m.start()]
        if not re.search(r'\b(says|said|asks|he says|she says)\b', after + ' ' + text[max(0, m.start() - 20):m.start()]): continue
        pre = text[pos:m.start()].strip(' ,')
        if pre: out.append(('N', pre))
        ctx = before + ' ' + after; who = 'B'
        for nm, v in NAMES:
            if nm in after: who = v; break
        else:
            hits = [(ctx.rfind(nm), v) for nm, v in NAMES if nm in before]
            if hits: who = max(hits)[1]
        out.append((who, m.group(1).strip(' ,'))); pos = m.end()
    post = text[pos:].strip(' ,')
    if post: out.append(('N', post))
    return out
def lines_for(rid):
    op, en = STORY[rid]; L = []
    for p in re.findall(r'<p>(.*?)</p>', op[1], flags=re.S): L += voiced(plain(p))
    L += [('piano', CUE.get(rid, 'C4 E4 G4')), ('B', 'Now, at the piano. ' + plain(op[2])), ('pause', 6)]
    if en:
        L += [('N', 'And here is how it ended.')]
        for p in re.findall(r'<p>(.*?)</p>', en[1], flags=re.S): L += voiced(plain(p))
        L += [('B', 'One more thing to try. ' + plain(en[2])), ('pause', 6)]
    return L
if __name__ == '__main__':
    OUT = '/mnt/user-data/outputs/audio-stories'; os.makedirs(OUT, exist_ok=True); meta = {}
    keys = [k for k in STORY if (len(sys.argv) < 2 or k in sys.argv[1:])]
    for rid in os.environ.get('ONLY', '').split() or keys:
        L = lines_for(rid); w = A.render(L, None, first=True); fn = f'{OUT}/{rid}.mp3'; A.mp3(w, fn)
        meta[rid] = {'sec': round(len(w) / A.SR), 'lines': [l for l in L if l[0] != 'pause']}; print(rid, meta[rid]['sec'], 's', flush=True)
    json.dump(meta, open(f'{OUT}/stories.json', 'w'), indent=1, ensure_ascii=False)
