import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AN: the Workbooks for the three new Grades 2-3 rooms (Scales Further, Intervals and Chords Further, Rhythm Further), the
# way Build AI made them: pages 2 to 6 face the Lesson Book's steps (try it, your turn, play), page 7 is the check-up on paper, and the
# teacher's copy gains every answer and the scoring (4 marks a part, pass 3+, go back to the step's page). Every answer is computed
# from the room's own data, so the paper and the app cannot disagree.

CODE = r'''
// ─── Scales Further: the Workbook (Build AN) ───
const SCF_WB = {
  thumb: [['Bb', 'R'], ['Eb', 'R'], ['Fsm', 'R'], ['Bb', 'L'], ['D', 'L'], ['Bm', 'L']],
  meet: ['D', 'Bb', 'Bm'],
  mel: ['Gm', 'Cm'],
  mirror: ['G', 'F', 'Bmh', 'Dmh'],
  chrom: [[0, 'R'], [1, 'L']],
  chk: { thumb: [['Eb', 'L'], ['A', 'R'], ['Gm', 'L'], ['Fsm', 'L']], meet: ['A', 'Eb', 'Gm', 'Bm'], mirror: ['D', 'Bb', 'Emh', 'Gmh'], chrom: [[0, 'R', 1], [1, 'L', 2], [2, 'R', 1], [1, 'R', 3]] },
};
const scfwThumbs = (k, h) => { const K = scfKeys(k, 1), N = scfNames(k, 1); return scfThumbPcs(k, h).map(pc => N[K.findIndex(x => spPc(x) === pc)]); };
const scfwMeet = (k) => { const m = scfMeet(k), N = scfNames(k); return m.length ? m.map(j => N[j]).join(', ') : 'never'; };
const scfwHand = (h) => (h === 'R' ? 'right hand' : 'left hand');
const scfwChromNames = (st) => Array.from({ length: 13 }, (_, j) => scfChLet(SCF_CHROM[st][1] + j).split('/')[0]);
function ScfwThumbCell({ item, n, ex, small }) {
  const [k, h] = item, K = scfKeys(k, 1), a = scfwThumbs(k, h);
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
    <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{SCF[k].en}, {scfwHand(h)}</div>
    <SpKb lo={K[0]} hi={K[7]} W={small ? 12 : 17} H={small ? 32 : 46} lit={Object.fromEntries(K.map(x => [x, 'pale']))} names={{ [K[0]]: scfNames(k, 1)[0] }} k={1}/>
    <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11.5,fontWeight:800,color:BK.ink}}>thumb: {nvBox(ex, a[0], 34, 26)} {nvBox(ex, a[1], 34, 26)}</div>
  </div></ExCell>;
}
const scfwLetters = (names, size = 32, coral = []) => <div style={{display:'flex',gap:3,justifyContent:'center',flexWrap:'wrap'}}>{names.map((x, j) => <span key={j} style={{width:size,height:size,border:'1.6px solid ' + (coral.includes(j) ? BK.coral : BK.ink),borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:size * 0.42,fontWeight:800,color:BK.ink}}>{x}</span>)}</div>;
function ScfWorkbook({ startNo = 1 }) {
  const W = SCF_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-23">{content}</WbPage>);
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Where does the thumb play?" how="The scale's keys are pale. Find the two letters the thumb plays in one octave: it only plays white keys. A black-key start: the right hand begins on 2.">
      <BkGrid cols={3} gap="6px 10px">{W.thumb.map((it, i) => <ScfwThumbCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Black-key starts this week" how="Do each one at the piano and tick a box each day. Find the thumb's keys before you start.">
      <PhLog rows={['B♭ major, right hand: 2 1 2 3 1 2 3 4, thumbs on C and F', 'E♭ major, each hand, one octave then two', 'F♯ minor, right hand: start on 2, thumbs on A and D']} label={300}/>
    </Part>
    <Part kind="play" title="E♭ major, right hand" how="Write the finger number under each letter. Start on 2; the thumb takes the first white key.">
      <div style={{display:'grid',gap:6,padding:'6px 0'}}>{scfwLetters(scfNames('Eb', 1), 38)}<div style={{display:'flex',gap:3,justifyContent:'center'}}>{scfNames('Eb', 1).map((_, j) => <span key={j}>{bkBox(38, 30)}</span>)}</div></div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Where do the thumbs meet?" how="Two octaves, hands together. The right hand's fingers are on top, the left hand's underneath. Write every letter where both play 1, or write never.">
      <div style={{display:'grid',gap:10}}>{W.meet.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:4}}>{SCF[k].en}, two octaves</div><ScfStrip k={k} found={i === 0 ? scfMeet(k) : []} mw={640} legend={i === 0}/>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink,marginTop:4}}>both thumbs: {nvBox(i === 0, scfwMeet(k), 120, 28)}</div></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Hands together this week" how="Tick a box each day. Very slowly first; stop at each turn and check.">
      <PhLog rows={['D major, two octaves hands together: the thumbs meet on the middle D', 'B♭ major: the thumbs never meet; the three notes round each turn, hands together', 'Run-ning at 60, then 84 (Grade 2) or 92 (Grade 3)']} label={300}/>
    </Part>
    <Part kind="play" title="Guess, then check" how="Guess first, then find out at the piano: two octaves hands together, where do both thumbs play?">
      <div style={{display:'flex',gap:30,justifyContent:'center',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'10px 0'}}>{[['A major', 4], ['F♯ minor', 5]].map(([l, n]) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {l} {bkBox(110, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Write the melodic minor" how="Up: raise the 6th and the 7th. Down: the natural minor. The first and last letters are there.">
      <div style={{display:'grid',gap:10}}>{W.mel.map((m, i) => { const c = SCF_MEL[m]; return <ExCell key={m} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:6,padding:'16px 4px 4px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{c.en}</div>
        {['up', 'dn'].map(d => <div key={d} style={{display:'flex',gap:4,justifyContent:'center',alignItems:'center'}}><span style={{width:44,fontSize:11,fontWeight:900,color:BK.muted}}>{d === 'up' ? 'up ↗' : 'down ↘'}</span>{c[d].map((x, j) => <span key={j}>{j === 0 || j === 7 ? bkHand(x, 34, 28) : nvBox(i === 0, x, 34, 28)}</span>)}</div>)}
      </div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Melodic minor this week" how="Tick a box each day.">
      <PhLog rows={['G melodic minor, each hand: E and F♯ going up, F and E♭ coming down', 'C melodic minor, each hand (Grade 3: hands together too)', 'Sing the top four notes up, then down: hear the change']} label={300}/>
    </Part>
    <Part kind="play" title="Three kinds of minor" how="Write the 6th and the 7th of G minor in each form.">
      <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{[['natural', 3], ['harmonic', 4], ['melodic, going up', 5]].map(([l, n]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l}: {bkBox(44, 30)} {bkBox(44, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Mirror twins, or not?" how="Contrary motion from one note: the right hand's fingers above, the left hand's below. Same numbers all the way? Write Y. Not? Write N.">
      <BkGrid cols={2} gap="6px 10px">{W.mirror.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{SCF_CM[k].en}</div><ScfCmKb k={k} W={11} H={40} kk={1.1}/>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>mirror twins? {nvBox(i === 0, scfMirror(k) ? 'Y' : 'N', 34, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Contrary motion this week" how="Tick a box each day.">
      <PhLog rows={['G major and D major from one note: the same numbers both ways', 'F major: the right hand plays 4 on B♭, the left hand 4 on G', 'Say each hand\'s numbers aloud, slowly, then at 66 (Grade 2) or 80 (Grade 3)']} label={300}/>
    </Part>
    <Part kind="play" title="B♭ major, contrary motion" how="Both hands on the same B♭. Write the left hand's finger numbers going down.">
      <div style={{display:'grid',gap:6,padding:'6px 0'}}>{scfwLetters(scfCm('Bb').nmL, 38)}<div style={{display:'flex',gap:3,justifyContent:'center'}}>{scfCm('Bb').nmL.map((_, j) => <span key={j}>{bkBox(38, 30)}</span>)}</div></div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Chromatic fingers" how="Write the finger under each letter: 3 on black keys, 1 on white keys, 2 where two white keys sit together.">
      <div style={{display:'grid',gap:10}}>{W.chrom.map(([st, h], i) => { const N = scfwChromNames(st), F = N.map((_, j) => scfChF(SCF_CHROM[st][1] + j, h, j === 0 || j === 12));
        return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:5,padding:'16px 4px 4px'}}>
          <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>From {SCF_CHROM[st][0]}, {scfwHand(h)}, going up</div>
          {scfwLetters(N, 30)}<div style={{display:'flex',gap:3,justifyContent:'center'}}>{F.map((f, j) => <span key={j}>{nvBox(i === 0, String(f), 30, 28)}</span>)}</div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Chromatic this week" how="Tick a box each day.">
      <PhLog rows={['From D, right hand then left, one octave, then two', 'From A and from E♭ (Grade 3), each hand', 'Grade 3, hands together: listen for the 3s landing together']} label={300}/>
    </Part>
    <Part kind="play" title="Where is the 2?" how="On which white keys does each hand use finger 2?">
      <div style={{display:'flex',gap:30,justifyContent:'center',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'10px 0'}}>{[['right hand', 3], ['left hand', 4]].map(([l, n]) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {l}: {bkBox(40, 30)} {bkBox(40, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<ScfPaperCheck/>);
  return <>{pages}</>;
}
function ScfPaperCheck() {
  const C = SCF_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which two letters does the thumb play?')}
    <BkGrid cols={2} gap="6px 8px">{C.thumb.map(([k, h], i) => { const K = scfKeys(k, 1); return <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{SCF[k].en}, {scfwHand(h)}</div><SpKb lo={K[0]} hi={K[7]} W={13} H={30} lit={Object.fromEntries(K.map(x => [x, 'pale']))} names={{ [K[0]]: scfNames(k, 1)[0] }} k={1}/>
      <div style={{display:'flex',justifyContent:'center',gap:6}}>{bkBox(30, 24)}{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Two octaves hands together: where do both thumbs play? (letters, or never)')}
    <BkGrid cols={2} gap="6px 8px">{C.meet.map((k, i) => <BkCell key={i} n={i + 5}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,padding:'14px 4px 2px',fontSize:12.5,fontWeight:800,color:BK.ink}}>{SCF[k].en}{bkBox(100, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Contrary motion from one note: mirror twins? Y or N')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((k, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:6,padding:'14px 0 0'}}><div><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{SCF_CM[k].en}</div><ScfCmKb k={k} W={9} H={24} kk={1} bare/></div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Chromatic scale: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.chrom.map(([st, h, j], i) => { const s0 = SCF_CHROM[st][1]; return <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>From {SCF_CHROM[st][0]}, {scfwHand(h)}</div><SpKb lo={s0} hi={s0 + 12} W={10} H={28} lit={{ [s0 + j]: 'cor' }} names={{ [s0]: SCF_CHROM[st][0] }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
  </div>;
}
WORKBOOKS['scales-23'] = ScfWorkbook;

// ─── Intervals and Chords Further: the Workbook (Build AN) ───
const H3_WB = {
  iv: [['Am', 3, 'treble'], ['Em', 6, 'treble'], ['Dm', 7, 'treble'], ['Gm', 3, 'bass'], ['Cm', 6, 'bass'], ['Am', 4, 'treble']],
  deg: [5, 4, 7, 2, 3, 6],
  inv: [['C', 1, 0, 'treble'], ['G', 5, 1, 'treble'], ['F', 4, 1, 'bass'], ['D', 1, 1, 'treble'], ['Bb', 5, 0, 'bass'], ['Am', 5, 1, 'treble']],
  satb: [['C', 'perfect', 1, 'S'], ['G', 'plagal', 0, 'T'], ['F', 'perfect', 0, 'A'], ['D', 'plagal', 1, 'B']],
  cad: [['C', 'plagal'], ['G', 'perfect'], ['Am', 'perfect'], ['F', 'plagal']],
  chk: { iv: [['Dm', 3, 'treble'], ['Am', 7, 'bass'], ['Em', 5, 'treble'], ['Gm', 6, 'treble']], deg: [4, 7, 3, 5], inv: [['G', 1, 1, 'bass'], ['C', 4, 0, 'treble'], ['D', 5, 1, 'treble'], ['F', 1, 0, 'bass']], cad: [['D', 'perfect'], ['C', 'plagal'], ['Dm', 'plagal'], ['G', 'perfect']] },
};
const h3wIv = ([k, n]) => ({ M: 'M', m: 'm', P: 'P' }[H3_QMIN[n]] + (n === 8 ? '8' : n));
const h3wIvLong = ([k, n]) => H3_QW[H3_QMIN[n]][0] + ' ' + H3_ORD[n];
const h3wInv = ([k, d, inv]) => h3Rom(k, d) + (inv ? 'b' : '');
function H3Workbook({ startNo = 1 }) {
  const W = H3_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="harmony-23">{content}</WbPage>);
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the interval" how="The lower note is the tonic of the minor key. Count the number, then the quality: M major, m minor, P perfect.">
      <BkGrid cols={3} gap="6px 10px">{W.iv.map((it, i) => { const [a, b] = h3Above(it[0], it[2], it[1]); return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_MIN[it[0]].en}</div><IntervalStaff clef={it[2]} notes={[a, b]} width={150}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, h3wIv(it), 50, 28)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Intervals this week" how="Play each one, then say its name. Tick a box each day.">
      <PhLog rows={['A minor: A with each note of the harmonic minor above it', 'D minor and E minor the same way', 'Grade 3: G minor and C minor, reading the bass clef']} label={300}/>
    </Part>
    <Part kind="play" title="Major or minor?" how="Write the note a 3rd above the tonic, then say major or minor.">
      <div style={{display:'flex',gap:20,justifyContent:'center',flexWrap:'wrap',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'8px 0'}}>{[['A major', 7], ['A minor', 8], ['D major', 9], ['D minor', 10]].map(([l, n]) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {l} {bkBox(40, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="The degree names" how="Write the name of each degree of the scale.">
      <BkGrid cols={3} gap="6px 10px">{W.deg.map((d, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,padding:'18px 4px 6px',fontSize:13,fontWeight:800,color:BK.ink}}>
        <span style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:900}}>{d}</span>{nvBox(i === 0, H3_DEGN[d - 1][0], 110, 28)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Degree names this week" how="Play a major scale slowly and say each name. Tick a box each day.">
      <PhLog rows={['C major: tonic, supertonic, mediant, subdominant, dominant, submediant, leading note', 'G major the same way', 'Find the dominant and the subdominant of D, F and B♭ major']} label={300}/>
    </Part>
    <Part kind="play" title="Find the note" how="Write the letter.">
      <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{[['the dominant of F major', 7], ['the subdominant of G major', 8], ['the leading note of D major', 9], ['the mediant of B♭ major', 10]].map(([l, n]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l}: {bkBox(44, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Name the chord" how="Write I, IV or V for root position; Ib, IVb or Vb for first inversion (the 3rd at the bottom).">
      <BkGrid cols={3} gap="6px 10px">{W.inv.map((it, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_TRI[it[0]].en}</div><ChordStaff clef={it[3]} chords={[{ notes: h3Triad(it[0], it[1], it[3], it[2]) }]} width={150}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, h3wInv(it), 50, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Triads this week" how="Play each chord, then its first inversion. Tick a box each day.">
      <PhLog rows={['C major: I, IV, V, then Ib, IVb, Vb', 'G and F major the same way', 'A minor: i, iv, V (with G♯)']} label={300}/>
    </Part>
    <Part kind="play" title="Write the letters" how="Write the three letters of each chord, lowest first.">
      <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{[['G major, IVb', 7], ['F major, Vb', 8], ['D major, I', 9]].map(([l, n]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l}: {bkBox(36, 30)}{bkBox(36, 30)}{bkBox(36, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Which voice?" how="Look at the staff and the stem of the coral note. Write S, A, T or B.">
      <BkGrid cols={4} gap="6px 10px">{W.satb.map(([k, id, j, v], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>
        <div style={{maxWidth:120,width:'100%',margin:'0 auto'}}><SatbStaff chords={[h3CadChords(k, id)[j]]} ks={H3_CAD[k].ks} hi={{ i: 0, v }} width={150}/></div><div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, v, 34, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Four voices this week" how="Tick a box each day.">
      <PhLog rows={['Play the C major chord in four parts; sing each part on its own', 'Point to each voice: soprano and alto on the treble staff, tenor and bass on the bass staff', 'Say each voice\'s range out loud']} label={300}/>
    </Part>
    <Part kind="play" title="Stems" how="Which way do the stems go?">
      <div style={{display:'flex',gap:16,justifyContent:'center',flexWrap:'wrap',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'8px 0'}}>{[['soprano', 5], ['alto', 6], ['tenor', 7], ['bass', 8]].map(([l, n]) => <span key={l} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {l} {bkBox(52, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Perfect or plagal?" how="Write the chords (V–I or IV–I), then P for perfect or Pl for plagal.">
      <BkGrid cols={4} gap="6px 8px">{W.cad.map(([k, id], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_CAD[k].en}</div><div style={{maxWidth:150,width:'100%',margin:'0 auto'}}><SatbStaff chords={h3CadChords(k, id)} ks={H3_CAD[k].ks} width={200}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:8}}>{nvBox(i === 0, h3CadRom(k, id).join('–'), 60, 28)}{nvBox(i === 0, id === 'perfect' ? 'P' : 'Pl', 40, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Cadences this week" how="Tick a box each day.">
      <PhLog rows={['Play the perfect and plagal cadences in C: left hand the bass, right hand the other three', 'G and F major the same way', 'Write one of each in four parts; check the leading note rises']} label={300}/>
    </Part>
    <Part kind="play" title="Finish the cadence" how="The bass of a perfect cadence in G major goes from D to G. Write the bass of a plagal cadence in G major.">
      <div style={{display:'flex',gap:10,justifyContent:'center',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'10px 0'}}>{nvNum(5)} {bkBox(44, 30)} → {bkBox(44, 30)}</div>
    </Part>
    <Faces/>
  </>);
  P(<H3PaperCheck/>);
  return <>{pages}</>;
}
function H3PaperCheck() {
  const C = H3_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the interval above the tonic (M, m or P and the number).')}
    <BkGrid cols={4} gap="6px 8px">{C.iv.map((it, i) => { const [a, b] = h3Above(it[0], it[2], it[1]); return <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_MIN[it[0]].en}</div><IntervalStaff clef={it[2]} notes={[a, b]} width={130}/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Write the name of the degree.')}
    <BkGrid cols={4} gap="6px 8px">{C.deg.map((d, i) => <BkCell key={i} n={i + 5}><div style={{display:'flex',alignItems:'center',gap:6,padding:'14px 2px 2px',fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink}}>{d}{bkBox(84, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Name the chord: I, IV, V, Ib, IVb or Vb.')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map((it, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_TRI[it[0]].en}</div><ChordStaff clef={it[3]} chords={[{ notes: h3Triad(it[0], it[1], it[3], it[2]) }]} width={130}/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Perfect (P) or plagal (Pl)?')}
    <BkGrid cols={4} gap="6px 8px">{C.cad.map(([k, id], i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{H3_CAD[k].en}</div><div style={{maxWidth:130,width:'100%',margin:'0 auto'}}><SatbStaff chords={h3CadChords(k, id)} ks={H3_CAD[k].ks} width={170} stems={false}/></div><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['harmony-23'] = H3Workbook;

// ─── Rhythm Further: the Workbook (Build AN) ───
Object.assign(R2, { chkA: { items: [['ts', 2], ['es'], ['s4'], ['|'], ['ds'], ['q'], ['||']], g: 3 }, chkB: { items: [['ts', 3], ['ds'], ['se'], ['q'], ['|'], ['es'], ['ds'], ['q'], ['||']], g: 3 } });   // the check-up's two lines: four bars
const R2_WB = { counts: { semi: ['semiB', 'semiC'], dot: ['dotA', 'dotB'], trip: ['tripA', 'duA'], minim: ['minA', 'minB'], e98: ['e38', 'e98'] } };
function R2Workbook({ startNo = 1 }) {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="rhythm-23">{content}</WbPage>);
  const cnt = (keys) => <div style={{display:'grid',gap:10}}>{keys.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px'}}>{r2El(k, { counts: i === 0 ? 'ans' : 'blank', hearts: true })}</div></ExCell>)}</div>;
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 50, 30)}</span>)}</div>;
  const page = (step, title, keys, log, playT, playH, rows) => P(<>
    <WbTop step={step}/>
    <Part kind="together" title={title} how="Write the count under every note (the grey boxes are counts held through). Then clap the line, counting aloud.">{cnt(keys)}</Part>
    <Part kind="home" title="This week" how="Tick a box each day.">
      <PhLog rows={log} label={300}/>
    </Part>
    <Part kind="play" title={playT} how={playH}>{quiz(rows)}</Part>
    <Faces/>
  </>);
  page(1, 'Count the semiquavers', R2_WB.counts.semi, ['Say 1 e + a on every beat, steadily, with the metronome at 60', 'Clap line 1, then line 2, counting aloud', 'Find semiquavers in your piece and count them'], 'Semiquaver sums', 'How many semiquavers?', [['in a crotchet', 3], ['in a quaver', 4], ['in a dotted quaver', 5]]);
  page(2, 'Count the dotted rhythms', R2_WB.counts.dot, ['Count 1 e + a, clapping only on 1 and a', 'Clap line 1 and line 2, counting aloud', 'Play a scale in dotted rhythm: long-short, long-short'], 'Long and short', 'Answer.', [['the count of the semiquaver after a dotted quaver', 3], ['a dotted quaver and a semiquaver make how many beats?', 4]]);
  page(3, 'Count the triplets and duplets', R2_WB.counts.trip, ['Walk the beat and say 1 trip let on each step', 'Clap line 1; then line 2 in 6/8, two even notes across three quavers', 'Make up a bar of 2/4 with one triplet in it']);
  page(4, 'Count the minim beats', R2_WB.counts.minim, ['Count 1 + 2 + with a minim on each number', 'Clap line 1 in 2/2, then line 2 in 3/2', 'Find a piece in cut common time and count it in two'], 'Beats in a bar', 'How many beats in one bar?', [['3/2', 3], ['2/2', 4], ['cut common time', 5]]);
  page(5, 'Count 3/8 and 9/8', R2_WB.counts.e98, ['Count 1 2 3 in 3/8, one quaver to each number', '9/8: count 1 to 9, leaning on 1, 4 and 7', 'Clap line 2, feeling three big beats'], 'Simple or compound?', 'Write S or C.', [['3/8', 3], ['6/8', 4], ['9/8', 5], ['3/4', 6]]);
  P(<R2PaperCheck/>);
  return <>{pages}</>;
}
// page 3's play part (triplets) has its own questions
const R2_PLAY3 = [['a triplet: how many quavers in one crotchet beat?', 3], ['a duplet: how many notes in one dotted-crotchet beat?', 4]];
function R2PaperCheck() {
  const rows = (items, n0) => <BkGrid cols={2} gap="6px 8px">{items.map(([l, w], i) => <BkCell key={i} n={i + n0}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,padding:'14px 4px 2px',fontSize:12.5,fontWeight:800,color:BK.ink}}>{l}{bkBox(w || 44, 24)}</div></BkCell>)}</BkGrid>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the counts under the notes.')}
    <div style={{display:'grid',gap:6}}>{['chkA', 'chkB'].map((k, i) => <BkCell key={k} n={i === 0 ? '1–2' : '3–4'}><div style={{padding:'14px 2px 0'}}>{r2El(k, { counts: 'blank', hearts: true })}</div></BkCell>)}</div>
    {bkSec('B', 'How many?')}
    {rows([['semiquavers in a crotchet'], ['semiquavers in a dotted quaver'], ['quavers in a triplet'], ['notes in a duplet']], 5)}
    {bkSec('C', 'How many beats in a bar?')}
    {rows([['3/2'], ['2/2'], ['3/8'], ['9/8']], 9)}
    {bkSec('D', 'Simple (S) or compound (C)?')}
    {rows([['9/8'], ['3/8'], ['6/8'], ['3/2']], 13)}
  </div>;
}
WORKBOOKS['rhythm-23'] = R2Workbook;
'''
rep("""function ScfCmKb({ k, mark = -1, W = 22, H = 70 }) {""", """function ScfCmKb({ k, mark = -1, W = 22, H = 70, kk = 1.5, bare = false }) {""")
rep("""  return <><SpKb lo={c.L[7]} hi={c.R[7]} W={W} H={H} lit={lit} names={nm} up={up} dn={dn} label={scfCmName(k)} k={1.5}/>
    <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 4px 0'}}>""", """  return <><SpKb lo={c.L[7]} hi={c.R[7]} W={W} H={H} lit={lit} names={bare ? {} : nm} up={up} dn={dn} label={scfCmName(k)} k={kk}/>
    {!bare && <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 4px 0'}}>""")
