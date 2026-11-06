// ─── Phase 467: chapter 10's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: soft and loud, pp to f, hairpins,
// legato and staccato, slur and tie; page 7 the check-up on paper) and its Teacher copy. English, like every Workbook.
// Staves about 4.5 to 5 mm between the lines; every task set (rule 3) and done alone (rule 4); a word to write is words
// to circle (rule 5); the signs themselves (p f pp mf, a hairpin, a dot, a curve) are written, as in a theory paper.
// No PLAY task copies its Lesson Book picture.
function SdyPaper({ items, clef = 'treble', o = {}, k = {}, mm = 4.5, label, extra }) {
  const vbw = sdyVbw(items, o, clef), px = vbw * mm / 5 * 1.89;
  return <div style={{width:'100%',maxWidth:px,minWidth:0,margin:'0 auto'}}><SdyStaff full clef={clef} items={items} o={o} k={k} label={label} extra={extra}/></div>;
}
const sdyBox = (w = 38, h = 38, txt, coral) => <span style={{display:'inline-flex',alignItems:'center',justifyContent:'center',width:w,height:h,border:'1.5px solid ' + (coral ? BK.coral : 'rgba(38,41,107,0.55)'),borderRadius:3,background:'#fff',color:BK.coral,fontFamily:SDY_FONT,fontStyle:'italic',fontWeight:900,fontSize:20}}>{txt}</span>;
const sdySign = (s, size = 34) => <div style={{textAlign:'center',lineHeight:1,padding:'2px 0'}}>{sdyBig(s, size, BK.ink)}</div>;
// words to circle, far enough apart to circle one cleanly; the worked example's ringed in coral
const sdyCircle = (words, on, small, gx) => <div style={{display:'flex',justifyContent:'center',flexWrap:'wrap',gap:'4px ' + (gx || (small ? 22 : 30)) + 'px',fontSize:small ? 13 : 14,fontWeight:800,color:BK.ink,marginTop:'auto',paddingTop:4}}>{words.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:'0 7px',color:on === w ? BK.coral : BK.ink,whiteSpace:'nowrap'}}>{w}</span>)}</div>;
// a cell's content: the picture at the top, the words to circle on its bottom line
const sdyCol = (kids, pad = '12px 2px 2px') => <div style={{display:'flex',flexDirection:'column',height:'100%',padding:pad,boxSizing:'border-box'}}>{kids}</div>;

