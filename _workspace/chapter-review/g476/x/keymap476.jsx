// ─── Phase 476: the twelve keys, macro first (her 2026-10-17 02:05 '1.2.3. 다동의해': see the whole, then the parts).
// Scales (chapter 16) and Key Signatures (chapter 19) open with a map of all twelve major keys and end with it again; in
// between, the steps zoom in on a few keys. The scales map is the keyboard bent into a clock (a semitone a step), the major
// scale one shape that turns to start on any key; the key-signature map is the circle of fifths (from C at the top, one
// more sharp each step clockwise, one more flat anticlockwise). The teacher sets each student's keys in the dashboard
// ("For the student", saved as a line [keys:C,G,D]); the student's drills and maps use them (default: the chapter's exam
// keys). Reading key signatures stays step by step: the map shows them all, the steps teach five.
// Colour on the maps (review r1): the keys keep the piano's colours; coral is only the half steps (the clock) and the key
// being looked at with its signs (the circle); navy marks are the student's (stamps, my keys, keys I know).

// the student's keys (set by the teacher's [keys:...] line; kept on the device until a new line comes; [keys:-]: none)
const PB_KEYS_LS = 'pb_my_keys_v1';
const KEY12 = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];   // a semitone a step, the major keys' usual names
const KEY_ALIAS = { 'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb', Cb: 'B', Fb: 'E', 'E#': 'F', 'B#': 'C' };
const pbKeyId = (k) => { const s = String(k || '').trim().replace(/♯/g, '#').replace(/♭/g, 'b'); const n = s ? s[0].toUpperCase() + s.slice(1) : ''; return KEY12.includes(n) ? n : KEY_ALIAS[n] || null; };
function pbMyKeys() { try { const a = JSON.parse(localStorage.getItem(PB_KEYS_LS)); const k = Array.isArray(a) ? [...new Set(a.map(pbKeyId).filter(Boolean))] : []; return k.length ? k : null; } catch (e) { return null; } }
function pbSetMyKeys(a) { try { localStorage.setItem(PB_KEYS_LS, JSON.stringify(a)); } catch (e) {} }
function pbClearMyKeys() { try { localStorage.removeItem(PB_KEYS_LS); } catch (e) {} }   // [keys:-]: back to the chapter's keys
const HW_KEYS_RE = /^\s*\[keys:([^\]]{0,80})\]\s*$/;
const pbHwLine = (x) => String(x).replace(/^\s*(?:[-*•·]|\d+[.)])\s+/, '').trim();   // a homework line without its list mark
// -> null (no keys line), [] (a line with no keys: [keys:-]) or the keys
function pbKeysFromHomework(text) {
  const line = String(text || '').split(/\r?\n/).map(pbHwLine).find(x => HW_KEYS_RE.test(x)); if (!line) return null;
  return [...new Set(HW_KEYS_RE.exec(line)[1].split(/[\s,]+/).map(pbKeyId).filter(Boolean))];
}
const PB_KEYS_DEFAULT = { scales: ['C', 'G', 'F'], 'key-signatures': ['C', 'G', 'D', 'F', 'Bb'] };
const pbKeysFor = (ch) => { const m = pbMyKeys(); return { keys: m || PB_KEYS_DEFAULT[ch], fromTeacher: !!m }; };
const pbKeyName = (k) => prettyNote(k);
const pbKeyPc = (k) => KEY12.indexOf(pbKeyId(k));
// its scale, spelled (D major: D E F♯ G A B C♯)
const pbSpell = (k) => spellScale(k);
// its fingering (one octave), and the keys that share both hands' (C G D A E: one group), in the teaching order
const pbFingers = (k) => { const s = SCALES[k] || SCALES[{ Gb: 'F#', Db: 'C#' }[k]]; return s ? s.octaves[1] : null; };
const pbSameFingers = (k) => { const f = pbFingers(k); if (!f) return []; return SCALE_PATH.filter(x => x !== k && pbFingers(x) && pbFingers(x).RH.join() === f.RH.join() && pbFingers(x).LH.join() === f.LH.join()); };
// a list of MIDI notes (or null for a rest), each a beat; the returned timers carry each note's release (pbStopMidi)
function pbPlayMidi(list, bpm, onStep) {
  const ctx = getAudio(); if (!ctx) return [];
  const spb = 60 / bpm, t0 = ctx.currentTime + 0.1, timers = [];
  timers.rel = [];
  list.forEach((m, i) => { if (m != null) { const r = blip(ctx, t0 + i * spb, 440 * Math.pow(2, (m - 69) / 12), spb * 0.9, 0.17, 'triangle'); if (typeof r === 'function') timers.rel.push(r); } if (onStep) timers.push(setTimeout(() => onStep(i), (0.1 + i * spb) * 1000)); });
  if (onStep) timers.push(setTimeout(() => onStep(-1), (0.1 + list.length * spb) * 1000 + 150));
  return timers;
}
const pbScaleMidi = (k) => { const pc = pbKeyPc(k), base = 60 + pc - (pc > 6 ? 12 : 0); return [0, 2, 4, 5, 7, 9, 11, 12].map(o => base + o); };
const PB_MAJOR = [0, 2, 4, 5, 7, 9, 11];
const pbStopMidi = (timers) => { (timers || []).forEach(clearTimeout); ((timers && timers.rel) || []).forEach(r => { try { r(); } catch (e) {} }); };
// a spelled note's other name (F♯ / G♭, C♭ / B); a natural has none
const PB_SH = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'], PB_FL = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'];
const pbEnh = (n) => n.length < 2 ? null : (n[1] === '#' ? PB_FL : PB_SH)[scalePcOf(n)];
const KEY_ALIAS_BACK = { Db: 'C#', Eb: 'D#', Gb: 'F#', Ab: 'G#', Bb: 'A#' };
// in SVG text: a sharp or flat in Inter (the serif has none, and its fallback prints wide)
const pbAccT = (x) => typeof x !== 'string' || !/[♯♭]/.test(x) ? x : x.split(/([♯♭])/).map((p, i) => /[♯♭]/.test(p) ? <tspan key={i} style={{fontFamily:'Inter, sans-serif'}}>{p}</tspan> : p);
// a Workbook part with its own badge (the clock or circle kept all year)
Object.assign(BK_TAG, { year: { label: 'ALL YEAR', sub: 'kept all year', bg: BK.ink, fg: '#fff' } });

