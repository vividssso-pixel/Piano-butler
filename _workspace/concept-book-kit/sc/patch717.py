import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AX: the Workbooks for the Grade 4 rooms, the way Build AN made them for Grades 2-3: one page facing each Lesson Book step
# (try it, at home this week, play), then the check-up on paper; the teacher's copy gains every answer and the scoring (4 marks a
# part, pass 3+, go back to the step's page). Every answer is computed from the room's own data, so the paper and the app cannot
# disagree. Hear and Sing, Grade 4 has no Workbook (every step is by ear), as Hear and Sing Further has none.
# Also: the harmony teacher's copy, page 5, listed only the melody notes under "one way to harmonise each"; it now lists the chords.

CODE = r'''
// ─── Scales and Arpeggios, Grade 4: the Workbook (Build AX) ───
const S4_WB = {
  four: [['E', 'R'], ['E', 'L'], ['Csm', 'L'], ['Ab', 'R'], ['Ab', 'L'], ['Fm', 'R']],
  touch: ['Ab', 'Fmel'],
  arp: [['E', 'R'], ['E', 'L'], ['Em', 'L'], ['Ab', 'R'], ['Abm', 'L'], ['Ab', 'L']],
  chk: { four: [['Csm', 'R'], ['Fm', 'L'], ['Csmel', 'R'], ['Csmel', 'L']], mirror: ['A4', 'Fsmh', 'Eb4', 'Cmh'], chrom: [[0, 'R', 1], [0, 'L', 1], [1, 'R', 3], [1, 'L', 3]], arp: [['E', 'L', 1], ['Em', 'L', 1], ['Ab', 'R', 1], ['Abm', 'L', 3]] },
};
const s4wRows = (rows) => rows.map(r => spTx(r));   // the crotchet sign in the print face
const s4wName = (k) => S4_SC[k].en + (k === 'Csmel' ? ', going up' : '');
const s4wBeatNames = (k) => s4Two(k).filter((_, n) => n % 4 === 0).map(x => x.nm);
const s4wChNames = (st) => Array.from({ length: 13 }, (_, j) => s4ChLet(S4_CH[st][1] + j));
const s4wLabel = (txt) => <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{txt}</div>;
const s4wRow = (lab, cells) => <div style={{display:'flex',gap:3,justifyContent:'center',alignItems:'center'}}><span style={{width:46,flex:'0 0 46px',fontSize:10.5,fontWeight:900,color:BK.muted,whiteSpace:'nowrap'}}>{lab}</span>{cells}</div>;
function S4wFourCell({ item, n, ex, small }) {
  const [k, h] = item, c = S4_SC[k], K = s4Oct(k), F = s4Mid(k, h), lit = {}, nums = {};
  K.forEach((x, j) => { lit[x] = 'pale'; if (F[j] === 1) nums[x] = 1; });
  const kb = <SpKb lo={K[0]} hi={K[7]} W={small ? 12 : 17} H={small ? 32 : 46} lit={lit} names={{ [K[0]]: c.nm[0] }} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} k={1}/>;
  if (small) return <BkCell n={n}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>{s4wLabel(s4wName(k) + ', ' + scfwHand(h))}{kb}<div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>;
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>{s4wLabel(s4wName(k) + ', ' + scfwHand(h))}{kb}
    <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11.5,fontWeight:800,color:BK.ink}}>finger 4: {nvBox(ex, s4F4Note(k, h), 40, 26)}</div></div></ExCell>;
}
function S4wArpCell({ item, n, ex }) {
  const [k, h] = item, c = S4_AR[k], K = s4ArKeys(k), nm = K.map((_, j) => c.nm[j % 3]);
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:4,padding:'16px 2px 2px'}}>{s4wLabel(c.en + ', ' + scfwHand(h) + ', two octaves up')}
    <SpKb lo={c.r} hi={c.r + 24} W={9} H={30} lit={Object.fromEntries(K.map(x => [x, 'pale']))} names={{ [K[0]]: c.nm[0] }} k={1}/>
    {scfwLetters(nm, 26)}<div style={{display:'flex',gap:3,justifyContent:'center'}}>{c[h].map((f, j) => <span key={j}>{nvBox(ex, String(f), 26, 24)}</span>)}</div></div></ExCell>;
}
function S4Workbook({ startNo = 1 }) {
  const W = S4_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-4">{content}</WbPage>);
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 44, 30)}</span>)}</div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which note does finger 4 play?" how="One octave of each scale, the thumbs shown. Finger 4 plays once an octave, always the same note: write it.">
      <BkGrid cols={3} gap="6px 10px">{W.four.map((it, i) => <S4wFourCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Four octaves this week" how="Do each one at the piano and tick a box each day. Find the 4s before you start.">
      <PhLog rows={s4wRows(['E major, each hand: finger 4 on D♯ (right hand) and F♯ (left hand) in every octave', 'C♯ minor in all three forms, A♭ major and F minor: find the 4s, then four octaves', 'Hands together, four notes a beat, up to ♩ = 63'])} label={300}/>
    </Part>
    <Part kind="play" title="A♭ major, right hand" how="A middle octave, from A♭ to A♭. Write the finger under each letter: it starts on 3.">
      <div style={{display:'grid',gap:6,padding:'6px 0'}}>{scfwLetters(S4_SC.Ab.nm.concat([S4_SC.Ab.nm[0]]), 38)}<div style={{display:'flex',gap:3,justifyContent:'center'}}>{S4_SC.Ab.nm.concat(['']).map((_, j) => <span key={j}>{bkBox(38, 30)}</span>)}</div></div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Find the beat notes" how="Two octaves up and down, four notes a beat. The first of every group of four is a beat note: colour or circle each one, going up and coming down.">
      <div style={{display:'grid',gap:10}}>{W.touch.map((k, i) => { const sq = s4Two(k), row = (xs, off) => scfwLetters(xs.map(x => x.nm), 24, i === 0 ? xs.map((_, j) => j).filter(j => (off + j) % 4 === 0) : []);
        return <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel(S4_ST[k].en + (k === 'Fmel' ? ' (the natural minor coming down)' : ''))}
          {s4wRow('up ↗', row(sq.slice(0, 15), 0))}{s4wRow('down ↘', row(sq.slice(15), 15))}</div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Four to a beat this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['A♭ major, one octave: two notes a beat, then four (1 e + a)', 'Staccato A♭ major and F melodic minor: the same fingers, short, up to ♩ = 52', 'Tap or count the beat while the scale runs: even beat notes'])} label={300}/>
    </Part>
    <Part kind="play" title="Count the notes" how="Write the answer.">
      {quiz([['notes in four beats', 3], ['the scale above has 29 notes: how many full beats of four?', 4], ['staccato: the same fingers as legato? (Y or N)', 5]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Mirror twins, or not?" how="Contrary motion from one note: the right hand's fingers above, the left hand's below. Same numbers all the way? Write Y. Not? Write N.">
      <BkGrid cols={2} gap="6px 10px">{S4_CM_KEYS.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
        {s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={11} H={40} kk={1.1}/>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>mirror twins? {nvBox(i === 0, scfMirror(k) ? 'Y' : 'N', 34, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Contrary motion this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['A major and C harmonic minor: the same numbers both ways', 'E♭ major: both hands start on 2', 'F♯ harmonic minor: say each hand\'s numbers aloud, slowly, then up to ♩ = 52'])} label={300}/>
    </Part>
    <Part kind="play" title="F♯ harmonic minor, contrary motion" how="Both hands start on the same F♯. Write each hand's fingers under its letters.">
      <div style={{display:'grid',gap:5,padding:'4px 0'}}>{[['RH ↗', scfCm('Fsmh').nmR], ['LH ↘', scfCm('Fsmh').nmL]].map(([l, nm]) => <div key={l} style={{display:'grid',gap:3}}>{s4wRow(l, scfwLetters(nm, 30))}{s4wRow('', <div style={{display:'flex',gap:3}}>{nm.map((_, j) => <span key={j}>{bkBox(30, 26)}</span>)}</div>)}</div>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Both hands' fingers" how="The chromatic scale going up, hands together. Write the right hand's finger above each letter and the left hand's below: 3 on black keys, 1 on white keys, 2 where two white keys sit together.">
      <div style={{display:'grid',gap:10}}>{[0, 1].map(st => { const N = s4wChNames(st), K = N.map((_, j) => S4_CH[st][1] + j);
        return <ExCell key={st} n={st + 1} ex={st === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel('From ' + S4_CH[st][0] + ', one octave up')}
          {s4wRow('RH', <div style={{display:'flex',gap:3}}>{K.map((x, j) => <span key={j}>{nvBox(st === 0, String(s4ChR(x)), 28, 24)}</span>)}</div>)}
          {s4wRow('', scfwLetters(N, 28))}
          {s4wRow('LH', <div style={{display:'flex',gap:3}}>{K.map((x, j) => <span key={j}>{nvBox(st === 0, String(s4ChL(x)), 28, 24)}</span>)}</div>)}</div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Chromatic this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['From E, each hand, one octave: check E–F and B–C', 'Hands together, very slowly: hear the 3s land together', 'From E and from G♯/A♭, four octaves, four notes a beat, up to ♩ = 63'])} label={300}/>
    </Part>
    <Part kind="play" title="Where do the hands part?" how="On which four white keys do the two hands use different fingers?">
      <div style={{display:'flex',gap:8,justifyContent:'center',alignItems:'center',padding:'8px 0'}}>{nvNum(3)} {bkBox(40, 30)}{bkBox(40, 30)}{bkBox(40, 30)}{bkBox(40, 30)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Arpeggio fingers" how="Two octaves going up, as the book prints them. Write the finger under each letter.">
      <BkGrid cols={2} gap="6px 10px">{W.arp.map((it, i) => <S4wArpCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Arpeggios this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['E major and minor, each hand: the thumb on E', 'A♭ major and minor: find the thumb\'s C (C♭ in the minor) first', 'Four octaves, two notes a beat, up to ♩ = 76'])} label={300}/>
    </Part>
    <Part kind="play" title="Major or minor fingers" how="Which finger does the left hand use?">
      {quiz([['on G♯ in E major', 7], ['on G in E minor', 8]])}
    </Part>
    <Faces/>
  </>);
  P(<S4PaperCheck/>);
  return <>{pages}</>;
}
function S4PaperCheck() {
  const C = S4_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which note does finger 4 play in every octave?')}
    <BkGrid cols={4} gap="6px 8px">{C.four.map((it, i) => <S4wFourCell key={i} item={it} n={i + 1} small/>)}</BkGrid>
    {bkSec('B', 'Contrary motion from one note: mirror twins? Y or N')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((k, i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:6,padding:'14px 0 0'}}><div>{s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={9} H={24} kk={1} bare/></div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Chromatic scale: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.chrom.map(([st, h, j], i) => { const s0 = S4_CH[st][1]; return <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>From {S4_CH[st][0]}, {scfwHand(h)}</div><SpKb lo={s0} hi={s0 + 12} W={10} H={28} lit={{ [s0 + j]: 'cor' }} names={{ [s0]: s4ChLet(s0) }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('D', 'Arpeggio: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.arp.map(([k, h, j], i) => { const c = S4_AR[k], K = s4ArKeys(k), lit = Object.fromEntries(K.map(x => [x, 'pale'])); lit[K[j]] = 'cor'; return <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>{c.en}, {scfwHand(h)}</div><SpKb lo={c.r} hi={c.r + 24} W={8} H={26} lit={lit} names={{}} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
  </div>;
}
WORKBOOKS['scales-4'] = S4Workbook;

// ─── Keys and Intervals, Grade 4: the Workbook (Build AX) ───
const K4_WB = {
  sig: [['sharp', 5, false, 'treble'], ['flat', 6, false, 'treble'], ['sharp', 3, true, 'bass'], ['flat', 5, true, 'treble'], ['sharp', 6, false, 'bass'], ['sharp', 4, true, 'treble']],
  lead: ['Bm', 'Fsm', 'Csm', 'Fm', 'Bbm'],
  semi: [0, 2, 1, 3, 6, 5],
  iv: [['Db', 'treble', 'down', 7], ['B', 'treble', 'up', 2], ['Fsm', 'bass', 'up', 5], ['Gb', 'treble', 'up', 6], ['Bbm', 'bass', 'down', 3], ['Csm', 'treble', 'down', 5]],
  inv: ['M3', 'm7', 'P4', 'm6'],
  mod: [0, 3, 6],
  tr: [0, 2],
  chk: { sig: [['flat', 5, false, 'bass'], ['sharp', 2, true, 'treble'], ['flat', 4, true, 'bass'], ['sharp', 6, false, 'treble']], lead: ['Bbm', 'Csm', 'Fsm', 'Fm'], semi: [7, 8, 9, 10], iv: [['Fs', 'treble', 'up', 4], ['Db', 'bass', 'up', 7], ['Fm', 'treble', 'down', 2], ['B', 'bass', 'down', 6]] },
};
const k4wKey = (id) => (id.endsWith('m') ? id.slice(0, -1) + ' minor' : id + ' major');
const k4wSig = ([ty, n, minor]) => k4wKey(k4SigId(ty, n, minor));
const k4wNs = ([k, clef, dir, x]) => (dir === 'up' ? [k4Note(k, clef, 0), k4Note(k, clef, x)] : [k4Note(k, clef, x - 1), k4Note(k, clef, 7)]);
const k4wIv = (it) => { const ns = k4wNs(it); return k4Iv(ns[0], ns[1]); };
const k4wHarm = (k) => Array.from({ length: 8 }, (_, x) => h3Let(k4Note(k, 'treble', x)));
const k4wIvStaff = (it, w) => <IntervalStaff clef={it[1]} notes={k4wNs(it)} labels={it[2] === 'up' ? ['tonic', ''] : ['', 'tonic']} width={w}/>;
const k4wSemiStaff = (i, w) => <IntervalStaff clef="treble" notes={K4_SEMI[i].map(h3N)} width={w}/>;
const k4wLeadRow = (k, ex, size = 32) => { const L = k4wHarm(k); return <div style={{display:'flex',gap:3,justifyContent:'center',alignItems:'center'}}>
  <span style={{width:84,fontSize:11,fontWeight:900,color:BK.muted}}>{K4[k].en}</span>{L.map((x, j) => <span key={j}>{j === 6 ? nvBox(ex, K4_LEAD[k].lead, size, size) : k4wLet(x, size)}</span>)}</div>; };
const k4wLet = (x, size) => <span style={{width:size,height:size,boxSizing:'border-box',border:'1.6px solid ' + BK.ink,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:size * 0.42,fontWeight:800,color:BK.ink}}>{x}</span>;
function K4Workbook({ startNo = 1 }) {
  const W = K4_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="keys-4">{content}</WbPage>);
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 50, 30)}</span>)}</div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the key" how="Read the key signature. Write the major or minor key it asks for. Sharps: up a semitone from the last sharp. Flats: the second-last flat. Minor: three semitones below the major.">
      <BkGrid cols={3} gap="6px 10px">{W.sig.map((it, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
        <div style={{maxWidth:150,width:'100%',margin:'0 auto'}}><KSStaff count={it[1]} type={it[0]} width={150} clef={it[3]} accent={BK.ink} ink={BK.ink}/></div>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11.5,fontWeight:800,color:BK.ink}}>{it[2] ? 'minor:' : 'major:'} {nvBox(i === 0, k4wSig(it), 96, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Key signatures this week" how="Tick a box each day.">
      <PhLog rows={['Say the order of the sharps (F C G D A E B) and the flats (B E A D G C F)', 'Write the signatures of B, F♯, D♭ and G♭ major, treble and bass', 'B, F♯, C♯, F and B♭ minor: each three semitones below its relative major']} label={300}/>
    </Part>
    <Part kind="play" title="Write the key signature" how="On each staff, write the key signature.">
      <div style={{display:'flex',gap:20,justifyContent:'center',flexWrap:'wrap',padding:'4px 0'}}>{[['D♭ major', 7, 'treble'], ['F♯ minor', 8, 'bass']].map(([l, n, clef]) => <div key={l} style={{display:'grid',gap:2,justifyItems:'center'}}><span style={{fontSize:13,fontWeight:800,color:BK.ink}}>{nvNum(n)} {l}</span><div style={{width:170}}><KSStaff count={0} type="sharp" width={170} clef={clef} accent={BK.ink} ink={BK.ink}/></div></div>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="The raised 7th" how="Each harmonic minor scale, its 7th left out. Write the raised 7th with its accidental, and the right letter: each letter once in a scale.">
      <div style={{display:'grid',gap:6}}>{W.lead.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px'}}>{k4wLeadRow(k, i === 0)}</div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Harmonic minors this week" how="Tick a box each day.">
      <PhLog rows={['Play each Grade 4 harmonic minor, one octave, and say the 7th aloud', 'F♯ minor: E♯ is the white key F, but it is written E♯', 'F minor and B♭ minor: the 7th needs a natural sign']} label={300}/>
    </Part>
    <Part kind="play" title="Two white keys" how="Which white key is it?">
      {quiz([['E♯', 6, 40], ['B♯', 7, 40]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Diatonic or chromatic?" how="Each pair is a semitone. Different letters: write D (diatonic). The same letter: write C (chromatic).">
      <BkGrid cols={3} gap="6px 10px">{W.semi.map((j, i) => <ExCell key={j} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{k4wSemiStaff(j, 150)}
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, k4SemiKind(j) === 'dia' ? 'D' : 'C', 34, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Semitones this week" how="Tick a box each day.">
      <PhLog rows={['Play a chromatic scale from C; name each semitone as you go', 'Two names for each black key: C♯ and D♭, F♯ and G♭', 'Different letters: diatonic. The same letter: chromatic']} label={300}/>
    </Part>
    <Part kind="play" title="A semitone above F" how="Write the note.">
      {quiz([['a diatonic semitone above F', 7, 44], ['a chromatic semitone above F', 8, 44]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Name the interval" how="The tonic and a note above or below it. Count up from the lower note: number, then quality (M, m or P).">
      <BkGrid cols={3} gap="6px 10px">{W.iv.map((it, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{s4wLabel(K4[it[0]].en + ', ' + (it[2] === 'up' ? 'above' : 'below') + ' the tonic')}
        {k4wIvStaff(it, 150)}<div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, k4wIv(it), 50, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Intervals this week" how="Tick a box each day.">
      <PhLog rows={['Above the tonic: count up from the tonic. Below: count up from the note to the tonic', 'Invert: the numbers add to 9; major and minor swap; perfect stays perfect', 'Play each one and sing it']} label={300}/>
    </Part>
    <Part kind="play" title="Turn it upside down" how="Write the inversion.">
      <div style={{display:'flex',gap:22,justifyContent:'center',flexWrap:'wrap',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'8px 0'}}>{W.inv.map((id, i) => <span key={id} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(i + 7)} {id} → {bkBox(44, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Where does the tune go?" how="Circle the note that tells: a new sharp or natural. Then write the new key, and D (the dominant) or R (the relative).">
      <div style={{display:'grid',gap:8}}>{W.mod.map((j, i) => { const m = K4_MOD[j]; return <ExCell key={j} n={i + 1} ex={i === 0}><div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) auto',gap:10,alignItems:'center',padding:'14px 4px 2px'}}>
        <div style={{minWidth:0,maxWidth:430}}>{s4wLabel('Starts in ' + k4wKey(m.h))}<K4Melody notes={k4ModNotes(j)} ks={m.ks} hi={i === 0 ? [m.clue] : []} width={360}/></div>
        <div style={{display:'grid',gap:6,justifyItems:'center',fontSize:11,fontWeight:800,color:BK.muted}}>new key {nvBox(i === 0, k4wKey(m[m.to]), 100, 26)}{nvBox(i === 0, m.to === 'dom' ? 'D' : 'R', 34, 26)}</div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Modulation this week" how="Tick a box each day.">
      <PhLog rows={['Play each tune; stop on the note that tells, and name the new key', 'To the dominant: the leading note of the dominant (F♯ in C major)', 'To the relative: its leading note (G♯ in C major); a minor key to its major: the raised 7th cancelled']} label={300}/>
    </Part>
    <Part kind="play" title="The note that tells" how="A tune in C major. Which note would take it there?">
      {quiz([['to G major', 4, 44], ['to A minor', 5, 44]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={6}/>
    <Part kind="together" title="Transpose the melody" how="Write the melody in the new key, on the staff below it. Find the first note, move every note the same distance, and move the accidentals too.">
      <div style={{display:'grid',gap:8}}>{W.tr.map((j, i) => { const T = K4_TR[j]; return <ExCell key={j} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'14px 4px 2px'}}>
        {s4wLabel(K4_TRK[T.from][2] + ' → ' + K4_TRK[T.to][2])}<div style={{maxWidth:440,width:'100%',margin:'0 auto',display:'grid',gap:2}}><K4Melody notes={k4TrNotes(T.from, T.m)} ks={K4_TRK[T.from][1]} width={400}/>
        <K4Melody notes={i === 0 ? k4TrNotes(T.to, T.m) : []} ks={K4_TRK[T.to][1]} width={400}/></div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Transposing this week" how="Tick a box each day.">
      <PhLog rows={['Name the first note in the new key, then move every note the same distance', 'Move the accidentals too: F♯ in C major becomes G♯ in D major', 'Play both versions: the same tune, only higher or lower']} label={300}/>
    </Part>
    <Part kind="play" title="G major to F major" how="Write each note a tone lower, in F major.">
      <div style={{display:'flex',gap:22,justifyContent:'center',flexWrap:'wrap',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'8px 0'}}>{['B', 'F♯', 'C'].map((x, i) => <span key={x} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(i + 3)} {x} → {bkBox(44, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<K4PaperCheck/>);
  return <>{pages}</>;
}
function K4PaperCheck() {
  const C = K4_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the key (major or minor, as asked).')}
    <BkGrid cols={4} gap="6px 8px">{C.sig.map((it, i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{maxWidth:140,width:'100%',margin:'0 auto'}}><KSStaff count={it[1]} type={it[0]} width={170} clef={it[3]} accent={BK.ink} ink={BK.ink}/></div>
      <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:5,fontSize:10.5,fontWeight:800,color:BK.muted}}>{it[2] ? 'minor' : 'major'} {bkBox(70, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('B', 'Write the raised 7th of the harmonic minor.')}
    <BkGrid cols={2} gap="6px 8px">{C.lead.map((k, i) => <BkCell key={k} n={i + 5}><div style={{padding:'14px 0 0'}}>{k4wLeadRow(k, false, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Diatonic (D) or chromatic (C) semitone?')}
    <BkGrid cols={4} gap="6px 8px">{C.semi.map((j, i) => <BkCell key={j} n={i + 9}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}>{k4wSemiStaff(j, 130)}<div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Name the interval (M, m or P and the number).')}
    <BkGrid cols={4} gap="6px 8px">{C.iv.map((it, i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{K4[it[0]].en}</div>{k4wIvStaff(it, 130)}<div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['keys-4'] = K4Workbook;

// ─── Chords and Cadences, Grade 4: the Workbook (Build AX) ───
const H4_WB = {
  deg: [['C', 5], ['G', 4], ['F', 2], ['Am', 6], ['D', 6], ['Em', 4]],
  inv: [['G', 1], ['C', 4], ['D', 5], ['F', 2], ['Dm', 1], ['Am', 5]],
  cad: [['C', 'perfect'], ['F', 'imperfect'], ['G', 'interrupted'], ['Am', 'plagal']],
  harm: [[0, [1, 4, 2, 1, 5, 1]], [1, [1, 2, 5, 6, 5, 1]], [4, [1, 5, 6, 4, 5, 1]]],   // one way for each (the teacher's copy lists every chord that fits)
  chk: { deg: [['Bb', 6], ['E', 2], ['Gm', 4], ['A', 5]], inv: [['Eb', 1], ['Bm', 5], ['A', 4], ['Cm', 1]], cad: [['Bb', 'plagal'], ['Dm', 'interrupted'], ['E', 'imperfect'], ['Gm', 'perfect']], let: [['D', 4], ['Fsm', 5], ['Bb', 2], ['Cm', 6]] },
};
const H4_CAD_AB = { perfect: 'P', plagal: 'Pl', imperfect: 'Imp', interrupted: 'Int' };
const h4wHarm = (i) => { const M = H4_MEL[i]; return M.m.map(x => { const n = h3N(x); return h3Let(n) + ' (' + H4_DEGS(M.k).filter(d => h4Has(M.k, d, n)).map(d => h4Rom(M.k, d, 0)).join(', ') + ')'; }).join(' · '); };
const h4wChordCell = (k, deg, inv, n, ex, w = 104) => <ExCell key={k + deg} n={n} ex={ex}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{s4wLabel(h4Name(k))}
  <div style={{maxWidth:w,width:'100%',margin:'0 auto'}}><SatbStaff chords={[h4Chord(k, deg, inv)]} ks={H4_KEYS[k][2]} width={150}/></div>
  <div style={{display:'flex',justifyContent:'center'}}>{nvBox(ex, h4Rom(k, deg, inv), 50, 26)}</div></div></ExCell>;
function H4Workbook({ startNo = 1 }) {
  const W = H4_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="harmony-4">{content}</WbPage>);
  const rows = (items, n0) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{items.map(([l, w], i) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(i + n0)} {l} {bkBox(w || 50, 30)}</span>)}</div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the chord" how="Root position: the bass is the root. Count from the key's tonic and write the numeral: I, ii, IV, V, vi in a major key; i, iv, V, VI in a minor key.">
      <BkGrid cols={6} gap="6px 8px">{W.deg.map(([k, d], i) => h4wChordCell(k, d, 0, i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="Chords this week" how="Tick a box each day.">
      <PhLog rows={['G major: play I, ii, IV, V, vi, the root in the left hand', 'A minor: i, iv, V (with G♯) and VI', 'Name each chord by its root, then say its letters']} label={300}/>
    </Part>
    <Part kind="play" title="Spell the chord" how="Write the three letters, the root first.">
      {rows([['ii in G major', 110], ['VI in A minor', 110], ['V in E minor', 110]], 7)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="First inversions" how="The 3rd is in the bass. Find the root (stack the notes in 3rds) and write the numeral with b: Ib, iib, IVb, Vb …">
      <BkGrid cols={6} gap="6px 8px">{W.inv.map(([k, d], i) => h4wChordCell(k, d, 1, i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="First inversions this week" how="Tick a box each day.">
      <PhLog rows={['C major: I, IV, V in root position, then Ib, IVb, Vb', 'A minor: ib, ivb, and Vb with G♯ in the bass', 'Name a chord by its root, not by its bass note']} label={300}/>
    </Part>
    <Part kind="play" title="The bass note" how="In G major, which note is in the bass?">
      {rows([['Ib', 44], ['IVb', 44], ['Vb', 44]], 7)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Which cadence?" how="Write the two chords, then P (perfect, V–I), Pl (plagal, IV–I), Imp (imperfect, ending on V) or Int (interrupted, V–vi).">
      <BkGrid cols={4} gap="6px 8px">{W.cad.map(([k, c], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{s4wLabel(h4Name(k))}
        <div style={{maxWidth:150,width:'100%',margin:'0 auto'}}><SatbStaff chords={h4CadChords(k, c)} ks={H4_KEYS[k][2]} width={210}/></div>
        <div style={{display:'flex',justifyContent:'center',gap:6}}>{nvBox(i === 0, h4CadRom(k, c).join('–'), 64, 26)}{nvBox(i === 0, H4_CAD_AB[c], 40, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Cadences this week" how="Tick a box each day.">
      <PhLog rows={['C major and A minor: play the four cadences, the bass in the left hand', 'Listen: which one ends, which one waits, which one surprises?', 'Write one of each in four parts in G major']} label={300}/>
    </Part>
    <Part kind="play" title="Name it" how="Which cadence is it?">
      {rows([['the full stop', 110], ['the “Amen”', 110], ['the comma', 110], ['the surprise', 110]], 7)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Chords for a melody" how="Write a chord under every note: one that holds the note. End with a cadence (V–I).">
      <div style={{display:'grid',gap:8}}>{W.harm.map(([j, sel], i) => { const M = H4_MEL[j]; return <ExCell key={j} n={i + 1} ex={i === 0}><div style={{padding:'14px 4px 2px'}}>{s4wLabel(h4Name(M.k))}
        <div style={{maxWidth:420,margin:'0 auto'}}><K4Melody notes={M.m.map(h3N)} ks={H4_KEYS[M.k][2]} labels={i === 0 ? sel.map(d => h4Rom(M.k, d, 0)) : M.m.map(() => '_')} width={380}/></div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Harmonising this week" how="Tick a box each day.">
      <PhLog rows={['Play each melody with your chords: the root in the left hand, the tune in the right', 'End with a cadence: V–I for a full stop', 'Try two chords for the same note and hear the change']} label={300}/>
    </Part>
    <Part kind="play" title="Which chords hold it?" how="Write every chord (from I, ii, IV, V, vi) that holds the note.">
      {rows([['E in C major', 110], ['D in G major', 110]], 4)}
    </Part>
    <Faces/>
  </>);
  P(<H4PaperCheck/>);
  return <>{pages}</>;
}
function H4PaperCheck() {
  const C = H4_WB.chk;
  const cell = (k, deg, inv, n) => <BkCell key={n} n={n}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{h4Name(k)}</div><div style={{maxWidth:96,width:'100%',margin:'0 auto'}}><SatbStaff chords={[h4Chord(k, deg, inv)]} ks={H4_KEYS[k][2]} width={150} stems={false}/></div><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the chord (root position).')}
    <BkGrid cols={4} gap="6px 8px">{C.deg.map(([k, d], i) => cell(k, d, 0, i + 1))}</BkGrid>
    {bkSec('B', 'Name the chord (first inversion).')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map(([k, d], i) => cell(k, d, 1, i + 5))}</BkGrid>
    {bkSec('C', 'Which cadence? P, Pl, Imp or Int')}
    <BkGrid cols={4} gap="6px 8px">{C.cad.map(([k, c], i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{h4Name(k)}</div><div style={{maxWidth:116,width:'100%',margin:'0 auto'}}><SatbStaff chords={h4CadChords(k, c)} ks={H4_KEYS[k][2]} width={170} stems={false}/></div><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Write the three letters of the chord, the root first.')}
    <BkGrid cols={2} gap="6px 8px">{C.let.map(([k, d], i) => <BkCell key={i} n={i + 13}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,padding:'14px 4px 2px',fontSize:12.5,fontWeight:800,color:BK.ink}}>{h4Rom(k, d, 0)} in {h4Name(k)}{bkBox(110, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['harmony-4'] = H4Workbook;

// ─── Rhythm, Grade 4: the Workbook (Build AX) ───
Object.assign(R2, { c4A: { items: [['ts', 4], ['q'], ['e'], ['q'], ['e'], ['q'], ['|'], ['e'], ['q'], ['q'], ['q'], ['e'], ['||']], g: 4 },   // the check-up's two lines: two bars each
  c4B: { items: [['ts', 3], ['h'], ['q'], ['|'], ['q'], ['h'], ['||']], g: 4, ties: [[2, 4]] } });
const R4_WB = { bar: [0, 1, 3, 5], chk: { ts: [['6', '8', 'cd'], ['6', '4', 'cd'], ['12', '8', 'cq'], ['3', '4', 'st']], bar: 4 } };
function R4Workbook({ startNo = 1 }) {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="rhythm-4">{content}</WbPage>);
  const cnt = (keys) => <div style={{display:'grid',gap:10}}>{keys.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px'}}>{r2El(k, { counts: i === 0 ? 'ans' : 'blank', hearts: true })}</div></ExCell>)}</div>;
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 50, 30)}</span>)}</div>;
  const page = (step, title, how, keys, log, playT, playH, rows) => P(<>
    <WbTop step={step}/>
    <Part kind="together" title={title} how={how}>{cnt(keys)}</Part>
    <Part kind="home" title="This week" how="Tick a box each day.">
      <PhLog rows={log} label={300}/>
    </Part>
    <Part kind="play" title={playT} how={playH}>{quiz(rows)}</Part>
    <Faces/>
  </>);
  page(1, 'Count the syncopation', 'Write the count under every note (the grey boxes are counts held through). Then clap the line, counting aloud: the syncopated notes start between the beats.', ['syncA', 'syncB'],
    ['Count 1 + 2 + aloud and clap quaver, crotchet, quaver: the crotchet lands on the +', 'Clap line 1, then line 2, counting aloud', 'Find a syncopation in a piece you are learning'], 'Off the beat', 'Answer.',
    [['in 4/4, a minim starting on beat 2: syncopated? (Y or N)', 3], ['quaver, crotchet, quaver: which note is syncopated? (1, 2 or 3)', 4]]);
  page(2, 'Count the hemiola', 'Write the count under every note. The tie joins two notes into one sound: count through it. Then clap, feeling 2 + 2 + 2 across two bars.', ['hemA', 'hemB'],
    ['Count 1 2 3 | 1 2 3, then clap minims across the two bars: 2 + 2 + 2', 'Clap line 1 and line 2, counting aloud', 'Find a hemiola just before a cadence in a minuet or a courante'], 'Three twos', 'Answer.',
    [['two bars of 3/4 as a hemiola: how many groups of two?', 3], ['they sound like one bar of which time signature?', 4]]);
  page(3, 'Count 6/4 and 12/8', 'Write the count under every note. 6/4: two dotted-minim beats. 12/8: four dotted-crotchet beats. Then clap, leaning on each beat.', ['e64', 'e128'],
    ['6/4: count 1 to 6, leaning on 1 and 4', '12/8: count 1 to 12, leaning on 1, 4, 7 and 10', 'Clap each line, then walk the beat while you count'], 'Name the time', 'Simple or compound; duple, triple or quadruple?',
    [['6/4', 3, 170], ['12/8', 4, 170], ['9/8', 5, 170], ['3/2', 6, 170]]);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Draw the bar lines" how="Read the time signature: how many beats in a bar? Add up the notes and draw a bar line each time a bar is full. A phrase may start with an anacrusis.">
      <div style={{display:'grid',gap:8}}>{R4_WB.bar.map((j, i) => <ExCell key={j} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px',maxWidth:560,margin:'0 auto',width:'100%'}}>{r4BarEl(R4_BAR[j], i === 0 ? r4BarAt(R4_BAR[j]) : [])}</div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="This week" how="Tick a box each day.">
      <PhLog rows={['Bar a line of a piece you know, written out without bar lines', 'With an anacrusis: the last bar is short by the same amount', 'Clap each phrase, leaning on the first beat of every bar']} label={300}/>
    </Part>
    <Part kind="play" title="Full bars" how="Answer.">
      {quiz([['4/4 with an anacrusis of one beat: how many beats in the last bar?', 5], ['12/8: how many quavers in a bar?', 6]])}
    </Part>
    <Faces/>
  </>);
  P(<R4PaperCheck/>);
  return <>{pages}</>;
}
function R4PaperCheck() {
  const C = R4_WB.chk;
  const rows = (items, n0, w) => <BkGrid cols={2} gap="6px 8px">{items.map((l, i) => <BkCell key={i} n={i + n0}><div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,padding:'14px 4px 2px',fontSize:12.5,fontWeight:800,color:BK.ink}}>{l}{bkBox(w || 44, 24)}</div></BkCell>)}</BkGrid>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the counts under the notes.')}
    <div style={{display:'grid',gap:6}}>{['c4A', 'c4B'].map((k, i) => <BkCell key={k} n={i === 0 ? '1–2' : '3–4'}><div style={{padding:'14px 2px 0'}}>{r2El(k, { counts: 'blank', hearts: true })}</div></BkCell>)}</div>
    {bkSec('B', 'Simple or compound; duple, triple or quadruple?')}
    {rows(C.ts.map(([a, b]) => a + '/' + b), 5, 170)}
    {bkSec('C', 'How many?')}
    {rows(['crotchets in a bar of 6/4', 'dotted-crotchet beats in a bar of 12/8', 'minims in a hemiola across two bars of 3/4', 'quavers in a bar of 9/8'], 9)}
    {bkSec('D', 'Draw the four bar lines.')}
    <BkCell n="13–16"><div style={{padding:'14px 2px 0',maxWidth:560,margin:'0 auto',width:'100%'}}>{r4BarEl(R4_BAR[C.bar], [])}</div></BkCell>
  </div>;
}
WORKBOOKS['rhythm-4'] = R4Workbook;
'''
rep("""WORKBOOKS['rhythm-23'] = R2Workbook;""", """WORKBOOKS['rhythm-23'] = R2Workbook;""" + CODE)

