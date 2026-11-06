// ─── Phase 471: chapter 16's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: the major scale; C major fingering;
// scale degrees; G major; F major; page 7 the check-up on paper) and its Teacher copy. English, like every Workbook.
// Every task set (rule 3) and done alone (rule 4); a word to write is words to circle (rule 5); no PLAY task repeats its
// Lesson Book page; nothing on a page gives away a task on the same page; the check-up repeats no practice item and asks
// nothing the practice pages did not; the sets' answers vary (rule 7).
// a pair of keys on a small keyboard (TnPKeys keys: 'w0' C ... 'w7' C, 'b3' F♯/G♭, 'b5' A♯/B♭), a dot on each (it shows
// in black and white too), words to circle under it
const sscPairCell = (you, ans, ex) => sdyCol(<><div style={{maxWidth:230,margin:'0 auto',width:'100%'}}><TnPKeys start="C" whites={8} w={28} h={80} you={you} dots={you}/></div>{sdyCircle(['whole', 'half'], ex ? ans : null, false, 30)}</>, '12px 6px 4px');
// the steps of a scale to circle: its eight names in even columns, under each gap 'whole' over 'half'
const sscStepsRow = (names) => <div style={{display:'grid',gridTemplateColumns:'repeat(16, minmax(0, 1fr))',alignItems:'center',width:'100%',maxWidth:600,margin:'0 auto'}}>
  {names.map((n, i) => <div key={'n' + i} style={{gridColumn:(2 * i + 1) + ' / span 2',gridRow:1,textAlign:'center',fontSize:20,fontWeight:900,color:BK.ink}}>{sscName(n)}</div>)}
  {names.slice(1).map((_, i) => <div key={'w' + i} style={{gridColumn:(2 * i + 2) + ' / span 2',gridRow:2,display:'flex',flexDirection:'column',alignItems:'center',gap:6,fontSize:14,fontWeight:800,color:BK.ink,lineHeight:1.1,paddingTop:4}}>
    <span>whole</span><span>half</span></div>)}
</div>;
// four degrees to circle, in their own labelled row away from the notes; lo: the first of the four
const sscDegRow = (lo, small) => <div style={{display:'flex',alignItems:'center',justifyContent:small ? 'center' : 'flex-start',gap:small ? 18 : 26,marginTop:small ? 6 : 3,padding:small ? '2px 0 0' : '5px 0 0 10px',borderTop:small ? 'none' : '0.8px dashed rgba(38,41,107,0.3)'}}>
  {!small && <span style={{fontSize:10,fontWeight:900,letterSpacing:'0.12em',color:BK.muted}}>DEGREE</span>}
  {[0, 1, 2, 3].map(j => <span key={j} style={{fontSize:small ? 16 : 18,fontWeight:900,color:BK.ink,minWidth:14,textAlign:'center'}}>{lo + j}</span>)}</div>;
// C major up and down on the staff (15 notes), to play from, with a final bar line
const sscUpDown = (k) => { const d0 = SSC_D0[k], gap = 30, x0 = 74, ds = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0], w = x0 + 14 * gap + 40;
  return <SfStaff clef="treble" width={w} span={[4, w - 4]} pad={[12, 14]} notes={ds.map((i, j) => ({ d: d0 + i, x: x0 + j * gap, color: PEN_N }))}
    extra={(yOf, layer) => layer === 'over' && <g><line x1={w - 12} x2={w - 12} y1={yOf(38)} y2={yOf(30)} stroke={PEN_N} strokeWidth="1.2"/><line x1={w - 6} x2={w - 6} y1={yOf(38)} y2={yOf(30)} stroke={PEN_N} strokeWidth="3.6"/></g>}/>; };
// a line of degree numbers, a box under each for its letter, and a tick
const sscNumLine = (s) => <div key={s} style={{display:'flex',alignItems:'center',gap:10}}>{sprTick()}<div style={{display:'flex',gap:5}}>{s.split(' ').map((n, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3}}>
  <span style={{fontSize:19,fontWeight:900,color:BK.ink,lineHeight:1}}>{n}</span><span style={{width:34,height:36,border:'1.4px solid ' + BK.ink,borderRadius:3,background:'#fff'}}/></div>)}</div></div>;
