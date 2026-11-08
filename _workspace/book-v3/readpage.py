# "Read & listen" (her 8 Nov): the Handbook online, page by page, with the Butler's audio for each chapter that has it.
# Writes /mnt/user-data/outputs/books/read/ : index.html, pages/pNNN.webp (from the merged Handbook PDF), audio/<key>/ clips.
import json, os, glob, shutil, subprocess, sys
sys.path.insert(0, '/tmp/claude-0/pk'); import pagemap as PM, openart as OA, checkbank as CB
OUT = '/mnt/user-data/outputs/books/read'
os.makedirs(OUT + '/pages', exist_ok=True)
if '--pages' in sys.argv:   # re-render the page images from the merged PDF (pdf page + 20 = printed page)
    tmp = '/tmp/claude-0/read/pages'; os.makedirs(tmp, exist_ok=True)
    for f in glob.glob(tmp + '/*'): os.remove(f)
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=72', '-scale-to-x', '1000', '-scale-to-y', '-1', '/mnt/user-data/outputs/books/handbook-draft.pdf', tmp + '/pg'], check=True)
    from PIL import Image
    for f in sorted(glob.glob(tmp + '/pg-*.jpg')):
        n = int(os.path.basename(f)[3:6]) + 20; Image.open(f).save(f'{OUT}/pages/p{n:03d}.webp', 'WEBP', quality=70, method=5)
else:
    for f in glob.glob('/tmp/claude-0/read/pages/*.webp'): shutil.copy(f, OUT + '/pages/')
LAST = max(int(os.path.basename(f)[1:4]) for f in glob.glob(OUT + '/pages/*.webp'))
TIPS = {L[-1][3]: L[-1][1] for L in (OA.LEG_P, OA.LEG_T, OA.LEG_E, OA.LEG_S, OA.LEG_H, OA.LEG_M, OA.LEG_F, OA.LEG_L)}
PNAME = dict(CB.PARTS)
CH = []
for p, name, k in PM.PARTS:
    part = PNAME[p]
    CH.append({'k': p + 'O', 'part': part, 't': 'Opening map', 'pages': [PM.PAGE[p + 'O']]})
    for i in range(1, k + 1):
        key = f'{p}{i}'; a, n = PM.pages_of(key)
        CH.append({'k': key, 'part': part, 't': f'{i} · {CB.TITLES[key]}', 'pages': list(range(a, a + n))})
    CH.append({'k': p + 'T', 'part': part, 't': TIPS[p + 'T'], 'pages': [PM.PAGE[p + 'T']]})
CH.append({'k': 'X', 'part': 'At the end', 't': 'Putting it together', 'pages': [PM.PAGE['X'], PM.PAGE['X'] + 1]})
CH.append({'k': 'GL', 'part': 'At the end', 't': 'Glossary and index', 'pages': list(range(PM.PAGE['X'] + 2, LAST + 1))})
# audio: clips.json per chapter; clip 1 sits on the chapter's first page, the last on its last page, the rest on page 2
for c in CH:
    j = f'/mnt/user-data/outputs/audio/{c["k"]}/clips.json'
    if not os.path.exists(j): continue
    meta = json.load(open(j)); d = f'{OUT}/audio/{c["k"]}'; os.makedirs(d, exist_ok=True)
    n = len(meta['clips']); pg = c['pages']
    c['clips'] = []
    for i, m in enumerate(meta['clips']):
        shutil.copy(f'/mnt/user-data/outputs/audio/{c["k"]}/{m["file"]}', d)
        at = pg[0] if i == 0 else (pg[-1] if i == n - 1 else pg[min(1, len(pg) - 1)])
        c['clips'].append({'t': m['title'], 'f': f'audio/{c["k"]}/{m["file"]}', 's': m['sec'], 'p': at, 'l': m.get('lines', [])})
