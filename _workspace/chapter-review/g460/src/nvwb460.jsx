// ─── Phase 460: chapter 5's Workbook (B11: W1 name it and write its beats, W2 sound lines over the hearts, W3 the count
// with held beats in grey boxes, W4 1 + 2 + under quaver pairs, W5 the count under every beat, rests too; the check-up on
// paper) and its Teacher copy. English, like every Workbook. Each page faces its Lesson Book page (2 to 6). ───
// a bar on paper, drawn like the book. notes: 'show' | 'trace' (pale, to draw over) | 'none'; lines: 'show' | 'guide' (a
// dotted line to draw the sound lines on) | 'none'; count: 'show' | 'boxes' | 'ans' (a worked example) | 'none';
// words: 'show' (walk / run-ning under each note) | 'none'
function NvPaperBar({ row, D = 84, notes = 'show', lines = 'show', count = 'show', words = 'none', hearts = true, maxW = 380 }) {
  const n = nvBeats(row), P = 10, W = P * 2 + n * D, H = (b) => P + D * (b + 0.5);
  const yN = 50, yL = 66, yW = 86, yH = words === 'show' ? 104 : 84, yC = yH + 34, HT = !hearts ? (words === 'show' ? yW + 8 : yL + 8) : count === 'none' ? yH + 12 : yC + 10;
  const raw = [], els = [], held = new Set(), rest = new Set(), pairAt = new Set();
  let b = 0;
  row.forEach(([k, len], j) => {
    if (k === 'p') { raw.push(nvbPair(H(b) - 15, H(b) + 11, yN, { k: 0.92 }).svg); pairAt.add(b); }
    else if (k === 'r') { raw.push(nvbRest(H(b) + 1, yN - 12, 'q').svg); rest.add(b); }
    else if (k === 'hr' || k === 'wr') { const xm = (H(b) + H(b + len - 1)) / 2; raw.push(nvbRest(xm, k === 'hr' ? yN - 2 : yN - 14, k === 'hr' ? 'h' : 'w', { k: 1.3 }).svg); for (let i = 0; i < len; i++) rest.add(b + i); }
    else { raw.push(nvbNote(k === 'w' ? H(b) - 1 : H(b) - 3, yN, k === 'hd' ? 'h' : k, { dot: k === 'hd' }).svg); for (let i = 1; i < len; i++) held.add(b + i); }
    if (words === 'show' && !nvRestKind(k)) els.push(<text key={'w' + j} x={H(b)} y={yW} textAnchor="middle" fontSize="13.5" fontWeight="900" fill={BK.ink}>{k === 'p' ? 'run-ning' : 'walk'}</text>);
    b += len;
  });
  if (lines === 'show') nvSounds(row).forEach((s, k) => {
    const pr = row[s.j][0] === 'p', B = Math.floor(s.b);
    const x0 = pr ? (s.h ? H(B) + 3 : H(B) - D / 2 + 6) : H(s.b) - D / 2 + 6, x1 = pr ? (s.h ? H(B) + D / 2 - 6 : H(B) - 3) : H(s.b + s.d - 1) + D / 2 - 6;
    els.push(<line key={'l' + k} x1={x0} x2={x1} y1={yL} y2={yL} stroke={BK.coral} strokeWidth="4" strokeLinecap="round"/>);
  });
  if (lines === 'guide') els.push(<line key="g" x1={P + 4} x2={W - P - 4} y1={yL} y2={yL} stroke={BK.muted} strokeWidth="1" strokeDasharray="2 3"/>);
  for (let i = 0; i < n; i++) {
    const x = H(i), pr = pairAt.has(i);
    if (!hearts) continue;
    els.push(<path key={'h' + i} d="M0 5 Q-7.5 -0.5 -5 -4.2 Q-2.4 -6.8 0 -3 Q2.4 -6.8 5 -4.2 Q7.5 -0.5 0 5 Z" transform={'translate(' + x + ' ' + yH + ') scale(1.6)'} fill={BK.coral}/>);
    if (count === 'none') continue;
    const cells = pr ? [[x - 16, String(i % 4 + 1)], [x + 15, '+']] : [[x, String(i % 4 + 1)]];
    cells.forEach(([cx, txt], c) => {
      const bw = pr ? 28 : 32, lightNo = held.has(i);
      if (count === 'show') els.push(<text key={'c' + i + c} x={cx} y={yC} textAnchor="middle" fontSize="17" fontWeight="900" fill={lightNo ? 'rgba(38,41,107,0.38)' : BK.ink}>{txt}</text>);
      else {
        els.push(<rect key={'b' + i + c} x={cx - bw / 2} y={yC - 23} width={bw} height="32" rx="3" fill={lightNo ? 'rgba(38,41,107,0.11)' : '#fff'} stroke={count === 'ans' ? BK.coral : BK.line} strokeWidth="1.5" strokeDasharray={rest.has(i) ? '3.4 2.8' : undefined}/>);
        if (count === 'ans') els.push(<text key={'a' + i + c} x={cx} y={yC - 1} textAnchor="middle" fontSize="16" fontWeight="900" fontStyle="italic" fill={lightNo ? 'rgba(228,87,46,0.55)' : BK.coral}>{txt}</text>);
      }
    });
  }
  return <svg viewBox={'0 0 ' + W + ' ' + HT} style={{width:'100%',maxWidth:maxW,display:'block',margin:'0 auto'}}>
    {notes !== 'none' && <g opacity={notes === 'trace' ? 0.2 : 1} dangerouslySetInnerHTML={{ __html: raw.join('') }}/>}
    {els}
  </svg>;
}
// words to circle (a box for a word is replaced by words to circle, Book rule 5)
const nvChoose = (words, on) => <span style={{display:'inline-flex',gap:3,flexWrap:'nowrap'}}>{words.map(w => <span key={w} style={{fontSize:12,fontWeight:800,color:on === w ? BK.coral : BK.ink,border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:12,padding:'0 5px',lineHeight:'19px',whiteSpace:'nowrap'}}>{w}</span>)}</span>;
const nvNameEn = { w: 'semibreve', h: 'minim', hd: 'dotted minim', q: 'crotchet', p: 'two quavers', r: 'crotchet rest', hr: 'minim rest', wr: 'semibreve rest' };
const NV_BEATS = { w: 4, h: 2, hd: 3, q: 1, p: 1, r: 1, hr: 2, wr: 4 };
// a single note: words to circle (its name), and a box for its beats
function NvNameCell({ k, n, ex, words, beats = true }) {
  return <ExCell n={n} ex={ex}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3,padding:'4px 2px 0'}}>
    <NvGlyph kind={k} size={46}/>
    {words && <div style={{display:'flex',justifyContent:'center'}}>{nvChoose(words, ex ? nvNameEn[k] : null)}</div>}
    {beats && <span style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:12,fontWeight:800,color:BK.ink}}>beats {ex ? bkHand(String(NV_BEATS[k]), 36, 30) : bkBox(36, 30)}</span>}
  </div></ExCell>;
}
const nvNum = (i) => <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14,color:BK.ink}}>{i}</span>;
const nvBarCell = (row, i, n0, ex, o) => <ExCell key={i} n={n0 + i} ex={ex}><div style={{padding:'14px 2px 0'}}><NvPaperBar row={row} {...o(ex)}/></div></ExCell>;

