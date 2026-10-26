import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AI-1 (the decision board's queue: the Workbook and teacher's copy for the new rooms): Playing Scales.
# Each Workbook page faces its Lesson Book page (2 to 6); the last one, facing My five checks, is the check-up on paper.
# Fixed items, so the teacher's copy always matches the page. Every answer is worked out from the room's own scale data
# (spNames, spFing, spCm, spStripCols), the same data the lessons play, so the paper and the app cannot disagree.
CODE = r'''
// ─── Chapter: Playing Scales, the Workbook and teacher's copy (Build AI-1) ───
const SP_WB = {
  turn: [['C', 'R', 'up'], ['C', 'L', 'up'], ['G', 'R', 'up'], ['G', 'L', 'up'], ['C', 'R', 'dn'], ['C', 'L', 'dn']],   // where does the turn land?
  fing: [['C', 'R', [3, 6]], ['G', 'L', [2, 5]], ['G', 'R', [3, 6]], ['C', 'L', [4, 6]]],   // one octave, the hidden fingers (by note)
  form: ['Am', 'Emh', 'Amh', 'Em'],                                                          // natural or harmonic?
  mirror: [['C', 2], ['C', 4], ['C', 6], ['Amh', 6]],                                        // contrary motion: the right hand's note j; the left hand's note j
  thumbs: ['G', 'F'],                                                                        // two octaves: where do both thumbs play?
  chk: { turn: [['G', 'R', 'dn'], ['C', 'L', 'up'], ['G', 'L', 'dn'], ['C', 'R', 'up']], form: ['Emh', 'Am', 'Amh', 'Em'],
    mirror: [['C', 1], ['C', 5], ['Amh', 2], ['Amh', 4]], fing: [['C', 'R', [3]], ['G', 'L', [5]], ['G', 'R', [6]], ['C', 'L', [2]]] },
};
// the turn, one octave: the first note where the finger number jumps (3 to 1: the thumb goes under; 1 to 3: 3 crosses over)
function spwTurn(k, h, dir) {
  const F = spFing(k, h, 1), N = spNames(k, 1), seq = dir === 'up' ? [0, 1, 2, 3, 4, 5, 6, 7] : [7, 6, 5, 4, 3, 2, 1, 0];
  for (let s = 1; s < seq.length; s++) if (Math.abs(F[seq[s]] - F[seq[s - 1]]) > 1) return { j: seq[s], name: N[seq[s]], kind: F[seq[s]] === 1 ? 'thumb under' : F[seq[s]] + ' over' };
  return null;
}
const spwHand = (h) => (h === 'R' ? 'Right hand' : 'Left hand');
const spwDir = (d) => (d === 'up' ? 'going up' : 'coming down');
const spwForm = (k) => (/h$/.test(k) ? 'H' : 'N');
const spwMirror = ([k, j]) => { const c = spCm(k); return { r: c.nmR[j], l: c.nmL[j], f: SP_CM_F[j], R: c.R[j], L: c.L[j], c }; };
// one octave on the keys, the hand's finger numbers shown (above for the right hand, below for the left)
function SpwKeys({ k, h, W = 15, H = 46, lit = {} }) {
  const K = spKeys(k, h, 1), F = spFing(k, h, 1), names = spNameMap(K, spNames(k, 1)), fm = spFingMap(K, F);
  return <SpKb lo={K[0]} hi={K[7]} W={W} H={H} lit={Object.assign(Object.fromEntries(K.map(x => [x, 'pale'])), lit)} names={names} up={h === 'R' ? fm : {}} dn={h === 'L' ? fm : {}} k={1}/>;
}
function SpwTurnCell({ item, n, ex, small }) {
  const [k, h, d] = item, a = spwTurn(k, h, d);
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
    <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{SP_SC[k].en}: {spwHand(h).toLowerCase()}, {spwDir(d)}</div>
    <SpwKeys k={k} h={h} W={small ? 11 : 18} H={small ? 34 : 50}/>
    <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>the turn lands on {nvBox(ex, a.name, 40, 28)}</div>
  </div></ExCell>;
}
// the scale's letters in a row, with its finger numbers under them; the hidden ones are coral circles
function SpwFingRow({ k, h, hide, ex }) {
  const N = spNames(k, 1), F = spFing(k, h, 1);
  return <div style={{display:'grid',gridTemplateColumns:'repeat(8, 1fr)',gap:4,alignItems:'center',justifyItems:'center'}}>
    {N.map((x, j) => <span key={'n' + j} style={{fontFamily:LB_SERIF,fontSize:16,fontWeight:800,color:BK.ink}}>{x}</span>)}
    {F.map((f, j) => hide.includes(j)
      ? <span key={'f' + j} style={{width:26,height:26,borderRadius:13,border:'2px solid ' + BK.coral,display:'inline-flex',alignItems:'center',justifyContent:'center',color:BK.coral,fontWeight:900,fontStyle:'italic',fontSize:14}}>{ex && j === hide[0] ? f : ''}</span>
      : <span key={'f' + j} style={{width:26,height:26,borderRadius:13,border:'2px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',color:BK.ink,fontWeight:900,fontSize:14}}>{f}</span>)}
  </div>;
}
// a scale's eight letters, in boxes
const spwLetters = (k, size = 34) => <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap'}}>{spNames(k, 1).map((x, j) => <span key={j} style={{width:size,height:size,border:'1.6px solid ' + BK.ink,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:size * 0.5,fontWeight:800,color:BK.ink}}>{x}</span>)}</div>;
function SpwMirrorCell({ item, n, ex, W = 13 }) {
  const m = spwMirror(item), c = m.c;
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
    <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{SP_CM[item[0]].en}</div>
    <SpKb lo={c.L[7]} hi={c.R[7]} W={W} H={40} lit={{ [c.R[0]]: 'pale', [m.R]: 'cor' }} k={1}/>
    <div style={{fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>Both start on the pale key. Right hand: {m.r}, finger {m.f}</div>
    <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.coral}}>left hand's finger {m.f} plays {nvBox(ex, m.l, 40, 28)}</div>
  </div></ExCell>;
}
function SpWorkbook({ startNo = 1 }) {
  const W = SP_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scale-play">{content}</WbPage>);
  const KC = spKeys('C', 'R', 1);

  // 2 (faces "Smooth turns")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Where does the turn land?" how="The finger numbers are on the keys. Find the turn: the thumb goes under, or 3 crosses over. Write the letter it lands on.">
      <BkGrid cols={3} gap="6px 10px">{W.turn.map((it, i) => <SpwTurnCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Smooth turns this week" how="Do each one at the piano and tick a box each day. Listen to the turn: no bump.">
      <PhLog rows={['Right hand, C major: up and back 4 times, the thumb ready early', 'Left hand, C major: 3 over going up, thumb under coming down', 'G major, each hand, the same way']} label={300}/>
    </Part>
    <Part kind="play" title="The thumb's tunnel" how="Draw the thumb's path under the hand: from C, under fingers 2 and 3, to F. Then play it and listen: no bump.">
      <div style={{padding:'4px 30px'}}><SpKb lo={KC[0]} hi={KC[7]} W={44} H={92} lit={Object.fromEntries(KC.map(x => [x, 'pale']))} names={spNameMap(KC, spNames('C', 1))} up={spFingMap(KC, spFing('C', 'R', 1))} k={1}/></div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "On the beat")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Fill in the fingers" how="Write the missing finger numbers in the coral circles. Then play the scale, one note a beat.">
      <div style={{display:'grid',gap:8}}>{W.fing.map(([k, h, hide], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gridTemplateColumns:'120px 1fr',gap:10,alignItems:'center',padding:'14px 6px 4px'}}>
        <span style={{fontFamily:LB_SERIF,fontSize:14,fontWeight:800,color:BK.ink,lineHeight:1.2}}>{SP_SC[k].en}<br/><span style={{fontFamily:'Inter, sans-serif',fontSize:11,color:BK.muted}}>{spwHand(h).toLowerCase()}, going up</span></span>
        <SpwFingRow k={k} h={h} hide={hide} ex={i === 0}/></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="With the metronome" how="Tick a box each day. Move up to 76 only when the turns are even. Play from memory.">
      <PhLog rows={['C major, right hand, then left: at 60', 'G major, right hand, then left: at 60', 'C and G major at 76, the last note held for two beats']} label={300}/>
    </Part>
    <Part kind="play" title="Beat puzzle" how="One note a beat, up and back, and the last note held for two beats. Count it out.">
      <div style={{display:'grid',gap:12,padding:'10px 4px',fontSize:13.5,fontWeight:800,color:BK.ink}}>
        <span style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(5)} How many beats is one C major scale, up and back? {bkBox(48, 32)}</span>
        <span style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(6)} And G major? {bkBox(48, 32)}</span>
        <span style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(7)} At metronome 76, is one scale more or less than 15 seconds? {bkBox(64, 32)}</span>
      </div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "A and E minor")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Natural or harmonic?" how="Read the eight letters. Write N for the natural minor, H for the harmonic minor (its 7th goes up a half step).">
      <BkGrid cols={2} gap="6px 10px">{W.form.map((k, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:6,padding:'16px 4px 4px'}}>
        {spwLetters(k, 30)}<div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>N or H {nvBox(i === 0, spwForm(k), 40, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="The raised 7th" how="Write the note that goes up a half step in each harmonic minor. Then play both forms, each hand.">
      <div style={{display:'flex',gap:30,justifyContent:'center',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'6px 0'}}>{[['A minor', 5], ['E minor', 6]].map(([l, n]) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {l}: {bkBox(48, 32)}</span>)}</div>
    </Part>
    <Part kind="play" title="Colour A harmonic minor" how="Colour the eight keys of A harmonic minor, from A to A. Make the raised 7th a different colour. Write the letters on the keys.">
      <div style={{padding:'4px 30px'}}><SpKb lo={-3} hi={9} W={44} H={92} k={1}/></div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Mirror twins")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Mirror twins" how="Both hands start on one note and move apart, always with the same finger numbers. The right hand plays the coral key. Which note does the left hand's same finger play?">
      <BkGrid cols={2} gap="6px 10px">{W.mirror.map((it, i) => <SpwMirrorCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Mirror twins this week" how="Do each one at the piano and tick a box each day.">
      <PhLog rows={['C major from middle C, both thumbs together, saying the numbers', 'Coming back: both 3s cross over together', 'A harmonic minor from the A below middle C, at 66']} label={300}/>
    </Part>
    <Part kind="play" title="Mirror letters" how="The right hand goes up from A. Write the left hand's letters as it goes down from the same A: the twin of each note is under it.">
      <div style={{display:'grid',gap:6,padding:'8px 0'}}>{spwLetters('Amh', 40)}
        <div style={{display:'flex',gap:4,justifyContent:'center'}}>{spCm('Amh').nmL.map((x, j) => <span key={j} style={{width:40,height:40,border:'2px solid ' + (j === 0 ? BK.ink : BK.coral),borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>{j === 0 ? x : ''}</span>)}</div></div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Two octaves, hands together")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Where do the thumbs meet?" how="Two octaves, hands together. The right hand's fingers are on top, the left hand's underneath. Circle every letter where both hands play finger 1.">
      <div style={{display:'grid',gap:10}}>{W.thumbs.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:4}}>{SP_SC[k].en}, two octaves</div><SpStrip k={k} found={i === 0 ? spThumbs(k) : []} mw={640}/></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Hands together this week" how="Tick a box each day. Very slowly first; stop at each turn and check.">
      <PhLog rows={['G major, two octaves, each hand', 'G major hands together: the thumbs meet on the middle G', 'Run-ning at 60, then 76', 'F major, E minor and D minor the same way']} label={300}/>
    </Part>
    <Part kind="play" title="Thumb hunt" how="Guess first, then check at the piano: in E minor and D minor, two octaves hands together, where do both thumbs play?">
      <div style={{display:'flex',gap:30,justifyContent:'center',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'10px 0'}}>{[['E minor', 3], ['D minor', 4]].map(([l, n]) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {l}: {bkBox(56, 32)}</span>)}</div>
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (faces My five checks)
  P(<SpPaperCheck/>);
  return <>{pages}</>;
}
function SpPaperCheck() {
  const C = SP_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Where does the turn land? Write the letter.')}
    <BkGrid cols={2} gap="6px 8px">{C.turn.map(([k, h, d], i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>{SP_SC[k].en}, {spwHand(h).toLowerCase()}, {spwDir(d)}</div><SpwKeys k={k} h={h} W={13} H={32}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(32, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('B', 'Natural (N) or harmonic (H)?')}
    <BkGrid cols={2} gap="6px 8px">{C.form.map((k, i) => <BkCell key={i} n={i + 5}><div style={{display:'flex',alignItems:'center',gap:8,padding:'14px 2px 2px'}}><div style={{flex:1}}>{spwLetters(k, 24)}</div>{bkBox(32, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Mirror twins: which note does the left hand\'s same finger play?')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((it, i) => { const m = spwMirror(it); return <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>{SP_CM[it[0]].en.split(',')[0]}, from the pale key: right hand {m.r}, finger {m.f}</div><SpKb lo={m.c.L[7]} hi={m.c.R[7]} W={10} H={26} lit={{ [m.c.R[0]]: 'pale', [m.R]: 'cor' }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(32, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('D', 'Write the missing finger number.')}
    <BkGrid cols={2} gap="6px 8px">{C.fing.map(([k, h, hide], i) => <BkCell key={i} n={i + 13}><div style={{padding:'14px 2px 2px'}}><div style={{fontSize:9.5,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:3}}>{SP_SC[k].en}, {spwHand(h).toLowerCase()}, going up</div><SpwFingRow k={k} h={h} hide={hide}/></div></BkCell>)}</BkGrid>
  </div>;
}
function SpTeacher() {
  const W = SP_WB, C = W.chk, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scale-play" teacher>{content}</WbPage>);
  const turn = ([k, h, d]) => { const a = spwTurn(k, h, d); return a.name + ' (' + a.kind + ')'; };
  const fing = ([k, h, hide]) => hide.map(j => spNames(k, 1)[j] + ' ' + spFing(k, h, 1)[j]).join(', ');
  const thumbs = (k) => spThumbs(k).map(j => spStripCols(k).N[j]).join(', ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scale-play')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. The paper is the reminder; the scale itself is checked at the piano, from memory, mf and legato. The fingerings are the usual ones; another fingering is fine if it is logical and the same every time. The exam's own key lists stay in the technical work book.</div>
    <TcBlock page={2} title="Smooth turns" answers={<>{tcAns('TRY IT', W.turn.map(turn))}{tcAns('PLAY', ['an arc from C, under fingers 2 and 3, to F'])}</>}
      watch="A late thumb, a loud note on the turn, a hand that jumps. The wrist stays level and the elbow does not fly out: the arm carries the hand along."
      say="“The thumb gets ready early: it is under F before you need it.”"/>
    <TcBlock page={3} title="On the beat" answers={<>{tcAns('TRY IT', W.fing.map(fing))}{tcAns('PLAY', ['16 beats (15 notes, the last held for two)', '16', 'less (16 beats at 76 is about 13 seconds)'], 5)}</>}
      watch="The hands running ahead after a turn; the last note cut short. Start at 60; move to 76 only when the turns are even."
      say="“One note on every click. The last one holds for two.”"/>
    <TcBlock page={4} title="A and E minor" answers={<>{tcAns('TRY IT', W.form.map(k => spwForm(k) + ' (' + SP_SC[k].en + ')'))}{tcAns('YOUR TURN', ['A minor: G♯', 'E minor: D♯'], 5)}{tcAns('PLAY', ['A B C D E F G♯ A, G♯ in its own colour'])}</>}
      watch="Forgetting the raised 7th on the way down, or playing it in the natural form. The fingers are C major's in both hands."
      say="“Harmonic minor: the 7th goes up a half step, both ways.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Mirror twins" answers={<>{tcAns('TRY IT', W.mirror.map(it => { const m = spwMirror(it); return 'right ' + m.r + ' (' + m.f + ') → left ' + m.l; }))}{tcAns('PLAY', [spCm('Amh').nmL.join(' ')])}</>}
      watch="One hand leading and the other following. Both thumbs turn at the same moment, and both 3s cross over together: say the numbers out loud."
      say="“Same numbers, both ways: mirror twins.”"/>
    <TcBlock page={6} title="Two octaves, hands together" answers={<>{tcAns('TRY IT', W.thumbs.map(k => SP_SC[k].en + ': ' + thumbs(k)))}{tcAns('PLAY', ['E minor: ' + thumbs('Em'), 'D minor: ' + thumbs('Dm')], 3)}</>}
      watch="Hands together: the turns come at different moments in each hand, so a turn in one hand often pulls the other. Run-ning must stay even across the middle."
      say="“The thumbs meet in the middle. Two notes a beat: run-ning.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', C.turn.map(turn))}{tcAns('B', C.form.map(spwForm), 5)}{tcAns('C', C.mirror.map(it => spwMirror(it).l), 9)}{tcAns('D', C.fing.map(fing), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.4 · C p.5 · D p.3. Then hear the scale at the piano, not just on paper.</div></>}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['scale-play'] = SpWorkbook;
TEACHER_COPIES['scale-play'] = SpTeacher;
'''
rep("""function ScalePlayLessonBook() { return <>{spLbPages(false)}</>; }""",
    """function ScalePlayLessonBook() { return <>{spLbPages(false)}</>; }""" + CODE)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
