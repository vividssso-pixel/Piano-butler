import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BD (board call 23): the Workbooks for the Grade 5 rooms, as Build AX made them for Grade 4: one page facing each Lesson
# Book step (try it with an example, at home this week, play), then the check-up on paper (four parts of four marks, pass 3+);
# the teacher's copies gain every answer and the scoring. Hear and Sing, Grade 5 has no Workbook (all by ear), as Grade 4.

rep("""const s4wName = (k) => S4_SC[k].en + (k === 'Csmel' ? ', going up' : '');""", """const s4wName = (k) => S4_SC[k].en + (S4_SC[k].dn ? ', going up' : '');""")

WB = r'''
// ─── Scales and Arpeggios, Grade 5: the Workbook (Build BD) ───
const S5_WB = {
  four: [['B', 'R'], ['B', 'L'], ['Gsm', 'R'], ['Db', 'L'], ['Bbm', 'R'], ['Bbmel', 'L']],
  ways: ['cd', 'p', 'st', 'f'],
  arp: [['B', 'R'], ['B', 'L'], ['Bm', 'L'], ['Db', 'R'], ['Dbm', 'L'], ['Db', 'L']],
  chk: { four: [['Gsm', 'L'], ['Db', 'R'], ['Bbm', 'L'], ['B', 'R']], mirror: ['E5', 'Csmh', 'Ab5', 'Fmh'], chrom: [[0, 'R', 0], [0, 'L', 0], [1, 'R', 4], [1, 'L', 10]], arp: [['B', 'L', 1], ['Bm', 'L', 1], ['Db', 'R', 1], ['Dbm', 'L', 2]] },
};
const S5_WAY_AB = { p: 'p', f: 'f', cd: '< >', st: 'st' };
function S5Workbook({ startNo = 1 }) {
  const W = S5_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-5">{content}</WbPage>);
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 44, 30)}</span>)}</div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which note does finger 4 play?" how="One octave of each scale, the thumbs shown. Finger 4 plays once an octave, always the same note: write it.">
      <BkGrid cols={3} gap="6px 10px">{W.four.map((it, i) => <S4wFourCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Four octaves this week" how="Do each one at the piano and tick a box each day. Find the 4s before you start.">
      <PhLog rows={s4wRows(['B major, each hand: the right hand\'s 4 on A♯, the left hand\'s on F♯ (and the bottom B)', 'G♯ minor, D♭ major and B♭ minor: the right hand\'s 4 on the same black key, A♯ = B♭', 'Hands together, four notes a beat, up to ♩ = 84'])} label={300}/>
    </Part>
    <Part kind="play" title="D♭ major, right hand" how="A middle octave, from D♭ to D♭. Write the finger under each letter: it starts on 2.">
      <div style={{display:'grid',gap:6,padding:'6px 0'}}>{scfwLetters(S4_SC.Db.nm.concat([S4_SC.Db.nm[0]]), 38)}<div style={{display:'flex',gap:3,justifyContent:'center'}}>{S4_SC.Db.nm.concat(['']).map((_, j) => <span key={j}>{bkBox(38, 30)}</span>)}</div></div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Which way?" how="The thicker the line, the louder; dots are staccato. Write the way under each picture: p, f, &lt; &gt; (louder up, softer down) or st (staccato).">
      <BkGrid cols={2} gap="6px 10px">{W.ways.map((m, i) => <ExCell key={m} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}><S5Ribbon m={m} w={260} marks={false}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, S5_WAY_AB[m], 60, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Four ways this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['D♭ major, one octave: all p, then all f; every note even', 'Four octaves: p at the bottom, f at the top, p again at the end', 'Staccato D♭ major and B♭ melodic minor: the same fingers, short, up to ♩ = 60'])} label={300}/>
    </Part>
    <Part kind="play" title="Loud and soft" how="Write the answer.">
      {quiz([['louder up, softer down: which note is the loudest?', 5, 70], ['all f: do the fingers change? (Y or N)', 6], ['staccato: how many notes in a beat?', 7]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Mirror twins, or not?" how="Contrary motion from one note: the right hand's fingers above, the left hand's below. Same numbers all the way? Write Y. Not? Write N.">
      <BkGrid cols={2} gap="6px 10px">{S5_CM_KEYS.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
        {s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={11} H={40} kk={1.1}/>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>mirror twins? {nvBox(i === 0, scfMirror(k) ? 'Y' : 'N', 34, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Contrary motion this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['E major: the same numbers both ways', 'C♯ minor and A♭ major: both hands start on 2; say each hand\'s numbers', 'F minor, then all four, two octaves, up to ♩ = 60'])} label={300}/>
    </Part>
    <Part kind="play" title="A♭ major, contrary motion" how="Both hands start on the same A♭. Write each hand's fingers under its letters.">
      <div style={{display:'grid',gap:5,padding:'4px 0'}}>{[['RH ↗', scfCm('Ab5').nmR], ['LH ↘', scfCm('Ab5').nmL]].map(([l, nm]) => <div key={l} style={{display:'grid',gap:3}}>{s4wRow(l, scfwLetters(nm, 30))}{s4wRow('', <div style={{display:'flex',gap:3}}>{nm.map((_, j) => <span key={j}>{bkBox(30, 26)}</span>)}</div>)}</div>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Both hands' fingers" how="The chromatic scale going up, hands together. Write the right hand's finger above each letter and the left hand's below: 3 on black keys, 1 on white keys, 2 where two white keys sit together.">
      <div style={{display:'grid',gap:10}}>{[0, 1].map(st => { const s0 = S5_CH[st][1], K = Array.from({ length: 13 }, (_, j) => s0 + j), N = K.map(s4ChLet);
        return <ExCell key={st} n={st + 1} ex={st === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel('From ' + S5_CH[st][0] + ', one octave up')}
          {s4wRow('RH', <div style={{display:'flex',gap:3}}>{K.map((x, j) => <span key={j}>{nvBox(st === 0, String(s4ChR(x)), 28, 24)}</span>)}</div>)}
          {s4wRow('', scfwLetters(N, 28))}
          {s4wRow('LH', <div style={{display:'flex',gap:3}}>{K.map((x, j) => <span key={j}>{nvBox(st === 0, String(s4ChL(x)), 28, 24)}</span>)}</div>)}</div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Chromatic this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['From B, each hand, one octave: the right hand starts on 1, the left on 2', 'Hands together, all p: every note still sounds', 'From B and from C♯/D♭, four octaves, all p and all f, up to ♩ = 84'])} label={300}/>
    </Part>
    <Part kind="play" title="From B" how="Which finger starts?">
      {quiz([['the right hand, on B', 3, 40], ['the left hand, on B', 4, 40]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Arpeggio fingers" how="Two octaves going up, as the book prints them. Write the finger under each letter.">
      <BkGrid cols={2} gap="6px 10px">{W.arp.map((it, i) => <S4wArpCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Arpeggios this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['B major and minor, each hand: the thumb on B', 'D♭ major and minor: find the thumb\'s F (F♭ in the minor) first', 'Hands together, four notes a beat, up to ♩ = 52'])} label={300}/>
    </Part>
    <Part kind="play" title="The thumb's white key" how="Write the note the thumb plays.">
      {quiz([['D♭ major', 7], ['D♭ minor', 8]])}
    </Part>
    <Faces/>
  </>);
  P(<S5PaperCheck/>);
  return <>{pages}</>;
}
function S5PaperCheck() {
  const C = S5_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which note does finger 4 play in every octave?')}
    <BkGrid cols={4} gap="6px 8px">{C.four.map((it, i) => <S4wFourCell key={i} item={it} n={i + 1} small/>)}</BkGrid>
    {bkSec('B', 'Contrary motion from one note: mirror twins? Y or N')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((k, i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:6,padding:'14px 0 0'}}><div>{s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={9} H={24} kk={1} bare/></div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Chromatic scale: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.chrom.map(([st, h, j], i) => { const s0 = S5_CH[st][1]; return <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>From {S5_CH[st][0]}, {scfwHand(h)}</div><SpKb lo={s0} hi={s0 + 12} W={10} H={28} lit={{ [s0 + j]: 'cor' }} names={{ [s0]: s4ChLet(s0) }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('D', 'Arpeggio: which finger plays the coral key?')}
    <BkGrid cols={4} gap="6px 8px">{C.arp.map(([k, h, j], i) => { const c = S4_AR[k], K = s4ArKeys(k), lit = Object.fromEntries(K.map(x => [x, 'pale'])); lit[K[j]] = 'cor'; return <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>{c.en}, {scfwHand(h)}</div><SpKb lo={c.r} hi={c.r + 24} W={8} H={26} lit={lit} names={{}} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
  </div>;
}
WORKBOOKS['scales-5'] = S5Workbook;

// ─── Keys and Intervals, Grade 5: the Workbook (Build BD) ───
const K5_WB = {
  sig: [['sharp', 7, false, 'treble'], ['flat', 7, false, 'treble'], ['sharp', 5, true, 'bass'], ['flat', 6, true, 'treble'], ['sharp', 7, true, 'bass'], ['flat', 7, true, 'treble']],
  mel: ['Gsm', 'Dsm', 'Asm', 'Ebm', 'Abm'],
  iv: [0, 2, 6, 8, 10, 4],
  inv: [0, 6, 4, 13, 12, 10],
  mod: [1, 3, 8],
  chk: { sig: [['flat', 6, false, 'bass'], ['sharp', 6, true, 'treble'], ['sharp', 7, false, 'bass'], ['flat', 7, true, 'bass']], mel: ['Asm', 'Ebm', 'Csm', 'Bbm'], iv: [1, 3, 9, 11], inv: [2, 7, 5, 14] },
};
const k5wMelRow = (k, ex, size = 30) => { const sig = k5Sig(K5M[k].ks), L = Array.from({ length: 8 }, (_, x) => k5Let(k5MNote(k, x, 'mel'), sig)); return <div style={{display:'flex',gap:3,justifyContent:'center',alignItems:'center'}}>
  <span style={{width:74,fontSize:11,fontWeight:900,color:BK.muted}}>{K5M[k].en}</span>{L.map((x, j) => <span key={j}>{j === 5 || j === 6 ? nvBox(ex, x, size, size) : k4wLet(x, size)}</span>)}</div>; };
const k5wIvStaff = (i, w) => <IntervalStaff clef="treble" notes={K5_AD[i].map(h3N)} labels={K5_AD[i].map(x => h3Let(h3N(x)))} width={w}/>;
const k5wIv = (i) => { const ns = K5_AD[i].map(h3N); return k5Iv(ns[0], ns[1]); };
const k5wKey = (id) => (id.endsWith('m') ? id.slice(0, -1) + ' minor' : id + ' major');
function K5Workbook({ startNo = 1 }) {
  const W = K5_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="keys-5">{content}</WbPage>);
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 50, 30)}</span>)}</div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the key" how="Read the key signature. Write the major or minor key it asks for. Sharps: up a semitone from the last sharp. Flats: the second-last flat. Minor: three semitones below the major.">
      <BkGrid cols={3} gap="6px 10px">{W.sig.map((it, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
        <div style={{maxWidth:160,width:'100%',margin:'0 auto'}}><KSStaff count={it[1]} type={it[0]} width={180} clef={it[3]} accent={BK.ink} ink={BK.ink}/></div>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11.5,fontWeight:800,color:BK.ink}}>{it[2] ? 'minor:' : 'major:'} {nvBox(i === 0, k4wSig(it), 96, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Key signatures this week" how="Tick a box each day.">
      <PhLog rows={['Write C♯ major and C♭ major, treble and bass: all seven sharps, all seven flats', 'G♯, D♯, A♯, E♭ and A♭ minor: each three semitones below its relative major', 'The same keys, two names: B = C♭, F♯ = G♭, C♯ = D♭']} label={300}/>
    </Part>
    <Part kind="play" title="Write the key signature" how="On each staff, write the key signature.">
      <div style={{display:'flex',gap:20,justifyContent:'center',flexWrap:'wrap',padding:'4px 0'}}>{[['C♯ major', 7, 'treble'], ['E♭ minor', 8, 'bass']].map(([l, n, clef]) => <div key={l} style={{display:'grid',gap:2,justifyItems:'center'}}><span style={{fontSize:13,fontWeight:800,color:BK.ink}}>{nvNum(n)} {l}</span><div style={{width:180}}><KSStaff count={0} type="sharp" width={180} clef={clef} accent={BK.ink} ink={BK.ink}/></div></div>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="The melodic minor, going up" how="Each melodic minor going up, its 6th and 7th left out. Write them, each raised a semitone from the key signature: a sharp becomes a double sharp (𝄪), a flat a natural (♮).">
      <div style={{display:'grid',gap:6}}>{W.mel.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 2px'}}>{k5wMelRow(k, i === 0)}</div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Both forms this week" how="Tick a box each day.">
      <PhLog rows={['Play each one, harmonic then melodic: hear the 6th rise as well', 'Coming down, the melodic minor goes back to the key signature', 'Write G♯ melodic minor up and down, with every accidental']} label={300}/>
    </Part>
    <Part kind="play" title="Coming down" how="G♯ melodic minor, coming down: write the 7th and the 6th.">
      {quiz([['the 7th', 6, 44], ['the 6th', 7, 44]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Name the interval" how="Count the letters for the number, then the semitones for the quality. Augmented: one more than perfect or major. Diminished: one less than perfect or minor. Write A4, d5 and so on.">
      <BkGrid cols={3} gap="6px 10px">{W.iv.map((j, i) => <ExCell key={j} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{k5wIvStaff(j, 150)}
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, k5wIv(j), 50, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Intervals this week" how="Tick a box each day.">
      <PhLog rows={['Play C–F♯, then C–G♭: the same keys, a 4th and a 5th', 'In A harmonic minor: F–G♯ (augmented 2nd), G♯–F (diminished 7th)', 'Sing each one after you play it']} label={300}/>
    </Part>
    <Part kind="play" title="The same keys" how="Name each interval.">
      {quiz([['C up to F♯', 7], ['C up to G♭', 8]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Turn it upside down" how="Write the inversion. The numbers add to 9; major and minor swap; augmented and diminished swap; perfect stays perfect.">
      <BkGrid cols={3} gap="6px 10px">{W.inv.map((j, i) => <ExCell key={j} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{k5wIvStaff(j, 150)}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:12,fontWeight:800,color:BK.ink}}>{k5wIv(j)} → {nvBox(i === 0, k5Inv(k5wIv(j)), 50, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Inversions this week" how="Tick a box each day.">
      <PhLog rows={['Play an interval, then move the lower note up an octave', 'Add to 9: a 4th becomes a 5th, a 2nd a 7th', 'Augmented 4th ↔ diminished 5th; augmented 2nd ↔ diminished 7th']} label={300}/>
    </Part>
    <Part kind="play" title="Quick inversions" how="Write the inversion.">
      <div style={{display:'flex',gap:22,justifyContent:'center',flexWrap:'wrap',fontSize:13.5,fontWeight:800,color:BK.ink,padding:'8px 0'}}>{['A2', 'd4', 'M6', 'P5'].map((id, i) => <span key={id} style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(i + 7)} {id} → {bkBox(44, 30)}</span>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Where does the tune go?" how="Circle the note that tells: a new sharp, flat or natural. Then write the new key, and D (dominant), S (subdominant) or R (relative).">
      <div style={{display:'grid',gap:8}}>{W.mod.map((j, i) => { const m = K5_MOD[j]; return <ExCell key={j} n={i + 1} ex={i === 0}><div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) auto',gap:10,alignItems:'center',padding:'14px 4px 2px'}}>
        <div style={{minWidth:0,maxWidth:430}}>{s4wLabel('Starts in ' + k5wKey(m.h))}<K4Melody notes={k5ModNotes(j)} ks={m.ks} hi={i === 0 ? [m.clue] : []} width={360}/></div>
        <div style={{display:'grid',gap:6,justifyItems:'center',fontSize:11,fontWeight:800,color:BK.muted}}>new key {nvBox(i === 0, k5wKey(m[m.to]), 100, 26)}{nvBox(i === 0, ({ dom: 'D', sub: 'S', rel: 'R' })[m.to], 34, 26)}</div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Modulation this week" how="Tick a box each day.">
      <PhLog rows={['Play each tune; stop on the note that tells, and name the new key', 'To the subdominant from a major key: a lowered note (B♭ in C major)', 'To the dominant: a raised note, its leading note (F♯ in C major)']} label={300}/>
    </Part>
    <Part kind="play" title="The note that tells" how="A tune in G major. Which note would take it there?">
      {quiz([['to C major', 4, 44], ['to D major', 5, 44]])}
    </Part>
    <Faces/>
  </>);
  P(<K5PaperCheck/>);
  return <>{pages}</>;
}
function K5PaperCheck() {
  const C = K5_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the key (major or minor, as asked).')}
    <BkGrid cols={4} gap="6px 8px">{C.sig.map((it, i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}><div style={{maxWidth:150,width:'100%',margin:'0 auto'}}><KSStaff count={it[1]} type={it[0]} width={180} clef={it[3]} accent={BK.ink} ink={BK.ink}/></div>
      <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:5,fontSize:10.5,fontWeight:800,color:BK.muted}}>{it[2] ? 'minor' : 'major'} {bkBox(70, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('B', 'The melodic minor going up: write the 6th and the 7th.')}
    <BkGrid cols={2} gap="6px 8px">{C.mel.map((k, i) => <BkCell key={k} n={i + 5}><div style={{padding:'14px 0 0'}}>{k5wMelRow(k, false, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Name the interval (A, d, M, m or P and the number).')}
    <BkGrid cols={4} gap="6px 8px">{C.iv.map((j, i) => <BkCell key={j} n={i + 9}><div style={{display:'grid',gap:2,padding:'14px 0 0'}}>{k5wIvStaff(j, 130)}<div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Write the inversion.')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map((j, i) => <BkCell key={j} n={i + 13}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,padding:'14px 0 2px',fontSize:13,fontWeight:800,color:BK.ink}}>{k5wIv(j)} → {bkBox(40, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['keys-5'] = K5Workbook;

// ─── Chords and Cadences, Grade 5: the Workbook (Build BD) ───
const H5_WB = {
  inv: [['C', 7], ['G', 2], ['F', 5], ['D', 4], ['Am', 7], ['Bb', 6]],
  c64: [['C', 2], ['G', 1], ['Dm', 2], ['F', 0]],
  pass: [0, 3, 4],
  pre: [['C', 'c64'], ['G', 'iib'], ['F', 'ivb'], ['Am', 'vi']],
  harm: [[0, [[1, 0], [5, 0], [4, 0], [1, 0], [4, 0], [1, 2], [5, 0], [1, 0]]], [1]],
  chk: { inv: [['D', 7], ['Bb', 2], ['Em', 4], ['A', 5]], c64: [['A', 2], ['Bb', 0], ['Em', 1], ['Gm', 2]], pass: [[6, 1], [7, 3], [1, 5], [5, 3]], pre: [['D', 'ivb'], ['Bb', 'c64'], ['Em', 'vi'], ['A', 'iib']] },
};
const h5wInvCell = (k, deg, n, ex) => <ExCell key={k + deg} n={n} ex={ex}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{s4wLabel(h4Name(k))}
  <div style={{maxWidth:104,width:'100%',margin:'0 auto'}}><SatbStaff chords={[h5Chord(k, deg, 1)]} ks={H4_KEYS[k][2]} width={150}/></div>
  <div style={{display:'flex',justifyContent:'center'}}>{nvBox(ex, h5Rom(k, deg, 1), 54, 26)}</div></div></ExCell>;
const h5wProgCell = (k, nm, ans, n, ex) => <ExCell key={k + nm} n={n} ex={ex}><div style={{display:'grid',gap:2,padding:'16px 2px 2px'}}>{s4wLabel(h4Name(k))}
  <div style={{maxWidth:150,width:'100%',margin:'0 auto'}}><SatbStaff chords={h5Prog(k, nm)} ks={H4_KEYS[k][2]} labels={['?', 'V', h5Rom(k, 1, 0)]} width={220}/></div>
  <div style={{display:'flex',justifyContent:'center'}}>{nvBox(ex, ans, 54, 26)}</div></div></ExCell>;
const H5_PASS_AB = { chord: 'c', pass: 'p', aux: 'a' };
const h5wPassLabels = (i, show) => H5_PASS[i].m.map((_, x) => (x % 2 === 0 ? h5Rom(H5_PASS[i].k, H5_PASS[i].c[x / 2], 0) : show ? H5_PASS_AB[h5PassKind(i, x)] : '_'));
function H5Workbook({ startNo = 1 }) {
  const W = H5_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="harmony-5">{content}</WbPage>);
  const rows = (items, n0) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{items.map(([l, w], i) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(i + n0)} {l} {bkBox(w || 50, 30)}</span>)}</div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the first inversion" how="The 3rd is in the bass. Stack the notes in 3rds to find the root, and write the numeral with b: Ib, iib, IVb, Vb, vib, or vii°b for the chord on the leading note.">
      <BkGrid cols={6} gap="6px 8px">{W.inv.map(([k, d], i) => h5wInvCell(k, d, i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="First inversions this week" how="Tick a box each day.">
      <PhLog rows={['C major: I, vii°b, Ib: the bass climbs C, D, E', 'G major: every first inversion; say each one\'s bass note', 'A minor: vii°b is G♯ B D with B in the bass']} label={300}/>
    </Part>
    <Part kind="play" title="Spell vii°b" how="Write the three letters, the root first.">
      {rows([['vii°b in G major', 110], ['vii°b in F major', 110]], 7)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="I, Ib or Ic?" how="The first chord is the tonic chord. Which note of it is in the bass? Root: I. 3rd: Ib. 5th, the same bass as V: Ic.">
      <BkGrid cols={4} gap="6px 8px">{W.c64.map(([k, p], i) => h5wProgCell(k, ['r64', 'b64', 'c64'][p], h5Rom(k, 1, p), i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="The cadential 6-4 this week" how="Tick a box each day.">
      <PhLog rows={['C major: hold G in the bass; C and E above it fall to B and D: Ic–V', 'Then on to I: Ic–V–I', 'Play it in G, F and A minor']} label={300}/>
    </Part>
    <Part kind="play" title="Ic" how="Write the answer.">
      {rows([['the bass note of Ic in C major', 50], ['the chord that comes after Ic', 50]], 5)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Passing or auxiliary?" how="The chords change on the named notes. Under each note between them write p (passing: a step through), a (auxiliary: a step away and back) or c (a note of the chord).">
      <div style={{display:'grid',gap:8}}>{W.pass.map((j, i) => { const M = H5_PASS[j]; return <ExCell key={j} n={i + 1} ex={i === 0}><div style={{padding:'10px 4px 0'}}>{s4wLabel(h4Name(M.k))}
        <div style={{maxWidth:360,margin:'0 auto'}}><K4Melody notes={M.m.map(h3N)} ks={H4_KEYS[M.k][2]} labels={h5wPassLabels(j, i === 0)} width={330}/></div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Passing notes this week" how="Tick a box each day.">
      <PhLog rows={['Play each melody with its chords on the named notes', 'Sing it: lean on the strong notes', 'Make up a passing note between notes a 3rd apart']} label={300}/>
    </Part>
    <Part kind="play" title="Fill the gap" how="Write the note.">
      {rows([['a passing note between C and E', 44], ['an auxiliary note above G', 44]], 4)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="The chord before V" how="A perfect cadence with a chord before it. Name that first chord: iib, IV, IVb or Ic in a major key; iv, ivb, VI or ic in a minor key.">
      <BkGrid cols={4} gap="6px 8px">{W.pre.map(([k, o], i) => h5wProgCell(k, o, h5PreRom(k, o), i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="Cadences this week" how="Tick a box each day.">
      <PhLog rows={['C major: iib–V–I, IV–V–I, IVb–V–I, Ic–V–I', 'Hear which one leads into V most smoothly for you', 'Write one in four parts in G major']} label={300}/>
    </Part>
    <Part kind="play" title="Before V in C major" how="Write the numeral.">
      {rows([['F A C, root position', 50], ['D F A, F in the bass', 50], ['C E G, G in the bass', 50]], 5)}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Harmonise eight notes" how="Write a chord under every note: one that holds it. Start on the tonic, and end with a cadence; Ic–V–I where the melody allows.">
      <div style={{display:'grid',gap:8}}>{W.harm.map(([j, sel], i) => { const M = H5_MEL[j]; return <ExCell key={j} n={i + 1} ex={i === 0}><div style={{padding:'14px 4px 2px'}}>{s4wLabel(h4Name(M.k))}
        <div style={{maxWidth:440,margin:'0 auto'}}><K4Melody notes={M.m.map(h3N)} ks={H4_KEYS[M.k][2]} labels={sel ? sel.map(x => h5Rom(M.k, x[0], x[1])) : M.m.map(() => '_')} width={400}/></div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Harmonising this week" how="Tick a box each day.">
      <PhLog rows={['Play the melody with your chords: the bass in the left hand', 'Try a first inversion where the bass would rather step', 'Write the four parts on paper with your teacher']} label={300}/>
    </Part>
    <Part kind="play" title="Which chords hold it?" how="Write every chord (I, ii, IV, V, vi) that holds the note.">
      {rows([['A in C major', 110], ['F♯ in G major', 110]], 3)}
    </Part>
    <Faces/>
  </>);
  P(<H5PaperCheck/>);
  return <>{pages}</>;
}
function H5PaperCheck() {
  const C = H5_WB.chk;
  const lab = (k) => <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center'}}>{h4Name(k)}</div>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the first inversion.')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map(([k, d], i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:2,padding:'12px 0 0'}}>{lab(k)}<div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8}}><div style={{width:84,flex:'none'}}><SatbStaff chords={[h5Chord(k, d, 1)]} ks={H4_KEYS[k][2]} width={150} stems={false}/></div>{bkBox(44, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('B', 'The first chord: I, Ib or Ic?')}
    <BkGrid cols={4} gap="6px 8px">{C.c64.map(([k, p], i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:2,padding:'12px 0 0'}}>{lab(k)}<div style={{maxWidth:118,width:'100%',margin:'0 auto'}}><SatbStaff chords={h5Prog(k, ['r64', 'b64', 'c64'][p])} ks={H4_KEYS[k][2]} width={220} stems={false}/></div><div style={{display:'flex',justifyContent:'center'}}>{bkBox(40, 24)}</div></div></BkCell>)}</BkGrid>
    {bkSec('C', 'The coral note: p (passing), a (auxiliary) or c (chord note)?')}
    <BkGrid cols={2} gap="6px 8px">{C.pass.map(([j, x], i) => { const M = H5_PASS[j]; return <BkCell key={i} n={i + 9}><div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) auto',alignItems:'center',gap:6,padding:'10px 0 0'}}><div style={{minWidth:0}}><K4Melody notes={M.m.map(h3N)} ks={H4_KEYS[M.k][2]} hi={[x]} labels={h5PassLabels(j)} width={300}/></div>{bkBox(30, 24)}</div></BkCell>; })}</BkGrid>
    {bkSec('D', 'Name the chord before V.')}
    <BkGrid cols={4} gap="6px 8px">{C.pre.map(([k, o], i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:2,padding:'12px 0 0'}}>{lab(k)}<div style={{maxWidth:118,width:'100%',margin:'0 auto'}}><SatbStaff chords={h5Prog(k, o)} ks={H4_KEYS[k][2]} width={220} stems={false}/></div><div style={{display:'flex',justifyContent:'center'}}>{bkBox(44, 24)}</div></div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['harmony-5'] = H5Workbook;
'''
rep("""WORKBOOKS['harmony-4'] = H4Workbook;""", """WORKBOOKS['harmony-4'] = H4Workbook;""" + WB)

