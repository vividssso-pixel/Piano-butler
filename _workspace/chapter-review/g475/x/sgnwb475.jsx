// ─── Phase 475: chapter 20's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: repeat signs; 1st and 2nd time bars;
// D.C. al Fine; D.S. al Fine; the pause; page 7 the check-up on paper) and its Teacher copy. English, like every Workbook.
// Every task set (rule 3) and done alone (rule 4); no road copied from the facing book page; nothing on a page gives away
// another task on it; the check-up repeats no practice item; answers vary (rule 7).
// Sizes (rule 5): a road to read or to write over at about 3.4 mm a staff space (one row, at most 5 bars; rw 520 for a
// page 680 wide); a road to draw the repeat signs on, at about 4 mm (3 bars, D 18, room at every bar line).
// a bar from a string: 'q30 q31 h32' (kind and step), with its signs
const sgnB = (str, x = {}) => ({ n: str.split(' ').map(w => sgnQ(+w.slice(1), w[0])), ...x });
const SGN_WB_RW = 520, SGN_WB_DRAW = 430;
// a box to write the order in (as long as the longest order of the set, so its length gives nothing away)
const sgnOrderBox = (w = 240, done) => <div style={{display:'flex',alignItems:'center',gap:8,justifyContent:'center'}}><span style={{fontSize:12,fontWeight:800,color:BK.muted,letterSpacing:'0.06em'}}>ORDER</span>
  <span style={{display:'inline-flex',alignItems:'center',width:w,height:34,border:'1.5px solid ' + (done ? BK.coral : BK.line),borderRadius:3,background:'#fff',padding:'0 8px',fontSize:16,fontWeight:900,color:BK.coral,fontStyle:'italic',letterSpacing:'0.12em',boxSizing:'border-box'}}>{done || ''}</span></div>;
const sgnPaperRoad = (bars, o, rw = SGN_WB_RW, box) => <SgnRoad bars={bars} rows={[[0, bars.length - 1]]} rw={rw} box={box} o={{ ts: 4, nums: true, D: 20, ...o }}/>;
const sgnTicks = (ws) => <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{ws.map(w => sprTickW(w))}</div>;