// the Workbook's tasks, fixed so the Teacher copy always matches
const SDY_WB = {
  // p2: the meaning of p and f (the first done); the sign for a word; mark a tune and play it
  mean: ['p', 'f', 'f', 'p'],
  write: ['loud', 'soft', 'soft', 'loud'],
  pf: [['ts', 4], ...sdyQ([28, 29, 30, 29]), ['|'], ...sdyQ([32, 31]), ['h', 2, 30], ['||']],
  fp: [['ts', 3], ...sdyQ([32, 30, 31]), ['|'], ...sdyQ([29, 30, 28]), ['|'], ['hd', 3, 28], ['||']],
  // p3: number from the softest (pp done); the louder of two; the signs getting softer under a new tune
  order1: ['mf', 'pp', 'f', 'p'], order2: ['f', 'p', 'pp', 'mf'],
  louder: [['p', 'mf'], ['f', 'pp'], ['mf', 'f'], ['pp', 'p']],
  softer: [['ts', 2], ...sdyQ([32, 30]), ['|'], ...sdyQ([31, 29]), ['|'], ...sdyQ([30, 28]), ['|'], ['h', 2, 28], ['||']],
  louder8: [['ts', 4], ...sdyQ([28, 29, 30, 28]), ['|'], ...sdyQ([29, 30, 31, 29]), ['|'], ...sdyQ([30, 31, 32, 30]), ['|'], ['w', 4, 32], ['||']],
  // p4: what a hairpin means (the first done); draw it between two signs; write p or f to fit the hairpins
  hairs: ['cresc', 'dim', 'dim', 'cresc'],
  draw: [{ items: [['ts', 4], ...sdyQ([28, 29, 30, 31]), ['|'], ['w', 4, 32], ['||']], k: { dyn: [[0, 'p'], [4, 'f']], hairBox: [[0, 3]] }, dir: 'cresc' },
    { items: [['ts', 3], ...sdyQ([32, 31, 30]), ['|'], ...sdyQ([29, 30, 29]), ['|'], ['hd', 3, 28], ['||']], k: { dyn: [[0, 'f'], [6, 'p']], hairBox: [[0, 5]] }, dir: 'dim' }],
  fit: { items: [['ts', 4], ...sdyQ([28, 30, 29, 31]), ['|'], ...sdyQ([32, 30, 31, 29]), ['|'], ['w', 4, 28], ['||']], k: { dynBox: [0, 4, 8], hair: [[0, 3, 'dim'], [4, 7, 'cresc']] }, ans: ['f', 'p', 'f'] },
  // p5: legato or staccato (the first done); add the dots; find the staccato notes and play
  touch: [['legato', [28, 29, 30, 31]], ['staccato', [32, 31, 30, 29]], ['staccato', [28, 30, 32, 30]], ['legato', [30, 29, 28, 29]]],
  dots: [['ts', 4], ...sdyQ([28, 30, 29, 31]), ['|'], ...sdyQ([32, 30, 31, 29]), ['||']],
  read5: { items: [['ts', 4], ...sdyQ([32, 31, 30, 29]), ['|'], ...sdyQ([28, 30]), ['h', 2, 28], ['||']], k: { slurs: [[0, 3]], stacc: [4, 5] } },
  // p6: tie or slur (the first done); circle, then draw the curve; count a tie and play
  curves: [[30, 30, 'tie'], [29, 31, 'slur'], [32, 31, 'slur'], [28, 28, 'tie']],
  drawC: [[31, 31], [28, 30], [32, 32], [30, 29]],
  read6: { items: [['ts', 4], ['h', 2, 28], ['h', 2, 30], ['|'], ['h', 2, 30], ['h', 2, 29], ['|'], ['w', 4, 28], ['||']], k: { ties: [[1, 2]], slurs: [[3, 4]], dynBox: [1] } },
  read6b: { items: [['ts', 3], ['q', 1, 30], ['h', 2, 32], ['|'], ['hd', 3, 32], ['|'], ...sdyQ([31, 30, 29]), ['|'], ['hd', 3, 28], ['||']], k: { ties: [[1, 2]], slurs: [[3, 6]], dynBox: [1] } },
};
const SDY_CHK = {
  order: ['f', 'pp', 'mf', 'p'],
  mean: [['p', ['soft', 'loud']], ['mf', ['medium loud', 'loud']], ['f', ['soft', 'loud']], ['pp', ['very soft', 'soft']]],
  hair: [['pin', 'dim'], ['word', 'cresc.'], ['pin', 'cresc'], ['word', 'decresc.']],
  touch: [['staccato', [29, 31, 30, 28]], ['legato', [32, 30, 31, 29]]],
  curves: [[29, 30, 'slur'], [31, 31, 'tie'], [32, 32, 'tie'], [30, 28, 'slur']],
  drawHair: { items: [['ts', 4], ...sdyQ([28, 29, 30, 31]), ['|'], ['w', 4, 32], ['||']], k: { dyn: [[0, 'p'], [4, 'f']], hairBox: [[0, 3]] } },
  dots: [['ts', 2], ...sdyQ([30, 32]), ['sp', 10], ['||']],
};
const SDY_MEANS = { p: 'soft', f: 'loud', pp: 'very soft', mf: 'medium loud' };
const sdyRank = (s) => SDY_SIX.indexOf(s);
const sdyOrderOf = (list) => list.map(s => 1 + list.slice().sort((a, b) => sdyRank(a) - sdyRank(b)).indexOf(s));
// a bar of four crotchets with a slur or staccato dots; a pair across a bar line with a curve (or none, to draw)
const sdyTouchBar = (kind, ds, mm = 3.8) => <SdyPaper mm={mm} items={[...sdyQ(ds), ['sp', 14], ['||']]} o={{ D: 20, x0: 44 }} k={kind === 'legato' ? { slurs: [[0, 3]] } : kind === 'staccato' ? { stacc: [0, 1, 2, 3] } : {}}/>;
const sdyCurvePair = (a, b, kind, mm = 3.8) => <SdyPaper mm={mm} items={[['h', 2, a], ['|'], ['h', 2, b], ['sp', 10]]} o={{ D: 13, x0: 44 }} k={kind === 'tie' ? { ties: [[0, 1]] } : kind === 'slur' ? { slurs: [[0, 1]] } : {}}/>;
const sdyHow = (s) => sdyRich(s, '1.15em');

