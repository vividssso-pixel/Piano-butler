// ─── Phase 467: chapter 10 (Dynamics & Articulation): the Lesson Book, built in full under Book rules 14 and 15 (her
// 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게': chapters built back to back, her final review of several at once).
// The level plan's scope for room 10 (Level 2): pp p mf f, getting louder and softer; staccato, and the sign for the
// legato they already play (AMEB Preliminary: pp p mf f, staccato, legato; Grade 1: mp ff, cresc., decresc.; mp and
// ff are the drill's extra level). Book rule 13: the slur, legato's sign, comes here, set beside chapter 8's tie: the
// same curve; on the same note a tie, on different notes a slur. Every tune is new and right hand in C position
// (chapter 9).

// the marks a tune carries, drawn over sskRaw's notes. k: dyn [[note, 'p']] and hair [[from, to, 'cresc' | 'dim']] on a
// row under the staff, each sign centred under its note (dynBox [note]: an empty box there to write a sign or a number
// in; hairBox [[from, to]]: a dashed space to draw a hairpin in; dynOk / hairOk: the revealed answers, green); stacc
// [notes] (the dot on the side away from the stem; inside the staff, in a space); slurs and ties [[from, to]] (a curve
// on the side away from the stems: a slur's ends centred on the heads, a tie's between them; never along a staff line);
// sound (each note's sound line, as long as it sounds: a staccato note's short, the others reaching the next note; a
// tie one line; lit: the one sounding now, the others pale). rowGap: the room above the row of signs. Returns the raw
// SVG, its top and bottom, and where the curves and dots are (for words beside them).
const SDY_FONT = "Georgia, 'Times New Roman', serif";
const SDY_HW = { pp: 11, p: 6, mp: 12, mf: 12, f: 5, ff: 9 };   // half the width of each sign as drawn (22 px)
const sdyDm = (s, size) => <span style={{fontFamily:SDY_FONT,fontStyle:'italic',fontWeight:900,fontSize:size,letterSpacing:'-0.01em'}}>{s}</span>;
// running text with its dynamics set as signs (bold italic)
const sdyRich = (str, size = '1.1em') => { const out = []; let last = 0; const re = /(^|[^A-Za-z.])(pp|mp|mf|ff|p|f)(?![A-Za-z])/g; let m;
  while ((m = re.exec(str))) { const at = m.index + m[1].length; out.push(str.slice(last, at), <React.Fragment key={at}>{sdyDm(m[2], size)}</React.Fragment>); last = at + m[2].length; }
  out.push(str.slice(last)); return out; };