# ── the teacher's copies: the Workbook's answers and the check-up's scoring ──
rep("""    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns(spTx('SIMILAR MOTION, FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, ♩ = 84""",
    """    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns('TRY IT', S5_WB.four.map(([k, h]) => s4wName(k) + ', ' + scfwHand(h) + ': ' + s4F4Note(k, h)))}{tcAns('PLAY', ['D♭ major RH, a middle octave: ' + s4Mid('Db', 'R').join(' ')], null)}{tcAns(spTx('SIMILAR MOTION, FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, ♩ = 84""")
rep("""    <TcBlock page={3} title="One scale, four ways" answers={<>{tcAns(spTx('EVERY SCALE ABOVE, ♩ = 84')""",
    """    <TcBlock page={3} title="One scale, four ways" answers={<>{tcAns('TRY IT', S5_WB.ways.map(m => S5_WAY_AB[m]))}{tcAns('PLAY', ['the top note', 'N', '4'], 5)}{tcAns(spTx('EVERY SCALE ABOVE, ♩ = 84')""")
rep("""    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns('MIRROR TWINS?', S5_CM_KEYS.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}""",
    """    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns('TRY IT', S5_CM_KEYS.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}{tcAns('PLAY', ['A♭ major RH up: ' + SCF_CM.Ab5.R.join(' ') + ' · LH down: ' + SCF_CM.Ab5.L.join(' ')], null)}""")
