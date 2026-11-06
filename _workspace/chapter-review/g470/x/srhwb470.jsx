// ─── Phase 470: chapter 14's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: grouping quavers; a quaver alone;
// the dotted crotchet; before beat 1; count, clap, play; page 7 the check-up on paper) and its Teacher copy. English,
// like every Workbook. Every task set (rule 3) and done alone (rule 4); a word to write is words to circle (rule 5); no
// PLAY task repeats its Lesson Book page; the check-up repeats no practice bar. The sets' answers vary (rule 7).
// a staff at a set size: mm between the lines, never wider than its box
function SrhPaper({ items, o = {}, mm = 4.2, label }) {
  const m = srhRaw((d) => dY(d), items, o), vbw = Math.ceil(m.last + 6), px = vbw * mm / 5 * 1.89;
  return <div style={{width:'100%',maxWidth:px,minWidth:0,margin:'0 auto'}}><SrhStaff full items={items} o={o} label={label} pad={[o.padTop || 14, srhPadBottom(o)]}/></div>;
}
// the count of a row, as the answer: every beat and every note between them; a rest's count in brackets
function srhCountText(items, from = 0) {
  const out = []; let b = 0, barB = -from;
  items.forEach(it => { const k = it[0];
    if (k === '|') { out.push('|'); barB = b; return; }
    if (!srhIsNote(it)) return;
    if (k === 'box') { b += srhLen(it); return; }
    const len = srhLen(it), n = SRH_HEADS[k] || 1, d = len / n, pts = [];
    for (let h = 0; h < n; h++) pts.push(b + h * d);
    for (let P = Math.ceil(b - barB - 1e-6); P < b + len - barB - 1e-6; P++) { const B = P + barB; if (!pts.some(p => Math.abs(p - B) < 1e-6)) pts.push(B); }
    pts.sort((x, y) => x - y).forEach(p => { const tx = srhCount(p - barB); out.push(srhRest(k) ? '(' + tx + ')' : tx); });
    b += len; });
  return out.join(' ');   // wide spaces: '1 + 2' never reads '1+2'
}
// a tune that starts before beat 1: the anacrusis, a full bar, then open (start) or the last bar as a box (last)
// the last bar's choices: short bars only (1 beat up to one less than the bar)
const srhLastPick = (top) => Array.from({ length: top - 1 }, (_, j) => j ? (j + 1) + ' beats' : '1 beat');
const srhUpItems = ([top, ana, from, full], mode) => [['ts', top], ...ana.map(k => [k]), ['|'], ...full.map(k => [k]), ...(mode === 'last' ? [['|'], ['box', from, 58], ['||']] : [['sp', 18]])];
const srhFillItems = ([top, ks]) => srhGapItems(top, ks);
// glyphs to circle; the worked example's ringed in coral
const srhGlyphCircle = (ks, on, h = 46) => <div style={{display:'flex',justifyContent:'center',gap:14,marginTop:'auto',paddingTop:4}}>{ks.map(k => <span key={k} style={{border:'1.5px solid ' + (on === k ? BK.coral : 'transparent'),borderRadius:26,padding:'0 6px',lineHeight:0}}><SrhGlyph k={k} h={h}/></span>)}</div>;
// the beat a tune starts on: tokens to circle, apart from the staff and labelled, so they never read as a count
const srhBeatPick = (n, on) => <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:14,marginTop:'auto',paddingTop:6,fontSize:13,fontWeight:800,color:BK.ink}}>
  <span style={{color:BK.muted}}>starts on beat</span>{Array.from({ length: n }, (_, j) => String(j + 1)).map(x => <span key={x} style={{width:26,height:26,borderRadius:13,display:'inline-flex',alignItems:'center',justifyContent:'center',border:'1.5px solid ' + (on === x ? BK.coral : 'rgba(38,41,107,0.3)'),color:on === x ? BK.coral : BK.ink,fontSize:14}}>{x}</span>)}</div>;