// the keyboard clock: twelve keys round a circle, white and black as on the piano, C at the top, clockwise up.
// o.shape: the major scale from the selected key as one shape (it turns when the key changes; its two half steps coral;
// the scale's first note the big dot), the keys named as the scale spells them; o.plain: the keys' own names (a white key
// the scale spells with a sign shows both, B / C♭); o.tonicOnly: only the big dot; o.nums: the shape's dots numbered;
// o.mark: a key (0-11) outlined; o.mine: the student's keys (a navy arc outside); o.stamps: { key: [right, left, together] }
// (three dots in each key, read left to right; a tick when all three); o.paper: for print (the black keys white with a navy band, to colour)
function KeyRing({ sel = 'C', onPick, o = {}, label }) {
  const C = 180, R1 = 160, R0 = 106, RP = 88, idx = Math.max(0, KEY12.indexOf(sel)), black = [1, 3, 6, 8, 10], P = !!o.paper;
  const sp = pbSpell(sel), deg = (i) => (i - idx + 12) % 12, inScale = (i) => PB_MAJOR.includes(deg(i));
  const spAt = (i) => inScale(i) ? sp[PB_MAJOR.indexOf(deg(i))] : null, spelled = o.shape && !o.plain;
  const pt = (a, r) => [C + r * Math.cos(a * Math.PI / 180), C + r * Math.sin(a * Math.PI / 180)];
  const arcPath = (i, ra, rb) => { const a0 = -105 + i * 30, a1 = a0 + 30, [x0, y0] = pt(a0, ra), [x1, y1] = pt(a0, rb), [x2, y2] = pt(a1, rb), [x3, y3] = pt(a1, ra);
    return `M${x0} ${y0} L${x1} ${y1} A${rb} ${rb} 0 0 1 ${x2} ${y2} L${x3} ${y3} A${ra} ${ra} 0 0 0 ${x0} ${y0} Z`; };
  const mine = new Set((o.mine || []).map(pbKeyId)), st = o.stamps;
  const shapePts = PB_MAJOR.map(s => pt(-90 + s * 30, RP)), LR = st ? 126 : 133;
  const two = (x, y, a, b, fill, fs) => <text x={x} y={y} textAnchor="middle" fontSize={fs} fontWeight="900" fill={fill} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-2.5">{a}</tspan><tspan x={x} dy="15">{b}</tspan></text>;
  const one = (x, y, a, fill, fs) => <text x={x} y={y + 6} textAnchor="middle" fontSize={fs} fontWeight="900" fill={fill} style={{fontFamily:"'Playfair Display', Georgia, serif",pointerEvents:'none'}}>{pbAccT(a)}</text>;
  const tick = (x, y, bg, fg) => <g style={{pointerEvents:'none'}}><circle cx={x} cy={y} r="8.5" fill={bg}/><path d={`M${x - 4} ${y} L${x - 1} ${y + 3.2} L${x + 4.5} ${y - 3.5}`} fill="none" stroke={fg} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/></g>;
  return (
    <svg viewBox="0 0 360 360" role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      {KEY12.map((k, i) => { const b = black.includes(i), fill = b && !P ? PEN_N : '#fff', ink = b && !P ? '#fff' : PEN_N;
        const [lx, ly] = pt(-90 + i * 30, LR), nm = spAt(i), fs2 = P ? 15 : 14.5;
        const lab = spelled && nm ? one(lx, ly, prettyNote(nm), ink, b ? 16 : 18)
          : b ? two(lx, ly, prettyNote(KEY_ALIAS_BACK[k]), prettyNote(k), ink, fs2)
          : o.plain && o.shape && nm && nm !== k ? two(lx, ly, prettyNote(k), prettyNote(nm), ink, fs2)
          : one(lx, ly, k, ink, 18);
        const f3 = st ? (st[k] || [false, false, false]) : [], n = f3.filter(Boolean).length, [tx, ty] = pt(-90 + i * 30, 151), lr = i >= 4 && i <= 8 ? -1 : 1;
        return <g key={k} data-key={k} onClick={onPick ? () => onPick(k) : undefined} style={{cursor:onPick ? 'pointer' : 'default'}}>
          {onPick && <path d={arcPath(i, 96, 176)} fill="transparent"/>}
          <path d={arcPath(i, R0, R1)} fill={fill} stroke={PEN_N} strokeWidth="1.4" strokeLinejoin="round"/>
          {P && b && <path d={arcPath(i, R1 - 12, R1)} fill={PEN_N} stroke={PEN_N} strokeWidth="1.4" strokeLinejoin="round"/>}
          {lab}
          {mine.has(k) && (() => { const a0 = -101 + i * 30, a1 = a0 + 22, [x1, y1] = pt(a0, R1 + 7), [x2, y2] = pt(a1, R1 + 7); return <path d={`M${x1} ${y1} A${R1 + 7} ${R1 + 7} 0 0 1 ${x2} ${y2}`} fill="none" stroke={PEN_N} strokeWidth="4" strokeLinecap="round"/>; })()}
          {st && (n >= 3 ? tick(tx, ty, b ? '#fff' : PEN_N, b ? PEN_N : '#fff')
            : [0, 1, 2].map(j => { const [x, y] = pt(-90 + i * 30 + lr * (j - 1) * 7, 151); return <circle key={j} cx={x} cy={y} r="5" fill={f3[j] ? ink : fill} stroke={ink} strokeWidth="1.3" style={{pointerEvents:'none'}}/>; }))}
        </g>; })}
      {[onPick ? idx : null, o.mark != null ? o.mark : null].filter(x => x != null).map((m, j) => <g key={'o' + j} style={{pointerEvents:'none'}}><path d={arcPath(m, R0, R1)} fill="none" stroke={PEN_N} strokeWidth="3.5" strokeLinejoin="round"/>
        {black.includes(m) && !P && <path d={arcPath(m, R0 + 4, R1 - 4)} fill="none" stroke="#fff" strokeWidth="2.5" strokeLinejoin="round"/>}</g>)}
      {o.shape && <g style={{transform:'rotate(' + idx * 30 + 'deg)',transformOrigin:C + 'px ' + C + 'px',transformBox:'view-box',transition:'transform 0.5s ease',pointerEvents:'none'}}>
        {shapePts.map((p, j) => { const q = shapePts[(j + 1) % 7], half = j === 2 || j === 6; return <line key={j} x1={p[0]} y1={p[1]} x2={q[0]} y2={q[1]} stroke={half ? PEN_C : PEN_N} strokeWidth={half ? 3.4 : 2} strokeLinecap="round"/>; })}
        {shapePts.map((p, j) => <circle key={'d' + j} cx={p[0]} cy={p[1]} r={j === 0 ? 8 : 4.5} fill={PEN_N} stroke={j === 0 ? '#fff' : 'none'} strokeWidth="2.5"/>)}
      </g>}
      {o.tonicOnly && (() => { const [x, y] = pt(-90 + idx * 30, RP); return <circle cx={x} cy={y} r="8" fill={PEN_N} stroke="#fff" strokeWidth="2.5"/>; })()}
      {o.nums && PB_MAJOR.map((s, j) => { const [x, y] = pt(-90 + ((idx + s) % 12) * 30, RP - 19); return <text key={'n' + j} x={x} y={y + 4} textAnchor="middle" fontSize="12" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{j + 1}</text>; })}
      {o.center && <g style={{pointerEvents:'none'}}>{o.center(C)}</g>}
    </svg>
  );
}
// the circle of fifths: the twelve major keys. o.filled: navy circles (the keys being learnt: the chapter's, or the
// student's); sel: the key looked at (coral ring); o.known: a tick (keys I know); o.paper: bigger labels for print;
// o.en: English hints (the Workbook is English only)
const FIFTHS = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F'];
const FIFTHS_SIG = ['0', '1♯', '2♯', '3♯', '4♯', '5♯', '6♯ 6♭', '5♭', '4♭', '3♭', '2♭', '1♭'];
function FifthsRing({ sel, onPick, o = {}, label }) {
  const C = 180, R = 124, r = 28, have = new Set((o.filled || []).map(pbKeyId)), known = new Set(o.known || []), P = !!o.paper;
  const hint = (en, ko) => o.en ? en : t(en, ko);
  const pt = (a, rr) => [C + rr * Math.cos(a * Math.PI / 180), C + rr * Math.sin(a * Math.PI / 180)];
  const hit = (i) => { const a0 = -105 + i * 30, a1 = a0 + 30, [x0, y0] = pt(a0, 70), [x1, y1] = pt(a0, 176), [x2, y2] = pt(a1, 176), [x3, y3] = pt(a1, 70);
    return `M${x0} ${y0} L${x1} ${y1} A176 176 0 0 1 ${x2} ${y2} L${x3} ${y3} A70 70 0 0 0 ${x0} ${y0} Z`; };
  return (
    <svg viewBox="0 0 360 360" role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      <circle cx={C} cy={C} r={R} fill="none" stroke="rgba(38,41,107,0.18)" strokeWidth="1.5" strokeDasharray="3 5"/>
      <text x={C + 44} y={C - 56} textAnchor="middle" fontSize={P ? 13 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{hint('more ♯ →', '♯ 많아짐 →')}</text>
      <text x={C - 44} y={C - 56} textAnchor="middle" fontSize={P ? 13 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{hint('← more ♭', '← ♭ 많아짐')}</text>
      {FIFTHS.map((k, i) => { const [x, y] = pt(-90 + i * 30, R), [lx, ly] = pt(-90 + i * 30, R + 44);
        const f = have.has(k), s = sel === k, ink = f ? '#fff' : PEN_N;
        return <g key={k} data-key={k} onClick={onPick ? () => onPick(k) : undefined} style={{cursor:onPick ? 'pointer' : 'default'}}>
          {onPick && <path d={hit(i)} fill="transparent"/>}
          {s && <circle cx={x} cy={y} r={r + 5} fill="none" stroke={PEN_C} strokeWidth="3"/>}
          <circle cx={x} cy={y} r={r} fill={f ? PEN_N : '#fff'} stroke={PEN_N} strokeWidth="1.5"/>
          {k === 'Gb' ? <text x={x} y={y} textAnchor="middle" fontSize={P ? 14 : 13.5} fontWeight="900" fill={ink} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-2.5">F♯</tspan><tspan x={x} dy="15">G♭</tspan></text>
            : <text x={x} y={y + 7} textAnchor="middle" fontSize="20" fontWeight="900" fill={ink} style={{fontFamily:"'Playfair Display', Georgia, serif",pointerEvents:'none'}}>{pbAccT(prettyNote(k))}</text>}
          {known.has(k) && <g style={{pointerEvents:'none'}}><circle cx={x + 21} cy={y - 21} r="9" fill="#fff" stroke={PEN_N} strokeWidth="1.6"/><path d={`M${x + 17} ${y - 21} L${x + 20} ${y - 17.8} L${x + 25.5} ${y - 24.5}`} fill="none" stroke={PEN_N} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/></g>}
          <text x={lx} y={ly + 4} textAnchor="middle" fontSize={P ? 14 : 12} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{FIFTHS_SIG[i]}</text>
        </g>; })}
      {o.center && <g style={{pointerEvents:'none'}}>{o.center(C)}</g>}
    </svg>
  );
}
// the key-signature data for every major key (chapter 19 knew seven): the sign and how many
Object.assign(SKG_KEY, { E: ['#', 4], B: ['#', 5], 'F#': ['#', 6], 'C#': ['#', 7], Ab: ['b', 4], Db: ['b', 5], Gb: ['b', 6], Cb: ['b', 7] });
const PB_NUM = { en: ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven'], ko: ['', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱'] };
const pbCountWords = (key) => { const [s, n] = SKG_KEY[key]; return n === 0 ? t('no sharps or flats', '샤프도 플랫도 없음') : t(PB_NUM.en[n] + (s === '#' ? ' sharp' : ' flat') + (n > 1 ? 's' : ''), (s === '#' ? '샤프 ' : '플랫 ') + PB_NUM.ko[n]); };
// the scale stamps (the same store as the Today page's scales: right hand, left hand, hands together) and, under 'ks:',
// the key signatures I know (chapter 19's map)
const pbStampCounts = () => { const s = loadStamps(), out = {}; KEY12.forEach(k => { out[k] = ['RH', 'LH', 'HT'].map(st => !!(s[k + ':' + st] || (KEY_ALIAS_BACK[k] && s[KEY_ALIAS_BACK[k] + ':' + st]))); }); return out; };
const pbKnownKeys = () => { const s = loadStamps(); return KEY12.filter(k => s['ks:' + k]); };
// the keys line under a map: the mark, the words, the keys (each with its dot, so a dot never stands alone)
const pbKeysRow = (mark, fromTeacher, keys) => <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.ink,margin:'4px 0',lineHeight:1.6}}>
  <span style={{whiteSpace:'nowrap'}}>{mark}{fromTeacher ? t('My keys from my teacher:', '선생님이 정한 나의 조:') : t('This chapter’s keys:', '이 챕터의 조:')}</span><br/>
  {keys.map((k, i) => <React.Fragment key={k}>{i ? ' ' : ''}<span style={{whiteSpace:'nowrap'}}>{i ? '· ' : ''}{sscSx(pbKeyName(k))}</span></React.Fragment>)}</div>;