rep("""    <TcBlock page={5} title="Chromatic from B and C♯" answers={<>{tcAns('FROM B', """,
    """    <TcBlock page={5} title="Chromatic from B and C♯" answers={<>{tcAns('TRY IT, FROM C♯', ['RH ' + Array.from({ length: 13 }, (_, j) => s4ChR(1 + j)).join(' '), 'LH ' + Array.from({ length: 13 }, (_, j) => s4ChL(1 + j)).join(' ')], null)}{tcAns('PLAY', ['1', '2'], 3)}{tcAns('FROM B', """)
rep("""    <TcBlock page={6} title="Arpeggios, four notes a beat" answers={<>{tcAns(spTx('FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, mf, ♩ = 52 FOUR NOTES A BEAT'), [arp('B'), arp('Bm'), arp('Db'), arp('Dbm')])}</>}""",
    """    <TcBlock page={6} title="Arpeggios, four notes a beat" answers={<>{tcAns('TRY IT', S5_WB.arp.map(([k, h]) => S4_AR[k].en + ', ' + scfwHand(h) + ': ' + S4_AR[k][h].join(' ')))}{tcAns('PLAY', ['F', 'F♭'], 7)}{tcAns(spTx('FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, mf, ♩ = 52 FOUR NOTES A BEAT'), [arp('B'), arp('Bm'), arp('Db'), arp('Dbm')])}</>}""")