RG = json.load(open('/tmp/claude-0/pk/regions.json')) if os.path.exists('/tmp/claude-0/pk/regions.json') else {}
REG = {}
for c in CH:
    for k in c.get('clips', []):
        for ln in k['l']:
            pg = str(ln.get('cue', {}).get('p', ''))
            if pg and pg in RG and pg not in REG:
                seen = {}; REG[pg] = {}
                for b in RG[pg]:
                    seen[b['key']] = seen.get(b['key'], 0) + 1; key = b['key'] + (str(seen[b['key']]) if seen[b['key']] > 1 else '')
                    REG[pg][key] = {'b': b['box'], 'l': b['labs'], 'r': b.get('res')}
# her 8 Nov: as each term is spoken, mark its key on the page there and then. Kokoro gives no word timings, so a term's
# moment is estimated from where it sits in the line (speech runs evenly enough over a short sentence).
import re as _re
_LAST = {}
def _hits(ln):
    c = ln.get('cue') or {}; reg = (REG.get(str(c.get('p', ''))) or {}).get(c.get('r'))
    text = ln.get('text') or ''
    if not reg or not text or ln.get('who') not in ('B', 'P') or str(c.get('r', '')).startswith('ex'): return []
    names = sorted({L[0] for L in reg['l'] if _re.search('[A-Z]', L[0]) and L[0] != '?'}, key=len, reverse=True)
    used = [False] * len(text); out = []
    for nm in names:
        for m in _re.finditer(r'(?<![A-Za-z])' + _re.escape(nm) + r'(?![A-Za-z0-9])', text):
            if any(used[m.start():m.end()]): continue
            if nm == 'A':   # the article "A" opens a sentence and is followed by a lower-case word
                pre = text[:m.start()].rstrip()
                if (pre == '' or pre[-1] in '.!?') and _re.match(r'A [a-z]', text[m.start():]): continue
            for q in range(m.start(), m.end()): used[q] = True
            out.append((m.start(), m.end(), nm))
    out.sort(); d = max(0.3, ln['t1'] - ln['t0'] - 0.35); L = max(1, len(text))
    labs = reg['l']; occ = {nm: [i for i, x in enumerate(labs) if x[0] == nm] for _, _, nm in out}
    cx = lambda i: labs[i][1][0] + labs[i][1][2] / 2
    pick = [occ[nm][0] if len(occ[nm]) == 1 else None for _, _, nm in out]
    for n in range(len(out)):   # a repeated name: take the one nearest its neighbours in the sentence
        if pick[n] is None:
            near = [pick[m] for m in sorted(range(len(out)), key=lambda m: abs(m - n)) if m != n and pick[m] is not None]
            ref = cx(near[0]) if near else _LAST.get((c.get('p'), c.get('r')))
            pick[n] = min(occ[out[n][2]], key=lambda i: abs(cx(i) - ref)) if ref is not None else occ[out[n][2]][0]
    if pick: _LAST[(c.get('p'), c.get('r'))] = cx(pick[-1])
    return [[round(ln['t0'] + d * a / L - 0.12, 2), '#' + str(pick[n]), a, b] for n, (a, b, nm) in enumerate(out)]
for c in CH:
    for k in c.get('clips', []):
        for ln in k['l']:
            h = _hits(ln)
            if h: ln['hits'] = h
PRACT = {   # chapter: (workbook pages in the merged workbook draft, [(drill id, drill name, extra query)])
    'P1': ((1, 2), [('first-steps', 'Keyboard Patterns', ''), ('note-names', 'The Musical Alphabet', '')]),
    'P2': ((3, 4), [('staff', 'The Staff & the Two Clefs', ''), ('ledger-lines', 'Ledger Lines', '')]),
    'P3': ((5, 6), [('whole-staff', 'Line and Space Names', ''), ('reading-steps', 'Steps & Skips', '')]),
    'P4': ((7, 8), [('staff', 'The Staff & the Two Clefs', ''), ('whole-staff', 'Line and Space Names', '')]),
    'P5': ((9, 10), [('accidentals', 'Accidentals', ''), ('tones', 'Tones & Semitones', '')]),
    'P6': ((11, 12), [('intervals', 'Intervals', ''), ('tones', 'Tones & Semitones', '')]),
    'P7': ((13, 14), [('intervals', 'Intervals', '')]),
}
for c in CH:
    if c['k'] in PRACT: c['pr'] = PRACT[c['k']]
