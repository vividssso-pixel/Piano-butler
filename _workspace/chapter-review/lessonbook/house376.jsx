// ─── Phase 377: the Piano Butler's House, the chapter map (Sohyun 2026-10-08: "the whole dollhouse") ───
// Every floor is a stage, every room is a chapter, in the map's order from the front door to the attic. The siblings
// stand on the stairs of the floor you are on; your room is tinted coral; a finished room has its number filled in.
// Drawn in the Lesson Book's pen and ink (pen376.js). Two drawings of the same house: phones get a tall house with
// the rooms of a floor in rows of up to three; wider screens get one row of rooms per floor and the butler outside.
const HOUSE_ICONS = __HOUSE_ICONS__;   // the room pictures from the house design (48 x 34 each), by chapter number
const HOUSE_STAND = { hip: [64, 104], neck: [64, 63], head: [65, 49], arms: [[[66, 66], [69, 86], [68, 104]], [[62, 66], [58, 86], [59, 104]]], legs: [[[66, 104], [67, 131], [68, 157]], [[62, 104], [60, 131], [58, 157]]] };
function houseWrap(text, maxW, size) {
  const words = text.split(' '), lines = []; let cur = '';
  words.forEach(w => { const nx = cur ? cur + ' ' + w : w; if (cur && rdWidth(nx, 700, size) > maxW) { lines.push(cur); cur = w; } else cur = nx; });
  if (cur) lines.push(cur);
  return lines.slice(0, 2);
}
function houseStairs(x, y, w, h, right, railTop = 2) {
  const n = Math.max(5, Math.round(h / 12)), sw = (w - 8) / n, sh = (h - 4) / n, pts = [];
  for (let k = 0; k < n; k++) { const sx = 4 + k * sw, sy = h - k * sh; pts.push([sx, sy], [sx, sy - sh], [sx + sw, sy - sh]); }
  const P = pts.map(([a, b]) => [right ? x + a : x + w - a, y + b]);
  return [{ k: 'pl', p: P, s: PEN_N, w: 1.8 },
    penLine([right ? x + 3 : x + w - 3, y + h - 24], [right ? x + w - 6 : x + 6, y + railTop], 1.2)];
}
function houseShapes(view, wide) {
  const { stages, here, nums } = view;
  const s = [], W = wide ? 900 : 360, X0 = wide ? 132 : 6, HW = wide ? 760 : 348, SC = wide ? 118 : 42;
  const LH = wide ? 0 : 20, RH = wide ? 92 : 70, SLAB = 6, TOP = wide ? 112 : 92;
  const floors = stages.map(st => {
    const n = st.ids.length, cols = wide ? n : n <= 3 ? n : n === 4 ? 2 : 3, rows = Math.ceil(n / cols);
    return { ...st, n, cols, rows, h: LH + rows * RH + SLAB };
  });
  // the roof: tiles, a plaque with the bow tie, two round windows, a chimney and a curl of smoke
  const rx0 = X0, rx1 = X0 + HW, ry = TOP, peak = wide ? 86 : 64;
  s.push({ k: 'rc', x: rx1 - (wide ? 120 : 52), y: ry - peak - 26, w: wide ? 30 : 20, h: wide ? 56 : 40, rx: 0, f: 'H@0.8', s: PEN_N, sw: 2.2 });
  s.push({ k: 'pa', seg: [['M', [rx1 - (wide ? 104 : 42), ry - peak - 30]], ['Q', [rx1 - (wide ? 116 : 52), ry - peak - 40], [rx1 - (wide ? 104 : 42), ry - peak - 50]], ['Q', [rx1 - (wide ? 94 : 34), ry - peak - 60], [rx1 - (wide ? 102 : 40), ry - peak - 70]]], f: 'none', s: PEN_N, w: 1.5 });
  s.push({ k: 'pa', seg: [['M', [rx0, ry]], ['L', [rx0 + (wide ? 70 : 34), ry - peak]], ['L', [rx1 - (wide ? 70 : 34), ry - peak]], ['L', [rx1, ry]], ['Z']], f: 'H', s: PEN_N, w: 2.8 });
  const cx = (rx0 + rx1) / 2, pw = wide ? 250 : 170, ph = wide ? 56 : 44;
  s.push({ k: 'rc', x: cx - pw / 2, y: ry - peak + (wide ? 12 : 8), w: pw, h: ph, rx: 9, f: PEN_P, s: PEN_N, sw: 2.2 });
  const by = ry - peak + (wide ? 24 : 18);
  s.push({ k: 'pa', seg: [['M', [cx - 15, by - 6]], ['L', [cx - 2, by]], ['L', [cx - 15, by + 6]], ['Z'], ['M', [cx + 15, by - 6]], ['L', [cx + 2, by]], ['L', [cx + 15, by + 6]], ['Z']], f: 'none', s: PEN_N, w: 1.8 },
    { k: 'el', c: [cx, by], rx: 2.8, ry: 2.8, f: PEN_C });
  s.push({ ...penText(cx, by + (wide ? 27 : 21), 'Piano Butler', { size: wide ? 24 : 17, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }) });
  if (wide) [cx - 230, cx + 230].forEach(wx => s.push({ k: 'el', c: [wx, ry - 40], rx: 15, ry: 15, f: PEN_P, s: PEN_N, w: 2.2 }, penLine([wx - 15, ry - 40], [wx + 15, ry - 40], 1.3), penLine([wx, ry - 55], [wx, ry - 25], 1.3)));
  // the floors, top (stage 7) to bottom (stage 1)
  let y = TOP; const rooms = []; let kidsAt = null;
  [...floors].reverse().forEach(fl => {
    const fy = y, right = (fl.i + 1) % 2 === 1;
    s.push({ k: 'g', floor: fl.i, kids: [
      { k: 'rc', x: X0, y: fy, w: HW, h: fl.h, rx: 0, f: PEN_P, s: PEN_N, sw: 2.6 },
      { k: 'rc', x: X0, y: fy + fl.h - SLAB, w: HW, h: SLAB, rx: 0, f: 'H@0.7', s: PEN_N, sw: 1.4 },
      penLine([X0 + SC, fy], [X0 + SC, fy + fl.h - SLAB], 2),
      ...houseStairs(X0, fy + LH, SC, fl.h - SLAB - LH, right, wide ? 26 : 2)] });
    const label = (fl.i + 1) + ' · ' + t(fl.s.en[0], fl.s.ko[0]);
    if (wide) s.push(penText(right ? X0 + 8 : X0 + SC - 8, fy + 16, label, { size: 12.5, weight: 800, fill: PEN_N, anchor: right ? 'start' : 'end', serif: true, halo: true }));
    else { s.push(penLine([X0 + SC, fy + LH], [X0 + HW, fy + LH], 1.2), penText(X0 + SC + 8, fy + 14, label, { size: 12, weight: 800, fill: PEN_N, serif: true })); }
    if (fl.ids.includes(here)) kidsAt = { x: X0, y: fy + LH, w: SC, h: fl.h - SLAB - LH, right };
    // the rooms of this floor, in rows
    const RA = HW - SC;
    fl.ids.forEach((id, j) => {
      const row = Math.floor(j / fl.cols), inRow = Math.min(fl.cols, fl.n - row * fl.cols), col = j - row * fl.cols, rw = RA / inRow;
      const rx = X0 + SC + col * rw, ry2 = fy + LH + row * RH;
      rooms.push({ id, rx, ry: ry2, rw, rh: RH, st: fl.st[j], on: id === here, num: nums[id] });
      if (col > 0) s.push(penLine([rx, ry2], [rx, ry2 + RH], 1.8));
      if (row > 0 && col === 0) s.push(penLine([X0 + SC, ry2], [X0 + HW, ry2], 1.2));
    });
    y += fl.h;
  });
  // the rooms' insides (in chapter order, so the buttons are met 1 to 25)
  rooms.sort((a, b) => a.num - b.num).forEach(r => {
    const { rx, ry, rw, rh, st, on, num } = r, done = st === 'done';
    if (on) s.push({ k: 'rc', x: rx + 2, y: ry + 2, w: rw - 4, h: rh - 4, rx: 0, f: '#fde9e1' });
    const ncx = rx + (wide ? 16 : 13), ncy = ry + (wide ? 20 : 14), nr = wide ? 10 : 9;
    s.push({ k: 'el', c: [ncx, ncy], rx: nr, ry: nr, f: done ? PEN_N : PEN_P, s: on ? PEN_C : PEN_N, w: 1.8 });
    s.push(penText(ncx, ncy + 4, String(num), { size: wide ? 12 : 11, weight: 800, fill: done ? '#fff' : on ? PEN_C : PEN_N, anchor: 'middle', serif: true }));
    if (st === 'started' && !on) s.push({ k: 'el', c: [ncx + nr - 1, ncy - nr + 1], rx: 3, ry: 3, f: PEN_C });
    const nm = CH_SHORT[r.id] || [(DRILLS.find(d => d.id === r.id) || {}).label || r.id, ''];
    const name = (done ? '✓ ' : '') + t(nm[0], nm[1] || nm[0]);
    const tx = ncx + nr + 5, lines = houseWrap(name, rw - (tx - rx) - 4, wide ? 12.5 : 11.5);
    lines.forEach((ln, li) => s.push(penText(tx, ncy + 4 + li * (wide ? 15 : 13), ln, { size: wide ? 12.5 : 11.5, weight: on || done ? 800 : 600, fill: on ? PEN_C : st === 'new' ? '#7f82a8' : PEN_N })));
    const ic = HOUSE_ICONS[num], k = wide ? 1.05 : 0.72, iw = 48 * k, ih = 34 * k;
    if (ic) s.push({ k: 'raw', svg: '<g transform="translate(' + pFix(rx + rw / 2 - iw / 2) + ' ' + pFix(ry + rh - ih - (wide ? 8 : 5)) + ') scale(' + k + ')" fill="none" stroke="#26296b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="' + (st === 'new' && !on ? 0.55 : 1) + '">' + ic + '</g>' });
    if (on && wide) s.push(penText(rx + rw - 8, ry + rh - 8, t('you are here', '지금 여기'), { size: 11, weight: 700, fill: PEN_C, anchor: 'end', serif: true, italic: true }));
    // the room as a button (the house is drawn as markup, so the page listens for taps on [data-chapter])
    s.push({ k: 'raw', svg: '<g data-chapter="' + r.id + '" data-status="' + st + '" data-here="' + (on ? '1' : '0') + '" role="button" tabindex="0" aria-label="' + penEsc(num + '. ' + t(nm[0], nm[1] || nm[0])) + (done ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '') + '" style="cursor:pointer"><rect x="' + pFix(rx + 1) + '" y="' + pFix(ry + 1) + '" width="' + pFix(rw - 2) + '" height="' + pFix(rh - 2) + '" fill="transparent"/></g>' });
  });
  // the siblings on the stairs of your floor
  if (kidsAt) {
    const k = wide ? 0.4 : 0.36, { x, y: ky, w, h, right } = kidsAt, foot = (f) => [right ? x + 8 + f * (w - 22) : x + w - 8 - f * (w - 22), ky + h - f * (h - 8)];
    const a = foot(0.18), b = foot(0.5);
    s.push({ k: 'g', testid: 'map-figure', kids: [...penPlace(penKid(HOUSE_STAND, right ? 1 : -1, 'boy'), k, [64, 157], [a[0], a[1] - 1]), ...penPlace(penKid(HOUSE_STAND, right ? 1 : -1, 'girl'), k, [64, 157], [b[0], b[1] - 1])] });
  }
  // the ground, and the butler at the front door
  const gy = y + 2;
  s.push(penLine([4, gy], [W - 4, gy], 1.8));
  for (let gx = 10; gx < W - 10; gx += 23) s.push({ k: 'pa', seg: [['M', [gx, gy]], ['L', [gx + 2, gy - 6]], ['M', [gx + 4, gy]], ['L', [gx + 3, gy - 5]]], f: 'none', s: PEN_N, w: 0.9 });
  const rab = (PB_ART.rabbit || '').replace(/^<svg[^>]*>|<\/svg>$/g, '');
  if (wide) s.push({ k: 'raw', svg: '<g transform="translate(4 ' + pFix(gy - 210 * 0.6) + ') scale(0.6)">' + rab + '</g>' },
    penText(58, gy + 18, t('Your butler', '버틀러가'), { size: 11.5, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }),
    penText(58, gy + 32, t('opens the door', '문을 열어 줘요'), { size: 11.5, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }));
  else s.push({ k: 'raw', svg: '<g transform="translate(8 ' + pFix(gy + 4) + ') scale(0.34)">' + rab + '</g>' },
    penText(70, gy + 34, t('Your butler opens the door.', '버틀러가 문을 열어 줘요.'), { size: 12, weight: 700, fill: PEN_N, serif: true, italic: true }),
    penText(70, gy + 50, t('Climb the stairs, one room at a time.', '한 방씩, 계단을 올라가요.'), { size: 12, weight: 700, fill: PEN_N, serif: true, italic: true }));
  return { shapes: s, W, H: wide ? gy + 40 : gy + 80 };
}
function HouseMap({ onOpen, compact, noIntro }) {
  const box = useRef(null);
  const [wide, setWide] = useState(() => { try { return window.innerWidth >= 1000; } catch (e) { return false; } });
  const [, setFontTick] = useState(0);
  useEffect(() => { try { document.fonts && document.fonts.ready.then(() => { rdCtx = null; setFontTick(n => n + 1); }); } catch (e) {} }, []);
  useEffect(() => {
    const el = box.current; if (!el) return;
    const f = () => setWide(el.clientWidth >= 820); f();
    let ro = null; try { ro = new ResizeObserver(f); ro.observe(el); } catch (e) { window.addEventListener('resize', f); }
    return () => { try { ro && ro.disconnect(); } catch (e) {} window.removeEventListener('resize', f); };
  }, []);
  const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(id => chapterState(id).status) }; });
  const all = stages.flatMap(x => x.ids), nums = {}; all.forEach((id, k) => { nums[id] = k + 1; });
  const finished = stages.reduce((a, x) => a + x.st.filter(v => v === 'done').length, 0);
  let last = null; try { last = localStorage.getItem(LAST_CHAPTER_KEY); } catch (e) {}
  const here = last && all.includes(last) && chapterState(last).status !== 'done' ? last : all.find(id => chapterState(id).status !== 'done');
  const sig = stages.map(x => x.st.join(',')).join('|') + here + wide + LANG;
  const house = useMemo(() => houseShapes({ stages, here, nums }, wide), [sig]);
  const open = (e) => { const g = e.target.closest && e.target.closest('[data-chapter]'); if (g) onOpen(g.getAttribute('data-chapter')); };
  const key = (e) => { if ((e.key === 'Enter' || e.key === ' ') && e.target.getAttribute && e.target.getAttribute('data-chapter')) { e.preventDefault(); onOpen(e.target.getAttribute('data-chapter')); } };
  return (
    <div data-testid="music-map" data-layout={wide ? 'wide' : 'tall'} data-house ref={box} className={compact ? '' : 'fade-up'}>
      <style>{'[data-house] [data-chapter]:focus-visible{outline:none}[data-house] [data-chapter]:focus-visible rect{stroke:#e4572e;stroke-width:3}'}</style>
      {!compact && !noIntro && <PageIntro title={UI_TEACHER ? t('Music map', '음악 지도') : t('My music map', '나의 음악 지도')} text={t('The Piano Butler’s house: every floor is a stage, every room is a chapter. Tap a room to open it.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나. 방을 누르면 열려요.')}/>}
      <div data-testid="map-count" style={{fontSize:12.5,fontWeight:600,color:'#6d6f9c',maxWidth:wide ? 900 : 440,margin:'0 auto 4px'}}>{t(finished + ' of ' + all.length + ' chapters done', all.length + '개 챕터 중 ' + finished + '개 완료')}</div>
      <div onClick={open} onKeyDown={key} role="group" aria-label={t('The Piano Butler’s house: the chapter map', '피아노 버틀러의 집: 챕터 지도')} style={{maxWidth:wide ? 900 : 440,margin:'0 auto'}}>
        <PenArt shapes={house.shapes} vb={[0, 0, house.W, house.H]} inter/>
      </div>
    </div>
  );
}
