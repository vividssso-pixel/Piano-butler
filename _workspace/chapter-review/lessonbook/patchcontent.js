// Content added from Sohyun's cheat sheets, inside the existing chapters (the map keeps its 25 chapters).
// Reads drills.src.t352.html (after patch352p.js), writes drills.src.t358.html.
const fs = require('fs');
const dir = __dirname;
let s = fs.readFileSync(dir + '/' + (process.env.SRC || 'drills.src.t352.html'), 'utf8');
function once(str, what) { const n = s.split(str).length - 1; if (n !== 1) throw new Error(what + ': expected 1 match, got ' + n); }
function rep(a, b, what) { once(a, what); s = s.replace(a, () => b); }
const read = (f) => fs.readFileSync(dir + '/' + f, 'utf8');
function repIn(fn, a, b, what, n) {
  const i = s.indexOf('function ' + fn + '('); if (i < 0) throw new Error(what + ': no function ' + fn);
  const j = s.indexOf('\nfunction ', i + 10), body = s.slice(i, j < 0 ? s.length : j);
  const c = body.split(a).length - 1; if (c !== (n || 1)) throw new Error(what + ': expected ' + (n || 1) + ' in ' + fn + ', got ' + c);
  s = s.slice(0, i) + body.split(a).join(b) + s.slice(i + body.length);
}


// Phase 358: Styles -- two hands, four ways (after "Which texture is this?"); the old steps keep their ticks
rep('function StylesLearn({ onStart }) {', read('motion358.jsx') + '\nfunction StylesLearn({ onStart }) {', 'motion code');
rep(`      <Step title={t('What makes each style different?', '각 스타일은 무엇이 다를까요')}>
        <GenreTraits/>
      </Step>
      <Step title={t('Straight or swing?', '스트레이트일까, 스윙일까?')}>
        <SwingFeel/>
      </Step>
      <Step title={t('The 12-bar blues', '12마디 블루스')}>
        <TwelveBarBlues/>
      </Step>`, `      <Step storeAs={5} title={t('Two hands, four ways', '두 손, 네 가지 움직임')}>
        <MotionTypes/>
      </Step>
      <Step storeAs={2} title={t('What makes each style different?', '각 스타일은 무엇이 다를까요')}>
        <GenreTraits/>
      </Step>
      <Step storeAs={3} title={t('Straight or swing?', '스트레이트일까, 스윙일까?')}>
        <SwingFeel/>
      </Step>
      <Step storeAs={4} title={t('The 12-bar blues', '12마디 블루스')}>
        <TwelveBarBlues/>
      </Step>`, 'styles steps');

// Phase 359: Form -- song shapes (last step); Chords -- four chords, one song (last step)
rep('function FormLearn({ onStart }) {', read('songs359.jsx') + '\nfunction FormLearn({ onStart }) {', 'songs code');
rep(`      <Step title={t('Two sections, or three?', '두 부분일까요, 세 부분일까요?')}>
        <BinaryTernarySpot/>
      </Step>
    </Lesson>`, `      <Step title={t('Two sections, or three?', '두 부분일까요, 세 부분일까요?')}>
        <BinaryTernarySpot/>
      </Step>
      <Step title={t('Song shapes', '노래의 모양')}>
        <SongForms/>
      </Step>
    </Lesson>`, 'form step');
rep(`      <Step title={t('Cadences', '종지')}>
        <ExplChords6/>
        <CadencePlayer/>
      </Step>
    </Lesson>`, `      <Step title={t('Cadences', '종지')}>
        <ExplChords6/>
        <CadencePlayer/>
      </Step>
      <Step title={t('Four chords, one song', '코드 네 개로 노래 만들기')}>
        <FourChordSong/>
      </Step>
    </Lesson>`, 'chords step');

// Phase 360: Chords -- arpeggios (step 8); Styles -- the eight elements of music (step 7); Dynamics -- ppp and fff
rep('function ChordsLearn(', read('extras360.jsx') + '\nfunction ChordsLearn(', 'extras code');
rep(`      <Step title={t('Four chords, one song', '코드 네 개로 노래 만들기')}>
        <FourChordSong/>
      </Step>
    </Lesson>`, `      <Step title={t('Four chords, one song', '코드 네 개로 노래 만들기')}>
        <FourChordSong/>
      </Step>
      <Step title={t('Arpeggios', '아르페지오')}>
        <ArpeggioTool/>
      </Step>
    </Lesson>`, 'arpeggio step');