rep("""    <TcBlock page={7} title="The check-up" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one at the piano, from memory, in the Grade 5 keys at the book's speeds: every scale all p, all f and with the hairpins; the staccato pair; contrary motion; chromatic in p and in f; arpeggios hands separately and together. Listen for the top of the crescendo, even groups of four, and smooth thumbs.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', S5_WB.chk.four.map(([k, h]) => s4F4Note(k, h)))}{tcAns('B', S5_WB.chk.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 5)}{tcAns('C', S5_WB.chk.chrom.map(([st, h, j]) => String((h === 'R' ? s4ChR : s4ChL)(S5_CH[st][1] + j))), 9)}{tcAns('D', S5_WB.chk.arp.map(([k, h, j]) => String(S4_AR[k][h][j])), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.4 · C p.5 · D p.6. Then hear each one at the piano, from memory, in the Grade 5 keys at the book's speeds: every scale all p, all f and with the hairpins; the staccato pair; contrary motion; chromatic in p and in f; arpeggios hands separately and together.</div></>}/>""")

rep("""    <TcBlock page={2} title="Every key, up to seven" answers={<>{tcAns('NEW MAJOR',""",
    """    <TcBlock page={2} title="Every key, up to seven" answers={<>{tcAns('TRY IT', K5_WB.sig.map(k4wSig))}{tcAns('PLAY', ['C♯ major: F♯ C♯ G♯ D♯ A♯ E♯ B♯', 'E♭ minor: B♭ E♭ A♭ D♭ G♭ C♭'], 7)}{tcAns('NEW MAJOR',""")