const PB_ARC = <svg width="18" height="8" viewBox="0 0 18 8" aria-hidden="true" style={{marginRight:5,verticalAlign:'middle'}}><path d="M2 6 Q9 1 16 6" fill="none" stroke={PEN_N} strokeWidth="3" strokeLinecap="round"/></svg>;
const PB_DOT = <svg width="13" height="13" viewBox="0 0 13 13" aria-hidden="true" style={{marginRight:5,verticalAlign:'-1px'}}><circle cx="6.5" cy="6.5" r="5.5" fill={PEN_N}/></svg>;

// ── chapter 16: the map pad (the opener; again at the end, with the stamps and the fingering) ──
function SscMapPad({ end }) {
  const { keys, fromTeacher } = pbKeysFor('scales');
  const [sel, setSel] = useState(end ? keys[0] : 'C');
  const [stamps, setStamps] = useState(() => end ? pbStampCounts() : {});
  const [lit, setLit] = useState(-1);
  const timers = useRef([]);
  const stop = () => { pbStopMidi(timers.current); timers.current = []; setLit(-1); };
  useEffect(() => () => stop(), []);
  const choose = (k) => { stop(); setSel(k); };
  const listen = () => { stop(); timers.current = pbPlayMidi(pbScaleMidi(sel), 110, (i) => { if (i < 0) { timers.current = []; setLit(-1); } else setLit(i); }); };
  const names = pbSpell(sel), same = pbSameFingers(sel), F = pbFingers(sel);
  const stampBtn = (st, en, ko) => { const s = loadStamps(), id = sel + ':' + st, v = !!s[id];
    return <button key={st} className={'chip' + (v ? ' active' : '')} style={{minHeight:44,width:'100%',justifyContent:'center',padding:'4px 6px'}} aria-pressed={v} onClick={() => { const n = { ...loadStamps() }; if (n[id]) delete n[id]; else n[id] = Date.now(); saveStamps(n); setStamps(pbStampCounts()); }}>{v ? '✓ ' : ''}{t(en, ko)}</button>; };
  const dot = (f) => <svg width="11" height="11" viewBox="0 0 11 11" aria-hidden="true" style={{verticalAlign:'-1px'}}><circle cx="5.5" cy="5.5" r="4" fill={f ? PEN_N : '#fff'} stroke={PEN_N} strokeWidth="1.3"/></svg>;
  return (
    <div className="try-box" style={actBox} data-pb="scale-map">
      {!end && <div style={actTitle}>{t('One shape, twelve keys', '모양 하나, 열두 조')}</div>}
      <div style={{...actNote,textWrap:'pretty'}}>{end ? t('Tap a key: its scale’s shape turns to start there. When you can play the scale well, stamp it: right hand, left hand, hands together.', '조를 누르면 음계 모양이 돌아서 그 조에서 시작해요. 음계를 잘 칠 수 있으면 도장을 찍어요: 오른손, 왼손, 양손.')
        : t('The keys in a ring, clockwise up: the next key is a half step, skip one for a whole step. Tap a key: the major scale’s shape turns to start there. Every major key has the same shape.', '건반을 둥글게 이었어요. 시계 방향으로 가면 올라가요. 바로 옆 건반은 반 걸음, 하나 건너뛰면 온 걸음이에요. 조를 누르면 장음계 모양이 돌아서 그 조에서 시작해요. 장조는 모두 모양이 같아요.')}</div>
      <div style={{maxWidth:330,margin:'0 auto'}}><KeyRing sel={sel} onPick={choose} o={{ shape: true, mine: keys, stamps: end ? stamps : null,
        center: (C) => <><text x={C} y={C - 4} textAnchor="middle" fontSize="22" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(prettyNote(sel))}</text><text x={C} y={C + 18} textAnchor="middle" fontSize="13" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('major', '장조')}</text></> }}
        label={t('The keyboard clock: the twelve keys in a ring, the ' + prettyNote(sel) + ' major scale drawn as a shape.', '건반 시계: 열두 건반이 원을 이루고, ' + prettyNote(sel) + '장조 음계가 모양으로 그려져 있어요.')}/></div>
      <div style={{display:'flex',justifyContent:'center',gap:3,margin:'6px auto 2px',maxWidth:340}}>{[...names, names[0]].map((n, i) => <span key={i} style={{flex:'1 1 0',minWidth:0,maxWidth:40,textAlign:'center',padding:'3px 0',borderRadius:6,border:'1.5px solid ' + (i === 0 || i === 7 ? PEN_N : 'rgba(38,41,107,0.3)'),fontSize:'clamp(13px, 4vw, 16px)',fontWeight:900,color:BK.ink,background:lit === i ? '#fbe3da' : '#fff'}}>{sscSx(prettyNote(n))}</span>)}</div>
      {end && <div style={{textAlign:'center',fontSize:12.5,fontWeight:700,color:BK.muted,margin:'4px 0'}}>{dot(true)}{dot(true)}{dot(false)} {t('right hand, left hand, together', '오른손, 왼손, 양손')} <span style={{whiteSpace:'nowrap'}}>· ✓ {t('all three', '셋 다')}</span></div>}
      {end && F && <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.muted,margin:'6px 0',lineHeight:1.5}}><span style={{whiteSpace:'nowrap'}}>{t('RH', '오른손')} {F.RH.join(' ')}</span> <span style={{whiteSpace:'nowrap'}}>· {t('LH', '왼손')} {F.LH.join(' ')}</span>{same.length ? <><br/>{sscSx(t('Same fingers: ' + same.map(pbKeyName).join(', '), '손가락 번호가 같은 조: ' + same.map(pbKeyName).join(', ')))}</> : null}</div>}
      {pbKeysRow(PB_ARC, fromTeacher, keys)}
      {end && <div style={{margin:'6px auto',maxWidth:360}}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,margin:'0 0 5px'}}>{sscSx(t('Stamp ' + prettyNote(sel) + ' major:', prettyNote(sel) + '장조 도장:'))}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6}}>{stampBtn('RH', 'Right', '오른손')}{stampBtn('LH', 'Left', '왼손')}{stampBtn('HT', 'Together', '양손')}</div></div>}
      <div style={{display:'flex',gap:6,justifyContent:'center',alignItems:'center'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <a className="ghost-btn" style={{minHeight:44,display:'inline-flex',alignItems:'center',textDecoration:'none'}} href={'?tool=scale-finder&key=' + encodeURIComponent(sel) + (LANG === 'ko' ? '&lang=ko' : '')}>{t('Fingering →', '손가락 번호 →')}</a>
      </div>
    </div>
  );
}