rep(`      <Step storeAs={4} title={t('The 12-bar blues', '12마디 블루스')}>
        <TwelveBarBlues/>
      </Step>`, `      <Step storeAs={4} title={t('The 12-bar blues', '12마디 블루스')}>
        <TwelveBarBlues/>
      </Step>
      <Step storeAs={6} title={t('The eight elements of music', '음악의 여덟 가지 요소')}>
        <ElementsOfMusic/>
      </Step>`, 'elements step');
rep(`      <DynOrder/>
      </Step>`, `      <div data-testid="dyn-extremes" style={{margin:'-4px 0 12px'}}>
        <div style={{fontSize:13,fontWeight:800,color:'var(--navy)',margin:'0 0 5px'}}>{t('Even further: the softest and the loudest', '더 끝까지: 가장 여리게, 가장 세게')}</div>
        <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:6}}>
          {cell('ppp', <span style={{lineHeight:1.1}}><DynMark id="ppp" size={15}/></span>, t('pianississimo · as soft as you can', 'pianississimo · 가장 여리게'), () => pick('ppp', () => playDyn(0.022)))}
          {cell('fff', <span style={{lineHeight:1.1}}><DynMark id="fff" size={34}/></span>, t('fortississimo · as loud as you can', 'fortississimo · 가장 세게'), () => pick('fff', () => playDyn(0.75)))}
        </div>
      </div>
      <DynOrder/>
      </Step>`, 'ppp fff');
rep('  function update(patch) { setSt(prev => ({ ...prev, ...patch })); }', `  function update(patch) { setSt(prev => ({ ...prev, ...patch })); }
  OPEN_CH = (id) => { update({ drill: id, tab: 'learn', level: 1 }); try { window.scrollTo(0, 0); } catch (e) {} }; // Phase 360: chapter links inside a lesson`, 'open chapter hook');

// ── Phase 361: one order everywhere -- the music map's seven stages ──
// (a) STAGES (books, Books shelf, chapter numbers) is now made from PATH_STAGES instead of its own older grouping
{
  const i = s.indexOf('// ─── Lesson Path: stages in the order a beginner meets them (Phase 120)');
  const j = s.indexOf('const GRADE_TAGS = {', i);
  if (i < 0 || j < 0) throw new Error('old STAGES block');
  s = s.slice(0, i) + '// Phase 361: STAGES is defined right after PATH_STAGES (the music map) -- one order for the map, the books and the shelf.\n' + s.slice(j);
}
rep('const pathIds = () => PATH_STAGES.flatMap(pathStageIds);', `const pathIds = () => PATH_STAGES.flatMap(pathStageIds);
// Phase 361 (Sohyun: "지도 순서로"): the books, the Books shelf and every "Chapter n" follow the map's seven stages.
const STAGES = PATH_STAGES.map((st, n) => ({ n, en: st.en, ko: st.ko, title: st.en[0], blurb: st.en[1], ids: pathStageIds(st) }));`, 'STAGES from PATH_STAGES');
rep('function catChapterIds(catId) { const ids = STAGES.flatMap(s => s.ids).filter(', 'function catChapterIds(catId) { const ids = DRILLS.map(d => d.id).filter(', 'catChapterIds base order');
// (b) DRILLS listed in the map's order (only DRILLS[0] and tie-breaks inside a category used its order)
{
  const i = s.indexOf('const DRILLS = [\n'), j = s.indexOf('\n];', i);
  const lines = s.slice(i + 'const DRILLS = [\n'.length, j).split('\n');
  const order = ['posture-hands', 'first-steps', 'note-names', 'staff', 'ledger-lines', 'tones', 'pulse', 'note-values', 'time-signatures', 'rhythm', 'reading-steps', 'tempo', 'intervals', 'scales', 'key-signatures', 'chords', 'melody', 'form', 'dynamics', 'signs', 'terms', 'piano-story', 'composers', 'pitch-range', 'styles'];
  const byId = {}; lines.forEach(l => { const m = /id: '([a-z-]+)'/.exec(l); if (m) byId[m[1]] = l; });
  if (Object.keys(byId).length !== 25 || order.some(id => !byId[id])) throw new Error('DRILLS lines');
  s = s.slice(0, i) + 'const DRILLS = [ // Phase 361: in the music map\'s order\n' + order.map(id => byId[id]).join('\n') + s.slice(j);
}
// (c) the Books shelf: stage names from the map, in English and Korean
rep(`{t(st.title.toUpperCase(), STAGE_KO[st.n] || st.title)}`, `{t(st.en[0].toUpperCase(), st.ko[0])}`, 'shelf stage names');
// (d) the exam ladder lists its chapters in map order
rep(`  { name: 'Preliminary', ids: ['note-values', 'time-signatures', 'staff', 'ledger-lines', 'tones', 'scales', 'key-signatures', 'terms'] },
  { name: 'Grade 1–2', ids: ['scales', 'key-signatures', 'intervals', 'chords', 'signs', 'terms'] },
  { name: 'Grade 3–4', ids: ['intervals', 'chords', 'time-signatures', 'terms', 'piano-story'] },`, `  { name: 'Preliminary', ids: ['staff', 'ledger-lines', 'tones', 'note-values', 'time-signatures', 'scales', 'key-signatures', 'terms'] },
  { name: 'Grade 1–2', ids: ['intervals', 'scales', 'key-signatures', 'chords', 'signs', 'terms'] },
  { name: 'Grade 3–4', ids: ['time-signatures', 'intervals', 'chords', 'terms', 'piano-story'] },`, 'exam ladder order');
