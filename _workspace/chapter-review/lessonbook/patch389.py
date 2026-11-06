# Phase 389 (Sohyun 2026-10-09): keyboards are drawn straight -- "pen-drawn, not wobbly"; and the songs on paper
# are only the ones the page itself teaches. Lesson Book, Workbook, the app and the guide pages move together.
# Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch389.py
import json, re, os
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b); done.append(what)

# 1. the baked Lesson Book drawings with keyboards (30 of 48), rebaked with straight keys (chars5/handside/chars8)
art = json.load(open(os.path.join(here, '..', 'art', 'art389.json'), encoding='utf-8'))
for k, v in art.items():
    m = re.search(r'("%s": )(".*?")(,\n|\n)' % re.escape(k), s)
    assert m, k
    s = s[:m.start(2)] + json.dumps(v, ensure_ascii=False) + s[m.end(2):]
done.append('%d baked drawings' % len(art))

# 2. the live pen engine: a shape with nw:true is drawn exactly as given (no wobble)
rep("""    if (e.k === 'raw') { out += e.svg; return; }   // already drawn (a baked book picture, a small icon): passed through as it is""",
    """    if (e.k === 'raw') { out += e.svg; return; }   // already drawn (a baked book picture, a small icon): passed through as it is
    if (e.nw) { out += penPlain(e, hatch); return; }   // keyboards: straight, no wobble (Sohyun 2026-10-09)""",
    'penBakeList nw')
# penHatch must keep the flag (it copies shapes with spread, so nw survives) -- the keyboard makers set it:
rep("""function penPiano(x = 150, y = 58, floorY = 162, keyY = 98) {
  const a = [{ k: 'rc', x, y, w: 56, h: floorY - y, rx: 2.5, f: PEN_P, s: PEN_N, sw: 2.4 }, { k: 'rc', x: x - 26, y: keyY, w: 30, h: 8.5, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 }];
  for (let i = 1; i < 4; i++) a.push(penLine([x - 26 + i * 7.5, keyY], [x - 26 + i * 7.5, keyY + 8.5], 1.2));
  return a;
}""",
"""function penPiano(x = 150, y = 58, floorY = 162, keyY = 98) {
  const a = [{ k: 'rc', x, y, w: 56, h: floorY - y, rx: 2.5, f: PEN_P, s: PEN_N, sw: 2.4, nw: true }, { k: 'rc', x: x - 26, y: keyY, w: 30, h: 8.5, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2, nw: true }];
  for (let i = 1; i < 4; i++) a.push({ ...penLine([x - 26 + i * 7.5, keyY], [x - 26 + i * 7.5, keyY + 8.5], 1.2), nw: true });
  return a;
}""", 'penPiano straight')
rep("""function penKeyrow(x, y, n, w = 9.5, h = 10) {
  const a = [{ k: 'rc', x, y, w: n * w, h, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 }];
  for (let i = 1; i < n; i++) a.push(penLine([x + i * w, y], [x + i * w, y + h], 1.2));
  return a;
}""",
"""function penKeyrow(x, y, n, w = 9.5, h = 10) {
  const a = [{ k: 'rc', x, y, w: n * w, h, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2, nw: true }];
  for (let i = 1; i < n; i++) a.push({ ...penLine([x + i * w, y], [x + i * w, y + h], 1.2), nw: true });
  return a;
}""", 'penKeyrow straight')
rep("""  const s = [{ k: 'rc', x: 150, y: 118 + (o.press || 0), w: 134, h: 16, rx: 0, f: PEN_P, s: PEN_N, sw: 2 }, penLine([206, 118 + (o.press || 0)], [206, 134 + (o.press || 0)], 1.2),
    { k: 'pa', seg: [['M', [120, 134]], ['L', [290, 134]], ['L', [290, 148]], ['L', [120, 148]], ['Z']], f: PEN_N, s: PEN_N, w: 2 },""",
"""  const s = [{ k: 'rc', x: 150, y: 118 + (o.press || 0), w: 134, h: 16, rx: 0, f: PEN_P, s: PEN_N, sw: 2, nw: true }, { ...penLine([206, 118 + (o.press || 0)], [206, 134 + (o.press || 0)], 1.2), nw: true },
    { k: 'pa', seg: [['M', [120, 134]], ['L', [290, 134]], ['L', [290, 148]], ['L', [120, 148]], ['Z']], f: PEN_N, s: PEN_N, w: 2, nw: true },""",
    'penHandSide key straight')
