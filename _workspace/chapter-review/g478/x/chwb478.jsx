// ─── Phase 478: chapter 22's Workbook (pages 2 to 8: one per lesson step, any key, the check-up) and the Teacher copy ───
// (they replace the Phase 117 ones). Chapter 21's ivxAns, ivxCircle and ivxTicks are reused.
const chxW = (r) => [0, 2, 4].map(s => IVX_N(CHX_D[r] + s));                     // a white-key triad, treble
const chxWB = (r) => { const d = CHX_D[r] - (CHX_D[r] >= 32 ? 14 : 7); return [0, 2, 4].map(s => IVX_N(d + s)); };   // and on the bass staff
const CHX_WB = {
  try2: ['C', 'D', 'F', 'A'],                                       // C E G (done), D F A, F A C, A C E
  turn2: [['E', 'treble'], ['G', 'treble'], ['B', 'treble'], ['C', 'bass'], ['F', 'bass'], ['A', 'bass']],   // E G B, G B D, B D F; C E G, F A C, A C E
  try3: ['C', 'D', 'F', 'E'],                                       // major (done), minor, major, minor
  turn3: ['C', 'G', 'D', 'F', 'A', 'E'],                            // C E♭ G, G B♭ D, D F A, F A♭ C, A C E, E G B
  try4: ['G', 'D', 'F', 'C'],                                       // G major (done), D major, F major, C major
  turn4: [['G', 'treble'], ['D', 'treble'], ['F', 'treble'], ['D', 'treble', 1], ['C', 'bass'], ['G', 'bass']],   // #8: no key signature (the ♯ written in)
  try5: [['G', 1], ['G', 5], ['C', 4], ['F', 5]],                   // I (done), V, IV, V
  turn5: ['G', 'F'],
  try6: [['C', 'treble', 0], ['F', 'bass', 1], ['G', 'treble', 1], ['A', 'bass', 0]],   // blocked (done), broken, broken, blocked
  turn6: [['C', 'treble'], ['G', 'treble'], ['F', 'treble'], ['F', 'bass'], ['D', 'bass'], ['C', 'bass']],
};
const CHX_CHK = {
  root: [['treble', 'G'], ['bass', 'D'], ['treble', 'F'], ['bass', 'A']],   // G, D, F, A
  draw: [['E', 'treble'], ['C', 'bass'], ['A', 'treble']],                  // E G B, C E G, A C E
  mm: [['D', 'major'], ['E', 'minor']],                                     // major (D F♯ A), minor (E G B)
  rom: [['G', 4], ['F', 5], ['D', 1]],                                      // IV, V, I
};
const chxChkNo = () => { const C = CHX_CHK, nB = C.root.length + 1, nC = nB + C.draw.length, nD = nC + C.mm.length; return { nB, nC, nD, total: nD + C.rom.length - 1 }; };
const chxPaper = (clef, places, w = 220, o = {}, k = 1) => <div style={{width:'100%',maxWidth:w * k,margin:'0 auto'}}><ChxStaff clef={clef} places={places} width={w} o={{ x0: 60, padTop: 14, ...o }}/></div>;
const chxTitle = (x) => <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginTop:4}}>{sscSx(x)}</div>;
// the root alone, room above it for the 3rd and the 5th
const chxWriteStaff = (notes, clef, w = 170, k = 1.25, o = {}) => chxPaper(clef, [{ notes: [notes[0]] }], w, { x0: 66, padTop: 22, ...o }, k);
const chxRomTitle = (k, dg) => chxTitle(skgKeyName(k));
const chxCircle = (words, on) => <div style={{display:'flex',justifyContent:'center',gap:6,fontSize:12.5,fontWeight:800,color:BK.ink,margin:'2px 0'}}>{words.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:'0 6px',color:on === w ? BK.coral : BK.ink}}>{w}</span>)}</div>;