const SGN_WB = {
  ord2: [[sgnB('q30 q31 h32'), sgnB('q32 q31 q30 q29'), sgnB('q30 q29 h28', { end: true }), sgnB('q32 q30 h28')],                             // 1 2 3 1 2 3 4 (done)
         [sgnB('h32 h30'), sgnB('q31 q30 h29'), sgnB('q30 q31 q32 q30', { start: true }), sgnB('q29 q31 h28', { end: true })]],                // 1 2 3 4 3 4
  // to draw: the bars with the signs (the answer), the signs left out
  draw2: [[[sgnB('q32 q32 h30'), sgnB('q31 q31 h29', { start: true, end: true }), sgnB('q30 q29 h28')], ['start', 'end']]],                // 1 2 2 3
  play2: [sgnB('q28 q30 q29 q31'), sgnB('q30 q32 h31', { start: true }), sgnB('q32 q30 q31 q29'), sgnB('q30 q29 h28', { end: true })],          // 1 2 3 4 2 3 4
  ord3: [[sgnB('q28 q29 q30 q28'), sgnB('q29 q30 h31'), sgnB('q32 q31 h29', { v: 1, end: true }), sgnB('w28', { v: 2 })],                     // 1 2 3 1 2 4 (done)
         [sgnB('h30 h32'), sgnB('q31 q30 q29 q30', { start: true }), sgnB('q31 q32 h30', { v: 1, end: true }), sgnB('q29 q29 h28', { v: 2 })]], // 1 2 3 2 4
  draw3: [[[sgnB('h28 h30'), sgnB('q29 q31 h30', { v: 1, end: true }), sgnB('q31 q30 h29', { v: 2 }), sgnB('q30 q29 h28')], ['v']]],         // 1 2 1 3 4
  play3: [sgnB('q30 q30 q31 q32'), sgnB('q31 q30 h29', { start: true }), sgnB('q30 q31 h32'), sgnB('q31 q30 h29', { v: 1, end: true }), sgnB('q30 q29 h28', { v: 2 })],  // 1 2 3 4 2 3 5
  ord4: [[sgnB('q28 q29 q30 q31'), sgnB('q32 q30 h28', { fine: true }), sgnB('q30 q30 q31 q31'), sgnB('q32 q31 h30', { dc: true })],           // 1 2 3 4 1 2 (done)
         [sgnB('h32 h31'), sgnB('q30 q29 q30 q31'), sgnB('q29 q29 h28', { fine: true }), sgnB('q31 q32 q31 q30'), sgnB('q29 q30 h31', { dc: true })]], // 1 2 3 4 5 1 2 3
  draw4: [[[sgnB('q30 q31 q32 q30'), sgnB('q29 q31 h30'), sgnB('q29 q29 h28', { fine: true }), sgnB('q32 q32 h31', { dc: true })], ['fine']]],               // 1 2 3 4 1 2 3
  play4: [sgnB('q32 q31 q30 q31'), sgnB('q32 q30 h28', { fine: true }), sgnB('q30 q31 h29', { dc: true })],                                  // 1 2 3 1 2
  ord5: [[sgnB('h28 h32'), sgnB('q31 q30 q29 q30', { segno: true }), sgnB('q31 q29 h28', { fine: true }), sgnB('q30 q30 q31 q31'), sgnB('q32 q31 h29', { ds: true })],  // 1 2 3 4 5 2 3 (done)
         [sgnB('q30 q30 h31'), sgnB('q32 q32 h31'), sgnB('q30 q29 q30 q31', { segno: true }), sgnB('q30 q29 h28', { fine: true }), sgnB('q32 q30 h29', { ds: true })]], // 1 2 3 4 5 3 4
  draw5: [[[sgnB('h30 h29'), sgnB('q28 q29 q30 q31'), sgnB('q32 q30 h31'), sgnB('q31 q29 h28', { segno: true, fine: true }), sgnB('q30 q31 h32', { ds: true })], ['segno']]],      // 1 2 3 4 5 4
  play5: [sgnB('q28 q29 h30'), sgnB('q31 q30 q29 q30', { segno: true }), sgnB('q31 q29 h28', { fine: true }), sgnB('q32 q32 h29', { ds: true })],          // 1 2 3 4 2 3
  // one bar each; the pause drawn on the first (done), the coral note on the others
  pause6: [[sgnB('q31 q30 h29', { pause: [2] }), null], [sgnB('q32 q30 q31 q29'), 1], [sgnB('h31 q30 q28'), 0]],
  // circle the pauses (3), not the ties or the slur
  hunt6: [sgnB('q28 q29 q30 q31', { curve: [[0, 3]] }), sgnB('h32 h32', { curve: [[0, 1]], pause: [1] }), sgnB('q31 q30 h29', { pause: [2] }), sgnB('q30 q30 h28', { curve: [[0, 1]], pause: [2] })],
  play6: [sgnB('q28 q30 h32', { pause: [2] }), sgnB('q32 q31 h30'), sgnB('q29 q30 q31 q29'), sgnB('h30 h28', { pause: [1] })],
};
// the check-up: two roads to order (1st and 2nd time bars; D.S. al Fine), four signs to match, two to draw (repeat signs; Fine)
const SGN_W1 = (d, x = {}) => ({ n: [sgnQ(d, 'w')], ...x });
const SGN_CHK = {
  ord: [[sgnB('h32 h30'), sgnB('q31 q29 h30', { v: 1, end: true }), sgnB('q29 q29 h28', { v: 2 })],                                           // 1 2 1 3
        [sgnB('q28 q29 h30'), sgnB('q31 q29 h28', { segno: true, fine: true }), sgnB('q32 q30 h31', { ds: true })]],                           // 1 2 3 2
  mean: [['start', [SGN_W1(30, { start: true })]], ['segno', [SGN_W1(32, { segno: true })]], ['pause', [SGN_W1(31, { pause: [0] })]], ['end', [SGN_W1(29, { end: true })]]],   // one sign alone, one bar each
  meanList: ['end', 'start', 'segno', 'dc', 'pause', 'fine'],   // the letters a to f
  draw: [[[sgnB('q30 q31 h32'), sgnB('q32 q30 h31', { end: true }), sgnB('q30 q29 h28')], ['start', 'end']],                                  // 1 2 1 2 3
         [[sgnB('q32 q30 h28', { fine: true }), sgnB('q29 q30 q31 q32'), sgnB('q31 q29 h30'), sgnB('q31 q30 h29', { dc: true })], ['fine']]],                  // 1 2 3 4 1
};
const SGN_MEAN_EN = { end: 'Go back and play again', start: 'Where the end-repeat sign goes back to', segno: 'Where D.S. goes back to', dc: 'Go back to the beginning, then play up to Fine', pause: 'Hold this note longer', fine: 'The end, after a D.C. or D.S.' };
// the signs a drawing task asks for, in words (the Teacher copy)
const sgnDrawAns = (bars, hide) => { const out = [];
  bars.forEach((b, i) => { const n = i + 1;
    if (hide.includes('start') && b.start) out.push('start-repeat sign before bar ' + n);
    if (hide.includes('end') && b.end) out.push('end-repeat sign after bar ' + n);
    if (hide.includes('v') && b.v) out.push(b.v + '. over bar ' + n);
    if (hide.includes('fine') && b.fine) out.push('Fine at the end of bar ' + n);
    if (hide.includes('segno') && b.segno) out.push('segno over the start of bar ' + n); });
  return out.join(', ').replace(/ /g, ' ').replace(/, /g, ', '); };