rep("""    <TcBlock page={3} title="The melodic minor" answers={<>{tcAns('MELODIC, UP · DOWN',""",
    """    <TcBlock page={3} title="The melodic minor" answers={<>{tcAns('TRY IT', K5_WB.mel.map(k => { const sig = k5Sig(K5M[k].ks); return K5M[k].en + ': ' + k5Let(k5MNote(k, 5, 'mel'), sig) + ' ' + k5Let(k5MNote(k, 6, 'mel'), sig); }))}{tcAns('PLAY', ['F♯', 'E'], 6)}{tcAns('MELODIC, UP · DOWN',""")
rep("""    <TcBlock page={4} title="Augmented and diminished" answers={<>{tcAns('THE PAIRS (treble; in the bass an octave lower)',""",
    """    <TcBlock page={4} title="Augmented and diminished" answers={<>{tcAns('TRY IT', K5_WB.iv.map(k5wIv))}{tcAns('PLAY', ['A4', 'd5'], 7)}{tcAns('THE PAIRS (treble; in the bass an octave lower)',""")
rep("""    <TcBlock page={5} title="Every interval upside down" answers={<>{tcAns('INVERSIONS',""",
    """    <TcBlock page={5} title="Every interval upside down" answers={<>{tcAns('TRY IT', K5_WB.inv.map(j => k5wIv(j) + ' → ' + k5Inv(k5wIv(j))))}{tcAns('PLAY', ['d7', 'A5', 'm3', 'P4'], 7)}{tcAns('INVERSIONS',""")
