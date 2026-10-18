// ─── Phase 485: the first concept book, Scales and keys (rule 16; her 2026-10-17 22:09 '스케일과 조 첫개념 책으로 만든거 보자') ───
// A concept is taught whole, once: the rule, then every key at once, then the steps to practise it, with the tools that
// already exist. The pages are written once (cbScalesPages): printed, the A4 concept book (?book=concept&ch=p-scales); on
// screen (the Toolbox's 'cb-p-scales'), the opener and then one step a page, each with a working tool beside its picture.
const CONCEPT_BOOKS = {};
const CB_TOOL = { 'p-scales': 'cb-p-scales' };   // a concept -> its book on screen
const cbRight = (cid) => { const c = TOOL_CATS.find(x => x.id === cid), a = c && TOOL_AREAS.find(x => x.id === c.area); return c ? a.name + ' · ' + c.name : ''; };
const cbBookName = () => t('Concept book', '개념책');
// signs in the music font (the natural too); the places a line must not break (rule 8: a sign stays with its syllable,
// 'ㄹ 수 있어요' and '조 이름' stay whole, a list of note names stays whole, a lone '반' never starts a line)
const cbSx = (x) => typeof x !== 'string' || !/[♯♭♮]/.test(x) ? x : x.split(/([♯♭♮])/).map((p, i) => p === '♯' ? <React.Fragment key={i}>{tnSign('#')}</React.Fragment> : p === '♭' ? <React.Fragment key={i}>{tnSign('b')}</React.Fragment> : p === '♮' ? <React.Fragment key={i}>{tnSign('n')}</React.Fragment> : p);
const cbNbKo = (x) => sscNbKo(x)
  .replace(/([♯♭♮])(?=[가-힣(])/g, '$1⁠')
  .replace(/(\S) 수(도)? 있어요/g, '$1 수$2 있어요')
  .replace(/조 이름/g, '조 이름').replace(/장조 이름/g, '장조 이름')
  .replace(/한 (걸음|칸|번|손|옥타브)/g, '한 $1')
  .replace(/([온반]), ([온반])(?=$|\.| 걸음)/g, '$1, $2')
  .replace(/(?<![A-Za-z])([A-G][♯♭♮]?) (?=[A-G][♯♭♮]?(?![A-Za-z]))/g, '$1 ')
  .replace(/(두|세|네|다섯) (개|번)(?=[가-힣])/g, '$1\u00a0$2').replace(/([가-힣])\(/g, '$1\u2060(').replace(/이름 둘/g, '이름\u00a0둘').replace(/(\d+도) (위|아래)/g, '$1\u00a0$2').replace(/(샤프|플랫) (\d)/g, '$1\u00a0$2')
  .replace(/‘([^’]+)’/g, (m) => m.replace(/ /g, '\u00a0'))
  .replace(/\(([^()]{1,8}) ([^()]{1,8})\)/g, '($1\u00a0$2)');
// a run of note names stays together; a long run may break once, in its middle (never a lone last note)
const cbNbEn = (x) => sscNbEn(x).replace(/(?<![A-Za-z])[A-G][♯♭♮]?(?:[ \u00a0][A-G][♯♭♮]?)+(?![A-Za-z])/g, (m) => { const w = m.split(/[ \u00a0]/), h = w.length > 4 ? Math.ceil(w.length / 2) : w.length;
  return w.slice(0, h).join('\u00a0') + (h < w.length ? ' ' + w.slice(h).join('\u00a0') : ''); });
const X5 = (en, ko) => cbSx(LANG === 'ko' ? cbNbKo(ko) : cbNbEn(en));
// a seven-note scale from a spelled tonic ('A', 'C#', 'Eb'), each letter once ('F##' a double sharp, 'Cbb' a double flat)
const CB_L = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], CB_PC = [0, 2, 4, 5, 7, 9, 11];
function cbSpell7(tonic, pat) {
  const l0 = CB_L.indexOf(tonic[0]), pc0 = (CB_PC[l0] + (tonic[1] === '#' ? 1 : tonic[1] === 'b' ? -1 : 0) + 12) % 12;
  return pat.map((o, i) => { const L = CB_L[(l0 + i) % 7], want = (pc0 + o) % 12; let d = ((want - CB_PC[CB_L.indexOf(L)]) % 12 + 12) % 12; if (d > 6) d -= 12;
    return L + (d === 1 ? '#' : d === 2 ? '##' : d === -1 ? 'b' : d === -2 ? 'bb' : ''); });
}
// a spelled name as text: the sign in the music font (a double sharp too)
const cbNoteEl = (n) => { if (n.length < 2) return n; const s = n.slice(1), g = s === '##' ? '𝄪' : s === 'bb' ? '𝄫' : null;
  return g ? <>{n[0]}<span style={{fontFamily:MUSIC_FONT,fontWeight:400,fontSize:'1.15em',lineHeight:0}}>{g}</span></> : cbSx(prettyNote(n)); };
const cbAcc = (n) => n.length > 1;
const CB_KEYNAME = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'];   // the piano key a spelled note is played on
const cbPlayedOn = (n) => { const L = CB_L.indexOf(n[0]), acc = n.slice(1); return CB_KEYNAME[(CB_PC[L] + (acc === '#' ? 1 : acc === '##' ? 2 : acc === 'b' ? -1 : acc === 'bb' ? -2 : 0) + 12) % 12]; };
// the scale shapes on the clock (offsets in half steps from the first note); down: the way back, when it differs
const CB_SHAPES = [
  { id: 'major', pat: [0, 2, 4, 5, 7, 9, 11], en: 'Major', ko: '장음계', at: 'C', full: (n) => t(n + ' major', n + '장조 음계') },
  { id: 'nat', pat: [0, 2, 3, 5, 7, 8, 10], en: 'Natural minor', ko: '자연단음계', at: 'A', full: (n) => t(n + ' natural minor', n + '단조 자연단음계') },
  { id: 'harm', pat: [0, 2, 3, 5, 7, 8, 11], en: 'Harmonic minor', ko: '화성단음계', at: 'A', full: (n) => t(n + ' harmonic minor', n + '단조 화성단음계') },
  { id: 'mel', pat: [0, 2, 3, 5, 7, 9, 11], down: [0, 2, 3, 5, 7, 8, 10], en: 'Melodic minor', ko: '가락단음계', at: 'A', full: (n) => t(n + ' melodic minor', n + '단조 가락단음계') },
  { id: 'penta', pat: [0, 2, 4, 7, 9], en: 'Major pentatonic', ko: '장조 5음음계', at: 'C', full: (n) => t(n + ' major pentatonic', n + '장조 5음음계') },
  { id: 'chrom', pat: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], en: 'Chromatic', ko: '반음계', at: 'C', full: (n) => t('Chromatic, from ' + n, n + ' 반음계') },
];
// its steps in words: T, S and T+S (a tone and a semitone); T+S and the last two never part
const cbSteps = (pat) => { if (pat.length === 12) return t('12 half steps', '반 걸음 12번');
  const s = pat.map((o, i) => { const g = ((i + 1 < pat.length ? pat[i + 1] : 12) - o); return g === 1 ? t('S', '반') : g === 2 ? t('T', '온') : t('T⁠+⁠S', '온⁠+⁠반'); });
  return s.slice(0, -1).join(' ') + ' ' + s[s.length - 1]; };
