// ── Build EC, call 41 (her 14:32 'a space that takes in the whole, like a book's reference pages: it becomes the map, easier
// to see'; 14:36 'all at once', Beginner to Grade 8): the Reference. One table per topic, no explanations beyond a line;
// each row carries the floor where the house teaches it and is a door into that room. Every row comes from a room's own
// teaching (its steps, its key lists: SCF, SCF_CM, S4_KEYS..., K4_IDS, MM_KEYS, H3_MIN, DEGREE_NAMES, DICT_TERMS); the
// patterns (tones and semitones, semitones in an interval, the key signatures) are counted by the code, not typed.
// On screen: ?tool=reference (the Home's Quick line); on paper: ?book=reference (A4, the books' look). The Scales map lives
// inside it (Scales, floor by floor) and the dictionary's terms are in Words about music.
// ── Build ED (her 31 Oct 15:56: 'the book's Reference is so good, I want almost all of it in the Reference; there is more
// after my screenshots'): the whole of the reference pages of the theory book in her folder (its pp. 226-251), in the
// house's own data and drawings, never the book's words or pictures: the grand staff and the four clefs; every note value
// from the breve to the hemidemisemiquaver with its rest; the time signatures the book lists (x/16, 9/4, 12/4, five and
// seven beats, 3 + 3 + 2); every major and minor scale spelt out; every chord on any root; the signs (the book's visual
// index); the words for how to play (the terms room's 96 and the book's others); words about music (the dictionary, the
// pieces rooms' kinds of piece and forms, the styles room's words); the periods (the composers room's six); the
// instruments (the Stories of music room's families, clefs and the score order). Rows the house does not teach say 'extra'.
// A ♪ plays the room's own sound where it has one. Spellings and steps are counted by the code (refSpell), not typed.
const RefPaper = React.createContext(false);
const RefGo = React.createContext(null);
const refFloor = (room) => { const s = STAGES.find(x => x.ids.includes(room)); return s && s.en ? s.en[0] : ''; };
const REF_STORY = { 'pitch-range': ['Instruments', '악기'], composers: ['Composers', '작곡가'], styles: ['Styles', '양식'], 'piano-story': ['The piano’s story', '피아노 이야기'] };   // the attic's rooms by name
function RefDoor({ room, g }) {
  const paper = React.useContext(RefPaper), go = React.useContext(RefGo);
  if (!room) return <span data-ref-extra style={{fontSize:10.5,fontWeight:800,fontStyle:'italic',color:BK.muted,whiteSpace:'nowrap',justifySelf:'end'}}>{t('extra', '더 알기')}</span>;
  const lab = g || (REF_STORY[room] ? t(REF_STORY[room][0], REF_STORY[room][1]) : refFloor(room));
  if (paper) return <span style={{fontSize:10.5,fontWeight:800,color:BK.muted,whiteSpace:'nowrap'}}>{lab}</span>;
  return <button type="button" className="chip" data-ref-door={room} onClick={() => go && go(room)} title={bkChapterName(room)}
    style={{minHeight:28,padding:'2px 7px',fontSize:11,fontWeight:900,whiteSpace:'nowrap',justifySelf:'end'}}>{lab} ›</button>;
}
// ♪: the room's own sound (screen only)
function RefHear({ on, k }) {
  if (React.useContext(RefPaper)) return null;
  return <button type="button" className="chip" data-ref-hear={k} aria-label={t('Hear it', '들어 보기')} onClick={(e) => { e.stopPropagation(); try { on(); } catch (err) {} }}
    style={{minHeight:28,minWidth:30,padding:'2px 7px',fontSize:13.5,fontWeight:900,color:BK.coral,lineHeight:1}}>♪</button>;
}
// a table: hairlines between rows, the columns set by the caller
function RefTable({ cols, head, rows, k }) {
  return <div data-ref-table={k} style={{display:'grid',gridTemplateColumns:cols,alignItems:'center',columnGap:8,border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'2px 10px'}}>
    {head && head.map((h, i) => <div key={'h' + i} style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',textTransform:'uppercase',padding:'7px 0 5px',borderBottom:'1px solid rgba(38,41,107,0.18)'}}>{h}</div>)}
    {rows.map((r, j) => r.map((c, i) => <div key={j + '-' + i} style={{padding:'5px 0',minWidth:0,borderBottom:j < rows.length - 1 ? '1px solid rgba(38,41,107,0.1)' : 'none',fontSize:13.5,lineHeight:1.35,color:BK.ink}}>{c}</div>))}
  </div>;
}
const RefNote = ({ children }) => <div style={{fontSize:12.5,color:BK.muted,lineHeight:1.45,margin:'6px 2px 0'}}>{children}</div>;
const RefLab = ({ children }) => <div style={{fontSize:12,fontWeight:900,color:BK.coral,letterSpacing:'0.06em',textTransform:'uppercase',margin:'10px 2px 5px'}}>{children}</div>;
function RefSvgEl({ inner, w, h, vb }) { const k = React.useContext(RefPaper) ? 0.78 : 1; return <svg viewBox={vb || ('0 0 ' + w + ' ' + h)} width={w * k} height={h * k} style={{display:'block',overflow:'visible'}} dangerouslySetInnerHTML={{ __html: inner }}/>; }
const refSvg = (inner, w, h, vb) => <RefSvgEl inner={inner} w={w} h={h} vb={vb}/>;
// spelling: a key note, then letter steps and semitones from it; the letter decides, the semitones set the sign
const REF_LET = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], REF_NATPC = [0, 2, 4, 5, 7, 9, 11], REF_ACC = { '-2': '𝄫', '-1': '♭', 0: '', 1: '♯', 2: '𝄪' };
const refKey = (k) => { const L = REF_LET.indexOf(k[0]), a = k.slice(1); return { L, pc: (REF_NATPC[L] + (a === '♯' ? 1 : a === '♭' ? -1 : 0) + 12) % 12 }; };
const refSpell = (k, steps, semis) => { const r = refKey(k); return steps.map((st, i) => { const L = (r.L + st) % 7, d = (((r.pc + semis[i] - REF_NATPC[L]) % 12) + 18) % 12 - 6; return REF_LET[L] + REF_ACC[d]; }); };
// a name with a double sharp or flat: the sign in the music font
const refNm = (s, key) => /[𝄪𝄫]/u.test(s) ? <span key={key} style={{whiteSpace:'nowrap'}}>{s[0]}<span style={{fontFamily:MUSIC_FONT}}>{s.slice(1)}</span></span> : <span key={key} style={{whiteSpace:'nowrap'}}>{s}</span>;
const refRoot = (pc) => 60 + pc - (pc > 6 ? 12 : 0);
const refHz = (m) => 440 * Math.pow(2, (m - 69) / 12);
// notes one after another (gap), then together (block)
function refPlayNotes(midis, gap = 0.28, block = true, len = 0.45) {
  const ctx = getAudio(); if (!ctx) return; stopClicks(); const t0 = ctx.currentTime + 0.06;
  midis.forEach((m, i) => blip(ctx, t0 + i * gap, refHz(m), len, 0.15, 'triangle'));
  if (block) { const b = t0 + midis.length * gap + 0.12; midis.forEach(m => blip(ctx, b, refHz(m), 1.2, 0.1, 'triangle')); }
}
// one note or rest, drawn with the house's own glyphs (nvbNote, nvbRest, the rhythm staff's rests): heads, stems and flags as
// everywhere else. kind: b w h q e s d x (breve to hemidemisemiquaver); dot: dotted
function refNoteSvg(kind, dot) {
  const y = 46, x = 14, col = PEN_N, flags = { s: 2, d: 3, x: 4 }[kind];
  let s;
  if (flags) {   // the quaver's flag two, three or four times, on a longer stem
    const sx = x + NV_SX, top = y - 30 - flags * 8;
    s = nvbHead(x, y, 'q', col, 1) + '<line x1="' + sx + '" y1="' + y + '" x2="' + sx + '" y2="' + top + '" stroke="' + col + '" stroke-width="1.9" stroke-linecap="round"/>'
      + Array.from({ length: flags }, (_, i) => '<path d="M' + sx + ' ' + (top + i * 8) + ' c 2 8 12 10 7.5 22" fill="none" stroke="' + col + '" stroke-width="2.4" stroke-linecap="round"/>').join('');
  } else if (kind === 'b') {   // the breve: the semibreve between two pairs of upright lines
    s = nvbHead(x, y, 'w', col, 1) + [-11.5, -9, 9, 11.5].map(d => '<line x1="' + (x + d) + '" x2="' + (x + d) + '" y1="' + (y - 6.5) + '" y2="' + (y + 6.5) + '" stroke="' + col + '" stroke-width="1.5"/>').join('');
  } else s = nvbNote(x, y, kind, { col }).svg;
  if (dot) s += '<circle cx="' + (x + (kind === 'b' ? 18 : 14)) + '" cy="' + (y - 2) + '" r="2.6" fill="' + col + '"/>';
  return flags > 2 ? refSvg(s, 30, 57, '0 -8 34 64') : refSvg(s, 30, 46, '0 4 34 52');
}
// a rest with n hooks on one slanting stroke (the quaver rest's own hook, again and again down the stroke)
const refHookRest = (x, y, n, col) => { const o = (n - 1) * 4; let s = '';
  for (let i = 0; i < n; i++) { const dx = -2.4 * i, dy = 8 * i - o;
    s += '<circle cx="' + (x - 2.6 + dx) + '" cy="' + (y - 6.6 + dy) + '" r="3" fill="' + col + '"/><path d="M' + (x - 3.4 + dx) + ' ' + (y - 4.6 + dy) + ' Q' + (x + 1.6 + dx) + ' ' + (y - 3.4 + dy) + ' ' + (x + 4.6 + dx) + ' ' + (y - 9 + dy) + '" fill="none" stroke="' + col + '" stroke-width="2.1" stroke-linecap="round"/>'; }
  return s + '<line x1="' + (x + 4.6) + '" y1="' + (y - 9 - o) + '" x2="' + (x - 1 - 2.4 * (n - 1)) + '" y2="' + (y + 9.5 + o) + '" stroke="' + col + '" stroke-width="2.1" stroke-linecap="round"/>'; };
function refRestSvg(kind, dot) {
  const col = PEN_N, n = { e: 1, s: 2, d: 3, x: 4 }[kind];
  let s = kind === 'b' ? [22, 30].map(yy => '<line x1="6" x2="28" y1="' + yy + '" y2="' + yy + '" stroke="' + col + '" stroke-width="1.4"/>').join('') + '<rect x="13" y="22" width="8" height="8" fill="' + col + '"/>'
    : kind === 'w' ? nvbRest(17, 22, 'w', { col }).svg : kind === 'h' ? nvbRest(17, 34, 'h', { col }).svg : kind === 'q' ? nvbRest(17, 30, 'q', { col, k: 1.05 }).svg : refHookRest(19, 32, n, col);
  if (dot) s += '<circle cx="' + (kind === 'b' || kind === 'w' || kind === 'h' ? 30 : 27) + '" cy="' + (kind === 'w' ? 26 : 28) + '" r="2.6" fill="' + col + '"/>';
  return n > 2 ? refSvg(s, 30, 57, '0 -8 34 64') : refSvg(s, 30, 46, '0 4 34 52');
}
// a beamed group with its number over the beam: the triplet (3) and the duplet (2)
function refTupletSvg(n) {
  const xs = n === 3 ? [10, 30, 50] : [10, 34], y = 46;
  return refSvg(srhGroup(xs, y, xs.map(() => PEN_N), 1, PEN_N) + '<text x="' + ((xs[0] + xs[xs.length - 1]) / 2 + NV_SX) + '" y="7" text-anchor="middle" font-size="12" font-weight="900" font-style="italic" font-family="Georgia, serif" fill="' + PEN_N + '">' + n + '</text>', n === 3 ? 64 : 48, 52, '0 -4 ' + (n === 3 ? 64 : 48) + ' 56');
}
// a time signature: two numbers on a short staff, or the C and the cut C
function RefTime({ top, bot, sym }) {
  const lines = [0, 1, 2, 3, 4].map(i => '<line x1="0" x2="34" y1="' + (6 + i * 8) + '" y2="' + (6 + i * 8) + '" stroke="' + PEN_N + '" stroke-opacity="0.45" stroke-width="1"/>').join('');
  const num = (v, y) => '<text x="17" y="' + y + '" text-anchor="middle" font-size="' + (String(v).length > 1 ? 15.5 : 17.5) + '" font-weight="900" font-family="Georgia, serif" fill="' + PEN_N + '">' + v + '</text>';
  const inner = sym ? '<text x="17" y="28.5" text-anchor="middle" font-size="24" font-weight="900" font-family="Georgia, serif" fill="' + PEN_N + '">C</text>' + (sym === 'cut' ? '<line x1="17.5" x2="17.5" y1="6" y2="40" stroke="' + PEN_N + '" stroke-width="1.8"/>' : '')
    : num(top, 21.5) + num(bot, 37.5);
  return refSvg(lines + inner, 34, 46);
}
const refSec = (id, en, ko) => ({ id, en, ko });
const REF_SECS = [refSec('staff', 'The staff and the clefs', '오선과 음자리표'), refSec('notes', 'Notes and rests', '음표와 쉼표'), refSec('time', 'Time signatures', '박자표'), refSec('keys', 'Keys and key signatures', '조와 조표'),
  refSec('scales', 'Scales', '음계'), refSec('intervals', 'Intervals', '음정'), refSec('chords', 'Chords and cadences', '화음과 종지'), refSec('signs', 'Signs', '기호'),
  refSec('play', 'Words for how to play', '연주 용어'), refSec('terms', 'Words about music', '음악 낱말'), refSec('periods', 'Periods', '시대'), refSec('instruments', 'Instruments', '악기')];
function RefHead({ id }) { const s = REF_SECS.find(x => x.id === id); return <div id={'ref-' + id} data-ref-sec={id} style={{scrollMarginTop:12,margin:'0 0 8px'}}><StaffHead title={t(s.en, s.ko)}/></div>; }

// 1. the staff: every white key from C two octaves below middle C to C two octaves above, on the grand staff (tap: hear it);
// the four clefs, each with middle C where it sits
function RefGrandStaff() {
  const paper = React.useContext(RefPaper), [on, setOn] = useState(-1), tm = useRef(null);
  const yT = (d) => 68 - (d - 30) * 4, yB = (d) => yT(d) + 24, x0 = 62, dx = 15, W = x0 + 28 * dx + 14, H = 190;
  const ln = (y, a = 18, b = W - 4) => '<line x1="' + a + '" x2="' + b + '" y1="' + y + '" y2="' + y + '" stroke="' + PEN_N + '" stroke-opacity="0.55" stroke-width="1"/>';
  let s = [30, 32, 34, 36, 38].map(d => ln(yT(d))).join('') + [18, 20, 22, 24, 26].map(d => ln(yB(d))).join('');
  s += '<line x1="18" x2="18" y1="' + yT(38) + '" y2="' + yB(18) + '" stroke="' + PEN_N + '" stroke-width="1.3"/>';
  const ya = yT(38), yb = yB(18), ym = (ya + yb) / 2;   // the brace
  s += '<path d="M14 ' + ya + ' C6 ' + (ya + 8) + ' 12 ' + (ym - 14) + ' 6 ' + ym + ' C12 ' + (ym + 14) + ' 6 ' + (yb - 8) + ' 14 ' + yb + '" fill="none" stroke="' + PEN_N + '" stroke-width="2.4" stroke-linecap="round"/>';
  const notes = []; for (let d = 14; d <= 42; d++) notes.push(d);
  notes.forEach((d, i) => { const x = x0 + i * dx, up = d >= 28, y = up ? yT(d) : yB(d), col = i === on || d === 28 ? PEN_C : PEN_N;
    const led = (l) => ln(up ? yT(l) : yB(l), x - 8.5, x + 8.5).replace('stroke-opacity="0.55" stroke-width="1"', 'stroke-width="1.3"');
    if (up && d === 28) s += led(28);
    if (up) for (let l = 40; l <= d; l += 2) s += led(l);
    if (!up) for (let l = 16; l >= d; l -= 2) s += led(l);
    s += '<ellipse cx="' + x + '" cy="' + y + '" rx="5.4" ry="3.9" transform="rotate(-20 ' + x + ' ' + y + ')" fill="' + col + '"/>';
    s += '<text x="' + x + '" y="' + (H - 6) + '" text-anchor="middle" font-size="11" font-weight="900" font-family="Georgia, serif" fill="' + col + '">' + REF_LET[d % 7] + '</text>'; });
  const hit = (d, i) => { setOn(i); playKey(12 * (Math.floor(d / 7) + 1) + REF_NATPC[d % 7] - 60, 0.6); clearTimeout(tm.current); tm.current = setTimeout(() => setOn(-1), 450); };
  return <div style={{overflowX:paper ? 'visible' : 'auto',margin:'0 0 4px'}}>
    <svg data-ref-grand viewBox={'0 0 ' + W + ' ' + H} style={{width:paper ? '78%' : W,minWidth:paper ? 0 : W,display:'block',margin:paper ? '0 auto' : 0}} role="img" aria-label={t('Every white key from C2 to C6 on the grand staff', '큰보표 위의 흰건반, C2부터 C6까지')}>
      <g transform="translate(12 0)"><ClefGlyph clef="treble" st="treble" yOf={yT} ink={PEN_N}/><ClefGlyph clef="bass" st="bass" yOf={yB} ink={PEN_N}/></g>
      <g dangerouslySetInnerHTML={{ __html: s }}/>
      {!paper && notes.map((d, i) => <rect key={d} x={x0 + i * dx - 7.5} y="0" width={dx} height={H} fill="transparent" style={{cursor:'pointer'}} onClick={() => hit(d, i)}/>)}
    </svg>
  </div>;
}
const REF_CLEFS = [
  ['treble', 30, 'treble', 'Treble clef · G clef', '높은음자리표 · G음자리표', 'curls round G, line 2', 'G(둘째 줄)를 감아요', 'staff'],
  ['bass', 18, 'bass', 'Bass clef · F clef', '낮은음자리표 · F음자리표', 'its dots round F, line 4', '두 점이 F(넷째 줄)를 감싸요', 'staff'],
  ['alto', 24, 'alto', 'Alto clef · C clef', '알토음자리표 · C음자리표', 'middle C on line 3', '가운데 C가 셋째 줄', 'staff', 'Grade 2'],
  ['tenor', 22, 'alto', 'Tenor clef · C clef', '테너음자리표 · C음자리표', 'middle C on line 4', '가운데 C가 넷째 줄', 'pitch-range'],
];
function RefClefPic({ bottom, glyph }) {
  const yOf = (d) => 48 - (d - bottom) * 4, x = 70;
  let s = [0, 2, 4, 6, 8].map(p => '<line x1="2" x2="92" y1="' + yOf(bottom + p) + '" y2="' + yOf(bottom + p) + '" stroke="' + PEN_N + '" stroke-opacity="0.55" stroke-width="1"/>').join('');
  if (28 < bottom || 28 > bottom + 8) s += '<line x1="' + (x - 10) + '" x2="' + (x + 10) + '" y1="' + yOf(28) + '" y2="' + yOf(28) + '" stroke="' + PEN_N + '" stroke-width="1.3"/>';
  s += '<ellipse cx="' + x + '" cy="' + yOf(28) + '" rx="5.6" ry="4" transform="rotate(-20 ' + x + ' ' + yOf(28) + ')" fill="' + PEN_C + '"/>';
  const k = React.useContext(RefPaper) ? 0.8 : 1;
  return <svg viewBox="0 0 96 72" width={96 * k} height={72 * k} style={{display:'block',overflow:'visible'}}><ClefGlyph clef={glyph} st={glyph} yOf={yOf} ink={PEN_N}/><g dangerouslySetInnerHTML={{ __html: s }}/></svg>;
}
function RefStaff() {
  return <div>
    <RefGrandStaff/>
    <RefNote>{t('Every white key from C two octaves below middle C to C two octaves above; middle C in coral, on its own ledger line between the staves.', '가운데 C 두 옥타브 아래 C부터 두 옥타브 위 C까지의 흰건반 모두. 코랄색이 가운데 C, 두 오선 사이의 덧줄 위.')}{React.useContext(RefPaper) ? '' : t(' Tap a note to hear it.', ' 음표를 누르면 소리가 나요.')}</RefNote>
    <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'flex-end',marginTop:6}}><RefDoor room="whole-staff"/><RefDoor room="ledger-lines"/></div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(150px,1fr))',gap:6,marginTop:8}}>{REF_CLEFS.map(([id, bottom, glyph, en, ko, hen, hko, room, g]) =>
      <div key={id} data-ref-clef={id} style={{border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'6px 8px',display:'flex',flexDirection:'column',alignItems:'flex-start',gap:3,minWidth:0}}>
        <RefClefPic bottom={bottom} glyph={glyph}/>
        <b style={{fontSize:12.5,fontWeight:800,lineHeight:1.25}}>{t(en, ko)}</b>
        <span style={{fontSize:12,color:BK.muted,lineHeight:1.3}}>{t(hen, hko)}</span>
        <RefDoor room={room} g={g}/>
      </div>)}</div>
  </div>;
}