rep("""    <TcBlock page={6} title="Dominant, subdominant or relative?" answers={<>{tcAns('MELODIES',""",
    """    <TcBlock page={6} title="Dominant, subdominant or relative?" answers={<>{tcAns('TRY IT', K5_WB.mod.map(j => { const m = K5_MOD[j], c = k5ModNotes(j)[m.clue]; return k5wKey(m[m.to]) + ' ' + ({ dom: 'D', sub: 'S', rel: 'R' })[m.to] + ' (clue ' + h3Let(c) + (c.acc === 0 ? '♮' : '') + ')'; }))}{tcAns('PLAY', ['F♮', 'C♯'], 4)}{tcAns('MELODIES',""")
rep("""    <TcBlock page={7} title="The check-up" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one on paper or at the piano, treble and bass, with and without key signatures, in keys the child has not just practised. The drill's levels 1 to 5 match the steps.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', K5_WB.chk.sig.map(k4wSig))}{tcAns('B', K5_WB.chk.mel.map(k => { const sig = k5Sig(K5M[k].ks); return k5Let(k5MNote(k, 5, 'mel'), sig) + ' ' + k5Let(k5MNote(k, 6, 'mel'), sig); }), 5)}{tcAns('C', K5_WB.chk.iv.map(k5wIv), 9)}{tcAns('D', K5_WB.chk.inv.map(j => k5Inv(k5wIv(j))), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5. Modulation (p.6) is checked with a melody you choose.</div></>}/>""")