// ── chapter 19: the map pad (the opener; again at the end, with the keys I know) ──
function SkgMapPad({ end }) {
  const { keys, fromTeacher } = pbKeysFor('key-signatures');
  const [sel, setSel] = useState(end ? keys[0] : 'G');
  const [known, setKnown] = useState(() => pbKnownKeys());
  const sg = SKG_KEY[sel] ? sel : 'C', n = SKG_KEY[sg][1];
  const staff = (clef) => <div style={{flex:'1 1 0',minWidth:0,maxWidth:190}}><SkgStaff items={SKG_ALONE} k={sg} clef={clef} width={200} full pad={[26, 18]} o={{ base: 54, ksRoom: Math.max(2, n), ksCol: PEN_C }}/></div>;
  const isKnown = known.includes(sel);
  const toggle = () => { const s = { ...loadStamps() }, id = 'ks:' + sel; if (s[id]) delete s[id]; else s[id] = Date.now(); saveStamps(s); setKnown(pbKnownKeys()); };
  return (
    <div className="try-box" style={actBox} data-pb="key-map">
      {!end && <div style={actTitle}>{t('The twelve keys', '열두 조')}</div>}
      <div style={{...actNote,textWrap:'pretty'}}>{end ? t('Tap a key to see its key signature. When you can draw it and name the key, mark it ✓.', '조를 누르면 조표가 보여요. 조표를 그리고 조 이름을 말할 수 있으면 ✓ 표시를 해요.')
        : t('From C at the top (no sharps or flats): one more sharp each step clockwise, one more flat each step anticlockwise. They meet at the bottom: F♯ and G♭. Tap a key to see its key signature.', '맨 위의 C(샤프도 플랫도 없음)에서 시계 방향으로 한 칸마다 샤프가 하나씩, 반시계 방향으로 한 칸마다 플랫이 하나씩 늘어요. 둘은 맨 아래 F♯와 G♭에서 만나요. 조를 누르면 조표가 보여요.')}</div>
      <div style={{maxWidth:330,margin:'0 auto'}}><FifthsRing sel={sel} onPick={setSel} o={{ filled: keys, known: end ? known : [],
        center: (C) => <><text x={C} y={C - 4} textAnchor="middle" fontSize="20" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(skgKeyName(sel))}</text><text x={C} y={C + 18} textAnchor="middle" fontSize="13" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{pbCountWords(sg)}</text></> }}
        label={t('The circle of fifths: the twelve major keys in a ring, C at the top; ' + (fromTeacher ? 'my keys' : 'this chapter’s keys') + ' filled.', '5도권: 열두 장조가 원을 이루고, 맨 위에 C가 있어요. ' + (fromTeacher ? '나의 조' : '이 챕터의 조') + '는 칠해져 있어요.')}/></div>
      <div style={{display:'flex',gap:8,justifyContent:'center',margin:'4px 0'}}>{staff('treble')}{staff('bass')}</div>
      {sel === 'Gb' && <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted}}>{sscSx(t('Played on the same piano keys as F♯ major (six sharps).', 'G♭장조는 F♯장조(샤프 여섯)와 건반이 같아요.'))}</div>}
      {pbKeysRow(PB_DOT, fromTeacher, keys)}
      {end && <div style={{display:'flex',justifyContent:'center',margin:'6px 0 0'}}><button className={'chip' + (isKnown ? ' active' : '')} style={{minHeight:44,maxWidth:'100%',whiteSpace:'normal',textAlign:'center',lineHeight:1.3,textWrap:'balance'}} aria-pressed={isKnown} onClick={toggle}>{isKnown ? '✓ ' : ''}{sscSx(t('I can draw it and name it: ' + prettyNote(sel) + ' major', prettyNote(sel) + '장조: 조표를 그리고 이름을 말할 수 있어요'))}</button></div>}
    </div>
  );
}