const SRH_EN = { e: 'a quaver', q: 'a crotchet', qd: 'a dotted crotchet', h: 'a minim' };
// the paper count line: room for a box under every half beat
const SRH_PO = { dyH: 18, dyC: 33, wide: true, bw: 28 };
const srhCntLine = (items, ex, mm = 3.3, from = 0) => <SrhPaper mm={mm} items={items} o={{ D: 44, from, counts: ex ? 'ans' : 'blank', ...SRH_PO }}/>;
const srhBareCell = (items, mm = 3.1, D = 40) => <SrhPaper mm={mm} items={items} o={{ D, counts: false, hearts: false }}/>;

const SRH_WB = {
  cnt2: [[['ts', 4], ['p'], ['q'], ['p'], ['q'], ['|'], ['p4'], ['h'], ['||']], [['ts', 3], ['q'], ['p'], ['p'], ['|'], ['p'], ['p'], ['q'], ['||']]],
  beam2: [[srhBar(4, 'q', 'q', 'p', 'p'), 'right'], [srhBar(4, 'q', 'p4', 'q'), 'wrong'], [srhBar(4, 'p', 'p4', 'q'), 'wrong'], [srhBar(3, 'p', 'p', 'p'), 'right']],
  play2: [['ts', 4], ['p'], ['q'], ['q'], ['p'], ['|'], ['q'], ['q'], ['p4'], ['||']],
  cnt3: [[['ts', 2], ['q'], ['er'], ['e'], ['|'], ['q'], ['e'], ['er'], ['||']], [['ts', 4], ['q'], ['er'], ['e'], ['h'], ['|'], ['er'], ['e'], ['q'], ['q'], ['q'], ['||']]],
  long3: [['p', '1'], ['er', '½'], ['p4', '2'], ['r', '1']],
  play3: [[['ts', 4], ['q'], ['er'], ['e'], ['p'], ['q'], ['|'], ['er'], ['e'], ['q'], ['h'], ['||']], [['ts', 3], ['q'], ['er'], ['e'], ['q'], ['|'], ['e'], ['er'], ['q'], ['q'], ['||']]],
  cnt4: [[['ts', 4], ['qd'], ['e'], ['q'], ['q'], ['|'], ['h'], ['qd'], ['e'], ['||']], [['ts', 3], ['qd'], ['e'], ['q'], ['|'], ['q'], ['qd'], ['e'], ['||']]],
  fill4: [[4, ['q', 'q', 'qd', ['box', 0.5]], 'e'], [3, [['box', 1.5], 'e', 'q'], 'qd'], [4, ['h', ['box', 1], 'q'], 'q'], [2, [['box', 1.5], 'e'], 'qd']],
  play4: [['ts', 4], ['q'], ['qd'], ['e'], ['q'], ['|'], ['qd'], ['e'], ['p'], ['q'], ['||']],
  start5: [[4, ['q'], 3, ['h', 'h']], [3, ['q'], 2, ['h', 'q']], [3, ['h'], 1, ['q', 'q', 'q']], [4, ['h'], 2, ['q', 'q', 'h']]],
  last5: [[4, ['p'], 3, ['q', 'q', 'h']], [3, ['p'], 2, ['q', 'q', 'q']], [4, ['hd'], 1, ['h', 'h']], [4, ['q', 'q'], 2, ['p', 'p', 'h']]],
  play5: [[[['ts', 4], ['q'], ['q'], ['|'], ['p'], ['p'], ['h'], ['|'], ['h'], ['||']], 2, 'count in 1 2 3 4, then 1 2'], [[['ts', 3], ['q'], ['q'], ['|'], ['h'], ['q'], ['|'], ['q'], ['||']], 1, 'count in 1 2 3, then 1']],
  cnt6: [[['ts', 4], ['p'], ['qd'], ['e'], ['q'], ['|'], ['q'], ['er'], ['e'], ['h'], ['||']], [['ts', 4], ['p4'], ['qd'], ['e'], ['|'], ['q'], ['er'], ['e'], ['p'], ['q'], ['||']]],
  match6: [['1 2 + 3 4', [srhBar(4, 'p', 'q', 'h'), srhBar(4, 'qd', 'e', 'h')], 'b'], ['1 + 2 + 3 4', [srhBar(4, 'p4', 'h'), srhBar(4, 'q', 'q', 'p', 'q')], 'a'],
    ['1 (2) + 3 4', [srhBar(4, 'q', 'er', 'e', 'h'), srhBar(4, 'q', 'p', 'h')], 'a'], ['1 2 3 +', [srhBar(3, 'p', 'q', 'q'), srhBar(3, 'q', 'q', 'p')], 'b']],
  play6: [['ts', 4], ['p'], ['|'], ['qd'], ['e'], ['q'], ['q'], ['|'], ['q'], ['er'], ['e'], ['q'], ['||']],
};
const SRH_CHK = {
  cnt: [['ts', 4], ['q'], ['p'], ['qd'], ['e'], ['|'], ['p4'], ['q'], ['er'], ['e'], ['||']],
  beam: [[srhBar(4, 'q', 'p4', 'p'), 'wrong'], [srhBar(4, 'q', 'p', 'q', 'p'), 'right'], [srhBar(4, 'h', 'p', 'p'), 'right'], [srhBar(4, 'e', 'p', 'e', 'q', 'q'), 'wrong']],
  beats: [['qd', '1½'], ['e', '½'], ['qde', '2'], ['q', '1']],
  fill: [[4, ['q', ['box', 1.5], 'e', 'q'], 'qd'], [3, ['q', 'qd', ['box', 0.5]], 'e']],
  start: [[4, ['hd'], 1, ['q', 'q', 'h']], [3, ['p'], 2, ['q', 'h']]],
  last: [[4, ['q'], 3, ['p', 'q', 'h']], [3, ['q', 'q'], 1, ['q', 'q', 'q']]],
};
const SRH_BOXES = 'A grey box is a beat a note holds through; a dashed box is a rest: write those counts too.';