function SdyWorkbook({ startNo = 1 }) {
  const W = SDY_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="dynamics">{content}</WbPage>);

  // 2 (faces "Soft and loud")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="What does it mean?" how="Circle the meaning of each sign. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.mean.map((s, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{sdySign(s, 40)}{sdyCircle(['soft', 'loud'], i === 0 ? SDY_MEANS[s] : null)}</>)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the sign" how={sdyHow('Write p or f in each box.')}>
      <BkGrid cols={4} gap="8px 10px">{W.write.map((w, i) => <BkCell key={i} n={i + 5}><div style={{padding:'14px 2px 4px',display:'flex',flexDirection:'column',alignItems:'center',gap:6}}><span style={{fontSize:14,fontWeight:900,color:BK.ink}}>{w}</span>{sdyBox(42, 40)}</div></BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Mark it, then play it" how="Tune 9: write the sign for soft under bar 1 and the sign for loud under bar 2. Tune 10: loud for bars 1 and 2, soft for bar 3. Then right hand in C position: play each, at the same speed all through.">
      <div style={{display:'grid',gap:12}}>{sskRowN(9, <SdyPaper mm={5} items={W.pf} o={{ D: 26 }} k={{ dynBox: [0, 4] }}/>)}
        {sskRowN(10, <SdyPaper mm={5} items={W.fp} o={{ D: 26 }} k={{ dynBox: [0, 6] }}/>)}</div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "From pp to f")
  const order = (list, ex) => <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:'4px 16px',maxWidth:400,margin:'0 auto',justifyItems:'center'}}>
    {list.map((s, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4}}>{sdySign(s, 34)}{sdyBox(40, 38, ex && s === 'pp' ? '1' : null, ex && s === 'pp')}</div>)}</div>;
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Soft to loud" how={sdyHow('Number the signs from the softest (1) to the loudest (4). pp is done for you.')}>
      {sskRowN(1, order(W.order1, true))}
    </Part>
    <Part kind="home" title="Number them, then the louder one" how="Row 2: number them 1 to 4, softest first. Boxes 3 to 6: circle the louder sign.">
      <div style={{display:'grid',gap:10}}>{sskRowN(2, order(W.order2))}
        <BkGrid cols={4} gap="8px 10px">{W.louder.map((pr, i) => <BkCell key={i} n={i + 3}><div style={{padding:'14px 2px 6px',display:'flex',justifyContent:'center',gap:40}}>{pr.map(s => <span key={s}>{sdyBig(s, 32, BK.ink)}</span>)}</div></BkCell>)}</BkGrid></div>
    </Part>
    <Part kind="play" title="Mark it, then play it" how={sdyHow('Write pp, p, mf and f, one in each box. Tune 7: each bar a little softer than the one before. Tune 8: each bar a little louder. Then right hand in C position: play each.')}>
      <div style={{display:'grid',gap:12}}>{sskRowN(7, <SdyPaper mm={5} items={W.softer} o={{ D: 26 }} k={{ dynBox: [0, 2, 4, 6] }}/>)}
        {sskRowN(8, <SdyPaper mm={4.8} items={W.louder8} o={{ D: 20 }} k={{ dynBox: [0, 4, 8, 12] }}/>)}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Getting louder and softer")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Louder or softer?" how="Under each hairpin, circle louder or softer. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.hairs.map((d, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<><div style={{padding:'6px 4px 0'}}><BkHairpin kind={d} w={96}/></div>{sdyCircle(['louder', 'softer'], i === 0 ? (d === 'cresc' ? 'louder' : 'softer') : null, false, 14)}</>, '12px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the hairpin" how="In each dashed box, draw a hairpin: one that opens if the music gets louder, one that closes if it gets softer.">
      <div style={{display:'grid',gap:4}}>{W.draw.map((r, i) => sskRowN(i + 5, <SdyPaper mm={4.6} items={r.items} o={{ D: 26 }} k={r.k}/>))}</div>
    </Part>
    <Part kind="play" title="Mark it, then play it" how={sdyHow('Write p or f in each box to match the hairpins. Then right hand in C position: play it.')}>
      {sskRowN(7, <SdyPaper mm={4.8} items={W.fit.items} o={{ D: 22 }} k={W.fit.k}/>)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Legato and staccato")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Legato or staccato?" how="Circle legato or staccato for each bar. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.touch.map(([kind, ds], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{sdyTouchBar(kind, ds)}{sdyCircle(['legato', 'staccato'], i === 0 ? kind : null)}</>, '8px 4px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Add the dots" how="Make every note staccato: draw a dot under each note head, never on a line. The first one is done.">
      {sskRowN(5, <SdyPaper mm={5} items={W.dots} o={{ D: 26 }} k={{ stacc: [0], stacCol: PEN_C }}/>)}
    </Part>
    <Part kind="play" title="Find it, then play it" how="Circle the two staccato notes. Then right hand in C position: play it, smooth where there is a slur and short where there is a dot.">
      {sskRowN(6, <SdyPaper mm={5} items={W.read5.items} o={{ D: 26 }} k={W.read5.k}/>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Slur and tie")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Tie or slur?" how="Look at the two notes: the same, or different? Circle tie or slur. The first one is done.">
      <BkGrid cols={4} gap="8px 10px">{W.curves.map(([a, b, kind], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{sdyCurvePair(a, b, kind, 3.6)}{sdyCircle(['tie', 'slur'], i === 0 ? kind : null)}</>, '10px 2px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Circle it, then draw it" how="Circle tie or slur. Then draw the curve under the two note heads.">
      <BkGrid cols={4} gap="8px 10px">{W.drawC.map(([a, b], i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{sdyCurvePair(a, b, null, 3.8)}<div style={{height:10}}/>{sdyCircle(['tie', 'slur'])}</>, '10px 2px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="In each box, write how many beats you hold the tied note. Circle each slur. Then right hand in C position: play each, counting the beats out loud.">
      <div style={{display:'grid',gap:4}}>{[W.read6, W.read6b].map((r, i) => sskRowN(9 + i, <SdyPaper mm={4.1} items={r.items} o={{ D: 20 }} k={r.k}
        extra={(yOf, txt, mm, mk) => <text x={mm.notes[r.k.dynBox[0]].x + 24} y={mk.ry - 2} fontSize="12" fontWeight="800" fill={BK.ink} style={txt}>beats</text>}/>))}</div>
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<SdyPaperCheck/>);
  return <>{pages}</>;
}
function SdyPaperCheck() {
  const C = SDY_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Number the signs from the softest (1) to the loudest (4).')}
    <BkCell n={1}><div style={{padding:'10px 4px 4px',display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:'4px 16px',maxWidth:380,margin:'0 auto',justifyItems:'center'}}>
      {C.order.map((s, i) => <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4}}>{sdySign(s, 28)}{sdyBox(38, 36)}</div>)}</div></BkCell>
    {bkSec('B', 'Circle the meaning.')}
    <BkGrid cols={4} gap="6px 8px">{C.mean.map(([s, ws], i) => <BkCell key={i} n={i + 2}>{sdyCol(<>{sdySign(s, 30)}<div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:8,marginTop:'auto',paddingTop:4,fontSize:13,fontWeight:800,color:BK.ink}}>{ws.map(w => <span key={w} style={{whiteSpace:'nowrap'}}>{w}</span>)}</div></>, '10px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('C', 'Circle louder or softer.')}
    <BkGrid cols={4} gap="6px 8px">{C.hair.map(([kind, v], i) => <BkCell key={i} n={i + 6}>{sdyCol(<>{kind === 'pin' ? <div style={{padding:'4px 4px 0'}}><BkHairpin kind={v} w={84}/></div> : <div style={{textAlign:'center',fontFamily:SDY_FONT,fontStyle:'italic',fontSize:24,color:BK.ink,lineHeight:'30px'}}>{v}</div>}{sdyCircle(['louder', 'softer'], null, true, 12)}</>, '12px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Circle legato or staccato.')}
    <BkGrid cols={2} gap="6px 10px">{C.touch.map(([kind, ds], i) => <BkCell key={i} n={i + 10}>{sdyCol(<>{sdyTouchBar(kind, ds, 3.4)}{sdyCircle(['legato', 'staccato'], null, true)}</>, '8px 4px 4px')}</BkCell>)}</BkGrid>
    {bkSec('E', 'Circle tie or slur.')}
    <BkGrid cols={4} gap="6px 8px">{C.curves.map(([a, b, kind], i) => <BkCell key={i} n={i + 12}>{sdyCol(<>{sdyCurvePair(a, b, kind, 3.2)}{sdyCircle(['tie', 'slur'], null, true)}</>, '8px 0 4px')}</BkCell>)}</BkGrid>
    {bkSec('F', 'Write it.')}
    <div style={{display:'grid',gridTemplateColumns:'1.5fr 1fr 1fr',gap:'6px 8px'}}>
      <BkCell n={16}>{sdyCol(<><div style={{fontSize:12.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>Draw the hairpin.</div><SdyPaper mm={3.3} items={C.drawHair.items} o={{ D: 22 }} k={C.drawHair.k}/></>, '15px 2px 2px')}</BkCell>
      <BkCell n={17}>{sdyCol(<><div style={{fontSize:12.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>Add staccato dots.</div><SdyPaper mm={3.5} items={C.dots} o={{ D: 26 }}/></>, '15px 2px 2px')}</BkCell>
      <BkCell n={18}>{sdyCol(<><div style={{fontSize:12.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>The sign for very soft:</div><div style={{display:'flex',justifyContent:'center',marginTop:'auto',paddingBottom:6}}>{sdyBox(48, 44)}</div></>, '15px 2px 2px')}</BkCell>
    </div>
  </div>;
}

const sdyLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{sdyRich(txt)}</div>;
function SdyTeacher() {
  const W = SDY_WB, C = SDY_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="dynamics" teacher>{content}</WbPage>);
  const louder = (pr) => sdyRank(pr[0]) > sdyRank(pr[1]) ? pr[0] : pr[1];
  const hw = (d) => d === 'cresc' ? 'louder' : 'softer';
  const touchAns = (list) => list.map(([k]) => k);
  const nm = (d) => dName(d);
  const marks = { B: C.mean.length, C: C.hair.length, D: C.touch.length, E: C.curves.length, F: 3 };
  const R = (s) => sdyRich(s);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('dynamics')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{R('Each Workbook page faces its Lesson Book page. Every tune is right hand in C position (chapter ' + bkChapterNo('reading-steps') + '). Dynamics: p and f, then pp p mf f; the hairpins (crescendo, cresc.; diminuendo, dim., also decrescendo, decresc.). Articulation: legato and staccato; the slur is legato’s sign, set beside chapter ' + bkChapterNo('time-signatures') + '’s tie; a slur ends with a small lift. Unmarked notes are played the way the child already plays: joined. Not yet: mp and ff (drill level 9, AMEB Grade 1); accent, tenuto, the fermata and the pedals (later rooms). Drill: levels 1 and 2 after page 3, 3 after page 4, 4 and 5 after page 6, 6 to 8 by ear; level 9 is extra.')}</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: loud is weight, not speed.</b> {R('Play one tune p, then f, keeping the pulse: the arm’s weight changes, the speed does not. Then a crescendo on five notes, a little more weight on each.')}</div>
    <TcBlock page={2} title="Soft and loud" answers={<>{sdyLesson('Play a note p and then f; the child copies. Then the child plays and the teacher, eyes shut, says p or f.')}{tcAns('TRY IT', W.mean.map(s => SDY_MEANS[s]))}{tcAns('YOUR TURN', W.write.map(w => w === 'loud' ? 'f' : 'p'), 5)}{tcAns('PLAY', ['p under bar 1, f under bar 2', 'f under bar 1, p under bar 3'], 9)}</>}
      watch={R('Getting faster when loud, slower when soft. f from a stiff wrist or caving fingertip joints, not arm weight. p so soft that notes do not sound. The sign written over the staff.')}
      say={R('“p soft, f loud: the same speed.”')}/>
    <TcBlock page={3} title="From pp to f" answers={<>{sdyLesson('Four steps of loudness: the child plays one C E G at each, and the teacher names the sign. Then the teacher plays one, and the child names it.')}{tcAns('TRY IT', [sdyOrderOf(W.order1).join(' ')], 1)}{tcAns('YOUR TURN', [sdyOrderOf(W.order2).join(' '), ...W.louder.map(louder)], 2)}{tcAns('PLAY', ['f mf p pp', 'pp p mf f'], 7)}</>}
      watch={R('pp and p played the same. mf heard as “medium soft”: it is medium loud. mf read as louder than f. Letters written upright or as capitals: dynamics are small italic letters.')}
      say="“m means medium. The same letter twice means very.”"/>
    <TcBlock page={4} title="Getting louder and softer" answers={<>{sdyLesson('Five notes up, a crescendo; five notes down, a diminuendo. The loudness grows a little on every note, not all at once at the end.')}{tcAns('TRY IT', W.hairs.map(hw))}{tcAns('YOUR TURN', W.draw.map(r => r.dir === 'cresc' ? 'opening (crescendo)' : 'closing (diminuendo)'), 5)}{tcAns('PLAY', [W.fit.ans.join(' ')], 7)}</>}
      watch="The whole crescendo saved for the last note. A hairpin read as an accent. Opening and closing mixed up: the open end is the loud end. Speeding up through a crescendo, slowing down through a diminuendo."
      say="“Opening: louder. Closing: softer.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Legato and staccato" answers={<>{sdyLesson('Legato: one finger comes up as the next goes down, no gap and no blur. Staccato: a light bounce from the wrist, the key let go straight away; the note is short, not loud.')}{tcAns('TRY IT', touchAns(W.touch))}{tcAns('YOUR TURN', ['a dot under every note head'], 5)}{tcAns('PLAY', ['notes ' + W.read5.k.stacc.map(j => j + 1).join(' and ') + ' (' + W.read5.k.stacc.map(j => nm(sskNotesOf(W.read5.items)[j].d)).join(', ') + ')'], 6)}</>}
      watch="Legato gaps: the hand lifting between notes, or fingers 4 and 5 coming up early. Legato with two keys held down together (blurred). Staccato jabbed from the elbow, the hand flying up, or played loud. Dots drawn on the stem side or on a line. The note without a dot after staccato notes cut short too."
      say="“Legato joins. Staccato bounces.”"/>
    <TcBlock page={6} title="Slur and tie" answers={<>{sdyLesson('The same curve twice: over different notes, play them joined and lift after the last; between two of the same note, play once and hold. Ask the child to count a tied note out loud.')}{tcAns('TRY IT', W.curves.map(c => c[2]))}{tcAns('YOUR TURN', W.drawC.map(([a, b]) => a === b ? 'tie' : 'slur'), 5)}{tcAns('PLAY', ['4 beats (the tied E); the slur joins D to C', '5 beats (the tied G); the slur joins F E D C'], 9)}</>}
      watch="A tied note played twice. A slur read as a tie because the curve looks the same: look at the notes. Letting go too early at the end of a tie. No lift at the end of a slur. A tie drawn to a different note."
      say="“Different notes: a slur. The same note: a tie.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', [sdyOrderOf(C.order).join(' ')])}
      {tcAns('B', C.mean.map(([s]) => SDY_MEANS[s]), 2)}
      {tcAns('C', C.hair.map(([kind, v]) => kind === 'pin' ? hw(v) : v === 'cresc.' ? 'louder' : 'softer'), 6)}
      {tcAns('D', touchAns(C.touch), 10)}
      {tcAns('E', C.curves.map(c => c[2]), 12)}
      {tcAns('F', ['an opening hairpin', 'a dot under each head', 'pp'], 16)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Section A is one mark if all four numbers are right. One mark for each answer in B to F: A 1, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}, F {marks.F}; {1 + marks.B + marks.C + marks.D + marks.E + marks.F} in all. A section with any wrong answer is not passed yet: go back to its page below. The paper shows the reading; the playing is heard: also listen to the student play (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 2, page: 3 }, { id: 'b', step: '1\u2060–\u20602', page: '2\u2060–\u20603' }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }, { id: 'f', step: '2\u2060–\u20604', page: '3\u2060–\u20605' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> {R('1. Page 2: the tune p, then f, at the same speed. 2. Page 3: the four bars pp, p, mf, f, each a little louder. 3. Page 4: the tune with its hairpins, the loudness changing on every note. 4. Page 5: C D E F G legato, then C D E F staccato and G held. 5. Page 6: the slur smooth with a lift at its end; the tied G played once and held to the end of bar 2. Got it! means you can hear the difference without looking.')}</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['dynamics'] = SdyWorkbook;
TEACHER_COPIES['dynamics'] = SdyTeacher;