// (e) step links: a chapter with two lessons (Scales: major and minor) -- the code on a workbook page opens the right one
rep(`const el = document.getElementById(st.drill + '-step-' + (n - 1));`, `const part = BOOT_PARAMS.get('part'); const el = [st.drill + '-step-', st.drill + '-' + (part === 'minor' ? 'minor' : 'major') + '-step-'].map(x => document.getElementById(x + (n - 1))).find(Boolean); /* Phase 361: Scales has two lessons */`, 'step link scroll');
// the address is rewritten from the app's state as soon as it starts (which drops ?step and ?part), so read them from the address the page was opened with
rep(`useEffect(() => { try { const n = parseInt(new URLSearchParams(location.search).get('step'), 10);`, `useEffect(() => { try { const n = parseInt(BOOT_PARAMS.get('step'), 10);`, 'step from boot params');
rep('function readUrlState(studentMode) {', `// Phase 361: the address as the page was opened (workbook codes add &step= and &part=; the app rewrites the address on start)
const BOOT_PARAMS = (() => { try { return new URLSearchParams(location.search); } catch (e) { return new URLSearchParams(''); } })();
function readUrlState(studentMode) {`, 'boot params');
rep(`  return bkLink('drill=' + ch + '&lock=1' + (isNaN(n) ? '' : '&step=' + n));
}`, `  return bkLink('drill=' + ch + '&lock=1' + (isNaN(n) ? '' : '&step=' + n) + (/^minor /.test(String(st)) ? '&part=minor' : ''));
}`, 'minor step link');
repIn('ScalesLearn', `  const [mode, setMode] = useState('major');`, `  const [mode, setMode] = useState(() => { try { return BOOT_PARAMS.get('part') === 'minor' ? 'minor' : 'major'; } catch (e) { return 'major'; } }); // Phase 361: ?part=minor (workbook codes)`, 'scales start part');
// (f) the chapter map page lists the minor lesson's steps too
rep(`function WbMap({ id, concepts, tasks, steps, checkPage }) {`, `function WbMap({ id, concepts, tasks, steps, checkPage, minor }) {`, 'WbMap minor prop');
rep(`          {Array.from({ length: total }, (_, k) => k + 1).map(n => {
            const pg = pages[n], cs = concepts.filter(c => String(c.step).split(',').some(s => { const r = s.trim().match(/^(\\d+)-(\\d+)$/); return r ? n >= +r[1] && n <= +r[2] : parseInt(s, 10) === n; }));
            return <div key={n} style={{display:'grid',gridTemplateColumns:'110px 1fr 1fr 44px',fontSize:12.5,color:BK.ink,padding:(total > 7 ? '3px' : '6px') + ' 10px',borderTop:'1px solid #ece6d8',alignItems:'center'}}>
              <span><b style={{color:BK.coral}}>Step {n}</b></span>`, `          {[...Array.from({ length: total }, (_, k) => ({ n: k + 1, pre: '' })), ...Array.from({ length: minor || 0 }, (_, k) => ({ n: k + 1, pre: 'minor ' }))].map(({ n, pre }) => {
            const own = pre ? concepts.filter(c => String(c.step).startsWith(pre)).map(c => ({ ...c, step: String(c.step).slice(pre.length) })) : concepts;
            const pg = (pre ? bkStepPages(own) : pages)[n], cs = own.filter(c => String(c.step).split(',').some(s => { const r = s.trim().match(/^(\\d+)-(\\d+)$/); return r ? n >= +r[1] && n <= +r[2] : parseInt(s, 10) === n; }));
            return <div key={pre + n} data-map-row={pre + n} style={{display:'grid',gridTemplateColumns:'110px 1fr 1fr 44px',fontSize:12.5,color:BK.ink,padding:(total + (minor || 0) > 7 ? '3px' : '6px') + ' 10px',borderTop:'1px solid #ece6d8',alignItems:'center'}}>
              <span><b style={{color:BK.coral}}>{pre ? 'Minor step ' + n : 'Step ' + n}</b></span>`, 'WbMap rows');