function SrhWorkbook({ startNo = 1 }) {
  const W = SRH_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="rhythm">{content}</WbPage>);

  // 2 (faces "Grouping quavers")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Count the quavers" how="Write the count in every box: 1 + under two quavers. A grey box is a beat a note holds through: write it too. The first line is done.">
      <div style={{display:'grid',gap:4}}>{W.cnt2.map((r, i) => sskRowN(i + 1, srhCntLine(r, i === 0)))}</div>
    </Part>
    <Part kind="home" title="Beamed right?" how="Circle right or wrong.">
      <BkGrid cols={2} gap="8px 14px">{W.beam2.map(([r], i) => <BkCell key={i} n={i + 3}>{sdyCol(<>{srhBareCell(r, 3)}{sdyCircle(['right', 'wrong'], null)}</>, '10px 4px 2px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the count in every box. Then right hand, finger 3 on G: play it, counting out loud.">
      {sskRowN(7, srhCntLine(W.play2, false, 3.4))}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "A quaver alone")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Count the quaver rests" how={'Write the count in every box. ' + SRH_BOXES + ' The first line is done.'}>
      <div style={{display:'grid',gap:4}}>{W.cnt3.map((r, i) => sskRowN(i + 1, srhCntLine(r, i === 0)))}</div>
    </Part>
    <Part kind="home" title="How many beats?" how="Circle how many beats each picture lasts in all.">
      <BkGrid cols={4} gap="8px 10px">{W.long3.map(([k], i) => <BkCell key={i} n={i + 3}>{sdyCol(<><div style={{textAlign:'center'}}><SrhGlyph k={k} h={52}/></div>{sdyCircle(['½', '1', '1½', '2'], null, true, 10)}</>, '12px 2px 4px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the count in every box. Then right hand, finger 3 on G: play it. In a rest, lift your hand and keep counting.">
      <div style={{display:'grid',gap:2}}>{W.play3.map((r, i) => sskRowN(i + 7, srhCntLine(r, false, 3.2)))}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "The dotted crotchet")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Count the dotted crotchet" how="Write the count in every box. A grey box is a beat a note holds through: write it too. The first line is done.">
      <div style={{display:'grid',gap:8}}>{W.cnt4.map((r, i) => sskRowN(i + 1, srhCntLine(r, i === 0, 3.05)))}</div>
    </Part>
    <Part kind="home" title="Which note fills the gap?" how="Circle the note that fills the dashed box.">
      <BkGrid cols={2} gap="8px 14px">{W.fill4.map((f, i) => <BkCell key={i} n={i + 3}>{sdyCol(<>{srhBareCell(srhFillItems(f), 2.7)}{srhGlyphCircle(['e', 'q', 'qd'], null, 34)}</>, '10px 4px 2px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the count in every box. Then right hand, finger 3 on G: play it, long and short.">
      {sskRowN(7, srhCntLine(W.play4, false, 3.1))}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Before beat 1")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Which beat does it start on?" how="Count the missing beats out loud. The tune starts on the next beat: circle it. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.start5.map((u, i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{srhBareCell(srhUpItems(u, 'start'), 2.6, 36)}{srhBeatPick(u[0], i === 0 ? String(u[2] + 1) : null)}</>, '14px 4px 4px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="How long is the last bar?" how="Circle how many beats the last bar has.">
      <BkGrid cols={2} gap="8px 14px">{W.last5.map((u, i) => <BkCell key={i} n={i + 5}>{sdyCol(<>{srhBareCell(srhUpItems(u, 'last'), 2.3, 28)}{sdyCircle(srhLastPick(u[0]), null, true, 18)}</>, '10px 4px 2px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Count in, then play" how="Count in out loud: a bar, then the missing beats. Then right hand, finger 3 on G: play the tune. Tick each one you play.">
      <div style={{display:'grid',gap:10}}>{W.play5.map(([items, from, ci], i) => sskRowN(i + 9, <div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 210px',gap:14,alignItems:'center',width:'100%'}}>
        <SrhPaper mm={2.9} items={items} o={{ D: 40, from, counts: false, hearts: false }}/><span style={{display:'flex',alignItems:'center',gap:8,fontSize:14,fontWeight:800,color:BK.ink}}>{sprTick()}{ci}</span></div>))}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Count, clap, play")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Write the count" how={'Write the count in every box. ' + SRH_BOXES + ' The first line is done.'}>
      <div style={{display:'grid',gap:2}}>{W.cnt6.map((r, i) => sskRowN(i + 1, srhCntLine(r, i === 0, 2.95)))}</div>
    </Part>
    <Part kind="home" title="Which bar matches the count?" how="Read the count. Circle the bar it belongs to: a or b.">
      <div style={{display:'grid',gap:4}}>{W.match6.map(([c, bars], i) => sskRowN(i + 3, <div style={{display:'grid',gridTemplateColumns:'118px minmax(0,1fr) minmax(0,1fr)',gap:10,alignItems:'center',width:'100%',borderBottom:'0.8px solid ' + BK.hair,padding:'2px 0'}}>
        <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.ink,whiteSpace:'nowrap'}}>{c.split(' ').map((x, j) => <span key={j} style={{margin:'0 3px'}}>{x}</span>)}</div>
        {bars.map((b, j) => <div key={j} style={{display:'flex',alignItems:'center',gap:6}}><span style={{fontSize:15,fontWeight:900,color:BK.ink}}>{'ab'[j]}</span>{srhBareCell(b, 2.25, 36)}</div>)}</div>))}</div>
    </Part>
    <Part kind="play" title="Count it, clap it, play it" how="It starts on beat 4: count in 1 2 3 4, then 1 2 3. Write the count in every box. Then count it, clap it and play it on G.">
      {sskRowN(7, srhCntLine(W.play6, false, 2.75, 3))}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<SrhPaperCheck/>);
  return <>{pages}</>;
}
function SrhPaperCheck() {
  const C = SRH_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the count in every box. A grey box is a beat a note holds through; a dashed box is a rest.')}
    <BkCell n={1}><div style={{padding:'4px 4px 0'}}>{srhCntLine(C.cnt, false, 2.7)}</div></BkCell>
    {bkSec('B', 'Beamed right? Circle right or wrong.')}
    <BkGrid cols={2} gap="6px 10px">{C.beam.map(([r], i) => <BkCell key={i} n={i + 2}><div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 64px',alignItems:'center',gap:6,padding:'4px 4px 2px'}}>{srhBareCell(r, 2.3, 36)}<div style={{display:'flex',flexDirection:'column',gap:10,fontSize:13,fontWeight:800,color:BK.ink,alignItems:'center'}}><span>right</span><span>wrong</span></div></div></BkCell>)}</BkGrid>
    {bkSec('C', 'How many beats? Circle the answer.')}
    <BkGrid cols={4} gap="6px 8px">{C.beats.map(([k], i) => <BkCell key={i} n={i + 6}>{sdyCol(<><div style={{textAlign:'center'}}><SrhGlyph k={k} h={36}/></div>{sdyCircle(['½', '1', '1½', '2'], null, true, 9)}</>, '8px 2px 2px')}</BkCell>)}</BkGrid>
    {bkSec('D', 'Circle the note that fills the dashed box.')}
    <BkGrid cols={2} gap="6px 10px">{C.fill.map((f, i) => <BkCell key={i} n={i + 10}>{sdyCol(<>{srhBareCell(srhFillItems(f), 2.3)}{srhGlyphCircle(['e', 'q', 'qd'], null, 28)}</>, '6px 4px 2px')}</BkCell>)}</BkGrid>
    {bkSec('E', 'Circle the beat the tune starts on.')}
    <BkGrid cols={2} gap="6px 10px">{C.start.map((u, i) => <BkCell key={i} n={i + 12}>{sdyCol(<>{srhBareCell(srhUpItems(u, 'start'), 2.3, 34)}{srhBeatPick(u[0], null)}</>, '6px 4px 2px')}</BkCell>)}</BkGrid>
    {bkSec('F', 'Circle how many beats the last bar has.')}
    <BkGrid cols={2} gap="6px 10px">{C.last.map((u, i) => <BkCell key={i} n={i + 14}>{sdyCol(<>{srhBareCell(srhUpItems(u, 'last'), 2.3, 28)}{sdyCircle(srhLastPick(u[0]), null, true, 18)}</>, '6px 4px 2px')}</BkCell>)}</BkGrid>
  </div>;
}

const srhLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{txt}</div>;
function SrhTeacher() {
  const W = SRH_WB, C = SRH_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="rhythm" teacher>{content}</WbPage>);
  const fillA = (f) => SRH_EN[f[2]];
  const beatsW = (n) => n === 1 ? '1 beat' : n + ' beats';
  const marks = { A: 2, B: C.beam.length, C: C.beats.length, D: C.fill.length, E: C.start.length, F: C.last.length };
  const total = Object.values(marks).reduce((a, b) => a + b, 0);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('rhythm')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Rhythm patterns in 2/4, 3/4 and 4/4 (chapter {bkChapterNo('note-values')}: two quavers on a beat, the dotted minim; chapter {bkChapterNo('time-signatures')}: bars, time signatures, the tie). The level plan puts this at AMEB Grade 1: quaver groupings, the single quaver and the quaver rest, the dotted crotchet, the anacrusis. The count says + for ‘and’: 1 + 2 +. Every note sits on G, right hand finger 3 (as in chapter {bkChapterNo('time-signatures')}), so the eyes stay on the rhythm. The count-in is one bar, then the beats an anacrusis leaves out (1 2 3 4, 1 2 3); the app scores each tap on time and on length. Drill: in the book's order (1 page 2; 2 to 4 pages 2 to 4; 5 page 5; 6 and 7 page 6); 8 (semiquavers, 1 e + a) and 9 (syncopation) are extra.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: echo the rhythm.</b> Clap a bar while counting out loud; the child claps it back. Then the child claps one for you.</div>
    <TcBlock page={2} title="Grouping quavers" answers={<>{srhLesson('Clap line 1 while counting 1 + 2 + 3 4; the child echoes. Then the ✓ bar (line 2).')}{tcAns('TRY IT', W.cnt2.map(r => srhCountText(r)))}{tcAns('YOUR TURN', W.beam2.map(b => b[1]), 3)}{tcAns('PLAY', [srhCountText(W.play2)], 7)}</>}
      watch="Quavers rushed instead of two even halves of the beat. Quavers counted 1 2 3 4 instead of 1 + 2 +. Four quavers beamed across the middle of a 4/4 bar (beats 2 and 3)."
      say="“Beams group quavers by the beat: 1 +, 2 +.”"/>
    <TcBlock page={3} title="A quaver alone" answers={<>{srhLesson('Play a quaver rest and a quaver: the child counts (2) + out loud and comes in on the +.')}{tcAns('TRY IT', W.cnt3.map(r => srhCountText(r)))}{tcAns('YOUR TURN', W.long3.map(l => l[1] + (l[1] === '1' || l[1] === '½' ? ' beat' : ' beats')), 3)}{tcAns('PLAY', W.play3.map(r => srhCountText(r)), 7)}</>}
      watch="The quaver after a quaver rest played on the beat, not on the +. Counting stops in a rest. The flag taken for a beam to the next note."
      say="“A flag: a quaver alone. A quaver rest: half a beat of silence.”"/>
    <TcBlock page={4} title="The dotted crotchet" answers={<>{srhLesson('Play a crotchet tied to a quaver, then a dotted crotchet: the same length. Then long, short: 1 2 +.')}{tcAns('TRY IT', W.cnt4.map(r => srhCountText(r)))}{tcAns('YOUR TURN', W.fill4.map(fillA), 3)}{tcAns('PLAY', [srhCountText(W.play4)], 7)}</>}
      watch="The dotted crotchet cut to one beat, or the quaver played on 2 instead of the + after 2. The pattern evened out into two equal notes. Count 2 dropped while the note holds."
      say="“A dotted crotchet: one and a half beats. Long, short: 1 2 +.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Before beat 1" answers={<>{srhLesson('Open a piece the child knows that starts before beat 1: count in a bar and the missing beats together, start on the right beat, and look at the last bar.')}{tcAns('TRY IT', W.start5.map(u => 'beat ' + (u[2] + 1)))}{tcAns('YOUR TURN', W.last5.map(u => beatsW(u[2])), 5)}{tcAns('PLAY', W.play5.map(p => p[2] + ', then play'), 9)}</>}
      watch="The anacrusis played as beat 1, with the accent on it. No count-in, or the missing beats left out of it. The last bar held out to a full bar."
      say="“Before beat 1: count the missing beats, then start.”"/>
    <TcBlock page={6} title="Count, clap, play" answers={<>{srhLesson('Show a new line: the child finds the count and says it, claps it while counting, then plays it.')}{tcAns('TRY IT', W.cnt6.map(r => srhCountText(r)))}{tcAns('YOUR TURN', W.match6.map(m => m[2]), 3)}{tcAns('PLAY', [srhCountText(W.play6, 3)], 7)}</>}
      watch="Playing before the count is clear. Counting aloud dropped once the hands start. Tempo slowing for the dotted crotchet or the quavers: keep one steady beat."
      say="“Count it, clap it, play it.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', [srhCountText(C.cnt)])}
      {tcAns('B', C.beam.map(b => b[1]), 2)}
      {tcAns('C', C.beats.map(b => b[1] + (b[1] === '1' || b[1] === '½' ? ' beat' : ' beats')), 6)}
      {tcAns('D', C.fill.map(fillA), 10)}
      {tcAns('E', C.start.map(u => 'beat ' + (u[2] + 1)), 12)}
      {tcAns('F', C.last.map(u => beatsW(u[2])), 14)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer; A is two marks, one for each bar with every box right: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}, F {marks.F}; {total} in all. A section with any wrong answer is not passed yet: go back to its page below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 5, page: 6 }, { id: 'b', step: 1, page: 2 }, { id: 'c', step: 2, page: 3 }, { id: 'd', step: 3, page: 4 }, { id: 'e', step: 4, page: 5 }, { id: 'f', step: 4, page: 5 }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: count a line of quavers 1 + 2 +; why four quavers may share one beam. 2. Page 3: a quaver after a quaver rest, on the +. 3. Page 4: a dotted crotchet and a quaver, 1 2 +. 4. Page 5: count in, count the missing beats, then start before beat 1. 5. Page 6: a new line counted, clapped and played. Got it! means right without help.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5,marginTop:8}}><b style={{color:BK.coral}}>Beaming, as this chapter teaches it.</b> A beam joins the quavers of one beat; in 4/4 four quavers may share a beam on beats 1 and 2 or 3 and 4, never across the middle. A note may still start on beat 2 and hold across the middle (a dotted crotchet on 2): only beams stop there. AMEB and ABRSM also accept four quavers under one beam in 2/4 and six in 3/4, and nothing here marks those wrong. ABRSM Grade 1 theory already has semiquavers (drill level 8).</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS.rhythm = SrhWorkbook;
TEACHER_COPIES.rhythm = SrhTeacher;