function sdyMarks(yOf, items, m, k = {}, clef = 'treble') {
  const low = CLEFS[clef].low, high = CLEFS[clef].high, yTop = yOf(high), yBot = yOf(low), col = PEN_N, cor = PEN_C, ok = PEN_G;
  const lines = []; for (let yy = yTop; yy <= yBot + 0.01; yy += 10) lines.push(yy);
  const onLine = (y) => lines.some(L => Math.abs(L - y) < 0.6);
  const ns = m.notes, out = [], curves = [], dots = [];
  let top = m.top, bottom = m.bottom;
  // staccato: centred on the head, on the side away from the stem; inside the staff, in a space
  (k.stacc || []).forEach(j => { const n = ns[j]; if (!n) return;
    const s = n.up ? 1 : -1, want = n.y + s * 9.5;
    let y = want;
    if (want > yTop - 4 && want < yBot + 4) { const cands = []; for (let yy = yTop - 5; yy <= yBot + 5.01; yy += 10) cands.push(yy);
      y = s > 0 ? cands.find(c => c >= want - 0.5) : cands.slice().reverse().find(c => c <= want + 0.5); }
    out.push('<circle cx="' + pFix(n.x) + '" cy="' + pFix(y) + '" r="2.1" fill="' + (k.stacCol || col) + '"/>'); dots.push({ x: n.x, y });
    if (s > 0) bottom = Math.max(bottom, y + 4); else top = Math.min(top, y - 4); });
  // a curve from note a to note b, under the heads when every stem goes up (all of this book's tunes), else over
  const curve = (a, b, tie) => { const A = ns[a], B = ns[b]; if (!A || !B) return;
    const span = ns.slice(a, b + 1), c = k.curveCol || col;
    if (span.every(n => n.up)) {
      // an end clear of the head; a line note's end goes into the space below it, a space note's below the next line
      // a tie between two line notes inside the staff stays flat in the space below them; any other end goes clear of
      // its head (a semibreve's a little more) and never along a line: a line note's slur end goes under the next line
      const inside = tie && onLine(A.y) && A.y < yBot - 1;
      const end = (n) => { const y = n.y + 8.5 + (n.end === n.y ? 1.5 : 0); if (y < yTop - 2 || y > yBot + 2.5) return y;
        const near = lines.find(L => Math.abs(L - y) < 2.5); if (near == null) return y; return onLine(n.y) ? n.y + 12.5 : near + 3; };
      const y1 = inside ? A.y + 6.5 : end(A), y2 = inside ? B.y + 6.5 : end(B);
      let apex = inside ? A.y + 7.9 : Math.max(y1, y2, ...span.slice(1, -1).map(n => n.y + 8.5)) + (tie ? 4.5 : Math.min(9, 3 + 1.5 * (b - a)));
      if (!inside && apex > yTop && apex < yBot + 2 && lines.some(L => Math.abs(L - apex) < 1.6)) apex += 2.2;
      const x1 = inside ? A.x + 5.5 : tie ? A.x + 4 : A.x, x2 = inside ? B.x - 5.5 : tie ? B.x - 4 : B.x, cy = 2 * apex - (y1 + y2) / 2;
      out.push('<path d="M' + pFix(x1) + ' ' + pFix(y1) + ' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(cy) + ' ' + pFix(x2) + ' ' + pFix(y2) + '" fill="none" stroke="' + c + '" stroke-width="' + (inside ? 1.6 : 1.9) + '" stroke-linecap="round"/>');
      curves.push({ a, b, x: (x1 + x2) / 2, y: apex, under: true }); bottom = Math.max(bottom, apex + 2);
    } else {
      const tp = (n) => n.up ? n.end - 4 : n.y - 8.5, y1 = tp(A), y2 = tp(B), apex = Math.min(...span.map(tp)) - (tie ? 4.5 : Math.min(9, 3 + 1.5 * (b - a)));
      const x1 = A.x + (A.up ? 6.4 : tie ? 4 : 0), x2 = B.x + (B.up ? 6.4 : tie ? -4 : 0), cy = 2 * apex - (y1 + y2) / 2;
      out.push('<path d="M' + pFix(x1) + ' ' + pFix(y1) + ' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(cy) + ' ' + pFix(x2) + ' ' + pFix(y2) + '" fill="none" stroke="' + c + '" stroke-width="1.9" stroke-linecap="round"/>');
      curves.push({ a, b, x: (x1 + x2) / 2, y: apex, under: false }); top = Math.min(top, apex - 2);
    } };
  (k.slurs || []).forEach(([a, b]) => curve(a, b, false));
  (k.ties || []).forEach(([a, b]) => curve(a, b, true));
  // the row under the staff: dynamics and hairpins (and boxes to write them in)
  const dynB = k.dynBox || [], dyn = k.dyn || [], hasRow = dyn.length || (k.hair && k.hair.length) || dynB.length || (k.hairBox && k.hairBox.length);
  let ry = null;
  if (hasRow) {
    ry = Math.max(yBot + 34, bottom + (k.rowGap || 26));
    const at = (j) => ns[j] ? ns[j].x : 0, dc = k.dynCol || col, dynAt = (j) => dyn.find(([i]) => i === j);
    dyn.forEach(([j, s]) => out.push('<text x="' + pFix(at(j)) + '" y="' + pFix(ry) + '" text-anchor="middle" style="font-family:' + SDY_FONT + ';font-style:italic;font-weight:900;font-size:22px" fill="' + ((k.dynOk || []).includes(j) ? ok : dc) + '">' + s + '</text>'));
    dynB.forEach(j => out.push('<rect x="' + pFix(at(j) - 18) + '" y="' + pFix(ry - 23) + '" width="36" height="31" rx="3" fill="#fff" stroke="rgba(38,41,107,0.55)" stroke-width="1.3"/>'));
    const left = (j) => dynB.includes(j) ? at(j) + 18 + 4 : dynAt(j) ? at(j) + SDY_HW[dynAt(j)[1]] + 5 : at(j) - 4;
    const right = (b) => { const nx = b + 1, lim = dynB.includes(nx) ? at(nx) - 18 - 4 : dynAt(nx) ? at(nx) - SDY_HW[dynAt(nx)[1]] - 6 : Infinity; return Math.min(at(b) + 12, lim); };
    (k.hair || []).forEach(([a, b, dir]) => { const x1 = left(a), x2 = right(b), yc = ry - 7, h = 6.5, c = (k.hairOk || []).includes(a) ? ok : dc;
      out.push(dir === 'cresc' ? '<polyline points="' + pFix(x2) + ',' + pFix(yc - h) + ' ' + pFix(x1) + ',' + pFix(yc) + ' ' + pFix(x2) + ',' + pFix(yc + h) + '" fill="none" stroke="' + c + '" stroke-width="1.8" stroke-linejoin="round"/>'
        : '<polyline points="' + pFix(x1) + ',' + pFix(yc - h) + ' ' + pFix(x2) + ',' + pFix(yc) + ' ' + pFix(x1) + ',' + pFix(yc + h) + '" fill="none" stroke="' + c + '" stroke-width="1.8" stroke-linejoin="round"/>'); });
    (k.hairBox || []).forEach(([a, b]) => { const x1 = left(a), x2 = right(b); out.push('<rect x="' + pFix(x1 - 2) + '" y="' + pFix(ry - 20) + '" width="' + pFix(x2 - x1 + 4) + '" height="26" rx="3" fill="none" stroke="rgba(38,41,107,0.55)" stroke-width="1.2" stroke-dasharray="4 3"/>'); });
    bottom = ry + 9;
  }
  // sound lines: each note's sound, as long as it lasts; a note held into the next one reaches it
  if (k.sound) {
    const beats = sskNotesOf(items).map(x => x.b), D = k.D || 34, sy = Math.max(yBot + 20, bottom + 14), st = new Set(k.stacc || []);
    const tiedTo = new Set((k.ties || []).map(([, b]) => b)), tieEnd = {}; (k.ties || []).forEach(([a, b]) => { tieEnd[a] = b; });
    const endX = (j) => j + 1 < ns.length ? ns[j + 1].x - 1.5 : ns[j].x + beats[j] * D - 8;
    const playing = k.lit != null && k.lit >= 0;
    ns.forEach((n, j) => { if (tiedTo.has(j)) return;
      const w = st.has(j) ? Math.min(beats[j], 1) * D * 0.3 : endX(tieEnd[j] != null ? tieEnd[j] : j) - n.x;
      out.push('<rect x="' + pFix(n.x - 5) + '" y="' + pFix(sy - 3) + '" width="' + pFix(Math.max(7, w)) + '" height="6" rx="3" fill="' + (!playing || k.lit === j ? cor : '#f6cdbf') + '"/>'); });
    bottom = sy + 7;
  }
  return { raw: out.join(''), top, bottom, curves, dots, ry };
}
// a tune with its marks on one staff (o: sskRaw's options; k: the marks); extra(yOf, txt, notes, marks)
function SdyStaff({ items, clef = 'treble', width = 400, o = {}, k = {}, label, extra, full, pad, room = 0 }) {   // room: more space above, for a word
  const oo = { ...o, clef }, kk = { ...k, D: o.D }, m = sskRaw((d) => dY(d), items, oo), mk = sdyMarks((d) => dY(d), items, m, kk, clef), vbw = Math.ceil(m.last + 6);
  const hi = dY(CLEFS[clef].high), lo = dY(CLEFS[clef].low);
  const p = pad || [Math.max(12, hi - mk.top + 6) + room, Math.max(12, mk.bottom - lo + 6)];
  return <div style={{width:full ? '100%' : Math.min(100, vbw / width * 100) + '%'}}><SfStaff clef={clef} width={vbw} span={[4, m.last]} pad={p} label={label}
    extra={(yOf, layer, txt) => { if (layer !== 'over') return null; const y2 = (d) => yOf(d, clef), mm = sskRaw(y2, items, oo), mk2 = sdyMarks(y2, items, mm, kk, clef);
      return <g><g dangerouslySetInnerHTML={{ __html: mm.raw + mk2.raw }}/>{extra && extra(yOf, txt, mm, mk2)}</g>; }}/></div>;
}
const sdyVbw = (items, o, clef = 'treble') => Math.ceil(sskRaw((d) => dY(d), items, { ...o, clef }).last + 6);
// tunes in systems, one scale
function SdySystems({ rows, clef = 'treble', os = [], ks = [], labels = [], extras = [], gap = 8 }) {
  const w = Math.max(...rows.map((r, i) => sdyVbw(r, os[i] || {}, clef)));
  return <div style={{display:'flex',flexDirection:'column',gap,width:'100%'}}>{rows.map((r, i) => <SdyStaff key={i} width={w} clef={clef} items={r} o={os[i] || {}} k={ks[i] || {}} label={labels[i]} extra={extras[i]} room={extras[i] ? 16 : 0}/>)}</div>;
}

// the book's tunes (right hand, C position, none of them a song), shared with the screen and the Workbook
const SDY_ROWS = {
  open: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['|'], ['q', 1, 32], ['q', 1, 30], ['h', 2, 28], ['||']],
  pf: [['ts', 4], ['q', 1, 28], ['q', 1, 30], ['q', 1, 29], ['q', 1, 31], ['|'], ['q', 1, 30], ['q', 1, 29], ['h', 2, 28], ['||']],
  four: [['ts', 3], ['q', 1, 28], ['q', 1, 30], ['q', 1, 32], ['|'], ['q', 1, 28], ['q', 1, 30], ['q', 1, 32], ['|'], ['q', 1, 28], ['q', 1, 30], ['q', 1, 32], ['|'], ['q', 1, 28], ['q', 1, 30], ['q', 1, 32], ['||']],
  hair: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['|'], ['w', 4, 32], ['|'], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['q', 1, 29], ['|'], ['w', 4, 28], ['||']],
  touch: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['|'], ['w', 4, 32], ['||']],
  slur: [['ts', 4], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['q', 1, 29], ['|'], ['w', 4, 28], ['||']],
  tie: [['ts', 4], ['h', 2, 30], ['h', 2, 32], ['|'], ['w', 4, 32], ['||']],
};
const SDY_MARKS = {
  open: { dyn: [[0, 'p'], [4, 'f']], hair: [[0, 3, 'cresc']], slurs: [[0, 3]], stacc: [4, 5], rowGap: 32 },
  pfp: { dyn: [[0, 'p']] }, pff: { dyn: [[0, 'f']] },
  four: { dyn: [[0, 'pp'], [3, 'p'], [6, 'mf'], [9, 'f']] },
  hair: { dyn: [[0, 'p'], [4, 'f'], [9, 'p']], hair: [[0, 3, 'cresc'], [5, 8, 'dim']] },
  leg: { slurs: [[0, 4]], sound: true }, stac: { stacc: [0, 1, 2, 3], sound: true },
  slur: { slurs: [[0, 4]], sound: true }, tie: { ties: [[1, 2]], sound: true },
};
// how loud each sign is (the drills' own levels)
const SDY_VOL = { pp: 0.05, p: 0.09, mp: 0.15, mf: 0.24, f: 0.36, ff: 0.55 };