// ── the drills' extra level: the student's own keys ──
// chapter 16: which note is degree N (the clock shows the shape from the big dot, the keys by their own names: the spelling
// is the question), or which note is in the scale (only the big dot: count round W W H W W W H); 'which' only for a key whose
// notes outside it are both plain and with a sign, so the answer is never the odd one out by its sign
function genMyScaleQ(prev) {
  const { keys } = pbKeysFor('scales'), uid = Math.random();
  for (let g = 0; g < 40; g++) {
    const k = pick(keys), names = pbSpell(k), flatKey = names.some(x => x[1] === 'b'), pcs = names.map(scalePcOf);
    const outs = (flatKey ? PB_FL : PB_SH).filter((n, pc) => !pcs.includes(pc)), mixed = outs.some(n => n.length === 1) && outs.some(n => n.length > 1);
    const sub = mixed && Math.random() < 0.4 ? 'which' : 'deg';
    if (sub === 'deg') {   // degree 2 to 7; the wrong answers: its other name, the letter with another sign, the notes either side
      const d = pick([1, 2, 3, 4, 5, 6]), ans = names[d], L = ans[0];
      const alt = ans.length > 1 ? L : (flatKey ? (['C', 'F'].includes(L) ? L + '#' : L + 'b') : (['E', 'B'].includes(L) ? L + 'b' : L + '#'));
      const ch = [...new Set([ans, pbEnh(ans), alt, names[d - 1], names[(d + 1) % 7]].filter(Boolean))].slice(0, 4), key = 'd' + k + d;
      if (prev && prev.key === key) continue;
      return { kind: 'mykeys', sub, k, d, key, raw: ans, answer: prettyNote(ans), choices: shuffle(ch.map(prettyNote)), uid };
    }
    const inS = pick(names.slice(1)), same = shuffle(outs.filter(n => (n.length > 1) === (inS.length > 1)));
    if (!same.length) continue;
    const rest = outs.filter(n => !same.includes(n)), key = 'w' + k + inS; if (prev && prev.key === key) continue;
    return { kind: 'mykeys', sub, k, key, raw: inS, answer: prettyNote(inS), choices: shuffle([inS, same[0], ...shuffle([...same.slice(1), ...rest]).slice(0, 2)].map(prettyNote)), uid };
  }
  return { kind: 'mykeys', sub: 'deg', k: 'C', d: 4, key: 'dC4', raw: 'G', answer: 'G', choices: shuffle(['G', 'G♯', 'F', 'A']), uid };
}
function MyScaleQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given), isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const ro = isDone ? { shape: true, nums: true, mark: scalePcOf(q.raw || 'C') } : q.sub === 'deg' ? { shape: true, plain: true } : { tonicOnly: true, plain: true };
  return <div><BoardTrack b={board} pixel={pixel}/>
    <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:pixel ? 14 : 24,fontWeight:900,color:'var(--navy)',margin:'0 0 4px'}}>{sscSx(sscScaleName(q.k))}</div>
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 2px',color:'var(--text)',textWrap:'balance',wordBreak:'keep-all'}}>{q.sub === 'deg' ? t('Which note is degree ' + (q.d + 1) + '?', (q.d + 1) + '번 음은 무엇일까요?') : t('Which note is in this scale?', '이 음계에 있는 음은?')}</p>
    <p style={{fontSize:pixel ? 10.5 : 13.5,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{q.sub === 'deg' ? t('The big dot is 1: count the dots clockwise.', '큰 점이 1번이에요. 시계 방향으로 점을 세어요.') : t('From the big dot: whole, whole, half, whole, whole, whole, half.', '큰 점에서: 온, 온, 반, 온, 온, 온, 반.')}</p>
    <div style={{maxWidth:260,margin:'0 auto 10px'}}><KeyRing sel={q.k} o={ro} label={t('The keyboard clock from ' + prettyNote(q.k) + '.', prettyNote(q.k) + '에서 시작하는 건반 시계.')}/></div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'12px 2px',minHeight:44}}><span style={{fontSize:pixel ? 11 : 20,fontWeight:900}}>{sscSx(c)}</span></button>)}</div>
  </div>;
}
const myScaleLabel = (q) => q.answer + ' (' + pbSpell(q.k).map(prettyNote).join(' ') + ')';   // a string (the game shows it in capitals)
// chapter 19: which major key has this key signature (the student's keys; with fewer than three, the chapter's join in)
function genMyKeySigQ(prev) {
  const { keys: mine } = pbKeysFor('key-signatures'), keys = mine.length >= 3 ? mine : [...new Set([...mine, ...PB_KEYS_DEFAULT['key-signatures']])], uid = Math.random();
  for (let g = 0; g < 30; g++) {
    const k0 = pick(keys), k = SKG_KEY[k0] ? k0 : 'C', i = FIFTHS.indexOf(k), clef = Math.random() < 0.35 ? 'bass' : 'treble', key = 'k' + k + clef;
    if (prev && prev.key === key) continue;
    const near = [FIFTHS[(i + 1) % 12], FIFTHS[(i + 11) % 12], FIFTHS[(i + 2) % 12], FIFTHS[(i + 10) % 12]].filter(x => x !== k);
    return { kind: 'mykeys', k, clef, key, answer: k, choices: shuffle([k, ...shuffle(near).slice(0, 3)]), uid };
  }
  return { kind: 'mykeys', k: 'G', clef: 'treble', key: 'kG', answer: 'G', choices: ['C', 'G', 'D', 'F'], uid };
}
function MyKeySigQuestion({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given), isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn', n = SKG_KEY[q.k][1];
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  return <div><BoardTrack b={board} pixel={pixel}/>
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 10px',color:'var(--text)',textWrap:'balance',wordBreak:'keep-all'}}>{t('Which major key has this key signature?', '이 조표는 어떤 장조일까요?')}</p>
    <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,margin:'0 auto 10px',maxWidth:230}}><SkgStaff items={SKG_ALONE} k={q.k} clef={q.clef} width={230} full pad={SKG_AL_PAD} o={{ base: 54, ksRoom: Math.max(2, n) }}/></div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'12px 4px',minHeight:44}}><span style={{fontSize:pixel ? 11 : 18,fontWeight:900}}>{sscSx(skgKeyName(c))}</span></button>)}</div>
    {isDone && !pixel && <div style={{maxWidth:240,margin:'8px auto 0'}}><FifthsRing sel={q.k} o={{ filled: [], paper: true }} label={t(skgKeyName(q.k) + ' on the circle of fifths.', '5도권의 ' + skgKeyName(q.k) + '.')}/></div>}
  </div>;
}
const myKeySigLabel = (q) => skgKeyName(q.k) + ' (' + pbCountWords(q.k) + (SKG_KEY[q.k][1] ? ': ' + skgSignNames(q.k).join(' ') : '') + ')';