rep("""<span>{t('right hand: up →', '오른손: 위로 →')}</span></div></>;
}
const scfFirstDiff""", """<span>{t('right hand: up →', '오른손: 위로 →')}</span></div>}</>;
}
const scfFirstDiff""")
rep('  </>);\n  P(<>\n    <TcBlock page={4} title="Three in a beat, two in a dotted beat"', '    <TcBlock page={4} title="Three in a beat, two in a dotted beat"')
rep('    <TcBlock page={5} title="The minim beat"', '  </>);\n  P(<>\n    <TcBlock page={5} title="The minim beat"')
rep("""function ScfStrip({ k, cur = -1, found = [], bad = null, onTap, mw = 460 }) {""", """function ScfStrip({ k, cur = -1, found = [], bad = null, onTap, mw = 460, legend = true }) {""")
rep("""  <div style={{display:'flex',justifyContent:'center',gap:8,marginTop:6,fontSize:12,fontWeight:800,color:BK.muted}}><span style={{display:'inline-block',width:22,height:12,borderRadius:4,background:'rgba(38,41,107,0.10)',verticalAlign:'middle'}}/>{t('one beat: run-ning, two notes', '한 박: 티-티, 두 음')}</div></div>;
}
function ScfMeetPad""", """  {legend && <div style={{display:'flex',justifyContent:'center',gap:8,marginTop:6,fontSize:12,fontWeight:800,color:BK.muted}}><span style={{display:'inline-block',width:22,height:12,borderRadius:4,background:'rgba(38,41,107,0.10)',verticalAlign:'middle'}}/>{t('one beat: run-ning, two notes', '한 박: 티-티, 두 음')}</div>}</div>;
}
function ScfMeetPad""")
rep("""  const lines = (keys) => <div style={{display:'flex',flexDirection:'column',gap:4}}>{keys.map((k, i) => <div key={k} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{r2El(k, { hearts: false })}</div></div>)}</div>;""",
    """  const lines = (keys) => <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{keys.map((k, i) => <div key={k} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0,maxWidth:330}}>{r2El(k, { hearts: false })}</div></div>)}</div>;""")
