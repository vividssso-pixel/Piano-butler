// ─── Phase 464: chapter 8's Workbook (B11: W1 draw the bar lines, W2 write the time signature, W3 mark the strong beats,
// W4 fill the bar, W5 ties: the count with held beats in grey boxes; the check-up on paper) and its Teacher copy.
// English, like every Workbook. Each page faces its Lesson Book page (2 to 6). Staves about 5 mm between lines (Book
// rule 5); every task set (rule 3) and done alone (rule 4).
// a row on paper: top, bars (lists of kinds; '?k' is a box where k belongs), sig: undefined | 'blank' | 'ans',
// end: '||' | 'open' (room to draw the end), show: the '?' kinds drawn (the Teacher copy, a worked example)
function tsPaperItems({ top, bars, sig, end = '||', show }) {
  const out = [['ts', top, sig]];
  bars.forEach((bar, i) => { if (i) out.push(['|']); bar.forEach(k => { if (k[0] === '?') { const kk = k.slice(1); out.push(show ? [kk, NV_ROOM[kk].b] : ['box', NV_ROOM[kk].b]); } else out.push([k, NV_ROOM[k].b]); }); });
  out.push(end === 'open' ? ['sp', 40] : ['||']);
  return out;
}
// a staff at a set size: mm between the lines (5 by default), never wider than its box
function TsPaper({ items, o = {}, mm = 5, label }) {
  const m = tsRaw((d) => dY(d), items, o), vbw = Math.ceil(m.last + 6), px = vbw * mm / 5 * 1.89;
  return <div style={{width:'100%',maxWidth:px,minWidth:0,margin:'0 auto'}}><TsStaff full items={items} o={o} label={label} pad={[o.padTop || 14, tsPadBottom(o)]}/></div>;
}
// the two tied notes' beats, added up (the worked example): '2 + 1'
const tsTieSum = (r) => { const [a, b] = r.ties[0]; const items = tsPaperItems(r); return items[a][1] + ' + ' + items[b][1]; };
const tsNum = (i) => <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink}}>{i}</span>;
// a numbered row; the number stands level with the staff (not the middle of the hearts and boxes under it)
const tsRowN = (n, kids, mm = 4.5, under = true) => <div key={n} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:under ? 'start' : 'center',gap:6}}><span style={{paddingTop:under ? Math.round(34 * mm / 5 * 1.89) - 9 : 0}}>{tsNum(n)}</span>{kids}</div>;
const TS_EN = { w: 'semibreve', h: 'minim', hd: 'dotted minim', q: 'crotchet', p: 'two quavers', r: 'crotchet rest', hr: 'minim rest', wr: 'semibreve rest' };
// words to circle under a cell: the three glyphs
const tsCircle = (kinds, on) => <div style={{display:'flex',justifyContent:'center',gap:6}}>{kinds.map(k => <span key={k} style={{border:'1.5px solid ' + (on === k ? BK.coral : 'transparent'),borderRadius:24,padding:'0 4px',lineHeight:0}}><NvGlyph kind={k} size={46}/></span>)}</div>;