# K4Melody: '_' in labels draws an empty box under the note (for the child to write a chord)
rep("""  const ys = [dY(38) - 10, dY(30) + 10, ...clefInkYs('treble', dY, 'treble')]; notes.forEach(nt => ys.push(dY(nt.d) - 36, dY(nt.d) + 36)); const yTop = Math.min(...ys), yBot = Math.max(...ys) + (labels ? 16 : 0);""",
    """  const ys = [dY(38) - 10, dY(30) + 10, ...clefInkYs('treble', dY, 'treble')]; notes.forEach(nt => ys.push(dY(nt.d) - 36, dY(nt.d) + 36)); const yTop = Math.min(...ys), yBot = Math.max(...ys) + (labels ? (labels.includes('_') ? 26 : 16) : 0);""")
rep("""        {labels && labels[i] && <text x={x} y={yBot - 3} textAnchor="middle" fontSize="11" fontWeight="900" fill={col} fontFamily="Inter, sans-serif">{labels[i]}</text>}</g>; })}""",
    """        {labels && labels[i] === '_' ? <rect x={x - 17} y={yBot - 23} width="34" height="21" rx="2" fill="#fff" stroke={BK.line} strokeWidth="1.3"/> : labels && labels[i] && <text x={x} y={yBot - 3} textAnchor="middle" fontSize="11" fontWeight="900" fill={col} fontFamily="Inter, sans-serif">{labels[i]}</text>}</g>; })}""")