// ── the Workbook's any-key page (page 7, before the check-up): the teacher writes the key; the clock or circle to
// colour all year (the student's first copy is the record) ──
const pbKeysHead = () => <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
  <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY KEY</div><div style={{fontSize:12.5,color:BK.muted,textWrap:'pretty'}}>Your teacher writes the key. Each new key gets a fresh copy of this page.</div></div>
  <div style={{display:'flex',alignItems:'center',gap:10,fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink,flex:'0 0 auto'}}><span style={{display:'inline-block',width:130,borderBottom:'2px solid ' + BK.ink,height:26}}/><span>major</span></div></div>;
const pbBoxes = (n, w = 46, h = 40, labels, gap = 6) => <div style={{display:'flex',gap,justifyContent:'center'}}>{Array.from({ length: n }, (_, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:2}}>{bkBox(w, h)}{labels && <span style={{fontSize:11,fontWeight:800,color:BK.muted}}>{labels[i]}</span>}</div>)}</div>;
const pbYear = (ring, text) => <Part kind="year" title="My twelve keys"><div style={{display:'grid',gridTemplateColumns:'260px 1fr',gap:18,alignItems:'center'}}><div style={{width:260}}>{ring}</div>
  <div style={{fontSize:13,color:BK.ink,lineHeight:1.55,textWrap:'pretty'}}>{text}</div></div></Part>;
