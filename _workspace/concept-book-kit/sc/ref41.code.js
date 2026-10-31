// ── Build EC, call 41 (her 14:32 'a space that takes in the whole, like a book's reference pages: it becomes the map, easier
// to see'; 14:36 'all at once', Beginner to Grade 8): the Reference. One table per topic, no explanations beyond a line;
// each row carries the floor where the house teaches it and is a door into that room. Every row comes from a room's own
// teaching (its steps, its key lists: SCF, SCF_CM, S4_KEYS..., K4_IDS, MM_KEYS, H3_MIN, DEGREE_NAMES, DICT_TERMS); the
// patterns (tones and semitones, semitones in an interval, the key signatures) are counted by the code, not typed.
// On screen: ?tool=reference (the Home's Quick line); on paper: ?book=reference (A4, the books' look). The Scales map lives
// inside it (Scales, floor by floor) and the dictionary's terms are its last table.
const RefPaper = React.createContext(false);
const refFloor = (room) => { const s = STAGES.find(x => x.ids.includes(room)); return s && s.en ? s.en[0] : ''; };
function RefDoor({ room, g }) {
  const paper = React.useContext(RefPaper), go = React.useContext(RefGo), lab = g || refFloor(room);
  if (paper) return <span style={{fontSize:10.5,fontWeight:800,color:BK.muted,whiteSpace:'nowrap'}}>{lab}</span>;
  return <button type="button" className="chip" data-ref-door={room} onClick={() => go && go(room)} title={bkChapterName(room)}
    style={{minHeight:28,padding:'2px 7px',fontSize:11,fontWeight:900,whiteSpace:'nowrap',justifySelf:'end'}}>{lab} ›</button>;
}
const RefGo = React.createContext(null);
// a table: hairlines between rows, the columns set by the caller
function RefTable({ cols, head, rows, k }) {
  return <div data-ref-table={k} style={{display:'grid',gridTemplateColumns:cols,alignItems:'center',columnGap:8,border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'2px 10px'}}>
    {head && head.map((h, i) => <div key={'h' + i} style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',textTransform:'uppercase',padding:'7px 0 5px',borderBottom:'1px solid rgba(38,41,107,0.18)'}}>{h}</div>)}
    {rows.map((r, j) => r.map((c, i) => <div key={j + '-' + i} style={{padding:'5px 0',minWidth:0,borderBottom:j < rows.length - 1 ? '1px solid rgba(38,41,107,0.1)' : 'none',fontSize:13.5,lineHeight:1.35,color:BK.ink}}>{c}</div>))}
  </div>;
}
const RefNote = ({ children }) => <div style={{fontSize:12.5,color:BK.muted,lineHeight:1.45,margin:'6px 2px 0'}}>{children}</div>;
function RefSvgEl({ inner, w, h, vb }) { const k = React.useContext(RefPaper) ? 0.78 : 1; return <svg viewBox={vb || ('0 0 ' + w + ' ' + h)} width={w * k} height={h * k} style={{display:'block',overflow:'visible'}} dangerouslySetInnerHTML={{ __html: inner }}/>; }
const refSvg = (inner, w, h, vb) => <RefSvgEl inner={inner} w={w} h={h} vb={vb}/>;
// one note or rest, drawn with the house's own glyphs (nvbNote, nvbRest, the rhythm staff's rests): heads, stems and flags as
// everywhere else. kind: w h q e s; dot: dotted
function refNoteSvg(kind, dot) {
  const y = 46, x = 14, col = PEN_N;
  let s;
  if (kind === 's') {   // the semiquaver: the quaver's flag twice, on a longer stem
    const sx = x + NV_SX, top = y - 38;
    s = nvbHead(x, y, 'q', col, 1) + '<line x1="' + sx + '" y1="' + y + '" x2="' + sx + '" y2="' + top + '" stroke="' + col + '" stroke-width="1.9" stroke-linecap="round"/>'
      + [0, 8].map(d => '<path d="M' + sx + ' ' + (top + d) + ' c 2 8 12 10 7.5 22" fill="none" stroke="' + col + '" stroke-width="2.4" stroke-linecap="round"/>').join('');
  } else s = nvbNote(x, y, kind, { col }).svg;
  if (dot) s += '<circle cx="' + (x + 14) + '" cy="' + (y - 2) + '" r="2.6" fill="' + col + '"/>';
  return refSvg(s, 30, 46, '0 4 34 52');
}
function refRestSvg(kind) {
  const col = PEN_N;
  const s = kind === 'w' ? nvbRest(17, 22, 'w', { col }).svg : kind === 'h' ? nvbRest(17, 34, 'h', { col }).svg : kind === 'q' ? nvbRest(17, 30, 'q', { col, k: 1.05 }).svg
    : kind === 'e' ? srhQuaverRest(19, 32, col, 1.2) : srhSemiRest(19, 32, col);
  return refSvg(s, 30, 46, '0 4 34 52');
}
// a beamed group with its number over the beam: the triplet (3) and the duplet (2)
function refTupletSvg(n) {
  const xs = n === 3 ? [10, 30, 50] : [10, 34], y = 46;
  return refSvg(srhGroup(xs, y, xs.map(() => PEN_N), 1, PEN_N) + '<text x="' + ((xs[0] + xs[xs.length - 1]) / 2 + NV_SX) + '" y="7" text-anchor="middle" font-size="12" font-weight="900" font-style="italic" font-family="Georgia, serif" fill="' + PEN_N + '">' + n + '</text>', n === 3 ? 64 : 48, 52, '0 -4 ' + (n === 3 ? 64 : 48) + ' 56');
}
// a time signature: two numbers on a short staff, or the C and the cut C
function RefTime({ top, bot, sym }) {
  const lines = [0, 1, 2, 3, 4].map(i => '<line x1="0" x2="34" y1="' + (6 + i * 8) + '" y2="' + (6 + i * 8) + '" stroke="' + PEN_N + '" stroke-opacity="0.45" stroke-width="1"/>').join('');
  const num = (v, y) => '<text x="17" y="' + y + '" text-anchor="middle" font-size="17.5" font-weight="900" font-family="Georgia, serif" fill="' + PEN_N + '">' + v + '</text>';
  const inner = sym ? '<text x="17" y="28.5" text-anchor="middle" font-size="24" font-weight="900" font-family="Georgia, serif" fill="' + PEN_N + '">C</text>' + (sym === 'cut' ? '<line x1="17.5" x2="17.5" y1="6" y2="40" stroke="' + PEN_N + '" stroke-width="1.8"/>' : '')
    : num(top, 21.5) + num(bot, 37.5);
  return refSvg(lines + inner, 34, 46);
}
const refSec = (id, en, ko) => ({ id, en, ko });
const REF_SECS = [refSec('notes', 'Notes and rests', '음표와 쉼표'), refSec('time', 'Time signatures', '박자표'), refSec('keys', 'Keys and key signatures', '조와 조표'), refSec('scales', 'Scales', '음계'), refSec('intervals', 'Intervals', '음정'), refSec('chords', 'Chords and cadences', '화음과 종지'), refSec('terms', 'Signs and terms', '기호와 용어')];
function RefHead({ id }) { const s = REF_SECS.find(x => x.id === id); return <div id={'ref-' + id} data-ref-sec={id} style={{scrollMarginTop:12,margin:'0 0 8px'}}><StaffHead title={t(s.en, s.ko)}/></div>; }

// 1. notes and rests (the beats with the crotchet as one beat, as in 2/4, 3/4 and 4/4)
const REF_NOTES = [
  ['w', 0, 'semibreve', '온음표', '4', 'w', 'note-values'], ['h', 1, 'dotted minim', '점2분음표', '3', null, 'note-values'], ['h', 0, 'minim', '2분음표', '2', 'h', 'note-values'],
  ['q', 1, 'dotted crotchet', '점4분음표', '1½', null, 'rhythm'], ['q', 0, 'crotchet', '4분음표', '1', 'q', 'note-values'], ['e', 1, 'dotted quaver', '점8분음표', '¾', null, 'rhythm-3'],
  ['e', 0, 'quaver', '8분음표', '½', 'e', 'note-values'], ['s', 0, 'semiquaver', '16분음표', '¼', null, 'rhythm-2'],
];
function RefNotes() {
  return <div>
    <RefTable k="notes" cols="30px 30px minmax(0,1fr) 30px auto" head={[t('Note', '음표'), t('Rest', '쉼표'), t('Name', '이름'), t('Beats', '박'), '']}
      rows={REF_NOTES.map(([k, d, en, ko, b, r, room]) => [refNoteSvg(k, d), r ? refRestSvg(r) : <span/>, <b style={{fontWeight:800}}>{t(en, ko)}</b>, <span style={{fontWeight:900,fontSize:15}}>{b}</span>, <RefDoor room={room}/>])}/>
    <div style={{height:6}}/>
    <RefTable k="tuplets" cols="64px minmax(0,1fr) auto" rows={[[refTupletSvg(3), t('triplet: three in the time of two', '셋잇단음표: 둘 자리에 셋'), <RefDoor room="rhythm-2"/>], [refTupletSvg(2), t('duplet: two in the time of three', '2잇단음표: 셋 자리에 둘'), <RefDoor room="rhythm-2" g="Grade 3"/>]]}/>
    <RefNote>{t('Beats with the crotchet as one beat (2/4, 3/4, 4/4). A dot adds half the note’s value.', '4분음표를 한 박으로 셀 때(2/4, 3/4, 4/4)의 박. 점은 그 음표 값의 절반을 더해요.')}</RefNote>
  </div>;
}
// 2. time signatures: the bottom number; simple and compound
const REF_TS = {
  simple: [[2, 4, null, '2 crotchets', '4분음표 둘', 'time-signatures'], [3, 4, null, '3 crotchets', '4분음표 셋', 'time-signatures'], [4, 4, 'c', '4 crotchets', '4분음표 넷', 'time-signatures'],
    [2, 2, 'cut', '2 minims', '2분음표 둘', 'rhythm-3'], [3, 2, null, '3 minims', '2분음표 셋', 'rhythm-3'], [3, 8, null, '3 quavers', '8분음표 셋', 'rhythm-3']],
  compound: [[6, 8, null, '2 dotted crotchets', '점4분음표 둘', 'six-eight'], [9, 8, null, '3 dotted crotchets', '점4분음표 셋', 'rhythm-3'], [12, 8, null, '4 dotted crotchets', '점4분음표 넷', 'rhythm-3'], [6, 4, null, '2 dotted minims', '점2분음표 둘', 'rhythm-4']],
};
function RefTimeTiles({ list }) {
  const paper = React.useContext(RefPaper);
  return <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(' + (paper ? 122 : 150) + 'px,1fr))',gap:6}}>{list.map(([a, b, sym, en, ko, room]) => <div key={a + '/' + b} data-ref-ts={a + '/' + b}
    style={{display:'grid',gridTemplateColumns:sym ? '34px 34px 1fr' : '34px 1fr',alignItems:'center',gap:6,border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:10,background:'#fff',padding:'5px 8px'}}>
    <RefTime top={a} bot={b}/>{sym && <RefTime sym={sym}/>}
    <div style={{display:'flex',flexDirection:'column',gap:3,alignItems:'flex-start',minWidth:0}}><span style={{fontSize:12.5,fontWeight:800,lineHeight:1.25}}>{t(en, ko)}</span><RefDoor room={room}/></div>
  </div>)}</div>;
}
function RefTimes() {
  const lab = (en, ko) => <div style={{fontSize:12,fontWeight:900,color:BK.coral,letterSpacing:'0.06em',textTransform:'uppercase',margin:'10px 2px 5px'}}>{t(en, ko)}</div>;
  return <div>
    <RefTable k="bottom" cols="40px 38px minmax(0,1fr) auto" head={[t('Bottom', '아래 숫자'), '', t('Each count is a', '세는 단위'), '']}
      rows={[[2, 'h', 'minim', '2분음표', 'rhythm-3'], [4, 'q', 'crotchet', '4분음표', 'time-signatures'], [8, 'e', 'quaver', '8분음표', 'six-eight']].map(([n, k, en, ko, room]) => [<span style={{fontFamily:LB_SERIF,fontWeight:900,fontSize:20}}>{n}</span>, refNoteSvg(k), <b style={{fontWeight:800}}>{t(en, ko)}</b>, <RefDoor room={room}/>])}/>
    <RefNote>{t('The top number: how many in a bar.', '위 숫자: 한 마디에 몇 개.')}</RefNote>
    {lab('Simple: each beat splits in two', '홑박자: 한 박이 둘로')}<RefTimeTiles list={REF_TS.simple}/>
    {lab('Compound: each beat is a dotted note and splits in three', '겹박자: 한 박이 점음표, 셋으로')}<RefTimeTiles list={REF_TS.compound}/>
  </div>;
}
// 3. keys: the order of the signs, every key with its relative minor, where the house first meets it (the scales rooms' key
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
// 4. scales: each form's steps counted from its notes (semitones from the key note); then the Scales map, floor by floor
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
function RefScales() {
  const paper = React.useContext(RefPaper), [map, setMap] = useState(false), go = React.useContext(RefGo);
  return <div>
    <RefTable k="scales" cols="minmax(0,1fr) auto" head={[t('Form · its steps (T tone, S semitone)', '형태 · 걸음(T 온음, S 반음)'), '']}
      rows={REF_SCALES.map(([id, en, ko, semis, room]) => { const steps = semis.slice(1).map((v, i) => v - semis[i]);
        return [<div data-ref-scale={id}><b style={{fontWeight:800}}>{t(en, ko)}</b><div style={{display:'flex',flexWrap:'wrap',gap:3,marginTop:3}}>{id === 'chr' ? <span style={{fontSize:12,fontWeight:800,color:BK.muted}}>{t('S × 12', 'S × 12')}</span>
          : steps.map((d, i) => <span key={i} style={{fontSize:11.5,fontWeight:900,padding:'1px 6px',borderRadius:6,border:'1.2px solid ' + (d === 1 ? BK.coral : 'rgba(38,41,107,0.35)'),color:d === 1 ? BK.coral : BK.ink}}>{refStep(d)}</span>)}</div></div>, <RefDoor room={room}/>]; })}/>
    {!paper && <div style={{margin:'8px 0 0'}}>
      <button type="button" className="ghost-btn" data-ref-scalesmap aria-expanded={map} onClick={() => setMap(x => !x)} style={{width:'100%',minHeight:44,fontSize:14}}>{map ? t('Hide the scales floor by floor', '층마다 스케일 닫기') : t('Every grade’s scales, floor by floor ›', '급마다 스케일, 층마다 ›')}</button>
      {map && <div style={{marginTop:8}}><ScalesMapView onChapter={go}/></div>}
    </div>}
  </div>;
}
// 5. intervals: by number, with the semitones in each quality; the rules
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
// 6. chords: the triad on every degree of C major (semibreves, no stems), the degree names, the kinds, the positions, cadences
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
function RefChords() {
  const rm = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°'], q = ['major', 'minor', 'minor', 'major', 'major', 'minor', 'diminished'], qk = { major: '장', minor: '단', diminished: '감' };
  return <div>
    <RefChordStaff/>
    <RefTable k="degrees" cols="44px minmax(0,1fr) auto" head={[t('Degree', '음'), t('Name · its triad in a major key', '이름 · 장조에서의 3화음'), '']}
      rows={rm.map((r, i) => [<b style={{fontFamily:LB_SERIF,fontWeight:900,fontSize:15,color:i === 0 || i === 3 || i === 4 ? BK.coral : BK.ink}}>{r}</b>, <span><b style={{fontWeight:800}}>{t(DEGREE_NAMES[i], DEGREE_NAMES_KO[i])}</b> · {t(q[i], qk[q[i]] + '3화음')}</span>, i === 0 ? <RefDoor room="harmony-3"/> : <span/>])}/>
    <div style={{height:8}}/>
    <RefTable k="chordkinds" cols="minmax(0,1fr) auto" rows={[
      [t('Major triad: a major 3rd, then a minor 3rd. Minor: a minor 3rd, then a major 3rd.', '장3화음: 장3도 위에 단3도. 단3화음: 단3도 위에 장3도.'), <RefDoor room="chords"/>],
      [t('I, IV and V: the primary triads.', 'I, IV, V: 주요 3화음.'), <RefDoor room="chords"/>],
      [t('Root position (a), first inversion (b): the 3rd in the bass.', '기본 위치(a), 첫째 자리바꿈(b): 3음이 베이스.'), <RefDoor room="harmony-3"/>],
      [t('Second inversion (c): the 5th in the bass; Ic before V is the cadential 6-4.', '둘째 자리바꿈(c): 5음이 베이스; V 앞의 Ic가 종지 6-4.'), <RefDoor room="harmony-5"/>],
      [t('Diminished triad: two minor 3rds (vii° in a major key).', '감3화음: 단3도 둘(장조의 vii°).'), <RefDoor room="harmony-5"/>],
      [t('Dominant 7th (V7): V with a minor 7th above its root; four positions, a b c d.', '딸림7화음(V7): V에 근음 위 단7도; 네 자리 a b c d.'), <RefDoor room="harmony-6"/>],
      [t('Diminished 7th of a key: three minor 3rds, starting on its leading note.', '조의 감7화음: 단3도 셋, 그 조의 이끎음에서 시작.'), <RefDoor room="arps-6"/>],
      [t('Augmented triad: two major 3rds.', '증3화음: 장3도 둘.'), <RefDoor room="listen-8"/>],
    ]}/>
    <div style={{height:8}}/>
    <RefTable k="cadences" cols="minmax(0,1fr) 58px auto" head={[t('Cadence', '종지'), '', '']} rows={[   // the rooms' own words (Chords and Cadences, Grade 4)
      [<span><b style={{fontWeight:800}}>{t('perfect', '정격종지')}</b> · {t('a full stop', '마침표(.)')}</span>, <b style={{fontFamily:LB_SERIF}}>V – I</b>, <RefDoor room="harmony-3"/>],
      [<span><b style={{fontWeight:800}}>{t('plagal', '변격종지')}</b> · {t('the “Amen”', '“아멘”')}</span>, <b style={{fontFamily:LB_SERIF}}>IV – I</b>, <RefDoor room="harmony-3"/>],
      [<span><b style={{fontWeight:800}}>{t('imperfect', '반종지')}</b> · {t('a comma', '쉼표(,)')}</span>, <b style={{fontFamily:LB_SERIF}}>… – V</b>, <RefDoor room="harmony-4"/>],
      [<span><b style={{fontWeight:800}}>{t('interrupted', '거짓종지')}</b> · {t('the surprise', '깜짝')}</span>, <b style={{fontFamily:LB_SERIF}}>V – vi</b>, <RefDoor room="harmony-4"/>],
    ]}/>
  </div>;
}
// 7. signs and terms: the dictionary's words, floor by floor; a tap opens its card
const REF_TERM_NAME = { 'dotted-note': ['dotted note', '점음표'], step: ['step', '차례가기'], natural: ['natural', '제자리표'], key: ['key', '조'] };   // these four keep no word list (so the text does not link every 'key' or 'step')
const refTermName = (x) => LANG === 'ko' ? (x.ko[0] || (REF_TERM_NAME[x.id] || [])[1] || x.id) : (x.en[0] || (REF_TERM_NAME[x.id] || [])[0] || x.id);
function RefTerms() {
  const paper = React.useContext(RefPaper), [card, setCard] = useState(null);
  const floors = STAGES.map(s => ({ name: s.en ? s.en[0] : '', terms: DICT_TERMS.filter(x => s.ids.includes(x.room)) })).filter(f => f.terms.length);
  return <div data-ref-terms>
    {floors.map(f => <div key={f.name} style={{display:'grid',gridTemplateColumns:'74px minmax(0,1fr)',gap:6,alignItems:'baseline',padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.1)'}}>
      <span style={{fontSize:11,fontWeight:900,color:BK.coral,letterSpacing:'0.04em'}}>{f.name}</span>
      <span style={{display:'flex',flexWrap:'wrap',gap:paper ? '0 10px' : 4}}>{f.terms.map(x => paper ? <span key={x.id} style={{fontSize:12.5,fontWeight:700}}>{refTermName(x)}</span>
        : <button key={x.id} type="button" className="chip" data-ref-term={x.id} onClick={() => setCard(x.id)} style={{minHeight:30,padding:'2px 9px',fontSize:12.5,fontWeight:800}}>{refTermName(x)}</button>)}</span>
    </div>)}
    {card && <DictCard id={card} onClose={() => setCard(null)}/>}
  </div>;
}
const REF_BODY = { notes: RefNotes, time: RefTimes, keys: RefKeys, scales: RefScales, intervals: RefIntervals, chords: RefChords, terms: RefTerms };
function ReferenceView({ onChapter }) {
  const jump = (id) => { const el = document.getElementById('ref-' + id); if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
  return <RefGo.Provider value={onChapter || null}><div data-reference style={{display:'flex',flexDirection:'column',gap:18}}>
    <div>
      <div style={{fontSize:14,color:'#4a4d86',lineHeight:1.5,margin:'0 0 8px'}}>{t('The whole of the theory on a few tables, Beginner to Grade 8. Each row shows the floor where you learn it: tap it to go to that room.', 'Beginner부터 Grade 8까지의 이론을 표 몇 장에. 줄마다 그걸 배우는 층이 있어요: 누르면 그 방으로 가요.')}</div>
      <div style={{display:'flex',flexWrap:'wrap',gap:5}}>{REF_SECS.map(s => <button key={s.id} type="button" className="chip" data-ref-jump={s.id} onClick={() => jump(s.id)} style={{minHeight:34,padding:'3px 11px',fontSize:12.5,fontWeight:800}}>{t(s.en, s.ko)}</button>)}</div>
    </div>
    {REF_SECS.map(s => { const B = REF_BODY[s.id]; return <section key={s.id} style={{minWidth:0}}><RefHead id={s.id}/><B/></section>; })}
  </div></RefGo.Provider>;
}
// on paper: five A4 pages in the books' look
const REF_PAGES = [['notes', 'time'], ['keys'], ['scales', 'intervals'], ['chords'], ['terms']], REF_PAGE_COLS = { 0: true };   // page 1 in two columns
function RefBook() {
  return <RefPaper.Provider value={true}>{REF_PAGES.map((ids, i) => <section key={i} className="bk-page" data-ref-page={i + 1} style={{position:'relative'}}>
    <VicFloor no={i + 1}/>
    <VicHead left={t('Reference', '한눈에 보기')} right={ids.map(id => { const s = REF_SECS.find(x => x.id === id); return t(s.en, s.ko); }).join(' · ')} mb={10}/>
    <div className="bk-body" style={REF_PAGE_COLS[i] ? {flex:1,minHeight:0,overflow:'hidden',display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,alignItems:'start'} : {flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:12}}>{ids.map(id => { const B = REF_BODY[id]; return <div key={id} style={{minWidth:0}}><RefHead id={id}/><B/></div>; })}</div>
  </section>)}</RefPaper.Provider>;
}