// the Workbook's tasks, fixed so the Teacher copy always matches
const TS_WB = {
  // p2: bar lines (the first row's first bar line drawn: a worked example)
  bl: { top: 3, bars: [['q', 'q', 'q'], ['h', 'q'], ['hd']] },
  bl2: [{ top: 3, bars: [['h', 'q'], ['q', 'q', 'q'], ['q', 'h']] }, { top: 4, bars: [['q', 'q', 'h'], ['w'], ['h', 'q', 'q']] }, { top: 2, bars: [['q', 'q'], ['h'], ['q', 'q'], ['h']] }],
  rep: { top: 3, bars: [['q', 'q', 'q'], ['h', 'q'], ['hd']], end: 'open' },
  // p3: the time signature (the first one written: a worked example)
  sig1: [{ top: 3, bars: [['q', 'q', 'q']] }, { top: 2, bars: [['h']] }],
  sig2: [{ top: 4, bars: [['h', 'q', 'q']] }, { top: 3, bars: [['hd']] }, { top: 2, bars: [['q', 'q']] }, { top: 4, bars: [['w']] }],
  sig3: [{ top: 3, bars: [['h', 'q'], ['q', 'q', 'q']] }, { top: 4, bars: [['q', 'q', 'h'], ['hd', 'q']] }],
  // p4: strong beats (the first heart coloured: a worked example)
  st1: { top: 3, bars: [['q', 'q', 'q'], ['q', 'q', 'q'], ['q', 'q', 'q']] },
  st2: [{ top: 2, bars: [['q', 'q'], ['h'], ['q', 'q'], ['h']] }, { top: 4, bars: [['q', 'q', 'q', 'q'], ['q', 'q', 'q', 'q']] }],
  st3: { top: 4, bars: [['q', 'q', 'q', 'q'], ['h', 'q', 'q']] },
  // p5: fill the bar (circle; draw the rest; count)
  f1: [{ top: 4, bars: [['q', 'q', '?h']], ch: ['q', 'h', 'w'] }, { top: 3, bars: [['?hd']], ch: ['h', 'w', 'hd'] }],
  f2: [{ top: 4, bars: [['q', '?r', 'h']] }, { top: 4, bars: [['h', '?hr']] }, { top: 3, bars: [['q', 'q', '?r']] }, { top: 4, bars: [['?wr']] }],
  f3: { top: 3, bars: [['q', 'r', 'q'], ['h', 'r'], ['hd']] },
  // p6: ties (how long; the count; draw one)
  t1: [{ top: 3, bars: [['q', 'h'], ['q', 'h']], ties: [[2, 4]], ans: 3 }, { top: 4, bars: [['h', 'h'], ['w']], ties: [[2, 4]], ans: 6 }],
  t2: [{ top: 4, bars: [['q', 'h', 'q'], ['q', 'q', 'h']], ties: [[3, 5]] }, { top: 3, bars: [['hd'], ['q', 'h']], ties: [[1, 3]] }],
  t3: { top: 4, bars: [['q', 'q', 'h'], ['h', 'h']], ties: [[3, 5]] },
};
const TS_CHK = {
  bl: { top: 4, bars: [['h', 'q', 'q'], ['q', 'q', 'h'], ['w']] },
  sig: [{ top: 4, bars: [['hd', 'q']] }, { top: 2, bars: [['q', 'q']] }],
  st: { top: 2, bars: [['q', 'q'], ['h'], ['q', 'q']] },
  fill: [{ top: 4, bars: [['?hr', 'h']] }, { top: 3, bars: [['h', '?r']] }],
  tie: [{ top: 3, bars: [['q', 'q', 'q'], ['hd']], ties: [[3, 5]], ans: 4 }, { top: 2, bars: [['q', 'q'], ['h']], ties: [[2, 4]], ans: 3 }],
};
// the beats at which each bar starts (for the answers)
const tsBarStarts = (r) => { let b = 0; return r.bars.slice(0, -1).map(bar => (b += bar.reduce((a, k) => a + NV_ROOM[k.replace('?', '')].b, 0))); };
const tsBeatsOf = (r) => r.bars.reduce((a, bar) => a + bar.reduce((x, k) => x + NV_ROOM[k.replace('?', '')].b, 0), 0);