// (g) chapter maps count every lesson step (steps added since the workbook was written show "in the app only" until they get a page)
repIn('StaffWorkbook', `<WbMap id="staff" concepts={C} steps={7}`, `<WbMap id="staff" concepts={C} steps={8}`, 'staff steps');
repIn('ChordsWorkbook', `steps={6}`, `steps={8}`, 'chords steps');
repIn('MusicalFormWorkbook', `steps={5}`, `steps={6}`, 'form steps');
repIn('StylesWorkbook', `steps={5}`, `steps={7}`, 'styles steps');
// (h) Styles: "Two hands, four ways" became step 3, so the old steps 3, 4, 5 are now 4, 5, 6
repIn('stConcepts', `{ id: 'fa', name: 'Style families and swing', step: '3-4', page: '5' },
    { id: 'bl', name: 'The 12-bar blues', step: 5, page: '6' },`, `{ id: 'fa', name: 'Style families and swing', step: '4-5', page: '5' },
    { id: 'bl', name: 'The 12-bar blues', step: 6, page: '6' },`, 'styles concepts');
repIn('StylesWorkbook', `<WbTop step="3-4"/>`, `<WbTop step="4-5"/>`, 'styles top 3-4');
repIn('StylesWorkbook', `<WbTop step={5}/>`, `<WbTop step={6}/>`, 'styles top 5');
// (i) Scales: the lesson now starts with the Scale finder and fingering (Phase 350), so the workbook does too:
//     fingering page first (steps 1-2), then shape and build (3-4), degree names (5), minor (minor 3-4)
repIn('scConcepts', `    { id: 'sh', name: 'The major-scale shape', step: '1', page: '3' },
    { id: 'bd', name: 'Building a major scale', step: '2', page: '3' },
    { id: 'dg', name: 'Degree names', step: '3', page: '4' },
    { id: 'fg', name: 'Fingering', step: '4-6', page: '5' },
    { id: 'mn', name: 'Harmonic minor', step: 'minor 1-2', page: '6' },`, `    { id: 'sh', name: 'The major-scale shape', step: '3', page: '4' },
    { id: 'bd', name: 'Building a major scale', step: '4', page: '4' },
    { id: 'dg', name: 'Degree names', step: '5', page: '5' },
    { id: 'fg', name: 'Fingering', step: '1-2', page: '3' },
    { id: 'mn', name: 'Harmonic minor', step: 'minor 3-4', page: '6' },`, 'scales concepts');
