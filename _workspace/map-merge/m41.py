p='drills.src.html'; s=open(p).read()
if 'function S1PaperCheck' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:100])
    s=s.replace(old,new)

# 1. scale-play's Workbook loses the two-octave page; scales-1 gets its own Workbook
rep("function SpWorkbook({ startNo = 1 }) {\n  const W = SP_WB, pages = [];\n  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId=\"scale-play\">{content}</WbPage>);",
    "function SpWorkbook({ startNo = 1, part }) {   // m40/m41: part '1', the Level 1 room's pages\n  const W = SP_WB, pages = [], CH = part === '1' ? 'scales-1' : 'scale-play';\n  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId={CH}>{content}</WbPage>);\n  const P1 = part === '1' ? P : () => {}, P0 = part === '1' ? () => {} : P;")
# the five scale-play pages: 1-4 only for scale-play; page 5 (two octaves) for scales-1 as its step 1
i0 = s.index("function SpWorkbook({ startNo = 1, part }) {")
iend = s.index("  // 7. the check-up on paper (faces My five checks)\n  P(<SpPaperCheck/>);\n  return <>{pages}</>;\n}", i0)
body = s[i0:iend]
i5 = body.index("  // 6 (faces \"Two octaves, hands together\")\n  P(<>\n    <WbTop step={5}/>")
before, after = body[:i5], body[i5:]
# pages 1-4 -> P0
hdr_end = before.index("const P1 = part === '1' ? P : () => {}, P0 = part === '1' ? () => {} : P;") + len("const P1 = part === '1' ? P : () => {}, P0 = part === '1' ? () => {} : P;")
before = before[:hdr_end] + before[hdr_end:].replace("\n  P(<>", "\n  P0(<>")
after = after.replace("  P(<>\n    <WbTop step={5}/>", "  P1(<>\n    <WbTop step={1}/>", 1)
s = s[:i0] + before + after + s[iend:]
rep("  // 7. the check-up on paper (faces My five checks)\n  P(<SpPaperCheck/>);\n  return <>{pages}</>;\n}",
    r'''  // m41: Level 1 -- mirror twins in G and E minor, chromatic from G, the check-up
  P1(<>
    <WbTop step={2}/>
    <Part kind="together" title="Mirror twins in G and E minor" how="Both hands start on the pale key and move apart, always with the same finger numbers. The right hand plays the red key. Which note does the left hand's same finger play?">
      <BkGrid cols={2} gap="8px 10px">{SP1_WB.mirror.map((it, i) => <SpwMirrorCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Mirror twins this week" how="Do each one at the piano and tick a box each day.">
      <PhLog rows={['G major from the G below middle C, two octaves, saying the numbers', 'E harmonic minor from the E below middle C: find both D♯s first', 'Both at 66, mf and even']} label={300}/>
    </Part>
    <Part kind="play" title="Mirror letters from E" how="The right hand goes up from E. Write the left hand's letters as it goes down from the same E: the twin of each note is under it.">
      <div style={{display:'grid',gap:6,padding:'8px 0'}}>{spwLetters('Emh', 40)}
        <div style={{display:'flex',gap:4,justifyContent:'center'}}>{spCm('Emh').nmL.map((x, j) => <span key={j} style={{width:40,height:40,border:'2px solid ' + (j === 0 ? BK.ink : BK.coral),borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>{j === 0 ? x : ''}</span>)}</div></div>
    </Part>
    <Faces/>
  </>);
  P1(<>
    <WbTop step={3}/>
    <Part kind="together" title="Chromatic from G" how="Write the finger under each letter: 3 on black keys, 1 on white keys, 2 where two white keys sit together. The first ones are done.">
      <div style={{display:'grid',gap:10}}>{['R', 'L'].map((h, i) => { const N = scfwChromNames(3), F = N.map((_, j) => scfChF(SCF_CHROM[3][1] + j, h, j === 0 || j === 12));
        return <ExCell key={h} n={i + 1} ex={i === 0}><div style={{padding:'16px 4px 4px'}}><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:4}}>From G, {spwHand(h).toLowerCase()}, going up</div>
          <div style={{display:'flex',gap:3,justifyContent:'center',flexWrap:'wrap'}}>{N.map((x, j) => <span key={j} style={{display:'inline-flex',flexDirection:'column',alignItems:'center',gap:3}}><span style={{fontFamily:LB_SERIF,fontWeight:800,fontSize:13,color:BK.ink}}>{x}</span>{nvBox(i === 0 && j < 4 || j === 0, String(F[j]), 30, 26)}</span>)}</div></div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Chromatic this week" how="Tick a box each day. Every key in order, black and white, one octave from G.">
      <PhLog rows={['Right hand, from G up to G and back, saying 3 on every black key', 'Left hand, the same', 'Even and legato: no bump at B C and E F']} label={300}/>
    </Part>
    <Faces/>
  </>);
  if (part === '1') { P(<S1PaperCheck/>); return <>{pages}</>; }
  // 7. the check-up on paper (faces My five checks)
  P(<SpPaperCheck/>);
  return <>{pages}</>;
}
const SP1_WB = { mirror: [['G', 3], ['G', 6], ['Emh', 4], ['Emh', 6]], chk: { thumbs: [['G', 'R', 4], ['F', 'R', 3], ['Em', 'L', 10]], mirror: [['G', 2], ['G', 5], ['Emh', 3], ['Emh', 6]], chrom: [['R', 3], ['L', 5], ['R', 8], ['L', 10]] } };   // m41
function S1PaperCheck() {   // m41: the Level 1 scales check-up on paper
  const C = SP1_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Two octaves: write the missing finger number.')}
    <BkGrid cols={1} gap="6px 8px">{C.thumbs.map(([k, h, j], i) => { const hide = spStripCols(k).N.map((_, x) => x === j); return <BkCell key={i} n={i + 1}><div style={{padding:'14px 2px 2px'}}><div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',marginBottom:2}}>{SP_SC[k].en}, {spwHand(h).toLowerCase()}, two octaves</div><SpStrip k={k} ask={j} hideR={h === 'R' ? hide : null} hideL={h === 'L' ? hide : null} mw={620}/></div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Mirror twins: which note does the left hand\'s same finger play?')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((it, i) => { const m = spwMirror(it); return <BkCell key={i} n={i + 4}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>{SP_CM[it[0]].en.split(',')[0]}, from the pale key: right hand {m.r}, finger {m.f}</div><SpKb lo={m.c.L[7]} hi={m.c.R[7]} W={10} H={26} lit={{ [m.c.R[0]]: 'pale', [m.R]: 'cor' }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(32, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('C', 'Chromatic from G: which finger plays the red key?')}
    <BkGrid cols={4} gap="6px 8px">{C.chrom.map(([h, j], i) => { const s0 = SCF_CHROM[3][1]; return <BkCell key={i} n={i + 8}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <div style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'center',lineHeight:1.2}}>From G, {spwHand(h).toLowerCase()}</div><SpKb lo={s0} hi={s0 + 12} W={10} H={28} lit={{ [s0 + j]: 'cor' }} k={1}/>
      <div style={{display:'flex',justifyContent:'center'}}>{bkBox(30, 24)}</div></div></BkCell>; })}</BkGrid>
  </div>;
}
function S1Teacher() {   // m41: the Level 1 scales teacher copy
  const W = SP1_WB, C = W.chk, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-1" teacher>{content}</WbPage>);
  const thumbs = (k) => spThumbs(k).map(j => spStripCols(k).N[j]).join(', ');
  const chromF = (h, j) => scfChF(SCF_CHROM[3][1] + j, h, j === 0 || j === 12);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-1')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Level 1 scales, as on the Grade 1 technical list: G and F major, E and D minor (natural and harmonic), two octaves, hands separately and together, two notes a beat at ♩ = 76; contrary motion over two octaves in C major, A harmonic minor, G major and E harmonic minor at ♩ = 66; the chromatic scale from G, one octave. Checked at the piano, from memory, mf and legato.</div>
    <TcBlock page={2} title="Two octaves, hands together" answers={<>{tcAns('TRY IT', SP_WB.thumbs.map(k => SP_SC[k].en + ': ' + thumbs(k)))}{tcAns('PLAY', ['E minor: ' + thumbs('Em'), 'D minor: ' + thumbs('Dm')], 3)}</>}
      watch="Hands together, the turns come at different moments: practise a few notes around each turn, hands together, very slowly." say="“The thumbs meet in the middle. Everywhere else they turn on their own.”"/>
    <TcBlock page={3} title="Mirror twins in G and E minor" answers={<>{tcAns('TRY IT', W.mirror.map(it => { const m = spwMirror(it); return 'right ' + m.r + ' (' + m.f + ') → left ' + m.l; }))}{tcAns('PLAY', [spCm('Emh').nmL.join(' ')])}</>}
      watch="E harmonic minor: the D♯ in both hands. The fingers match all the way, as in C major." say="“A new note, the same mirror.”"/>
    <TcBlock page={4} title="Chromatic from G" answers={<>{tcAns('TRY IT', ['R', 'L'].map(h => (h === 'R' ? 'right: ' : 'left: ') + scfwChromNames(3).map((_, j) => chromF(h, j)).join(' ')))}</>}
      watch="A loud thumb, a bump at B C and E F. Black keys always 3." say="“Black 3, white 1, two whites together: 2.”"/>
    <TcBlock page={5} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', C.thumbs.map(([k, h, j]) => String(spStripCols(k)[h][j])))}{tcAns('B', C.mirror.map(it => spwMirror(it).l), 4)}{tcAns('C', C.chrom.map(([h, j]) => String(chromF(h, j))), 8)}</>}/>
  </>);
  return <>{pages}</>;
}
''')
rep("WORKBOOKS['scale-play'] = SpWorkbook;", "WORKBOOKS['scale-play'] = SpWorkbook;\nWORKBOOKS['scales-1'] = (p) => <SpWorkbook part=\"1\" {...p}/>;   // m41\nTEACHER_COPIES['scales-1'] = S1Teacher;")