// the tonic's name for a shape: a minor key on a black key is spelled with a sharp (C♯, F♯, G♯), as it is written
const cbTonic = (k, sh) => sh.id === 'major' || sh.id === 'penta' || sh.id === 'chrom' ? k : ({ Db: 'C#', Gb: 'F#', Ab: 'G#' }[k] || k);
const cbNames = (k, sh) => { const tn = cbTonic(k, sh); return sh.id === 'penta' ? [0, 1, 2, 4, 5].map(i => pbSpell(k)[i]) : sh.id === 'chrom' ? null : cbSpell7(tn, sh.pat); };
const cbMidi = (k, sh) => { const pc = pbKeyPc(k), b = 60 + pc - (pc > 6 ? 12 : 0); return [...sh.pat.map(o => b + o), b + 12, ...[...(sh.down || sh.pat)].reverse().map(o => b + o)]; };
const cbDown = (names) => [names[0], ...[...names].reverse()];   // the way down: the top note, then back to the first
// the chromatic scale's names going up (sharps), from a key
const CB_SHARPS12 = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
const cbChromUp = (k) => { const p = pbKeyPc(k); return CB_SHARPS12.map((_, i) => CB_SHARPS12[(p + i) % 12]); };
const cbRingNames = (k, sh) => cbNames(k, sh) || cbChromUp(k);
// a narrow screen (a phone): the key pad shows one ring at a time, the note boxes get smaller
function useCbNarrow(px) {
  const q = '(max-width: ' + (px - 1) + 'px)';
  const [n, setN] = useState(() => { try { return window.matchMedia(q).matches; } catch (e) { return false; } });
  useEffect(() => { let m; try { m = window.matchMedia(q); } catch (e) { return undefined; } const f = () => setN(m.matches); f();
    if (m.addEventListener) m.addEventListener('change', f); else m.addListener(f);
    return () => { if (m.removeEventListener) m.removeEventListener('change', f); else m.removeListener(f); }; }, [q]);
  return n;
}
// one sound at a time: a pad that plays stops any other pad (chapter 16's too, through SSC_STOP), and stops when it goes
function cbUseOneSound(timers) {
  const me = useRef(null);
  if (!me.current) { const f = () => { pbStopMidi(timers.current); timers.current = []; }; f.claim = () => { if (SSC_STOP.fn && SSC_STOP.fn !== f) SSC_STOP.fn(); SSC_STOP.fn = f; }; me.current = f; }
  useEffect(() => () => { me.current(); if (SSC_STOP.fn === me.current) SSC_STOP.fn = null; }, []);
  return me.current;
}
// a key's line: its name, its sharps or flats, and its other name when it has one
const cbKeyLine = (sel) => { const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0], signs = sg.type ? (sg.type === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, sg.count) : [];
  const s = skgKeyName(sel) + ': ' + (sg.count ? pbCountWords(sel) + (LANG === 'ko' ? '(' : ' (') + signs.map(prettyNote).join(' ') + ')' : t('no sharps or flats', '샤프도 플랫도 없음')) + (CB_TWIN[sel] ? ' · ' + t(CB_TWIN[sel][0], CB_TWIN[sel][1]) : '');
  return cbSx(LANG === 'ko' ? cbNbKo(s) : s); };

// ── the pads ──
// the opener's: one key, everything at once (the clock's shape, the circle, the notes, the key signature, the sound)
const CB_TWIN = { Gb: ['the same keys as F♯ major (6 sharps)', 'F♯장조(샤프 여섯)와 건반이 같아요'], B: ['the same keys as C♭ major (7 flats)', 'C♭장조(플랫 일곱)와 건반이 같아요'], Db: ['the same keys as C♯ major (7 sharps)', 'C♯장조(샤프 일곱)와 건반이 같아요'] };
function CbKeyPad() {
  const [sel, setSel] = useState('C');
  const timers = useRef([]);
  const stop = cbUseOneSound(timers);
  const pickK = (k) => { stop(); setSel(k); };
  const narrow = useCbNarrow(560), tiny = useCbNarrow(360), [ring, setRing] = useState('clock');
  const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0], names = pbSpell(sel);
  const clock = <div><KeyRing sel={sel} onPick={pickK} o={{ shape: true, center: (C) => <text x={C} y={C + 7} textAnchor="middle" fontSize="22" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(prettyNote(sel))}</text> }} label={t('The keyboard clock with the ' + prettyNote(sel) + ' major scale drawn as a shape.', '건반 시계: ' + prettyNote(sel) + '장조 음계가 모양으로 그려져 있어요.')}/>
    <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted}}>{t('the keyboard clock', '건반 시계')}</div></div>;
  const circle = <div><FifthsRing sel={sel} onPick={pickK} o={{ filled: [], twins: true }} label={t('The circle of fifths, ' + skgKeyName(sel) + ' ringed.', '5도권: ' + skgKeyName(sel) + '에 동그라미.')}/>
    <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted}}>{t('the circle of fifths', '5도권')}</div></div>;
  return (
    <div className="try-box" style={tiny ? { ...actBox, paddingLeft:4, paddingRight:4 } : actBox} data-cb="key-pad">
      <div style={actTitle}>{t('One key, all at once', '조 하나를 한눈에')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{narrow
        ? t('The keyboard clock is one octave’s twelve keys in a ring, C at the top, each place a half step. Tap a piano key on the clock, or a key on the circle: the clock turns the scale’s shape to start there; the circle shows where the key sits. Switch rings with the two buttons.', '건반 시계는 한 옥타브의 열두 건반을 둥글게 놓은 거예요. 맨 위는 C, 한 칸이 반 걸음이에요. 건반 시계나 5도권에서 조를 눌러요. 건반 시계는 장음계 모양을 그 조에서 시작하도록 돌리고, 5도권은 그 조의 자리를 보여 줘요. 위의 두 버튼으로 원을 바꿔요.')
        : t('The keyboard clock is one octave’s twelve keys in a ring, C at the top, each place a half step. Tap a piano key on the clock, or a key on the circle: the clock turns the scale’s shape to start there; the circle shows where the key sits and how many sharps or flats it has.', '건반 시계는 한 옥타브의 열두 건반을 둥글게 놓은 거예요. 맨 위는 C, 한 칸이 반 걸음이에요. 두 원 어디에서든 조를 눌러요. 건반 시계는 장음계 모양을 그 조에서 시작하도록 돌리고, 5도권은 그 조의 자리와 샤프나 플랫의 개수를 보여 줘요.')}</div>
      {narrow ? <>
        <div role="tablist" style={{display:'flex',gap:6,justifyContent:'center',marginBottom:8}}>{[['clock', t('Clock', '건반 시계')], ['circle', t('Circle', '5도권')]].map(([v, l]) => <button key={v} role="tab" aria-selected={ring === v} className={'chip' + (ring === v ? ' active' : '')} style={{minHeight:44,minWidth:96}} onClick={() => setRing(v)}>{l}</button>)}</div>
        <div style={{maxWidth:tiny ? '100%' : 300,margin:'0 auto'}}>{ring === 'clock' ? clock : circle}</div>
      </> : <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10,maxWidth:600,margin:'0 auto'}}>{clock}{circle}</div>}
      <div style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:3,margin:'10px auto 4px',maxWidth:360}}>{[...names, names[0]].map((n, i) => <span key={i} style={{flex:'1 1 0',minWidth:0,maxWidth:tiny ? 38 : 42,textAlign:'center',padding:'4px 0',borderRadius:6,border:'1.5px solid ' + (cbAcc(n) ? PEN_C : BK.line),fontSize:tiny ? 13 : 15,fontWeight:900,color:cbAcc(n) ? PEN_C : BK.ink}}>{cbNoteEl(n)}</span>)}</div>
      <div style={{maxWidth:300,margin:'4px auto 0'}}><KSStaff count={sg.count} type={sg.type}/></div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,margin:'2px 0 8px',textWrap:'balance'}}>{cbKeyLine(sel)}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => { stop(); stop.claim(); timers.current = pbPlayMidi(pbScaleMidi(sel), 110); }}>{t('▶ Listen', '▶ 듣기')}</button>
        <a className="ghost-btn" style={{minHeight:44,display:'inline-flex',alignItems:'center',textDecoration:'none'}} href={cbHref('tool=scale-finder&key=' + encodeURIComponent(sel))}>{t('Fingering →', '손가락 번호 →')}</a>
      </div>
    </div>
  );
}
// pages 6 and 7: other shapes on the same clock, from any key
function CbShapesPad({ ids, first }) {
  const shapes = CB_SHAPES.filter(s => ids.includes(s.id));
  const [shId, setShId] = useState(first);
  const [sel, setSel] = useState(() => CB_SHAPES.find(s => s.id === first).at);
  const timers = useRef([]);
  const stop = cbUseOneSound(timers);
  const sh = CB_SHAPES.find(x => x.id === shId), names = cbNames(sel, sh), tn = cbTonic(sel, sh), tinyS = useCbNarrow(360);
  const downNames = sh.down ? cbSpell7(tn, sh.down) : null, dbl = names ? names.find(n => n.endsWith('##')) : null;
  return (
    <div className="try-box" style={actBox} data-cb="shapes-pad">
      <div style={actTitle}>{t('Other shapes, the same clock', '다른 모양, 같은 시계')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{t('Pick a shape, then tap a key on the clock to start it there.', '모양을 고르고, 시계에서 건반을 눌러 그 음에서 시작해요.')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:420,margin:'0 auto 8px'}}>{shapes.map(s => <button key={s.id} className={'chip' + (s.id === shId ? ' active' : '')} style={{minHeight:44,fontSize:13,padding:'6px 4px',whiteSpace:'normal',lineHeight:1.15}} onClick={() => { stop(); setShId(s.id); }}>{LANG === 'ko' && /.단음계$/.test(s.ko) ? <span style={{wordBreak:'keep-all'}}>{s.ko.slice(0, -3)}<wbr/>단음계</span> : t(s.en, s.ko)}</button>)}</div>
      <div style={{maxWidth:320,margin:'0 auto'}}><KeyRing sel={sel} onPick={(k) => { stop(); setSel(k); }} o={{ shape: true, plain: true, pat: sh.pat, names: cbRingNames(sel, sh), only: true, ghost: true, labFs: tinyS ? 30 : 24, center: (C) => <text x={C} y={C + 7} textAnchor="middle" fontSize="22" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(prettyNote(tn))}</text> }}
        label={t('The keyboard clock with the ' + sh.full(prettyNote(tn)) + ' scale drawn as a shape.', '건반 시계: ' + sh.full(prettyNote(tn)) + '가 모양으로 그려져 있어요.')}/></div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'6px 0 2px'}}>{names ? [...names, names[0]].map((n, i) => <React.Fragment key={i}>{i ? ' ' : ''}<span style={{color:cbAcc(n) ? PEN_C : BK.ink}}>{cbNoteEl(n)}</span></React.Fragment>) : t('Every note, white and black, a half step each', '흰건반과 검은건반 모두, 반 걸음씩')}</div>
      {downNames && <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted}}>{t('Coming down: ', '내려올 때: ')}{cbDown(downNames).map((n, i) => <React.Fragment key={i}>{i ? ' ' : ''}{cbNoteEl(n)}</React.Fragment>)}</div>}
      <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,margin:'2px 0 8px'}}>{sh.down ? t('up: ', '올라갈 때: ') : ''}{cbSteps(sh.pat)}</div>
      {dbl && <div data-cb="double-sharp" style={{textAlign:'center',fontSize:13,color:BK.ink,lineHeight:1.45,margin:'-2px auto 8px',maxWidth:440,textWrap:'pretty'}}>{LANG === 'ko'
        ? <>{cbNoteEl(dbl)}는 {dbl[0]} 겹샤프예요: {dbl[0]}에서 반 걸음 두 번 올린 음이라 {cbSx(cbPlayedOn(dbl))} 건반에서 쳐요. 글자는 한 번씩이라 {cbSx(cbPlayedOn(dbl))}로 쓰지 않아요.</>
        : <>{cbNoteEl(dbl)} is {dbl[0]} double sharp: two half steps up from {dbl[0]}, played on the key {cbSx(cbPlayedOn(dbl))}. Each letter once, so it is not written {cbSx(cbPlayedOn(dbl))}.</>}</div>}
      <div style={{display:'flex',justifyContent:'center'}}><button className="ghost-btn" style={{minHeight:44}} onClick={() => { stop(); stop.claim(); timers.current = pbPlayMidi(cbMidi(sel, sh), 120); }}>{t('▶ Listen: up and down', '▶ 듣기: 올라갔다 내려와요')}</button></div>
    </div>
  );
}
// page 5 on screen: walk round the circle, one key at a time (its key signature, its scale)
function CbCirclePad() {
  const [sel, setSel] = useState('C');
  const timers = useRef([]);
  const stop = cbUseOneSound(timers);
  const pick = (k) => { stop(); setSel(k); };
  const step = (d) => pick(FIFTHS[(FIFTHS.indexOf(sel) + d + 12) % 12]);
  const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0];
  return (
    <div className="try-box" style={actBox} data-cb="circle-pad">
      <div style={actTitle}>{t('Walk round the circle', '5도권을 한 칸씩')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{t('Tap a key on the circle, or step clockwise or anticlockwise: see its key signature and hear its scale.', '5도권에서 조를 누르거나, 시계 방향이나 반시계 방향으로 한 칸씩 가요. 조표를 보고 음계를 들어요.')}</div>
      <div style={{maxWidth:330,margin:'0 auto'}}><FifthsRing sel={sel} onPick={pick} o={{ filled: [], twins: true, minors: true }} label={t('The circle of fifths, ' + skgKeyName(sel) + ' ringed; inside each key, its relative minor.', '5도권: ' + skgKeyName(sel) + '에 동그라미. 조마다 안쪽에 그 나란한조.')}/></div>
      <div style={{maxWidth:300,margin:'4px auto 0'}}><KSStaff count={sg.count} type={sg.type}/></div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,margin:'2px 0 8px',textWrap:'balance'}}>{cbKeyLine(sel)}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => step(-1)}>{t('↺ Anticlockwise', '↺ 반시계 방향')}</button>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => step(1)}>{t('Clockwise ↻', '시계 방향 ↻')}</button>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => { stop(); stop.claim(); timers.current = pbPlayMidi(pbScaleMidi(sel), 110); }}>{t('▶ Listen', '▶ 듣기')}</button>
      </div>
    </div>
  );
}
// a link inside the screen book: keeps the language and a student link's lock (a student must not land in the teacher view)
const cbHref = (q) => { let lock = false; try { lock = new URLSearchParams(location.search).get('lock') === '1'; } catch (e) {} return '?' + q + (LANG === 'ko' ? '&lang=ko' : '') + (lock ? '&lock=1' : ''); };
// a tool of the Toolbox inside a page, on screen (the order builder has no box of its own: it gets one)
const CB_BOXLESS = ['sharps-order', 'flats-order'];
const cbTool = (id) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null;
  return CB_BOXLESS.includes(id) ? <div className="try-box" style={actBox} data-cb-tool={id}><tl.C/></div> : <div data-cb-tool={id}><tl.C/></div>; };