repIn('ScalesWorkbook', `<WbMap id="scales" concepts={C} steps={6} checkPage={startNo + 6}`, `<WbMap id="scales" concepts={C} steps={6} minor={5} checkPage={startNo + 6}`, 'scales map minor');
{
  const fi = s.indexOf('function ScalesWorkbook(');
  const fj = s.indexOf('\nfunction ', fi + 10);
  let b = s.slice(fi, fj);
  const cut = (startMark, endMark) => { const x = b.indexOf(startMark), y = b.indexOf(endMark, x); if (x < 0 || y < 0) throw new Error('scales cut ' + startMark.slice(0, 30)); const piece = b.slice(x, y + endMark.length); b = b.slice(0, x) + b.slice(y + endMark.length); return piece; };
  const pShape = cut(`  P(<>\n    <WbTop step="1-2"/>`, `    <Faces/>\n  </>);\n`);
  const pDeg = cut(`  P(<>\n    <WbTop step={3}/>`, `    <Faces/>\n  </>);\n`);
  const pFing = cut(`  const fC = SCALES.C.octaves[1], fG = SCALES.G.octaves[1], fF = SCALES.F.octaves[1];\n  P(<>\n    <WbTop step="4-6"/>`, `    <Faces/>\n  </>);\n`);
  const pMin = cut(`  P(<>\n    <WbTop step="minor 1-2"/>`, `    <Faces/>\n  </>);\n`);
  // the fingering page's puzzle: find the wrong finger (the old "broken staircase" needed the shape, which now comes later)
  const pz0 = pFing.indexOf(`    <Part kind="play" title="Broken staircase"`), pz1 = pFing.indexOf(`    </Part>\n    <Faces/>`, pz0);
  if (pz0 < 0 || pz1 < 0) throw new Error('broken staircase part');
  const newPlay = `    <Part kind="play" title="Find the wrong finger" how="A sleepy pianist wrote these fingerings, but each row has ONE wrong finger number. Circle it and write the right finger above it. Then play each one to check.">
      <div style={{display:'grid',gap:8}}>{scWrongs().map(([label, fs, wi, wv]) => <div key={label} style={{display:'flex',alignItems:'center',gap:12,border:'1.5px solid ' + BK.line,borderRadius:10,padding:'12px 10px 8px'}}><b style={{width:110,fontSize:12.5}}>{label}</b><div style={{display:'flex',gap:5}}>{fs.map((f, j) => <span key={j} style={{width:30,height:32,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:16,fontWeight:900,color:BK.ink,border:'1.2px solid ' + BK.line,background:'#fff'}}>{j === wi ? wv : f}</span>)}</div></div>)}</div>
      <div style={{fontSize:11.5,color:BK.muted,marginTop:8}}>Clue: the thumb (1) tucks under, finger 3 or 4 crosses over -- and a hand never uses the same finger twice in a row.</div>
`;
  const fing = pFing.slice(0, pz0) + newPlay + pFing.slice(pz1);
  const anchor = b.indexOf(`\n\n  const cnt = { sh: 4, bd: 4, dg: 4, fg: 4, mn: 4 };`);
  if (anchor < 0) throw new Error('scales cnt anchor');
  const re = (x, from, to) => { if (x.indexOf(from) < 0) throw new Error('scales top ' + from); return x.replace(from, to); };
  const ordered = '\n' + re(fing, `<WbTop step="4-6"/>`, `<WbTop step="1-2"/>`) + '\n' + re(pShape, `<WbTop step="1-2"/>`, `<WbTop step="3-4"/>`) + '\n' + re(pDeg, `<WbTop step={3}/>`, `<WbTop step={5}/>`) + '\n' + re(pMin, `<WbTop step="minor 1-2"/>`, `<WbTop step="minor 3-4"/>`);
  b = b.slice(0, anchor) + ordered + b.slice(anchor);
  s = s.slice(0, fi) + b + s.slice(fj);
}
rep(`function ScalesWorkbook({ startNo = 1 }) {`, `// Phase 361: the fingering puzzle -- each row has one wrong finger (label, the right fingering, which note, the wrong number)
function scWrongs() {
  const fC = SCALES.C.octaves[1], fG = SCALES.G.octaves[1], bad = (v) => v === 4 ? 3 : 4;
  return [['C major RH', fC.RH, 3, bad(fC.RH[3])], ['C major LH', fC.LH, 5, bad(fC.LH[5])], ['G major RH', fG.RH, 6, bad(fG.RH[6])]];
}
function ScalesWorkbook({ startNo = 1 }) {`, 'scWrongs');
// the teacher copy follows the new page order
{
  const fi = s.indexOf('function ScalesTeacher('), fj = s.indexOf('\nfunction ', fi + 10);
  let b = s.slice(fi, fj);
  const blk = (start) => { const x = b.indexOf(start); const y = b.indexOf('/>\n', b.indexOf('say=', x)); if (x < 0 || y < 0) throw new Error('teacher block ' + start); return [x, y + 3]; };
  const [a3, z3] = blk(`    <TcBlock page={3} title="Shape · build"`); const t3 = b.slice(a3, z3);
  const [a4, z4] = blk(`    <TcBlock page={4} title="Degree names"`); const t4 = b.slice(a4, z4);
  const [a5, z5] = blk(`    <TcBlock page={5} title="Fingering"`); const t5 = b.slice(a5, z5);
  if (!(a3 < a4 && a4 < a5 && z3 === a4 && z4 === a5)) throw new Error('teacher blocks not adjacent');
  const oldPlay = `{tcAns('PLAY', ['C major: the A-B riser is short, should be tall (a tone)', 'G major: the B-C riser is tall, should be short (a semitone); treads G A B C D E F♯ G'])}`;
  if (t5.indexOf(oldPlay) < 0) throw new Error('teacher fingering play answers');
  const n5 = t5.replace('page={5}', 'page={3}').replace(oldPlay, `{tcAns('PLAY', scWrongs().map(([l, fs, wi, wv]) => l + ': note ' + (wi + 1) + ' is ' + fs[wi] + ', not ' + wv))}`);
  b = b.slice(0, a3) + n5 + t3.replace('page={3}', 'page={4}') + t4.replace('page={4}', 'page={5}') + b.slice(z5);
  s = s.slice(0, fi) + b + s.slice(fj);
}