function TsWorkbook({ startNo = 1 }) {
  const W = TS_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="time-signatures">{content}</WbPage>);

  // 2 (faces "Bars and bar lines")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Draw the bar lines" how="Count the beats. Draw a bar line every time you reach 3. The first one is drawn.">
      {tsRowN(1, <TsPaper mm={4.5} items={tsPaperItems(W.bl)} o={{ D: 22, noBars: true, exBars: 1, hearts: false }}/>, 4.5, false)}
    </Part>
    <Part kind="home" title="More bar lines" how="Draw a bar line every time the beats reach the top number.">
      <div style={{display:'grid',gap:14}}>{W.bl2.map((r, i) => tsRowN(i + 2, <TsPaper mm={4.2} items={tsPaperItems(r)} o={{ D: r.top === 4 ? 17 : 20, noBars: true, hearts: false }}/>, 4.2, false))}</div>
    </Part>
    <Part kind="play" title="Draw the repeat sign" how="After bar 3, draw two dots in the middle two spaces, then a thin line and a thick line. Right hand, finger 3 on G: play the three bars twice, counting 1 2 3.">
      {tsRowN(5, <TsPaper mm={5} items={tsPaperItems(W.rep)} o={{ D: 22, hearts: false }}/>, 5, false)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The two numbers")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Write the time signature" how="Count the beats in the bar. Write the top number, and 4 under it. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.sig1.map((r, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'10px 4px 0'}}><TsPaper mm={4.5} items={tsPaperItems({ ...r, sig: i === 0 ? 'ans' : 'blank' })} o={{ D: 34, hearts: false }}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="More time signatures" how="Write the time signature for each bar.">
      <BkGrid cols={2} gap="8px 14px">{W.sig2.map((r, i) => <ExCell key={i} n={i + 3}><div style={{padding:'10px 4px 0'}}><TsPaper mm={4.5} items={tsPaperItems({ ...r, sig: 'blank' })} o={{ D: 30, hearts: false }}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Write it, then play it" how="Write the time signature. Then right hand, finger 3 on G: play it, counting out loud.">
      <div style={{display:'grid',gap:5}}>{W.sig3.map((r, i) => tsRowN(7 + i, <TsPaper mm={4.1} items={tsPaperItems({ ...r, sig: 'blank' })} o={{ D: 30, hearts: false }}/>, 4.1, false))}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Strong and weak beats")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Colour the strong beats" how="Colour the heart under beat 1 of every bar. The first one is coloured.">
      {tsRowN(1, <TsPaper mm={3.6} items={tsPaperItems(W.st1)} o={{ D: 30, hearts: 'outline', counts: false, fill: [0] }}/>, 3.6)}
    </Part>
    <Part kind="home" title="More strong beats" how="Colour the heart under every strong beat: beat 1 of every bar.">
      <div style={{display:'grid',gap:14}}>{W.st2.map((r, i) => tsRowN(i + 2, <TsPaper mm={3.6} items={tsPaperItems(r)} o={{ D: 30, hearts: 'outline', counts: false }}/>, 3.6))}</div>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the beat number in every box. A grey box is a beat you hold: write it too. Then right hand, finger 3 on G: play it, beat 1 a little louder.">
      {tsRowN(4, <TsPaper mm={3.6} items={tsPaperItems(W.st3)} o={{ D: 36, strong: true, mid: true, counts: 'boxes' }}/>, 3.6)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Fill the bar")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Which one fills the box?" how="Circle the note that fills the box. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.f1.map((r, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'10px 2px 2px'}}><TsPaper mm={4} items={tsPaperItems(r)} o={{ D: 30, hearts: false }}/>{tsCircle(r.ch, i === 0 ? r.bars[0].find(k => k[0] === '?').slice(1) : null)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the rest" how="Draw the rest that fills each box: a crotchet rest, a minim rest or a semibreve rest.">
      <BkGrid cols={2} gap="8px 14px">{W.f2.map((r, i) => <ExCell key={i} n={i + 3}><div style={{padding:'10px 4px 0'}}><TsPaper mm={4.5} items={tsPaperItems(r)} o={{ D: 30, hearts: false }}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the beat number in every box: a dashed box is a rest, a grey box a held beat. Then right hand, finger 3 on G: play it, counting out loud.">
      {tsRowN(7, <TsPaper mm={3.6} items={tsPaperItems(W.f3)} o={{ D: 34, counts: 'boxes' }}/>, 3.6)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "The tie")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="How long is the tied G?" how="Add up the two tied notes. Write how many beats G sounds. The first one is done.">
      <div style={{display:'grid',gap:10}}>{W.t1.map((r, i) => <div key={i} style={{display:'grid',gridTemplateColumns:'24px 1fr auto',alignItems:'center',gap:10}}>{tsNum(i + 1)}<TsPaper mm={3.6} items={tsPaperItems(r)} o={{ D: 28, hearts: false, ties: r.ties }}/>
        <span style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:12,fontWeight:800,color:BK.ink}}>{i === 0 ? <>{bkHand(String(r.ans), 38, 32)} beats <span style={{color:BK.coral,fontStyle:'italic',fontWeight:900}}>({tsTieSum(r)})</span></> : <>{bkBox(38, 32)} beats</>}</span></div>)}</div>
    </Part>
    <Part kind="home" title="Count the tie" how="Write the beat number in every box. A grey box is a held or tied beat: write it too.">
      <div style={{display:'grid',gap:12}}>{W.t2.map((r, i) => tsRowN(i + 3, <TsPaper mm={3.3} items={tsPaperItems(r)} o={{ D: 34, ties: r.ties, counts: 'boxes' }}/>, 3.3))}</div>
    </Part>
    <Part kind="play" title="Draw a tie, then play it" how="Draw a tie under the notes, from the minim at the end of bar 1 to the first minim of bar 2. Right hand, finger 3 on G: play the two bars; G sounds for 4 beats.">
      {tsRowN(5, <TsPaper mm={4.5} items={tsPaperItems(W.t3)} o={{ D: 34, hearts: false }}/>, 4.5, false)}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<TsPaperCheck/>);
  return <>{pages}</>;
}
function TsPaperCheck() {
  const C = TS_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Draw the bar lines: a bar line every time the beats reach the top number.')}
    <BkCell n={1}><div style={{padding:'6px 4px 0'}}><TsPaper mm={3.9} items={tsPaperItems(C.bl)} o={{ D: 15, noBars: true, hearts: false }}/></div></BkCell>
    {bkSec('B', 'Write the time signature for each bar.')}
    <BkGrid cols={2} gap="6px 10px">{C.sig.map((r, i) => <BkCell key={i} n={i + 2}><div style={{padding:'6px 4px 0'}}><TsPaper mm={3.6} items={tsPaperItems({ ...r, sig: 'blank' })} o={{ D: 30, hearts: false }}/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Colour the heart under every strong beat.')}
    <BkCell n={4}><div style={{padding:'6px 4px 0'}}><TsPaper mm={3.2} items={tsPaperItems(C.st)} o={{ D: 28, hearts: 'outline', counts: false }}/></div></BkCell>
    {bkSec('D', 'Draw the rest that fills each box.')}
    <BkGrid cols={2} gap="6px 10px">{C.fill.map((r, i) => <BkCell key={i} n={i + 5}><div style={{padding:'6px 4px 0'}}><TsPaper mm={4.2} items={tsPaperItems(r)} o={{ D: 30, hearts: false }}/></div></BkCell>)}</BkGrid>
    {bkSec('E', 'How many beats does the tied G sound?')}
    <div style={{display:'grid',gap:6}}>{C.tie.map((r, i) => <BkCell key={i} n={i + 7}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:8,padding:'8px 4px 4px'}}><TsPaper mm={3.2} items={tsPaperItems(r)} o={{ D: 30, hearts: false, ties: r.ties }}/>
      <span style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:12,fontWeight:800,color:BK.ink}}>{bkBox(36, 30)} beats</span></div></BkCell>)}</div>
  </div>;
}