const SGN_TC_HEAD = () => 'Signs that show the road (chapter ' + bkChapterNo('time-signatures') + ': bars, the double bar line and the repeat sign; chapter ' + bkChapterNo('dynamics') + ': the tie and the slur, not repeated here). AMEB Music Craft (2022 syllabus): repeat signs at Grade 1; first and second time bars, da capo, dal segno and al fine at Grade 2 (the pause is not named). ABRSM Music Theory (2023 specification): da capo, fine and al fine at Grade 1; dal segno at Grade 2; the pause, repeat marks and volta brackets by Grade 3. Not here: al Coda (drill level 9, extra, and the toolbox), 8va and ornaments (the toolbox).';

function SgnWorkbook({ startNo = 1 }) {
  const W = SGN_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="signs">{content}</WbPage>);
  const RO = { ts: 4, nums: true, D: 20 };
  // roads to order, one size for the set; the first done
  const orders = (list, n0) => { const box = Math.max(SGN_WB_RW, ...list.map(b => sgnBox(b, [[0, b.length - 1]], RO)));
    return <div style={{display:'grid',gap:5}}>{list.map((b, i) => sskRowN(n0 + i, <div style={{display:'flex',flexDirection:'column',gap:3,width:'100%'}}>{sgnPaperRoad(b, {}, SGN_WB_RW, box)}{sgnOrderBox(240, i === 0 ? sgnOrder(b).join(' ') : null)}</div>))}</div>; };
  // roads to draw signs on or over: the order to make above each. Repeat signs: on the staff, bigger, room at every bar line;
  // the others: over the staff, with a writing band above it
  const draws = (list, n0) => { const onStaff = list[0][1].includes('end'), o = onStaff ? { D: 18, room: true } : { band: list[0][1].includes('v') ? 24 : 5 }, rw = onStaff ? SGN_WB_DRAW : SGN_WB_RW;
    const box = Math.max(rw, ...list.map(([b, hide]) => sgnBox(b, [[0, b.length - 1]], { ...RO, ...o, noSigns: hide })));
    return <div style={{display:'grid',gap:8}}>{list.map(([b, hide], i) => sskRowN(n0 + i, <div style={{display:'flex',flexDirection:'column',gap:2,width:'100%'}}><div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,letterSpacing:'0.08em'}}>ORDER: {sgnOrder(b).join(' ')}</div>{sgnPaperRoad(b, { ...o, noSigns: hide }, rw, box)}</div>))}</div>; };
  const playRow = (n, bars, ticks, order = true, two, rw = SGN_WB_RW) => sskRowN(n, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{two ? <SgnRoad bars={bars} rows={[[0, 1], [2, bars.length - 1]]} rw={rw} o={{ ts: 4, nums: true, D: 24 }}/> : sgnPaperRoad(bars, {}, rw)}<div style={{display:'flex',justifyContent:'center',alignItems:'center',gap:'6px 30px',flexWrap:'wrap'}}>{order && sgnOrderBox(220)}{sgnTicks(ticks)}</div></div>);
  const T = ['saying the bar numbers', 'just playing'];
  const playHow = 'Write the order, then play it with the right hand in C position. Tick each time.';

  // 2 (faces "Repeat signs")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Write the order" how="Write the bar numbers in the order you play them. The first one is done.">{orders(W.ord2, 1)}</Part>
    <Part kind="home" title="Draw the repeat signs" how="Draw the repeat signs, dots and lines, so that you play the bars in this order.">{draws(W.draw2, 3)}</Part>
    <Part kind="play" title="Play it" how={playHow}>{playRow(4, W.play2, T, true, false, 440)}</Part>
    <Faces/>
  </>);
  // 3 (faces "1st and 2nd time bars")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Write the order" how="Write the bar numbers in the order you play them. The first one is done.">{orders(W.ord3, 1)}</Part>
    <Part kind="home" title="Draw the brackets" how="Draw the 1st and 2nd time brackets, with 1. and 2., so that you play the bars in this order.">{draws(W.draw3, 3)}</Part>
    <Part kind="play" title="Play it" how={playHow}>{playRow(4, W.play3, T, true, false, 480)}</Part>
    <Faces/>
  </>);
  // 4 (faces "D.C. al Fine")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Write the order" how="Write the bar numbers in the order you play them. The first one is done.">{orders(W.ord4, 1)}</Part>
    <Part kind="home" title="Write Fine" how="Write Fine over the bar line where the music ends, so that you play the bars in this order.">{draws(W.draw4, 3)}</Part>
    <Part kind="play" title="Play it" how={playHow}>{playRow(4, W.play4, T)}</Part>
    <Faces/>
  </>);
  // 5 (faces "D.S. al Fine")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Write the order" how="Write the bar numbers in the order you play them. The first one is done.">{orders(W.ord5, 1)}</Part>
    <Part kind="home" title="Draw the segno" how="Draw the segno over the start of the bar D.S. goes back to, so that you play the bars in this order.">{draws(W.draw5, 3)}</Part>
    <Part kind="play" title="Play it" how={playHow}>{playRow(4, W.play5, T, true, false, 600)}</Part>
    <Faces/>
  </>);
  // 6 (faces "The pause")
  const pBox = Math.max(...W.pause6.map(([b]) => sgnVbw([b], 0, 0, { ts: 4, D: 16 })));
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Draw the pause" how="Draw a pause over each coral note. The first one is done.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:14}}>{W.pause6.map(([b, at], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'6px 8px 2px'}}><SgnRoad bars={[b]} rows={[[0, 0]]} rw={pBox} box={pBox} o={{ ts: 4, D: 16, coral: ['pause'], band: i === 0 ? 0 : 6, hl: at == null ? [] : [[0, at]] }}/></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Circle the pauses" how="Circle each pause. Do not circle the ties or the slur.">
      {sskRowN(4, <div style={{width:'100%'}}>{sgnPaperRoad(W.hunt6, { nums: false })}</div>)}
    </Part>
    <Part kind="play" title="Play it" how="Play it twice: without the pauses, then with them. Hear the difference. Tick each time.">{playRow(5, W.play6, ['without the pauses', 'with the pauses'], false, true, 300)}</Part>
    <Faces/>
  </>);
  // 7. the check-up on paper
  P(<SgnPaperCheck/>);
  return <>{pages}</>;
}
const sgnChkNo = () => { const C = SGN_CHK, nB = C.ord.length + 1, nC = nB + C.mean.length; return { nB, nC }; };
function SgnPaperCheck() {
  const C = SGN_CHK, { nB, nC } = sgnChkNo(), L = 'abcdef', RO = { ts: 4, nums: true, D: 20 };
  const box = Math.max(...C.ord.map(b => sgnBox(b, [[0, b.length - 1]], RO)));
  const mBox = Math.max(...C.mean.map(([, bars]) => sgnVbw(bars, 0, bars.length - 1, { D: 11 })));
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the bar numbers in the order you play them.')}
    <BkGrid cols={1} gap="4px">{C.ord.map((b, i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gridTemplateColumns:'1fr 180px',alignItems:'center',gap:8,padding:'0 10px 2px 6px'}}><div style={{width:'100%'}}>{sgnPaperRoad(b, {}, box, box)}</div><span style={{display:'inline-block',width:170,height:36,border:'1.5px solid ' + BK.line,borderRadius:3,background:'#fff'}}/></div></BkCell>)}</BkGrid>
    {bkSec('B', 'Write the letter of what each coral sign tells you.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:'2px 14px',fontSize:12.5,color:BK.ink,margin:'0 4px 4px',lineHeight:1.35}}>{C.meanList.map((id, i) => <div key={id}><b>{L[i]}</b>{' '}{SGN_MEAN_EN[id]}</div>)}</div>
    <BkGrid cols={4} gap="6px 8px">{C.mean.map(([id, bars], i) => <BkCell key={id} n={nB + i}><div style={{display:'grid',gridTemplateColumns:'1fr 40px',alignItems:'end',height:'100%',boxSizing:'border-box',gap:4,padding:'2px 6px 8px 2px'}}><div style={{width:'100%'}}><SgnStaff bars={bars} width={mBox} full o={{ D: 11, coral: SGN_CORAL_OF[id], band: 6 }}/></div>{bkBox(36, 36)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Draw the signs so that you play the bars in this order.')}
    <BkGrid cols={1} gap="4px">{C.draw.map(([b, hide], i) => { const on = hide.includes('end'), o = on ? { D: 18, room: true } : { band: 5 };
      return <BkCell key={i} n={nC + i}><div style={{display:'flex',flexDirection:'column',gap:0,padding:'2px 10px 2px 6px'}}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,letterSpacing:'0.08em'}}>ORDER: {sgnOrder(b).join(' ')}</div>{sgnPaperRoad(b, { ...o, noSigns: hide }, on ? 470 : SGN_WB_RW)}</div></BkCell>; })}</BkGrid>
  </div>;
}

function SgnTeacher() {
  const W = SGN_WB, C = SGN_CHK, pages = [], { nB, nC } = sgnChkNo(), L = 'abcdef';
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="signs" teacher>{content}</WbPage>);
  const ord = (b) => sgnOrder(b).join(' ');
  const marks = { A: C.ord.length, B: C.mean.length, C: C.draw.length }, total = marks.A + marks.B + marks.C;
  const nameAt = (b, at) => dName(b.n[at][2]);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('signs')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{SGN_TC_HEAD()}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12.5,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>How the signs are written.</b> Start-repeat sign: thick line, thin line, then the two dots (in the 2nd and 3rd spaces). End-repeat sign: the two dots, then thin and thick. 1st time bracket: over the bar, closed at its end above the end-repeat sign; 2nd time bracket: open at its end. Fine: over the bar line where the music ends, usually two thin bar lines (chapter 8 showed only thin and thick). D.C. al Fine and D.S. al Fine: at the end of the last bar. Segno: over the start of its bar. Pause: a curve with a dot over the note or rest (upside down under it, when written below).</div>
    <TcBlock page={2} title="Repeat signs" answers={<>{sscLesson('The child points to the two repeat signs, then plays the page’s four bars saying each bar number.')}{skgTcAns('TRY IT', W.ord2.map((b, i) => ord(b) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.draw2.map(([b, h]) => sgnDrawAns(b, h)), 3)}{skgTcAns('PLAY', [ord(W.play2)], 4)}</>}
      watch="Going back to the beginning when there is a start-repeat sign. Going back twice (the part played three times). The dots drawn on the wrong side of the lines (they face the bars that are repeated)."
      say="“The dots point to the part you play twice.”"/>
    <TcBlock page={3} title={<span style={{fontFamily:'inherit',fontVariantNumeric:'lining-nums'}}>1st and 2nd time bars</span>} answers={<>{sscLesson('Play the page’s four bars; the child says “first time” or “second time” at bars 3 and 4.')}{skgTcAns('TRY IT', W.ord3.map((b, i) => ord(b) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.draw3.map(([b, h]) => sgnDrawAns(b, h) + ' (2. over bars 3 and 4 is also right)'), 3)}{skgTcAns('PLAY', [ord(W.play3)], 4)}</>}
      watch="The 1st time bar played again the second time. Playing straight through both brackets. The 2. bracket closed at its end, or drawn over the 1st time bar."
      say="“First time the 1. bar; second time, skip it and play the 2. bar.”"/>
    <TcBlock page={4} title="D.C. al Fine" answers={<>{sscLesson('The child points to Fine and to D.C. al Fine and says where the music ends.')}{skgTcAns('TRY IT', W.ord4.map((b, i) => ord(b) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.draw4.map(([b, h]) => sgnDrawAns(b, h)), 3)}{skgTcAns('PLAY', [ord(W.play4)], 4)}</>}
      watch="Stopping at Fine the first time. Playing past Fine after the D.C. Fine written at the start of a bar instead of over its bar line. Fine read as the English word: it is said fee-nay."
      say="“Fine is the finish line, but only on the way back.”"/>
  </>);
  P(<>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 10px',lineHeight:1.55,border:'0.8px solid ' + BK.hair,padding:'7px 12px'}}><b style={{color:BK.coral}}>Lesson time: the road check.</b> Open a piece the child is learning. Before playing, they point to every sign on the road and say the bar order aloud; then play it, in time, with no gap at the jumps. (After a D.C. or D.S., repeats are usually not played again and the 1st time bar is skipped; if a piece says otherwise, follow the piece.)</div>
    <TcBlock page={5} title="D.S. al Fine" answers={<>{sscLesson('The child points to the segno, to Fine and to D.S. al Fine; then plays the five bars in order.')}{skgTcAns('TRY IT', W.ord5.map((b, i) => ord(b) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.draw5.map(([b, h]) => sgnDrawAns(b, h) + ' (with Fine on the same bar)'), 3)}{skgTcAns('PLAY', [ord(W.play5)], 4)}</>}
      watch="D.S. read as D.C. (back to the beginning). The segno read as a percent sign, or drawn at the end of a bar. Not stopping at Fine."
      say="“D.C.: the beginning. D.S.: the sign.”"/>
    <TcBlock page={6} title="The pause" answers={<>{sscLesson('Play the page’s two bars without and with the pauses; the child says which is which.')}{skgTcAns('TRY IT', W.pause6.map(([b, at], i) => 'a pause over the ' + nameAt(b, i === 0 ? b.pause[0] : at) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', ['3 pauses: over the second G (bar 2), the D (bar 3) and the last C; not the slur (bar 1) or the two ties'], 4)}{skgTcAns('PLAY', ['without, then with the pauses'], 5)}</>}
      watch="The pause played as a silence, like pausing a video: it holds the sound. The pause counted as an exact number of beats every time. The note after the pause rushed. A tie or a slur taken for a pause (a pause has a dot)."
      say="“Hold it, breathe, go on.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {skgTcAns('A', C.ord.map(ord))}
      {skgTcAns('B', C.mean.map(([id]) => L[C.meanList.indexOf(id)]), nB)}
      {skgTcAns('C', C.draw.map(([b, h]) => sgnDrawAns(b, h) + (h.includes('end') && !b.some(x => x.start) ? ' (a start-repeat sign at the very beginning is also right)' : '')), nC)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer: A {marks.A}, B {marks.B}, C {marks.C}; {total} in all. A: the whole order, right, for the mark. C: the repeat sign with its dots on the right side, for the mark. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '2 and 4', page: '3 and 5' }, { id: 'b', step: '1, 4 and 5', page: '2, 5 and 6' }, { id: 'c', step: '1 and 3', page: '2 and 4' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> 1 what each sign tells you · 2 repeat signs · 3 1st and 2nd time bars · 4 D.C. al Fine · 5 D.S. al Fine · 6 how many bars · 7 listening (screen only) · 8 all the roads · 9 extra: al Coda.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: play the four bars with the repeat. 2. Page 3: play them, 1st time bar then 2nd. 3. Page 4: play them with D.C. al Fine. 4. Page 5: play them with D.S. al Fine. 5. Page 6: play the two bars, holding the pauses. Each in time, with no gap at the jumps. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['signs'] = SgnWorkbook;
TEACHER_COPIES['signs'] = SgnTeacher;