rep("""TEACHER_COPIES['rhythm-23'] = R2Teacher;""", """TEACHER_COPIES['rhythm-23'] = R2Teacher;""" + CODE)

# ── page 3's play part for Rhythm: the triplet questions (the generic page() has no rows for step 3) ──
rep("""  page(3, 'Count the triplets and duplets', R2_WB.counts.trip, ['Walk the beat and say 1 trip let on each step', 'Clap line 1; then line 2 in 6/8, two even notes across three quavers', 'Make up a bar of 2/4 with one triplet in it']);""",
    """  page(3, 'Count the triplets and duplets', R2_WB.counts.trip, ['Walk the beat and say 1 trip let on each step', 'Clap line 1; then line 2 in 6/8, two even notes across three quavers', 'Make up a bar of 2/4 with one triplet in it'], 'Three for two, two for three', 'Answer.', R2_PLAY3);""")

# ── the teacher's copies gain the Workbook's answers and the scoring ──
# Scales Further
rep("""    <TcBlock page={2} title="Start on a black key" answers={<>{tcAns('GRADE 2', [fing('D'), fing('Bm'), fing('Bb'), fing('Gm')])}{tcAns('GRADE 3', [fing('A'), fing('Fsm'), fing('Eb'), fing('Cm')])}</>}""",
    """    <TcBlock page={2} title="Start on a black key" answers={<>{tcAns('TRY IT', SCF_WB.thumb.map(([k, h]) => SCF[k].en + ', ' + scfwHand(h) + ': ' + scfwThumbs(k, h).join(', ')))}{tcAns('PLAY', ['E♭ major RH: ' + SCF.Eb.R.slice(0, 8).join(' ')])}{tcAns('GRADE 2', [fing('D'), fing('Bm'), fing('Bb'), fing('Gm')])}{tcAns('GRADE 3', [fing('A'), fing('Fsm'), fing('Eb'), fing('Cm')])}</>}""")