// the Workbook's tasks, fixed so the Teacher copy always matches
const NV_WB = {
  // p2: crotchets
  trace: [[['q', 1], ['q', 1], ['q', 1], ['q', 1]], [['q', 1], ['q', 1], ['q', 1], ['q', 1]]],
  howMany: [3, 1, 4, 2],
  lines2: [[['q', 1], ['q', 1], ['q', 1], ['q', 1]], [['q', 1], ['q', 1], ['q', 1], ['q', 1]]],
  // p3: minims
  qh: ['h', 'q', 'q', 'h', 'h', 'q', 'h', 'q'],
  lines3: [[['h', 2], ['h', 2]], [['q', 1], ['q', 1], ['h', 2]], [['h', 2], ['q', 1], ['q', 1]], [['q', 1], ['q', 1], ['q', 1], ['q', 1]]],
  count3: [[['q', 1], ['q', 1], ['h', 2]], [['h', 2], ['h', 2]]],
  // p4: longer notes
  beats4: ['hd', 'w', 'q', 'h', 'w', 'hd', 'h', 'q'],
  lines4: [[['hd', 3], ['q', 1]], [['w', 4]], [['q', 1], ['hd', 3]], [['h', 2], ['h', 2]]],
  count4: [[['hd', 3], ['q', 1]], [['w', 4]]],
  // p5: quavers
  walkRun: ['p', 'q', 'q', 'p', 'p', 'q', 'p', 'q'],
  plus: [[['q', 1], ['p', 1], ['q', 1], ['p', 1]], [['p', 1], ['p', 1], ['q', 1], ['q', 1]], [['p', 1], ['q', 1], ['h', 2]], [['q', 1], ['q', 1], ['p', 1], ['q', 1]]],
  fromWords: [[['q', 1], ['q', 1], ['p', 1], ['q', 1]], [['p', 1], ['q', 1], ['p', 1], ['q', 1]]],
  // p6: rests
  match: { notes: ['q', 'w', 'h'], rests: ['hr', 'r', 'wr'] },
  restCount: [[['q', 1], ['q', 1], ['r', 1], ['q', 1]], [['h', 2], ['hr', 2]], [['r', 1], ['q', 1], ['q', 1], ['q', 1]], [['q', 1], ['q', 1], ['hr', 2]]],
  draw: ['hr', 'wr', 'wr', 'hr'],
};
const NV_CHK = {
  name: ['hd', 'q', 'w', 'h', 'w', 'q'],
  lines: [[['h', 2], ['q', 1], ['q', 1]], [['hd', 3], ['q', 1]]],
  count: [[['q', 1], ['h', 2], ['q', 1]], [['w', 4]]],
  plus: [[['p', 1], ['q', 1], ['p', 1], ['q', 1]], [['q', 1], ['p', 1], ['p', 1], ['q', 1]]],
  rests: [[['q', 1], ['r', 1], ['hr', 2]], [['wr', 4]]],
};
// draw a line from each note to its rest; ex: the first line drawn
function NvMatch({ notes, rests, ex }) {
  const G = 66, x0 = 40, x1 = 370, y = (i) => 2 + i * G;
  const right = { q: 'r', h: 'hr', w: 'wr' };
  const j0 = rests.indexOf(right[notes[0]]);
  return <svg viewBox={'0 0 460 ' + (G * notes.length)} style={{width:'100%',maxWidth:310,display:'block',margin:'0 auto'}}>
    {notes.map((k, i) => <g key={'n' + i}><svg x={x0} y={y(i)} width="84" height="70" viewBox="0 10 80 66" dangerouslySetInnerHTML={{ __html: nvGlyphRaw(k) }}/><circle cx={x0 + 110} cy={y(i) + 36} r="5" fill={BK.ink}/></g>)}
    {rests.map((k, i) => <g key={'r' + i}><circle cx={x1 - 26} cy={y(i) + 36} r="5" fill={BK.ink}/><svg x={x1} y={y(i)} width="84" height="70" viewBox="0 10 80 66" dangerouslySetInnerHTML={{ __html: nvGlyphRaw(k) }}/></g>)}
    {ex && <line x1={x0 + 110} y1={y(0) + 36} x2={x1 - 26} y2={y(j0) + 36} stroke={BK.coral} strokeWidth="2.6" strokeLinecap="round"/>}
  </svg>;
}
// five lines to draw a rest on: numbered from the bottom, as on Lesson Book page 6
function NvFiveLines({ k, ex }) {
  const G = 12, y5 = 66, x0 = 30, x1 = 160;
  return <svg viewBox="0 0 180 76" style={{width:'100%',maxWidth:180,display:'block',margin:'0 auto'}}>
    {[0, 1, 2, 3, 4].map(i => <g key={i}><line x1={x0} x2={x1} y1={y5 - i * G} y2={y5 - i * G} stroke={BK.ink} strokeWidth="1.3"/><text x={x0 - 10} y={y5 - i * G + 4} textAnchor="middle" fontSize="10" fontWeight="900" fill={BK.muted}>{i + 1}</text></g>)}
    {ex && <rect x={(x0 + x1) / 2 - 12} y={k === 'hr' ? y5 - 2 * G - 6 : y5 - 3 * G} width="24" height="6" fill={BK.coral}/>}
  </svg>;
}