# ── the teacher's copies gain the Workbook's answers and the scoring ──
# Scales and Arpeggios, Grade 4
rep("""    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns(""",
    """    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns('TRY IT', S4_WB.four.map(([k, h]) => s4wName(k) + ', ' + scfwHand(h) + ': ' + s4F4Note(k, h)))}{tcAns('PLAY', ['A♭ major RH, a middle octave: ' + s4Mid('Ab', 'R').join(' ')], null)}{tcAns(""")
rep("""    <TcBlock page={3} title="Four notes a beat" answers={<>{tcAns(""",
    """    <TcBlock page={3} title="Four notes a beat" answers={<>{tcAns('TRY IT: THE BEAT NOTES', S4_WB.touch.map(k => S4_ST[k].en + ': ' + s4wBeatNames(k).join(' ')))}{tcAns('PLAY', ['16', '7 (and the last note)', 'Y'], 3)}{tcAns(""")
rep("""    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns(""",
    """    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns('TRY IT', S4_CM_KEYS.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}{tcAns('PLAY', ['F♯ harmonic minor RH up: ' + SCF_CM.Fsmh.R.join(' ') + ' · LH down: ' + SCF_CM.Fsmh.L.join(' ')], null)}{tcAns(""")
rep("""    <TcBlock page={5} title="Chromatic, hands together" answers={<>{tcAns(""",
    """    <TcBlock page={5} title="Chromatic, hands together" answers={<>{tcAns('TRY IT', [0, 1].map(st => 'from ' + S4_CH[st][0] + ': RH ' + s4wChNames(st).map((_, j) => s4ChR(S4_CH[st][1] + j)).join(' ') + ' · LH ' + s4wChNames(st).map((_, j) => s4ChL(S4_CH[st][1] + j)).join(' ')))}{tcAns('PLAY', ['E, F, B, C'], 3)}{tcAns(""")