# 2. scale-play's teacher copy: the two-octave block leaves, the check-up is page 6
i = s.index("    <TcBlock page={6} title=\"Two octaves, hands together\"")
j = s.index("    <TcBlock page={7} title=\"The check-up on paper", i)
s = s[:i] + s[j:].replace("<TcBlock page={7} title=\"The check-up on paper", "<TcBlock page={6} title=\"The check-up on paper", 1)

# 3. checkpoints
rep("scales: [1, 2, 3, 5, 6, 63, 64, 9], 'scale-play': [1, 2, 3, 4, 5, 6],", "scales: [1, 2, 3, 5, 6, 63, 64, 9], 'scale-play': [1, 2, 3, 5, 6], 'scales-1': [4, 7, 8],")
rep("  'scale-play': { secs: ['A', 'C'], back: { A: [1, 2], C: [4, 5] }, Paper: () => <SpPaperCheck/> },",
    "  'scale-play': { secs: ['A', 'C'], back: { A: [1, 2], C: [4, 5] }, Paper: () => <SpPaperCheck/> },\n  'scales-1': { secs: ['A', 'C'], back: { A: [2, 2], C: [4, 4] }, Paper: () => <S1PaperCheck/> },   // m41")
rep("'2': [['listen-write', 'accidentals'], ['key-signatures', 'terms'], ['six-eight', 'intervals'], ['chords', 'form']],",
    "'2': [['listen-write', 'accidentals'], ['key-signatures', 'terms'], ['six-eight', 'intervals'], ['chords', 'form'], ['scales-1']],")
# 4. little registries
rep("'scale-play': '스케일 치기', ", "'scale-play': '스케일 치기', 'scales-1': '스케일, Level 1', ")
rep("'minor-scales': ['key-signatures', 'scale-play'],", "'minor-scales': ['key-signatures', 'scale-play'], 'scales-1': ['scale-play'],")
open(p,'w').write(s); print('ok')