// 2. notes and rests (the beats with the crotchet as one beat, as in 2/4, 3/4 and 4/4), the breve to the hemidemisemiquaver
const REF_NOTES = [
  ['b', 0, 'breve', '겹온음표', '8', 'note-values', 'Grade 4'], ['w', 1, 'dotted semibreve', '점온음표', '6', null], ['w', 0, 'semibreve', '온음표', '4', 'note-values'],
  ['h', 1, 'dotted minim', '점2분음표', '3', 'note-values'], ['h', 0, 'minim', '2분음표', '2', 'note-values'], ['q', 1, 'dotted crotchet', '점4분음표', '1½', 'rhythm'],
  ['q', 0, 'crotchet', '4분음표', '1', 'note-values'], ['e', 1, 'dotted quaver', '점8분음표', '¾', 'rhythm-3'], ['e', 0, 'quaver', '8분음표', '½', 'note-values'],
  ['s', 0, 'semiquaver', '16분음표', '¼', 'rhythm-2'], ['d', 0, 'demi\u00adsemi\u00adquaver', '32분음표', '⅛', null], ['x', 0, 'hemi\u00addemi\u00adsemi\u00adquaver', '64분음표', '1/16', null],
];
function RefNotes() {
  const paper = React.useContext(RefPaper);
  return <div>
    <div style={{display:'grid',gridTemplateColumns:paper ? '1fr 1fr' : 'minmax(0,1fr)',gap:8,alignItems:'start'}}>{(paper ? [REF_NOTES.slice(0, 6), REF_NOTES.slice(6)] : [REF_NOTES]).map((list, li) =>
    <RefTable key={li} k="notes" cols="30px 30px minmax(0,1fr) 34px auto" head={[t('Note', '음표'), t('Rest', '쉼표'), t('Name', '이름'), t('Beats', '박'), '']}
      rows={list.map(([k, d, en, ko, b, room, g]) => [refNoteSvg(k, d), refRestSvg(k, d), <b style={{fontWeight:800}}>{t(en, ko)}</b>, <span style={{fontWeight:900,fontSize:b.length > 2 ? 12.5 : 15,whiteSpace:'nowrap'}}>{b}</span>, <RefDoor room={room} g={g}/>])}/>)}</div>
    <div style={{height:6}}/>
    <RefTable k="tuplets" cols="64px minmax(0,1fr) auto" rows={[[refTupletSvg(3), t('triplet: three in the time of two', '셋잇단음표: 둘 자리에 셋'), <RefDoor room="rhythm-2"/>], [refTupletSvg(2), t('duplet: two in the time of three', '2잇단음표: 셋 자리에 둘'), <RefDoor room="rhythm-2" g="Grade 3"/>]]}/>
    <RefNote>{t('Beats with the crotchet as one beat (2/4, 3/4, 4/4). Each plain note is half the plain note above it; a dot adds half the note’s value.', '4분음표를 한 박으로 셀 때(2/4, 3/4, 4/4)의 박. 점 없는 음표는 위의 점 없는 음표의 절반, 점은 그 음표 값의 절반을 더해요.')}</RefNote>
  </div>;
}
// 3. time signatures: the bottom number; simple, compound and irregular; a ♪ plays two bars, the strong beats louder
const REF_TS = {
  simple: [[2, 4, null, '2 crotchets', '4분음표 둘', 'time-signatures'], [3, 4, null, '3 crotchets', '4분음표 셋', 'time-signatures'], [4, 4, 'c', '4 crotchets', '4분음표 넷', 'time-signatures'],
    [2, 2, 'cut', '2 minims', '2분음표 둘', 'rhythm-3'], [3, 2, null, '3 minims', '2분음표 셋', 'rhythm-3'], [4, 2, null, '4 minims', '2분음표 넷', null], [3, 8, null, '3 quavers', '8분음표 셋', 'rhythm-3'], [3, 16, null, '3 semiquavers', '16분음표 셋', null]],
  compound: [[6, 8, null, '2 dotted crotchets', '점4분음표 둘', 'six-eight'], [9, 8, null, '3 dotted crotchets', '점4분음표 셋', 'rhythm-3'], [12, 8, null, '4 dotted crotchets', '점4분음표 넷', 'rhythm-3'],
    [6, 4, null, '2 dotted minims', '점2분음표 둘', 'rhythm-4'], [9, 4, null, '3 dotted minims', '점2분음표 셋', null], [12, 4, null, '4 dotted minims', '점2분음표 넷', null],
    [6, 16, null, '2 dotted quavers', '점8분음표 둘', null], [9, 16, null, '3 dotted quavers', '점8분음표 셋', null], [12, 16, null, '4 dotted quavers', '점8분음표 넷', null]],
  irregular: [[5, 4, null, '5 crotchets: 3 + 2 or 2 + 3', '4분음표 다섯: 3 + 2 또는 2 + 3', 'time-signatures', [3, 2]], [7, 4, null, '7 crotchets: 4 + 3 or 3 + 4', '4분음표 일곱: 4 + 3 또는 3 + 4', null, [4, 3]],
    [5, 8, null, '5 quavers: 3 + 2 or 2 + 3', '8분음표 다섯: 3 + 2 또는 2 + 3', null, [3, 2]], [7, 8, null, '7 quavers: 2 + 2 + 3 or 3 + 2 + 2', '8분음표 일곱: 2 + 2 + 3 또는 3 + 2 + 2', null, [2, 2, 3]]],
};
// two bars of clicks: accent 1 the bar's first, 0.5 each group's first, 0 the rest
function refPlayBar(acc, unit) {
  const ctx = getAudio(); if (!ctx) return; stopClicks(); const t0 = ctx.currentTime + 0.1;
  [0, 1].forEach(bar => acc.forEach((a, i) => { const at = t0 + (bar * acc.length + i) * unit;
    if (a === 1) beatTick(ctx, at, 0, 1320, 0.05, 0.4); else if (a === 0.5) beatTick(ctx, at, 1, 1040, 0.05, 0.22); else beatTick(ctx, at, 2, 880, 0.05, 0.1); }));
}
const refGroupsAcc = (groups) => groups.flatMap((g, i) => Array.from({ length: g }, (_, j) => (j ? 0 : i ? 0.5 : 1)));
function refTsHear(kind, a, b, groups) {
  if (kind === 'simple') return refPlayBar(Array.from({ length: a }, (_, i) => (i === 0 ? 1 : a === 4 && i === 2 ? 0.5 : 0)), { 2: 0.8, 4: 0.55, 8: 0.38, 16: 0.28 }[b]);
  if (kind === 'compound') return refPlayBar(refGroupsAcc(Array.from({ length: a / 3 }, () => 3)), { 4: 0.3, 8: 0.2, 16: 0.15 }[b]);
  return refPlayBar(refGroupsAcc(groups), { 4: 0.42, 8: 0.22 }[b]);
}
function RefTimeTiles({ list, kind }) {
  const paper = React.useContext(RefPaper);
  return <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(' + (paper ? 122 : 150) + 'px,1fr))',gap:6}}>{list.map(([a, b, sym, en, ko, room, groups]) => <div key={a + '/' + b} data-ref-ts={a + '/' + b}
    style={{display:'grid',gridTemplateColumns:sym ? '34px 34px 1fr' : '34px 1fr',alignItems:'center',gap:6,border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'5px 8px'}}>
    <RefTime top={a} bot={b}/>{sym && <RefTime sym={sym}/>}
    <div style={{display:'flex',flexDirection:'column',gap:3,alignItems:'flex-start',minWidth:0}}><span style={{fontSize:12.5,fontWeight:800,lineHeight:1.25}}>{t(en, ko)}</span>
      <span style={{display:'flex',gap:4,alignItems:'center',flexWrap:'wrap'}}><RefHear k={'ts' + a + '-' + b} on={() => refTsHear(kind, a, b, groups)}/><RefDoor room={room}/></span></div>
  </div>)}</div>;
}
function RefTimes() {
  return <div>
    <RefTable k="bottom" cols="40px 38px minmax(0,1fr) auto" head={[t('Bottom', '아래 숫자'), '', t('Each count is a', '세는 단위'), '']}
      rows={[[2, 'h', 'minim', '2분음표', 'rhythm-3'], [4, 'q', 'crotchet', '4분음표', 'time-signatures'], [8, 'e', 'quaver', '8분음표', 'six-eight'], [16, 's', 'semiquaver', '16분음표', null]].map(([n, k, en, ko, room]) => [<span style={{fontFamily:LB_SERIF,fontWeight:900,fontSize:20}}>{n}</span>, refNoteSvg(k), <b style={{fontWeight:800}}>{t(en, ko)}</b>, <RefDoor room={room}/>])}/>
    <RefNote>{t('The top number: how many in a bar.', '위 숫자: 한 마디에 몇 개.')}</RefNote>
    <RefLab>{t('Simple: each beat splits in two', '홑박자: 한 박이 둘로')}</RefLab><RefTimeTiles list={REF_TS.simple} kind="simple"/>
    <RefLab>{t('Compound: each beat is a dotted note and splits in three', '겹박자: 한 박이 점음표, 셋으로')}</RefLab><RefTimeTiles list={REF_TS.compound} kind="compound"/>
    <RefLab>{t('Irregular: five or seven, in uneven groups', '혼합박자: 다섯이나 일곱, 고르지 않은 묶음')}</RefLab><RefTimeTiles list={REF_TS.irregular} kind="irregular"/>
    <div style={{display:'flex',gap:6,alignItems:'center',margin:'6px 2px 0'}}><span style={{fontSize:12.5,color:BK.muted,lineHeight:1.45,flex:1,minWidth:0}}>{t('Calypso and many dances keep 4/4 but group the eight quavers 3 + 3 + 2.', '칼립소와 많은 춤곡은 4/4 그대로, 8분음표 여덟을 3 + 3 + 2로 묶어요.')}</span>
      <RefHear k="ts-calypso" on={() => refPlayBar(refGroupsAcc([3, 3, 2]), 0.2)}/><RefDoor room={null}/></div>
  </div>;
}
// 4. keys: the order of the signs, every key with its relative minor, where the house first meets it (the scales rooms' key
// lists, Key Signatures, Minor Scales, Keys and Intervals 4 and 5)
const REF_KEYS = [
  ['C', 'A', 0, null, 'scales', 'scales'], ['G', 'E', 1, 'sharp', 'scales', 'scales'], ['D', 'B', 2, 'sharp', 'key-signatures', 'scales-23'], ['A', 'F♯', 3, 'sharp', 'scales-3', 'scales-3'],
  ['E', 'C♯', 4, 'sharp', 'scales-4', 'scales-4'], ['B', 'G♯', 5, 'sharp', 'keys-4', 'scales-5'], ['F♯', 'D♯', 6, 'sharp', 'keys-4', 'keys-5'], ['C♯', 'A♯', 7, 'sharp', 'keys-5', 'keys-5'],
  ['F', 'D', 1, 'flat', 'scales', 'minor-scales'], ['B♭', 'G', 2, 'flat', 'key-signatures', 'minor-scales'], ['E♭', 'C', 3, 'flat', 'scales-3', 'scales-3'], ['A♭', 'F', 4, 'flat', 'scales-4', 'scales-4'],
  ['D♭', 'B♭', 5, 'flat', 'keys-4', 'keys-4'], ['G♭', 'E♭', 6, 'flat', 'keys-4', 'keys-5'], ['C♭', 'A♭', 7, 'flat', 'keys-5', 'keys-5'],
];
const refMaj = (k) => t(k + ' major', k + '장조'), refMin = (k) => t(k + ' minor', k + '단조');
function RefKeys() {
  const paper = React.useContext(RefPaper);
  // the letters under each sign, at KSStaff's own x (56 + 15 a sign)
  const order = (type, letters) => <div style={{maxWidth:221}}>
    <KSStaff count={7} type={type} width={170} zoom={1.3}/>
    <svg viewBox="0 0 170 16" style={{width:'100%',display:'block'}}>{letters.split(' ').map((l, i) => <text key={i} x={56 + i * 15} y="12" textAnchor="middle" fontSize="12" fontWeight="900" fontFamily="Georgia, serif" fill={PEN_N}>{l}</text>)}</svg></div>;
  return <div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(210px,1fr))',gap:8,margin:'0 0 6px'}}>
      <div>{order('sharp', 'F C G D A E B')}<RefNote>{t('Sharps, always in this order. The key note is a semitone above the last sharp.', '샵은 언제나 이 순서. 마지막 샵에서 반음 위가 으뜸음.')}</RefNote></div>
      <div>{order('flat', 'B E A D G C F')}<RefNote>{t('Flats, always in this order. From two flats, the second-last flat names the key (one flat: F major).', '플랫은 언제나 이 순서. 플랫 둘부터는 끝에서 두 번째 플랫이 조 이름(플랫 하나: F장조).')}</RefNote></div>
    </div>
    <div style={{display:'grid',gridTemplateColumns:paper ? '1fr 1fr' : 'minmax(0,1fr)',gap:8,alignItems:'start'}}>{(paper ? [REF_KEYS.slice(0, 8), REF_KEYS.slice(8)] : [REF_KEYS]).map((list, li) =>
    <RefTable key={li} k="keys" cols="minmax(0,1fr) 104px auto" head={[t('Major · relative minor', '장조 · 나란한조'), t('Signature', '조표'), '']}
      rows={list.map(([M, m, n, type, rM, rm]) => [<span style={{whiteSpace:'nowrap'}}><b style={{fontWeight:800}}>{refMaj(M)}</b> <span style={{fontWeight:900,color:BK.coral}}>{n ? n + (type === 'sharp' ? '♯' : '♭') : ''}</span><br/><span style={{color:BK.muted,fontWeight:700}}>{refMin(m)}</span></span>,
        <div style={{width:104}}>{n ? <KSStaff count={n} type={type} width={170} zoom={0.62}/> : <KSStaff count={0} type="sharp" width={170} zoom={0.62}/>}</div>,
        <div style={{display:'flex',flexDirection:'column',gap:3,alignItems:'flex-end'}}><RefDoor room={rM}/><RefDoor room={rm}/></div>])}/>)}</div>
    <RefNote>{t('The relative minor shares its major’s signature; its key note is three semitones lower. Same sounds, two names: B and C♭, F♯ and G♭, C♯ and D♭ major; G♯ and A♭, D♯ and E♭, A♯ and B♭ minor.', '나란한조는 장조와 조표가 같고, 으뜸음은 반음 셋 아래. 소리는 같고 이름은 둘: B와 C♭, F♯과 G♭, C♯과 D♭ 장조; G♯과 A♭, D♯과 E♭, A♯과 B♭ 단조.')}</RefNote>
  </div>;
}
// 5. scales: each form's steps counted from its notes (semitones from the key note); the Scales map, floor by floor; then
// every major and minor scale spelt out (part b), the 6th and 7th that the harmonic and melodic minor raise in coral
const REF_SCALES = [
  ['pent', 'pentatonic (the black keys)', '5음 음계(검은건반)', [0, 2, 4, 7, 9, 12], 'first-steps'],
  ['maj', 'major', '장음계', [0, 2, 4, 5, 7, 9, 11, 12], 'scales'],
  ['nat', 'natural minor', '자연 단음계', [0, 2, 3, 5, 7, 8, 10, 12], 'scale-play'],
  ['harm', 'harmonic minor', '화성 단음계', [0, 2, 3, 5, 7, 8, 11, 12], 'minor-scales'],
  ['mel', 'melodic minor, going up (down: the natural minor)', '가락 단음계, 올라갈 때(내려올 때: 자연 단음계)', [0, 2, 3, 5, 7, 9, 11, 12], 'scales-23'],
  ['chr', 'chromatic: every key', '반음계: 모든 건반', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'scales-23'],
  ['lyd', 'Lydian mode: the major with its 4th raised', '리디안 선법: 4도를 올린 장음계', [0, 2, 4, 6, 7, 9, 11, 12], 'scales-7'],
];
const refStep = (d) => d === 1 ? 'S' : d === 2 ? 'T' : d === 3 ? 'T+S' : d === 4 ? '2T' : String(d);
const REF_SC = { maj: [0, 2, 4, 5, 7, 9, 11, 12], nat: [0, 2, 3, 5, 7, 8, 10, 12], harm: [0, 2, 3, 5, 7, 8, 11, 12], mel: [0, 2, 3, 5, 7, 9, 11, 12] }, REF_ST8 = [0, 1, 2, 3, 4, 5, 6, 7], REF_ST7 = REF_ST8.slice(0, 7);
function RefAllScales() {
  const notes = (arr, hot) => <span style={{display:'flex',flexWrap:'wrap',gap:'0 6px',fontWeight:800,fontFamily:'Georgia, serif'}}>{arr.map((n, i) => <span key={i} style={{color:hot && hot.includes(i) ? BK.coral : BK.ink}}>{refNm(n)}</span>)}</span>;
  const maj = REF_KEYS.map(r => r[0]), min = REF_KEYS.map(r => r[1]), paper = React.useContext(RefPaper);
  return <div style={paper ? {display:'grid',gridTemplateColumns:'1fr 1.15fr',gap:12,alignItems:'start'} : null}><div>
    <RefLab>{t('Every major scale', '모든 장음계')}</RefLab>
    <RefTable k="allmajor" cols="62px minmax(0,1fr) auto" rows={maj.map((k, i) => { const nn = refSpell(k, REF_ST7, REF_SC.maj); return [<b style={{fontWeight:800,whiteSpace:'nowrap'}}>{refMaj(k)}</b>, <div data-ref-allscale={'M' + k}>{notes(nn)}</div>,
      <span style={{display:'flex',gap:4,alignItems:'center'}}><RefHear k={'sM' + k} on={() => playScaleNotes(refKey(k).pc, REF_SC.maj)}/><RefDoor room={REF_KEYS[i][4]}/></span>]; })}/></div><div>
    <RefLab>{t('Every minor scale: the natural minor; the harmonic raises the 7th, the melodic the 6th and 7th going up', '모든 단음계: 자연 단음계; 화성 단음계는 7음을, 가락 단음계는 올라갈 때 6음과 7음을 올려요')}</RefLab>
    <RefTable k="allminor" cols="62px minmax(0,1fr) auto" rows={min.map((k, i) => { const nat = refSpell(k, REF_ST7, REF_SC.nat), h = refSpell(k, REF_ST7, REF_SC.harm), m = refSpell(k, REF_ST7, REF_SC.mel), pc = refKey(k).pc;
      return [<b style={{fontWeight:800,whiteSpace:'nowrap'}}>{refMin(k)}</b>,
        <div data-ref-allscale={'m' + k} style={{display:'flex',flexDirection:'column',gap:2}}>{notes(nat)}<span style={{display:'flex',flexWrap:'wrap',alignItems:'center',gap:'2px 6px',fontSize:12,color:BK.muted,fontWeight:700}}>
          <span style={{display:'inline-flex',gap:4,alignItems:'center'}}>{t('harmonic', '화성')} <b style={{color:BK.coral}}>{refNm(h[6])}</b><RefHear k={'sm' + k} on={() => playScaleNotes(pc, REF_SC.harm)}/></span>
          <span style={{display:'inline-flex',gap:4,alignItems:'center'}}>{t('melodic up', '가락 ↑')} <b style={{color:BK.coral}}>{refNm(m[5])} {refNm(m[6])}</b><RefHear k={'sl' + k} on={() => playScaleNotes(pc, REF_SC.mel, REF_SC.nat)}/></span></span></div>,
        <span style={{display:'flex',gap:4,alignItems:'center'}}><RefHear k={'sn' + k} on={() => playScaleNotes(pc, REF_SC.nat)}/><RefDoor room={REF_KEYS[i][5]}/></span>]; })}/>
    <RefNote>{t('The melodic minor comes down as the natural minor.', '가락 단음계는 자연 단음계로 내려와요.')}</RefNote>
  </div></div>;
}
function RefScales({ part }) {
  const paper = React.useContext(RefPaper), [map, setMap] = useState(false), go = React.useContext(RefGo);
  if (part === 'b') return <RefAllScales/>;
  return <div>
    <RefTable k="scales" cols="minmax(0,1fr) auto" head={[t('Form · its steps (T tone, S semitone)', '형태 · 걸음(T 온음, S 반음)'), '']}
      rows={REF_SCALES.map(([id, en, ko, semis, room]) => { const steps = semis.slice(1).map((v, i) => v - semis[i]);
        return [<div data-ref-scale={id}><b style={{fontWeight:800}}>{t(en, ko)}</b><div style={{display:'flex',flexWrap:'wrap',gap:3,marginTop:3}}>{id === 'chr' ? <span style={{fontSize:12,fontWeight:800,color:BK.muted}}>{t('S × 12', 'S × 12')}</span>
          : steps.map((d, i) => <span key={i} style={{fontSize:11.5,fontWeight:900,padding:'1px 6px',borderRadius:6,border:'1.2px solid ' + (d === 1 ? BK.coral : 'rgba(38,41,107,0.35)'),color:d === 1 ? BK.coral : BK.ink}}>{refStep(d)}</span>)}</div></div>, <RefDoor room={room}/>]; })}/>
    {!paper && <div style={{margin:'8px 0 0'}}>
      <button type="button" className="ghost-btn" data-ref-scalesmap aria-expanded={map} onClick={() => setMap(x => !x)} style={{width:'100%',minHeight:44,fontSize:14}}>{map ? t('Hide the scales floor by floor', '층마다 스케일 닫기') : t('Every grade’s scales, floor by floor ›', '급마다 스케일, 층마다 ›')}</button>
      {map && <div style={{marginTop:8}}><ScalesMapView onChapter={go}/></div>}
    </div>}
    {!part && <RefAllScales/>}
  </div>;
}
// 6. intervals: by number, with the semitones in each quality; the rules
const REF_IV = [[2, [['minor', '단', 1], ['major', '장', 2]]], [3, [['minor', '단', 3], ['major', '장', 4]]], [4, [['perfect', '완전', 5], ['augmented', '증', 6]]], [5, [['diminished', '감', 6], ['perfect', '완전', 7]]],
  [6, [['minor', '단', 8], ['major', '장', 9]]], [7, [['minor', '단', 10], ['major', '장', 11]]], [8, [['perfect', '완전', 12]]]];
