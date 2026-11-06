// ─── Phase 477: chapter 21's Workbook (pages 2 to 8: one per lesson step, any key, the check-up) and the Teacher copy ───
// (they replace the Phase 116 ones)
const ivxP = (a, b, harm) => ({ a: IVX_N(a), b: IVX_N(b), harm: !!harm });
const IVX_WB = {
  try2: [ivxP(28, 30), ivxP(31, 35), ivxP(29, 32), ivxP(33, 34)],                                   // 3rd (done), 5th, 4th, 2nd
  turn2: [['bass', ivxP(18, 21)], ['treble', ivxP(30, 35, 1)], ['bass', ivxP(20, 26, 1)], ['treble', { ...ivxP(35, 37), down: true }]],   // 4th, 6th, 7th, 3rd (going down: E then C)
  play2: [ivxP(28, 32), ivxP(32, 34), ivxP(29, 35)],                                                 // 5th, 3rd, 7th
  try3: [2, 4, 1, 3],                                                                                // C position: the thumb and E (3rd, done), G, D, F
  turn3: [[28, 'treble', 3], [32, 'treble', 5], [30, 'treble', 4], [18, 'bass', 3], [29, 'treble', 2], [19, 'bass', 5]],   // E, D, A, B, E, E
  play3: [2, 3, 4, 5].map(n => ivxP(28, 28 + n - 1, 1)),
  try4: [ivxP(28, 33, 1), ivxP(29, 35, 1), ivxP(30, 37, 1), ivxP(31, 36, 1)],                       // 6th (done), 7th, octave, 6th
  turn4: [[29, 'treble', 6], [30, 'treble', 8], [31, 'treble', 7], [20, 'bass', 6]],                 // B, E, E, G
  play4: [28, 29, 30, 31].map(d => ivxP(d, d + 7, 1)),
  try5: [ivxP(28, 30), ivxP(32, 34, 1), ivxP(29, 30, 1), ivxP(31, 35)],                             // melodic 3rd (done), harmonic 3rd, harmonic 2nd, melodic 5th
  turn5: [['treble', ivxP(28, 32)], ['treble', ivxP(30, 31)], ['bass', ivxP(18, 22)], ['bass', ivxP(21, 23)]],
  try6: [3, 5, 6, 4],                                                                                // G major: major 3rd (done), perfect 5th, major 6th, perfect 4th
  turn6: [['D', 3], ['F', 4], ['C', 7], ['D', 7], ['C', 5], ['F', 7]],                               // F♯, B♭, B, C♯, G, E
};
const IVX_CHK = {
  num: [['treble', ivxP(29, 33)], ['bass', ivxP(18, 23, 1)], ['treble', ivxP(32, 33, 1)], ['bass', ivxP(21, 28)]],   // 5th, 6th, 2nd, octave
  above: [[30, 'treble', 4], [19, 'bass', 3], [28, 'treble', 7]],                                                  // A, C, B
  mh: [['treble', ivxP(31, 33, 1)], ['treble', ivxP(29, 34)]],                                                     // harmonic, melodic
  tonic: [['C', 3], ['F', 5], ['D', 6]],                                                                           // major 3rd, perfect 5th, major 6th
};
const ivxChkNo = () => { const C = IVX_CHK, nB = C.num.length + 1, nC = nB + C.above.length, nD = nC + C.mh.length; return { nB, nC, nD, total: nD + C.tonic.length - 1 }; };
// an answer under a picture: in the example, the answer in coral; else a box
const ivxAns = (ex, txt, w = 74, h = 30) => <div style={{display:'flex',justifyContent:'center',margin:'4px 0 2px'}}>{ex ? <span style={{display:'inline-flex',alignItems:'center',justifyContent:'center',minWidth:w,height:h,border:'1.5px solid ' + BK.coral,borderRadius:6,color:BK.coral,fontWeight:900,fontStyle:'italic',fontSize:14,padding:'0 6px'}}>{txt}</span> : bkBox(w, h)}</div>;
const ivxCircle = (words, on) => <div style={{display:'flex',justifyContent:'center',gap:14,fontSize:13,fontWeight:800,color:BK.ink,margin:'2px 0'}}>{words.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:'0 8px',color:on === w ? BK.coral : BK.ink}}>{w}</span>)}</div>;
const ivxPaper = (clef, pairs, w = 220, o = {}, k = 1) => <div style={{width:'100%',maxWidth:w * k,margin:'0 auto'}}><IvxStaff clef={clef} pairs={pairs} width={w} o={{ x0: 60, padTop: 14, ...o }}/></div>;
const ivxAboveTitle = (d, n) => <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginTop:4}}>{(n === 8 ? 'Octave' : ivxEn(n)) + ' above ' + dName(d)}</div>;
const ivxTicks = (ws) => <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{ws.map(w => sprTickW(w))}</div>;
// the note to write: the bottom note, and room for the top one (a blank pair beside it)
const ivxWriteStaff = (d, clef, w = 180, k = 1.2) => ivxPaper(clef, [{ a: IVX_N(d), b: IVX_N(d), harm: true, onlyA: true }], w, { x0: 66, padTop: 20 }, k);