// ── Phase 362: workbook pages (and teacher answers) for the lesson steps added in Phases 358-360 ──
rep('function ChordsWorkbook({ startNo = 1 }) {', read('wb362.jsx') + '\nfunction ChordsWorkbook({ startNo = 1 }) {', 'wb362 code');
// concepts with chk: false are on the chapter map and the opener but not in the check-up
repIn('CheckTable', `{concepts.map((c, i) => <div key={c.id}`, `{concepts.filter(c => c.chk !== false).map((c, i) => <div key={c.id}`, 'check table filter');
repIn('TcBlock', `{goBack.map((c, i) =>`, `{goBack.filter(c => c.chk !== false).map((c, i) =>`, 'go back filter');
// Chords: page 7 = steps 7-8, check-up moves to page 8
repIn('chConcepts', `    { id: 'cd', name: 'Cadences', step: '6', page: '6' },`, `    { id: 'cd', name: 'Cadences', step: '6', page: '6' },
    { id: 'fc', name: 'Four chords, one song', step: '7', page: '7', chk: false },
    { id: 'ar', name: 'Arpeggios', step: '8', page: '7', chk: false },`, 'chords concepts');
repIn('ChordsWorkbook', `steps={8} checkPage={startNo + 6}`, `steps={8} checkPage={startNo + 7}`, 'chords check page');
repIn('ChordsWorkbook', `\n  const cnt = { tr: 4, mm: 4, rn: 4, iv: 4, cd: 4 };`, `\n  P(<ChordsLoopPage/>);\n  const cnt = { tr: 4, mm: 4, rn: 4, iv: 4, cd: 4 };`, 'chords new page');
repIn('ChordsTeacher', `    <TcBlock page={7} title="Check-up" goBack={chConcepts()}`, `    <ChordsLoopTeacher/>\n    <TcBlock page={8} title="Check-up" goBack={chConcepts()}`, 'chords teacher');
// Form: page 7 = step 6, check-up moves to page 8
repIn('fmConcepts', `    { id: 'bt', name: 'Two sections or three?', step: 5, page: '6' },`, `    { id: 'bt', name: 'Two sections or three?', step: 5, page: '6' },
    { id: 'ss', name: 'Song shapes', step: 6, page: '7', chk: false },`, 'form concepts');
repIn('MusicalFormWorkbook', `steps={6} checkPage={startNo + 6}`, `steps={6} checkPage={startNo + 7}`, 'form check page');
repIn('MusicalFormWorkbook', `\n  const cnt = { sh: 5, sn: 5, ro: 5, bt: 5 };`, `\n  P(<FormSongPage/>);\n  const cnt = { sh: 5, sn: 5, ro: 5, bt: 5 };`, 'form new page');
repIn('MusicalFormTeacher', `    <TcBlock page={7} title="Check-up" goBack={fmConcepts()}`, `    <FormSongTeacher/>\n    <TcBlock page={8} title="Check-up" goBack={fmConcepts()}`, 'form teacher');
// Styles: page 4 = step 3 (two hands), page 8 = step 7 (elements); eras 5, families 6, blues 7, check-up 9
repIn('stConcepts', `    { id: 'tx', name: 'Textures: mono, homo, poly', step: '1-2', page: '3' },
    { id: 'er', name: 'The style eras', step: 'story 5', page: '4' },
    { id: 'fa', name: 'Style families and swing', step: '4-5', page: '5' },
    { id: 'bl', name: 'The 12-bar blues', step: 6, page: '6' },`, `    { id: 'tx', name: 'Textures: mono, homo, poly', step: '1-2', page: '3' },
    { id: 'mo', name: 'Two hands, four ways', step: 3, page: '4', chk: false },
    { id: 'er', name: 'The style eras', step: 'story 5', page: '5' },
    { id: 'fa', name: 'Style families and swing', step: '4-5', page: '6' },
    { id: 'bl', name: 'The 12-bar blues', step: 6, page: '7' },
    { id: 'el', name: 'The eight elements of music', step: 7, page: '8', chk: false },`, 'styles concepts');