function RefIntervals() {
  const nm = (n) => n === 8 ? t('octave', '옥타브(8도)') : t(H3_ORD[n], H3_ORDK[n]);
  return <div>
    <RefTable k="intervals" cols="70px minmax(0,1fr)" head={[t('Number', '숫자'), t('Quality · semitones', '성질 · 반음 수')]}
      rows={REF_IV.map(([n, qs]) => [<b style={{fontFamily:LB_SERIF,fontWeight:900,fontSize:15}}>{nm(n)}</b>, <span style={{display:'flex',flexWrap:'wrap',gap:'2px 10px'}}>{qs.map(([en, ko, s]) => <span key={en}>{t(en, ko)} <b style={{fontWeight:900}}>{s}</b></span>)}</span>])}/>
    <RefTable k="ivrules" cols="minmax(0,1fr) auto" rows={[
      [t('A semitone is the very next key; a tone is two semitones.', '반음은 바로 옆 건반, 온음은 반음 둘.'), <RefDoor room="tones"/>],
      [t('Count the letters, both ends included: that is the number.', '양 끝을 포함해 글자를 세면 그게 숫자.'), <RefDoor room="intervals"/>],
      [t('Major or minor 3rd: four semitones or three.', '장3도 또는 단3도: 반음 넷 또는 셋.'), <RefDoor room="minor-scales"/>],
      [t('In a minor key (the harmonic minor), above the tonic: the 3rd and 6th minor, the 7th major.', '단조(화성 단음계)에서 으뜸음 위로: 3도·6도는 단음정, 7도는 장음정.'), <RefDoor room="harmony-2"/>],
      [t('Augmented: a semitone wider than major or perfect. Diminished: a semitone narrower than minor or perfect.', '증음정: 장·완전보다 반음 넓게. 감음정: 단·완전보다 반음 좁게.'), <RefDoor room="keys-5"/>],
      [t('Upside down: the numbers add to 9; major and minor swap, augmented and diminished swap, perfect stays perfect.', '자리바꿈: 숫자의 합은 9, 장↔단, 증↔감, 완전은 그대로.'), <RefDoor room="keys-5"/>],
    ]}/>
  </div>;
}
// 7. chords: the triad on every degree of C major (semibreves, no stems), the degree names; every kind of chord on any root
// (its notes spelt by the code, its intervals counted from the root); the positions; cadences
function RefChordStaff() {
  const base = 64, yOf = (d) => base - (d - 30) * 5, x0 = 54, dx = 40, roman = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'];
  let s = [0, 2, 4, 6, 8].map(p => '<line x1="4" x2="' + (x0 + dx * 7 - 10) + '" y1="' + (base - p * 5) + '" y2="' + (base - p * 5) + '" stroke="' + PEN_N + '" stroke-opacity="0.5" stroke-width="1.1"/>').join('');
  roman.forEach((r, i) => { const x = x0 + i * dx, root = 28 + i;
    if (root <= 28) s += '<line x1="' + (x - 11) + '" x2="' + (x + 11) + '" y1="' + yOf(28) + '" y2="' + yOf(28) + '" stroke="' + PEN_N + '" stroke-width="1.3"/>';
    [root, root + 2, root + 4].forEach(d => { s += '<ellipse cx="' + x + '" cy="' + yOf(d) + '" rx="6.2" ry="2.8" transform="rotate(-12 ' + x + ' ' + yOf(d) + ')" fill="#fff" stroke="' + PEN_N + '" stroke-width="2.9"/>'; });
    s += '<text x="' + x + '" y="' + (base + 24) + '" text-anchor="middle" font-size="15" font-weight="900" font-family="Georgia, serif" fill="' + (i === 0 || i === 3 || i === 4 ? PEN_C : PEN_N) + '">' + r + '</text>'; });
  return <svg viewBox={'0 ' + (base - 52) + ' ' + (x0 + dx * 7 - 6) + ' 84'} style={{width:'100%',maxWidth:420,display:'block',margin:'0 auto'}} role="img" aria-label={t('The triad on every degree of C major, I to vii°', 'C장조 모든 음 위의 3화음, I부터 vii°까지')}>
    <ClefGlyph clef="treble" st="treble" yOf={yOf} ink={PEN_N}/><g dangerouslySetInnerHTML={{ __html: s }}/></svg>;
}
// [id, name en, name ko, symbol after the root, letter steps, semitones, room]; the house's own names (SEVENTH_TYPES)
const REF_CHORDS = [
  ['maj', 'major', '장3화음', '', [0, 2, 4], [0, 4, 7], 'chords'], ['min', 'minor', '단3화음', 'm', [0, 2, 4], [0, 3, 7], 'chords'],
  ['dim', 'diminished', '감3화음', '°', [0, 2, 4], [0, 3, 6], 'harmony-5'], ['aug', 'augmented', '증3화음', '+', [0, 2, 4], [0, 4, 8], 'listen-8'],
  ['dom7', 'dominant 7th', '딸림7화음', '7', [0, 2, 4, 6], [0, 4, 7, 10], 'harmony-6'], ['maj7', 'major 7th', '장7화음', 'maj7', [0, 2, 4, 6], [0, 4, 7, 11], 'chords'],
  ['min7', 'minor 7th', '단7화음', 'm7', [0, 2, 4, 6], [0, 3, 7, 10], 'chords'], ['hdim7', 'half-diminished', '반감7화음', 'm7♭5', [0, 2, 4, 6], [0, 3, 6, 10], 'chords'],
  ['dim7', 'diminished 7th', '감7화음', '°7', [0, 2, 4, 6], [0, 3, 6, 9], 'arps-6'], ['six', 'major 6th (added 6th)', '부가6화음', '6', [0, 2, 4, 5], [0, 4, 7, 9], null],
  ['min6', 'minor 6th', '단 부가6화음', 'm6', [0, 2, 4, 5], [0, 3, 7, 9], null],
];
const REF_ROOTS = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'];
// an interval's name from its letter steps and semitones: 'M3', 'P5', 'm7', 'd5', 'A5'
const refIvName = (st, se) => { const base = REF_NATPC[st], perf = [0, 3, 4].includes(st), d = se - base;
  const q = perf ? (d === 0 ? 'P' : d === 1 ? 'A' : d === -1 ? 'd' : '?') : (d === 0 ? 'M' : d === -1 ? 'm' : d === 1 ? 'A' : d === -2 ? 'd' : '?'); return q + (st + 1); };