rep("""    <TcBlock page={2} title="vii°b and the first inversions" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{tcAns('C MAJOR, FIRST INVERSION: THE BASS',""",
    """    <TcBlock page={2} title="vii°b and the first inversions" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{tcAns('TRY IT', H5_WB.inv.map(([k, d]) => h5Rom(k, d, 1)))}{tcAns('PLAY', [h5Letters('G', 7), h5Letters('F', 7)], 7)}{tcAns('C MAJOR, FIRST INVERSION: THE BASS',""")
rep("""    <TcBlock page={3} title="The cadential 6-4" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{H5_PKEYS.map(k =>""",
    """    <TcBlock page={3} title="The cadential 6-4" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{tcAns('TRY IT', H5_WB.c64.map(([k, p]) => h5Rom(k, 1, p)))}{tcAns('PLAY', ['G', 'V'], 5)}{H5_PKEYS.map(k =>""")
rep("""    <TcBlock page={4} title="Passing and auxiliary notes" answers={<>{tcAns('THE MELODIES""",
    """    <TcBlock page={4} title="Passing and auxiliary notes" answers={<>{tcAns('TRY IT', H5_WB.pass.map(j => h4Name(H5_PASS[j].k) + ': ' + [1, 3, 5].map(x => H5_PASS_AB[h5PassKind(j, x)]).join(' ')))}{tcAns('PLAY', ['D', 'A'], 4)}{tcAns('THE MELODIES""")