repIn('StylesWorkbook', `steps={7} checkPage={startNo + 6}`, `steps={7} checkPage={startNo + 8}`, 'styles check page');
repIn('StylesWorkbook', `\n  P(<>\n    <WbTop step="story 5"/>`, `\n  P(<StylesMotionPage/>);\n\n  P(<>\n    <WbTop step="story 5"/>`, 'styles motion page');
repIn('StylesWorkbook', `\n  const cnt = { tx: 5, er: 5, fa: 5, bl: 5 };`, `\n  P(<StylesElementsPage/>);\n  const cnt = { tx: 5, er: 5, fa: 5, bl: 5 };`, 'styles elements page');
{
  const fi = s.indexOf('function StylesTeacher('), fj = s.indexOf('\nfunction ', fi + 10);
  let b = s.slice(fi, fj);
  const swap = (a0, b0) => { if (b.split(a0).length !== 2) throw new Error('styles teacher ' + a0); b = b.replace(a0, b0); };
  swap('Page 4 (the style eras) goes with The Piano', 'Page 5 (the style eras) goes with The Piano');
  swap('<TcBlock page={4} title="The style eras"', '<TcBlock page={5} title="The style eras"');
  swap('<TcBlock page={5} title="Style families · swing"', '<TcBlock page={6} title="Style families · swing"');
  // the blues block moves to the second teacher page with the elements block and the check-up
  const x = b.indexOf('    <TcBlock page={6} title="The 12-bar blues"'), y = b.indexOf('/>\n', b.indexOf('say=', x)) + 3;
  if (x < 0) throw new Error('styles teacher blues');
  const blues = b.slice(x, y).replace('page={6}', 'page={7}'); b = b.slice(0, x) + b.slice(y);
  swap('    <TcBlock page={7} title="Check-up" goBack={stConcepts()}', blues + '    <StylesElementsTeacher/>\n    <TcBlock page={9} title="Check-up" goBack={stConcepts()}');
  const tx = b.indexOf('    <TcBlock page={3} title="Textures"'), ty = b.indexOf('/>\n', b.indexOf('say=', tx)) + 3;
  b = b.slice(0, ty) + '    <StylesMotionTeacher/>\n' + b.slice(ty);
  s = s.slice(0, fi) + b + s.slice(fj);
}

// seven step rows plus the whole-path box: slightly tighter rows so the map still fits its sheet
repIn('WbMap', `padding:(total + (minor || 0) > 7 ? '3px' : '6px') + ' 10px'`, `padding:(total + (minor || 0) > 7 ? '3px' : total + (minor || 0) > 6 ? '4px' : '6px') + ' 10px'`, 'map 7-row padding');

// ── Phase 363: workbooks + teacher copies for The Piano's Story, Famous Composers and Pitch, Hz & Range ──
rep('\nconst WORKBOOKS = {', '\n' + read('wb363.jsx') + '\nconst WORKBOOKS = {', 'wb363 insert');
rep(`form: MusicalFormWorkbook, styles: StylesWorkbook };`, `form: MusicalFormWorkbook, 'piano-story': PianoStoryWorkbook, composers: ComposersWorkbook, 'pitch-range': PitchRangeWorkbook, styles: StylesWorkbook };`, 'register workbooks');
rep(`form: MusicalFormTeacher, styles: StylesTeacher };`, `form: MusicalFormTeacher, 'piano-story': PianoStoryTeacher, composers: ComposersTeacher, 'pitch-range': PitchRangeTeacher, styles: StylesTeacher };`, 'register teacher copies');

