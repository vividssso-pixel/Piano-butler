// ─── Phase 473: chapter 18's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: before the piano; the first piano;
// inside the piano; the pedals; grand and upright; page 7 the check-up on paper) and its Teacher copy. English, like every
// Workbook. Every task set (rule 3) and done alone (rule 4); nothing on a page gives away another task on it; the check-up
// repeats no practice item; answers vary (rule 7).
const spsTicks = (ws) => <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{ws.map(w => sprTickW(w))}</div>;
// a sentence with words to circle, in one row: the sentence, then the words (at least 30 px apart)
const spsCircleRow = (n, text, words, done) => sskRowN(n, <div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:14,width:'100%',fontSize:15,color:BK.ink}}>
  <span style={{fontWeight:700}}>{text}</span>
  <div style={{display:'flex',gap:14}}>{words.map(w => <span key={w} style={{border:'1.6px solid ' + (done === w ? BK.coral : 'transparent'),borderRadius:14,padding:'1px 9px',fontWeight:800,color:done === w ? BK.coral : BK.ink,whiteSpace:'nowrap'}}>{w}</span>)}</div></div>);
// a sentence with its choices inline, one circled when done
const spsInline = (n, before, words, after, done) => sskRowN(n, <div style={{fontSize:15.5,color:BK.ink,lineHeight:1.9,fontWeight:700}}>{before} {words.map((w, i) => <React.Fragment key={w}>{i ? <span style={{color:BK.muted}}> / </span> : null}<span style={{border:'1.6px solid ' + (done === w ? BK.coral : 'transparent'),borderRadius:14,padding:'1px 7px',color:done === w ? BK.coral : BK.ink,fontWeight:800,whiteSpace:'nowrap'}}>{w}</span></React.Fragment>)}<span style={{marginLeft:-9}}>{after}</span></div>);
const spsBox = (w = 40, h = 34, txt) => <span style={{display:'inline-flex',alignItems:'center',justifyContent:'center',width:w,height:h,border:'1.4px solid ' + BK.ink,borderRadius:6,fontWeight:900,fontSize:17,color:BK.coral,verticalAlign:'middle',background:'#fff'}}>{txt || ''}</span>;
// the dynamics under a tune (p, f and cresc. in the music font)
const spsDyn = (c, sz = 20) => '<tspan style="font-family:' + MUSIC_FONT + ';font-style:italic;font-weight:700" font-size="' + sz + '">' + c + '</tspan>';
const SPS_CDEFG = [['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['q', 1, 32], ['||']];
const spsTune5 = (o = {}, ref = 420) => <div style={{width:'100%'}}><SacStaff items={SPS_CDEFG} width={ref} o={o}/></div>;

const SPS_WB = {
  how2: [['harpsichord', 'quill'], ['piano', 'hammer'], ['clavichord', 'tangent'], ['upright', 'hammer']],     // done: the harpsichord
  loud2: [['harpsichord', 'no'], ['clavichord', 'yes'], ['piano', 'yes']],
  first3: [['The first piano was built by', ['Mozart', 'Cristofori', 'Bach'], '.', 'Cristofori'],
           ['It was built in', ['Rome', 'Venice', 'Florence'], '.', 'Florence'],
           ['It was built about', ['1700', '1500', '1900'], '.', '1700'],
           ['Pianoforte means', ['high-low', 'soft-loud', 'fast-slow'], '.', 'soft-loud'],
           ['Cristofori was', ['a composer', 'an instrument maker', 'a king'], '.', 'an instrument maker']],
  order3: [['the 88-key piano', 3], ['the harpsichord', 1], ['Cristofori’s piano', 2]],
  parts4: { at: { hammer: 'A', damper: 'B', key: 'C', string: 'D' } },
  steps4: [['The hammer strikes the string.', 2], ['You let go of the key.', 3], ['You press the key.', 1], ['The damper stops the sound.', 4]],
  pedal5: [['Its other name is una corda.', 'left'], ['It moves every damper off the strings.', 'right'], ['On most uprights, it makes the piano very quiet for practice.', 'middle'], ['Its other name is the damper pedal.', 'right']],
  sound5: [['You play C and hold the key.', 'sounds'], ['You let go of the key, with no pedal.', 'stops'], ['You let go of the key with the right pedal down.', 'sounds'], ['Then you lift the right pedal.', 'stops']],
  kind6: [['grand', { cut: true, lidUp: true }], ['upright', { cut: false }], ['upright', { cut: true }], ['grand', { cut: false, lidUp: false }]],   // done: the first
};
const SPS_CHK = {
  mech: [['press', 'clavichord'], ['strike', 'piano'], ['pluck', 'harpsichord']],
  first: [['Cristofori was', ['German', 'Italian', 'English'], '.', 'Italian'], ['Forte means', ['loud', 'soft', 'slow'], '.', 'loud'], ['The first piano was built about', ['100', '300', '600'], ' years ago.', '300']],
  does: [['It strikes the string.', 'hammer'], ['It sounds when the hammer strikes it.', 'string'], ['It is a lever your finger presses.', 'key'], ['It rests on the string until you press the key.', 'damper']],
  pedal: [['With it, the notes keep sounding after you let go.', 'right'], ['On most grands, it keeps sounding only the notes you are holding.', 'middle'], ['It makes each note a little softer.', 'left']],
  keys: [['A piano has', ['61', '76', '88'], ' keys.', '88'], ['Its lowest key is', ['A', 'C', 'E'], '.', 'A'], ['A piano that fits against a wall is', ['a grand', 'an upright'], '.', 'an upright']],
};

function spsInstPic(id) {
  if (id === 'upright') return <svg viewBox="0 0 160 122" style={{width:'50%',display:'block',margin:'0 auto'}}><SpsUpright/></svg>;
  const C = id === 'harpsichord' ? SpsHarpsichord : id === 'clavichord' ? SpsClavichord : SpsGrand;
  return <svg viewBox="0 0 204 116" style={{width:'72%',display:'block',margin:'0 auto'}}><C x={2} y={0}/></svg>;
}

function SpsWorkbook({ startNo = 1 }) {
  const W = SPS_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="piano-story">{content}</WbPage>);
  const playSide = (n, node, tick) => sskRowN(n, <div style={{display:'grid',gridTemplateColumns:'1fr 150px',alignItems:'center',gap:10,width:'100%'}}>{node}{spsTicks([tick])}</div>);
  const playRow = (n, node, ticks) => sskRowN(n, <div style={{display:'flex',flexDirection:'column',gap:8,width:'100%'}}>{node}{spsTicks(ticks)}</div>);

  // 2 (faces "Before the piano")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="What sounds the strings?" how="Circle what sounds each one’s strings. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.how2.map(([id, part], i) => <ExCell key={id} n={i + 1} ex={i === 0}>{sdyCol(<>{spsInstPic(id)}
        <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'4px 0 2px'}}>{id === 'upright' ? 'an upright piano' : 'the ' + id}</div>
        {sdyCircle(['a quill', 'a tangent', 'a hammer'], i === 0 ? 'a ' + part : null, true, 16)}</>, '14px 6px 6px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Soft and loud?" how="Can it play soft and loud by how hard you press? Circle yes or no.">
      <div style={{display:'grid',gap:10}}>{W.loud2.map(([id], i) => spsCircleRow(i + 5, 'the ' + id, ['yes', 'no']))}</div>
    </Part>
    <Part kind="play" title="One loudness, then soft and loud" how="Play this tune all at one loudness. Then play it soft, then loud. Tick each time.">
      {playRow(8, spsTune5({}, 320), ['one loudness', 'soft', 'loud'])}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The first piano")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Circle the right word" how="Circle the word that makes each sentence right. The first one is done.">
      <div style={{display:'grid',gap:25,fontSize:17}}>{W.first3.map(([a, ws, b, ans], i) => spsInline(i + 1, a, ws, b, i === 0 ? ans : null))}</div>
    </Part>
    <Part kind="home" title="Oldest first" how="Number them 1, 2, 3, from the oldest to the newest.">
      <BkGrid cols={3} gap="8px 12px">{W.order3.map(([w], i) => <BkCell key={w} n={i + 6}>{sdyCol(<>
        <div style={{textAlign:'center',fontSize:17,fontWeight:900,color:BK.ink,margin:'8px 0 14px'}}>{w}</div>
        <div style={{textAlign:'center'}}>{spsBox(56, 52)}</div></>, '26px 6px 20px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Soft, loud, getting louder" how="Play this tune p, then f, then getting louder from p to f as it is marked. Tick each time.">
      {playRow(9, spsTune5({ under: [spsDyn('p'), undefined, spsDyn('cresc.', 17), undefined, spsDyn('f')] }, 268), ['p', 'f', 'p to f, as marked'])}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Inside the piano"): the key held down here (the book draws it at rest)
  const at4 = W.parts4.at, order4 = ['A', 'B', 'C', 'D'];
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Name the parts" how="Here the key is held down. Each letter marks a part: circle its name. The first one is done.">
      <div style={{display:'grid',gap:10}}>
        <div style={{maxWidth:350,margin:'0 auto',width:'100%'}}><SpsAction show="boxes" down arrow={false} letters={SPS_PARTS.map(p => at4[p]).join('')}/></div>
        <div style={{display:'grid',gap:4}}>{order4.map((L, i) => { const part = Object.keys(at4).find(p => at4[p] === L);
          return <div key={L} style={{display:'grid',gridTemplateColumns:'40px 1fr',alignItems:'center',gap:6}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:900,fontSize:19,color:BK.ink}}>{L}</span>
            <div style={{display:'flex',gap:34,flexWrap:'wrap'}}>{['key', 'hammer', 'string', 'damper'].map(w => <span key={w} style={{border:'1.6px solid ' + (i === 0 && w === part ? BK.coral : 'transparent'),borderRadius:14,padding:'1px 9px',fontSize:15,fontWeight:800,color:i === 0 && w === part ? BK.coral : BK.ink}}>{w}</span>)}</div></div>; })}</div>
      </div>
    </Part>
    <Part kind="home" title="In order" how="Number what happens, 1 to 4.">
      <div style={{display:'grid',gap:8}}>{W.steps4.map(([s], i) => sskRowN(i + 5, <div style={{display:'flex',alignItems:'center',gap:12,fontSize:15.5,fontWeight:700,color:BK.ink}}>{spsBox(40, 34)}<span>{s}</span></div>))}</div>
    </Part>
    <Part kind="play" title="Slowly, then hold and let go" how="On an acoustic piano, press middle C so slowly that it makes no sound. Then play it, hold it and let go: listen for the damper. Tick each time.">
      {playRow(9, <div style={{width:'100%'}}><SacStaff items={[['w', 4, 28], ['||']]} width={300} o={{ D: 16 }}/></div>, ['very slowly', 'hold, then let go'])}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "The pedals")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Which pedal?" how="Circle left, middle or right for each sentence. The first one is done.">
      <div style={{display:'grid',gap:8}}>{W.pedal5.map(([s, ans], i) => spsCircleRow(i + 1, s, ['left', 'middle', 'right'], i === 0 ? ans : null))}</div>
    </Part>
    <Part kind="home" title="Sounding or stopped?" how="Does the note keep sounding, or stop? Circle sounds or stops.">
      <div style={{display:'grid',gap:12}}>{W.sound5.map(([s], i) => spsCircleRow(i + 5, s, ['sounds', 'stops']))}</div>
    </Part>
    <Part kind="play" title="The two pedals" how="9: play C E G, press the right pedal, let go of the keys and count to four; then lift it. 10: play with the left pedal down. Tick each time.">
      <div style={{display:'grid',gap:10}}>{playRow(9, <div style={{width:'100%'}}><SacStaff items={[['q', 1, 28], ['q', 1, 30], ['h', 2, 32], ['||']]} width={285}/></div>, ['right pedal'])}
      {playRow(10, spsTune5({}, 285), ['left pedal'])}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Grand and upright")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Grand or upright?" how="Circle grand or upright under each piano. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.kind6.map(([ans, o], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>
        {ans === 'grand' ? <svg viewBox="0 0 204 116" style={{width:'94%',display:'block',margin:'0 auto'}}><SpsGrand x={2} y={0} cut={o.cut} lidUp={o.lidUp}/></svg> : <svg viewBox="0 0 160 122" style={{width:'66%',display:'block',margin:'0 auto'}}><SpsUpright cut={o.cut}/></svg>}
        {sdyCircle(['grand', 'upright'], i === 0 ? ans : null, true, 26)}</>, '20px 6px 10px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="The 88 keys" how="Put a dot on the lowest key and on the highest key. Then write how many white keys, black keys and Cs.">
      {sskRowN(5, <div style={{width:'100%'}}><svg viewBox="0 0 528 52" style={{width:'100%',display:'block'}}><SprKeys88 x0={2} y0={2} kw={10} h={46} middleC={false} sw={0.8}/></svg></div>)}
      <div style={{display:'flex',justifyContent:'center',gap:26,flexWrap:'wrap',marginTop:12}}>{[[6, 'white keys'], [7, 'black keys'], [8, 'Cs']].map(([n, w]) => <div key={n} style={{display:'flex',alignItems:'center',gap:8,fontSize:15.5,fontWeight:800,color:BK.ink}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:900,color:BK.muted}}>{n}</span>{spsBox(48, 38)}<span>{w}</span></div>)}</div>
    </Part>
    <Part kind="play" title="End to end" how="On an 88-key piano, play the lowest A and the highest C. Then play every C from the bottom to the top, counting. Tick each time.">
      {playRow(9, <svg viewBox="0 0 528 52" style={{width:'100%',display:'block'}}><SprKeys88 x0={2} y0={2} kw={10} h={46} middleC={false} sw={0.8}/></svg>, ['the two ends', 'every C'])}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<SpsPaperCheck/>);
  return <>{pages}</>;
}
const spsChkNo = () => { const C = SPS_CHK, nB = C.mech.length + 1, nC = nB + C.first.length, nD = nC + C.does.length, nE = nD + C.pedal.length; return { nB, nC, nD, nE }; };
function SpsPaperCheck() {
  const C = SPS_CHK, { nB, nC, nD, nE } = spsChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:12,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Which keyboard works like this? Circle it.')}
    <BkGrid cols={3} gap="6px 8px">{C.mech.map(([kind], i) => <BkCell key={kind} n={i + 1}>{sdyCol(<><svg viewBox="0 0 130 100" style={{width:'92%',display:'block',margin:'0 auto'}}><SpsMech kind={kind} hl={false}/></svg>
      <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:10,fontSize:14,fontWeight:800,color:BK.ink,marginTop:'auto',paddingTop:6}}>{['harpsichord', 'clavichord', 'piano'].map(w => <span key={w} style={{padding:'0 6px'}}>{w}</span>)}</div></>, '10px 2px 8px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Circle the word that makes each sentence right.')}
    <div style={{display:'grid',gap:6}}>{C.first.map(([a, ws, b], i) => spsInline(nB + i, a, ws, b))}</div>
    {bkSec('C', 'Circle the part each sentence names.')}
    <div style={{display:'grid',gap:9}}>{C.does.map(([s], i) => spsCircleRow(nC + i, s, ['key', 'hammer', 'string', 'damper']))}</div>
    {bkSec('D', 'Which pedal? Circle left, middle or right.')}
    <div style={{display:'grid',gap:9}}>{C.pedal.map(([s], i) => spsCircleRow(nD + i, s, ['left', 'middle', 'right']))}</div>
    {bkSec('E', 'Circle the right answer.')}
    <div style={{display:'grid',gap:6}}>{C.keys.map(([a, ws, b], i) => spsInline(nE + i, a, ws, b))}</div>
  </div>;
}