rep("""    <TcBlock page={3} title="Where the thumbs meet" answers={<>{tcAns(""",
    """    <TcBlock page={3} title="Where the thumbs meet" answers={<>{tcAns('TRY IT', SCF_WB.meet.map(k => SCF[k].en + ': ' + scfwMeet(k)))}{tcAns('PLAY', ['A major: ' + scfwMeet('A'), 'F♯ minor: ' + scfwMeet('Fsm')], 4)}{tcAns(""")
rep("""    <TcBlock page={4} title="The melodic minor" answers={<>{tcAns('UP / DOWN',""",
    """    <TcBlock page={4} title="The melodic minor" answers={<>{tcAns('PLAY: G MINOR 6TH AND 7TH', ['natural E♭ F', 'harmonic E♭ F♯', 'melodic going up E F♯'], 3)}{tcAns('UP / DOWN',""")
rep("""    <TcBlock page={5} title="Mirror twins, or not?" answers={<>{tcAns(""",
    """    <TcBlock page={5} title="Mirror twins, or not?" answers={<>{tcAns('TRY IT', SCF_WB.mirror.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}{tcAns('PLAY', ['B♭ major LH down: ' + SCF_CM.Bb.L.join(' ')])}{tcAns(""")
rep("""    <TcBlock page={6} title="Chromatic from any note" answers={<>{tcAns(""",
    """    <TcBlock page={6} title="Chromatic from any note" answers={<>{tcAns('TRY IT', SCF_WB.chrom.map(([st, h]) => 'from ' + SCF_CHROM[st][0] + ', ' + scfwHand(h) + ': ' + scfwChromNames(st).map((_, j) => scfChF(SCF_CHROM[st][1] + j, h, j === 0 || j === 12)).join(' ')))}{tcAns('PLAY', ['right hand: F and C', 'left hand: E and B'], 3)}{tcAns(""")
