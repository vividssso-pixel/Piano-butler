import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AV (board call 18, the fifth Grade 4 room): Rhythm, Grade 4. Theory of Music Grade 4, Time and Rhythm (Manual of Syllabuses
# 2026, read 26 Oct): note values and rests as before; syncopation (minim, crotchet and quaver values only) and hemiola; barring an
# unbarred phrase; the time signatures 6/4 and 12/8 added; general knowledge: compound quadruple time. The room reuses Rhythm
# Further's pad and lines (R2Pad, R2): the new lines join R2, and R2's lines learn ties.

rep("""const HARMONY_4_DRILL = { id: 'harmony-4', label: 'Chords and Cadences, Grade 4' };   // Build AU""",
    """const HARMONY_4_DRILL = { id: 'harmony-4', label: 'Chords and Cadences, Grade 4' };   // Build AU
const RHYTHM_4_DRILL = { id: 'rhythm-4', label: 'Rhythm, Grade 4' };   // Build AV""")
rep("""  { id: 'harmony-4', label: 'Chords and Cadences, Grade 4', concept: HARMONY_4_DRILL, track: 'start' },   // Build AU""",
    """  { id: 'harmony-4', label: 'Chords and Cadences, Grade 4', concept: HARMONY_4_DRILL, track: 'start' },   // Build AU
  { id: 'rhythm-4', label: 'Rhythm, Grade 4', concept: RHYTHM_4_DRILL, track: 'start' },   // Build AV""")
rep("""'harmony-4': '화음과 종지, Grade 4'""", """'harmony-4': '화음과 종지, Grade 4', 'rhythm-4': '리듬, Grade 4'""")
rep("""'harmony-4': ['harmony-23', 'keys-4'],""", """'harmony-4': ['harmony-23', 'keys-4'], 'rhythm-4': ['rhythm-23'],""")
rep("""'harmony-4': ['Chords, Grade 4', '화음 4'],""", """'harmony-4': ['Chords, Grade 4', '화음 4'], 'rhythm-4': ['Rhythm, Grade 4', '리듬 4'],""")
rep("""  'harmony-4': 'chords cadences grade 4""", """  'rhythm-4': 'rhythm grade 4 syncopation off the beat hemiola 6/4 12/8 compound duple compound quadruple barring bar lines unbarred phrase anacrusis time signature',
  'harmony-4': 'chords cadences grade 4""")
rep("""'harmony-4': 'p-chords', 'harmony-23'""", """'harmony-4': 'p-chords', 'rhythm-4': 'r-beat', 'harmony-23'""")
rep("""    { id: 'rb-23', en: 'Rhythm further', ko: '리듬 한 걸음 더', lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98'], check: 'rhythm-23' },   // Build AM""",
    """    { id: 'rb-23', en: 'Rhythm further', ko: '리듬 한 걸음 더', lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98'], check: 'rhythm-23' },   // Build AM
    { id: 'rb-4', en: 'Rhythm, Grade 4', ko: '리듬, Grade 4', lessons: ['r4-sync', 'r4-hem', 'r4-ts', 'r4-bar'], check: 'rhythm-4' },   // Build AV""")
rep("""  set('4', 'h4-deg h4-inv h4-cad h4-fit');   // Build AU: Chords and Cadences, Grade 4""",
    """  set('4', 'h4-deg h4-inv h4-cad h4-fit');   // Build AU: Chords and Cadences, Grade 4
  set('4', 'r4-sync r4-hem r4-ts r4-bar');   // Build AV: Rhythm, Grade 4""")
# R2's lines learn ties (sound and drawing)
rep("""const r2Props = (key, extra = {}) => { const R = R2[key]; return { items: R.items, unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, so: R.so, ...extra }; };
const r2El = (key, o = {}) => rqStaffEl(R2[key].items, { ...(R2[key].so || {}), ...o });
const r2Play = (key, o = {}) => { const R = R2[key]; return rqRunS(R.items, { unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, ...o }); };""",
    """const r2Props = (key, extra = {}) => { const R = R2[key]; return { items: R.items, unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, ties: R.ties, so: R.ties ? { ...(R.so || {}), ties: R.ties } : R.so, ...extra }; };   // Build AV: ties
const r2El = (key, o = {}) => rqStaffEl(R2[key].items, { ...(R2[key].so || {}), ...(R2[key].ties ? { ties: R2[key].ties } : {}), ...o });
const r2Play = (key, o = {}) => { const R = R2[key]; return rqRunS(R.items, { unit: R.unit, clicks: R.clicks, accentAt: R.accentAt, accent: !!R.accentAt, bpm: R.bpm, ties: R.ties, ...o }); };""")

CH = r'''
// ─── Chapter: Rhythm, Grade 4 (Build AV, 2026-10-26; board call 18, the fifth Grade 4 room) ───
// Syncopation (minims, crotchets and quavers), hemiola, 6/4 and 12/8 (compound duple and compound quadruple), barring an unbarred
// phrase. The lines join Rhythm Further's R2 so its pad, staff and player serve them.
Object.assign(R2, {
  syncA: { items: [['ts', 4], ['e'], ['q'], ['e'], ['q'], ['q'], ['|'], ['q'], ['h'], ['q'], ['|'], ['w'], ['||']], g: 4 },
  syncB: { items: [['ts', 2], ['e'], ['q'], ['e'], ['|'], ['e'], ['q'], ['e'], ['|'], ['q'], ['q'], ['|'], ['h'], ['||']], g: 4 },
  hemA: { items: [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['|'], ['q'], ['h'], ['|'], ['hd'], ['||']], g: 4, ties: [[6, 8]] },
  hemB: { items: [['ts', 3], ['q'], ['p'], ['q'], ['|'], ['hd'], ['|'], ['h'], ['q'], ['|'], ['q'], ['h'], ['|'], ['hd'], ['||']], g: 4, ties: [[8, 10]] },
  e64: { items: [['ts', 6, 4], ['hd'], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['hd'], ['|'], ['hd'], ['hd'], ['||']], g: 4, clicks: 6, accentAt: [0, 3], bpm: 120, so: { countStep: 1, heartStep: 3, countFn: (p) => String(Math.round(p) % 6 + 1) } },
  e128: { items: [['ts', 12, 8], ['e3'], ['e3'], ['qd'], ['qd'], ['|'], ['qd'], ['e3'], ['q'], ['e'], ['qd'], ['||']], g: 4, unit: 0.5, clicks: 12, accentAt: [0, 3, 6, 9], bpm: 72, so: { D: 34, countStep: 0.5, heartStep: 1.5, countFn: r2Cmp(12) } },
});
// time signatures: simple or compound; duple, triple or quadruple
const R4_TS = [['2', '4', 'sd'], ['3', '4', 'st'], ['4', '4', 'sq'], ['6', '8', 'cd'], ['9', '8', 'ct'], ['12', '8', 'cq'], ['6', '4', 'cd'], ['2', '2', 'sd'], ['3', '2', 'st'], ['3', '8', 'st']];
const R4_TSN = { sd: ['simple duple', '홑두박자'], st: ['simple triple', '홑세박자'], sq: ['simple quadruple', '홑네박자'], cd: ['compound duple', '겹두박자'], ct: ['compound triple', '겹세박자'], cq: ['compound quadruple', '겹네박자'] };
const r4TsName = (c) => t(R4_TSN[c][0], R4_TSN[c][1]);
const R4TsSig = ({ top, bot, size = 34 }) => <div style={{display:'inline-flex',flexDirection:'column',alignItems:'center',lineHeight:0.92,fontFamily:'Playfair Display, Georgia, serif',fontWeight:900,fontSize:size,color:BK.ink}}><span>{top}</span><span>{bot}</span></div>;
// unbarred phrases: the notes, the time signature, the beats in a bar (crotchets), the anacrusis (crotchets); compound phrases count quavers
const R4_BAR = [
  { ts: [3], len: 3, an: 0, n: ['q', 'q', 'q', 'h', 'q', 'qd', 'e', 'q', 'hd'] },
  { ts: [4], len: 4, an: 1, n: ['q', 'h', 'q', 'q', 'qd', 'e', 'q', 'q', 'w'] },
  { ts: [2], len: 2, an: 0, n: ['p', 'q', 'q', 'p', 'e', 'q', 'e', 'h'] },
  { ts: [6, 8], len: 3, an: 0, n: ['e3', 'qd', 'q', 'e', 'qd', 'hd'], so: { D: 44 } },
  { ts: [3], len: 3, an: 1, n: ['q', 'q', 'q', 'q', 'h', 'q', 'qd', 'e', 'q', 'h'] },
  { ts: [12, 8], len: 6, an: 0, n: ['qd', 'e3', 'qd', 'qd', 'e3', 'q', 'e', 'qd', 'qd'], so: { D: 30 } },
];
const r4BarAt = (P) => { const out = []; let b = 0; P.n.forEach((k, i) => { b += SRH_LEN[k]; if (i < P.n.length - 1 && Math.abs(((b - P.an) % P.len + P.len) % P.len) < 1e-6 && b > 1e-6) out.push(i); }); return out; };   // after which notes the bar lines go
const r4Items = (P, at) => [['ts', ...P.ts], ...P.n.flatMap((k, i) => (at.includes(i) ? [[k], ['|']] : [[k]])), ['||']];
const r4BarOpts = (P) => { const ok = r4BarAt(P), L = P.n.length, early = ok.map(i => i - 1).filter(i => i >= 0), late = ok.map(i => i + 1).filter(i => i < L - 1);
  return [['ok', ok], ['early', early], ['late', late]].filter(([, at], j, arr) => arr.findIndex(([, a2]) => a2.join() === at.join()) === j); };
const r4BarEl = (P, at, o = {}) => rqStaffEl(r4Items(P, at), { counts: false, hearts: false, ...(P.so || {}), ...o });
const R4_Q = {
  sync: () => { const v = Math.floor(Math.random() * 3); return [
    { prompt: ['Syncopation puts the accent…', '당김음은 강세를 어디에?'], opts: [['on', t('on the beat', '박 위에')], ['off', t('off the beat', '박 사이에')], ['one', t('only on beat 1', '1박에만')]], ans: 'off', cols: 1, yes: ['Off the beat: a note starts between beats and is held over the next one.', '박 사이에: 박과 박 사이에서 시작해 다음 박 위로 이어져요.'], no: ['Syncopation moves the accent off the beat.', '당김음은 강세를 박 사이로 옮겨요.'] },
    { prompt: ['Quaver, crotchet, quaver: which note is syncopated?', '8분음표, 4분음표, 8분음표: 당김음은 어느 음?'], opts: [['a', t('the first quaver', '첫 8분음표')], ['b', t('the crotchet', '4분음표')], ['c', t('the last quaver', '마지막 8분음표')]], ans: 'b', cols: 1, yes: ['The crotchet: it starts on the +, between beats, and is held over beat 2.', '4분음표: + 에서, 박 사이에서 시작해 2박 위로 이어져요.'], no: ['The crotchet starts on the + and is held across the beat: that is the syncopation.', '4분음표가 + 에서 시작해 박을 넘어 이어져요: 그게 당김음.'] },
    { prompt: ['In 4/4, a minim that starts on beat 2 is…', '4/4에서 2박에 시작하는 2분음표는…'], opts: [['yes', t('syncopated', '당김음')], ['no', t('not syncopated', '당김음 아님')]], ans: 'yes', yes: ['Syncopated: it starts on a weak beat and is held over the strong beat 3.', '당김음: 여린박에서 시작해 센박인 3박 위로 이어져요.'], no: ['It starts on weak beat 2 and is held over strong beat 3: syncopated.', '여린박 2에서 시작해 센박 3 위로 이어져요: 당김음.'] }][v]; },
  hem: () => { const v = Math.floor(Math.random() * 2); return [
    { prompt: ['A hemiola makes two bars of 3/4 sound like…', '헤미올라는 3/4 두 마디를 어떻게 들리게 할까요?'], opts: [['32', t('three groups of two', '둘씩 세 묶음')], ['23', t('two groups of three', '셋씩 두 묶음')], ['6', t('six even beats, no groups', '묶음 없이 고른 여섯 박')]], ans: '32', cols: 1, yes: ['Three groups of two, like one bar of 3/2, then back to 3/4.', '둘씩 세 묶음, 3/2 한 마디처럼. 그다음 다시 3/4.'], no: ['The six beats regroup as 2 + 2 + 2: three minims across two bars.', '여섯 박이 2 + 2 + 2로 다시 묶여요: 두 마디에 걸친 2분음표 셋.'] },
    { prompt: ['Where is a hemiola most often found?', '헤미올라는 어디에 가장 자주 나올까요?'], opts: [['cad', t('just before a cadence', '종지 바로 앞')], ['start', t('in the first bar', '첫 마디')], ['44', t('in 4/4 time', '4/4박자')]], ans: 'cad', cols: 1, yes: ['Just before a cadence, in triple time: it slows the phrase into its ending.', '세박자에서 종지 바로 앞: 프레이즈를 끝으로 늦춰 줘요.'], no: ['In triple time, just before a cadence, as in many minuets and courantes.', '세박자에서 종지 바로 앞, 미뉴에트와 쿠랑트에 많이 나와요.'] }][v]; },
  ts: () => { const [a, b, c] = pick(R4_TS), same = Object.keys(R4_TSN).filter(x => x[1] === c[1] && x !== c), sameT = Object.keys(R4_TSN).filter(x => x[0] === c[0] && x !== c), opts = shuffle([c, pick(same), pick(sameT)]);
    return { prompt: [a + '/' + b + ' is…', a + '/' + b + '는…'], sig: [a, b], opts: opts.map(x => [x, r4TsName(x)]), ans: c, cols: 1, yes: [a + '/' + b + ': ' + R4_TSN[c][0] + '.', a + '/' + b + ': ' + R4_TSN[c][1] + '.'],
      no: [a + '/' + b + ' is ' + R4_TSN[c][0] + (c[0] === 'c' ? ': its beat is a dotted note, worth three of the bottom number.' : ': its beat is the note the bottom number names.'), a + '/' + b + '는 ' + R4_TSN[c][1] + (c[0] === 'c' ? ': 한 박은 점음표, 아래 숫자 음표 셋 길이.' : ': 한 박은 아래 숫자가 가리키는 음표.')] }; },
};
const R4_STEP = { sync: ['Off the beat: syncopation', '박 사이로: 당김음'], hem: ['Three twos in two threes: hemiola', '셋 두 개를 둘 셋으로: 헤미올라'], ts: ['6/4 and 12/8', '6/4와 12/8'], bar: ['Bar lines for a phrase', '프레이즈에 마디선 긋기'] };
const r4StepT = (k) => t(R4_STEP[k][0], R4_STEP[k][1]);
// ── step 4: put in the bar lines: which version is right? ──
function R4BarPad({ fixed, onResult }) {
  const [i, setI] = useState(fixed != null ? fixed : 0), [ord, setOrd] = useState(() => shuffle(r4BarOpts(R4_BAR[fixed != null ? fixed : 0]))), [pickd, setPick] = useState(null);
  const P = R4_BAR[i], say = (id) => { if (pickd != null) return; setPick(id); if (onResult) onResult({ ok: id === 'ok' }); };
  const go = (j) => { setI(j); setOrd(shuffle(r4BarOpts(R4_BAR[j]))); setPick(null); };
  return (
    <div className="try-box" style={actBox} data-r4="bar">
      <div style={actTitle}>{r4StepT('bar')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>박자표를 보고 <b>한 마디에 몇 박</b>인지 정해요. 음표를 차례로 더해서 마디가 찰 때마다 마디선. <b>못갖춘마디</b>(첫 마디가 짧은)로 시작하는 프레이즈도 있어요: 그러면 마지막 마디가 그만큼 짧아요.</>
        : <>Read the time signature: <b>how many beats in a bar</b>? Add up the notes in order, and draw a bar line each time a bar is full. Some phrases start with an <b>anacrusis</b> (a short first bar); then the last bar is short by the same amount.</>}</div>
      {fixed == null && spChips(R4_BAR.map((x, j) => [j, t('Phrase ' + (j + 1), (j + 1) + '번')]), i, go)}
      <div style={{fontSize:12.5,fontWeight:900,color:BK.muted,textAlign:'center',margin:'2px 0 4px'}}>{t('Unbarred', '마디선 없이')}</div>
      <div style={{maxWidth:460,margin:'0 auto'}}>{r4BarEl(P, [])}</div>
      <div style={{fontSize:13.5,fontWeight:800,color:BK.ink,textAlign:'center',margin:'10px 0 4px'}}>{t('Which is barred correctly?', '마디선이 맞게 그어진 것은?')}</div>
      <div style={{display:'flex',flexDirection:'column',gap:8}}>{ord.map(([id, at]) => <button key={id} className={'choice-btn' + (pickd == null ? '' : id === 'ok' ? ' good' : id === pickd ? ' bad' : '')} onClick={() => say(id)} style={{padding:'6px 4px'}}><div style={{width:'100%',minWidth:0}}>{r4BarEl(P, at)}</div></button>)}</div>
      {pickd != null && spMsg(pickd === 'ok' ? t('Yes: every bar holds ' + (P.ts[1] === 8 ? P.len * 2 + ' quavers' : P.len + ' crotchet beats') + (P.an ? ', after an anacrusis of ' + P.an + '.' : '.'), '맞아요: 마디마다 ' + (P.ts[1] === 8 ? '8분음표 ' + P.len * 2 + '개' : '4분음표 ' + P.len + '박') + (P.an ? ', 못갖춘마디 ' + P.an + '박 다음부터.' : '.')) : t('Count again: each full bar holds ' + (P.ts[1] === 8 ? P.len * 2 + ' quavers.' : P.len + ' crotchet beats.'), '다시 세요: 꽉 찬 마디는 ' + (P.ts[1] === 8 ? '8분음표 ' + P.len * 2 + '개.' : '4분음표 ' + P.len + '박.')), pickd === 'ok' ? BK.green : BK.coral)}
      {pickd != null && fixed == null && <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" style={spBtn} onClick={() => go((i + 1) % R4_BAR.length)}>{t('▶ Another', '▶ 다른 것')}</button></div>}
    </div>
  );
}
// the time-signature step: the lines, and a question with the signature drawn big
function R4TsPad() {
  const [q, setQ] = useState(null), [pickd, setPick] = useState(null);
  return (<div>
    <R2Pad step="ts4" keys={['e64', 'e128']} title={r4StepT('ts')} note={t('6/4: two dotted-minim beats, each of three crotchets: compound duple. 12/8: four dotted-crotchet beats, each of three quavers: compound quadruple.', '6/4: 점2분음표 두 박, 한 박에 4분음표 셋: 겹두박자. 12/8: 점4분음표 네 박, 한 박에 8분음표 셋: 겹네박자.')}/>
    <div className="try-box" style={actBox} data-r4="ts">
      <div style={actTitle}>{t('Simple or compound? Two, three or four?', '홑박자? 겹박자? 둘, 셋, 넷?')}</div>
      {!q ? <div style={{textAlign:'center'}}><button className="ghost-btn" style={spBtn} onClick={() => { setQ(R4_Q.ts()); setPick(null); }}>{t('▶ A time signature', '▶ 박자표 하나')}</button></div>
        : <><div style={{textAlign:'center',margin:'4px 0 6px'}}><R4TsSig top={q.sig[0]} bot={q.sig[1]} size={40}/></div>
          <div style={{display:'grid',gridTemplateColumns:'1fr',gap:8}}>{q.opts.map(([id, lab]) => <button key={id} className={'choice-btn' + (pickd == null ? '' : id === q.ans ? ' good' : id === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(id); }} style={{padding:'11px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>
          {pickd != null && spMsg(pickd === q.ans ? t(q.yes[0], q.yes[1]) : t(q.no[0], q.no[1]), pickd === q.ans ? BK.green : BK.coral)}
          {pickd != null && <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" style={spBtn} onClick={() => { setQ(R4_Q.ts()); setPick(null); }}>{t('▶ Another', '▶ 다른 것')}</button></div>}</>}
    </div>
  </div>);
}

// ── the pictures on paper ──
const r4PicSync = () => r2Pic('<ellipse cx="14" cy="34" rx="5.5" ry="4" transform="rotate(-20 14 34)" fill="#26296b"/><line x1="19" x2="19" y1="33" y2="10" stroke="#26296b" stroke-width="1.8"/><path d="M19 10 Q26 16 24 24" fill="none" stroke="#26296b" stroke-width="2"/><ellipse cx="38" cy="34" rx="5.5" ry="4" transform="rotate(-20 38 34)" fill="#e4572e"/><line x1="43" x2="43" y1="33" y2="10" stroke="#e4572e" stroke-width="1.8"/><text x="40" y="8" font-size="12" font-weight="900" fill="#e4572e" text-anchor="middle">&gt;</text><ellipse cx="62" cy="34" rx="5.5" ry="4" transform="rotate(-20 62 34)" fill="#26296b"/><line x1="67" x2="67" y1="33" y2="10" stroke="#26296b" stroke-width="1.8"/><path d="M67 10 Q74 16 72 24" fill="none" stroke="#26296b" stroke-width="2"/>');
const r4PicHem = () => r2Pic([0, 1, 2].map(i => '<rect x="' + (4 + i * 25) + '" y="16" width="22" height="12" rx="6" fill="' + (i === 1 ? '#e4572e' : '#26296b') + '"/>').join('') + '<line x1="40" x2="40" y1="8" y2="36" stroke="#26296b" stroke-width="1.5"/>');
const r4PicTs = () => r2Pic('<text x="6" y="20" font-family="Georgia, serif" font-size="15" font-weight="900" fill="#e4572e">12</text><text x="10" y="38" font-family="Georgia, serif" font-size="15" font-weight="900" fill="#26296b">8</text>' + [0, 1, 2, 3].map(i => lsCircleSvg(38 + i * 11, 26, 4.5, 'play', '')).join(''));
const r4PicBar = () => r2Pic([0, 1, 2, 3, 4, 5].map(i => '<ellipse cx="' + (8 + i * 12) + '" cy="30" rx="4.5" ry="3.4" transform="rotate(-20 ' + (8 + i * 12) + ' 30)" fill="#26296b"/>').join('') + '<line x1="32" x2="32" y1="14" y2="38" stroke="#e4572e" stroke-width="2"/><line x1="68" x2="68" y1="14" y2="38" stroke="#e4572e" stroke-width="2"/>');

function r4LbPages(scr = false) {
  const ch = 'rhythm-4', r2c = bkChapterNo('rhythm-23');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks4 = [[r4PicSync(), t('I clap syncopated rhythms and say where the accent moves', '당김음 리듬을 치고, 강세가 어디로 옮겨 가는지 말해요')], [r4PicHem(), t('I hear and clap a hemiola: three twos across two bars of three', '헤미올라를 듣고 쳐요: 세 박 두 마디에 걸친 둘씩 셋')],
    [r4PicTs(), t('I count 6/4 and 12/8 and name any time signature: simple or compound, duple, triple or quadruple', '6/4와 12/8을 세고, 어떤 박자표든 홑박자·겹박자, 두·세·네 박자로 말해요')], [r4PicBar(), t('I put the bar lines into an unbarred phrase, anacrusis too', '마디선 없는 프레이즈에 마디선을 그어요, 못갖춘마디도')]];
  const kinds = ['sync', 'hem', 'ts', 'bar'];
  const toc = kinds.map((k, i) => [r4StepT(k), i + 2]).concat([[t('My four checks', '나의 네 가지 확인'), 6]]);
  const still = (keys) => <LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%',maxWidth:600,margin:'0 auto'}}>{keys.map(k => <div key={k}>{r2El(k)}</div>)}</div></LbPic>;
  const barStill = () => { const P = R4_BAR[1]; return <LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:600,margin:'0 auto'}}><div>{r4BarEl(P, [])}</div><div>{r4BarEl(P, r4BarAt(P))}</div></div></LbPic>; };
  const TEACH = {
    sync: t('Syncopation with minim, crotchet and quaver values only (Theory of Music Grade 4): a note that starts off the beat, or on a weak beat, and is held over the next beat or the strong beat. Clap with the beat said aloud, so the held-over beat is felt, not clapped.', '이론 4급의 당김음은 2분음표, 4분음표, 8분음표로만: 박 사이나 여린박에서 시작해 다음 박이나 센박 위로 이어지는 음. 박을 소리 내어 세며 쳐서, 이어지는 박은 치지 않고 느끼게 해요.'),
    hem: t('Hemiola: in triple time, two bars of three regrouped as three groups of two, often with a tie across the bar line, usually just before a cadence (minuets, courantes). Clap the line, then clap only the three long groups.', '헤미올라: 세박자에서 세 박 두 마디가 둘씩 세 묶음으로 바뀌어요. 마디선을 넘는 붙임줄과 함께, 대개 종지 바로 앞(미뉴에트, 쿠랑트). 줄을 친 다음, 긴 세 묶음만 쳐 봐요.'),
    ts: t('The time signatures 6/4 and 12/8 are added at Grade 4; general knowledge asks for compound quadruple time (12/8: four dotted-crotchet beats). Every time signature so far can be sorted two ways: simple or compound (the beat plain or dotted), and duple, triple or quadruple (beats in a bar). Chapter ' + r2c + ' has 3/8, 9/8 and the minim beat.', '4급에 6/4와 12/8이 더해지고, 일반 지식은 겹네박자를 물어요(12/8: 점4분음표 네 박). 지금까지의 박자표는 두 가지로 나눠요: 홑박자와 겹박자(박이 보통 음표인지 점음표인지), 그리고 두·세·네 박자(한 마디의 박 수). ' + r2c + '장에 3/8, 9/8, 2분음표 박이 있어요.'),
    bar: t('Barring an unbarred phrase: given the time signature, add the bar lines (and the double bar). If the phrase starts with an anacrusis, the first bar line comes after it and the last bar is short by the same amount. The app shows three barrings to choose from; on paper the child draws them.', '마디선 없는 프레이즈에 마디선 긋기: 박자표를 보고 마디선(과 끝세로줄)을 그어요. 못갖춘마디로 시작하면 첫 마디선은 그 뒤에, 마지막 마디는 그만큼 짧아요. 앱은 세 가지 중에서 고르고, 종이에서는 아이가 직접 그어요.'),
  };
  const SAY = {
    sync: <>{LANG === 'ko' ? <>당김음은 <b>강세를 박 사이로</b> 옮겨요: 8분음표-4분음표-8분음표에서 4분음표는 <b>+</b>에서 시작해 박 위로 이어져요.</> : <>Syncopation moves <b>the accent off the beat</b>: in quaver-crotchet-quaver the crotchet starts on the <b>+</b> and is held over the beat.</>}</>,
    hem: <>{LANG === 'ko' ? <>세박자 두 마디(<b>3 + 3</b>)가 <b>2 + 2 + 2</b>로 들려요: 마디선을 넘는 붙임줄이 가운데 2분음표를 만들어요.</> : <>Two bars of three (<b>3 + 3</b>) heard as <b>2 + 2 + 2</b>: a tie across the bar line makes the middle minim.</>}</>,
    ts: <>{LANG === 'ko' ? <><b>6/4</b>: 점2분음표 두 박(겹두박자). <b>12/8</b>: 점4분음표 네 박(<b>겹네박자</b>).</> : <><b>6/4</b>: two dotted-minim beats (compound duple). <b>12/8</b>: four dotted-crotchet beats (<b>compound quadruple</b>).</>}</>,
    bar: <>{LANG === 'ko' ? <>박자표가 한 마디의 박 수를 말해 줘요. 음표를 더해 마디가 찰 때마다 마디선.</> : <>The time signature says how many beats fill a bar. Add up the notes; a bar line each time a bar is full.</>}</>,
  };
  const PIANO = {
    sync: [t('Say 1 + 2 + and clap line 1: no clap on the beat the crotchet holds.', '1 + 2 + 를 말하며 1번 줄: 4분음표가 이어지는 박에서는 치지 않아요.'), t('Play it on one note, with a little accent on each syncopated note.', '한 음으로 치며, 당김음마다 살짝 강세.'), t('Find syncopation in a piece you are learning.', '배우는 곡에서 당김음을 찾아요.')],
    hem: [t('Clap line 1 counting 1 2 3.', '1 2 3을 세며 1번 줄을 쳐요.'), t('Now count bars 2 and 3 as 1 2, 1 2, 1 2.', '이번엔 2–3마디를 1 2, 1 2, 1 2로 세요.'), t('Find the hemiola before the end of a minuet.', '미뉴에트 끝 앞에서 헤미올라를 찾아요.')],
    ts: [t('Clap 6/4: count 1 2 3 4 5 6, accents on 1 and 4.', '6/4: 1 2 3 4 5 6, 1과 4에 강세.'), t('Clap 12/8: four big beats, each 1 + a… in threes.', '12/8: 큰 박 넷, 한 박에 셋씩.'), t('Sort five time signatures into simple and compound.', '박자표 다섯 개를 홑박자와 겹박자로 나눠요.')],
    bar: [t('Count the beats in a bar from the time signature.', '박자표에서 한 마디의 박 수를 세요.'), t('Add up the notes in a phrase; draw a bar line when a bar is full.', '프레이즈의 음표를 더하며, 마디가 차면 마디선.'), t('Check: the anacrusis and the last bar add up to one bar.', '확인: 못갖춘마디와 마지막 마디를 더하면 한 마디.')],
  };
  const live = { sync: <R2Pad step="sync" keys={['syncA', 'syncB']} title={r4StepT('sync')} note={t('Count the beats aloud; clap the notes. Where a note is held over a beat, feel that beat without clapping it.', '박을 소리 내어 세고, 음표를 쳐요. 음이 박 위로 이어지면 그 박은 치지 말고 느껴요.')} ask={R4_Q.sync}/>,
    hem: <R2Pad step="hem" keys={['hemA', 'hemB']} title={r4StepT('hem')} note={t('Bars of three; then a tie across the bar line makes three long notes of two beats each, before the end.', '세 박 마디; 그다음 마디선을 넘는 붙임줄이 끝 앞에서 두 박짜리 긴 음 셋을 만들어요.')} ask={R4_Q.hem}/>,
    ts: <R4TsPad/>, bar: <R4BarPad/> };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Theory of Music Grade 4, Time and Rhythm, one step each: syncopation (minim, crotchet and quaver values only), hemiola, 6/4 and 12/8 with compound quadruple time, and barring an unbarred phrase.', '이론 4급 박자와 리듬을 한 단계씩: 당김음(2분·4분·8분음표만), 헤미올라, 6/4와 12/8 그리고 겹네박자, 마디선 없는 프레이즈에 마디선 긋기.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {still(['syncA', 'hemA'])}
      <LbSay size={18}>{t('Rhythm for Grade 4: accents off the beat, threes that turn into twos, two new time signatures, and bar lines you draw yourself.', '4급 리듬: 박 사이의 강세, 둘로 바뀌는 셋, 새 박자표 둘, 그리고 직접 긋는 마디선.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks4.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    ...kinds.map((kind, i) => <LbPage key={kind} no={i + 2} chId={ch} kicker={t('Step ' + (i + 1), (i + 1) + '단계')} title={r4StepT(kind)} teacher={<>{TEACH[kind]}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=' + (i + 1))}>
      <LbLive still={kind === 'bar' ? barStill() : still(kind === 'sync' ? ['syncA', 'syncB'] : kind === 'hem' ? ['hemA', 'hemB'] : ['e64', 'e128'])} live={live[kind]}/>
      <LbSay>{SAY[kind]}</LbSay>
      <LbPiano steps={PIANO[kind].map((x, j) => <React.Fragment key={j}>{x}</React.Fragment>)}/>
      <LbRemember>{{ sync: t('Off the beat, held over the beat.', '박 사이에서, 박 위로 이어서.'), hem: t('3 + 3 becomes 2 + 2 + 2.', '3 + 3이 2 + 2 + 2로.'), ts: t('Dotted beat: compound. Count the beats: duple, triple, quadruple.', '점음표 박: 겹박자. 박을 세면: 두, 세, 네 박자.'), bar: t('Fill each bar, then a bar line.', '마디를 채우고, 마디선.') }[kind]}</LbRemember>
    </LbPage>),
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Clap each line with the beat said aloud; for the time signatures and bar lines, use a phrase from a piece the child is learning.', '줄마다 박을 소리 내어 세며 쳐요. 박자표와 마디선은 아이가 배우는 곡의 프레이즈로 해 보세요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_r4_four"/>}/>
    </LbPage>,
  ];
}
function Rhythm4LessonBook() { return <>{r4LbPages(false)}</>; }
function R4Learn({ onStart }) {
  const pages = r4LbPages(true), opener = pages[0];
  return (
    <Lesson id="rhythm-4" title={bkChapterName('rhythm-4')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="rhythm-4"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const R4_LEVELS = [
  { n: 1, label: 'Syncopation', kind: 'sync', time: 12 },
  { n: 2, label: 'Hemiola', kind: 'hem', time: 12 },
  { n: 3, label: 'Simple or compound? Duple, triple or quadruple?', kind: 'ts', time: 12 },
  { n: 4, label: 'Bar lines: which is right?', kind: 'bar', time: 25 },
];
Object.assign(LEVEL_KO, { 'Syncopation': '당김음', 'Hemiola': '헤미올라', 'Simple or compound? Duple, triple or quadruple?': '홑박자? 겹박자? 두·세·네 박자?', 'Bar lines: which is right?': '마디선: 어느 것이 맞을까?' });
function genR4Question(lv, prev) {
  const uid = Math.random();
  if (lv.kind === 'bar') { let i, g = 0; do { i = Math.floor(Math.random() * R4_BAR.length); } while (prev && prev.key === 'b' + i && g++ < 10); const opts = shuffle(r4BarOpts(R4_BAR[i]));
    return { kind: 'bar', i, opts, answer: 'ok', choices: opts.map(o => o[0]), key: 'b' + i, uid }; }
  let q, g = 0; do { q = R4_Q[lv.kind](); } while (prev && prev.key === q.prompt[0] + q.ans && g++ < 10);
  return { kind: lv.kind, q, answer: q.ans, choices: q.opts.map(o => o[0]), key: q.prompt[0] + q.ans, uid };
}
const r4Fig = { sync: 'syncA', hem: 'hemA' };
function r4AnswerLabel(q) { if (q.kind === 'bar') return t('the correct barring', '맞는 마디선'); const o = q.q.opts.find(x => x[0] === q.answer); return o ? o[1] : q.answer; }
function R4Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  if (q.kind === 'bar') { const P = R4_BAR[q.i]; return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)'}}>{t('Which is barred correctly?', '마디선이 맞게 그어진 것은?')}{P.an ? t(' (It starts with an anacrusis.)', ' (못갖춘마디로 시작해요.)') : ''}</p>
    <div style={{display:'flex',flexDirection:'column',gap:8}}>{q.opts.map(([id, at]) => <button key={id} disabled={locked} className={cls(id)} style={{padding:'6px 4px'}} onClick={() => pickIt(id)}><div style={{width:'100%',minWidth:0}}>{r4BarEl(P, at)}</div></button>)}</div>
  </div>); }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{t(q.q.prompt[0], q.q.prompt[1])}</p>
    {q.kind === 'ts' ? <div style={{textAlign:'center',margin:'4px 0'}}><R4TsSig top={q.q.sig[0]} bot={q.q.sig[1]} size={40}/></div> : <div style={{maxWidth:420,margin:'0 auto'}}>{r2El(r4Fig[q.kind], { counts: done ? undefined : false })}</div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + (q.q.cols || q.q.opts.length) + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.q.opts.map(([id, lab]) => <button key={id} disabled={locked} className={cls(id)} style={{padding:'11px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(id)}>{lab}</button>)}</div>
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{given.ans === q.answer ? t(q.q.yes[0], q.q.yes[1]) : t(q.q.no[0], q.q.no[1])}</div>}
  </div>);
}
Object.assign(RHYTHM_4_DRILL, { levels: R4_LEVELS, generate: genR4Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: r4AnswerLabel, Question: R4Question, Learn: R4Learn });
// the teacher's copy
function R4Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="rhythm-4" teacher>{content}</WbPage>);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('rhythm-4')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade 4, Time and Rhythm. Each line is the one the app plays and taps.</div>
    <TcBlock page={2} title="Syncopation" answers={<div style={{display:'grid',gap:6}}>{['syncA', 'syncB'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>}
      watch="Clapping the beat the syncopated note is held over. Say the beat aloud; clap only the notes."
      say="“Off the beat, held over the beat.”"/>
    <TcBlock page={3} title="Hemiola" answers={<div style={{display:'grid',gap:6}}>{['hemA', 'hemB'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>}
      watch="Re-striking the tied note. The tie makes the middle minim of 2 + 2 + 2."
      say="“3 + 3 becomes 2 + 2 + 2.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="6/4 and 12/8" answers={<>{tcAns('SIMPLE OR COMPOUND', R4_TS.map(([a, b, c]) => a + '/' + b + ' ' + R4_TSN[c][0]))}</>}
      watch="Calling 6/4 simple triple (six crotchets in threes is two dotted-minim beats: compound duple)."
      say="“Dotted beat: compound. Count the beats.”"/>
    <TcBlock page={5} title="Bar lines for a phrase" answers={<div style={{display:'grid',gap:6}}>{R4_BAR.map((x, j) => <div key={j}>{r4BarEl(x, r4BarAt(x))}</div>)}</div>}
      watch="Forgetting the anacrusis: the first bar line comes after it, and the last bar is short by the same amount."
      say="“Fill each bar, then a bar line.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Clap each line with the beat said aloud; bar a phrase from a piece the child is learning.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['rhythm-4'] = R4Teacher;
'''
rep("""TEACHER_COPIES['rhythm-23'] = R2Teacher;""", """TEACHER_COPIES['rhythm-23'] = R2Teacher;""" + CH)

HOME = r'''
// ══ Build AV: Rhythm, Grade 4 on the Home (Rhythm, after Rhythm further) ══
LBH_FN['rhythm-4'] = (s) => r4LbPages(s);
const r4Q = (kind) => (n, prev) => {
  if ((kind === 'sync' || kind === 'hem') && n % 2 === 0) { const R = R2[kind === 'sync' ? (n % 4 ? 'syncB' : 'syncA') : (n % 4 ? 'hemB' : 'hemA')]; return rqStaffQ(R.items, { ties: R.ties, so: R.ties ? { ties: R.ties } : undefined }); }
  if (kind === 'bar') { const q = genR4Question({ kind: 'bar' }, prev), P = R4_BAR[q.i];
    return { kind: 'choice', cols: 1, key: q.key, prompt: ['Which is barred correctly?', '마디선이 맞게 그어진 것은?'], opts: q.opts.map(([id, at]) => ({ id, label: () => <div style={{ width: '100%', minWidth: 0 }}>{r4BarEl(P, at)}</div> })), ans: 'ok', ok: (v) => v === 'ok',
      fig: () => ({ mid: <div style={{maxWidth:420,margin:'0 auto'}}>{r4BarEl(P, [])}</div> }), yes: ['Every bar is full.', '마디마다 꽉 찼어요.'], no: ['Count the beats in each bar again.', '마디마다 박을 다시 세어 봐요.'] }; }
  const q = R4_Q[kind](); return { kind: 'choice', cols: q.cols || q.opts.length, key: q.prompt[0] + q.ans, prompt: q.prompt, opts: q.opts.map(([id, lab]) => ({ id, label: lab })), ans: q.ans, ok: (v) => v === q.ans,
    fig: () => ({ mid: kind === 'ts' ? <div style={{textAlign:'center'}}><R4TsSig top={q.sig[0]} bot={q.sig[1]} size={40}/></div> : <div style={{maxWidth:420,margin:'0 auto'}}>{r2El(r4Fig[kind])}</div> }), yes: q.yes, no: q.no }; };
const r4HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'r-beat', 'rhythm', en, ko, benEn, bko, lbhSpec('rhythm-4', i, { make }));
r4HomeAdd('r4-sync', 1, 'Syncopation', '당김음', 'Off the beat, held over the beat.', '박 사이에서, 박 위로 이어서.', r4Q('sync'));
r4HomeAdd('r4-hem', 2, 'Hemiola', '헤미올라', '3 + 3 becomes 2 + 2 + 2.', '3 + 3이 2 + 2 + 2로.', r4Q('hem'));
r4HomeAdd('r4-ts', 3, '6/4 and 12/8', '6/4와 12/8', 'Simple or compound; duple, triple or quadruple.', '홑박자·겹박자, 두·세·네 박자.', r4Q('ts'));
r4HomeAdd('r4-bar', 4, 'Bar lines for a phrase', '프레이즈에 마디선 긋기', 'Fill each bar, then a bar line.', '마디를 채우고, 마디선.', r4Q('bar'));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'harmony-4': Harmony4LessonBook,""", """const LESSON_BOOKS = { 'rhythm-4': Rhythm4LessonBook, 'harmony-4': Harmony4LessonBook,""")
rep("""const LB_PAGE_FNS = { 'harmony-4': h4LbPages,""", """const LB_PAGE_FNS = { 'rhythm-4': r4LbPages, 'harmony-4': h4LbPages,""")
rep("""const HOUSE_ICONS = {"harmony-4": """, """const HOUSE_ICONS = {"rhythm-4": "<ellipse cx=\\"12\\" cy=\\"34\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 12 34)\\" fill=\\"#26296b\\"/><line x1=\\"17\\" x2=\\"17\\" y1=\\"33\\" y2=\\"12\\"/><ellipse cx=\\"28\\" cy=\\"34\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 28 34)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><line x1=\\"33\\" x2=\\"33\\" y1=\\"33\\" y2=\\"12\\" stroke=\\"#e4572e\\"/><text x=\\"30\\" y=\\"9\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" text-anchor=\\"middle\\">&gt;</text><ellipse cx=\\"42\\" cy=\\"34\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 42 34)\\" fill=\\"#26296b\\"/><line x1=\\"47\\" x2=\\"47\\" y1=\\"33\\" y2=\\"12\\"/>", "harmony-4": """)
# the house names the Grade 4 rooms on the Grade 4 floor: short names, the grade as a number
for a, b in [("'listen-4': ['Hear, Grade 4', '듣기 4']", "'listen-4': ['Hear & sing 4', '듣기 4']"), ("'scales-4': ['Scales, Grade 4', '스케일 4']", "'scales-4': ['Scales 4', '스케일 4']"),
             ("'keys-4': ['Keys, Grade 4', '조 4']", "'keys-4': ['Keys 4', '조 4']"), ("'harmony-4': ['Chords, Grade 4', '화음 4']", "'harmony-4': ['Chords 4', '화음 4']"), ("'rhythm-4': ['Rhythm, Grade 4', '리듬 4']", "'rhythm-4': ['Rhythm 4', '리듬 4']")]:
    rep(a, b)
# the Grade 4 floor keeps five rooms: the Grade 4 terms and ornaments already live in the Terms room (its Grade 4 step) and the Signs
# room (ornaments, grace notes): a separate room would repeat them (her 22:35: no twins)
rep("""  { ids: ['listen-4', 'scales-4', 'keys-4', 'harmony-4', 'rhythm-4', 'terms-4'], en: ['Grade 4', 'Your ears, scales and arpeggios, keys and intervals, chords and cadences, rhythm, and the words and ornaments.'], ko: ['Grade 4', '귀, 스케일과 아르페지오, 조와 음정, 화음과 종지, 리듬, 용어와 꾸밈음.'] },""",
    """  { ids: ['listen-4', 'scales-4', 'keys-4', 'harmony-4', 'rhythm-4'], en: ['Grade 4', 'Your ears, scales and arpeggios, keys and intervals, chords and cadences, and rhythm.'], ko: ['Grade 4', '귀, 스케일과 아르페지오, 조와 음정, 화음과 종지, 그리고 리듬.'] },""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