function sdyLbPages(scr = false) {
  const ch = 'dynamics';
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const dm = (s) => sdyDm(s, '1.12em');
  const RHC = t('Right hand in C position', '오른손 C 자리');
  const tag = (s, c = BK.coral) => (yOf, txt, mm) => <text x={mm.notes[0].x - 16} y={yOf(38) - 12} textAnchor="start" fontSize="12.5" fontWeight="900" fill={c} style={txt}>{s}</text>;

  const p1 = <SdyStaff full room={4} items={SDY_ROWS.open} o={{ D: 34 }} k={SDY_MARKS.open}
    label={t('Two bars of 4/4. C D E F with a slur, p, getting louder; then G E staccato and a minim C, f.', '4/4 두 마디. 이음줄로 이은 C D E F, p, 점점 세게; 그다음 스타카토 G E와 2분음표 C, f.')}
    extra={(yOf, txt, mm, mk) => { const sl = mk.curves[0], d = mk.dots;
      return <g style={txt}><text x={sl.x} y={sl.y + 13} textAnchor="middle" fontSize="12" fontWeight="900" fill={BK.coral}>{t('slur', '이음줄')}</text>
        <text x={(d[0].x + d[1].x) / 2} y={Math.max(d[0].y, d[1].y) + 14} textAnchor="middle" fontSize="12" fontWeight="900" fill={BK.coral}>{t('staccato', '스타카토')}</text></g>; }}/>;
  const p2 = <SdySystems rows={[SDY_ROWS.pf, SDY_ROWS.pf]} os={[{ D: 32 }, { D: 32 }]} ks={[SDY_MARKS.pfp, SDY_MARKS.pff]} gap={4}
    labels={[t('A tune in 4/4, C E D F, E D C, marked p: soft.', '4/4 선율 C E D F, E D C, p: 여리게.'), t('The same tune marked f: loud.', '같은 선율, f: 세게.')]}/>;
  const f1 = SDY_ROWS.four.slice(0, 9), f2 = SDY_ROWS.four.slice(9);   // two bars a system
  const p3 = <SdySystems rows={[f1, f2]} os={[{ D: 34 }, { D: 34 }]} ks={[{ dyn: [[0, 'pp'], [3, 'p']] }, { dyn: [[0, 'mf'], [3, 'f']] }]} gap={4}
    labels={[t('Bars 1 and 2 of 3/4, each C E G: the first pp, the second p.', '3/4의 1~2마디, 마디마다 C E G: 첫 마디 pp, 둘째 마디 p.'), t('Bars 3 and 4: the third mf, the fourth f.', '3~4마디: 셋째 마디 mf, 넷째 마디 f.')]}/>;
  const h1 = SDY_ROWS.hair.slice(0, 8), h2 = SDY_ROWS.hair.slice(8);   // two bars a system
  const p4 = <SdySystems rows={[h1, h2]} os={[{ D: 34 }, { D: 34 }]} ks={[{ dyn: [[0, 'p'], [4, 'f']], hair: [[0, 3, 'cresc']] }, { dyn: [[4, 'p']], hair: [[0, 3, 'dim']] }]} gap={4}
    labels={[t('Bar 1: C D E F from p, over a hairpin that opens. Bar 2: a semibreve G, f.', '1마디: p에서 벌어지는 헤어핀 위의 C D E F. 2마디: 온음표 G, f.'), t('Bar 3: G F E D over a hairpin that closes. Bar 4: a semibreve C, p.', '3마디: 좁아지는 헤어핀 위의 G F E D. 4마디: 온음표 C, p.')]}/>;
  const p5 = <SdySystems rows={[SDY_ROWS.touch, SDY_ROWS.touch]} os={[{ D: 32 }, { D: 32 }]} ks={[SDY_MARKS.leg, SDY_MARKS.stac]} gap={4}
    labels={[t('Legato: C D E F G with a slur. Under each note a coral sound line, each reaching the next.', '레가토: 이음줄로 이은 C D E F G. 음마다 산호색 소리 줄, 줄이 다음 줄까지 닿아요.'), t('Staccato: the same notes, a dot under C D E F. Their sound lines are short, with gaps; G, with no dot, sounds its full length.', '스타카토: 같은 음, C D E F 아래에 점. 소리 줄이 짧고 사이가 떠요; 점이 없는 G는 제 길이를 다 울려요.')]}
    extras={[tag(t('legato', '레가토')), tag(t('staccato', '스타카토'))]}/>;
  const p6 = <SdySystems rows={[SDY_ROWS.slur, SDY_ROWS.tie]} os={[{ D: 32 }, { D: 32 }]} ks={[SDY_MARKS.slur, SDY_MARKS.tie]} gap={4}
    labels={[t('A slur joining G F E D C, different notes: played legato, their sound lines touching.', '다른 음 G F E D C를 이은 이음줄: 레가토로 쳐요. 소리 줄이 서로 닿아요.'), t('A minim E, then a minim G tied to a semibreve G, the same note: one sound line for the G, six beats long.', '2분음표 E, 그다음 2분음표 G와 온음표 G를 잇는 붙임줄, 같은 음: G의 소리 줄은 하나, 여섯 박 길이.')]}
    extras={[tag(t('slur: different notes', '이음줄: 다른 음')), tag(t('tie: the same note', '붙임줄: 같은 음'))]}/>;

  // the check icons: a staff with 8 between the lines, the signs in navy, staccato dots and curves under the staff
  const STF = (() => { let s = ''; for (let i = 0; i < 5; i++) s += '<line x1="4" x2="88" y1="' + (6 + i * 8) + '" y2="' + (6 + i * 8) + '" stroke="' + PEN_N + '" stroke-width="1.1"/>'; return s; })();
  const hd = (x, y) => '<ellipse cx="' + x + '" cy="' + y + '" rx="5.4" ry="3.9" fill="' + PEN_N + '" transform="rotate(-20 ' + x + ' ' + y + ')"/><line x1="' + (x + 5) + '" x2="' + (x + 5) + '" y1="' + (y - 1) + '" y2="' + (y - 24) + '" stroke="' + PEN_N + '" stroke-width="1.4"/>';
  const dtxt = (x, s, size = 20) => '<text x="' + x + '" y="29" text-anchor="middle" style="font-family:' + SDY_FONT + ';font-style:italic;font-weight:900;font-size:' + size + 'px" fill="' + PEN_N + '">' + s + '</text>';
  const arc = (x1, y1, x2, y2, cy) => '<path d="M' + x1 + ' ' + y1 + ' Q' + ((x1 + x2) / 2) + ' ' + cy + ' ' + x2 + ' ' + y2 + '" fill="none" stroke="' + PEN_N + '" stroke-width="1.6" stroke-linecap="round"/>';
  const chkArts = {
    pf: [{ k: 'raw', svg: dtxt(30, 'p', 24) + dtxt(62, 'f', 24) }],
    four: [{ k: 'raw', svg: dtxt(14, 'pp', 15) + dtxt(36, 'p', 15) + dtxt(59, 'mf', 15) + dtxt(81, 'f', 15) }],
    hair: [{ k: 'raw', svg: '<polyline points="42,13 8,21 42,29" fill="none" stroke="' + PEN_N + '" stroke-width="2"/><polyline points="50,13 84,21 50,29" fill="none" stroke="' + PEN_N + '" stroke-width="2"/>' }],
    touch: [{ k: 'raw', svg: STF + hd(16, 38) + hd(32, 34) + arc(16, 44.5, 32, 41, 50) + hd(58, 38) + hd(74, 34) + '<circle cx="58" cy="46" r="1.8" fill="' + PEN_N + '"/><circle cx="74" cy="43" r="1.8" fill="' + PEN_N + '"/>' }],
    slur: [{ k: 'raw', svg: STF + hd(16, 38) + hd(32, 30) + arc(16, 44.5, 32, 37, 50) + hd(58, 38) + hd(76, 38) + arc(62, 44, 72, 44, 50) }],
  };
  const vbs = { pf: [0, 0, 92, 40], four: [0, 0, 92, 40], hair: [0, 0, 92, 40], touch: [0, 0, 92, 52], slur: [0, 0, 92, 52] };
  const nbKo = (s) => s.replace(/칠 수 있어요/g, '칠 수 있어요');
  const checksRows = [
    ['pf', t('I can play p and f', nbKo('p와 f로 칠 수 있어요'))],
    ['four', t('I can play pp, p, mf and f, each a little louder', nbKo('pp, p, mf, f를 조금씩 더 세게 칠 수 있어요'))],
    ['hair', t('I can get louder and softer, following the hairpins', nbKo('헤어핀을 따라 점점 세게, 점점 여리게 칠 수 있어요'))],
    ['touch', t('I can play legato and staccato', nbKo('레가토와 스타카토로 칠 수 있어요'))],
    ['slur', t('I can tell a slur from a tie, and play both', nbKo('이음줄과 붙임줄을 구별해서 칠 수 있어요'))],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Dynamics & Articulation', '다이나믹과 아티큘레이션')}</div>
      </div></LbOnly>
      {pic(p1, 220, 680)}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>셈여림</b>은 얼마나 세게 또는 여리게 칠지 알려 줘요. <b>아티큘레이션</b>은 음을 이어서 칠지 끊어서 칠지 알려 줘요.</>
        : <><b>Dynamics</b> tell you how loud or soft to play. <b>Articulation</b> tells you how to join or separate the notes.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Soft and loud', '여리게와 세게'), 2], [t('From pp to f', 'pp에서 f까지'), 3], [t('Getting louder and softer', '점점 세게, 점점 여리게'), 4], [t('Legato and staccato', '레가토와 스타카토'), 5], [t('Slur and tie', '이음줄과 붙임줄'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{sdyRich(n)}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{sdyRich(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. soft and loud
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Soft and loud', '여리게와 세게')}>
      {live(pic(p2, 250, 600), <SdyPad page={2}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['셈여림', '얼마나 세게 또는 여리게 칠지. 기호는 오선 아래에 써요. 다른 이름은 다이나믹이에요.'],
        [dm('p'), '여리게. 이탈리아어 피아노(piano)의 줄임말.'],
        [dm('f'), '세게. 이탈리아어 포르테(forte)의 줄임말.'],
      ] : [
        ['dynamics', 'How loud or soft to play. Their signs are written under the staff.'],
        [dm('p'), 'Soft. Short for piano, Italian for soft.'],
        [dm('f'), 'Loud. Short for forte, Italian for loud.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC}: 위 악보를 {dm('p')}로 쳐요. 손끝은 건반 가까이 두고, 팔은 가볍게 해요.</>,
        <>아래 악보를 {dm('f')}로 쳐요. 팔의 무게를 단단한 손끝에 실어요. 빠르기는 그대로예요.</>,
      ] : [
        <>{RHC}: play the top tune {dm('p')}, fingertips close to the keys and the arm light.</>,
        <>Play the bottom tune {dm('f')}, the arm’s weight sinking into firm fingertips. Keep the same speed.</>,
      ]}/>
      <LbRemember>{LANG === 'ko' ? <>{dm('p')} 여리게, {dm('f')} 세게.</> : <>{dm('p')} soft, {dm('f')} loud.</>}</LbRemember>
    </LbPage>,

    // 3. from pp to f
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('From pp to f', 'pp에서 f까지')}>
      {live(pic(p3, 230, 680), <SdyLadder/>)}
      <LbDefs lead={LANG === 'ko' ? <>여린 것부터 센 것까지: {dm('pp')}, {dm('p')}, {dm('mf')}, {dm('f')}.</> : <>From soft to loud: {dm('pp')}, {dm('p')}, {dm('mf')}, {dm('f')}.</>} items={LANG === 'ko' ? [
        [dm('pp'), '매우 여리게. 피아니시모(pianissimo)의 줄임말.'],
        [dm('mf'), '조금 세게. 메조포르테(mezzo forte)의 줄임말.'],
      ] : [
        [dm('pp'), 'Very soft. Short for pianissimo.'],
        [dm('mf'), 'Medium loud. Short for mezzo forte.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC}: 네 마디를 {dm('pp')}, {dm('p')}, {dm('mf')}, {dm('f')}로, 한 마디씩 조금 더 세게 쳐요.</>,
        <>한 번 더, 이번에는 {dm('f')}에서 {dm('pp')}까지, 한 마디씩 조금 더 여리게 쳐요.</>,
      ] : [
        <>{RHC}: play the four bars {dm('pp')}, {dm('p')}, {dm('mf')}, {dm('f')}, each a little louder.</>,
        <>Play them again from {dm('f')} to {dm('pp')}, each bar a little softer.</>,
      ]}/>
      <LbRemember>{t('m means medium. The same letter twice means very.', 'm은 ‘조금’, 같은 글자 두 개는 ‘매우’.')}</LbRemember>
    </LbPage>,

    // 4. getting louder and softer
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Getting louder and softer', '점점 세게, 점점 여리게')}>
      {live(pic(p4, 240, 600), <SdyPad page={4}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['헤어핀', '오선 아래에서 벌어지거나 좁아지는 두 줄.'],
        ['크레셴도', '점점 세게. 기호: 벌어지는 헤어핀. 줄임말: cresc.'],
        ['디미누엔도', '점점 여리게. 기호: 좁아지는 헤어핀. 줄임말: dim. 다른 이름: 데크레셴도(decresc.).'],
      ] : [
        ['hairpin', 'Two lines under the staff that open or close.'],
        ['crescendo', 'Getting louder, little by little. Sign: a hairpin that opens. Short form: cresc.'],
        ['diminuendo', 'Getting softer, little by little. Sign: a hairpin that closes. Short form: dim. Other name: decrescendo (decresc.).'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC}: C{' '}D{' '}E{' '}F{' '}G를 {dm('p')}에서 {dm('f')}까지 점점 세게, 그다음 G{' '}F{' '}E{' '}D{' '}C를 {dm('p')}까지 점점 여리게 쳐요.</>,
        <>위의 선율을 쳐요: 1마디는 점점 세게, 2마디는 {dm('f')}, 3마디는 점점 여리게. 빠르기는 그대로예요.</>,
      ] : [
        <>{RHC}: play C D E F G getting louder, from {dm('p')} to {dm('f')}; then G F E D C getting softer, back to {dm('p')}.</>,
        <>Play the tune above: louder through bar 1, {dm('f')} in bar 2, softer through bar 3. Keep the same speed.</>,
      ]}/>
      <LbRemember>{t('Opening: louder. Closing: softer.', '벌어지면 점점 세게, 좁아지면 점점 여리게.')}</LbRemember>
    </LbPage>,

    // 5. legato and staccato
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Legato and staccato', '레가토와 스타카토')}>
      {live(pic(p5, 270, 600), <SdyPad page={5}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['아티큘레이션', '음을 잇거나 끊어서 치는 방법.'],
        ['레가토', '부드럽게 이어서: 다음 음이 소리 날 때까지 앞 건반을 누르고 있어요. 기호는 이음줄(6쪽)이에요.'],
        ['스타카토', '짧게 끊어서: 건반을 바로 놓아요. 기호는 음표 머리 쪽, 기둥의 반대쪽에 찍는 점이에요.'],
      ] : [
        ['articulation', 'How the notes are joined or separated.'],
        ['legato', 'Smooth and joined: hold each key until the next note sounds. Its sign is a slur (page 6).'],
        ['staccato', 'Short: let go of each key straight away. Its sign is a dot by the note head, on the side away from the stem.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC}: C{' '}D{' '}E{' '}F{' '}G를 레가토로 쳐요. 다음 손가락이 내려갈 때 앞 손가락이 올라와요.</>,
        <>한 번 더 쳐요. C{' '}D{' '}E{' '}F는 스타카토로, 손목에서 가볍게 튀어 올라요. G는 네 박 다 눌러요.</>,
      ] : [
        <>{RHC}: play C D E F G legato. Each finger comes up as the next goes down.</>,
        <>Play it again, C D E F staccato: a light bounce from the wrist. Hold G for all four beats.</>,
      ]}/>
      <LbRemember>{t('Legato joins. Staccato bounces.', '레가토는 잇고, 스타카토는 튀어요.')}</LbRemember>
    </LbPage>,

    // 6. slur and tie
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Slur and tie', '이음줄과 붙임줄')}>
      {live(pic(p6, 280, 600), <SdyPad page={6}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['이음줄', '음높이가 다른 음들 위나 아래의 곡선. 레가토로 치고, 마지막 음 뒤에 손을 살짝 들어요.'],
        ['붙임줄', '같은 음 두 개를 잇는 곡선(' + bkChapterNo('time-signatures') + '챕터). 첫 음만 치고, 두 음의 길이만큼 누르고 있어요.'],
      ] : [
        ['slur', 'A curve over or under different notes. Play them legato, and lift after the last one.'],
        ['tie', 'A curve joining two of the same note (chapter ' + bkChapterNo('time-signatures') + '). Play the first, then hold it for both.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC}: 위 악보를 쳐요. 이음줄로 이은 G{' '}F{' '}E{' '}D{' '}C를 부드럽게 이어서 쳐요.</>,
        <>아래 악보를 1{' '}2{' '}3{' '}4로 세면서 쳐요: 1에 E, 3에 G. G는 한 번만 치고 둘째 마디 끝까지 누르고 있어요.</>,
      ] : [
        <>{RHC}: play the top tune, G F E D C with the slur, smooth and joined.</>,
        <>Play the bottom tune, counting 1 2 3 4: E on 1, G on 3. Play G once and hold it to the end of bar 2.</>,
      ]}/>
      <LbRemember>{t('Different notes: a slur. The same note: a tie.', '다른 음: 이음줄. 같은 음: 붙임줄.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={chkArts[a]} vb={vbs[a]} style={{width:80}}/>, sdyRich(x)])}/>} live={<FiveChecks376 storeKey="pb_five_sdy_v1" rows={checksRows.map(([a, x]) => [{ shapes: chkArts[a], vb: vbs[a] }, sdyRich(x)])}/>}/>
    </LbPage>,
  ];
}
function DynamicsLessonBook() { return <>{sdyLbPages(false)}</>; }