DATA = json.dumps(CH, ensure_ascii=False)
REGD = json.dumps(REG, ensure_ascii=False)
HTML = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex">
<title>Read and Listen</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Playfair+Display:wght@700;800&display=swap">
<style>
/* Layout: a reading desk. The page fills the left; the Butler's clips sit beside it (below it on a phone). */
:root{--bg:#f3f1ea;--panel:#ffffff;--ink:#26296b;--soft:#5a5d8f;--line:#e3e1ee;--accent:#e4572e;--accentbg:#fdece5;--paper:#ffffff;
 --display:'Playfair Display',Georgia,serif;--body:'Atkinson Hyperlegible',system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14153a;--panel:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--accentbg:#3a2620;--paper:#f7f6f1;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#14153a;--panel:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--accentbg:#3a2620;--paper:#f7f6f1;color-scheme:dark}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.45;padding-top:env(safe-area-inset-top,0px)}
.top{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;padding-block:14px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));border-bottom:1px solid var(--line);background:var(--panel)}
.brand{font-family:var(--display);font-weight:800;font-size:20px;margin-right:auto}
.brand small{display:block;font-family:var(--body);font-weight:700;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
select{font:inherit;font-size:15px;color:var(--ink);background:var(--panel);border:1.5px solid var(--line);border-radius:10px;padding:8px 10px;max-width:100%}
.desk{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:18px;max-width:1180px;margin:0 auto;padding-block:16px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
@media (max-width:880px){.desk{grid-template-columns:minmax(0,1fr)}}
.reader{min-width:0;width:100%;max-width:calc((100vh - 190px) / 1.414);justify-self:center} @media (max-width:880px){.reader{max-width:100%}}
.sheet{background:var(--paper);border-radius:4px;box-shadow:0 2px 10px rgba(20,22,60,.12);overflow:hidden;aspect-ratio:210/297;max-width:100%;display:flex;align-items:center;justify-content:center}
.sheet{position:relative} .stage{position:relative;width:100%;transform-origin:0 0;transition:transform .6s ease}
.sheet img{width:100%;height:auto;display:block}
.hl{position:absolute;border:3px solid var(--accent);border-radius:8px;box-shadow:0 0 0 9999px rgba(20,22,60,.18);} .hl.fog{box-shadow:0 0 0 9999px rgba(246,245,240,.94)} .cov{position:absolute;background:#fff;border-radius:3px;pointer-events:none} .cov.res{background:#fff7f3;border:1.5px dashed #e4572e;display:flex;align-items:center;justify-content:center;font:700 clamp(9px,1.4vw,14px) var(--body);color:#e4572e} .hl{transition:all .5s ease;pointer-events:none}
.sub mark,#sub mark{background:#fde3d8;color:#26296b;border-radius:3px;padding:0 2px} .mk{position:absolute;width:3.2%;aspect-ratio:1;border-radius:50%;border:3px solid var(--accent);background:rgba(228,87,46,.25);transform:translate(-50%,-50%);pointer-events:none;animation:pop .35s ease}
@keyframes pop{from{transform:translate(-50%,-50%) scale(.4);opacity:0}to{transform:translate(-50%,-50%) scale(1);opacity:1}}
.sub{min-height:3.2em;margin-top:10px;background:var(--panel);border:1.5px solid var(--line);border-radius:12px;padding:8px 12px;font-size:15.5px}
.sub b{color:var(--accent);margin-right:6px} .sub:empty{display:none}
.ctl{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 10px} .ctl .btn{padding:6px 12px;font-size:14px} .ctl .sp{font-size:12.5px;padding:4px 7px;border-radius:999px} .ctl .sp.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.prac{margin-top:12px;border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;display:flex;flex-direction:column;gap:6px} .prac .ph{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)} .prac a{display:block;font-weight:700;font-size:14.5px;color:var(--ink);text-decoration:none;border:1.5px solid var(--line);border-radius:9px;padding:7px 10px;background:var(--bg)} .prac a.dr{border-color:var(--accent)} .prac a:hover{border-color:var(--accent)}
.follow{display:flex;align-items:center;gap:8px;font-size:14px;color:var(--soft);margin-top:8px}
.nav{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px}
button{font:inherit;cursor:pointer;color:var(--ink)}
.btn{background:var(--panel);border:1.5px solid var(--line);border-radius:10px;padding:8px 14px;font-weight:700}
.btn:disabled{opacity:.4;cursor:default}
.pgno{font-variant-numeric:tabular-nums;color:var(--soft);font-size:14px}
button:focus-visible,select:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.side{background:var(--panel);border:1.5px solid var(--line);border-radius:14px;padding:14px;align-self:start;position:sticky;top:12px}
.side h2{font-family:var(--display);font-size:22px;margin:0 0 2px;text-wrap:balance}
.kick{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.play{display:flex;align-items:center;gap:10px;width:100%;background:var(--accent);color:#fff;border:0;border-radius:12px;padding:11px 14px;font-weight:700;margin:12px 0 8px}
.play svg{flex:none}
.clips{display:grid;gap:6px}
.clip{display:grid;grid-template-columns:26px 1fr auto;align-items:center;gap:8px;text-align:left;background:transparent;border:1.5px solid var(--line);border-radius:10px;padding:8px 10px}
.clip .n{width:24px;height:24px;border-radius:50%;border:1.5px solid var(--soft);display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:700}
.clip .s{font-size:12.5px;color:var(--soft);font-variant-numeric:tabular-nums}
.clip.on{border-color:var(--accent);background:var(--accentbg)} .clip.on .n{background:var(--accent);border-color:var(--accent);color:#fff}
audio{width:100%;margin-top:10px}
.none{color:var(--soft);font-size:14.5px;margin:10px 0 0}
.who{font-size:13px;color:var(--soft);margin-top:12px;border-top:1px solid var(--line);padding-top:10px}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto} .stage,.hl{transition:none}}
</style></head><body>
<header class="top"><div class="brand"><small>The Piano Butler Handbook</small>Read and listen</div><label class="sr" for="ch" style="position:absolute;left:-9999px">Chapter</label><select id="ch"></select></header>
<main class="desk">
 <section class="reader"><a class="sheet" id="zoom" target="_blank" rel="noopener" title="Open the page full size"><div class="stage" id="stage"><img id="img" alt=""><div id="ov"></div></div></a><div class="sub" id="sub"></div>
  <div class="nav"><button class="btn" id="prev">‹ Page</button><span class="pgno" id="pgno"></span><button class="btn" id="next">Page ›</button></div></section>
 <aside class="side" id="side"></aside>
</main>
<script>
const CH = __DATA__; const REG = __REG__;
const sel = document.getElementById('ch'), img = document.getElementById('img'), side = document.getElementById('side');
let ci = 0, pi = 0, playing = -1, chain = false, rate = 1;
const audio = new Audio(); audio.preload = 'none';
const parts = [...new Set(CH.map(c => c.part))];
sel.innerHTML = parts.map(p => `<optgroup label="${p}">` + CH.map((c, i) => c.part === p ? `<option value="${i}">${c.t}${c.clips ? ' ♪' : ''}</option>` : '').join('') + '</optgroup>').join('');
const pad = n => String(n).padStart(3, '0');
function showPage() {
  const c = CH[ci], n = c.pages[pi];
  img.src = `pages/p${pad(n)}.webp`; document.getElementById('zoom').href = img.src; img.alt = `Handbook page ${n}`;
  document.getElementById('pgno').textContent = `p. ${n} · ${pi + 1} of ${c.pages.length}`;
  document.getElementById('prev').disabled = ci === 0 && pi === 0; document.getElementById('next').disabled = ci === CH.length - 1 && pi === c.pages.length - 1;
  const nx = CH[ci + 1]; if (nx) { const im = new Image(); im.src = `pages/p${pad(nx.pages[0])}.webp`; }
}
function site(p) { const local = location.protocol === 'file:' || /thepianobutler\.com$/.test(location.hostname); return (local ? '../../' : 'https://thepianobutler.com/') + p; }
function drawSide() {
  const c = CH[ci];
  side.innerHTML = `<div class="kick">${c.part}</div><h2>${c.t}</h2>` + (c.clips ? `<button class="play" id="all"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M4 2l12 7-12 7z" fill="currentColor"/></svg>${playing >= 0 ? 'Playing…' : 'Listen to the whole chapter'}</button><div class="ctl"><button class="btn" id="pp">${audio.paused ? '▶ Resume' : '❚❚ Pause'}</button>${[0.8, 1, 1.2, 1.5].map(v => `<button class="btn sp${v === rate ? ' on' : ''}" data-v="${v}">${v}×</button>`).join('')}</div><div class="clips">` +
    c.clips.map((k, i) => `<button class="clip${i === playing ? ' on' : ''}" data-i="${i}"><span class="n">${i + 1}</span><span>${k.t}</span><span class="s">${Math.floor(k.s / 60)}:${String(k.s % 60).padStart(2, '0')}</span></button>`).join('') + '</div>'
    : `<p class="none">No audio for this chapter yet. The pages are all here.</p>`) + (c.pr ? `<div class="prac"><div class="ph">Practise it</div><a href="${site('books/workbook-draft.pdf')}#page=${c.pr[0][0]}" target="_blank" rel="noopener">Workbook pp. ${c.pr[0][0]}–${c.pr[0][1]}</a>${c.pr[1].map(d => `<a class="dr" href="${site('drills.html')}?drill=${d[0]}${d[2] || '&tab=learn'}" target="_blank" rel="noopener">Drill: ${d[1]}</a>`).join('')}</div>` : '') + `<label class="follow"><input type="checkbox" id="fol" ${follow ? 'checked' : ''}> Follow on the page</label><p class="who">The Butler explains, Pip asks. Each Example asks first, then pauses so you can try.</p>`;
  const fo = document.getElementById('fol'); if (fo) fo.onchange = () => { follow = fo.checked; };
  if (c.clips) { const pp = document.getElementById('pp'); pp.disabled = playing < 0; pp.onclick = () => { if (audio.paused) { audio.play().catch(() => {}); } else audio.pause(); drawSide(); };
    side.querySelectorAll('.sp').forEach(b => b.onclick = () => { rate = +b.dataset.v; audio.playbackRate = rate; drawSide(); });
    document.getElementById('all').onclick = () => { chain = true; play(0); }; side.querySelectorAll('.clip').forEach(b => b.onclick = () => { chain = false; play(+b.dataset.i); }); }
}
function play(i) {
  const k = CH[ci].clips[i]; playing = i; audio.src = k.f; audio.playbackRate = rate; audio.play().catch(() => {});
  const p = CH[ci].pages.indexOf(k.p); if (p >= 0) { pi = p; showPage(); } drawSide();
}
let follow = true;
const stage = document.getElementById('stage'), ov = document.getElementById('ov'), sub = document.getElementById('sub');
function clearFollow() { ov.innerHTML = ''; stage.style.transform = ''; sub.textContent = ''; }
function findLab(reg, name) { if (/^#\d+$/.test(name)) return reg.l[+name.slice(1)]; const m = reg.l.filter(x => x[0] === name); if (m.length < 2) return m[0]; const q = reg.l.find(x => x[0] === '?'); if (!q) return m[0]; return m.reduce((a, b) => Math.abs(b[1][0] - q[1][0]) < Math.abs(a[1][0] - q[1][0]) ? b : a); }
function tick() {
  if (playing < 0) return; const k = CH[ci].clips[playing], t = audio.currentTime; const ln = k.l.find(x => t >= x.t0 && t < x.t1);
  if (!ln) { requestAnimationFrame(tick); return; }
  const hit = ln.hits ? ln.hits.filter(h => h[0] <= t).pop() : null; let txt = ln.text || ''; if (hit) txt = txt.slice(0, hit[2]) + '<mark>' + txt.slice(hit[2], hit[3]) + '</mark>' + txt.slice(hit[3]);
  sub.innerHTML = ln.text ? `<b>${ln.who === 'B' ? 'Butler' : ln.who === 'P' ? 'Pip' : ''}</b>${txt}` : (ln.who === 'piano' ? '<b>♪</b>listen' : '');
  const c = ln.cue;
  if (c && follow) {
    const pidx = CH[ci].pages.indexOf(c.p); if (pidx >= 0 && pidx !== pi) { pi = pidx; showPage(); }
    const reg = (REG[c.p] || {})[c.r];
    if (reg) {
      const [x, y, w, h] = reg.b; const S = Math.min(2.2, Math.max(1, 0.94 / w));
      const tx = Math.min(0, Math.max(1 - S, 0.5 - S * (x + w / 2))), ty = Math.min(0, Math.max(1 - S, 0.42 - S * (y + h / 2)));
      stage.style.transform = `translate(${tx * 100}%, ${ty * 100}%) scale(${S})`;
      let marks = []; if (c.lab) marks = c.lab; if (hit) marks = [hit[1]]; if (c.seq && ln.notes) { const i = ln.notes.filter(v => v <= t).length - 1; if (i >= 0) marks = [c.seq[Math.min(i, c.seq.length - 1)]]; }
      const exm = /^ex/.test(c.r) && !c.reveal; const vis = new Set([...(c.show || []), ...marks, '?']);
      const key = c.p + c.r + marks.join(',') + (exm ? 'x' + [...vis].join('') : ''); if (ov.dataset.k !== key) { ov.dataset.k = key;
        const covers = exm ? reg.l.filter(L => !vis.has(L[0])).map(L => `<div class="cov" style="left:${L[1][0] * 100 - .3}%;top:${L[1][1] * 100 - .2}%;width:${L[1][2] * 100 + .6}%;height:${L[1][3] * 100 + .4}%"></div>`).join('') + (reg.r ? `<div class="cov res" style="left:${reg.r[0] * 100}%;top:${reg.r[1] * 100}%;width:${reg.r[2] * 100}%;height:${reg.r[3] * 100}%">Answer coming…</div>` : '') : '';
        ov.innerHTML = covers + `<div class="hl${/^ex/.test(c.r) ? ' fog' : ''}" style="left:${x * 100 - .6}%;top:${y * 100 - .4}%;width:${w * 100 + 1.2}%;height:${h * 100 + .8}%"></div>` +
          marks.map(m => findLab(reg, m)).filter(Boolean).map(L => `<div class="mk" style="left:${(L[1][0] + L[1][2] / 2) * 100}%;top:${(L[1][1] + L[1][3] / 2) * 100}%;width:${Math.max(3.2, L[1][2] * 100 + 2.4)}%"></div>`).join(''); }
    }
  } else if (!c || !follow) { stage.style.transform = ''; ov.innerHTML = ''; ov.dataset.k = ''; }
  requestAnimationFrame(tick);
}
audio.onplay = () => { requestAnimationFrame(tick); drawSide(); }; audio.onpause = () => { if (playing >= 0) drawSide(); };
audio.onended = () => { const c = CH[ci]; if (chain && playing + 1 < c.clips.length) play(playing + 1); else { playing = -1; drawSide(); clearFollow(); } };
function go(i, p = 0) { audio.pause(); playing = -1; if (typeof clearFollow === 'function') clearFollow(); ci = i; pi = p; sel.value = i; showPage(); drawSide(); history.replaceState(null, '', '#' + CH[i].k); window.scrollTo(0, 0); }
sel.onchange = () => go(+sel.value);
document.getElementById('prev').onclick = () => { if (pi > 0) { pi--; showPage(); } else if (ci > 0) go(ci - 1, CH[ci - 1].pages.length - 1); };
document.getElementById('next').onclick = () => { if (pi < CH[ci].pages.length - 1) { pi++; showPage(); } else if (ci < CH.length - 1) go(ci + 1); };
document.addEventListener('keydown', e => { if (e.target.tagName === 'SELECT') return; if (e.key === 'ArrowRight') document.getElementById('next').click(); if (e.key === 'ArrowLeft') document.getElementById('prev').click(); });
const start = CH.findIndex(c => c.k === (location.hash.slice(1) || new URLSearchParams(location.search).get('ch') || 'P1'));
go(start >= 0 ? start : 0);
</script></body></html>'''
open(OUT + '/index.html', 'w').write(HTML.replace('__DATA__', DATA).replace('__REG__', REGD))
print('ok read page', len(CH), 'sections,', sum(1 for c in CH if c.get('clips')), 'with audio, last page', LAST)