rep("""    <TcBlock page={6} title="Arpeggios: which finger?" answers={<>{tcAns(""",
    """    <TcBlock page={6} title="Arpeggios: which finger?" answers={<>{tcAns('TRY IT', S4_WB.arp.map(([k, h]) => S4_AR[k].en + ', ' + scfwHand(h) + ': ' + S4_AR[k][h].join(' ')))}{tcAns('PLAY', ['3', '4'], 7)}{tcAns(""")
rep("""    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one played to you from memory, in the Grade 4 keys, at the book's speeds. Listen for even groups of four, the same staccato, and the turns.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', S4_WB.chk.four.map(([k, h]) => s4F4Note(k, h)))}{tcAns('B', S4_WB.chk.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 5)}{tcAns('C', S4_WB.chk.chrom.map(([st, h, j]) => String((h === 'R' ? s4ChR : s4ChL)(S4_CH[st][1] + j))), 9)}{tcAns('D', S4_WB.chk.arp.map(([k, h, j]) => String(S4_AR[k][h][j])), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.4 · C p.5 · D p.6. Then hear each one at the piano, from memory, in the Grade 4 keys at the book's speeds: even groups of four, the same staccato, and smooth turns.</div></>}/>""")
# Keys and Intervals, Grade 4
rep("""    <TcBlock page={2} title="The Grade 4 keys" answers={<>{tcAns('MAJOR',""",
    """    <TcBlock page={2} title="The Grade 4 keys" answers={<>{tcAns('TRY IT', K4_WB.sig.map(k4wSig))}{tcAns('PLAY', ['D♭ major: B♭ E♭ A♭ D♭ G♭', 'F♯ minor: F♯ C♯ G♯'], 7)}{tcAns('MAJOR',""")