rep("""    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one played to you from memory, in the keys of the child's grade, at the grade's speed. Listen for an even run-ning through every turn.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', SCF_WB.chk.thumb.map(([k, h]) => scfwThumbs(k, h).join(', ')))}{tcAns('B', SCF_WB.chk.meet.map(scfwMeet), 5)}{tcAns('C', SCF_WB.chk.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 9)}{tcAns('D', SCF_WB.chk.chrom.map(([st, h, j]) => String(scfChF(SCF_CHROM[st][1] + j, h, false))), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.5 · D p.6. Then hear each scale at the piano, from memory, at the grade's speed: an even run-ning through every turn.</div></>}/>""")
# Intervals and Chords Further
rep("""    <TcBlock page={2} title="Above the tonic, in a minor key" answers={<>{tcAns('HARMONIC MINOR""",
    """    <TcBlock page={2} title="Above the tonic, in a minor key" answers={<>{tcAns('TRY IT', H3_WB.iv.map(h3wIv))}{tcAns('PLAY', ['A major C♯ (major)', 'A minor C (minor)', 'D major F♯ (major)', 'D minor F (minor)'], 7)}{tcAns('HARMONIC MINOR""")
rep("""    <TcBlock page={3} title="The degree names" answers={<>{tcAns('1 TO 7', H3_DEGN.map(([en]) => en))}</>}""",
    """    <TcBlock page={3} title="The degree names" answers={<>{tcAns('TRY IT', H3_WB.deg.map(d => d + ' ' + H3_DEGN[d - 1][0]))}{tcAns('PLAY', ['C', 'C', 'C♯', 'D'], 7)}{tcAns('1 TO 7', H3_DEGN.map(([en]) => en))}</>}""")
