// ─── Phase 466: chapter 9's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: which way, step or skip, C position,
// G position, read a tune; page 7 the check-up on paper) and its Teacher copy. English, like every Workbook. Staves
// about 5 mm between the lines (Book rule 5); every task set (rule 3) and done alone (rule 4); a word to write is
// words to circle (rule 5).
// a staff at a set size: mm between the lines, never wider than its box
function SskPaper({ items, clef = 'treble', o = {}, mm = 5, label }) {
  const m = sskRaw((d) => dY(d), items, { ...o, clef }), vbw = Math.ceil(m.last + 6), px = vbw * mm / 5 * 1.89;
  return <div style={{width:'100%',maxWidth:px,minWidth:0,margin:'0 auto'}}><SskStaff full clef={clef} items={items} o={o} label={label}/></div>;
}
const sskQ = (ds) => ds.map(d => ['q', 1, d]);
const sskW = (ds) => ds.map(d => ['w', 4, d]);
const sskNum = (i) => <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink}}>{i}</span>;
const sskRowN = (n, kids) => <div key={n} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{sskNum(n)}{kids}</div>;
// the moves of a row, in order: +1 up, 0 the same, -1 down; and as words
const sskDirs = (items) => { const ns = sskNotesOf(items).map(x => x.d); return ns.slice(1).map((d, j) => Math.sign(d - ns[j])); };
const sskWords = (items) => { const ns = sskNotesOf(items).map(x => x.d); return ns.slice(1).map((d, j) => sskMove(ns[j], d)); };
const SSK_ARROW_TXT = { 1: '↑', 0: '=', '-1': '↓' };
// words to circle: the worked example's ringed in coral
const sskCircle = (words, on, small) => <div style={{display:'flex',justifyContent:'center',flexWrap:'wrap',gap:small ? 4 : 8,fontSize:small ? 11.5 : 13,fontWeight:800,color:BK.ink,marginTop:2}}>{words.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:small ? '0 4px' : '0 7px',color:on === w ? BK.coral : BK.ink}}>{w}</span>)}</div>;