rep("""    <TcBlock page={3} title="The raised 7th" answers={<>{tcAns('HARMONIC MINOR 7TH',""",
    """    <TcBlock page={3} title="The raised 7th" answers={<>{tcAns('PLAY', ['F', 'C'], 6)}{tcAns('HARMONIC MINOR 7TH',""")
rep("""    <TcBlock page={4} title="Diatonic or chromatic?" answers={<>{tcAns('PAIRS',""",
    """    <TcBlock page={4} title="Diatonic or chromatic?" answers={<>{tcAns('TRY IT', K4_WB.semi.map(j => (k4SemiKind(j) === 'dia' ? 'D' : 'C')))}{tcAns('PLAY', ['G♭', 'F♯'], 7)}{tcAns('PAIRS',""")
rep("""    <TcBlock page={5} title="Above or below the tonic" answers={<>{tcAns(""",
    """    <TcBlock page={5} title="Above or below the tonic" answers={<>{tcAns('TRY IT', K4_WB.iv.map(k4wIv))}{tcAns('PLAY', K4_WB.inv.map(k4Inv), 7)}{tcAns(""")
rep("""    <TcBlock page={6} title="Where does the tune go?" answers={<>{tcAns('MELODIES',""",
    """    <TcBlock page={6} title="Where does the tune go?" answers={<>{tcAns('TRY IT', K4_WB.mod.map(j => k4wKey(K4_MOD[j][K4_MOD[j].to]) + ' ' + (K4_MOD[j].to === 'dom' ? 'D' : 'R') + ' (clue ' + h3Let(k4ModNotes(j)[K4_MOD[j].clue]) + ')'))}{tcAns('PLAY', ['F♯', 'G♯'], 4)}{tcAns('MELODIES',""")