if (process.env.UPTO !== '363') { // UPTO=363 builds the Phase 363 state only
// ── Phase 364: four new cut-out sets; the cut-out list follows the map order and shows each set's chapter ──
rep('\nconst CUTOUTS = {', '\n' + read('cut364.jsx') + '\nconst CUTOUTS = {', 'cut364 insert');
rep(`'practice-dice': CutDice, 'tempo-race': CutTempoRace };`, `'practice-dice': CutDice, 'tempo-race': CutTempoRace, 'chord-loop': CutChordLoop, 'song-builder': CutSongBuilder, 'composer-cards': CutComposerCards, 'cards-elements': CutElementCards };`, 'register cut-outs');
{
  const i = s.indexOf('const CUTOUT_LIST = ['), j = s.indexOf('];', i) + 2;
  if (i < 0) throw new Error('CUTOUT_LIST');
  s = s.slice(0, i) + `const CUTOUT_LIST = [ // in the music map's order; ch = the chapter it goes with (null = any chapter)
  { id: 'staff-mat', ch: 'staff', name: 'Staff mat and tokens', pages: 2, blurb: 'Build notes and words on the staff' },
  { id: 'cards-notes', ch: 'staff', name: 'Note flashcards', pages: 4, blurb: 'Treble and bass notes, double-sided' },
  { id: 'note-bars', ch: 'note-values', name: 'Note-value bars', pages: 2, blurb: 'Pieces that add up to a bar' },
  { id: 'cards-rhythm', ch: 'note-values', name: 'Rhythm flashcards', pages: 2, blurb: 'Notes and rests, double-sided' },
  { id: 'tempo-race', ch: 'tempo', name: 'Tempo Race board game', pages: 3, blurb: 'Race round the track by saying tempo words' },
  { id: 'scale-slider', ch: 'scales', name: 'Scale slider', pages: 2, blurb: 'Slide a pattern along the keys' },
  { id: 'fifths-wheel', ch: 'key-signatures', name: 'Circle-of-fifths wheel', pages: 2, blurb: 'A turning window on every key' },
  { id: 'chord-cake', ch: 'chords', name: 'Chord cake', pages: 2, blurb: 'Stack layers to build every triad' },
  { id: 'chord-loop', ch: 'chords', name: 'Four-chord loop', pages: 2, blurb: 'Chord cards and a loop mat' },
  { id: 'song-builder', ch: 'form', name: 'Song builder', pages: 2, blurb: 'Song blocks, letter tiles and a song mat' },
  { id: 'cards-terms', ch: 'terms', name: 'Term flashcards', pages: 4, blurb: 'Speed, volume and more, double-sided' },
  { id: 'composer-cards', ch: 'composers', name: 'Composer cards', pages: 5, blurb: '24 composers, double-sided, with games' },
  { id: 'cards-elements', ch: 'styles', name: 'Elements and motion cards', pages: 3, blurb: 'The eight elements and the four two-hand motions, with games' },
  { id: 'practice-dice', ch: null, name: 'Practice dice and week tracker', pages: 3, blurb: 'Roll how to play, then tick off the week' },
];` + s.slice(j);
}
rep(`<span style={{flex:'1 1 150px',fontSize:14,fontWeight:800,color:'var(--navy)'}}>{c.name}<span style={{color:'var(--muted)',fontWeight:600,fontSize:12,marginLeft:8}}>`, `<span style={{flex:'1 1 150px',fontSize:14,fontWeight:800,color:'var(--navy)'}}><span data-cut-ch={c.ch || ''} style={{color:'var(--muted)',fontWeight:700,marginRight:6}}>{c.ch ? bkChapterNo(c.ch) : t('any', '공통')}</span>{c.name}<span style={{color:'var(--muted)',fontWeight:600,fontSize:12,marginLeft:8}}>`, 'shelf: cut-out chapter number');

// the chapter opener names the cut-outs that go with the chapter
repIn('WbOpener', `        <div style={{fontSize:12,color:BK.muted,marginTop:7,lineHeight:1.5}}>Tick a box when you can do it without help.</div>
      </div>`, `        <div style={{fontSize:12,color:BK.muted,marginTop:7,lineHeight:1.5}}>Tick a box when you can do it without help.</div>
        {CUTOUT_LIST.some(c => c.ch === id) && <div data-opener-cutouts={id} style={{display:'flex',alignItems:'center',gap:'4px 10px',flexWrap:'wrap',marginTop:16,border:'1.4px dashed ' + CUT.cut,borderRadius:10,padding:'8px 12px',fontSize:12.5,color:BK.ink,lineHeight:1.45}}>
          <CutScissors size={16}/><b>Cut-outs for this chapter:</b>
          <span style={{fontWeight:800,color:CUT.cut}}>{CUTOUT_LIST.filter(c => c.ch === id).map(c => c.name).join(' · ')}</span>
          <span style={{color:BK.muted,fontSize:11.5}}>Print them from Books, Cut-outs in the app.</span>
        </div>}
      </div>`, 'opener: cut-outs for this chapter');

}
if (!['363', '364'].includes(process.env.UPTO)) { eval(read('p365.js')); }
if (!['363', '364', '365'].includes(process.env.UPTO)) { eval(read('p366.js')); }
if (!['363', '364', '365', '366'].includes(process.env.UPTO)) { eval(read('p368.js')); }
if (!['363', '364', '365', '366'].includes(process.env.UPTO)) { eval(read('p369.js')); }
if (!['363', '364', '365', '366', '370'].includes(process.env.UPTO)) { eval(read('p371.js')); }
if (!['363', '364', '365', '366', '370', '371'].includes(process.env.UPTO)) { eval(read('p372.js')); }
if (!['363', '364', '365', '366', '370', '371', '372'].includes(process.env.UPTO)) { eval(read('p373.js')); }
if (!['363', '364', '365', '366', '370', '371', '372', '373'].includes(process.env.UPTO)) { eval(read('p376.js')); }
if (!['363', '364', '365', '366', '370', '371', '372', '373', '376'].includes(process.env.UPTO)) { eval(read('p377.js')); }
if (!['363', '364', '365', '366', '370', '371', '372', '373', '376', '377'].includes(process.env.UPTO)) { eval(read('p378.js')); }
fs.writeFileSync(dir + '/' + (process.env.OUT || 'drills.src.t358.html'), s);
console.log('ok');