// the Workbook's tasks, fixed so the Teacher copy always matches
const SSK_WB = {
  // p2: which way (the first two moves done)
  dir1: { clef: 'treble', items: [['ts', 4], ...sskQ([28, 29, 29, 30]), ['|'], ...sskQ([31, 30]), ['h', 2, 28], ['||']] },
  dir2: [{ clef: 'treble', items: [['ts', 3], ...sskQ([32, 33, 33]), ['|'], ...sskQ([34, 33, 33]), ['|'], ['hd', 3, 32], ['||']] }, { clef: 'bass', items: [['ts', 4], ...sskQ([25, 24, 24, 23]), ['|'], ...sskQ([22, 23]), ['h', 2, 21], ['||']] }],
  dir3: { clef: 'treble', items: [['ts', 4], ...sskQ([28, 30, 29, 31]), ['|'], ...sskQ([30, 32]), ['h', 2, 32], ['||']] },
  // p3: step, skip or the same (the first one done); draw the second note
  ss1: [['treble', 30, 31], ['treble', 33, 35]],
  ss2: [['treble', 32, 32], ['bass', 20, 22], ['treble', 31, 29], ['bass', 24, 23]],
  ss3: [[30, 1], [28, 2], [32, -1], [31, -2]],
  // p4: C position: the finger numbers (the first two done); the note names
  f1: { clef: 'treble', pos: 'C', hand: 'rh', items: [['ts', 4], ...sskQ([28, 29, 30, 28]), ['|'], ...sskQ([30, 31]), ['h', 2, 32], ['||']] },
  f2: [{ clef: 'bass', pos: 'C', hand: 'lh', items: [['ts', 4], ...sskQ([21, 22, 23, 21]), ['|'], ...sskQ([23, 24]), ['h', 2, 25], ['||']] }, { clef: 'treble', pos: 'C', hand: 'rh', items: [['ts', 3], ...sskQ([32, 31, 30]), ['|'], ...sskQ([31, 30, 29]), ['|'], ['hd', 3, 28], ['||']] }],
  f3: { clef: 'bass', pos: 'C', hand: 'lh', items: [['ts', 4], ...sskQ([21, 23, 25, 23]), ['|'], ['w', 4, 21], ['||']] },
  // p5: G position: the finger numbers (the first two done); the same fingers in two places; the note names
  g1: { clef: 'treble', pos: 'G', hand: 'rh', items: [['ts', 4], ...sskQ([32, 33, 32, 34]), ['|'], ...sskQ([35, 34]), ['h', 2, 36], ['||']] },
  g2: { clef: 'bass', pos: 'G', hand: 'lh', items: [['ts', 4], ...sskQ([20, 21, 22, 20]), ['|'], ...sskQ([19, 20]), ['h', 2, 18], ['||']] },
  shape: [1, 2, 3, 1, 3, 5, 3, 1],
  g3: { clef: 'treble', pos: 'G', hand: 'rh', items: [['ts', 3], ...sskQ([32, 34, 36]), ['|'], ...sskQ([35, 34, 33]), ['|'], ['hd', 3, 32], ['||']] },
  // p6: the first note: its finger is printed, so the position follows (the first one done); the moves; a whole tune
  r1: [['treble', 32, 1, 'G'], ['treble', 32, 5, 'C'], ['bass', 21, 5, 'C'], ['bass', 21, 2, 'G']],
  r2: [{ clef: 'bass', items: [['ts', 3], ...sskQ([18, 20, 19]), ['|'], ...sskQ([21, 22, 20]), ['|'], ['hd', 3, 18], ['||']] }],
  r3a: [['ts', 4], ...sskQ([18, 19, 20, 22]), ['|'], ['h', 2, 20], ['h', 2, 19], ['|']],
  r3b: [...sskQ([20, 21, 22, 21]), ['|'], ...sskQ([20, 19]), ['h', 2, 18], ['||']],
};
SSK_WB.r3 = { clef: 'bass', pos: 'G', hand: 'lh', items: [...SSK_WB.r3a, ...SSK_WB.r3b] };
const SSK_CHK = {
  dir: { clef: 'bass', items: [['ts', 4], ...sskQ([21, 22, 22, 24]), ['|'], ...sskQ([23, 21]), ['h', 2, 21], ['||']] },
  ss: [['treble', 29, 30], ['treble', 35, 33], ['bass', 23, 23], ['bass', 22, 20]],
  fing: [{ clef: 'treble', pos: 'C', hand: 'rh', items: sskW([30, 32, 29, 28]) }, { clef: 'bass', pos: 'C', hand: 'lh', items: sskW([25, 23, 21, 24]) }],
  names: [{ clef: 'treble', items: sskW([33, 36, 34, 32]) }, { clef: 'bass', items: sskW([22, 19, 21, 18]) }],
  read: { clef: 'treble', items: [['ts', 3], ...sskQ([32, 34, 33]), ['|'], ...sskQ([33, 35, 34]), ['|'], ['hd', 3, 32], ['||']] },
};
const sskFingers = (r) => sskNotesOf(r.items).map(x => sskFingerOf(r.pos, r.hand, x.d));
const sskNames = (r) => sskNotesOf(r.items).map(x => dName(x.d));
// a two-note cell (step, skip or the same)
const sskPair = ([clef, a, b], mm = 4.5) => <SskPaper mm={mm} clef={clef} items={[['w', 4, a], ['w', 4, b]]} o={{ D: 12, x0: clef === 'bass' ? 54 : 42 }}/>;