rep("""    <TcBlock page={7} title="Transposing a melody" answers={<>{tcAns('MELODIES',""",
    """  </>);
  P(<>
    <TcBlock page={7} title="Transposing a melody" answers={<>{tcAns('PLAY', ['A', 'E', 'B♭'], 3)}{tcAns('MELODIES',""")
rep("""    <TcBlock page={8} title="My six checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>On paper or at the piano, in the Grade 4 keys, treble and bass.</div>}/>""",
    """    <TcBlock page={8} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', K4_WB.chk.sig.map(k4wSig))}{tcAns('B', K4_WB.chk.lead.map(k => K4_LEAD[k].lead), 5)}{tcAns('C', K4_WB.chk.semi.map(j => (k4SemiKind(j) === 'dia' ? 'D' : 'C')), 9)}{tcAns('D', K4_WB.chk.iv.map(k4wIv), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5. Modulation and transposition (pp.6 and 7) are checked on the Workbook pages themselves and at the piano.</div></>}/>""")
# Chords and Cadences, Grade 4
rep("""    <TcBlock page={2} title="Chords on every degree" answers={<>{tcAns(""",
    """    <TcBlock page={2} title="Chords on every degree" answers={<>{tcAns('TRY IT', H4_WB.deg.map(([k, d]) => h4Rom(k, d, 0)))}{tcAns('PLAY', [h4Letters('G', 2), h4Letters('Am', 6), h4Letters('Em', 5)], 7)}{tcAns(""")