function SscAnyKeyPage() {
  const steps = ['W', 'W', 'H', 'W', 'W', 'W', 'H'];
  return <>
    <WbTop step={7}/>
    {pbKeysHead()}
    <Part kind="together" title="Write the notes" how={<span style={{textWrap:'pretty'}}>Start on the key’s note and go up: whole, whole, half, whole, whole, whole, half. Use each letter once, in order; add a sharp or flat where the step needs one.</span>}>
      {sskRowN(1, <div style={{display:'flex',justifyContent:'center',alignItems:'flex-end',gap:3}}>{Array.from({ length: 8 }, (_, i) => <React.Fragment key={i}>{bkBox(44, 44)}{i < 7 && <span style={{fontSize:11.5,fontWeight:900,color:steps[i] === 'H' ? BK.coral : BK.muted,padding:'0 1px 14px'}}>{steps[i] === 'H' ? 'half' : 'whole'}</span>}</React.Fragment>)}</div>)}
    </Part>
    <Part kind="home" title="On the keys, on the staff" how={<span style={{textWrap:'pretty'}}>Fill the circle on each of the scale’s eight keys. Then write the scale on the staff as semibreves, going up, each sharp or flat before its note.</span>}>
      <div style={{display:'grid',gap:8}}>{sskRowN(2, <div style={{maxWidth:520,margin:'0 auto',width:'100%'}}><TnPKeys start="C" whites={14} w={37} h={96} slots wslots/></div>)}
        {sskRowN(3, <div style={{maxWidth:600,margin:'0 auto',width:'100%'}}><SfStaff clef="treble" width={600} pad={[22, 28]}/></div>)}</div>
    </Part>
    <Part kind="play" title="Its fingering, then play it" how="Write each hand’s fingers, going up. Play it with each hand, then hands together. Tick each one you can play.">
      {sskRowN(4, <div style={{display:'grid',gridTemplateColumns:'86px auto',justifyContent:'start',columnGap:10,rowGap:6,alignItems:'center'}}><b style={{fontSize:13,color:BK.ink}}>Right hand</b>{pbBoxes(8, 40, 34)}<b style={{fontSize:13,color:BK.ink}}>Left hand</b>{pbBoxes(8, 40, 34)}</div>)}
      <div style={{marginTop:8}}>{sscTicks(['right hand', 'left hand', 'hands together'])}</div>
    </Part>
    {pbYear(<KeyRing sel="C" o={{ paper: true }} label="The keyboard clock: the twelve keys, to colour."/>,
      <>Colour a key on the clock when you can play its scale with each hand; keep this clock on your first copy. <b>C, G, D, A and E share their fingering:</b> learn them as a group.</>)}
    <Faces/>
  </>;
}
function SkgAnyKeyPage() {
  const draw = (clef) => <div style={{maxWidth:300,width:'100%',margin:'0 auto'}}><SkgStaff items={[['sp', 120]]} k="C" clef={clef} width={300} full pad={[24, 18]} o={{ ...SKG_AL, ks: [] }}/></div>;
  return <>
    <WbTop step={7}/>
    {pbKeysHead()}
    <Part kind="together" title="Its sharps or flats, in order" how={<span style={{textWrap:'pretty'}}>Find the key on the circle below: the number beside it says how many. Write that many, in order, one in each box, each with its sign (sharps F C G D A E B; flats B E A D G C F). Leave the other boxes empty.</span>}>
      {sskRowN(1, pbBoxes(7, 50, 42, ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th']))}
    </Part>
    <Part kind="home" title="Draw the key signature" how="Draw it after each clef, in order, each sign on its line or space.">
      {sskRowN(2, <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>{draw('treble')}{draw('bass')}</div>)}
    </Part>
    <Part kind="play" title="Its scale, then play it" how={<span style={{textWrap:'pretty'}}>Draw the key signature, then write the scale going up as semibreves, with no sharp or flat beside a note (the key signature does it). In the boxes, name the notes, with any sharps or flats. Play it with each hand; tick each one you can play.</span>}>
      {sskRowN(3, <div style={{maxWidth:600,margin:'0 auto',width:'100%'}}><SfStaff clef="treble" width={600} pad={[22, 28]}/></div>)}
      {sskRowN(4, pbBoxes(8, 46, 38, null, 22))}
      <div style={{marginTop:8}}>{sscTicks(['right hand', 'left hand'])}</div>
    </Part>
    {pbYear(<FifthsRing o={{ filled: [], paper: true, en: true }} label="The circle of fifths: the twelve keys, to colour."/>,
      <>Colour a key on the circle when you can draw its key signature and name it. From C at the top: clockwise, one more sharp each step; anticlockwise, one more flat. They meet at the bottom: <span style={{whiteSpace:'nowrap'}}>F♯ and G♭.</span></>)}
    <Faces/>
  </>;
}