# the glide's top-view keyboard
rep("""  const s = [{ k: 'rc', x: X(10), y: Y(10), w: 165, h: 33, rx: 0, f: PEN_P, s: PEN_N, sw: 2 }];
  for (let i = 1; i < 21; i++) s.push(penLine([X(10 + i * 14.3), Y(10)], [X(10 + i * 14.3), Y(70)], 1.1));
  for (let i = 0; i < 20; i++) if ([1, 2, 4, 5, 6].includes(i % 7)) s.push({ k: 'rc', x: X(10 + i * 14.3 - 4.5), y: Y(10), w: 4.95, h: 19.2, rx: 0, f: PEN_N });
  s.push({ k: 'rc', x: X(0), y: Y(70), w: 176, h: 4.4, rx: 0, f: PEN_N, solid: true });""",
"""  const s = [{ k: 'rc', x: X(10), y: Y(10), w: 165, h: 33, rx: 0, f: PEN_P, s: PEN_N, sw: 2, nw: true }];
  for (let i = 1; i < 21; i++) s.push({ ...penLine([X(10 + i * 14.3), Y(10)], [X(10 + i * 14.3), Y(70)], 1.1), nw: true });
  for (let i = 0; i < 20; i++) if ([1, 2, 4, 5, 6].includes(i % 7)) s.push({ k: 'rc', x: X(10 + i * 14.3 - 4.5), y: Y(10), w: 4.95, h: 19.2, rx: 0, f: PEN_N, nw: true });
  s.push({ k: 'rc', x: X(0), y: Y(70), w: 176, h: 4.4, rx: 0, f: PEN_N, solid: true, nw: true });""",
    'glide top keyboard straight')
# chapter 2's keyboards, roofs, brackets and arrows
rep("""  const s = [{ k: 'rc', x, y, w: nw * W, h: H, rx: 2, f: PEN_P, s: PEN_N, sw: opts.sw || 2.2 }];
  if (opts.tints) for (let i = 0; i < nw; i++) {
    const m7 = (i + off) % 7;                                   // C D E pale coral, F G A B pale navy
    s.push({ k: 'rc', x: x + i * W + 1, y: y + 2, w: W - 2, h: H - 4, rx: 1.5, f: m7 < 3 ? '#fbe9e2' : '#e9eaf4' });
  }
  for (let i = 1; i < nw; i++) s.push(penLine([x + i * W, y], [x + i * W, y + H], 1.2));
  const blacks = [];
  for (let i = 0; i < nw - 1; i++) if (hasBlackAfter(i)) { blacks.push(i); s.push({ k: 'rc', x: x + (i + 1) * W - BW / 2, y, w: BW, h: BH, rx: 1, f: PEN_N, solid: true }); }""",
"""  const s = [{ k: 'rc', x, y, w: nw * W, h: H, rx: 2, f: PEN_P, s: PEN_N, sw: opts.sw || 2.2, nw: true }];
  if (opts.tints) for (let i = 0; i < nw; i++) {
    const m7 = (i + off) % 7;                                   // C D E pale coral, F G A B pale navy
    s.push({ k: 'rc', x: x + i * W + 1, y: y + 2, w: W - 2, h: H - 4, rx: 1.5, f: m7 < 3 ? '#fbe9e2' : '#e9eaf4', nw: true });
  }
  for (let i = 1; i < nw; i++) s.push({ ...penLine([x + i * W, y], [x + i * W, y + H], 1.2), nw: true });
  const blacks = [];
  for (let i = 0; i < nw - 1; i++) if (hasBlackAfter(i)) { blacks.push(i); s.push({ k: 'rc', x: x + (i + 1) * W - BW / 2, y, w: BW, h: BH, rx: 1, f: PEN_N, solid: true, nw: true }); }""",
    'fsKeysShapes straight')