function IvxWorkbook({ startNo = 1 }) {
  const W = IVX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="intervals">{content}</WbPage>);
  const nm = (p) => ivxEn(p.b.d - p.a.d + 1);

  // 2 (faces "Counting an interval")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Count it" how="Count the lines and spaces from the lower note to the higher; the lower note is 1. Write the number. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.try2.map((p, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{ivxPaper('treble', [{ ...p, ladder: i === 0 }])}{ivxAns(i === 0, nm(p))}</>, '8px 4px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="On both staves" how="Write the number of each interval: one note after the other, or both together.">
      <BkGrid cols={2} gap="8px 14px">{W.turn2.map(([clef, p], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{ivxPaper(clef, [p])}{ivxAns(false)}</>, '8px 4px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play and count" how="Play each interval, counting the letters aloud. Tick each one you can play.">
      {sskRowN(9, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{ivxPaper('treble', W.play2, 420, { x0: 70, bars: true })}{ivxTicks(['counting aloud', 'just playing'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "2nd to 5th, in the hand")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Which interval?" how="C position: the thumb plays C. Write the interval of the two dotted keys. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try3.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{maxWidth:150,margin:'0 auto',width:'100%'}}><TnPKeys start="C" whites={5} w={30} h={100} dots={['w0', 'w' + w]} labels={{ w0: '1', ['w' + w]: String(w + 1) }}/></div>{ivxAns(i === 0, ivxEn(w + 1), 60)}</>, '10px 4px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the note above" how="Draw the note, a semibreve, on its line or space.">
      <BkGrid cols={2} gap="8px 14px">{W.turn3.map(([d, clef, n], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{ivxAboveTitle(d, n)}{ivxWriteStaff(d, clef)}</>, '4px 4px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play them in the hand" how="Play each together: thumb and finger 2, 3, 4, 5. Then in G position. Tick each one.">
      {sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{ivxPaper('treble', W.play3.map((p, i) => ({ ...p, lab: '1 and ' + (i + 2) })), 340, { x0: 64, labSize: 12.5 })}{ivxTicks(['C position', 'G position'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "6th, 7th and octave")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="6th, 7th or octave?" how="Write the number of each interval. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.try4.map((p, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{ivxPaper('treble', [{ ...p, ladder: i === 0 }])}{ivxAns(i === 0, nm(p))}</>, '8px 4px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the note above" how="Draw the note, a semibreve. Odd numbers: line to line, or space to space; even: line to space, or space to line.">
      <BkGrid cols={2} gap="8px 14px">{W.turn4.map(([d, clef, n], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{ivxAboveTitle(d, n)}{ivxWriteStaff(d, clef)}</>, '4px 4px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Octaves" how="Play each note with the one an octave above, together. Then find every C on the piano. Tick each one.">
      {sskRowN(9, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{ivxPaper('treble', W.play4, 340, { x0: 64 })}{ivxTicks(['the four octaves', 'every C'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Melodic and harmonic")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Melodic or harmonic?" how="Circle melodic or harmonic, then write the number. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.try5.map((p, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{ivxPaper('treble', [p], 190, { x0: 56, padTop: 22 })}{ivxCircle(['melodic', 'harmonic'], i === 0 ? (p.harm ? 'harmonic' : 'melodic') : null)}{ivxAns(i === 0, nm(p), 70, 28)}</>, '8px 4px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Make it harmonic" how="Write the same two notes together after the arrow: one above the other (a 2nd: side by side, touching, the lower note on the left).">
      <BkGrid cols={2} gap="8px 14px">{W.turn5.map(([clef, p], i) => <BkCell key={i} n={i + 5}>{sdyCol(<div style={{position:'relative'}}>{ivxPaper(clef, [p, { ...p, blank: true }], 240, { x0: 56 }, 1.25)}<span style={{position:'absolute',left:'60%',top:4,transform:'translateX(-50%)',fontSize:18,fontWeight:900,color:BK.muted,lineHeight:1}}>→</span></div>, '8px 4px 6px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Listen and say" how="Your teacher plays six intervals. Write m (melodic) or h (harmonic) for each, and say its number.">
      {sskRowN(9, <div style={{display:'flex',justifyContent:'center',gap:16}}>{[1, 2, 3, 4, 5, 6].map(i => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>{bkBox(64, 56)}<span style={{fontSize:11,fontWeight:800,color:BK.muted}}>{i}</span></div>)}</div>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Above the tonic")
  const g = ivxScale('G');
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Above the tonic (G major)" how="With G major’s key signature (F♯). Write major or perfect, and the number. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.try6.map((n, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{ivxPaper('treble', [{ a: g[0], b: g[n - 1], harm: true }], 132, { x0: 50, padTop: 22, key: 'G' })}{ivxAns(i === 0, ivxQ(IVX_MP[n]) + ' ' + ivxEn(n), 112, 30)}</>, '8px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the note above the tonic" how="Draw the note. Add a sharp or flat only if that note has one in the key (D major: F♯ and C♯; F major: B♭).">
      <BkGrid cols={2} gap="8px 14px">{W.turn6.map(([k, n], i) => { const sc = ivxScale(k); return <BkCell key={i} n={i + 5}>{sdyCol(<><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginTop:4}}>{sscSx(prettyNote(k) + ' major: a ' + ivxQ(IVX_MP[n]) + ' ' + ivxEn(n) + ' above ' + ivxNoteTxt(sc[0]))}</div>{ivxPaper('treble', [{ a: sc[0], b: sc[0], harm: true, onlyA: true }], 180, { x0: 66, padTop: 26 }, 1.2)}</>, '4px 4px 4px')}</BkCell>; })}</BkGrid>
    </Part>
    <Part kind="play" title="The ladder" how="Play the tonic with each note of the scale above it, together, saying major or perfect. Tick each key.">
      {sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{ivxPaper('treble', ivxLadder('G', false).map(p => ({ ...p, lab: null })), 400, { x0: 60, key: 'G' })}{ivxTicks(['G major', 'C major', 'D major', 'F major'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 7. any key: the teacher writes the key; 8. the check-up on paper
  P(<IvxAnyKeyPage/>);
  P(<IvxPaperCheck/>);
  return <>{pages}</>;
}
function IvxAnyKeyPage() {
  return <>
    <WbTop step={7}/>
    {pbKeysHead()}
    <Part kind="together" title="Its scale" how={<span style={{textWrap:'pretty'}}>Write the key’s scale, going up from the tonic: eight notes, each with its sharp or flat.</span>}>
      {sskRowN(1, pbBoxes(8, 50, 44, null, 10))}
    </Part>
    <Part kind="home" title="The ladder" how={<span style={{textWrap:'pretty'}}>Write the tonic in each bar, and the note above it: a 2nd, a 3rd, up to the octave. Then write major or perfect under each.</span>}>
      {sskRowN(2, <div style={{width:'100%',maxWidth:640,margin:'0 auto'}}><SfStaff clef="treble" width={620} pad={[44, 70]} extra={(yOf, layer) => layer !== 'over' ? null : <g>{[1, 2, 3, 4, 5, 6].map(i => <line key={i} x1={60 + i * 79.5} x2={60 + i * 79.5} y1={yOf(38)} y2={yOf(30)} stroke={BK.ink} strokeWidth="1.3"/>)}<line x1={614} x2={614} y1={yOf(38)} y2={yOf(30)} stroke={BK.ink} strokeWidth="1.3"/>
        {['2nd', '3rd', '4th', '5th', '6th', '7th', '8ve'].map((w, i) => <text key={w} x={60 + (i + 0.5) * 79.5} y={yOf(38) - 16} textAnchor="middle" fontSize="13" fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{w}</text>)}
        {[0, 1, 2, 3, 4, 5, 6].map(i => <rect key={'bx' + i} x={60 + i * 79.5 + 5} y={yOf(30) + 32} width={69.5} height={30} rx="4" fill="#fff" stroke={BK.line} strokeWidth="1.3"/>)}</g>}/></div>)}
    </Part>
    <Part kind="play" title="Play the ladder" how="Fill the circles on the scale’s eight keys. Play the tonic with each note above it, together, saying the intervals. Tick each time.">
      {sskRowN(3, <div style={{maxWidth:620,margin:'0 auto',width:'100%'}}><TnPKeys start="C" whites={14} w={37} h={130} slots wslots/></div>)}
      <div style={{marginTop:8}}>{ivxTicks(['saying them', 'eyes closed'])}</div>
    </Part>
    <Part kind="year" title="My twelve keys"><div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',gap:'8px 10px'}}>{FIFTHS.map(k => <div key={k} style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,border:'1.2px solid ' + BK.line,borderRadius:8,padding:'6px 4px',fontFamily:'Inter, sans-serif',fontSize:16,fontWeight:900,color:BK.ink}}>{prettyNote(k)}{bkBox(20, 20)}</div>)}</div>
      <div style={{fontSize:12.5,color:BK.muted,marginTop:6}}>Tick a key when you can play its ladder and name every interval. Keep this on your first copy.</div></Part>
    <Faces/>
  </>;
}
function IvxPaperCheck() {
  const C = IVX_CHK, { nB, nC, nD } = ivxChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the number of each interval.')}
    <BkGrid cols={2} gap="6px 10px">{C.num.map(([clef, p], i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{ivxPaper(clef, [p], 200, { x0: 56 }, 1.2)}{ivxAns(false, '', 64, 28)}</>, '6px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Draw the note above, a semibreve.')}
    <BkGrid cols={3} gap="6px 8px">{C.above.map(([d, clef, n], i) => <BkCell key={i} n={nB + i}>{sdyCol(<>{ivxAboveTitle(d, n)}{ivxWriteStaff(d, clef, 150, 1.4)}</>, '4px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Circle melodic or harmonic.')}
    <BkGrid cols={2} gap="6px 10px">{C.mh.map(([clef, p], i) => <BkCell key={i} n={nC + i}>{sdyCol(<>{ivxPaper(clef, [p], 200, { x0: 56 }, 1.15)}{ivxCircle(['melodic', 'harmonic'])}</>, '6px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Name each interval above the tonic: major or perfect, and its number.')}
    <BkGrid cols={3} gap="6px 8px">{C.tonic.map(([k, n], i) => { const sc = ivxScale(k); return <BkCell key={i} n={nD + i}>{sdyCol(<><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginTop:4}}>{sscSx(prettyNote(k) + ' major')}</div>{ivxPaper('treble', [{ a: sc[0], b: sc[n - 1], harm: true }], 150, { x0: 56, key: k }, 1.45)}{ivxAns(false, '', 120, 28)}</>, '4px 2px 4px')}</BkCell>; })}</BkGrid>
  </div>;
}

function IvxTeacher() {
  const W = IVX_WB, C = IVX_CHK, pages = [], { nB, nC, nD, total } = ivxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="intervals" teacher>{content}</WbPage>);
  const num = (p) => ivxEn(p.b.d - p.a.d + 1), nmA = (d, n) => dName(d + n - 1);
  const ab = (k, n) => { const sc = ivxScale(k); return ivxNoteTxt(sc[n - 1]); };
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('intervals')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{sscSx('Intervals (chapter ' + bkChapterNo('reading-steps') + ': steps and skips; chapter ' + bkChapterNo('scales') + ': the major scale and its degrees). AMEB Music Craft: Grade 1, every interval by number; Grade 2, major and minor 2nds, 3rds, 6ths and 7ths; perfect unisons, 4ths, 5ths and octaves (Preliminary: 3rds, 4ths, 5ths and octaves by number). ABRSM Theory: Grade 1, the number above the tonic (C, G, D and F major); Grade 3, number and type. The interval ladder: Lesson Book page 1 and the end of the screen lesson (in the student’s keys, with major and perfect). Not here: minor intervals (chapter ' + bkChapterNo('chords') + '’s thirds), augmented and diminished, inversions, compound intervals (the toolbox).')}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12.5,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>Counting.</b> The lower note is 1; count every letter (every line and space) up to the higher note. Odd numbers: line to line or space to space; even numbers: line to space, or space to line. In a five-finger position the finger number is the interval (thumb and finger 3: a 3rd).</div>
    <TcBlock page={2} title="Counting an interval" answers={<>{sscLesson('Play C then E; the child counts C D E aloud and says a 3rd. Then G up to C.')}{skgTcAns('TRY IT', W.try2.map((p, i) => num(p) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn2.map(([, p]) => num(p)), 5)}</>}
      watch="Starting the count at 0 (C to E called a 2nd). Counting only the lines, or only the spaces. A falling interval given another number (E down to C is still a 3rd). On the bass staff, the notes read as if treble."
      say="“The bottom note is 1.”"/>
    <TcBlock page={3} title="2nd to 5th, in the hand" answers={<>{sscLesson('Right hand in C position: thumb with each finger, together; the child names each one. Then G position.')}{skgTcAns('TRY IT', W.try3.map((w, i) => ivxEn(w + 1) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn3.map(([d, , n]) => nmA(d, n)), 5)}</>}
      watch="Fingers 1 and 3 called a 2nd (counting the steps, not the notes). The 4th written line to line."
      say="“Thumb and finger 5: a 5th.”"/>
    <TcBlock page={4} title="6th, 7th and octave" answers={<>{sscLesson('C with A, B and C above; the child names them, then plays every C on the piano.')}{skgTcAns('TRY IT', W.try4.map((p, i) => num(p) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn4.map(([d, , n]) => nmA(d, n)), 5)}</>}
      watch="The octave called a 7th or a 9th. A 6th written line to line (6 is even: line to space, or space to line)."
      say="“Same letter, count to 8: an octave.”"/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 count it · 2 together too · 3 in C or G position · 4 write it (place the note, then Check) · 5 melodic or harmonic · 6 the bass staff · 7 listening: 2nd, 3rd, 5th or octave (screen only) · 8 above the tonic, in the student’s keys · 9 extra: major or perfect.</div>
  </>);
  P(<>
    <TcBlock page={5} title="Melodic and harmonic" answers={<>{sscLesson('Play C–E one after the other, then together; the child says melodic or harmonic. Then six for PLAY, mixed, e.g. C–E together, C–G apart, D–E together, F–A apart, G–B together, E–C apart (falling).')}{skgTcAns('TRY IT', W.try5.map((p, i) => (p.harm ? 'harmonic ' : 'melodic ') + num(p) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn5.map(([, p]) => dName(p.a.d) + ' and ' + dName(p.b.d) + ' together' + (p.b.d - p.a.d === 1 ? ', touching (' + dName(p.a.d) + ' on the left)' : '')), 5)}</>}
      watch="A harmonic 2nd drawn with one note on top of the other (they sit side by side, touching)."
      say="“Melodic: one after the other. Harmonic: together.”"/>
    <TcBlock page={6} title="Above the tonic" answers={<>{sscLesson('G with each note of G major above it, together; the child says major or perfect and the number. Then C, D and F major.')}{skgTcAns('TRY IT', W.try6.map((n, i) => ivxQ(IVX_MP[n]) + ' ' + ivxEn(n) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.turn6.map(([k, n]) => ab(k, n)), 5)}</>}
      watch="The key’s sharp or flat left out (D major’s 3rd is F♯), or one added where the key has none (F major’s 7th is E, not E♭). A 4th or 5th called major."
      say="“From the tonic: 2, 3, 6, 7 major; 4, 5, 8 perfect.”"/>
    <TcBlock page={7} title="Any key (photocopy it for each new key)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>For whichever key you write at the top (set in Log lesson › For the student › Keys). Its scale: the Scale finder (toolbox). The ladder: the tonic with the 2nd to the 8ve of its scale; from the tonic of any major key the 2nd, 3rd, 6th and 7th are major and the 4th, 5th and octave perfect. F♯ and C♯ major show as G♭ and D♭ (the same keys).</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook’s last page)" answers={<>
      {skgTcAns('A', C.num.map(([, p]) => num(p)))}
      {skgTcAns('B', C.above.map(([d, , n]) => nmA(d, n)), nB)}
      {skgTcAns('C', C.mh.map(([, p]) => p.harm ? 'harmonic' : 'melodic'), nC)}
      {skgTcAns('D', C.tonic.map(([k, n]) => ivxQ(IVX_MP[n]) + ' ' + ivxEn(n)), nD)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer: A {C.num.length}, B {C.above.length}, C {C.mh.length}, D {C.tonic.length}; {total} in all. D: both words for the mark; D shows the key signature, as exam papers do. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1, 3 and 4', page: '2, 4 and 5' }, { id: 'b', step: '2 and 3', page: '3 and 4' }, { id: 'c', step: '4', page: '5' }, { id: 'd', step: '5', page: '6' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: count an interval on the staff aloud. 2. Page 3: in C position, play a 2nd, 3rd, 4th and 5th and name them. 3. Page 4: show a 6th, a 7th and an octave on the staff and on the keys. 4. Page 5: point to a melodic and a harmonic interval, write one of each, play both. 5. Page 6: name each interval above the tonic of C, G, D and F major (number; major or perfect). Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['intervals'] = IvxWorkbook;
TEACHER_COPIES['intervals'] = IvxTeacher;