const tcLesson = (txt) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginBottom:4}}><b style={{color:BK.coral}}>In the lesson</b>{'  '}{txt}</div>;
function TsTeacher() {
  const W = TS_WB, C = TS_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="time-signatures" teacher>{content}</WbPage>);
  const after = (r) => 'after beat' + (tsBarStarts(r).length > 1 ? 's ' : ' ') + tsBarStarts(r).join(', ');
  const sigTxt = (r) => r.top + '/4';
  const strong = (r) => 'hearts ' + [0, ...tsBarStarts(r)].map(b => b + 1).join(', ');
  // the count: (n) a rest's beat, [n] a held or tied beat
  const cnt = (r) => { const tiedIn = new Set((r.ties || []).map(([, b]) => b)); const out = []; let b = 0, idx = 1;
    r.bars.forEach((bar, bi) => { if (bi) idx++; bar.forEach(k0 => { const k = k0.replace('?', ''), n = NV_ROOM[k].b; for (let i = 0; i < n; i++) { const no = String(b % r.top + 1); out.push(tsIsRest(k) ? '(' + no + ')' : i > 0 || (i === 0 && tiedIn.has(idx)) ? '[' + no + ']' : k === 'p' ? no + ' +' : no); b++; } idx++; }); });
    return out.join(' '); };
  const blank = (r) => TS_EN[r.bars.flat().find(k => k[0] === '?').slice(1)];
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('time-signatures')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Each Workbook page faces its Lesson Book page. Every rhythm is on G (line 2 of the treble clef), right hand finger 3. The book counts <b>1 2 3 4</b>, and <b>1 +</b> for two quavers. Beat 1 is strong; in 4/4 beat 3 is medium. Not yet: the anacrusis (AMEB Grade 1) and grouping quavers, duplets and triplets (chapter {bkChapterNo('rhythm')}); duple, triple and quadruple; cut time, 6/8 and the bottom numbers 2 and 8 (drill levels 8 to 10, each showing its rule); the whole-bar rest in 2/4 and 3/4 (level 7); the slur (chapter {bkChapterNo('dynamics')}); the start repeat and first and second endings. AMEB Theory: 2/4, 3/4, 4/4, C, the tie, the bar line and the double bar line at Grade 1; the repeat sign and the whole-bar rest at Grade 2.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: pat the 1.</b> March in 2/4 and 4/4; sway in 3/4. Pat your knees on every 1 and clap the other beats, counting out loud. In the count below, (n) is a rest's beat and [n] a held or tied beat.</div>
    <TcBlock page={2} title="Bars and bar lines" answers={<>{tcLesson('Play the repeat line with the child; at the dots, point back to bar 1 and say “back!”. The count never stops. Ask: how many bars did you play? (4)')}{tcAns('TRY IT', [after(W.bl)])}{tcAns('YOUR TURN', W.bl2.map(after), 2)}{tcAns('PLAY', ['two dots, then a thin and a thick line at the end; play the three bars twice'], 5)}</>}
      watch="Counting on past the top number instead of starting again at 1. A bar line after every note instead of after every bar. At the repeat sign: playing it only once. On paper: repeat dots on the lines or after the double bar line; bar lines that do not reach from the top line to the bottom line."
      say="“Count to the top number, then a bar line, then start again at 1.”"/>
    <TcBlock page={3} title="The two numbers" answers={<>{tcLesson('Point to the four staves in a mixed order; the child says the top number before playing.')}{tcAns('TRY IT', W.sig1.map(sigTxt))}{tcAns('YOUR TURN', W.sig2.map(sigTxt), 3)}{tcAns('PLAY', W.sig3.map(sigTxt), 7)}</>}
      watch="The numbers swapped, or a fraction line drawn between them: a time signature has none. Counting the notes instead of the beats: a bar with one minim written as 1/4."
      say="“Top: how many beats. Bottom 4: crotchets.”"/>
    <TcBlock page={4} title="Strong and weak beats" answers={<>{tcLesson('Clap the 4/4 line: ONE two THREE four, beat 3 less than beat 1.')}{tcAns('TRY IT', [strong(W.st1)])}{tcAns('YOUR TURN', W.st2.map(strong), 2)}{tcAns('PLAY', [cnt(W.st3)], 4)}</>}
      watch="Every beat loud, or the weak beats rushed. In 4/4, beat 3 louder than beat 1. A count that is not steady; a pause before every beat 1."
      say="“Big heart, small hearts: ONE two three.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Fill the bar" answers={<>{tcLesson('The child whispers the circled numbers (the rests) and says the others out loud. Online, Build a bar refuses what an exam marks wrong: in 4/4 silent beats 1 and 2, or 3 and 4, are one minim rest, and a whole silent bar is the semibreve rest.')}{tcAns('TRY IT', W.f1.map(blank))}{tcAns('YOUR TURN', W.f2.map(blank), 3)}{tcAns('PLAY', [cnt(W.f3)], 7)}</>}
      watch="Stopping the count in a rest, so the next note comes early. The minim rest and the semibreve rest swapped: the minim rest sits on line 3, the semibreve rest hangs from line 4. A crotchet rest drawn as a 7 (that is a quaver rest). A bar with a beat too many."
      say="“Fill the bar: count every beat, the silent ones too.”"/>
    <TcBlock page={6} title="The tie" answers={<>{tcLesson('Play both lines while the child closes their eyes: which one had G once? Then swap.')}{tcAns('TRY IT', W.t1.map(r => r.ans + ' beats'))}{tcAns('YOUR TURN', W.t2.map(cnt), 3)}{tcAns('PLAY', ['a tie from the minim at the end of bar 1 to the first minim of bar 2, under the noteheads; G sounds for 4 beats'], 5)}</>}
      watch="Letting go of the tied note early, or playing it again on the next beat. Counting the tied beats in silence and losing the place. A tie drawn over the stems or from stem to stem: it goes from notehead to notehead, under the notes. A tie joins the same note; a curve between different notes is a slur."
      say="“Play once, hold through the tie, keep counting.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', [after(C.bl)])}
      {tcAns('B', C.sig.map(sigTxt), 2)}
      {tcAns('C', [strong(C.st)], 4)}
      {tcAns('D', C.fill.map(blank), 5)}
      {tcAns('E', C.tie.map(r => r.ans + ' beats'), 7)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. A section with any wrong answer is not passed yet: go back to its page below. The paper shows the idea; the beat itself is heard: also listen to the student count and play (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: 1, page: 2 }, { id: 'b', step: 2, page: 3 }, { id: 'c', step: 3, page: 4 }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: point to a bar line, the double bar line and the repeat sign; play the repeat line, four bars. 2. Any staff on page 3: say the top number, then play two bars counting out loud. 3. Page 4, the 4/4 line: beat 1 a little louder, the count steady. 4. Page 5, the 3/4 line, the rest counted too. 5. Page 6, the top line: G once, held into bar 2. Got it! means right the first time, with a steady count.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['time-signatures'] = TsWorkbook;
TEACHER_COPIES['time-signatures'] = TsTeacher;