rep("""    <TcBlock page={4} title="Root position and first inversion" answers={<>{tcAns('ROOT / FIRST INVERSION',""",
    """    <TcBlock page={4} title="Root position and first inversion" answers={<>{tcAns('TRY IT', H3_WB.inv.map(h3wInv))}{tcAns('PLAY', ['E G C', 'E G C', 'D F♯ A'], 7)}{tcAns('ROOT / FIRST INVERSION',""")
rep("""    <TcBlock page={5} title="Soprano, alto, tenor, bass" answers={<>{tcAns('USUAL RANGES',""",
    """    <TcBlock page={5} title="Soprano, alto, tenor, bass" answers={<>{tcAns('TRY IT', H3_WB.satb.map(x => x[3]))}{tcAns('PLAY', ['up', 'down', 'up', 'down'], 5)}{tcAns('USUAL RANGES',""")
rep("""    <TcBlock page={6} title="Perfect and plagal cadences" answers={<>{tcAns('S, A, T, B',""",
    """    <TcBlock page={6} title="Perfect and plagal cadences" answers={<>{tcAns('TRY IT', H3_WB.cad.map(([k, id]) => h3CadRom(k, id).join('–') + ' ' + (id === 'perfect' ? 'P' : 'Pl')))}{tcAns('PLAY', ['C → G'], 5)}{tcAns('S, A, T, B',""")