// a tool's name: on screen, a chip that opens it; printed, its name
const cbToolLink = (id, scr) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null;
  return scr ? <a key={id} href={cbHref('tool=' + id)} style={{display:'inline-flex',alignItems:'center',minHeight:44,padding:'8px 14px',fontSize:14,fontWeight:800,lineHeight:1.25,border:'1.5px solid var(--navy-line)',borderRadius:22,background:'#fff',color:'var(--navy)',textDecoration:'none',whiteSpace:'normal',textAlign:'left'}}><span>{cbSx(tl.title)}</span></a>
    : <span key={id}>{cbSx(tl.title)}</span>; };

// ── the pictures ──
// every major key's scale, in the circle's order; the keys with two names sit together (B and C♭, F♯ and G♭, C♯ and D♭)
const CB_TABLE = ['C', 'G', 'D', 'A', 'E', 'B', 'Cb', 'F#', 'Gb', 'C#', 'Db', 'Ab', 'Eb', 'Bb', 'F'];
const CB_TWIN_FIRST = ['B', 'F#', 'C#'];
function CbScaleTable({ hl }) {
  const scr = lbScreen(), fs = scr ? 13 : 15, rh = scr ? 24 : 21.5;   // on screen the key column goes: degree 1 is the key
  const cell = { textAlign:'center', fontSize:fs, fontWeight:800, lineHeight:rh + 'px', fontVariantNumeric:'lining-nums' };
  const cols = scr ? 'repeat(7,minmax(0,1fr)) 30px' : '62px repeat(7,1fr) 50px';
  return <div role="table" aria-label={t('Every major scale, in the order of the circle of fifths: C, G, D, A, E, B and C flat, F sharp and G flat, C sharp and D flat, A flat, E flat, B flat, F. Each row is one scale’s seven notes; the sharps and flats are coral. Keys with two names sit together.', '모든 장음계를 5도권 순서로: C, G, D, A, E, B와 C♭, F♯와 G♭, C♯와 D♭, A♭, E♭, B♭, F. 한 줄이 음계 하나의 일곱 음이고, 샤프와 플랫은 산호색이에요. 이름이 둘인 조는 나란히 있어요.')} style={{width:'100%',minWidth:0,maxWidth:scr ? 420 : 470,margin:'0 auto'}}>
    <div style={{display:'grid',gridTemplateColumns:cols,borderBottom:'1.6px solid ' + BK.ink}}>
      {!scr && <span style={{...cell,fontSize:11,color:BK.muted,...VIC_CAPS,letterSpacing:'0.08em'}}>{t('Key', '조')}</span>}
      {[1, 2, 3, 4, 5, 6, 7].map(d => <span key={d} style={{...cell,fontSize:12,color:BK.muted}}>{d}</span>)}
      <span style={{...cell,fontSize:11,color:BK.muted}}>♯ ♭</span>
    </div>
    {CB_TABLE.map((k) => { const sg = KEY_SIGS.find(x => x.major === k), on = hl === k;
      return <div key={k} data-cb-row={k} style={{display:'grid',gridTemplateColumns:cols,borderBottom:(CB_TWIN_FIRST.includes(k) ? '0' : '0.8px') + ' solid ' + BK.hair,background:on ? 'rgba(38,41,107,0.06)' : 'transparent',boxShadow:on ? 'inset 0 0 0 1.6px ' + BK.ink : 'none'}}>
        {!scr && <span style={{...cell,fontFamily:LB_SERIF,fontWeight:900,fontSize:fs + 1.5,textAlign:'left',paddingLeft:6}}>{cbSx(prettyNote(k))}</span>}
        {spellScale(k).map((n, i) => <span key={i} style={{...cell,color:cbAcc(n) ? PEN_C : BK.ink,fontWeight:cbAcc(n) || (scr && !i) ? 900 : 700,...(scr && !i ? { fontFamily:LB_SERIF, fontSize:fs + 1.5 } : {})}}>{cbSx(prettyNote(n))}</span>)}
        <span style={{...cell,fontSize:fs - 1.5,color:BK.muted}}>{sg.count ? cbSx(sg.count + (sg.type === 'sharp' ? '♯' : '♭')) : '0'}</span>
      </div>; })}
  </div>;
}
// all the key signatures at once: the seven sharps and the seven flats in order, treble and bass, with the major key
// whose signature ends at each sign under it
const CB_SIGKEYS = { sharp: ['G', 'D', 'A', 'E', 'B', 'F#', 'C#'], flat: ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'] };
function CbSigs() {
  const scr = lbScreen();
  const one = (type, clef) => <div key={type + clef} style={{minWidth:0,width:'100%',maxWidth:scr ? 272 : 220,margin:'0 auto'}}>
    <KSStaff count={7} type={type} clef={clef} numbers/>
    <svg viewBox="0 0 170 16" aria-hidden="true" style={{width:'100%',maxWidth:272,display:'block',margin:'0 auto'}}>
      <text x="6" y="11" fontSize="8.5" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('key', '조')}</text>
      {CB_SIGKEYS[type].map((k, i) => { const n = prettyNote(k); return <text key={k} x={56 + i * 15} y="11" textAnchor="middle" fontSize="8.5" fontWeight="900" fill={PEN_N} style={{fontFamily:'Inter, sans-serif'}}>{n[0]}{n.length > 1 && <tspan fontSize="12.5" fontWeight="400" style={{fontFamily:MUSIC_FONT}}>{n.slice(1)}</tspan>}</text>; })}
    </svg></div>;
  const head = (en, ko, order) => <div style={{gridColumn:'1 / -1',textAlign:'center',fontSize:scr ? 14 : 15,fontWeight:900,color:BK.ink,marginTop:4}}>{t(en, ko)} <span style={{color:PEN_C,letterSpacing:'0.08em'}}>{order}</span></div>;
  return <div role="img" aria-label={t('The seven sharps in order, F C G D A E B, on the treble and the bass staff, numbered 1 to 7; under each sign, the major key whose signature ends there: G, D, A, E, B, F sharp, C sharp. Then the seven flats in order, B E A D G C F, with F, B flat, E flat, A flat, D flat, G flat, C flat.', '샤프 일곱 개를 순서대로(F C G D A E B) 높은음자리표와 낮은음자리표 오선에, 1부터 7까지 번호를 붙여 그렸어요. 기호마다 아래에, 조표가 거기서 끝나는 장조: G, D, A, E, B, F♯, C♯. 그다음 플랫 일곱 개를 순서대로(B E A D G C F), 장조는 F, B♭, E♭, A♭, D♭, G♭, C♭.')}
    style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:scr ? 6 : '4px 22px',width:'100%',maxWidth:620,margin:'0 auto'}}>
    {head('Sharps:', '샤프:', 'F C G D A E B')}{one('sharp', 'treble')}{one('sharp', 'bass')}
    {head('Flats:', '플랫:', 'B E A D G C F')}{one('flat', 'treble')}{one('flat', 'bass')}
    <div style={{gridColumn:'1 / -1',textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted,marginTop:2,textWrap:'balance'}}>{t('key: the major key whose key signature ends at the sign above it', '조: 조표가 바로 위 기호에서 끝나는 장조')}</div>
  </div>;
}
// a scale shape on its own small clock, with its name, notes and steps (pages 6 and 7)
function CbShapeFig({ sh, k, w = 196 }) {
  const scr = lbScreen(), names = cbNames(k, sh), tn = cbTonic(k, sh), down = sh.down ? cbSpell7(tn, sh.down) : null;
  return <div data-cb-fig={sh.id + (k === sh.at ? '' : '-' + k)} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:2,minWidth:0}}>
    <div style={{width:'100%',maxWidth:scr ? 220 : w}}><KeyRing sel={k} o={{ shape: true, plain: true, pat: sh.pat, names: cbRingNames(k, sh), only: true, labFs: 26, center: (C) => <text x={C} y={C + 8} textAnchor="middle" fontSize="26" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(prettyNote(tn))}</text> }}
      label={t(sh.full(prettyNote(tn)) + ' on the keyboard clock.', '건반 시계의 ' + sh.full(prettyNote(tn)) + '.')}/></div>
    <b style={{fontFamily:LANG === 'ko' ? 'inherit' : LB_SERIF,fontVariantNumeric:'lining-nums',fontSize:LANG === 'ko' ? 15 : 16.5,color:BK.ink,lineHeight:1.15,textAlign:'center'}}>{cbSx(sh.full(prettyNote(tn)))}</b>
    <span style={{display:'flex',gap:'0 6px',flexWrap:'wrap',justifyContent:'center',fontSize:13,fontWeight:800,color:BK.ink,lineHeight:1.3}}>{names ? names.map((n, i) => <span key={i} style={{color:cbAcc(n) ? PEN_C : BK.ink}}>{cbNoteEl(n)}</span>) : t('every note, white and black', '흰건반과 검은건반 모두')}</span>
    <span style={{fontSize:11.5,fontWeight:700,color:BK.muted,textAlign:'center',wordSpacing:'0.15em'}}>{sh.down ? t('up: ', '올라갈 때: ') : ''}{cbSteps(sh.pat)}</span>
    {down && <span style={{display:'flex',gap:'0 5px',flexWrap:'wrap',justifyContent:'center',fontSize:12,fontWeight:700,color:BK.muted,lineHeight:1.3}}><span>{t('down:', '내려올 때:')}</span>{cbDown(down).map((n, i) => <span key={i}>{cbNoteEl(n)}</span>)}</span>}
  </div>;
}