rep("""  const out = [{ k: 'pl', p: [[h.x1, baseY], [mid, baseY - peak], [h.x2, baseY]], s: col, w: opts.w || 2.6 }];""",
    """  const out = [{ k: 'pl', p: [[h.x1, baseY], [mid, baseY - peak], [h.x2, baseY]], s: col, w: opts.w || 2.6, nw: true }];""",
    'fsRoof straight')
rep("""    { k: 'pa', seg: [['M', [x1, y]], ['L', [x1, y + 5]], ['L', [x2, y + 5]], ['L', [x2, y]]], f: 'none', s: col, w: 2 },""",
    """    { k: 'pa', seg: [['M', [x1, y]], ['L', [x1, y + 5]], ['L', [x2, y + 5]], ['L', [x2, y]]], f: 'none', s: col, w: 2, nw: true },""",
    'fsBrace straight')
rep("""    s.push({ k: 'pa', seg: [['M', [60, 76]], ['L', [290, 76]]], f: 'none', s: PEN_C, w: 2 });""",
    """    s.push({ k: 'pa', seg: [['M', [60, 76]], ['L', [290, 76]]], f: 'none', s: PEN_C, w: 2, nw: true });""",
    'street arrow straight')

# 3. songs on paper = the songs the page teaches (Hot Cross Buns is written in the book; the others live in the app)
rep("""<b>Mary Had a Little Lamb</b>{t(' (떴다 떴다 비행기)', ' (떴다 떴다 비행기)')}, <b>Old MacDonald</b>, <b>Rain Rain Go Away</b>. {t('All famous, all free to use -- the finger rows are in the app and the Workbook.', '모두 유명하고 저작권 걱정 없는 곡이에요 -- 손가락 번호 악보는 앱과 워크북에 있어요.')}""",
    """<b>Mary Had a Little Lamb</b>{t(' (떴다 떴다 비행기)', ' (떴다 떴다 비행기)')}, <b>Old MacDonald</b>, <b>Rain Rain Go Away</b>. {t('All famous, all free to use -- play them with their finger numbers in the online lesson.', '모두 유명하고 저작권 걱정 없는 곡이에요 -- 손가락 번호와 함께 온라인 레슨에서 쳐 봐요.')}""",
    'book: more tunes live in the online lesson')
rep("""<b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('More tunes that live on the black keys', '검은건반에 사는 다른 노래들')}</b>""",
    """<b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('More tunes in the online lesson', '온라인 레슨에서 더 치기')}</b>""",
    'book: box title')
rep("""      <div style={{marginTop:8}}><PhLog rows={['Hot Cross Buns', 'Mary Had a Little Lamb', 'Old MacDonald', 'Rain Rain Go Away', 'Echo game with someone at home']} label={190}/></div>""",
    """      <div style={{marginTop:8}}><PhLog rows={['Hot Cross Buns, right hand', 'Hot Cross Buns, one big roof higher', 'Echo game with someone at home', 'My own black-key tune']} label={190}/></div>""",
    'workbook: practise only what the page teaches')
s = s.replace("""<Part kind="home" title="Hot Cross Buns" how="The song in finger numbers. Fill in the missing numbers, then tick each tune you play this week.">""",
              """<Part kind="home" title="Hot Cross Buns" how="The song in finger numbers. Fill in the missing numbers, then tick each one you do this week.">"""); done.append('workbook wording')

open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 389 DONE')