rep("""    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one written on paper, then played at the piano. Use keys the child has not practised this week.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', H3_WB.chk.iv.map(h3wIv))}{tcAns('B', H3_WB.chk.deg.map(d => H3_DEGN[d - 1][0]), 5)}{tcAns('C', H3_WB.chk.inv.map(h3wInv), 9)}{tcAns('D', H3_WB.chk.cad.map(([k, id]) => (id === 'perfect' ? 'P' : 'Pl')), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.6. Then play each one at the piano.</div></>}/>""")
# Rhythm Further
rep("""    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each line clapped and counted to you; then the child writes one bar of each new value. Transposition (Grades 2 and 3, a melody of up to eight bars into another key of the grade) is in the Transposing lesson on the Home.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px',marginBottom:4}}>{['chkA', 'chkB'].map(k => <div key={k} style={{maxWidth:300}}>{r2El(k, { counts: 'ans', hearts: false })}</div>)}</div>{tcAns('B', ['4', '3', '3', '2'], 5)}{tcAns('C', ['3', '2', '3', '3 (dotted crotchets)'], 9)}{tcAns('D', ['C', 'S', 'C', 'S'], 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Part A: one mark for each bar counted right (4 marks). Parts B to D: one mark each. Score each part on its own (4 marks each, pass 3+). Not passed? Go back: A p.2 and p.3 · B p.2 to p.4 · C p.5 and p.6 · D p.6. Then clap and count each line to you. Transposition (Grades 2 and 3, a melody of up to eight bars into another key of the grade) is in the Transposing lesson on the Home.</div></>}/>""")
rep("""    <TcBlock page={2} title="Semiquavers" answers={lines(['semiA', 'semiB', 'semiC'])}""",
    """    <TcBlock page={2} title="Semiquavers" answers={<>{lines(['semiA', 'semiB', 'semiC'])}{tcAns('PLAY', ['4', '2', '3'], 3)}</>}""")