const REF_IVQ_KO = { P: '완전', M: '장', m: '단', A: '증', d: '감' };
function RefChordKinds() {
  const paper = React.useContext(RefPaper), [root, setRoot] = useState('C'), r = paper ? 'C' : root, pc = refKey(r).pc;
  return <div data-ref-chordkinds>
    {!paper && <div style={{display:'flex',flexWrap:'wrap',gap:4,margin:'0 0 6px'}}>{REF_ROOTS.map(x => <button key={x} type="button" className={'chip' + (x === root ? ' active' : '')} data-ref-root={x} onClick={() => setRoot(x)} style={{minHeight:32,minWidth:38,padding:'2px 8px',fontSize:13,fontWeight:900}}>{x}</button>)}</div>}
    <RefTable k="chordtypes" cols="minmax(0,1fr) minmax(0,1.1fr) auto" head={[t('Chord · symbol', '화음 · 기호'), t('From the root · on ', '근음에서 · ') + r, '']}
      rows={REF_CHORDS.map(([id, en, ko, sym, st, se, room]) => { const nn = refSpell(r, st, se), ivs = st.slice(1).map((x, i) => refIvName(x, se[i + 1]));
        return [<span data-ref-chord={id}><b style={{fontWeight:800}}>{t(en, ko)}</b> <span style={{fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{r}{sym}</span></span>,
          <span style={{display:'flex',flexDirection:'column',gap:1}}><span style={{fontSize:12,color:BK.muted,fontWeight:700}}>{ivs.map(v => LANG === 'ko' ? REF_IVQ_KO[v[0]] + v.slice(1) + '도' : v).join(' · ')}</span>
            <span style={{display:'flex',gap:'0 6px',flexWrap:'wrap',fontWeight:800,fontFamily:'Georgia, serif'}}>{nn.map((n, i) => refNm(n, i))}</span></span>,
          <span style={{display:'flex',gap:4,alignItems:'center'}}><RefHear k={'ch' + id} on={() => refPlayNotes(se.map(x => refRoot(pc) + x))}/><RefDoor room={room}/></span>]; })}/>
    <RefNote>{t('M major, m minor, P perfect, A augmented, d diminished: each counted from the root.', 'M 장, m 단, P 완전, A 증, d 감: 모두 근음에서 센 음정.')}{paper ? ' ' + t('Shown on C.', 'C 위에서.') : ''}</RefNote>
  </div>;
}
function RefChords({ part }) {
  const rm = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'], q = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished'], qk = { major: '장', minor: '단', diminished: '감' };
  return <div>
    {part !== 'b' && <><RefChordStaff/>
    <RefTable k="degrees" cols="44px minmax(0,1fr) auto" head={[t('Degree', '음'), t('Name · its triad in a major key', '이름 · 장조에서의 3화음'), '']}
      rows={rm.map((r, i) => [<b style={{fontFamily:LB_SERIF,fontWeight:900,fontSize:15,color:i === 0 || i === 3 || i === 4 ? BK.coral : BK.ink}}>{r}</b>, <span><b style={{fontWeight:800}}>{t(DEGREE_NAMES[i], DEGREE_NAMES_KO[i])}</b> · {t(q[i], qk[q[i]] + '3화음')}</span>, i === 0 ? <RefDoor room="harmony-3"/> : <span/>])}/>
    <div style={{height:8}}/>
    <RefTable k="chordpos" cols="minmax(0,1fr) auto" rows={[
      [t('I, IV and V: the primary triads.', 'I, IV, V: 주요 3화음.'), <RefDoor room="chords"/>],
      [t('Root position (a), first inversion (b): the 3rd in the bass.', '기본 위치(a), 첫째 자리바꿈(b): 3음이 베이스.'), <RefDoor room="harmony-3"/>],
      [t('Second inversion (c): the 5th in the bass; Ic before V is the cadential 6-4.', '둘째 자리바꿈(c): 5음이 베이스; V 앞의 Ic가 종지 6-4.'), <RefDoor room="harmony-5"/>],
      [t('Dominant 7th (V7): four positions, a b c d.', '딸림7화음(V7): 네 자리 a b c d.'), <RefDoor room="harmony-6"/>],
      [t('Diminished 7th of a key: it starts on the key’s leading note.', '조의 감7화음: 그 조의 이끎음에서 시작.'), <RefDoor room="arps-6"/>],
    ]}/>
    <div style={{height:8}}/>
    <RefTable k="cadences" cols="minmax(0,1fr) 58px auto" head={[t('Cadence', '종지'), '', '']} rows={[   // the rooms' own words (Chords and Cadences, Grade 4)
      [<span><b style={{fontWeight:800}}>{t('perfect', '정격종지')}</b> · {t('a full stop', '마침표(.)')}</span>, <b style={{fontFamily:LB_SERIF}}>V – I</b>, <RefDoor room="harmony-3"/>],
      [<span><b style={{fontWeight:800}}>{t('plagal', '변격종지')}</b> · {t('the “Amen”', '“아멘”')}</span>, <b style={{fontFamily:LB_SERIF}}>IV – I</b>, <RefDoor room="harmony-3"/>],
      [<span><b style={{fontWeight:800}}>{t('imperfect', '반종지')}</b> · {t('a comma', '쉼표(,)')}</span>, <b style={{fontFamily:LB_SERIF}}>… – V</b>, <RefDoor room="harmony-4"/>],
      [<span><b style={{fontWeight:800}}>{t('interrupted', '거짓종지')}</b> · {t('the surprise', '깜짝')}</span>, <b style={{fontFamily:LB_SERIF}}>V – vi</b>, <RefDoor room="harmony-4"/>],
    ]}/></>}
    {part !== 'a' && <><RefLab>{t('Every kind of chord, on any root', '모든 화음, 어느 근음에서든')}</RefLab><RefChordKinds/></>}
  </div>;
}
// 8. signs: a picture of each (the book's visual index, drawn with the house's pens), its name, the room; ♪ the room's sound
const refHead = (x, y, fill = PEN_N) => '<ellipse cx="' + x + '" cy="' + y + '" rx="5.6" ry="4" transform="rotate(-20 ' + x + ' ' + y + ')" fill="' + fill + '"/>';
const refStemUp = (x, y, h = 26) => '<line x1="' + (x + 5.1) + '" x2="' + (x + 5.1) + '" y1="' + y + '" y2="' + (y - h) + '" stroke="' + PEN_N + '" stroke-width="1.6"/>';
const refLn = (x1, y1, x2, y2, w = 1.3, op) => '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + PEN_N + '" stroke-width="' + w + '"' + (op ? ' stroke-opacity="' + op + '"' : '') + ' stroke-linecap="round"/>';
const refTx = (s, x, y, size = 20, o = {}) => '<text x="' + x + '" y="' + y + '" text-anchor="' + (o.a || 'middle') + '" font-size="' + size + '" font-weight="' + (o.w || 900) + '"' + (o.it === false ? '' : ' font-style="italic"') + ' font-family="' + (o.f || 'Georgia, serif') + '" fill="' + (o.c || PEN_N) + '">' + s + '</text>';
const refStaff5 = (y0 = 10, gap = 8, a = 6, b = 58) => [0, 1, 2, 3, 4].map(i => refLn(a, y0 + i * gap, b, y0 + i * gap, 1, 0.5)).join('');
const REF_MUS = MUSIC_FONT.replace(/'/g, '&apos;');
function refSignSvg(id) {
  const P = PEN_N, dynTx = (s) => refTx(s, 32, 32, 25);
  const small = (cx, cy, slash) => '<ellipse cx="' + cx + '" cy="' + cy + '" rx="3.6" ry="2.7" transform="rotate(-20 ' + cx + ' ' + cy + ')" fill="' + P + '"/>' + refLn(cx + 3.3, cy, cx + 3.3, cy - 14, 1.1) + '<path d="M' + (cx + 3.3) + ' ' + (cy - 14) + ' c1 4 6 5 4 11" fill="none" stroke="' + P + '" stroke-width="1.2"/>' + (slash ? refLn(cx - 3, cy - 4, cx + 8, cy - 13, 1.2) : '');
  const big = (cx, cy) => refHead(cx, cy) + refStemUp(cx, cy, 24);
  switch (id) {
    case 'bar': return refStaff5() + refLn(32, 10, 32, 42, 1.4);
    case 'dbar': return refStaff5() + refLn(29, 10, 29, 42, 1.3) + refLn(35, 10, 35, 42, 1.3);
    case 'fbar': return refStaff5(10, 8, 6, 46) + refLn(41, 10, 41, 42, 1.3) + '<rect x="45" y="10" width="4.5" height="32" fill="' + P + '"/>';
    case 'repeat': return refStaff5() + '<rect x="6" y="10" width="4" height="32" fill="' + P + '"/>' + refLn(13.5, 10, 13.5, 42, 1.2) + '<circle cx="18" cy="22" r="2" fill="' + P + '"/><circle cx="18" cy="30" r="2" fill="' + P + '"/>'
      + '<circle cx="46" cy="22" r="2" fill="' + P + '"/><circle cx="46" cy="30" r="2" fill="' + P + '"/>' + refLn(50.5, 10, 50.5, 42, 1.2) + '<rect x="54" y="10" width="4" height="32" fill="' + P + '"/>';
    case 'volta': return refStaff5(18, 6) + '<path d="M6 16 V4 H30 V16 M34 16 V4 H58" fill="none" stroke="' + P + '" stroke-width="1.3"/>' + refTx('1.', 9, 13, 10, { a: 'start', it: false }) + refTx('2.', 37, 13, 10, { a: 'start', it: false });
    case 'brace': return [0, 1, 2, 3, 4].map(i => refLn(18, 4 + i * 4, 58, 4 + i * 4, 1, 0.5) + refLn(18, 30 + i * 4, 58, 30 + i * 4, 1, 0.5)).join('') + refLn(18, 4, 18, 46, 1.2)
      + '<path d="M14 4 C8 9 13 19 8 25 C13 31 8 41 14 46" fill="none" stroke="' + P + '" stroke-width="2.2" stroke-linecap="round"/>';
    case 'ledger': return refStaff5(22, 6) + refLn(24, 16, 40, 16, 1.3) + refLn(24, 10, 40, 10, 1.3) + refHead(32, 10);
    case 'sharp': case 'flat': case 'natural': case 'dsharp': case 'dflat':
      return '<text x="32" y="' + (id === 'dsharp' ? 38 : 36) + '" text-anchor="middle" font-size="' + (id === 'dsharp' ? 44 : 32) + '" font-family="' + REF_MUS + '" fill="' + P + '">' + { sharp: '♯', flat: '♭', natural: '♮', dsharp: '𝄪', dflat: '𝄫' }[id] + '</text>';
    case 'pp': case 'p': case 'mp': case 'mf': case 'f': case 'ff': case 'fp': return dynTx(id);
    case 'sf': return dynTx('sfz');
    case 'cresc': return '<path d="M56 16 L8 25 L56 34" fill="none" stroke="' + P + '" stroke-width="1.6" stroke-linejoin="round"/>';
    case 'dim': return '<path d="M8 16 L56 25 L8 34" fill="none" stroke="' + P + '" stroke-width="1.6" stroke-linejoin="round"/>';
    case 'stacc': return refHead(30, 30) + refStemUp(30, 30) + '<circle cx="30" cy="41" r="2.3" fill="' + P + '"/>';
    case 'ten': return refHead(30, 30) + refStemUp(30, 30) + refLn(23, 41, 37, 41, 2);
    case 'accent': return refHead(30, 30) + refStemUp(30, 30) + '<path d="M22 37 L38 41.5 L22 46" fill="none" stroke="' + P + '" stroke-width="1.6" stroke-linejoin="round"/>';
    case 'slur': return refHead(16, 34) + refHead(46, 26) + '<path d="M14 26 Q30 8 46 18" fill="none" stroke="' + P + '" stroke-width="1.6"/>';
    case 'tie': return refHead(16, 30) + refHead(46, 30) + '<path d="M18 38 Q31 47 44 38" fill="none" stroke="' + P + '" stroke-width="1.6"/>';
    case 'fermata': return '<path d="M12 34 C14 10 50 10 52 34" fill="none" stroke="' + P + '" stroke-width="2.6" stroke-linecap="round"/><circle cx="32" cy="30" r="3" fill="' + P + '"/>';
    case 'arp': return [16, 26, 36].map(y => refHead(40, y)) + '<path d="M24 6 q3 3 0 6 t0 6 t0 6 t0 6 t0 6 t0 6 t0 6" fill="none" stroke="' + P + '" stroke-width="1.6"/>';
    case 'gliss': return refHead(12, 38) + refHead(52, 12) + refLn(18, 35, 46, 15, 1.4) + refTx('gliss.', 34, 36, 9.5, { w: 700 });
    case 'trill': return refTx('tr', 18, 30, 17) + '<path d="M28 25 q3 -5 6 0 t6 0 t6 0 t6 0" fill="none" stroke="' + P + '" stroke-width="1.6"/>';
    case 'turn': case 'iturn': { const x = 32, y = 26; return '<path d="M' + (x - 11) + ',' + (y - 1) + ' c0,-7 7,-7 9,-2 c2,5 4,6 4,6 c2,5 9,5 9,-2 M' + (x - 11) + ',' + (y - 1) + ' c0,4 4,5 6,2 M' + (x + 11) + ',' + (y - 1) + ' c0,-4 -4,-5 -6,-2" fill="none" stroke="' + P + '" stroke-width="1.8"/>' + (id === 'iturn' ? refLn(x, y - 12, x, y + 10, 1.6) : ''); }
    case 'mord': case 'lmord': { const x = 32, y = 28; return '<path d="M' + (x - 10) + ',' + y + ' l4,-6 l4,6 l4,-6 l4,6 l4,-6" fill="none" stroke="' + P + '" stroke-width="2" stroke-linejoin="round"/>' + (id === 'lmord' ? refLn(x, y - 11, x, y + 5, 1.6) : ''); }
    case 'acc': return small(20, 30, true) + big(40, 34);
    case 'app': return small(20, 30, false) + big(40, 34);
    case 'dc': return refTx('D.C.', 32, 31, 17);
    case 'ds': return refTx('D.S.', 32, 31, 17);
    case 'fine': return refTx('Fine', 32, 31, 17);
    case 'segno': return '<text x="32" y="36" text-anchor="middle" font-size="32" font-family="' + REF_MUS + '" fill="' + P + '">𝄋</text>';
    case 'coda': return '<ellipse cx="32" cy="24" rx="8" ry="11" fill="none" stroke="' + P + '" stroke-width="2.6"/>' + refLn(32, 8, 32, 40, 1.4) + refLn(18, 24, 46, 24, 1.4);
    case '8va': return refTx('8va', 6, 24, 14, { a: 'start' }) + '<path d="M28 19 H56 V26" fill="none" stroke="' + P + '" stroke-width="1.3" stroke-dasharray="3 3"/>';
    case '8vb': return refTx('8vb', 6, 34, 14, { a: 'start' }) + '<path d="M28 29 H56 V22" fill="none" stroke="' + P + '" stroke-width="1.3" stroke-dasharray="3 3"/>';
    case 'ped': return refTx('Ped.', 6, 30, 15, { a: 'start', w: 800 }) + refTx('✱', 52, 31, 15, { it: false });
    case 'pedline': return '<path d="M6 16 V32 H28 L33 24 L38 32 H58 V16" fill="none" stroke="' + P + '" stroke-width="1.5" stroke-linejoin="round"/>';
    case 'unacorda': return refTx('una corda', 32, 30, 12.5, { w: 800 });
    case 'metro': return refHead(14, 34) + refStemUp(14, 34) + refTx('= 60', 40, 38, 14, { it: false });
    default: return '';
  }
}
// [id, name en, name ko, room (null: the house doesn't teach it), grade label, sound]
const REF_SIGNS = [
  ['lines', 'Lines and bars', '선과 마디', [['bar', 'bar line', '세로줄', 'pulse'], ['dbar', 'double bar line: a new section', '겹세로줄: 새 부분', 'time-signatures'], ['fbar', 'final bar line: the end', '끝세로줄: 끝', 'time-signatures'],
    ['repeat', 'repeat signs', '도돌이표', 'signs'], ['volta', '1st and 2nd time bars', '1번·2번 괄호', 'signs'], ['brace', 'brace: the grand staff', '중괄호: 큰보표', 'staff'], ['ledger', 'ledger lines', '덧줄', 'ledger-lines']]],
  ['acc', 'Sharps and flats', '샵과 플랫', [['sharp', 'sharp: a semitone higher', '샵: 반음 위로', 'tones'], ['flat', 'flat: a semitone lower', '플랫: 반음 아래로', 'tones'], ['natural', 'natural: cancels the sharp or flat', '내추럴: 샵·플랫을 취소', 'accidentals'],
    ['dsharp', 'double sharp: two semitones higher', '겹샵: 반음 둘 위로', 'tones', 'Grade 4'], ['dflat', 'double flat: two semitones lower', '겹플랫: 반음 둘 아래로', 'tones', 'Grade 4']]],
  ['dyn', 'Loud and soft', '셈여림', [['pp', 'pianissimo: very soft', '피아니시모: 매우 여리게', 'dynamics'], ['p', 'piano: soft', '피아노: 여리게', 'dynamics'], ['mp', 'mezzo piano: moderately soft', '메조 피아노: 조금 여리게', 'dynamics'],
    ['mf', 'mezzo forte: moderately loud', '메조 포르테: 조금 세게', 'dynamics'], ['f', 'forte: loud', '포르테: 세게', 'dynamics'], ['ff', 'fortissimo: very loud', '포르티시모: 매우 세게', 'dynamics'],
    ['fp', 'forte-piano: loud, then at once soft', '포르테피아노: 세게, 곧바로 여리게', 'terms', 'Grade 3'], ['sf', 'sforzando: a strong accent', '스포르찬도: 강한 악센트', 'terms', 'Grade 3'],
    ['cresc', 'crescendo: getting louder', '크레셴도: 점점 세게', 'dynamics'], ['dim', 'diminuendo: getting softer', '디미누엔도: 점점 여리게', 'dynamics']]],
  ['touch', 'Touch', '터치', [['stacc', 'staccato: short, detached', '스타카토: 짧게 끊어서', 'dynamics'], ['ten', 'tenuto: held, full length', '테누토: 길이를 꽉 채워', 'terms', 'Grade 4'], ['accent', 'accent: stronger', '악센트: 더 강하게', 'dynamics'],
    ['slur', 'slur: smooth, joined', '이음줄: 부드럽게 이어서', 'dynamics'], ['tie', 'tie: one note, held for both', '붙임줄: 한 음을 둘 길이만큼', 'note-values'], ['fermata', 'pause (fermata): hold it longer', '늘임표(페르마타): 더 길게', 'signs'],
    ['arp', 'spread chord: bottom to top', '펼침화음: 아래에서 위로', null], ['gliss', 'glissando: slide across the keys', '글리산도: 건반 위로 미끄러지듯', null]]],
  ['orn', 'Ornaments', '꾸밈음', [['trill', 'trill', '트릴', 'signs', 'Grade 4'], ['turn', 'turn', '턴', 'signs', 'Grade 4'], ['iturn', 'inverted turn: below first', '뒤집힌 턴: 아래부터', null], ['mord', 'upper mordent', '모르덴트 (위)', 'signs', 'Grade 4'], ['lmord', 'lower mordent', '모르덴트 (아래)', 'signs', 'Grade 4'],
    ['acc', 'acciaccatura: crushed in', '아치아카투라: 짧게 끼워서', 'signs', 'Grade 4'], ['app', 'appoggiatura: leaning', '아포자투라: 기대어서', 'signs', 'Grade 4']]],
  ['road', 'Finding your way', '길 찾기', [['dc', 'da capo: from the beginning', '다 카포: 처음부터', 'signs'], ['ds', 'dal segno: from the sign', '달 세뇨: 표시부터', 'signs'], ['segno', 'segno: the sign', '세뇨: 그 표시', 'signs'],
    ['coda', 'coda: the ending', '코다: 끝맺는 부분', 'signs'], ['fine', 'fine: the end', '피네: 끝', 'signs'], ['8va', '8va: an octave higher', '8va: 한 옥타브 높게', 'signs'], ['8vb', '8vb: an octave lower', '8vb: 한 옥타브 낮게', 'signs']]],
  ['ped', 'Pedals and speed', '페달과 빠르기', [['ped', 'sustain pedal: down, then up (✱)', '댐퍼 페달: 밟고, 떼기(✱)', 'dynamics'], ['pedline', 'pedal line: down, change, up', '페달 선: 밟고, 바꾸고, 떼기', 'dynamics'],
    ['unacorda', 'una corda: the soft pedal', '우나 코르다: 약음 페달', 'terms', 'Grade 3'], ['metro', 'metronome mark: crotchet beats per minute', '메트로놈 표: 1분에 4분음표 몇 박', 'tempo']]],
];
const REF_SIGN_ORN = { trill: 'trill', turn: 'turn', mord: 'mordent', lmord: 'lower', acc: 'acc', app: 'app' };
function refSignSound(id) {
  const dy = DYNAMICS.find(x => x.id === id); if (dy) return () => playDyn(dy.vol);
  if (id === 'fp') return () => playChange('fp'); if (id === 'sf') return () => playChange('sfz');
  if (id === 'cresc' || id === 'dim') return () => playChange(id);
  const ar = { stacc: 'dot', ten: 'tenuto', accent: 'accent', slur: 'slur', fermata: 'fermata' }[id]; if (ar) return () => playArtic(ar);
  if (id === 'tie') return () => refPlayNotes([67], 0, false, 1.4);
  if (REF_SIGN_ORN[id]) return () => playOrnament(ORNAMENTS.find(o => o.id === REF_SIGN_ORN[id]));
  if (id === 'iturn') return () => refPlayNotes([65, 67, 69, 67], 0.16, false, 0.2);
  if (id === 'arp') return () => refPlayNotes([55, 60, 64, 67, 72], 0.07, false, 1.4);
  if (id === 'gliss') return () => refPlayNotes([60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84], 0.045, false, 0.18);
  if (id === 'metro') return () => { const ctx = getAudio(); if (!ctx) return; stopClicks(); const t0 = ctx.currentTime + 0.08; for (let i = 0; i < 4; i++) metroClick(ctx, t0 + i, i === 0, i === 0 ? 0.3 : 0.18); };
  return null;
}
function RefSigns() {
  const paper = React.useContext(RefPaper), k = paper ? 0.62 : 1;
  return <div data-ref-signs>{REF_SIGNS.map(([gid, gen, gko, list]) => <div key={gid}>
    <RefLab>{t(gen, gko)}</RefLab>
    <div style={{display:'grid',gridTemplateColumns:paper ? 'repeat(4,minmax(0,1fr))' : 'repeat(auto-fill,minmax(112px,1fr))',gap:paper ? 4 : 5}}>{list.map(([id, en, ko, room, g]) => { const snd = refSignSound(id);
      if (paper) return <div key={id} data-ref-sign={id} style={{border:'1.2px solid rgba(38,41,107,0.22)',borderRadius:8,background:'#fff',padding:'3px 6px',display:'grid',gridTemplateColumns:'42px minmax(0,1fr)',gap:6,alignItems:'center'}}>
        <svg viewBox="0 0 64 48" width={64 * k} height={48 * k} style={{display:'block',overflow:'visible'}} dangerouslySetInnerHTML={{ __html: refSignSvg(id) }}/>
        <span style={{fontSize:10,fontWeight:800,lineHeight:1.2}}>{t(en, ko)}<br/><RefDoor room={room} g={g}/></span></div>;
      return <div key={id} data-ref-sign={id} style={{border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'5px 7px',display:'flex',flexDirection:'column',gap:3,minWidth:0}}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:4}}><svg viewBox="0 0 64 48" width={64 * k} height={48 * k} style={{display:'block',overflow:'visible',flex:'0 0 auto'}} dangerouslySetInnerHTML={{ __html: refSignSvg(id) }}/>{snd && <RefHear k={'sg' + id} on={snd}/>}</div>
        <span style={{fontSize:11.5,fontWeight:800,lineHeight:1.25,minHeight:paper ? 0 : 29}}>{t(en, ko)}</span>
        <span style={{display:'flex',justifyContent:'flex-end'}}><RefDoor room={room} g={g}/></span>
      </div>; })}</div>
  </div>)}</div>;
}
// 9. words for how to play: the terms room's 96 (its own meanings, grades and sounds) and the book's others, by what they do;
// speed from slow to fast by the house's own beats a minute
const REF_JOBS = [['speed', 'Speed, slow to fast', '빠르기, 느림에서 빠름으로'], ['change', 'Changing speed', '빠르기 바꾸기'], ['loud', 'Loud and soft', '셈여림'], ['mood', 'Mood and character', '분위기와 성격'],
  ['touch', 'Touch and sound', '터치와 소리'], ['way', 'Finding your way in the score', '악보에서 길 찾기'], ['little', 'Little words', '덧붙이는 말'], ['others', 'For other players and groups', '다른 악기와 합주에서']];