const sscScaleNames = (k) => sscScale(k).map(s => s.name);   // eight names, the tonic at both ends
// the white keys from a letter to the same letter (to find where a major scale's pattern breaks)
const sscWhiteNames = (L) => Array.from({ length: 8 }, (_, i) => SSC_L[(SSC_L.indexOf(L) + i) % 7]);
// two octaves and a fifth of white keys, C to G, with two brackets over them: C to C and G to G, each with a box to tick
function SscTwoScales() {
  const w = 28, n = 12, W = n * w + 4, cx = (i) => 2 + (i + 0.5) * w;
  const br = (a, b, y, txt) => <g><path d={`M${cx(a) - 10} ${y + 6} L${cx(a) - 10} ${y} L${cx(b) + 10} ${y} L${cx(b) + 10} ${y + 6}`} fill="none" stroke={PEN_N} strokeWidth="1.6"/>
    <rect x={cx(a) - 10} y={y - 16} width="11" height="11" rx="1.5" fill="#fff" stroke={PEN_N} strokeWidth="1.2"/>
    <text x={cx(a) + 6} y={y - 7} fontSize="10.5" fontWeight="900" fill={PEN_N}>{txt}</text></g>;
  return <div style={{width:'100%'}}><svg viewBox={`0 0 ${W} 54`} style={{width:'100%',display:'block'}}>{br(0, 7, 22, 'C to C')}{br(4, 11, 48, 'G to G')}</svg>
    <TnPKeys start="C" whites={n} w={w} h={96} labels={Object.fromEntries(Array.from({ length: n }, (_, i) => ['w' + i, TN_WL[i % 7]]))}/></div>;
}

const SSC_WB = {
  pairs2: [[['w0', 'w1'], 'whole'], [['w2', 'w3'], 'half'], [['w6', 'w7'], 'half'], [['w4', 'w5'], 'whole']],
  num4: [2, 6, 3, 7],   // the degrees to number on C major's keys (the first, D, done)
  degs4: [['C', 4, 3], ['C', 2, 1], ['C', 6, 3], ['C', 1, 1], ['C', 7, 5], ['C', 5, 2]],   // [scale, degree, first choice]
  play4: ['1 4 6 8', '8 7 6 5', '2 4 6 7'],
  pairs5: [[['w2', 'b3'], 'whole'], [['b3', 'w4'], 'half'], [['w6', 'w7'], 'half'], [['w4', 'w5'], 'whole']],
  pairs6: [[['w5', 'b5'], 'half'], [['w4', 'w5'], 'whole'], [['b5', 'w7'], 'whole'], [['w2', 'w3'], 'half']],
};
const SSC_CHK = {
  pairs: [['A B', 'whole'], ['C♯ D', 'half'], ['G♯ A', 'half'], ['E♭ F', 'whole']],
  degs: [[32, 5, 4], [30, 3, 3], [33, 6, 4], [31, 4, 1]],   // C major, one note: [its place, its degree, first choice]
  part: [['G', [4, 7], 'G major, notes 5 to 8', true], ['F', [0, 3], 'F major, notes 1 to 4', false]],
  yes: [['F', 'F major', 'no'], ['C', 'C major', 'yes']],
};
const sscKeysBox = (start, hand, ex, mw = 540, H, hide) => <div style={{maxWidth:mw,margin:'0 auto',width:'100%'}}><SscKeys start={start} o={{ H, hideNames: hide, boxes: SCALES[start].octaves[1][hand].map((f, d) => ex && d === 0 ? f : ''), hand: hand === 'RH' ? 'RIGHT HAND' : 'LEFT HAND' }}/></div>;
const sscTicks = (ws) => <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{ws.map(w => sprTickW(w))}</div>;