rep("""    <TcBlock page={3} title="First inversions" answers={<>{tcAns(""",
    """    <TcBlock page={3} title="First inversions" answers={<>{tcAns('TRY IT', H4_WB.inv.map(([k, d]) => h4Rom(k, d, 1)))}{tcAns('PLAY', [1, 4, 5].map(d => h3Let(h4Chord('G', d, 1).B)), 7)}{tcAns(""")
rep("""    <TcBlock page={4} title="The four cadences" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>""",
    """    <TcBlock page={4} title="The four cadences" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{tcAns('TRY IT', H4_WB.cad.map(([k, c]) => h4CadRom(k, c).join('–') + ' ' + H4_CAD_AB[c]))}{tcAns('PLAY', ['perfect', 'plagal', 'imperfect', 'interrupted'], 7)}""")
rep("""    <TcBlock page={5} title="Chords for a melody" answers={<>{tcAns('ONE WAY TO HARMONISE EACH (others work)', H4_MEL.map(M => h4Name(M.k) + ': ' + M.m.map(x => h3Let(h3N(x))).join(' ')))}</>}""",
    """    <TcBlock page={5} title="Chords for a melody" answers={<>{tcAns('TRY IT: ONE WAY (any chord that holds its note is right; the last two must make a cadence)', H4_WB.harm.map(([j, sel]) => h4Name(H4_MEL[j].k) + ': ' + sel.map(d => h4Rom(H4_MEL[j].k, d, 0)).join(' ')))}{tcAns('EVERY CHORD THAT HOLDS EACH NOTE', H4_WB.harm.map(([j]) => h4Name(H4_MEL[j].k) + ': ' + h4wHarm(j)))}{tcAns('PLAY', [['C', 'E4'], ['G', 'D4']].map(([k, x]) => H4_DEGS(k).filter(d => h4Has(k, d, h3N(x))).map(d => h4Rom(k, d, 0)).join(', ')), 4)}</>}""")