// ── the book ──
function cbScalesPages(scr = false) {
  const ch = 'scales', cid = 'p-scales', X = X5, head = cbRight(cid), book = cbBookName();
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;
  const P = (no, kicker, title, frag) => <LbPage key={no} no={no} chId={ch} head={head} book={book} kicker={kicker} title={title}>{frag.props.children}</LbPage>;
  const ringCap = (txt) => <div style={{fontSize:13.5,fontWeight:800,color:BK.ink,textAlign:'center',lineHeight:1.35,maxWidth:280,textWrap:'balance'}}>{txt}</div>;

  // p1: the rule and the whole: the clock (every major scale, one shape) and the circle (every key in order)
  const p1 = <LbPic h={330}><div role="img" aria-label={t('Two rings. Left, the keyboard clock: the twelve keys in a ring, C major drawn as one shape, its two half steps coral. Right, the circle of fifths: the twelve major keys, C at the top; from C, one more sharp each step clockwise, one more flat anticlockwise.', '원 두 개. 왼쪽은 건반 시계: 열두 건반이 원을 이루고, C장조 음계가 모양 하나로 그려져 있고 반 걸음 둘은 산호색. 오른쪽은 5도권: 열두 장조, 맨 위에 C. C에서 시계 방향으로 한 칸마다 샤프 하나 더, 반시계 방향으로 플랫 하나 더.')}
    style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:26,width:'100%',maxWidth:630,alignItems:'start'}}>
    <div aria-hidden="true" style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}><div style={{width:'100%',maxWidth:290}}><KeyRing sel="C" o={{ shape: true, nums: true, numFs: 17, center: (C) => <text x={C} y={C + 8} textAnchor="middle" fontSize="26" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>C</text> }}/></div>
      {ringCap(LANG === 'ko' ? <><b>건반 시계</b>: 한 옥타브의 열두 건반을 둥글게 놓고, 시계 방향으로 한 칸이 반 걸음. 모든 장음계는 그 위의 같은 모양이에요.</> : <><b>Keyboard clock</b>: one octave’s twelve keys in a ring, each place clockwise a half step higher. Every major scale is one shape on it.</>)}</div>
    <div aria-hidden="true" style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}><div style={{width:'100%',maxWidth:290}}><FifthsRing o={{ filled: [], paper: true, twins: true }}/></div>
      {ringCap(t('Every key in order: from C, one more sharp or flat each step.', '모든 조를 순서대로: C에서 한 칸마다 샤프나 플랫이 하나씩 더.'))}</div>
  </div></LbPic>;

  // p2: the rule, on C
  const p2 = <LbPic h={280}><div style={{width:'100%',maxWidth:420,margin:'0 auto',display:'flex',flexDirection:'column',gap:12}}>
    <SscKeys start="C" o={{ nums: true, steps: true, H: 150, tonicInk: PEN_N }} label={t('C major on the keys, numbered 1 to 8, with every step under the keys: whole, whole, half, whole, whole, whole, half. The two half steps are E F (3 to 4) and B C (7 to 8).', '건반의 C장조 음계, 1에서 8까지 번호. 건반 아래에 걸음마다: 온, 온, 반, 온, 온, 온, 반. 반 걸음 둘은 E F(3과 4 사이)와 B C(7과 8 사이).')}/>
      <SscStaff start="C" o={{ under: 'nums', tonic: false, tonicInk: PEN_N, tonicLabel: t('tonic', '으뜸음'), gap: 40 }} label={t('C major on the treble staff, each note numbered under it, 1 to 8; under the two Cs, the word tonic.', '높은음자리표 오선의 C장조 음계, 음마다 아래에 번호 1에서 8. 두 C 아래에 으뜸음.')}/>
  </div></LbPic>;

  // p3: any key: D major built from the rule, and every major scale at once
  const p3 = <LbPic h={396}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1.05fr 1.1fr',gap:20,alignItems:'center',width:'100%',maxWidth:690}}>
    <div style={{display:'flex',flexDirection:'column',gap:6,alignItems:'center',minWidth:0}}>
      <b style={{fontFamily:LB_SERIF,fontSize:17,color:BK.ink}}>{t('D major from the rule', '규칙으로 만든 D장조')}</b>
      <div style={{width:'100%',maxWidth:340}}><SscKeys start="D" o={{ nums: true, steps: true, coral: [2, 6], H: 170, tonicInk: PEN_N, stepFs: scr ? 17 : 13 }} label={t('D major on the keys: D E F sharp G A B C sharp D, numbered 1 to 8, the steps under them. Degrees 3 and 7, F sharp and C sharp, are coral: the steps need them.', '건반의 D장조: D E F♯ G A B C♯ D, 1에서 8까지 번호, 아래에 걸음. 3번과 7번 음 F♯와 C♯는 산호색: 걸음을 맞추려면 이 두 음이 필요해요.')}/></div>
      <div style={{fontSize:13,fontWeight:800,color:BK.muted,textAlign:'center',lineHeight:1.35,maxWidth:300,textWrap:'balance'}}>{X('E to F is only a half step, so 3 is F♯; B to C is a half step, so 7 is C♯.', 'E에서 F는 반 걸음뿐이라 3번 음은 F♯, B에서 C도 반 걸음이라 7번 음은 C♯.')}</div>
    </div>
    <div style={{minWidth:0}}><CbScaleTable hl="D"/></div>
  </div></LbPic>;

  // p4: every key signature at once
  const p4 = <LbPic h={392}><CbSigs/></LbPic>;

  // p5: the circle of fifths
  const legend = (sym, en, ko) => <div style={{display:'flex',gap:10,alignItems:'baseline',fontSize:scr ? 15 : 16.5,lineHeight:1.45,color:BK.ink}}><b style={{fontSize:22,color:PEN_N,flex:'0 0 24px',textAlign:'center'}}>{sym}</b><span>{X(en, ko)}</span></div>;
  const legends = <div style={{display:'flex',flexDirection:'column',gap:scr ? 10 : 16,width:'100%'}}>
      {legend('↻', 'Clockwise from C: each key a 5th higher, one more sharp.', 'C에서 시계 방향: 한 칸마다 5도 위, 샤프 하나 더.')}
      {legend('↺', 'Anticlockwise from C: each key a 5th lower, one more flat.', 'C에서 반시계 방향: 한 칸마다 5도 아래, 플랫 하나 더.')}
      {legend('○', 'Inside: each key’s relative minor, three half steps lower (C and A minor).', '안쪽: 조마다 그 나란한조, 반 걸음 세 개 아래(C와 A단조).')}
      {legend('↓', 'At the bottom they meet: F♯ major (6 sharps) and G♭ major (6 flats) sound the same and are played on the same piano keys.', '맨 아래에서 만나요: F♯장조(샤프 6개)와 G♭장조(플랫 6개)는 소리가 같고 같은 건반에서 쳐요.')}
    </div>;
  const p5 = <LbPic h={330}><div style={{display:'grid',gridTemplateColumns:'1.3fr 1fr',gap:22,alignItems:'center',width:'100%',maxWidth:710}}>
    <div style={{width:'100%',maxWidth:380,margin:'0 auto'}}><FifthsRing o={{ filled: [], paper: true, twins: true, minors: true }} label={t('The circle of fifths: the twelve major keys in a ring, each with its relative minor inside it, C at the top with no sharps or flats; clockwise G 1 sharp, D 2, A 3, E 4, B 5 (also C flat, 7 flats), F sharp 6; anticlockwise F 1 flat, B flat 2, E flat 3, A flat 4, D flat 5 (also C sharp, 7 sharps), G flat 6. F sharp and G flat share the bottom.', '5도권: 열두 장조가 원을 이루고, 조마다 안쪽에 그 나란한조가 있어요. 맨 위 C는 샤프도 플랫도 없어요. 시계 방향으로 G 샤프 1, D 2, A 3, E 4, B 5(C♭은 플랫 7), F♯ 6. 반시계 방향으로 F 플랫 1, B♭ 2, E♭ 3, A♭ 4, D♭ 5(C♯은 샤프 7), G♭ 6. F♯와 G♭은 맨 아래 한 자리.')}/></div>
    {legends}
  </div></LbPic>;

  // p6 and p7: other shapes on the same clock
  // (printed only: on screen the pad shows them one at a time)
  const fig = (w) => ([id, k]) => { const sh = CB_SHAPES.find(x => x.id === id); return <CbShapeFig key={id + (k || '')} sh={sh} k={k || sh.at} w={w}/>; };
  const p6 = <LbPic h={300}><div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:'6px 14px',width:'100%',maxWidth:640,alignItems:'start'}}>{[['nat'], ['harm'], ['mel']].map(fig(196))}</div></LbPic>;
  const p7 = <LbPic h={520}><div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:'4px 40px',width:'100%',maxWidth:520,alignItems:'start'}}>{[['major'], ['penta'], ['penta', 'Gb'], ['chrom']].map(fig(186))}</div></LbPic>;

  // p8: the steps, with the tools for each
  const STEPS = [
    [t('First', '처음에'), X('C, G and F major, and their key signatures', 'C, G, F장조와 그 조표'), X('Build each from the rule (Any key); say its sharps or flats (Key signatures).', '규칙으로 하나씩 만들고(어느 음에서나 장음계), 샤프나 플랫을 말해요(조표).'), ['ssc-steps', 'ssc-g', 'ssc-f', 'skg-five'], ['C', 'G', 'F']],
    [t('Then', '그다음에'), X('D and B♭ major; A, E, D and G minor', 'D장조와 B♭장조, A단조·E단조·D단조·G단조'), X('The order of sharps and flats (Key signatures); a major key’s relative minor, natural and harmonic (Minor scales).', '샤프와 플랫의 순서(조표), 장조의 나란한조, 자연단음계와 화성단음계(단음계).'), ['build-major', 'sharps-order', 'flats-order', 'relative-minor', 'build-minor'], ['D', 'Bb', 'Am', 'Em', 'Dm', 'Gm']],
    [t('Further', '더 나아가서'), X('Up to four sharps and four flats, and their minors', '샤프 넷, 플랫 넷까지의 장조와 그 나란한조'), X('The circle of fifths; placing a key signature (Key signatures); the melodic minor (Minor scales); the major pentatonic on C and G (Other scales).', '5도권, 조표 자리 찾기(조표), 가락단음계(단음계), C와 G의 장조 5음음계(다른 음계).'), ['circle-fifths', 'place-it', 'minor-forms', 'csx-penta', 'scale-finder'], ['A', 'E', 'Eb', 'Ab', 'Bm', 'F#m', 'C#m', 'Cm', 'Fm']],
    [t('Later', '나중에'), X('Every key, major and minor', '모든 장조와 단조'), X('All fifteen key signatures (The circle of fifths); double sharps (G♯ minor’s F𝄪); the chromatic scale (Other scales); the modes.', '조표 15개 전부(5도권), 겹샤프(G♯단조의 F𝄪), 반음계(다른 음계), 선법.'), ['all-keys', 'chromatic', 'modes'], null],
  ];
  const coin = (k) => { const m = /m$/.test(k), n = prettyNote(m ? k.slice(0, -1) : k); return <span key={k} style={{display:'inline-flex',alignItems:'center',justifyContent:'center',minWidth:scr ? 34 : 38,height:scr ? 34 : 38,padding:'0 6px',borderRadius:19,border:'1.6px solid ' + PEN_N,background:m ? '#fff' : PEN_N,color:m ? PEN_N : '#fff',fontFamily:LB_SERIF,fontWeight:900,fontSize:scr ? 15 : 16,fontVariantNumeric:'lining-nums'}}><span>{n[0]}{n.length > 1 ? tnSign(n[1] === '♯' ? '#' : 'b') : null}{m ? <span style={{fontFamily:'Inter, sans-serif',fontSize:'0.8em',fontWeight:800}}>m</span> : null}</span></span>; };
  const coinKey = <div style={{display:'flex',gap:8,alignItems:'center',flexWrap:'wrap',fontSize:13,fontWeight:700,color:BK.muted,margin:'0 0 2px'}}>{coin('C')}<span>{t('a major key', '장조')}</span>{coin('Am')}<span>{t('a minor key', '단조')}</span></div>;
  const ladder = <div className="cb-ladder" style={{display:'flex',flexDirection:'column',flex:scr ? undefined : '1 0 auto',borderTop:'3px double ' + BK.ink,borderBottom:'3px double ' + BK.ink}}>
    {STEPS.map(([g, keys, what, tools, coins], i) => <div key={i} style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '118px 1fr',gap:scr ? 4 : 14,padding:scr ? '10px 4px' : '12px 8px',flex:scr ? undefined : '1 0 auto',borderTop:i ? '0.8px solid ' + BK.hair : 'none',alignContent:'center',alignItems:'start'}}>
      <div style={{fontFamily:LANG === 'ko' ? 'inherit' : LB_SERIF,fontStyle:LANG === 'ko' ? 'normal' : 'italic',fontWeight:LANG === 'ko' ? 800 : 700,fontSize:scr ? 19 : 22,color:BK.ink,lineHeight:1.1}}>{g}</div>
      <div style={{display:'flex',flexDirection:'column',gap:5,minWidth:0}}>
        <div style={{fontSize:scr ? 16 : 17.5,fontWeight:900,color:BK.ink,lineHeight:1.3}}>{keys}</div>
        {coins ? <div style={{display:'flex',flexWrap:'wrap',gap:6,margin:'2px 0'}}>{coins.map(coin)}</div>
          : <div style={{display:'flex',alignItems:'center',gap:8,margin:'2px 0',fontSize:13,fontWeight:800,color:BK.muted}}><div style={{width:38,flex:'0 0 auto'}}><FifthsRing o={{ filled: FIFTHS, paper: true, bare: true }}/></div>{t('all 15 keys', '15개 조 모두')}</div>}
        <div style={{fontSize:scr ? 14 : 15,color:BK.ink,lineHeight:1.4}}>{what}</div>
        <div style={{display:'flex',flexWrap:'wrap',gap:scr ? 8 : '2px 8px',alignItems:'center',fontSize:13,fontWeight:800,color:BK.muted,lineHeight:1.45}}>
          {!scr && <span style={{color:PEN_C,...VIC_CAPS,fontSize:10,letterSpacing:'0.12em'}}>{t('Tools', '도구')}</span>}
          {scr ? tools.map(id => cbToolLink(id, true)) : tools.map((id, j) => <span key={id} style={{whiteSpace:'nowrap'}}>{j ? '· ' : ''}{cbToolLink(id, false)}</span>)}
        </div>
      </div>
    </div>)}
  </div>;

  // the five checks
  const ic = {
    steps: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => { const x = 6 + i * 21, c = i === 2 ? PEN_C : PEN_N; return '<path d="M' + x + ' 18 L' + x + ' 24 L' + (x + 17) + ' 24 L' + (x + 17) + ' 18" fill="none" stroke="' + c + '" stroke-width="' + (i === 2 ? 2.8 : 2) + '" stroke-linejoin="round"/>'; }).join('') }],
    any: [{ k: 'raw', svg: '<circle cx="46" cy="20" r="15" fill="none" stroke="' + PEN_N + '" stroke-width="2"/>' + [0, 2, 4, 5, 7, 9, 11].map(s => { const a = (-90 + s * 30) * Math.PI / 180; return '<circle cx="' + (46 + 15 * Math.cos(a)).toFixed(1) + '" cy="' + (20 + 15 * Math.sin(a)).toFixed(1) + '" r="' + (s ? 2.6 : 4) + '" fill="' + PEN_N + '"/>'; }).join('') + '<path d="M66 12 A22 22 0 0 1 66 28" fill="none" stroke="' + PEN_C + '" stroke-width="2.2" stroke-linecap="round"/><path d="M63 26 L66 29 L69 25" fill="none" stroke="' + PEN_C + '" stroke-width="2" stroke-linecap="round"/>' }],
    sig: [{ k: 'raw', svg: '<text x="46" y="30" text-anchor="middle" font-family="' + MUSIC_FONT.replace(/"/g, "'") + '" font-size="26" fill="' + PEN_C + '">♯♯♯</text>' }],
    circle: [{ k: 'raw', svg: '<circle cx="46" cy="20" r="15" fill="none" stroke="' + PEN_N + '" stroke-width="1.6" stroke-dasharray="3 3"/>' + Array.from({ length: 12 }, (_, i) => { const a = (-90 + i * 30) * Math.PI / 180; return '<circle cx="' + (46 + 15 * Math.cos(a)).toFixed(1) + '" cy="' + (20 + 15 * Math.sin(a)).toFixed(1) + '" r="' + (i === 0 ? 4.2 : 2.6) + '" fill="' + (i === 0 ? PEN_C : PEN_N) + '"/>'; }).join('') }],
    minor: [{ k: 'raw', svg: '<text x="46" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="17" font-weight="900" fill="' + PEN_N + '">C → Am</text>' }],
  };
  const checksRows = [
    ['steps', t('I can say the major scale’s steps: whole, whole, half, whole, whole, whole, half', '장음계의 걸음을 말할 수 있어요: 온, 온, 반, 온, 온, 온, 반')],
    ['any', t('I can build a major scale from any note, using each letter once', '글자를 한 번씩 써서, 어느 음에서나 장음계를 만들 수 있어요')],
    ['sig', t('I can say the order of sharps and of flats, and name the major key from its key signature', '샤프와 플랫의 순서를 말하고, 조표를 보고 장조 이름을 말할 수 있어요')],
    ['circle', t('I can find a key on the circle of fifths and say its sharps or flats', '5도권에서 조를 찾아 그 샤프나 플랫을 말할 수 있어요')],
    ['minor', t('I can find a major key’s relative minor and play it, natural and harmonic', '장조의 나란한조를 찾아 자연단음계와 화성단음계로 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? cbNbKo(x) : cbNbEn(x)]);

  return [
    <LbPage key="1" no={1} chId={ch} head={head} book={book}>
      <LbOnly print><div data-ch={cid}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>{(TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + cbBookName()).toUpperCase()}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales and keys', '스케일과 조')}</div>
      </div></LbOnly>
      <LbSay size={17.5}>{LANG === 'ko'
        ? <><b>한 가지 규칙</b>으로 모든 장음계를 만들어요. 어느 음에서 시작하든 온, 온, 반, 온, 온, 온,{' '}반 걸음이에요. 장음계의 샤프나 플랫은 그 조의 <b>조표</b>가 되고, <b>5도권</b>에는 열두 장조가 차례로 놓여 있어요.</>
        : <>Every major scale follows <b>one rule</b>: whole, whole, half, whole, whole, whole,{' '}half, from any note. Its sharps or flats are its <b>key signature</b>. The <b>circle of fifths</b> puts the twelve major keys in order.</>}</LbSay>
      <LbLive still={p1} live={<CbKeyPad/>}/>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this book', '이 책에서는')}</div>
          {[[t('The major scale', '장음계'), 2], [t('Any key', '어느 음에서나 장음계'), 3], [t('Key signatures', '조표'), 4], [t('The circle of fifths', '5도권'), 5], [t('Minor scales', '단음계'), 6], [t('Other scales', '다른 음계'), 7], [t('Practise in steps', '단계별로 연습하기'), 8], [t('My five checks', '나의 다섯 가지 확인'), 9]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'3px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 책을 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'3px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{cbSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><div style={{display:'flex',justifyContent:'flex-end',alignItems:'center',gap:8,marginTop:'auto'}}>
        <span style={{fontSize:10.5,color:BK.muted}}>{t('this book on screen', '화면으로 보기')}</span>
        <div style={{padding:4,border:'0.8px solid ' + BK.hair,borderRadius:2,background:'#fff',lineHeight:0}}><QR url={bkLink('tool=cb-p-scales')} size={64}/></div>
      </div></LbOnly>
    </LbPage>,

    P(2, t('The rule', '규칙'), t('The major scale', '장음계'), <>
      <LbLive still={p2} live={<SscPad page={2} tonicInk={PEN_N}/>}/>
      <LbDefs items={[
        [t('half step, whole step', '반 걸음, 온 걸음'), X('A half step goes to the very next key, black or white. Its other name is a semitone (S). A whole step is two half steps. Its other name is a tone (T).', '반 걸음은 바로 옆 건반까지 가요. 검은건반이든 흰건반이든 상관없어요. 다른 이름은 반음(반)이에요. 온 걸음은 반 걸음 두 개예요. 다른 이름은 온음(온)이에요.')],
        [t('scale', '음계'), X('Notes in order from one note to the same note an octave higher or lower. A major or minor scale goes step by step, each letter once.', '한 음에서 한 옥타브 위나 아래의 같은 음까지 차례로 가는 음들. 장음계와 단음계는 한 걸음씩, 글자를 한 번씩 써요. 다른 이름은 스케일이에요.')],
        [t('major scale', '장음계'), X('Eight notes going up whole, whole, half, whole, whole, whole, half. In tones and semitones: T T S T T T S.', '여덟 음이 온, 온, 반, 온, 온, 온, 반 걸음으로 올라가요.')],
        [t('degree', '음의 번호'), X('A note’s number in its scale, 1 to 8. Degree 1 is the tonic, the scale’s home note; 8 is the tonic again.', '음계의 음마다 아래에서부터 붙이는 번호, 1에서 8까지. 1번 음과 8번 음은 음계의 집 같은 으뜸음이에요. 다른 이름은 음도예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C major up from C, saying whole or half between each pair of keys.', 'C에서 C장조 음계를 올라가며, 두 건반 사이마다 “온” 또는 “반”이라고 말해요.'),
        X('Find the two half steps, E F and B C, in every octave of the piano.', '피아노의 모든 옥타브에서 반 걸음 둘, E F와 B C를 찾아요.'),
      ]}/>
      <LbRemember>{X('Every major scale: whole, whole, half, whole, whole, whole, half.', '모든 장음계: 온, 온, 반, 온, 온, 온, 반.')}</LbRemember>
    </>),

    P(3, t('Every key', '모든 조'), t('Any key', '어느 음에서나 장음계'), <>
      {live(p3, cbTool('build-major'))}
      <LbDefs items={[
        [t('key', '조'), X('The scale a piece uses, named after its tonic: a piece in D major uses the notes of the D major scale. Every major key’s scale starts on its tonic and follows the same steps.', '곡이 쓰는 음계를 그 으뜸음 이름으로 부른 것. D장조 곡은 D장조 음계의 음을 써요. 어느 장조든 으뜸음에서 시작해 같은 걸음으로 올라가요.')],
        [t('each letter once', '글자는 한 번씩'), X('Name the notes with the seven letters in order, each once. When the steps need a note the plain letter does not give, the letter takes a sharp or a flat: so D major has F♯, never G♭. That note can be a white key: F♯ major has E♯, played on F.', '일곱 글자를 차례로 한 번씩 써서 음이름을 붙여요. 걸음에 맞는 음이 원래 글자의 음과 다르면, 그 글자에 샤프나 플랫을 붙여요. 그래서 D장조에는 G♭이 아니라 F♯가 있어요. 그 음이 흰건반일 수도 있어요. F♯장조의 E♯는 F 건반에서 쳐요.')],
      ]}/>
      <LbPiano steps={[
        X('Play G major up from G with the steps, saying each note’s name. Then F major from F.', 'G에서 걸음대로 G장조 음계를 올라가며 음이름을 하나씩 말해요. 그다음 F에서 F장조 음계를 쳐요.'),
        X('Check each note against its row in the table. Next time: D major, then B♭ major.', '표에서 그 조의 줄과 음을 하나씩 맞춰 봐요. 다음에는 D장조, 그다음 B♭장조를 쳐요.'),
      ]}/>
      <LbRemember>{X('Any key: the same steps, each letter once.', '어느 조든: 같은 걸음, 글자는 한 번씩.')}</LbRemember>
    </>),

    P(4, t('Every key', '모든 조'), t('Key signatures', '조표'), <>
      {live(p4, cbTool('sharps-order'))}
      <LbDefs items={[
        [t('key signature', '조표'), X('The sharps or flats of a key, written after the clef at the start of every line of music, before the time signature. They last the whole piece, in every octave.', '그 조의 샤프나 플랫을 오선마다 맨 앞, 음자리표 바로 뒤에, 박자표보다 먼저 적어요. 곡 끝까지, 모든 옥타브에서 효과가 있어요.')],
        [t('the order', '순서'), X('Sharps always come F C G D A E B. Flats come B E A D G C F, the sharps backwards. A key with three sharps has the first three.', '샤프는 언제나 F C G D A E B 순서예요. 플랫은 B E A D G C F, 샤프 순서를 거꾸로 한 거예요. 샤프가 셋인 조에는 앞의 셋, F♯ C♯ G♯가 붙어요.')],
        [t('naming the key', '조 이름'), X('Sharps: the major key is a half step above the last sharp (its degree 7). Flats: it is the last flat but one, and one flat is F major.', '샤프가 있으면 마지막 샤프보다 반 걸음 위가 장조 이름이에요. 마지막 샤프가 그 조의 7번 음이에요. 플랫이 있으면 끝에서 두 번째 플랫이 장조 이름이에요. 플랫이 하나뿐이면 F장조예요.')],
      ]}/>
      <LbPiano steps={[
        X('Say the order of sharps, playing each one on the keys: F♯ C♯ G♯ D♯ A♯ E♯ B♯ (E♯ is played on F, B♯ on C).', '샤프의 순서를 말하며 건반에서 하나씩 쳐요: F♯ C♯ G♯ D♯ A♯ E♯ B♯(E♯는 F 건반, B♯는 C 건반에서 쳐요).'),
        X('Cover the key names under the signs. Count a key signature’s sharps or flats, name the major key, then play its scale.', '기호 아래의 조 이름을 가려요. 조표의 샤프나 플랫을 하나씩 세고, 장조 이름을 말한 다음 그 음계를 쳐요.'),
      ]}/>
      <LbRemember>{X('Sharps F C G D A E B. Flats B E A D G C F.', '샤프 F C G D A E B. 플랫 B E A D G C F.')}</LbRemember>
    </>),

    P(5, t('Every key', '모든 조'), t('The circle of fifths', '5도권'), <>
      <LbLive still={p5} live={<><CbCirclePad/><div style={{padding:'0 4px 8px'}}>{legends}</div></>}/>
      <LbDefs items={[
        [t('circle of fifths', '5도권'), X('The twelve major keys in a ring, C at the top. Clockwise, each key is a 5th above the one before and has one more sharp or one fewer flat.', '열두 장조를 둥글게 놓은 거예요. 맨 위는 C예요. 시계 방향으로 한 칸마다 5도 위의 조가 오고, 샤프가 하나 늘거나 플랫이 하나 줄어요.')],
        [t('same keys, two names', '같은 건반, 두 이름'), X('Three places on the circle have two names: B and C♭, F♯ and G♭, C♯ and D♭ major are played on the same piano keys. So there are fifteen key signatures. Its other name is enharmonic: one sound, two names.', '5도권의 세 자리는 이름이 둘이에요. B장조와 C♭장조, F♯장조와 G♭장조, C♯장조와 D♭장조는 같은 건반에서 쳐요. 그래서 조표는 모두 15개예요. 다른 이름은 딴이름한소리예요: 소리 하나, 이름 둘.')],
        [t('a 5th', '5도'), X('Five letters up, counting both ends: C D E F G. On the circle every 5th is 7 half steps (a perfect 5th), so a 5th above B is F♯, not F.', '두 음을 모두 세어 다섯 글자 위예요: C D E F G. 5도권의 5도는 언제나 반 걸음 7개(완전5도)라서, B에서 5도 위는 F가 아니라 F♯예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the tonic of each key clockwise, C G D A E B, each a 5th higher (or a 4th lower, to stay in the middle); say how many sharps each has.', '5도권을 따라 시계 방향으로 각 조의 으뜸음을 쳐요: C G D A E B. 한 칸마다 5도 위로, 또는 가운데에 머물려면 4도 아래로 가요. 조마다 샤프가 몇 개인지 말해요.'),
        X('Now anticlockwise from C: F B♭ E♭ A♭ D♭ G♭, saying how many flats.', '이번에는 C에서 반시계 방향으로 쳐요: F B♭ E♭ A♭ D♭ G♭. 조마다 플랫이 몇 개인지 말해요.'),
      ]}/>
      <LbRemember>{X('From C: clockwise one more sharp, anticlockwise one more flat.', 'C에서 시계 방향은 샤프 하나 더, 반시계 방향은 플랫 하나 더.')}</LbRemember>
    </>),

    P(6, t('Other shapes', '다른 모양'), t('Minor scales', '단음계'), <>
      <LbLive still={p6} live={<CbShapesPad ids={['nat', 'harm', 'mel']} first="nat"/>}/>
      <LbDefs items={[
        [t('relative minor', '나란한조'), X('A minor key that starts on degree 6 of a major scale and shares its key signature: A minor is C major’s, three half steps below C. Its natural minor goes T S T T S T T.', '장음계의 6번 음에서 시작하고, 그 장조와 조표가 같은 단조예요. 장조 으뜸음에서 반 걸음 세 개 아래예요(C → A). 조표 그대로 치는 자연단음계의 걸음은 온 반 온 온 반 온 온이에요.')],
        [t('harmonic minor', '화성단음계'), X('The natural minor with degree 7 raised a half step: G♯ in A minor, B♮ (B natural) in C minor. It is written as an accidental, never in the key signature. Degree 6 to 7 is then T+S: a tone and a semitone, 3 half steps.', '자연단음계에서 7번 음을 반 걸음 올린 음계예요. A단조에서는 G♯, C단조에서는 B♮(B 내추럴)로 올려요. 올린 음은 임시표로 적고, 조표에는 넣지 않아요. 그러면 6번 음에서 7번 음까지는 온+반, 온음과 반음을 합한 반 걸음 세 개예요.')],
        [t('melodic minor', '가락단음계'), X('Up: degrees 6 and 7 raised a half step (A minor: F♯ G♯; C minor: A♮ B♮). Down: the natural minor.', '올라갈 때는 6번과 7번 음을 반 걸음 올리고(A단조는 F♯ G♯, C단조는 A♮ B♮), 내려올 때는 자연단음계로 내려와요.')],
        [t('which key?', '어느 조?'), X('A key signature belongs to a major key and its relative minor. A minor piece shows its raised degree 7 (G♯ in A minor) and usually ends on its tonic.', '조표 하나는 장조와 그 나란한조, 두 조의 것이에요. 단조 곡에는 올린 7번 음(A단조의 G♯)이 나오고, 보통 으뜸음으로 끝나요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C major, then A natural minor: the same white keys, a new home note.', 'C장조 음계를 치고, 그다음 A단조 자연단음계를 쳐요: 흰건반은 같고, 집(으뜸음)만 A로 바뀌어요.'),
        X('Play A harmonic minor with G♯, then A melodic minor up and down.', 'G♯를 넣어 A단조 화성단음계를 치고, 그다음 A단조 가락단음계를 올라갔다 내려와요.'),
      ]}/>
      <LbRemember>{X('A relative minor starts on degree 6 and keeps the key signature.', '나란한조는 6번 음에서 시작하고 조표는 그대로예요.')}</LbRemember>
    </>),

    P(7, t('Other shapes', '다른 모양'), t('Other scales', '다른 음계'), <>
      <LbLive still={p7} live={<CbShapesPad ids={['major', 'penta', 'chrom']} first="penta"/>}/>
      <LbDefs items={[
        [t('major pentatonic', '장조 5음음계'), X('A major scale without degrees 4 and 7: five notes, C D E G A in C. Its T+S steps are skips over a letter: E to G, A to C.', '장음계에서 4번과 7번 음을 뺀 음계예요. C에서는 C D E G A, 다섯 음이에요. 온+반은 글자 하나를 건너뛰는 거리예요: E에서 G, A에서 C.')],
        [t('chromatic scale', '반음계'), X('Every note, white and black, a half step each: twelve notes to the octave.', '흰건반과 검은건반을 모두 반 걸음씩 가는 음계예요. 한 옥타브에 열두 음이에요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C major pentatonic, C D E G A, then G major pentatonic, G A B D E.', 'C장조 5음음계 C D E G A를 치고, 그다음 G장조 5음음계 G A B D E를 쳐요.'),
        X('Play G♭ major pentatonic: it is the five black keys.', 'G♭장조 5음음계를 쳐요: 검은건반 다섯 개예요.'),
        X('Play the chromatic scale up from C, every key, white and black.', 'C에서 반음계를 올라가요: 흰건반과 검은건반을 모두 쳐요.'),
      ]}/>
      <LbRemember>{X('Other scales are other shapes on the same clock.', '다른 음계는 같은 시계 위의 다른 모양이에요.')}</LbRemember>
    </>),

    P(8, t('How to practise', '연습하는 방법'), t('Practise in steps', '단계별로 연습하기'), <>
      <LbSay>{X('The rule is the same for every key. Start at First; go up a step when you can show checks 1 to 3 in every key of your step, without the book.', '규칙은 모든 조에서 같아요. ‘처음에’부터 시작해서, 그 단계의 모든 조에서 책을 보지 않고 확인 1~3을 보여 줄 수 있으면 다음 단계로 가요.')}</LbSay>
      {coinKey}
      {ladder}
      <div style={{...VIC_PANEL,padding:'10px 16px',fontSize:15,lineHeight:1.45,color:BK.ink}}>{X('Playing them, with each hand’s fingering, is in Technique: Playing scales and chords.', '음계를 손가락 번호대로 한 손씩, 그다음 양손으로 치는 연습은 테크닉 영역의 ‘스케일과 화음 치기’에 있어요.')}
        {scr && <div style={{marginTop:8}}><a href={cbHref('tool=scale-finder')} style={{display:'inline-flex',alignItems:'center',minHeight:44,padding:'8px 14px',fontSize:14,fontWeight:800,border:'1.5px solid var(--navy-line)',borderRadius:22,background:'#fff',color:'var(--navy)',textDecoration:'none'}}>{t('The scale finder: every scale’s fingering →', '스케일 찾기: 모든 음계의 손가락 번호 →')}</a></div>}</div>
    </>),

    P(9, t('Check-up', '점검'), t('My five checks', '나의 다섯 가지 확인'), <>
      <LbSay>{scr ? t('Show each one at the piano, using steps 1 to 5, in the keys of your step (step 7).', '7단계에서 내가 있는 단계의 조로, 1~5단계를 하나씩 펴고 피아노 앞에서 보여 줘요.') : t('Show each one at the piano, on its page (2 to 6), in the keys of your step (page 8).', '8쪽에서 내가 있는 단계의 조로, 2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, cbSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_cb_scales_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, cbSx(x)])}/>}/>
    </>),
  ];
}
function CbScalesBook() { return <>{cbScalesPages(false)}</>; }
CONCEPT_BOOKS['p-scales'] = CbScalesBook;
// on screen: the opener as the head, then one step a page
function CbScalesLearn() {
  const pages = cbScalesPages(true), opener = pages[0];
  return (
    <Lesson id="cb-p-scales" title={t('Scales and keys', '스케일과 조')} noArt
      intro={t('The rule, every key at once, then the steps to practise it.', '규칙 하나로 모든 조를 한눈에 보고, 단계별로 연습해요.')}
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
TOOLS.push({ id: 'cb-p-scales', ch: 'concept', title: 'Concept book: Scales and keys', blurb: 'The rule, every key at once, and the steps to practise it.', hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + cbBookName(); }, C: () => <CbScalesLearn/> });
TOOL_KO['cb-p-scales'] = ['개념책: 스케일과 조', '규칙 하나, 모든 조를 한눈에, 그리고 단계별 연습.'];
(() => { const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[tl.id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true }); })();
TOOL_CONCEPT['cb-p-scales'] = 'p-scales';
// the Toolbox: a concept's book, right under its name (open on screen, or print)
function CbCard({ cid, onOpen }) {
  const id = CB_TOOL[cid]; if (!id) return null;
  const href = '?book=concept&ch=' + cid + '&lang=en';
  return <div style={{display:'flex',alignItems:'center',gap:10,flexWrap:'wrap',margin:'8px 14px 2px',padding:'8px 12px',border:'1px solid var(--navy-line)',borderRadius:10,background:'#fff'}}>
    <svg width="22" height="18" viewBox="0 0 22 18" aria-hidden="true" style={{flex:'0 0 auto'}}><path d="M11 3 C8 1 4 1 1.5 2 L1.5 16 C4 15 8 15 11 17 C14 15 18 15 20.5 16 L20.5 2 C18 1 14 1 11 3 Z M11 3 L11 17" fill="none" stroke="var(--navy)" strokeWidth="1.6" strokeLinejoin="round"/></svg>
    <div style={{flex:'1 1 200px',minWidth:0}}><div style={{fontSize:14.5,fontWeight:900,color:'var(--navy)'}}>{t('The concept book', '개념책')}</div>
      <div style={{fontSize:12.5,color:'var(--navy-soft)',lineHeight:1.35}}>{t('The rule, every key at once, then the steps to practise it.', '규칙 하나, 모든 조를 한눈에, 그리고 단계별 연습.')}</div></div>
    <div style={{display:'flex',gap:6}}><button className="ghost-btn" style={{minHeight:44}} onClick={() => onOpen(id)}>{t('Open', '열기')}</button>
      <a className="ghost-btn" style={{minHeight:44,display:'inline-flex',alignItems:'center',textDecoration:'none'}} href={href} target="_blank" rel="noopener">{t('Print', '인쇄')}</a></div>
  </div>;
}