function SscWorkbook({ startNo = 1 }) {
  const W = SSC_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales">{content}</WbPage>);

  // 2 (faces "The major scale")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Whole or half?" how="Circle whole or half for the two dotted keys. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.pairs2.map(([you, ans], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sscPairCell(you, ans, i === 0)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="The steps" how="Under each two notes, circle whole or half: C to C, then G to G on the white keys.">
      <div style={{display:'grid',gap:10}}>{sskRowN(5, sscStepsRow(sscScaleNames('C')))}
        {sskRowN(6, sscStepsRow(sscWhiteNames('G')))}</div>
    </Part>
    <Part kind="play" title="Which one is major?" how="Play the white keys C to C, then G to G, slowly. Tick the one that sounds like a major scale.">
      {sskRowN(7, <div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><SscTwoScales/></div>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "C major fingering")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Right-hand fingers" how="Write the right hand’s finger for each note of C major, going up. The first one is done.">
      {sskRowN(1, sscKeysBox('C', 'RH', true, 540, 126))}
    </Part>
    <Part kind="home" title="Left-hand fingers" how="Write the left hand’s finger for each note of C major, going up.">
      {sskRowN(2, sscKeysBox('C', 'LH', false, 540, 126))}
    </Part>
    <Part kind="play" title="Play it, each hand" how="Play this, C major up and down, with the fingers you wrote; the left hand an octave lower. Tick each one.">
      {sskRowN(3, <div style={{display:'flex',flexDirection:'column',gap:8,width:'100%'}}><div style={{maxWidth:560,margin:'0 auto',width:'100%'}}>{sscUpDown('C')}</div>
        {sscTicks(['right hand', 'left hand', 'right hand, eyes closed'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Scale degrees")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Number the keys" how="C major: write the degree of each key with a box over it. The first one is done.">
      {sskRowN(1, <div style={{maxWidth:420,margin:'0 auto',width:'100%'}}><SscKeys start="C" o={{ boxes: Array.from({ length: 8 }, (_, d) => W.num4.includes(d + 1) ? (d + 1 === W.num4[0] ? String(d + 1) : '') : undefined) }}/></div>)}
    </Part>
    <Part kind="home" title="Which degree?" how="Circle the coral note’s degree.">
      <BkGrid cols={2} gap="8px 14px">{W.degs4.map(([k, d, lo], i) => <BkCell key={i} n={i + 2}>{sdyCol(<><SscStaff start={k} o={{ lit: d - 1, gap: 32 }}/>{sscDegRow(lo)}</>, '4px 4px 2px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play the numbers" how="C major: write each number’s letter. Then play the line, saying the numbers. Tick it.">
      {sskRowN(8, <div style={{display:'flex',justifyContent:'space-around',gap:12,flexWrap:'wrap'}}>{W.play4.map(w => sscNumLine(w))}</div>)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "G major")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Whole or half? (G major)" how="Circle whole or half for the two dotted keys. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.pairs5.map(([you, ans], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sscPairCell(you, ans, i === 0)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="G major’s keys" how="Put a dot on each of G major’s eight keys, G to G.">
      {sskRowN(5, <div style={{maxWidth:600,margin:'0 auto',width:'100%'}}><TnPKeys start="F" whites={10} w={28} h={104} slots/></div>)}
    </Part>
    <Part kind="play" title="Draw it, play it" how="Draw G major’s sharp before its note. Play up and down: the right hand with these fingers; the left hand an octave lower, 5 4 3 2 1, 3 over, 3 2 1.">
      {sskRowN(6, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}><div style={{maxWidth:560,margin:'0 auto',width:'100%'}}><SscStaff start="G" o={{ gap: 40, noAcc: true, fingers: { RH: SCALES.G.octaves[1].RH } }}/></div>
        {sscTicks(['right hand', 'left hand'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "F major")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Whole or half? (F major)" how="Circle whole or half for the two dotted keys. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.pairs6.map(([you, ans], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sscPairCell(you, ans, i === 0)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="F major’s right hand" how="Write the right hand’s finger for each note of F major, going up.">
      {sskRowN(5, sscKeysBox('F', 'RH', false, 520, 118, true))}
    </Part>
    <Part kind="play" title="Draw it, play it" how="Draw F major’s flat before its note. Play up and down: the right hand with the fingers you wrote in 5; the left hand an octave lower, as in C major.">
      {sskRowN(6, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}><div style={{maxWidth:560,margin:'0 auto',width:'100%'}}><SscStaff start="F" o={{ gap: 40, noAcc: true }}/></div>
        {sscTicks(['right hand', 'left hand'])}</div>)}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<SscPaperCheck/>);
  return <>{pages}</>;
}
function SscPaperCheck() {
  const C = SSC_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Whole or half? Circle one.')}
    <BkGrid cols={4} gap="6px 8px">{C.pairs.map(([pair], i) => <BkCell key={i} n={i + 1}>{sdyCol(<><div style={{textAlign:'center',fontSize:24,fontWeight:900,color:BK.ink,letterSpacing:'0.08em',padding:'6px 0 2px'}}>{sscSx(pair)}</div>{sdyCircle(['whole', 'half'], null, false, 16)}</>, '10px 4px 4px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Write the left hand’s fingers for G major, going up.')}
    <BkCell n={5}><div style={{padding:'6px 4px 2px'}}>{sscKeysBox('G', 'LH', false, 480, 142, true)}</div></BkCell>
    {bkSec('C', 'In C major, circle the note’s degree.')}
    <BkGrid cols={4} gap="6px 8px">{C.degs.map(([dd, d, lo], i) => <BkCell key={i} n={i + 6}>{sdyCol(<><div style={{maxWidth:150,margin:'0 auto',width:'100%'}}><SfStaff clef="treble" width={130} span={[4, 126]} pad={[20, 20]} notes={[{ d: dd, x: 96 }]}/></div>{sscDegRow(lo, true)}</>, '8px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Draw the sign each scale needs, just before its note.')}
    <BkGrid cols={2} gap="6px 10px">{C.part.map(([k, r, cap, low], i) => <BkCell key={k} n={i + 10}><div style={{padding:'8px 4px 2px'}}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{cap}</div><div style={{maxWidth:320,margin:'0 auto',width:'100%'}}><SscStaff start={k} o={{ noAcc: true, gap: 38, range: r, octDown: low, padTop: 26 }}/></div></div></BkCell>)}</BkGrid>
    {bkSec('E', 'Is it a major scale? Circle yes or no.')}
    <BkGrid cols={2} gap="6px 10px">{C.yes.map(([k, nm], i) => <BkCell key={i} n={i + 12}>{sdyCol(<><div style={{textAlign:'center',fontSize:18,fontWeight:900,color:BK.ink,letterSpacing:'0.08em',padding:'12px 0 4px'}}>{sscWhiteNames(k).join(' ')}</div>
      <div style={{display:'flex',justifyContent:'center',alignItems:'baseline',gap:16,fontSize:14,fontWeight:800,color:BK.ink,paddingTop:4}}>{nm}?<span style={{display:'flex',gap:22,fontSize:15,fontWeight:900}}><span>yes</span><span>no</span></span></div></>, '14px 4px 16px')}</BkCell>)}</BkGrid>
  </div>;
}

const sscLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{txt}</div>;
function SscTeacher() {
  const W = SSC_WB, C = SSC_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales" teacher>{content}</WbPage>);
  const fing = (k, h) => SCALES[k].octaves[1][h].join(' ');
  const degName = (k, d) => sscNameTxt(sscScale(k)[d - 1].name);
  const letters = (l) => l.split(' ').map(n => SSC_L[(+n - 1) % 7]).join(' ');
  const marks = { A: C.pairs.length, B: 1, C: C.degs.length, D: C.part.length, E: C.yes.length };
  const total = Object.values(marks).reduce((a, b) => a + b, 0);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>The major scale on C, G and F (chapter {bkChapterNo('tones')}: half and whole steps, sharps and flats). One octave, hands separately. AMEB Piano technical work (the app’s Scale finder): C and G major and A harmonic minor at Preliminary; F major, E and D harmonic minor at Grade 1; B♭ major at Grade 2. Steps: whole and half (tone and semitone: T T S T T T S). Every letter once: F♯ not G♭, B♭ not A♯. Fingering: C and G, right hand {fing('C', 'RH')}, left hand {fing('C', 'LH')}; F, right hand {fing('F', 'RH')}, left hand {fing('F', 'LH')}. Degrees: 1 to 8, the tonic named. The drill comes after page 6; levels 8 and 9 (D and B♭ major, the harmonic minors) are extra.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: sing the steps.</b> Play C major slowly; the child sings or says whole or half at every step, then plays while you say them.</div>
    <TcBlock page={2} title="The major scale" answers={<>{sscLesson('Play each white pair from C to C; the child says whole or half. Then find E F and B C together in every octave.')}{tcAns('TRY IT', W.pairs2.map(p => p[1]))}{tcAns('YOUR TURN', [SSC_STEPS.join(', '), 'whole, whole, half, whole, whole, half, whole'], 5)}{tcAns('PLAY', ['C to C (G to G has F, not F♯)'], 7)}</>}
      watch="Half and whole mixed up where a black key sits between (C D, F G). E F and B C taken for whole steps. A scale started on the wrong C or stopped on B."
      say="“A major scale: whole, whole, half, whole, whole, whole, half.”"/>
    <TcBlock page={3} title="C major fingering" answers={<>{sscLesson('Practise the thumb under slowly on its own: E then F with the right hand (3 then 1); the left hand’s 3 over: G then A (1 then 3).')}{tcAns('TRY IT', [fing('C', 'RH')])}{tcAns('YOUR TURN', [fing('C', 'LH')], 2)}{tcAns('PLAY', ['each hand, up and down; the left hand an octave lower'], 3)}</>}
      watch="The thumb tucked under too late, with a bump or a jump. The wrist twisting at the crossing. The left hand starting on 1. Uneven sound at the crossing."
      say="“Right hand up: 1 2 3, thumb under, 1 2 3 4 5. Left hand up: 5 4 3 2 1, 3 over, 3 2 1.”"/>
    <TcBlock page={4} title="Scale degrees" answers={<>{sscLesson('Play a scale note and ask its number; then ask for a number and the child plays it. Always come home to the tonic.')}{tcAns('TRY IT', [[...W.num4].sort((a, b) => a - b).map(d => sscNameTxt(sscScale('C')[d - 1].name) + ' ' + d).join(', ')])}{tcAns('YOUR TURN', W.degs4.map(([k, d]) => d + ' (' + degName(k, d) + ')'), 2)}{tcAns('PLAY', [W.play4.map(letters).join(', ')], 8)}</>}
      watch="Degrees counted from 0, or from the top. The 8 not recognised as the tonic again. A degree taken for a finger number."
      say="“Degrees 1 to 8. Degree 1, the tonic, is home.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="G major" answers={<>{sscLesson('Play G major on white keys only first: the child hears the wrong 7th. Then with F♯.')}{tcAns('TRY IT', W.pairs5.map(p => p[1]))}{tcAns('YOUR TURN', ['dots on G A B C D E F♯ G (F♯ the black key)'], 5)}{tcAns('PLAY', ['a sharp before F, on the top line (F♯, never G♭); each hand up and down'], 6)}</>}
      watch="F played instead of F♯. The sharp drawn on the wrong line or after the note. Right-hand finger 4 not on F♯. G♭ written for F♯."
      say="“G major: one sharp, F♯.”"/>
    <TcBlock page={6} title="F major" answers={<>{sscLesson('Play F major with B instead of B♭: hear the wrong 4th. Then the right hand’s 1 2 3 4, 1 2 3 4, slowly.')}{tcAns('TRY IT', W.pairs6.map(p => p[1]))}{tcAns('YOUR TURN', [fing('F', 'RH')], 5)}{tcAns('PLAY', ['a flat before B, on the middle line; each hand up and down'], 6)}</>}
      watch="B played instead of B♭. The right hand turning the thumb under after 3 (as in C) and landing the thumb on B♭. Coming down, 4 not crossing over to B♭."
      say="“F major: one flat, B♭. Right hand 1 2 3 4, 1 2 3 4.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.pairs.map(p => p[1]))}
      {tcAns('B', [fing('G', 'LH')], 5)}
      {tcAns('C', C.degs.map(([, d]) => d + ' (' + degName('C', d) + ')'), 6)}
      {tcAns('D', ['G major: a sharp before F, in the bottom space', 'F major: a flat before B, on the middle line'], 10)}
      {tcAns('E', C.yes.map(([k, , a]) => a + (a === 'no' ? ' (F major has B♭)' : '')), 12)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer; B is one mark if all eight fingers are right: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}; {total} in all. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1, 4 and 5', page: '2, 5 and 6' }, { id: 'b', step: '2 and 4', page: '3 and 5' }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: '4 and 5', page: '5 and 6' }, { id: 'e', step: '1, 4 and 5', page: '2, 5 and 6' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: the steps of a major scale, said in order. 2. Page 3: C major with each hand, the right fingering. 3. Page 4: the number of any note of C major; the tonic. 4. Page 5: G major with F♯, each hand. 5. Page 6: F major with B♭ and the right hand’s 1 2 3 4, 1 2 3 4. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS.scales = SscWorkbook;
TEACHER_COPIES.scales = SscTeacher;