const REF_JOB_OF = { Legato: 'touch', Staccato: 'touch', 'Mezzo staccato': 'touch', Sostenuto: 'touch', Leggiero: 'touch', 'Ben marcato': 'touch', Cantabile: 'touch', Cantando: 'touch', Tenuto: 'touch',
  Portamento: 'touch', 'Una corda': 'touch', 'Tre corde': 'touch', 'Sotto voce': 'loud', Sempre: 'little', Poco: 'little', Molto: 'little', Senza: 'little', Assai: 'little', Quasi: 'little', Subito: 'little',
  'Non troppo': 'little', 'Dal segno': 'way', 'Da capo al fine': 'way', Attacca: 'way', 'Main droite': 'way', 'Main gauche': 'way', Loco: 'way', Opus: 'way', 'M.M.': 'way', 'Ad libitum': 'change' };
const REF_JOB_CAT = { Speed: 'speed', 'Changing speed': 'change', Volume: 'loud', Strings: 'others', Other: 'mood' };
// where the house teaches a word first, before the terms room (Speed in Tempo, loud and soft and the touches in Dynamics, the
// road signs in Signs)
const REF_FIRST = { Adagio: 'tempo', Andante: 'tempo', Moderato: 'tempo', Allegretto: 'tempo', Allegro: 'tempo', Presto: 'tempo', Pianissimo: 'dynamics', Piano: 'dynamics', 'Mezzo piano': 'dynamics',
  'Mezzo forte': 'dynamics', Forte: 'dynamics', Fortissimo: 'dynamics', Crescendo: 'dynamics', Diminuendo: 'dynamics', Decrescendo: 'dynamics', Legato: 'dynamics', Staccato: 'dynamics',
  'Dal segno': 'signs', 'Da capo al fine': 'signs' };