function SskWorkbook({ startNo = 1 }) {
  const W = SSK_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="reading-steps">{content}</WbPage>);
  const boxes = (r, ex = 0) => ({ D: 32, moves: 'box', moveAns: sskDirs(r.items).map((_, j) => j < ex) });
  const fing = (r, ex = 0) => { const f = sskFingers(r); return { D: 34, fingerR: 10, fingers: f.map((v, j) => j < ex ? v : ''), fingerAt: r.hand === 'rh' ? 'above' : 'below' }; };
  const names = (r, ex = 0) => { const nm = sskNames(r); return { D: 34, boxS: 30, under: nm.map((v, j) => j < ex ? v : null), underCoral: nm.map((_, j) => j).filter(j => j < ex) }; };
  const ARROWS = 'In each box, draw ↑ up, ↓ down or = the same.';

  // 2 (faces "Up, down or the same")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which way?" how={ARROWS + ' The first two are done.'}>
      {sskRowN(1, <SskPaper mm={4.5} clef={W.dir1.clef} items={W.dir1.items} o={boxes(W.dir1, 2)}/>)}
    </Part>
    <Part kind="home" title="More moves" how={ARROWS}>
      <div style={{display:'grid',gap:12}}>{W.dir2.map((r, i) => sskRowN(i + 2, <SskPaper mm={4.3} clef={r.clef} items={r.items} o={boxes(r)}/>))}</div>
    </Part>
    <Part kind="play" title="Mark it, then play it" how={ARROWS + ' Then right hand, thumb on middle C: play it, counting 1 2 3 4.'}>
      {sskRowN(4, <SskPaper mm={4.6} clef={W.dir3.clef} items={W.dir3.items} o={boxes(W.dir3)}/>)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Steps and skips")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Step, skip or the same?" how="Circle step, skip or same. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.ss1.map((c, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'8px 4px 2px'}}>{sskPair(c, 3.6)}{sskCircle(['step', 'skip', 'same'], i === 0 ? sskMove(c[1], c[2]) : null)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="More pairs" how="Circle step, skip or same.">
      <BkGrid cols={2} gap="8px 14px">{W.ss2.map((c, i) => <ExCell key={i} n={i + 3}><div style={{padding:'10px 4px 2px'}}>{sskPair(c, 3.5)}{sskCircle(['step', 'skip', 'same'])}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Draw it, then play it" how="Draw the second note: a step or a skip from the first. Then right hand, thumb on middle C: play the two notes.">
      <BkGrid cols={2} gap="8px 14px">{W.ss3.map(([d, mv], i) => <ExCell key={i} n={i + 7}><div style={{padding:'10px 2px 2px'}}><SskPaper mm={3.5} items={[['w', 4, d], ['sp', 50]]} o={{ D: 12, x0: 42 }}/>
        <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.ink}}>{(Math.abs(mv) === 1 ? 'a step ' : 'a skip ') + (mv > 0 ? 'up' : 'down')}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "C position")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Write the finger numbers" how="Right hand in C position: C is finger 1. Write the finger number in each circle. The first two are done.">
      {sskRowN(1, <SskPaper mm={4.3} clef={W.f1.clef} items={W.f1.items} o={fing(W.f1, 2)}/>)}
    </Part>
    <Part kind="home" title="More finger numbers" how="Write the finger number in each circle. Left hand (bass clef): C is finger 5. Right hand (treble clef): C is finger 1.">
      <div style={{display:'grid',gap:10}}>{W.f2.map((r, i) => sskRowN(i + 2, <SskPaper mm={4.2} clef={r.clef} items={r.items} o={fing(r)}/>))}</div>
    </Part>
    <Part kind="play" title="Name it, then play it" how="Write the note names in the boxes. Then left hand in C position: play it, counting 1 2 3 4.">
      {sskRowN(4, <SskPaper mm={4.6} clef={W.f3.clef} items={W.f3.items} o={names(W.f3)}/>)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "G position")
  const cell = () => <span style={{display:'inline-block',width:34,height:30,border:'1.5px solid ' + BK.line,borderRadius:3,background:'#fff'}}/>;
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Write the finger numbers" how="Right hand in G position: G is finger 1. Write the finger number in each circle. The first two are done.">
      {sskRowN(1, <SskPaper mm={4.2} clef={W.g1.clef} items={W.g1.items} o={fing(W.g1, 2)}/>)}
    </Part>
    <Part kind="home" title="Same fingers, new place" how="Left hand in G position: G is finger 5. Write the finger numbers. Then write the right hand's notes for these fingers, in C position and in G position.">
      {sskRowN(2, <SskPaper mm={4.1} clef={W.g2.clef} items={W.g2.items} o={fing(W.g2)}/>)}
      {sskRowN(3, <div style={{display:'grid',gridTemplateColumns:'92px repeat(8, 38px)',alignItems:'center',justifyContent:'center',gap:'6px 4px',fontSize:12.5,fontWeight:800,color:BK.ink}}>
        <span>Fingers</span>{W.shape.map((f, i) => <span key={i} style={{display:'inline-flex',alignItems:'center',justifyContent:'center',width:28,height:28,borderRadius:14,border:'1.5px solid ' + BK.coral,color:BK.coral,fontWeight:900,justifySelf:'center'}}>{f}</span>)}
        <span>C position</span>{W.shape.map((_, i) => <span key={i} style={{justifySelf:'center'}}>{cell()}</span>)}
        <span>G position</span>{W.shape.map((_, i) => <span key={i} style={{justifySelf:'center'}}>{cell()}</span>)}
      </div>)}
    </Part>
    <Part kind="play" title="Name it, then play it" how="Write the note names in the boxes. Then right hand in G position: play it, counting 1 2 3.">
      {sskRowN(4, <SskPaper mm={5} clef={W.g3.clef} items={W.g3.items} o={names(W.g3)}/>)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Read a tune")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Find the first note" how="Write the note's name. Its finger number is printed: circle the position, C or G. The first one is done.">
      <BkGrid cols={4} gap="8px 8px">{W.r1.map(([clef, d, f, pos], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'8px 2px 0'}}><SskPaper mm={3.4} clef={clef} items={[['w', 4, d], ['sp', 18]]} o={{ D: 12, x0: 42, fingers: [f], fingerAt: clef === 'treble' ? 'above' : 'below', boxS: 30, under: [i === 0 ? dName(d) : null], underCoral: i === 0 ? [0] : [], underBoxed: true }}/>
        {sskCircle(['C', 'G'], i === 0 ? pos : null)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Circle the moves" how="Over each move, circle step, skip or same.">
      <div style={{display:'grid',gap:10}}>{W.r2.map((r, i) => sskRowN(i + 5, <SskPaper mm={3.6} clef={r.clef} items={r.items} o={{ D: 44, moves: 'circ' }}/>))}</div>
    </Part>
    <Part kind="play" title="Read it, then play it" how="Write the first note's name and its finger number. Clap and count the rhythm. Say the moves. Then left hand in G position: play it, counting 1 2 3 4.">
      {sskRowN(6, <div style={{width:'100%',maxWidth:Math.max(sskVbw(W.r3a, { D: 30 }, 'bass'), sskVbw(W.r3b, { D: 30 }, 'bass')) * 3.8 / 5 * 1.89,margin:'0 auto'}}>
        <SskSystems clef="bass" rows={[W.r3a, W.r3b]} gap={6} os={[{ D: 30, fingerR: 12, fingers: [''], fingerAt: 'above', boxS: 32, under: [null] }, { D: 30 }]}/>
      </div>)}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<SskPaperCheck/>);
  return <>{pages}</>;
}
function SskPaperCheck() {
  const C = SSK_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'In each box, draw ↑ up, ↓ down or = the same.')}
    <BkCell n={1}><div style={{padding:'6px 4px 0'}}><SskPaper mm={3.5} clef={C.dir.clef} items={C.dir.items} o={{ D: 32, moves: 'box' }}/></div></BkCell>
    {bkSec('B', 'Circle step, skip or same.')}
    <BkGrid cols={4} gap="6px 8px">{C.ss.map((c, i) => <BkCell key={i} n={i + 2}><div style={{padding:'8px 0 1px',minWidth:0}}>{sskPair(c, 3.4)}{sskCircle(['step', 'skip', 'same'], null, true)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'C position: write the finger numbers.')}
    <BkGrid cols={2} gap="6px 10px">{C.fing.map((r, i) => <BkCell key={i} n={i + 6}><div style={{padding:'8px 4px 0'}}><SskPaper mm={3.4} clef={r.clef} items={r.items} o={{ D: 11, x0: 46, fingerR: 10, fingers: r.items.map(() => ''), fingerAt: r.hand === 'rh' ? 'above' : 'below' }}/>
      <div style={{textAlign:'center',fontSize:11.5,fontWeight:800,color:BK.ink}}>{r.hand === 'rh' ? 'right hand' : 'left hand'}</div></div></BkCell>)}</BkGrid>
    {bkSec('D', 'G position: write the note names.')}
    <BkGrid cols={2} gap="6px 10px">{C.names.map((r, i) => <BkCell key={i} n={i + 8}><div style={{padding:'8px 4px 0'}}><SskPaper mm={3.4} clef={r.clef} items={r.items} o={{ D: 11, x0: 46, boxS: 30, under: r.items.map(() => null) }}/></div></BkCell>)}</BkGrid>
    {bkSec('E', 'A new tune: over each move, circle step, skip or same.')}
    <BkCell n={10}><div style={{padding:'4px 4px 0'}}><SskPaper mm={3.4} clef={C.read.clef} items={C.read.items} o={{ D: 44, moves: 'circ' }}/></div></BkCell>
  </div>;
}

const sskLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{txt}</div>;
function SskTeacher() {
  const W = SSK_WB, C = SSK_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="reading-steps" teacher>{content}</WbPage>);
  const arrows = (r, from = 0) => sskDirs(r.items).slice(from).map(d => SSK_ARROW_TXT[d]).join(' ');
  const words = (r) => sskWords(r.items).join(', ');
  const fings = (r, from = 0) => sskFingers(r).slice(from).join(' ');
  const nms = (r, from = 0) => sskNames(r).slice(from).join(' ');
  const shapeIn = (pos) => W.shape.map(f => dName(SSK_POS[pos].rh[f - 1])).join(' ');
  const marks = { A: sskDirs(C.dir.items).length, B: C.ss.length, C: C.fing.reduce((a, r) => a + r.items.length, 0), D: C.names.reduce((a, r) => a + r.items.length, 0), E: sskDirs(C.read.items).length };
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('reading-steps')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Each Workbook page faces its Lesson Book page. A tune is read by its moves: up, down or the same; a step (line to space or space to line: the next letter) or a skip (line to line or space to space: one letter jumped), named once as a 2nd and a 3rd. C position: right thumb on middle C, left finger 5 on the C below. G position: right thumb on G (line 2, treble staff), left finger 5 on G (line 1, bass staff). No songs. Not yet: leaps and intervals by number (chapter {bkChapterNo('intervals')}); hands together; ledger lines past middle C (chapter {bkChapterNo('ledger-lines')}); the slur (chapter {bkChapterNo('dynamics')}). Drill: levels 1 to 3 after page 3, 4 to 6 after page 5, 7 and 8 after page 6; level 9 (all twelve positions, with sharps and flats) is extra.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: the hand on the staircase.</b> The hand walks the staff in the air: a step is line to space or space to line, a skip line to line or space to space. Then on the keys, saying “step” or “skip” before each note.</div>
    <TcBlock page={2} title="Up, down or the same" answers={<>{sskLesson('Play a few notes; the child, eyes shut, points up, down or straight ahead. Then swap.')}{tcAns('TRY IT', [arrows(W.dir1, 2)], 1)}{tcAns('YOUR TURN', W.dir2.map(r => arrows(r)), 2)}{tcAns('PLAY', [arrows(W.dir3)], 4)}</>}
      watch="Reading every note name instead of the move. A repeated note played as a step. Up on the staff mixed up with up the keyboard: higher notes are to the right. Arrows drawn on the notes instead of between them."
      say="“Higher on the staff, further right on the keys.”"/>
    <TcBlock page={3} title="Steps and skips" answers={<>{sskLesson('Ask for a step or a skip from any note, up or down, in both clefs; the child names the line or space it lands on.')}{tcAns('TRY IT', W.ss1.map(c => sskMove(c[1], c[2])))}{tcAns('YOUR TURN', W.ss2.map(c => sskMove(c[1], c[2])), 3)}{tcAns('PLAY', W.ss3.map(([d, mv]) => dName(d) + ' → ' + dName(d + mv)), 7)}</>}
      watch="A line-to-space move read as a skip (it is a step). A skip on the keys that jumps a black key instead of a white one. A skip from a line drawn on a space."
      say="“Line to space: a step. Line to line: a skip.”"/>
    <TcBlock page={4} title="C position" answers={<>{sskLesson('Every finger curved and touching its key before playing. Name a finger; the child plays it and says the note name.')}{tcAns('TRY IT', [fings(W.f1, 2)], 1)}{tcAns('YOUR TURN', W.f2.map(r => fings(r)), 2)}{tcAns('PLAY', [nms(W.f3)], 4)}</>}
      watch="The left hand's numbers reversed (its thumb is on G, finger 5 on C). The right thumb on the wrong C: it sits on middle C. Fingers lifting high or the hand going flat. Reading the finger circles as the count."
      say="“Thumbs near the middle: right on middle C, left on G.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="G position" answers={<>{sskLesson('Move one hand from C position to G position and back, the shape never changing. Row 3: play the C-position notes, then the G-position notes.')}{tcAns('TRY IT', [fings(W.g1, 2)], 1)}{tcAns('YOUR TURN', [fings(W.g2), 'C position ' + shapeIn('C') + ' · G position ' + shapeIn('G')], 2)}{tcAns('PLAY', [nms(W.g3)], 4)}</>}
      watch="The left hand on the G below middle C instead of G on line 1 of the bass staff. The right thumb on the G below middle C. Thinking the same fingers play the same notes. B C in G position played as a skip: they are next to each other."
      say="“Same fingers, same shape, a new place.”"/>
    <TcBlock page={6} title="Read a tune" answers={<>{sskLesson('Give a new tune and keep to the order: the first note and its finger, clap and count, say the moves, then play without stopping. The printed finger, not the note alone, gives the position.')}{tcAns('TRY IT', W.r1.map(([, d, f, pos]) => dName(d) + ', ' + pos + ' position'))}{tcAns('YOUR TURN', W.r2.map(words), 5)}{tcAns('PLAY', ['first note ' + dName(W.r3.items[1][2]) + ', finger ' + sskFingers(W.r3)[0] + '; moves: ' + words(W.r3)], 6)}</>}
      watch="Playing before finding the first note. Stopping the count to search for keys: in a position every key is already under a finger. Looking at the hands instead of the music. Losing the place at a bar line or at the start of the second line."
      say="“First note, rhythm, moves, then play.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', [arrows(C.dir)])}
      {tcAns('B', C.ss.map(c => sskMove(c[1], c[2])), 2)}
      {tcAns('C', C.fing.map(r => fings(r)), 6)}
      {tcAns('D', C.names.map(r => nms(r)), 8)}
      {tcAns('E', [words(C.read)], 10)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each move, pair, finger number and note name: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}; {marks.A + marks.B + marks.C + marks.D + marks.E} in all. A section with any wrong answer is not passed yet: go back to its page below. The paper shows the reading; the playing is heard: also listen to the student play (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: say the moves of the tune, then play it. 2. Page 3: a step and a skip up and down from any note you point to. 3. Page 4: C position, each hand, up and down saying the finger numbers. 4. Page 5: G position, each hand, up and down: the right hand saying the note names, the left hand the finger numbers. 5. Page 6, or a new tune you choose: first note, rhythm, moves, then play without stopping. Got it! means right the first time, with a steady count.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['reading-steps'] = SskWorkbook;
TEACHER_COPIES['reading-steps'] = SskTeacher;
