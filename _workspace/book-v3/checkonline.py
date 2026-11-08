# The Handbook check, online (her 8 Nov): the same 144 questions; marks itself and draws the chapter map.
import json
BANK = json.load(open('/tmp/claude-0/pk/checkbank.json'))
data = json.dumps([{'k': c['key'], 'p': c['part'], 't': c['title'], 'pg': c['page'], 'q': [[q['q'], q['o'], q['a']] for q in c['qs']]} for c in BANK], ensure_ascii=False)
page = r'''<title>Where Do I Start?</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Playfair+Display:wght@700;800&display=swap">
<style>
/* Layout: one column, a book-like card per chapter; the map of all 48 chapters is the home screen */
:root{--bg:#fbfaf6;--card:#ffffff;--ink:#26296b;--soft:#5a5d8f;--line:#e3e1ee;--accent:#e4572e;--good:#2f7d4a;--goodbg:#e3f1e6;--mid:#a56a00;--midbg:#fdf1d6;--badbg:#fde3d8;
 --display:'Playfair Display',Georgia,serif;--body:'Atkinson Hyperlegible',system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15163a;--card:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--good:#7fd39a;--goodbg:#1f3b2c;--mid:#f0c060;--midbg:#3b3018;--badbg:#45261e;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15163a;--card:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--good:#7fd39a;--goodbg:#1f3b2c;--mid:#f0c060;--midbg:#3b3018;--badbg:#45261e;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.5}
.wrap{max-width:760px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px}
h1{font-family:var(--display);font-weight:800;font-size:clamp(34px,7vw,52px);line-height:1.05;margin:4px 0 10px;text-wrap:balance}
h2{font-family:var(--display);font-size:24px;margin:0;text-wrap:balance}
.kick{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.lead{color:var(--soft);max-width:60ch;margin:0 0 18px}
.legend{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
.pill{display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:4px 12px;font-size:13.5px;font-weight:700}
.pill.g{background:var(--goodbg);color:var(--good)} .pill.y{background:var(--midbg);color:var(--mid)} .pill.r{background:var(--badbg);color:var(--accent)} .pill.n{background:transparent;border:1.5px dashed var(--line);color:var(--soft)}
.start{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:22px}
button{font:inherit;cursor:pointer;border-radius:10px}
.btn{background:var(--accent);color:#fff;border:0;padding:11px 20px;font-weight:700;font-size:16px}
.btn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--line)}
.btn:disabled{opacity:.45;cursor:default}
button:focus-visible,label:focus-within{outline:3px solid var(--accent);outline-offset:2px}
.parts{display:grid;gap:14px}
.part{background:var(--card);border:1.5px solid var(--line);border-radius:14px;padding:12px 14px}
.ph{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.ph h3{margin:0;font-size:16px;flex:1;min-width:0}
.ph .sel{display:inline-flex;align-items:center;gap:6px;font-size:14px;color:var(--soft)}
.ph input{width:18px;height:18px;accent-color:var(--accent)}
.ch{display:grid;grid-template-columns:34px 1fr auto auto;gap:8px;align-items:center;padding:6px 0;border-top:1px solid var(--line);font-size:15px}
.ch .k{font-weight:700;font-size:12.5px;color:var(--soft);font-variant-numeric:tabular-nums}
.ch .t{min-width:0} .ch .pg{color:var(--soft);font-size:13px;font-variant-numeric:tabular-nums;white-space:nowrap}
.ch .pill{padding:2px 10px;font-size:12.5px}
.next{background:var(--card);border:2px solid var(--accent);border-radius:14px;padding:14px 16px;margin:0 0 18px}
.next b{font-size:18px}
.quiz{background:var(--card);border:1.5px solid var(--line);border-radius:16px;padding:18px}
.bar{height:6px;background:var(--line);border-radius:6px;overflow:hidden;margin:6px 0 16px} .bar i{display:block;height:100%;background:var(--accent);transition:width .3s}
.q{margin:14px 0 4px;font-weight:700}
.opts{display:grid;gap:8px}
.opt{display:flex;align-items:center;gap:10px;border:1.5px solid var(--line);border-radius:10px;padding:9px 12px;background:transparent;color:var(--ink);text-align:left;width:100%}
.opt .l{flex:none;width:26px;height:26px;border-radius:50%;border:1.5px solid var(--soft);display:inline-flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.opt[aria-pressed="true"]{border-color:var(--accent)} .opt[aria-pressed="true"] .l{background:var(--accent);border-color:var(--accent);color:#fff}
.opt.right{border-color:var(--good);background:var(--goodbg)} .opt.wrong{border-color:var(--accent);background:var(--badbg)}
.dk{font-size:14px;color:var(--soft);margin-top:4px}
.row{display:flex;gap:10px;flex-wrap:wrap;justify-content:space-between;align-items:center;margin-top:18px}
.verdict{border-radius:12px;padding:12px 14px;margin-top:14px;font-weight:700}
.note{font-size:13.5px;color:var(--soft);margin-top:24px}
@media (prefers-reduced-motion:reduce){.bar i{transition:none}}
@media (max-width:480px){.ch{grid-template-columns:30px 1fr auto}.ch .pg{display:none}}
</style>
<div class="wrap">
 <div class="kick">The Piano Butler Handbook · Check</div>
 <h1>Where do I start?</h1>
 <p class="lead">Three questions for each chapter. Get all three and you can skip it; two, skim it; fewer, that is where to start reading. Tick the parts you want to check.</p>
 <div class="legend"><span class="pill g">3 right · skip it</span><span class="pill y">2 right · skim it</span><span class="pill r">0–1 right · study it</span><span class="pill n">not checked yet</span></div>
 <main id="app"></main>
 <p class="note">Your results stay in this browser only. The same questions are printed in the booklet “Where do I start?”.</p>
</div>
<script>
const BANK = __DATA__;
const L = 'ABC', KEY = 'pb-check-v1';
let res = {}; try { res = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { res = {}; }
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(res)); } catch (e) {} };
const parts = [...new Set(BANK.map(c => c.p))];
let picked = new Set([parts[0]]), queue = [], qi = 0, ans = [], shown = false;
const app = document.getElementById('app');
const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const pill = s => s == null ? '<span class="pill n">not yet</span>' : s === 3 ? '<span class="pill g">skip</span>' : s === 2 ? '<span class="pill y">skim</span>' : '<span class="pill r">study</span>';
function home() {
  const firstRed = BANK.find(c => res[c.k] != null && res[c.k] < 2) || BANK.find(c => res[c.k] === 2);
  const done = BANK.filter(c => res[c.k] != null).length;
  app.innerHTML = (firstRed ? `<div class="next"><div class="kick">Start here</div><b>${esc(firstRed.k)} · ${esc(firstRed.t)}</b><div>Handbook p. ${firstRed.pg}</div></div>` : '') +
   `<div class="start"><button class="btn" id="go" ${picked.size ? '' : 'disabled'}>Check ${picked.size === 1 ? 'this part' : picked.size + ' parts'}</button>` +
   (done ? `<button class="btn ghost" id="reset">Clear my results</button><span class="dk">${done} of 48 chapters checked</span>` : '') + `</div><div class="parts">` +
   parts.map((p, i) => `<section class="part"><div class="ph"><h3>${esc(p)}</h3><label class="sel"><input type="checkbox" id="pt${i}" data-p="${esc(p)}" ${picked.has(p) ? 'checked' : ''}> check it</label></div>` +
     BANK.filter(c => c.p === p).map(c => `<div class="ch"><span class="k">${c.k}</span><span class="t">${esc(c.t)}</span><span class="pg">p. ${c.pg}</span>${pill(res[c.k])}</div>`).join('') + `</section>`).join('') + `</div>`;
  app.querySelectorAll('input[data-p]').forEach(x => x.onchange = () => { x.checked ? picked.add(x.dataset.p) : picked.delete(x.dataset.p); home(); });
  document.getElementById('go').onclick = () => { queue = BANK.filter(c => picked.has(c.p)); qi = 0; quiz(); };
  const r = document.getElementById('reset'); if (r) { let armed = false; r.onclick = () => { if (!armed) { armed = true; r.textContent = 'Tap again to clear'; return; } res = {}; save(); home(); }; }
}
function quiz() {
  const c = queue[qi]; ans = [null, null, null]; shown = false;
  const draw = () => {
    app.innerHTML = `<div class="quiz"><div class="kick">${esc(c.p)} · chapter ${qi + 1} of ${queue.length}</div><div class="bar"><i style="width:${100 * qi / queue.length}%"></i></div>` +
     `<h2>${esc(c.k)} · ${esc(c.t)}</h2>` +
     c.q.map(([q, o, a], i) => `<div class="q">${i + 1}. ${esc(q)}</div><div class="opts">` + o.map((t, j) => {
        let cls = 'opt'; if (shown) { if (j === a) cls += ' right'; else if (ans[i] === j) cls += ' wrong'; }
        return `<button class="${cls}" data-i="${i}" data-j="${j}" aria-pressed="${ans[i] === j}" ${shown ? 'disabled' : ''}><span class="l">${L[j]}</span><span>${esc(t)}</span></button>`; }).join('') +
        `<button class="opt" data-i="${i}" data-j="-1" aria-pressed="${ans[i] === -1}" ${shown ? 'disabled' : ''}><span class="l">?</span><span>I don’t know</span></button></div>`).join('') +
     (shown ? verdict() : '') +
     `<div class="row"><button class="btn ghost" id="quit">Back to my map</button><button class="btn" id="nx" ${ans.includes(null) ? 'disabled' : ''}>${shown ? (qi + 1 < queue.length ? 'Next chapter' : 'See my map') : 'Mark it'}</button></div></div>`;
    app.querySelectorAll('.opt[data-i]').forEach(b => b.onclick = () => { ans[+b.dataset.i] = +b.dataset.j; draw(); });
    document.getElementById('quit').onclick = home;
    document.getElementById('nx').onclick = () => { if (!shown) { res[c.k] = c.q.filter(([q, o, a], i) => ans[i] === a).length; save(); shown = true; draw(); } else { qi++; qi < queue.length ? quiz() : home(); } };
  };
  const verdict = () => { const s = res[c.k]; const [bg, t] = s === 3 ? ['var(--goodbg)', 'Skip it: you know this chapter.'] : s === 2 ? ['var(--midbg)', `Skim it: read the Examples on p. ${c.pg}.`] : ['var(--badbg)', `Study it: start reading at p. ${c.pg}.`];
    return `<div class="verdict" style="background:${bg}">${s} of 3 right. ${t}</div>`; };
  draw(); window.scrollTo(0, 0);
}
home();
</script>'''
open('/tmp/claude-0/-home-claude/52a2d1ee-1a91-5ee7-bfb7-a2b3df8fcebc/scratchpad/check/handbook-check.html', 'w').write(page.replace('__DATA__', data))
open('/tmp/claude-0/pk/handbook-check-online.html', 'w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">' + page.replace('__DATA__', data).replace('<title>', '<title>', 1) + '</html>')
print('ok online')