// the book's other words (its pp. 240-241), in my words: [term, abbr, meaning en, meaning ko, job, language ('fr' 'de'), sort (speed)]
const REF_MORE_WORDS = [
  ['Adagietto', '', 'fairly slow, a little faster than adagio', '조금 느리게, 아다지오보다 조금 빠르게', 'speed', '', 66], ['Lent', '', 'slow', '느리게', 'speed', 'fr'], ['Langsam', '', 'slow', '느리게', 'speed', 'de'],
  ['Modéré', '', 'at a moderate speed', '보통 빠르기로', 'speed', 'fr'], ['Vite', '', 'fast', '빠르게', 'speed', 'fr'], ['Schnell', '', 'fast', '빠르게', 'speed', 'de'], ['Veloce', '', 'swift, nimble', '날쌔게', 'speed'],
  ['Animando', '', 'getting more lively', '점점 활기 있게', 'change'], ['Stretto', '', 'pressing on, faster', '몰아가며 빠르게', 'change'], ['A piacere', '', 'as you please: free in time', '마음대로: 박을 자유롭게', 'change'],
  ['Liberamente', '', 'freely', '자유롭게', 'change'], ['Come prima', '', 'as at first', '처음처럼', 'change'], ['Rigoroso', '', 'in strict time', '박자를 엄격하게 지켜', 'change'],
  ['Senza misura', '', 'without strict time', '박에 매이지 않고', 'change'], ['Ralentir', '', 'slow down', '느려지게', 'change', 'fr'], ['En retenant', '', 'holding back', '조금씩 늦추며', 'change', 'fr'],
  ['Retenu', '', 'held back', '늦추어', 'change', 'fr'], ['Au mouvement', '', 'back to the first speed (a tempo)', '원래 빠르기로(a tempo)', 'change', 'fr'],
  ['Mezza voce', '', 'half voice: quietly', '목소리를 반쯤 줄여: 조용히', 'loud'],
  ['Affettuoso', '', 'tenderly', '다정하게', 'mood'], ['Amabile', '', 'lovingly, pleasantly', '사랑스럽게', 'mood'], ['Appassionato', '', 'with passion', '열정적으로', 'mood'], ['Con bravura', '', 'brilliantly, showing skill', '화려하게, 솜씨를 뽐내며', 'mood'],
  ['Calmato', '', 'calmed', '가라앉혀 고요하게', 'mood'], ['Capriccioso', '', 'fanciful, unpredictable', '변덕스럽게', 'mood'], ['Deciso', '', 'decisively', '단호하게', 'mood'], ['Energico', '', 'with energy', '힘차게', 'mood'],
  ['Espressivo', 'espress.', 'with expression', '표정 있게', 'mood'], ['Furioso', '', 'furiously', '격렬하게', 'mood'], ['Grandioso', '', 'grandly', '웅대하게', 'mood'], ['Lacrimoso', '', 'tearfully', '눈물 젖은 듯', 'mood'],
  ['Lamentoso', '', 'mournfully', '애통하게', 'mood'], ['Mesto', '', 'sad', '슬프게', 'mood'], ['Misterioso', '', 'mysteriously', '신비롭게', 'mood'], ['Nobilmente', '', 'nobly', '고귀하게', 'mood'],
  ['Spiritoso', '', 'with spirit', '생기 있게', 'mood'], ['Vigoroso', '', 'vigorously', '활발하고 힘차게', 'mood'], ['Alla marcia', '', 'like a march', '행진곡풍으로', 'mood'], ['Ritmico', '', 'rhythmically', '리듬을 살려', 'mood'],
  ['Joyeux', '', 'joyful', '즐겁게', 'mood', 'fr'], ['Doux, douce', '', 'soft and sweet', '부드럽고 달콤하게', 'mood', 'fr'],
  ['Marcato', 'marc.', 'marked, each note stressed', '또렷하게, 음마다 힘을 주어', 'touch'], ['Martellato', '', 'hammered', '망치로 치듯', 'touch'], ['Secco', '', 'dry: short, with no ring', '건조하게: 짧게, 울림 없이', 'touch'],
  ['Parlando', '', 'like speaking', '말하듯이', 'touch'], ['Glissando', 'gliss.', 'slide across the keys', '건반 위로 미끄러지듯', 'touch'], ['Légèrement', '', 'lightly', '가볍게', 'touch', 'fr'], ['Leicht', '', 'lightly', '가볍게', 'touch', 'de'],
  ['Naturale', 'nat.', 'normally again, after a special effect', '특수 효과 뒤에 다시 보통으로', 'touch'],
  ['Fine', '', 'the end', '끝', 'way'], ['Segue', '', 'go straight on to the next', '쉬지 않고 다음으로', 'way'], ['Come sopra', '', 'as above', '위와 같이', 'way'], ['Di nuovo', '', 'again', '다시', 'way'],
  ['Ossia', '', 'or: another (often easier) version', '또는: 다른(흔히 더 쉬운) 버전', 'way'], ['G.P.', '', 'general pause: everyone silent', '총휴지: 모두 쉼', 'way'], ['Lunga', '', 'long: a long pause', '길게: 긴 늘임', 'way'],
  ['Ottava', '8va', 'an octave higher (ottava bassa: lower)', '한 옥타브 높게(ottava bassa: 낮게)', 'way'], ['Mano destra, mano sinistra', 'M.D., M.S.', 'right hand, left hand', '오른손, 왼손', 'way'],
  ['Tacet', '', 'silent: do not play', '쉬어요: 연주하지 않음', 'others'], ['Tutti', '', 'everyone', '모두 함께', 'others'],
  ['Unisono', 'unis.', 'in unison: all on the same notes', '같은 음으로 함께', 'others'], ['Divisi', 'div.', 'divided into groups', '나누어서', 'others'], ['Colla voce, colla parte', '', 'follow the singer, follow the soloist', '노래를, 독주를 따라가며', 'others'],
  ['Obbligato', '', 'a part that must be played', '꼭 연주해야 하는 파트', 'others'],
  ['Col legno', '', 'with the wood of the bow', '활대 나무로', 'others'], ['Détaché', '', 'a separate bow for each note', '음마다 활을 따로', 'others', 'fr'], ['Spiccato', '', 'a bouncing bow', '활을 튀기며', 'others'],
  ['Con sordino', 'con sord.', 'with a mute', '약음기를 끼고', 'others'], ['Sourdine', '', 'mute', '약음기', 'others', 'fr'], ['Vibrato', '', 'a slight wobble of the pitch, for warmth', '음높이를 살짝 떨어 따뜻하게', 'others'],
  ['Flatterzunge', 'Flzg.', 'flutter-tonguing (wind players)', '플러터 텅잉(관악기)', 'others', 'de'],
];
const REF_LANG = { fr: ['French', '프랑스어'], de: ['German', '독일어'] };
const refPlayWordsList = () => {
  const out = TERMS.map(tm => ({ term: tm.term, abbr: tm.abbr, mean: tm.meaning, job: REF_JOB_OF[tm.term] || REF_JOB_CAT[tm.cat] || 'mood', tm: tm.hear ? tm : null, room: REF_FIRST[tm.term] || 'terms', g: REF_FIRST[tm.term] ? null : 'Grade ' + tm.grade, sort: tm.hear && tm.hear.bpm }));
  const an = TEMPO_TERMS.find(x => x.term === 'Andantino');
  if (an) out.push({ term: 'Andantino', abbr: '', mean: an.meaning, job: 'speed', tm: { term: 'Andantino', cat: 'Speed', hear: { bpm: an.demo } }, room: 'tempo', sort: an.demo });
  REF_MORE_WORDS.forEach(([term, abbr, en, ko, job, lang, sort]) => out.push({ term, abbr, mean: t(en, ko), job, lang, room: null, sort, tm: sort ? { term, cat: 'Speed', hear: { bpm: sort } } : null }));
  return out;
};
function RefWordRow({ w }) {
  return <div data-ref-word={w.term} style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) auto',alignItems:'center',gap:6,padding:'3px 0',borderBottom:'1px solid rgba(38,41,107,0.08)',breakInside:'avoid'}}>
    <div style={{minWidth:0,lineHeight:1.35}}><b style={{fontWeight:800}}>{w.term}</b>{w.abbr ? <span style={{color:BK.muted,fontWeight:700}}> ({w.abbr})</span> : null}{w.lang ? <span style={{color:BK.muted,fontSize:'0.85em',fontWeight:700}}> {t(REF_LANG[w.lang][0], REF_LANG[w.lang][1])}</span> : null}
      <span style={{color:BK.muted}}> · </span><span>{w.mean}</span></div>
    <span style={{display:'flex',gap:4,alignItems:'center'}}>{w.tm && <RefHear k={'w' + w.term} on={() => playTerm(w.tm)}/>}<RefDoor room={w.room} g={w.g}/></span>
  </div>;
}
function RefWordGroups({ groups }) {
  const paper = React.useContext(RefPaper);
  return <div>{groups.map(([id, en, ko, list]) => <div key={id} data-ref-wordgroup={id}>
    <RefLab>{t(en, ko)}</RefLab>
    <div style={paper ? {columnCount:3,columnGap:14,fontSize:11} : {display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(290px,1fr))',columnGap:16,fontSize:13.5}}>{list.map(w => <RefWordRow key={w.term} w={w}/>)}</div>
  </div>)}</div>;
}
function RefPlay({ part }) {
  const all = refPlayWordsList(), jobs = part === 'a' ? REF_JOBS.slice(0, 3) : part === 'b' ? REF_JOBS.slice(3, 5) : part === 'c' ? REF_JOBS.slice(5) : REF_JOBS;
  const groups = jobs.map(([id, en, ko]) => { let list = all.filter(w => w.job === id);
    if (id === 'speed') list = [...list.filter(w => w.sort).sort((a, b) => a.sort - b.sort), ...list.filter(w => !w.sort)];
    return [id, en, ko, list]; });
  return <div data-ref-play>
    {(!part || part === 'a') && <RefNote>{t('The terms room’s words with their grade, and more from the reference pages (extra). ♪ plays the room’s own example.', '용어 방의 낱말과 그 급, 그리고 레퍼런스의 낱말 더(더 알기). ♪는 그 방의 예를 들려줘요.')}</RefNote>}
    <RefWordGroups groups={groups}/>
  </div>;
}
// 10. words about music: the dictionary's words floor by floor (a tap opens its card); kinds of piece (Knowing your pieces),
// forms (Form, Knowing your pieces), texture and style (Styles), the voices (the instruments room), and the book's others
const REF_TERM_NAME = { 'dotted-note': ['dotted note', '점음표'], step: ['step', '차례가기'], natural: ['natural', '내추럴'], key: ['key', '조'] };   // these four keep no word list (so the text does not link every 'key' or 'step')
const refTermName = (x) => LANG === 'ko' ? (x.ko[0] || (REF_TERM_NAME[x.id] || [])[1] || x.id) : (x.en[0] || (REF_TERM_NAME[x.id] || [])[0] || x.id);
const refTrim = (s) => { s = String(s).replace(/\.$/, ''); return LANG === 'ko' || !/^[A-Z][a-z ]/.test(s) || /^[A-Z][a-z]+ [A-Z]/.test(s) ? s : s[0].toLowerCase() + s.slice(1); };
const REF_FORM_KO = { 'Exposition, development, recapitulation': '제시부, 전개부, 재현부', 'Theme, var. 1, var. 2, var. 3': '주제, 변주 1, 변주 2, 변주 3', 'Minuet, trio, minuet': '미뉴에트, 트리오, 미뉴에트' };
// the book's other words (its glossary, pp. 246-249), in my words: [term en, term ko, meaning en, meaning ko, group]
const REF_MORE_TERMS = [
  ['Concerto', '협주곡', 'a soloist with an orchestra, usually in three movements', '독주자와 오케스트라, 보통 세 악장', 'kinds'], ['Symphony', '교향곡', 'a large work for orchestra in several movements', '오케스트라를 위한 여러 악장의 큰 작품', 'kinds', 'pieces-78'],
  ['Suite', '모음곡', 'a set of pieces; in the Baroque, dances in one key', '여러 곡의 모음; 바로크에서는 한 조의 춤곡들', 'kinds', 'pieces-78'], ['String quartet', '현악 4중주', 'two violins, a viola and a cello', '바이올린 둘, 비올라, 첼로', 'kinds', 'pieces-78'],
  ['Opera', '오페라', 'a story sung on stage, with an orchestra', '오케스트라와 함께 무대에서 노래로 하는 이야기', 'kinds'], ['Aria', '아리아', 'a song for one singer in an opera or oratorio', '오페라나 오라토리오의 독창곡', 'kinds', 'form', 'Grade 5'],
  ['Oratorio', '오라토리오', 'a sacred story for voices and orchestra, not acted', '목소리와 오케스트라의 종교적인 이야기, 연기 없이', 'kinds', 'pieces-78'], ['Overture', '서곡', 'the orchestra’s opening piece before an opera or ballet', '오페라나 발레 앞에 오케스트라가 여는 곡', 'kinds'],
  ['Canon', '카논', 'one tune, started by each voice in turn', '한 선율을 성부마다 차례로 시작', 'forms'], ['Ground bass', '그라운드 베이스', 'a bass line repeated under changing music above', '위의 음악이 바뀌는 동안 되풀이되는 베이스', 'forms'],
  ['Cadenza', '카덴차', 'a solo passage to show off, near a concerto movement’s end', '협주곡 악장 끝 무렵 솜씨를 보여 주는 독주 부분', 'forms'], ['Coda', '코다', 'the closing section of a piece', '곡을 끝맺는 부분', 'forms', 'signs'],
  ['Ostinato', '오스티나토', 'a pattern repeated again and again', '계속 되풀이되는 음형', 'forms'],
  ['Movement', '악장', 'a complete section of a larger work', '큰 작품 속의 완결된 한 부분', 'forms', 'pieces-78'],
  ['Counterpoint', '대위법', 'two or more independent tunes at once', '둘 이상의 독립된 선율이 동시에', 'tex', 'composers'], ['Consonance', '협화음', 'notes that sound at rest together', '함께 울려 편안한 음들', 'tex'],
  ['Dissonance', '불협화음', 'notes that clash and want to move on', '부딪쳐 다음으로 가고 싶어 하는 음들', 'tex'], ['Timbre', '음색', 'the colour of a sound: a flute and a violin on the same note', '소리의 색깔: 같은 음의 플루트와 바이올린', 'tex'],
  ['Tonality', '조성', 'music built round a home key', '으뜸조를 중심으로 짜인 음악', 'tex'], ['Atonal', '무조', 'music with no home key', '으뜸조가 없는 음악', 'tex'],
  ['Twelve-tone music', '12음 음악', 'all twelve notes in a fixed row, none the home note', '열두 음을 정한 순서로, 어느 음도 으뜸음이 아님', 'tex', 'composers'], ['Programme music', '표제 음악', 'music that tells a story or paints a scene', '이야기를 들려주거나 장면을 그리는 음악', 'tex'],
  ['A cappella', '아카펠라', 'voices alone, no instruments', '악기 없이 목소리만', 'more'], ['Accompaniment', '반주', 'the part that supports the tune', '선율을 받쳐 주는 파트', 'more'],
  ['Chamber music', '실내악', 'music for a small group, one player a part', '작은 앙상블, 파트마다 한 명', 'more'], ['Continuo', '통주저음', 'Baroque bass line with a keyboard filling in the chords', '건반이 화음을 채우는 바로크의 베이스', 'more'],
  ['Libretto', '리브레토', 'the words of an opera', '오페라의 대본', 'more'], ['Recitative', '레치타티보', 'singing in the rhythm of speech, to move the story on', '말하는 리듬으로 이야기를 이끌어 가는 노래', 'kinds', 'form', 'Grade 5'],
  ['Leitmotif', '라이트모티프', 'a short tune that stands for a person or idea', '인물이나 생각을 나타내는 짧은 선율', 'more'], ['Score', '총보', 'the music with every part, one above another', '모든 파트를 위아래로 적은 악보', 'more'],
  ['Repertoire', '레퍼토리', 'the pieces a player can perform', '연주자가 연주할 수 있는 곡들', 'more'], ['Recital', '리사이틀', 'a concert by one player or a small group', '한 명이나 작은 그룹의 연주회', 'more'],
];
function RefTerms({ part }) {
  const paper = React.useContext(RefPaper), [card, setCard] = useState(null);
  const floors = STAGES.map(s => ({ name: s.en ? s.en[0] : '', terms: DICT_TERMS.filter(x => s.ids.includes(x.room)) })).filter(f => f.terms.length);
  const more = (gr) => REF_MORE_TERMS.filter(x => x[4] === gr).map(([en, ko, men, mko, , room, g]) => ({ term: t(en, ko), mean: t(men, mko), room: room || null, g }));
  const kinds = [...P8_TITLES.map(([, en, ko, men, mko]) => ({ term: t(en, ko), mean: refTrim(t(men, mko)), room: 'pieces-8' })), ...more('kinds')];
  // the Form room's lessons: binary, ternary and rondo (Grade 1), minuet and trio and variations (Grade 5), sonata form (Grade 6)
  const forms = [...FORM_Q.map(([shape, id]) => ({ term: t(FORM_N[id][0], FORM_N[id][1]), mean: LANG === 'ko' ? REF_FORM_KO[shape] || shape : refTrim(shape), room: 'form', g: id === 'sonata' ? 'Grade 6' : ['minuet', 'variations'].includes(id) ? 'Grade 5' : null })),
    { term: t('Fugue', '푸가'), mean: t('a subject that enters in each voice in turn; the answer, the countersubject, episodes between the entries', '성부마다 차례로 들어오는 주제; 응답, 대주제, 주제 제시 사이의 간주부(에피소드)'), room: 'form', g: 'Grade 6' }, ...more('forms')];
  const tex = [...CSX_WORDS.map(([en, men, mko]) => ({ term: sprCap(t(en, CSX_WORD_KO[en] || en)), mean: t(men, mko), room: 'styles' })), ...more('tex')];
  const vo = RANGES.find(g => g.g === 'Voices'), voices = vo ? vo.rows.map(([n, lo, hi]) => ({ term: rangeName(n), mean: t('sings about ', '대략 ') + lo + '–' + hi + t('', ' 음역을 노래해요'), room: 'pitch-range' })) : [];
  return <div data-ref-terms>
    {part !== 'b' && <><RefLab>{t('The dictionary, floor by floor', '사전, 층마다')}</RefLab>
    {floors.map(f => <div key={f.name} style={{display:'grid',gridTemplateColumns:'74px minmax(0,1fr)',gap:6,alignItems:'baseline',padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.1)'}}>
      <span style={{fontSize:11,fontWeight:900,color:BK.coral,letterSpacing:'0.04em'}}>{f.name}</span>
      <span style={{display:'flex',flexWrap:'wrap',gap:paper ? '0 10px' : 4}}>{f.terms.map(x => paper ? <span key={x.id} style={{fontSize:12.5,fontWeight:700}}>{refTermName(x)}</span>
        : <button key={x.id} type="button" className="chip" data-ref-term={x.id} onClick={() => setCard(x.id)} style={{minHeight:30,padding:'2px 9px',fontSize:12.5,fontWeight:800}}>{refTermName(x)}</button>)}</span>
    </div>)}
    {card && <DictCard id={card} onClose={() => setCard(null)}/>}</>}
    <RefWordGroups groups={[...(part !== 'b' ? [['kinds', 'Kinds of piece', '곡의 종류', kinds]] : []), ...(part !== 'a' ? [['forms', 'Forms', '형식', forms], ['tex', 'Texture, style and sound', '짜임, 양식, 소리', tex],
      ['voices', 'Voices', '목소리', voices], ['more', 'More words', '낱말 더', more('more')]] : [])]}/>
  </div>;
}
// 11. the periods: the composers room's six (its years, its first 'what you hear', its composers in its own order); ♪ the
// styles room's example of each
const REF_REN = [['Tallis', '탈리스'], ['Byrd', '버드'], ['Palestrina', '팔레스트리나']];   // the book's p. 242 (the house's composers start in the Baroque)
function RefPeriods() {
  const paper = React.useContext(RefPaper), y0 = 1400, y1 = 2026, W = 600, X = (y) => (y - y0) / (y1 - y0) * W;
  return <div data-ref-periods>
    <svg viewBox={'0 0 ' + W + ' 40'} style={{width:'100%',display:'block',margin:'0 0 6px'}} role="img" aria-label={t('The six periods on one line, 1400 to today', '여섯 시대를 한 줄에, 1400년부터 오늘까지')}>
      {CMP_ERA_IDS.map((id, i) => { const p = CMP_PERIODS[id], a = X(p.years[0]), b = X(Math.min(p.years[1], y1)); return <g key={id}>
        <rect x={a} y="6" width={b - a} height="14" fill={i % 2 ? '#fff' : 'rgba(38,41,107,0.12)'} stroke={PEN_N} strokeWidth="1"/>
        <text x={a + 3} y="33" fontSize="10.5" fontWeight="900" fill={PEN_N} fontFamily="Georgia, serif">{p.years[0]}</text>
        {paper && <text x={(a + b) / 2} y="16.5" textAnchor="middle" fontSize="8.5" fontWeight="800" fill={PEN_N}>{t(p.short[0], p.short[1])}</text>}</g>; })}
    </svg>
    <RefTable k="periods" cols="minmax(0,1fr) auto" rows={CMP_ERA_IDS.map(id => { const p = CMP_PERIODS[id], who = id === 'renaissance' ? REF_REN.map(x => t(x[0], x[1])) : CMP.filter(c => c.era === id).slice(0, 4).map(c => (c.name[0].indexOf(c.sur[0]) === 0 ? t(c.name[0], c.name[1]) : t(c.sur[0], c.sur[1])));
        return [<div data-ref-period={id}><b style={{fontWeight:800}}>{t(p.short[0], p.short[1])}</b> <span style={{fontSize:12,fontWeight:800,color:BK.coral,whiteSpace:'nowrap'}}>{p.years[0]}–{p.years[1] > 2025 ? t('today', '오늘') : p.years[1]}</span>
          <div style={{fontSize:13}}>{t(p.sound[0][0], p.sound[0][1])}</div><div style={{color:BK.muted,fontWeight:700,fontSize:12.5}}>{who.join(', ')}</div></div>,
          <span style={{display:'flex',gap:4,alignItems:'center'}}>{id !== 'renaissance' && <RefHear k={'era' + id} on={() => csxEraHear(id)}/>}<RefDoor room="composers" g={id === 'renaissance' ? t('Composers', '작곡가') : null}/></span>]; })}/>
    {!paper && <RefNote>{t('♪ plays the Styles room’s example of each period.', '♪는 양식 방의 시대별 예를 들려줘요.')}</RefNote>}
  </div>;
}
// 12. the instruments: the four families (how they sound, the Stories of music room's own words) and the keyboards; the
// orchestra's instruments with the clef each reads (its Grade 4 and 5 pages); the score order (the book's p. 245)
const REF_PERC = [['timpani', '팀파니'], ['side drum', '작은북'], ['bass drum', '큰북'], ['cymbals', '심벌즈'], ['triangle', '트라이앵글'], ['xylophone', '실로폰'], ['glockenspiel', '글로켄슈필']];
const REF_STR_CLEF = { Violin: ['treble clef', '높은음자리표'], Viola: ['alto clef', '알토음자리표'], Cello: ['bass clef, tenor and treble for high notes', '낮은음자리표, 높은 음은 테너·높은음자리표'], 'Double bass': ['bass clef, sounding an octave lower', '낮은음자리표, 한 옥타브 낮게 소리 나요'] };
const REF_SCORE = [['Woodwind', '목관 악기', 'piccolo, flutes, oboes, cor anglais, clarinets, bass clarinet, bassoons, contrabassoon', '피콜로, 플루트, 오보에, 잉글리시 호른, 클라리넷, 베이스 클라리넷, 바순, 콘트라바순'],
  ['Brass', '금관 악기', 'horns, trumpets, trombones, tuba', '호른, 트럼펫, 트롬본, 튜바'], ['Percussion', '타악기', 'timpani, then the other percussion', '팀파니, 그다음 다른 타악기'],
  ['Harp and keyboards', '하프와 건반', 'harp, celesta, piano', '하프, 첼레스타, 피아노'], ['The soloist', '독주자', 'in a concerto, just above the strings', '협주곡에서는 현악기 바로 위'],
  ['Strings', '현악기', 'violins I, violins II, violas, cellos, double basses', '제1바이올린, 제2바이올린, 비올라, 첼로, 더블베이스']];
function RefInstruments() {
  const paper = React.useContext(RefPaper), k = paper ? 0.5 : 0.6;
  const icons = (ids) => <svg viewBox={'0 0 ' + ids.length * 62 + ' 62'} width={ids.length * 62 * k} height={62 * k} style={{display:'block',flex:'0 0 auto'}}>{ids.map((id, i) => <SprInst key={id} id={id} x={i * 62} y={0} s={1}/>)}</svg>;
  const fam = (id, icn, name, how, rows, g, room = 'pitch-range') => <div key={id} data-ref-family={id} style={{border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'6px 10px',breakInside:'avoid'}}>
    <div style={{display:'flex',gap:8,alignItems:'center',flexWrap:'wrap'}}>{icn && icons(icn)}<div style={{flex:'1 1 140px',minWidth:0}}><b style={{fontWeight:800,fontSize:14}}>{sprCap(name)}</b><br/><span style={{fontSize:12.5,color:BK.muted}}>{how}</span></div><RefDoor room={room} g={g}/></div>
    {rows && <div style={{marginTop:4}}>{rows.map(([n, clef, snd], i) => <div key={i} style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) auto',gap:6,alignItems:'center',padding:'2px 0',borderTop:'1px solid rgba(38,41,107,0.08)',fontSize:13}}>
      <span><b style={{fontWeight:800}}>{n}</b>{clef ? <span style={{color:BK.muted}}> · {clef}</span> : null}</span>{snd === 'x' ? <RefDoor room={null}/> : snd ? <RefHear k={'in' + id + i} on={snd}/> : <span/>}</div>)}</div>}
  </div>;
  return <div data-ref-instruments>
    <div style={{display:'grid',gridTemplateColumns:paper ? '1fr 1fr' : 'repeat(auto-fill,minmax(280px,1fr))',gap:6}}>
      {fam('strings', ['violin', 'cello', 'harp'], sprFamName('strings'), SPR_FAM.strings.howLong(), SPR_TUNE.map(v => [rangeName(v.n), t(REF_STR_CLEF[v.n][0], REF_STR_CLEF[v.n][1]), () => sprTunePlay(v)]), t('Instruments · Grade 4', '악기 · Grade 4'))}
      {fam('woodwind', ['flute', 'clarinet', 'recorder'], sprFamName('woodwind'), SPR_FAM.woodwind.howLong(), SPR_WIND.map(v => [t(v.n[0], v.n[1]), t(v.clef[0], v.clef[1]), () => sprWindPlay(v)]), t('Instruments · Grade 5', '악기 · Grade 5'))}
      {fam('brass', ['trumpet', 'trombone', 'tuba'], sprFamName('brass'), SPR_FAM.brass.howLong(), SPR_BRASS.map(v => [t(v.n[0], v.n[1]), t(v.clef[0], v.clef[1]), () => sprWindPlay(v)]), t('Instruments · Grade 6', '악기 · Grade 6'))}
      {fam('percussion', ['drum', 'xylophone', 'triangle'], sprFamName('percussion'), SPR_FAM.percussion.howLong(), [[sprCap(REF_PERC.map(x => t(x[0], x[1])).join(', ')), '', 'x']])}
      {fam('keyboards', null, t('Keyboards', '건반 악기'), t('Keys move hammers that strike strings (piano), tangents that press them (clavichord), quills that pluck them (harpsichord) or valves that let air into pipes (organ).', '건반이 줄을 치는 해머(피아노), 줄을 누르는 탄젠트(클라비코드), 줄을 뜯는 깃촉(하프시코드), 파이프에 바람을 넣는 밸브(오르간)를 움직여요.'),
        [[t('Piano, harpsichord, clavichord, organ', '피아노, 하프시코드, 클라비코드, 오르간'), t('the grand staff', '큰보표'), null]], null, 'piano-story')}
    </div>
    <div style={{display:'flex',alignItems:'baseline',justifyContent:'space-between',gap:8}}><RefLab>{t('The score, top to bottom', '총보, 위에서 아래로')}</RefLab><RefDoor room={null}/></div>
    <RefTable k="score" cols="minmax(0,0.8fr) minmax(0,2fr)" rows={REF_SCORE.map(([en, ko, men, mko]) => [<b style={{fontWeight:800}}>{t(en, ko)}</b>, <span style={{fontSize:12.5}}>{t(men, mko)}</span>])}/>
  </div>;
}
const REF_BODY = { staff: RefStaff, notes: RefNotes, time: RefTimes, keys: RefKeys, scales: RefScales, intervals: RefIntervals, chords: RefChords, signs: RefSigns, play: RefPlay, terms: RefTerms, periods: RefPeriods, instruments: RefInstruments };
function ReferenceView({ onChapter }) {
  const jump = (id) => { const el = document.getElementById('ref-' + id); if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
  return <RefGo.Provider value={onChapter || null}><div data-reference style={{display:'flex',flexDirection:'column',gap:18}}>
    <div>
      <div style={{fontSize:14,color:'#4a4d86',lineHeight:1.5,margin:'0 0 8px'}}>{t('The whole of the theory on a few tables, Beginner to Grade 8. Each row shows the floor where you learn it: tap it to go to that room. ♪ plays it.', 'Beginner부터 Grade 8까지의 이론을 표 몇 장에. 줄마다 그걸 배우는 층이 있어요: 누르면 그 방으로 가요. ♪는 소리.')}</div>
      <div style={{display:'flex',flexWrap:'wrap',gap:5}}>{REF_SECS.map(s => <button key={s.id} type="button" className="chip" data-ref-jump={s.id} onClick={() => jump(s.id)} style={{minHeight:34,padding:'3px 11px',fontSize:12.5,fontWeight:800}}>{t(s.en, s.ko)}</button>)}</div>
    </div>
    {REF_SECS.map(s => { const B = REF_BODY[s.id]; return <section key={s.id} style={{minWidth:0}}><RefHead id={s.id}/><B/></section>; })}
  </div></RefGo.Provider>;
}
// on paper: A4 pages in the books' look; 'id:a' and 'id:b' split a long section over two pages
const REF_PAGES = [['staff', 'notes'], ['time'], ['keys'], ['scales:a', 'intervals'], ['scales:b'], ['chords:a'], ['chords:b'], ['signs'], ['play:a'], ['play:b'], ['play:c'], ['terms:a'], ['terms:b'], ['periods'], ['instruments']], REF_PAGE_COLS = {};
function RefBook() {
  return <RefPaper.Provider value={true}>{REF_PAGES.map((ids, i) => <section key={i} className="bk-page" data-ref-page={i + 1} style={{position:'relative'}}>
    <VicFloor no={i + 1}/>
    <VicHead left={t('Reference', '한눈에 보기')} right={ids.map(x => { const [id, part] = x.split(':'), s = REF_SECS.find(y => y.id === id); return t(s.en, s.ko) + (part && part !== 'a' ? t(' (cont.)', ' (이어서)') : ''); }).join(' · ')} mb={10}/>
    <div className="bk-body" style={REF_PAGE_COLS[i] ? {flex:1,minHeight:0,overflow:'hidden',display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,alignItems:'start'} : {flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:12}}>{ids.map(x => { const [id, part] = x.split(':'), B = REF_BODY[id]; return <div key={x} style={{minWidth:0}}>{(!part || part === 'a') && <RefHead id={id}/>}<B part={part}/></div>; })}</div>
  </section>)}</RefPaper.Provider>;
}