rep("""    <TcBlock page={5} title="The chord before the cadence" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{['C', 'G', 'F', 'Am', 'Dm']""",
    """    <TcBlock page={5} title="The chord before the cadence" answers={<div style={{fontSize:11,color:BK.ink,lineHeight:1.55}}>{tcAns('TRY IT', H5_WB.pre.map(([k, o]) => h5PreRom(k, o)))}{tcAns('PLAY', ['IV', 'iib', 'Ic'], 5)}{['C', 'G', 'F', 'Am', 'Dm']""")
rep("""    <TcBlock page={6} title="Harmonise eight notes" answers={<>{tcAns('EVERY ROOT-POSITION CHORD THAT HOLDS EACH NOTE',""",
    """  </>);
  P(<>
    <TcBlock page={6} title="Harmonise eight notes" answers={<>{tcAns('TRY IT: ONE WAY (any chord that holds its note is right; the last two must make a cadence)', [h4Name(H5_MEL[1].k) + ': I IV I ii V vi V I (Ic–V–I also fits the last three notes, B A G: I IV I ii V Ic V I)'], null)}{tcAns('PLAY', ['ii, IV, vi', 'V'], 3)}{tcAns('EVERY ROOT-POSITION CHORD THAT HOLDS EACH NOTE',""")
rep("""    <TcBlock page={7} title="The check-up" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one on paper and at the piano, in keys the child has not just practised: one vii°b between I and Ib, one Ic–V–I, one cadence with a chord before it, and a short melody harmonised in four parts with a passing note.</div>}/>""",
    """    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', H5_WB.chk.inv.map(([k, d]) => h5Rom(k, d, 1)))}{tcAns('B', H5_WB.chk.c64.map(([k, p]) => h5Rom(k, 1, p)), 5)}{tcAns('C', H5_WB.chk.pass.map(([j, x]) => H5_PASS_AB[h5PassKind(j, x)]), 9)}{tcAns('D', H5_WB.chk.pre.map(([k, o]) => h5PreRom(k, o)), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5. Then, in a key not practised here: one vii°b between I and Ib, one Ic–V–I, and a short melody harmonised in four parts with a passing note.</div></>}/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