rep("""    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>On paper and at the piano. One cadence of each kind written in four parts.</div>}/>""",
    """    <TcBlock page={6} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', H4_WB.chk.deg.map(([k, d]) => h4Rom(k, d, 0)))}{tcAns('B', H4_WB.chk.inv.map(([k, d]) => h4Rom(k, d, 1)), 5)}{tcAns('C', H4_WB.chk.cad.map(([, c]) => H4_CAD_AB[c]), 9)}{tcAns('D', H4_WB.chk.let.map(([k, d]) => h4Letters(k, d)), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.2. Then one cadence of each kind written in four parts, and played at the piano.</div></>}/>""")
# Rhythm, Grade 4
rep("""    <TcBlock page={2} title="Syncopation" answers={<div style={{display:'grid',gap:6}}>{['syncA', 'syncB'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>}""",
    """    <TcBlock page={2} title="Syncopation" answers={<><div style={{display:'grid',gap:6}}>{['syncA', 'syncB'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>{tcAns('PLAY', ['Y', '2 (the crotchet)'], 3)}</>}""")
rep("""    <TcBlock page={3} title="Hemiola" answers={<div style={{display:'grid',gap:6}}>{['hemA', 'hemB'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>}""",
    """    <TcBlock page={3} title="Hemiola" answers={<><div style={{display:'grid',gap:6}}>{['hemA', 'hemB'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>{tcAns('PLAY', ['3', '3/2'], 3)}</>}""")
rep("""    <TcBlock page={4} title="6/4 and 12/8" answers={<>{tcAns('SIMPLE OR COMPOUND',""",
    """    <TcBlock page={4} title="6/4 and 12/8" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px',marginBottom:4}}>{['e64', 'e128'].map(k => <div key={k}>{r2El(k, { counts: true, hearts: false })}</div>)}</div>{tcAns('PLAY', ['compound duple', 'compound quadruple', 'compound triple', 'simple triple'], 3)}{tcAns('SIMPLE OR COMPOUND',""")
rep("""    <TcBlock page={5} title="Bar lines for a phrase" answers={<div style={{display:'grid',gap:6}}>{R4_BAR.map((x, j) => <div key={j}>{r4BarEl(x, r4BarAt(x))}</div>)}</div>}""",
    """    <TcBlock page={5} title="Bar lines for a phrase" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{R4_BAR.map((x, j) => <div key={j} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(j + 1)}<div style={{flex:1,minWidth:0}}>{r4BarEl(x, r4BarAt(x))}</div></div>)}</div><div style={{fontSize:12,color:BK.ink,margin:'4px 0'}}><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>TRY IT</b>  Workbook 1–4 are phrases {R4_WB.bar.map(j => j + 1).join(', ')} above.</div>{tcAns('PLAY', ['3', '12'], 5)}</>}""")
rep("""    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Clap each line with the beat said aloud; bar a phrase from a piece the child is learning.</div>}/>""",
    """  </>);
  P(<>
    <TcBlock page={6} title="The check-up on paper (the Workbook's last page)" answers={<><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px',marginBottom:4}}>{['c4A', 'c4B'].map(k => <div key={k} style={{maxWidth:k === 'c4B' ? 190 : 320}}>{r2El(k, { counts: 'ans', hearts: false })}</div>)}</div>{tcAns('B', R4_WB.chk.ts.map(([, , c]) => R4_TSN[c][0]), 5)}{tcAns('C', ['6', '4', '3', '9'], 9)}
      <div style={{maxWidth:420,margin:'4px 0'}}>{r4BarEl(R4_BAR[R4_WB.chk.bar], r4BarAt(R4_BAR[R4_WB.chk.bar]))}</div>
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Part A: one mark for each bar counted right (4 marks). Parts B and C: one mark each. Part D: one mark for each bar line in the right place (4 marks). Score each part on its own (pass 3+). Not passed? Go back: A p.2 and p.3 · B p.4 · C p.3 and p.4 · D p.5. Then clap each line with the beat said aloud, and bar a phrase from a piece the child is learning.</div></>}/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