function NvWorkbook({ startNo = 1 }) {
  const W = NV_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="note-values">{content}</WbPage>);

  // 2 (faces "The crotchet: one beat")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Draw crotchets" how="Trace the pale crotchets in 1. Then draw a crotchet over every heart in 2.">
      <BkGrid cols={2} gap="8px 12px">{W.trace.map((row, i) => nvBarCell(row, i, 1, false, () => ({ notes: i === 0 ? 'trace' : 'none', lines: 'none', count: 'show' })))}</BkGrid>
    </Part>
    <Part kind="home" title="How many beats?" how="Write how many beats each row lasts.">
      <BkGrid cols={4} gap="8px 10px">{W.howMany.map((c, i) => <ExCell key={i} n={i + 3}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6,padding:'14px 2px 2px'}}>
        <NvPaperBar row={Array.from({ length: c }, () => ['q', 1])} D={30} lines="none" count="none" hearts={false} maxW={30 * c + 20}/>
        <span style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:12,fontWeight:800,color:BK.ink}}>beats {bkBox(36, 30)}</span></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Draw the sound lines" how="Draw each crotchet's sound line, one heart long. Then play it on middle C, right hand finger 1, counting out loud.">
      <div style={{display:'grid',gap:18}}>{W.lines2.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{nvNum(7 + r)}<NvPaperBar row={row} lines="guide" maxW={470}/></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The minim: two beats")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Crotchet or minim?" how="Circle its name. Then write how many beats it lasts.">
      <BkGrid cols={4} gap="8px 10px">{W.qh.map((k, i) => <NvNameCell key={i} k={k} n={i + 1} ex={i === 0} words={['crotchet', 'minim']}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the sound lines" how="Draw each note's sound line on the dotted line: one heart or two.">
      <BkGrid cols={2} gap="8px 12px">{W.lines3.map((row, i) => nvBarCell(row, i, 9, false, () => ({ lines: 'guide', count: 'none' })))}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the count in every box, grey ones too. A grey box is a beat you hold. Then play it on middle C, counting out loud.">
      <div style={{display:'grid',gap:16}}>{W.count3.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{nvNum(13 + r)}<NvPaperBar row={row} count="boxes" maxW={278}/></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Longer notes: 3 and 4 beats")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="How many beats?" how="Write how many beats each note lasts: 1, 2, 3 or 4.">
      <BkGrid cols={4} gap="8px 10px">{W.beats4.map((k, i) => <NvNameCell key={i} k={k} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the sound lines" how="Draw each note's sound line on the dotted line, as long as its beats.">
      <BkGrid cols={2} gap="8px 12px">{W.lines4.map((row, i) => nvBarCell(row, i, 9, false, () => ({ lines: 'guide', count: 'none' })))}</BkGrid>
    </Part>
    <Part kind="play" title="Count it, then play it" how="Write the count in every box, grey ones too. A grey box is a beat you hold. Then play it on middle C, counting out loud.">
      <div style={{display:'grid',gap:16}}>{W.count4.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{nvNum(13 + r)}<NvPaperBar row={row} count="boxes" maxW={340}/></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Two quavers on one beat")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Walk or run-ning?" how="Circle walk or run-ning for each one.">
      <BkGrid cols={4} gap="8px 10px">{W.walkRun.map((k, i) => <NvNameCell key={i} k={k} n={i + 1} ex={i === 0} words={['walk', 'run-ning']} beats={false}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write 1 + 2 +" how="Write the count under every heart. Under two quavers, write the beat's number and then +.">
      <BkGrid cols={2} gap="8px 12px">{W.plus.map((row, i) => nvBarCell(row, i, 9, false, () => ({ count: 'boxes' })))}</BkGrid>
    </Part>
    <Part kind="play" title="Notes from words" how="Over each word, draw a crotchet for walk or two quavers for run-ning. Then clap it, saying the words.">
      <div style={{display:'grid',gap:14}}>{W.fromWords.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{nvNum(13 + r)}<NvPaperBar row={row} notes="none" lines="none" words="show" count="none" maxW={345}/></div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Rests: silence you count")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Note and rest" how="Draw a line from each note to the rest that lasts just as long. The first one is done.">
      <ExCell n={1}><div style={{padding:'12px 4px 2px'}}><NvMatch notes={W.match.notes} rests={W.match.rests} ex/></div></ExCell>
    </Part>
    <Part kind="home" title="Count every beat, rests too" how="Write the count under every heart. A dashed box is a rest: count it too.">
      <BkGrid cols={2} gap="8px 12px">{W.restCount.map((row, i) => nvBarCell(row, i, 2, false, () => ({ count: 'boxes' })))}</BkGrid>
    </Part>
    <Part kind="play" title="Draw the rests" how="Draw the rest named in each box on the five lines.">
      <BkGrid cols={2} gap="8px 12px">{W.draw.map((k, i) => <ExCell key={i} n={i + 6}><div style={{display:'grid',gap:4,justifyItems:'center',padding:'16px 4px 4px'}}>
        <span style={{fontSize:13,fontWeight:900,color:BK.ink}}>{k === 'hr' ? 'a minim rest' : 'a semibreve rest'}</span><NvFiveLines k={k}/></div></ExCell>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<NvPaperCheck/>);
  return <>{pages}</>;
}
function NvPaperCheck() {
  const C = NV_CHK;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Circle each note\'s name. Write how many beats it lasts.')}
    <BkGrid cols={3} gap="6px 10px">{C.name.map((k, i) => <BkCell key={i} n={i + 1}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:3,padding:'4px 2px 0'}}><NvGlyph kind={k} size={44}/>
      <div style={{display:'flex',justifyContent:'center'}}>{nvChoose(k === 'q' || k === 'h' ? ['crotchet', 'minim'] : ['dotted minim', 'semibreve'], null)}</div>
      <span style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:12,fontWeight:800,color:BK.ink}}>beats {bkBox(36, 30)}</span></div></BkCell>)}</BkGrid>
    {bkSec('B', 'Draw each note\'s sound line on the dotted line, as long as its beats.')}
    <BkGrid cols={2} gap="6px 10px">{C.lines.map((row, i) => <BkCell key={i} n={i + 7}><div style={{padding:'12px 2px 0'}}><NvPaperBar row={row} lines="guide" count="none"/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Write the count under every heart. A grey box is a beat you hold.')}
    <BkGrid cols={2} gap="6px 10px">{C.count.map((row, i) => <BkCell key={i} n={i + 9}><div style={{padding:'12px 2px 0'}}><NvPaperBar row={row} count="boxes"/></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Write the count. Under two quavers, write the beat\'s number and then +.')}
    <BkGrid cols={2} gap="6px 10px">{C.plus.map((row, i) => <BkCell key={i} n={i + 11}><div style={{padding:'12px 2px 0'}}><NvPaperBar row={row} count="boxes"/></div></BkCell>)}</BkGrid>
    {bkSec('E', 'Write the count under every heart, the rests too.')}
    <BkGrid cols={2} gap="6px 10px">{C.rests.map((row, i) => <BkCell key={i} n={i + 13}><div style={{padding:'12px 2px 0'}}><NvPaperBar row={row} count="boxes"/></div></BkCell>)}</BkGrid>
  </div>;
}

function NvTeacher() {
  const W = NV_WB, C = NV_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="note-values" teacher>{content}</WbPage>);
  const lineTxt = (row) => row.map(([k, n]) => nvNameEn[k] + ' ' + n + (n === 1 ? ' heart' : ' hearts')).join(', ');
  const cnt = (row) => { const out = []; let b = 0; row.forEach(([k, len]) => { for (let i = 0; i < len; i++) { const no = String(b % 4 + 1); out.push(nvRestKind(k) ? '(' + no + ')' : i > 0 ? '[' + no + ']' : k === 'p' ? no + ' +' : no); b++; } }); return out.join(' '); };
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('note-values')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. The book uses the British names; each note's page gives its other name once (quarter note, half note, dotted half note, whole note, eighth notes; quarter, half and whole rests). It counts <b>1 2 3 4</b>, and <b>1 + 2 +</b> for quavers (+ is said “and”). Under every note a coral sound line as long as its beats; held beats are lighter, a rest's beats are dashed. Not yet: the single quaver and its rest, the dotted crotchet and semiquavers (chapter {bkChapterNo('rhythm')}, Rhythm patterns, and the drill's higher levels); rests in bars and filling bars (chapter {bkChapterNo('time-signatures')}, Time signatures). Page 6 shows five lines only to show where the minim and semibreve rests sit; the staff is chapter {bkChapterNo('staff')}. AMEB: Preliminary.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: walk, then run.</b> Walk round the room on the crotchets, one step a beat. Hold a minim like a long step: one step, then stand for the second beat. Run on the quavers: two quick steps on a beat. In this book the count in brackets below is a rest's beat, and a count in square brackets is a held beat.</div>
    <TcBlock page={2} title="The crotchet: one beat" answers={<>{tcAns('TRY IT', ['1 traced; 2 four crotchets, one over each heart'], null)}{tcAns('YOUR TURN', W.howMany.map(c => c + (c === 1 ? ' beat' : ' beats')), 3)}{tcAns('PLAY', ['7 and 8: one heart-long line under each crotchet'], null)}</>}
      watch="A crotchet drawn with a hollow head (that is a minim) or the stem on the wrong side. At the piano: the count stopping between notes, or the notes getting quicker."
      say="“One crotchet, one heart, one step.”"/>
    <TcBlock page={3} title="The minim: two beats" answers={<>{tcAns('TRY IT', W.qh.map(k => nvNameEn[k] + ', ' + NV_BEATS[k]))}{tcAns('YOUR TURN', W.lines3.map(lineTxt), 9)}{tcAns('PLAY', W.count3.map(cnt), 13)}</>}
      watch="Cutting the minim short: letting go on its second beat, or saying only “1” and going on. The held number is still said, just more quietly."
      say="“Play on 1, hold on 2: keep the key down while you say it.”"/>
    <TcBlock page={4} title="Longer notes: 3 and 4 beats" answers={<>{tcAns('TRY IT', W.beats4.map(k => nvNameEn[k] + ', ' + NV_BEATS[k]))}{tcAns('YOUR TURN', W.lines4.map(lineTxt), 9)}{tcAns('PLAY', W.count4.map(cnt), 13)}</>}
      watch="Mixing up the dotted minim (stem, dot) and the semibreve (no stem). Letting a semibreve go after two or three beats."
      say="“The dot adds half the minim: two beats and one more.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Two quavers on one beat" answers={<>{tcAns('TRY IT', W.walkRun.map(k => k === 'p' ? 'run-ning' : 'walk'))}{tcAns('YOUR TURN', W.plus.map(cnt), 9)}{tcAns('PLAY', W.fromWords.map(row => row.map(([k]) => k === 'p' ? 'two quavers' : 'crotchet').join(', ')), 13)}</>}
      watch="Rushing the quavers so the beat speeds up; giving each quaver a whole beat. The two quavers share one heart: the + is exactly halfway."
      say="“Run-ning is two steps in the time of one walk.”"/>
    <TcBlock page={6} title="Rests: silence you count" answers={<>{tcAns('TRY IT', ['crotchet to crotchet rest, semibreve to semibreve rest, minim to minim rest'], 1)}{tcAns('YOUR TURN', W.restCount.map(cnt), 2)}{tcAns('PLAY', W.draw.map(k => k === 'hr' ? 'a block sitting on line 3' : 'a block hanging from line 4'), 6)}</>}
      watch="Stopping the count in a rest, so the next note comes early. Mixing up the minim rest (sits on the line) and the semibreve rest (hangs from it)."
      say="“Your hand rests; your count doesn't.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.name.map(k => nvNameEn[k] + ', ' + NV_BEATS[k]))}
      {tcAns('B', C.lines.map(lineTxt), 7)}
      {tcAns('C', C.count.map(cnt), 9)}
      {tcAns('D', C.plus.map(cnt), 11)}
      {tcAns('E', C.rests.map(cnt), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. The paper shows the idea; the note lengths themselves are heard: also listen to the student play and count (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1 to 3', page: '2 to 4' }, { id: 'b', step: '2 and 3', page: '3 and 4' }, { id: 'c', step: '2 and 3', page: '3 and 4' }, { id: 'd', step: 4, page: 5 }, { id: 'e', step: 5, page: 6 }]}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['note-values'] = NvWorkbook;
TEACHER_COPIES['note-values'] = NvTeacher;