function SpsTeacher() {
  const W = SPS_WB, C = SPS_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="piano-story" teacher>{content}</WbPage>);
  const at4 = W.parts4.at, { nB, nC, nD, nE } = spsChkNo();
  const marks = { A: C.mech.length, B: C.first.length, C: C.does.length, D: C.pedal.length, E: C.keys.length };
  const total = Object.values(marks).reduce((a, b) => a + b, 0);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('piano-story')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>The instrument itself: the two keyboards before it, the first piano, the action, the pedals, grand and upright (chapter {bkChapterNo('dynamics')}: p and f; chapter {bkChapterNo('pitch-range')}: long, thick strings sound low, the 88 keys). Facts: Cristofori built the first piano in Florence about 1700 (an inventory of the Medici court, 1700; the oldest that survives is from 1720); the name comes from “gravicembalo col piano e forte”. The clavichord’s tangent strikes the string and stays on it while the key is held. On a modern grand the soft pedal shifts the hammers so that most notes are struck on two strings of three; an upright’s left pedal moves the hammers closer to the strings instead. The book draws a grand’s action: in an upright the hammer swings forward to the string and the damper moves back off it. Not here: the eras and how the piano grew (the toolbox’s timeline and eras; the drill’s extra level 9), the composers (chapter {bkChapterNo('composers')}). General knowledge, not an exam requirement at this level. On a digital piano or a smaller keyboard, use the screen pads for the slow press (page 4), the pedals (page 5) and the 88 keys (page 6).</div>
    <TcBlock page={2} title="Before the piano" answers={<>{sscLesson('Play a tune twice: all at one loudness (like a harpsichord), then soft and loud (a piano); the child says which keyboard each sounded like.')}{tcAns('TRY IT', W.how2.map(([id, part], i) => (id === 'upright' ? 'upright piano' : id) + ': a ' + part + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', W.loud2.map(([id, a]) => id + ': ' + a + (id === 'clavichord' ? ' (but always quietly)' : '')), 5)}{tcAns('PLAY', ['the tune three ways'], 8)}</>}
      watch="The clavichord thought to be loud (it is the quietest keyboard). The upright piano thought to work differently (it has hammers too). Pressing harder on a harpsichord thought to help."
      say="“A quill plucks; a tangent pushes and stays; a hammer strikes.”"/>
    <TcBlock page={3} title="The first piano" answers={<>{sscLesson('Say “piano”: the child plays soft; say “forte”: loud. Then a crescendo on C D E F G.')}{tcAns('TRY IT', W.first3.map(([, , , a], i) => a + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', W.order3.map(([w, n]) => w + ' ' + n), 6)}{tcAns('PLAY', ['p, f, then p to f'], 9)}</>}
      watch="Piano read as 'the instrument' only (it also means soft). 1700 mixed up with Mozart's time (the 1780s)."
      say="“Pianoforte: soft and loud.”"/>
    <TcBlock page={4} title="Inside the piano" answers={<>{sscLesson('On an acoustic piano, press a key very slowly with the child watching: no sound. Then quickly: the hammer reaches the string.')}{tcAns('TRY IT', ['A', 'B', 'C', 'D'].map((L, i) => L + ' ' + Object.keys(at4).find(p => at4[p] === L) + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', W.steps4.map(([s, n]) => n + ': ' + s.replace(/\.$/, '')), 5)}{tcAns('PLAY', ['very slowly; hold, then let go'], 9)}</>}
      watch="The damper and the hammer mixed up (the damper rests on the string; the hammer strikes it). Thinking the key itself touches the string."
      say="“The hammer strikes the string; the damper stops the sound.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="The pedals" answers={<>{sscLesson('The child keeps the heel on the floor and presses the right pedal with the right foot, then the left pedal with the left foot.')}{tcAns('TRY IT', W.pedal5.map(([, a], i) => a + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', W.sound5.map(([, a]) => a), 5)}{tcAns('PLAY', ['the right pedal', 'the left pedal'], 9)}</>}
      watch="The right pedal called the 'loud' pedal (it keeps the sound; it does not make it louder). The middle pedal: on an upright it is usually the practice (mute) pedal, on a grand the sostenuto."
      say="“The right pedal keeps the sound; the left pedal softens it.”"/>
    <TcBlock page={6} title="Grand and upright" answers={<>{sscLesson('Count the black-key groups together: seven sets of two and three, and one more black key at the bottom.')}{tcAns('TRY IT', W.kind6.map(([a], i) => a + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', ['dots on the bottom key (A) and the top key (C)', '52', '36', '8'], 5)}{tcAns('PLAY', ['the two ends; every C'], 9)}</>}
      watch="The lowest key thought to be a C. Black keys counted as 35 (the single black key at the bottom is missed)."
      say="“88 keys, from A to C.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.mech.map(([, a]) => a))}
      {tcAns('B', C.first.map(([, , , a]) => a), nB)}
      {tcAns('C', C.does.map(([, a]) => a), nC)}
      {tcAns('D', C.pedal.map(([, a]) => a), nD)}
      {tcAns('E', C.keys.map(([, , , a]) => a), nE)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}; {total} in all. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }]}/>
    <div style={{fontSize:13,color:BK.ink,margin:'0 0 12px',lineHeight:1.6,border:'0.8px solid ' + BK.hair,padding:'10px 14px'}}><b style={{color:BK.coral}}>Lesson time: open the lid.</b> On an upright, lift the top lid; on a grand, look in from the side. The child plays one key at a time and watches its hammer and damper, then holds the right pedal and watches every damper move off the strings.</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'10px 14px',fontSize:13,color:BK.ink,lineHeight:1.6}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: how do the harpsichord and the clavichord sound their strings? 2. Page 3: who built the first piano, where and when; what does its name mean? 3. Page 4: point to each part and say what it does. 4. Page 5: show each pedal and what it does. 5. Page 6: grand or upright; play both ends of the keys. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['piano-story'] = SpsWorkbook;
TEACHER_COPIES['piano-story'] = SpsTeacher;