function ChxWorkbook({ startNo = 1 }) {
  const W = CHX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="chords">{content}</WbPage>);

  // 2 (faces "Stack a triad")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Its letters" how="Skip a letter, skip a letter: write the triad’s three letters on each root. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try2.map((r, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{chxPaper('treble', [{ notes: i === 0 ? chxW(r) : [chxW(r)[0]] }], 130, { x0: 50, padTop: 22 })}<div style={{marginTop:'auto'}}>{ivxAns(i === 0, chxNotesTxt(chxW(r)), 96, 30)}</div></>, '8px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the triad" how="Draw the 3rd and the 5th above each root: all three on lines, or all three in spaces.">
      <BkGrid cols={3} gap="8px 10px">{W.turn2.map(([r, clef], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{chxTitle('The triad on ' + r)}{chxWriteStaff(clef === 'bass' ? chxWB(r) : chxW(r), clef, 160, 1.45, { padTop: 54 })}</>, '4px 2px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Every white key" how="Play the triad on each white key from C to B, saying its letters. Then with the left hand. Tick each one.">
      {sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{chxPaper('treble', CHX_L.split('').map(r => ({ notes: chxW(r), lab: r })), 440, { x0: 64, labSize: 13 }, 1.35)}{ivxTicks(['right hand', 'left hand'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Major and minor")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Count the half steps" how="Count from the root to the 3rd: 4 half steps make it major, 3 make it minor. Write major or minor. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try3.map((r, i) => { const nt = chxW(r); return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{maxWidth:140,margin:'0 auto',width:'100%'}}><ChxKeys d0={CHX_D[r]} n={5} o={{ H: 92, lit: [ivMidi(nt[0])], pale: [ivMidi(nt[1]), ivMidi(nt[2])], nums: i === 0 ? chxCount(nt) : {} }}/></div><div style={{marginTop:'auto'}}>{ivxAns(i === 0, chxWhiteQ(r), 80, 30)}</div></>, '16px 4px 4px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Make it minor" how="After the arrow, write the same triad minor: the 3rd a half step lower (C E G becomes C E♭ G).">
      <BkGrid cols={2} gap="8px 14px">{W.turn3.map((r, i) => { const nt = chxNotes(r); return <BkCell key={i} n={i + 5}>{sdyCol(chxPaper('treble', [{ notes: nt, lab: r + ' major' }, { blank: true }], 240, { x0: 56, arrow: true }, 1.25), '8px 4px 6px')}</BkCell>; })}</BkGrid>
    </Part>
    <Part kind="play" title="Listen and say" how="Your teacher plays six triads. Circle major or minor for each.">
      {sskRowN(9, <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:'10px 12px'}}>{[1, 2, 3, 4, 5, 6].map(i => <div key={i} style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,border:'1.2px solid ' + BK.line,borderRadius:8,padding:'10px 4px'}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:15,fontWeight:800,color:BK.muted}}>{i}</span>{chxCircle(['major', 'minor'])}</div>)}</div>)}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "The tonic triad")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Whose tonic triad?" how="Read the key signature and the triad. Write the key. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try4.map((k, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{chxPaper('treble', [{ notes: chxDeg(k, 1) }], 132, { x0: 46, padTop: 22, key: k })}{ivxAns(i === 0, prettyNote(k) + ' major', 100, 30)}</>, '8px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the tonic triad" how="Draw the tonic triad: the 1st, 3rd and 5th notes of the scale. With no key signature (8), write its sharp or flat.">
      <BkGrid cols={3} gap="8px 10px">{W.turn4.map(([k, clef, nk], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{chxTitle(skgKeyName(k) + (nk ? ', no key signature' : ''))}{chxPaper(clef, [{ blank: true }], 160, { x0: 52, padTop: 46, key: nk ? null : k }, 1.45)}</>, '4px 2px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Tonic triads" how="Play the tonic triad of each key, together and then one note at a time. Tick each way.">
      {sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{chxPaper('treble', CHX_TONIC_KEYS.map(k => ({ notes: chxDeg(k, 1), lab: prettyNote(k) + ' major' })), 400, { x0: 64, labSize: 12.5, bars: true }, 1.4)}{ivxTicks(['together', 'one note at a time'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "I, IV and V")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="I, IV or V?" how="Read the key, then the triad’s root. Write I, IV or V. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try5.map(([k, dg], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{chxRomTitle(k)}{chxPaper('treble', [{ notes: chxDeg(k, dg) }], 132, { x0: 46, padTop: 22, key: k })}<div style={{marginTop:'auto'}}>{ivxAns(i === 0, CHX_ROM[dg], 60, 30)}</div></>, '6px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write I, IV and V" how="Draw each triad in its bar. The key signature gives its sharps or flats.">
      <BkGrid cols={1} gap="8px">{W.turn5.map((k, i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{chxTitle(skgKeyName(k))}{chxPaper('treble', [1, 4, 5].map(dg => ({ blank: true, lab: CHX_ROM[dg] })), 420, { x0: 60, padTop: 26, key: k, bars: true, labSize: 16 }, 1.2)}</>, '4px 6px 6px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="I IV V I" how="Play I, IV, V and I again, blocked, saying the numerals. Tick each key.">
      {sskRowN(8, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{chxPaper('treble', [1, 4, 5, 1].map(dg => ({ notes: chxDeg('C', dg), lab: CHX_ROM[dg] })), 360, { x0: 64, labSize: 14, bars: true }, 1.35)}{ivxTicks(['C major', 'G major', 'F major'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Both hands")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Blocked or broken?" how="Circle blocked or broken, and the hand that plays it. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try6.map(([r, clef, br], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{chxPaper(clef, [{ notes: clef === 'bass' ? chxWB(r) : chxW(r), broken: !!br }], 130, { x0: 48, padTop: 20, gap: 21 })}<div style={{marginTop:'auto'}}>{chxCircle(['blocked', 'broken'], i === 0 ? (br ? 'broken' : 'blocked') : null)}{chxCircle(['RH', 'LH'], i === 0 ? (clef === 'bass' ? 'LH' : 'RH') : null)}</div></>, '8px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write it broken" how="After the arrow, write the same triad broken: its three notes one after the other, from the root up.">
      <BkGrid cols={2} gap="8px 14px">{W.turn6.map(([r, clef], i) => <BkCell key={i} n={i + 5}>{sdyCol(chxPaper(clef, [{ notes: clef === 'bass' ? chxWB(r) : chxW(r) }, { blank: true }], 240, { x0: 56, padTop: 8, arrow: true }, 1.05), '8px 4px 6px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Both hands" how="Left hand blocked, right hand broken: C, then F, then G. Then swap. Tick each.">
      {sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:0,width:'100%'}}>{chxPaper('treble', ['C', 'F', 'G'].map(r => ({ notes: chxW(r), broken: true })), 380, { x0: 60, bars: true, padTop: 6 }, 1.12)}{chxPaper('bass', ['C', 'F', 'G'].map(r => ({ notes: chxWB(r), lab: r })), 380, { x0: 60, bars: true, padTop: 4, labSize: 14 }, 1.12)}<div style={{marginTop:6}}>{ivxTicks(['C', 'F', 'G', 'swapped'])}</div></div>)}
    </Part>
    <Faces/>
  </>);

  // 7. any key: the teacher writes the key; 8. the check-up on paper
  P(<ChxAnyKeyPage/>);
  P(<ChxPaperCheck/>);
  return <>{pages}</>;
}
function ChxAnyKeyPage() {
  const bw = 128.5;   // a bar: four between x 100 and 614
  return <>
    <WbTop step={7}/>
    {pbKeysHead()}
    <Part kind="together" title="Its scale" how={<span style={{textWrap:'pretty'}}>Write the key’s scale, going up from the tonic: eight notes, each with its sharp or flat. Circle the 1st, 4th and 5th.</span>}>
      {sskRowN(1, pbBoxes(8, 50, 44, null, 10))}
    </Part>
    <Part kind="home" title="I, IV, V and I" how={<span style={{textWrap:'pretty'}}>Write the key signature, then I, IV, V and I in the bars. Write each one’s letters in the box under it.</span>}>
      {sskRowN(2, <div style={{width:'100%',maxWidth:640,margin:'0 auto'}}><SfStaff clef="treble" width={620} pad={[44, 66]} extra={(yOf, layer) => layer !== 'over' ? null : <g>{[1, 2, 3].map(i => <line key={i} x1={100 + i * bw} x2={100 + i * bw} y1={yOf(38)} y2={yOf(30)} stroke={BK.ink} strokeWidth="1.3"/>)}<line x1={614} x2={614} y1={yOf(38)} y2={yOf(30)} stroke={BK.ink} strokeWidth="1.3"/>
        {['I', 'IV', 'V', 'I'].map((w, i) => <text key={i} x={100 + (i + 0.5) * bw} y={yOf(38) - 18} textAnchor="middle" fontSize="17" fontWeight="900" fill={BK.ink} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{w}</text>)}
        {[0, 1, 2, 3].map(i => <rect key={'bx' + i} x={100 + i * bw + 14} y={yOf(30) + 28} width={bw - 28} height={30} rx="4" fill="#fff" stroke={BK.line} strokeWidth="1.3"/>)}</g>}/></div>)}
    </Part>
    <Part kind="play" title="Play them" how="Fill the circles of I on the keys. Play I, IV, V and I: blocked, then broken, then the left hand blocked under the right hand broken. Tick each time.">
      {sskRowN(3, <div style={{maxWidth:620,margin:'0 auto',width:'100%'}}><TnPKeys start="C" whites={14} w={37} h={130} slots wslots/></div>)}
      <div style={{marginTop:8}}>{ivxTicks(['blocked', 'broken', 'both hands'])}</div>
    </Part>
    <Part kind="year" title="My twelve keys"><div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',gap:'8px 10px'}}>{FIFTHS.map(k => <div key={k} style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,border:'1.2px solid ' + BK.line,borderRadius:8,padding:'6px 4px',fontFamily:'Inter, sans-serif',fontSize:16,fontWeight:900,color:BK.ink}}>{prettyNote(k)}{bkBox(20, 20)}</div>)}</div>
      <div style={{fontSize:12.5,color:BK.muted,marginTop:6}}>Tick a key when you can play its I, IV and V and name their letters. Keep this on your first copy.</div></Part>
    <Faces/>
  </>;
}
function ChxPaperCheck() {
  const C = CHX_CHK, { nB, nC, nD } = chxChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the root of each triad.')}
    <BkGrid cols={2} gap="6px 10px">{C.root.map(([clef, r], i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{chxPaper(clef, [{ notes: clef === 'bass' ? chxWB(r) : chxW(r) }], 180, { x0: 56, padTop: 20 }, 1.3)}{ivxAns(false, '', 56, 28)}</>, '6px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Draw the triad on each note: the 3rd and the 5th above it.')}
    <BkGrid cols={3} gap="6px 8px">{C.draw.map(([r, clef], i) => <BkCell key={i} n={nB + i}>{sdyCol(<>{chxTitle('The triad on ' + r)}{chxWriteStaff(clef === 'bass' ? chxWB(r) : chxW(r), clef, 150, 1.5, { padTop: 30 })}</>, '4px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Major or minor? Circle one.')}
    <BkGrid cols={2} gap="6px 10px">{C.mm.map(([r, q], i) => <BkCell key={i} n={nC + i}>{sdyCol(<>{chxPaper('treble', [{ notes: chxNotes(r, q) }], 180, { x0: 56, padTop: 20 }, 1.3)}{ivxCircle(['major', 'minor'])}</>, '6px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Write I, IV or V.')}
    <BkGrid cols={3} gap="6px 8px">{C.rom.map(([k, dg], i) => <BkCell key={i} n={nD + i}>{sdyCol(<>{chxTitle(skgKeyName(k))}{chxPaper('treble', [{ notes: chxDeg(k, dg) }], 150, { x0: 56, key: k, padTop: 20 }, 1.5)}{ivxAns(false, '', 60, 28)}</>, '4px 2px 4px')}</BkCell>)}</BkGrid>
  </div>;
}

function ChxTeacher() {
  const W = CHX_WB, C = CHX_CHK, pages = [], { nB, nC, nD, total } = chxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="chords" teacher>{content}</WbPage>);
  const wl = (r) => chxNotesTxt(chxW(r)), minorOf = (r) => chxTxt(chxSpell(r, 'minor'));
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('chords')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{sscSx('Triads (chapter ' + bkChapterNo('tones') + ': half steps; chapter ' + bkChapterNo('scales') + ': the scale’s degrees; chapter ' + bkChapterNo('intervals') + ': 3rds and 5ths). AMEB Music Craft: Preliminary, the tonic triad of C, G and F major in root position (treble), with or without key signature; Grade 1, I and V in root position, treble and bass, in C, G, D, F and B♭ major (and i and V in A, E, D and G harmonic minor); Grade 2, I, ii, IV and V (root and 1st inversion, with Roman numerals), major and minor triads by ear; Grade 3, major and minor triads in writing. ABRSM Theory: Grade 1, the tonic triads of C, G, D and F major; Grade 2, minor tonic triads; Grade 4, I, IV and V in root position. The chord clock: Lesson Book page 1 (every major triad one shape, 4 + 3 half steps); the screen lesson ends with I, IV and V in the student’s keys. Not here: inversions, cadences, chords in minor keys, 7ths (the toolbox).')}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12.5,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>Stacking.</b> Root, 3rd, 5th: skip a letter, skip a letter; on the staff all lines or all spaces. Major: a major 3rd (4 half steps), then a minor 3rd (3); minor: a minor 3rd, then a major 3rd. The 5th is the same in both (7 half steps). In a major key, I, IV and V are major. B D F (3 + 3 half steps) is neither: a diminished triad, not taught here.</div>
    <TcBlock page={2} title="Stack a triad" answers={<>{sscLesson('Right hand C E G with 1 3 5; then the triad on each white key, saying the letters.')}{skgTcAns('TRY IT', W.try2.map((r, i) => wl(r) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn2.map(([r, clef]) => chxNotesTxt(clef === 'bass' ? chxWB(r) : chxW(r)) + (clef === 'bass' ? ' (bass)' : '')), 5)}</>}
      watch="A triad written line, space, line (stacked 2nds or 4ths). The root taken as the top note. On the bass staff, the notes read as if treble. Exam papers say “root position”: the root at the bottom."
      say="“Skip a letter, skip a letter.”"/>
    <TcBlock page={3} title="Major and minor" answers={<>{sscLesson('C E G, then C E♭ G: the child counts the half steps (4 + 3, 3 + 4). Then six triads to hear, the child circling major or minor: e.g. C major, A minor, F major, D minor, G major, E minor.')}{skgTcAns('TRY IT', W.try3.map((r, i) => chxWhiteQ(r) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn3.map(r => minorOf(r)), 5)}</>}
      watch="Counting the keys from the root including it (5 for a major 3rd). D major taken as D F A. Moving the 5th instead of the 3rd."
      say="“Major: 4 + 3. Minor: 3 + 4.”"/>
    <TcBlock page={4} title="The tonic triad" answers={<>{sscLesson('The scale of G major, then G B D; the same in C, D and F. (The screen pad adds B♭ major.)')}{skgTcAns('TRY IT', W.try4.map((k, i) => skgKeyName(k) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn4.map(([k, clef, nk]) => chxNotesTxt(chxDeg(k, 1)) + (clef === 'bass' ? ' (bass)' : '') + (nk ? ' (the ♯ written in)' : '')), 5)}</>}
      watch="A sharp or flat written again beside the note when the key signature already gives it (allowed, but not needed). D major’s triad without F♯ when there is no key signature."
      say="“1, 3, 5 of the scale.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="I, IV and V" answers={<>{sscLesson('I IV V I in C, saying the numerals; then in G and F, saying the letters G, C, D, G and F, B♭, C, F.')}{skgTcAns('TRY IT', W.try5.map(([k, dg], i) => CHX_ROM[dg] + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn5.map(k => skgKeyName(k) + ': ' + [1, 4, 5].map(dg => CHX_ROM[dg] + ' ' + chxNotesTxt(chxDeg(k, dg))).join(', ')), 5)}</>}
      watch="IV found by counting four letters up from the tonic (G → D) instead of counting the tonic as 1 (G A B C). F major’s IV written B D F (B♭ needed when there is no key signature)."
      say="“I, IV, V: the 1st, 4th and 5th notes.”"/>
    <TcBlock page={6} title="Both hands" answers={<>{sscLesson('C E G blocked and broken, right hand 1 3 5, left hand 5 3 1; then LH blocked under RH broken on C, F and G.')}{skgTcAns('TRY IT', W.try6.map(([, clef, br], i) => (br ? 'broken' : 'blocked') + ', ' + (clef === 'bass' ? 'LH' : 'RH') + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn6.map(([r, clef]) => chxNotesTxt(clef === 'bass' ? chxWB(r) : chxW(r)) + ' in a row' + (clef === 'bass' ? ' (bass)' : '')), 5)}</>}
      watch="A broken chord written top down. The left hand fingering 1 3 5 from the root."
      say="“Together, then one after the other.”"/>
    <TcBlock page={7} title="Any key (photocopy it for each new key)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>For whichever key you write at the top (set in Log lesson › For the student › Keys). Its scale: the Scale finder (toolbox). I, IV and V: the triads on the scale’s 1st, 4th and 5th notes, all major (e.g. E♭ major: E♭ G B♭, A♭ C E♭, B♭ D F). F♯ and C♯ major show as G♭ and D♭ (the same keys).</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.root.map(([, r]) => r))}
      {skgTcAns('B', C.draw.map(([r, clef]) => chxNotesTxt(clef === 'bass' ? chxWB(r) : chxW(r))), nB)}
      {skgTcAns('C', C.mm.map(([r, q]) => q + ' (' + chxTxt(chxSpell(r, q)) + ')'), nC)}
      {skgTcAns('D', C.rom.map(([k, dg]) => CHX_ROM[dg]), nD)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer: A {C.root.length}, B {C.draw.length}, C {C.mm.length}, D {C.rom.length}; {total} in all. B: both notes for the mark. D shows the key signature, as exam papers do. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1 and 5', page: '2 and 6' }, { id: 'b', step: '1', page: '2' }, { id: 'c', step: '2', page: '3' }, { id: 'd', step: '3 and 4', page: '4 and 5' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 stack a triad: its letters · 2 name the root · 3 major or minor · 4 write it (tap the notes, then Check) · 5 listening: major or minor (screen only) · 6 the bass staff · 7 tonic triads: which key · 8 I, IV or V in the student’s keys · 9 extra: spell I, IV and V.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: stack a triad on two white keys you name; the child says its letters. 2. Page 3: play C E G and C E♭ G; the child counts the half steps and names each, then names two by ear. 3. Page 4: write and play the tonic triad of C, G, D and F major. 4. Page 5: play I, IV and V in C and G major and name their letters. 5. Page 6: a triad blocked and broken in each hand. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['chords'] = ChxWorkbook;
TEACHER_COPIES['chords'] = ChxTeacher;