rep("""    <TcBlock page={3} title="Dotted quaver and semiquaver" answers={lines(['dotA', 'dotB'])}""",
    """    <TcBlock page={3} title="Dotted quaver and semiquaver" answers={<>{lines(['dotA', 'dotB'])}{tcAns('PLAY', ['a', 'one beat'], 3)}</>}""")
rep("""    <TcBlock page={4} title="Three in a beat, two in a dotted beat" answers={lines(['tripA', 'duA'])}""",
    """    <TcBlock page={4} title="Three in a beat, two in a dotted beat" answers={<>{lines(['tripA', 'duA'])}{tcAns('PLAY', ['3', '2'], 3)}</>}""")
rep("""    <TcBlock page={5} title="The minim beat" answers={lines(['minA', 'minB', 'minC'])}""",
    """    <TcBlock page={5} title="The minim beat" answers={<>{lines(['minA', 'minB', 'minC'])}{tcAns('PLAY', ['3', '2', '2'], 3)}</>}""")
rep("""    <TcBlock page={6} title="3/8 and 9/8" answers={lines(['e38', 'e98'])}""",
    """    <TcBlock page={6} title="3/8 and 9/8" answers={<>{lines(['e38', 'e98'])}{tcAns('PLAY', ['S', 'C', 'C', 'S'], 3)}</>}""")
# the Lesson Books' check-up pages point to the Workbook now
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
