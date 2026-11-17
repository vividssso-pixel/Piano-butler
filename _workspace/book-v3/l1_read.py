# Her 17 Nov: Read & listen for the reworked "Piano finger numbers and fingering" (L1): the new clips 2 and 3, the new
# pages' regions, and every L1 line's marks measured again. Edits the live Read & listen page data in place.
import json, re, sys
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
SRC, OUT = sys.argv[1], sys.argv[2]
AUD = '/mnt/user-data/outputs/books/read2/'
h = open(SRC).read()
i = h.index('const CH = ') + len('const CH = '); CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ch_end = i + n1
j = h.index('const REG = ') + len('const REG = '); REG, n2 = json.JSONDecoder().raw_decode(h[j:]); reg_end = j + n2
REG.update({k: {kk: {'b': vv} for kk, vv in v.items()} for k, v in json.load(open('/tmp/claude-0/pk/regs_l1.json')).items()})
new = json.load(open('/tmp/claude-0/tts/l1_clips.json'))
c = next(x for x in CH if x['k'] == 'L1')
def clip(slug):
    title, (lines, sec) = new[slug]
    return {'t': title, 'f': f'audio/L1/{slug}.mp3', 's': sec, 'p': 128 if 'plan' in slug else 127, 'l': lines}
c['clips'][1] = clip('02-plan-your-fingering'); c['clips'][2] = clip('03-example-left-hand-or-right')
for ln in c['clips'][2]['l']:   # the example: question picture until the pause, then the answer
    ln['lens'] = {'k': 'pop', 'src': 'pops/L1-2-q.webp' if ln['who'] in ('B',) and ln['t0'] < 1 or ln['who'] == 'pause' else 'pops/L1-2.webp'}
SPECS = {0: ['C4 D4 E4 F4 G4 F4 E4 D4 C4*2'], 2: ['C4 D4 E4 F4 G4']}
for ci, cl in enumerate(c['clips']):
    path = AUD + cl['f'].split('?')[0]; k = 0; answered = not any(l.get('who') == 'pause' for l in cl['l'])
    for ln in cl['l']:
        if ln.get('who') == 'pause': answered = True
        spec = None
        if ln.get('who') == 'piano': spec = (SPECS.get(ci) or [None])[k] if k < len(SPECS.get(ci, [])) else None; k += 1
        ln.pop('mk', None); ln.pop('sp', None)
        mk = marks.line_marks(ln, spec=spec, REG=REG, audio=path, answered=answered)
        if mk: ln['mk'] = mk
        sp = marks.phrase_spans(ln, path)
        if sp and len(sp) > 1: ln['sp'] = sp
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ch_end:j] + json.dumps(REG, ensure_ascii=False) + h[reg_end:]
open(OUT, 'w').write(h)
for ci, cl in enumerate(c['clips']): print(ci, cl['t'], [(l.get('who'), len(l.get('mk', []))) for l in cl['l']])
