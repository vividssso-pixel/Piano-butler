import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AI-2: Minor Scales, the Workbook and teacher's copy. Pages 2 to 6 face the Lesson Book's steps; page 7, facing My
# five checks, is the check-up on paper. Answers come from the room's own data (msNames, MS_REL, MS_GAPS).
CODE = r'''
// ─── Chapter: Minor Scales, the Workbook and teacher's copy (Build AI-2) ───
const MS_WB = {
  third: [[0, 'maj'], [9, 'min'], [2, 'min'], [7, 'maj'], [4, 'min'], [5, 'maj']],   // root (semitones from middle C), major or minor third
  sig: ['G', 'Bb', 'C', 'F'],                                                         // a major key's signature: name both keys
  down: ['C', 'G', 'F', 'Bb'],                                                        // three half steps down from the major's first note
  raise: ['A', 'E', 'D', 'G'],                                                        // the raised 7th
  wrong: [['D', 5, 'B'], ['G', 6, 'F']],                                              // harmonic minor with one mistake: [minor, index, what is written]
  gaps: ['A', 'E', 'D', 'G'],
  count: [['F', 'G♯', 3], ['G♯', 'A', 1], ['B', 'C', 1], ['A', 'B', 2]],             // in A harmonic minor
  kind: [['C', 'maj'], ['E', 'min'], ['G', 'maj'], ['D', 'min']],
  code: ['T T S T T T S', 'T S T T S T½ S'],
  chk: { third: [[4, 'min'], [5, 'maj'], [9, 'min'], [7, 'maj']], sig: ['F', 'C', 'Bb', 'G'], raise: ['E', 'G', 'A', 'D'],
    gap: [['E', 1], ['D', 3], ['G', 5], ['A', 1]], kind: [['G', 'min'], ['F', 'maj'], ['A', 'min'], ['D', 'maj']] },
};
const msMinOf = (M) => Object.keys(MS_REL).find(m => MS_REL[m] === M);
const mswThirdName = (r) => ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'][spPc(r)];
const mswKindLetters = ([x, q]) => (q === 'maj' ? spellScale(x).map(prettyAny).concat([prettyNote(x)]) : msNames(x, 'harmonic'));
const mswGapAns = (n) => (n === 1 ? 'S' : n === 2 ? 'T' : 'T½');
const mswBoxes = (names, opts = {}) => <div style={{display:'flex',gap:opts.gap || 4,justifyContent:'center',flexWrap:'wrap'}}>{names.map((x, j) => <span key={j} style={{minWidth:opts.size || 34,height:opts.size || 34,padding:'0 3px',boxSizing:'border-box',border:'1.6px solid ' + (x === '?' ? BK.coral : BK.ink),borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:(opts.size || 34) * 0.48,fontWeight:800,color:x === '?' ? BK.coral : BK.ink,fontStyle:x === '?' ? 'italic' : 'normal'}}>{x === '?' ? (opts.ans || '') : x}</span>)}</div>;
// the letters with a box in every gap: write T, S or T½
function MswGapRow({ m, ex, size = 32, only }) {
  const N = msNames(m, 'harmonic');
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',flexWrap:'wrap',gap:3}}>{N.map((nm, j) => <React.Fragment key={j}>
    <span style={{minWidth:size,height:size,padding:'0 3px',boxSizing:'border-box',border:'1.6px solid ' + BK.ink,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:size * 0.48,fontWeight:800,color:BK.ink}}>{nm}</span>
    {j < N.length - 1 && (only == null || only === j ? <span style={{minWidth:size * 0.95,height:size * 0.8,border:'1.5px solid ' + BK.coral,borderRadius:4,display:'inline-flex',alignItems:'center',justifyContent:'center',color:BK.coral,fontWeight:900,fontStyle:'italic',fontSize:size * 0.4}}>{ex && j === 0 ? mswGapAns(MS_GAPS[j]) : ''}</span> : <span style={{width:size * 0.4}}/>)}
  </React.Fragment>)}</div>;
}
function MswThirdCell({ r, q, n, ex, W = 20, small }) {
  const K = msThirdKeys(r, q), top = r + (q === 'maj' ? 4 : 3);
  return <ExCell n={n} ex={ex}><div style={{display:'grid',gap:4,padding:'16px 2px 2px'}}>
    <SpKb lo={r - 1} hi={r + 7} W={W} H={small ? 34 : 54} lit={K.lit} names={{ [r]: mswThirdName(r), [top]: mswThirdName(top) }} k={1}/>
    <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:11,fontWeight:800,color:BK.ink,flexWrap:'wrap'}}>half steps {nvBox(ex, q === 'maj' ? '4' : '3', 30, 26)} major or minor {nvBox(ex, q === 'maj' ? 'major' : 'minor', 58, 26)}</div>
  </div></ExCell>;
}
const mswSig = (M, w = 150) => <div style={{maxWidth:w,margin:'0 auto'}}><SkgStaff items={[['sp', 6]]} k={M} width={w} full pad={[22, 16]} o={{ ...SKG_AL }}/></div>;
function MsWorkbook({ startNo = 1 }) {
  const W = MS_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="minor-scales">{content}</WbPage>);
  const line = (n, label, box) => <span style={{display:'inline-flex',alignItems:'center',gap:8}}>{nvNum(n)} {label} {box}</span>;

  // 2 (faces "Major or minor third?")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Major or minor third?" how="Count the half steps from the first coral key to the second. Four: a major third. Three: a minor third.">
      <BkGrid cols={3} gap="6px 10px">{W.third.map(([r, q], i) => <MswThirdCell key={i} r={r} q={q} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Thirds this week" how="Do each one at the piano and tick a box each day.">
      <PhLog rows={['C to E, then A to C: one after the other, then together', 'Sing do re mi, then la ti do: where is the third?', 'A minor third from D, E and A; a major third from C, F and G']} label={300}/>
    </Part>
    <Part kind="play" title="Brighter or darker?" how="Play each pair, one after the other and then together. Write B for the brighter third and D for the darker one.">
      <div style={{display:'flex',gap:22,justifyContent:'center',flexWrap:'wrap',fontSize:14,fontWeight:800,color:BK.ink,padding:'10px 0'}}>{[['C', 'E'], ['D', 'F'], ['F', 'A'], ['E', 'G']].map(([a, b], i) => line(7 + i, a + ' to ' + b, bkBox(40, 32)))}</div>
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The minor key's key signature")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Name both keys" how="Every key signature belongs to a major key and a minor key. Write both.">
      <BkGrid cols={4} gap="6px 10px">{W.sig.map((M, i) => <ExCell key={M} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'14px 2px 2px'}}>{mswSig(M, 120)}
        <div style={{display:'grid',gap:4,justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink}}><span style={{display:'inline-flex',alignItems:'center',gap:5}}>major {nvBox(i === 0, prettyNote(M), 44, 26)}</span><span style={{display:'inline-flex',alignItems:'center',gap:5}}>minor {nvBox(i === 0, msMinOf(M), 44, 26)}</span></div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Three half steps down" how="From the major key's first note, count three half steps down on the piano. Write the minor key's first note.">
      <div style={{display:'flex',gap:22,justifyContent:'center',flexWrap:'wrap',fontSize:14,fontWeight:800,color:BK.ink,padding:'6px 0'}}>{W.down.map((M, i) => line(5 + i, prettyNote(M) + ' major →', bkBox(40, 32)))}</div>
    </Part>
    <Part kind="play" title="Key signature twins" how="Draw a line from each major key to the minor key that shares its key signature.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'14px 120px',justifyContent:'center',padding:'14px 40px',fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>
        {[['C major', 'D minor'], ['G major', 'A minor'], ['F major', 'G minor'], ['B♭ major', 'E minor']].map(([a, b]) => <React.Fragment key={a}><span style={{display:'flex',alignItems:'center',justifyContent:'flex-end',gap:10}}>{a}<span style={{width:9,height:9,borderRadius:5,background:BK.ink}}/></span><span style={{display:'flex',alignItems:'center',gap:10}}><span style={{width:9,height:9,borderRadius:5,background:BK.ink}}/>{b}</span></React.Fragment>)}
      </div>
    </Part>
    <Faces/>
  </>);

  // 4 (faces "The harmonic minor")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Raise the 7th" how="Here is each natural minor. Write the harmonic minor's 7th in the coral box: the 7th goes up a half step.">
      <BkGrid cols={2} gap="6px 10px">{W.raise.map((m, i) => <ExCell key={m} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 2px 2px'}}>
        <div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{m} harmonic minor</div>
        {mswBoxes(msNames(m, 'natural').map((x, j) => (j === 6 ? '?' : x)), { size: 30, ans: i === 0 ? msNames(m, 'harmonic')[6] : '' })}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write it on the staff" how="Write A harmonic minor going up, one note on each line or space, from the A on the second space. Write the sharp beside the 7th.">
      <div style={{padding:'0 10px'}}><PaperStaff clef="treble" notes={[]} width={560}/></div>
    </Part>
    <Part kind="play" title="Spot the mistake" how="Each harmonic minor has one wrong note. Circle it, and write the right one underneath.">
      <div style={{display:'grid',gap:14,padding:'10px 0'}}>{W.wrong.map(([m, j, w], i) => <div key={m} style={{display:'grid',gap:4,justifyItems:'center'}}><span style={{fontSize:12,fontWeight:900,color:BK.muted}}>{nvNum(5 + i)} {m} harmonic minor</span>{mswBoxes(msNames(m, 'harmonic').map((x, k) => (k === j ? w : x)), { size: 38 })}</div>)}</div>
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Tone, semitone, tone and a half")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="T, S or T½?" how="Count the half steps between neighbours. One: a semitone (S). Two: a tone (T). Three: a tone and a half (T½). Write it in each coral box.">
      <div style={{display:'grid',gap:8}}>{W.gaps.map((m, i) => <ExCell key={m} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 4px'}}><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{m} harmonic minor</div><MswGapRow m={m} ex={i === 0} size={30}/></div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="Count on the keys" how="A harmonic minor. Count the half steps on the piano, then write the number.">
      <div style={{display:'flex',gap:20,justifyContent:'center',flexWrap:'wrap',fontSize:14,fontWeight:800,color:BK.ink,padding:'6px 0'}}>{W.count.map(([a, b], i) => line(5 + i, a + ' to ' + b, bkBox(40, 32)))}</div>
    </Part>
    <Part kind="play" title="The secret code" how="Every harmonic minor has the same code of seven steps. Write it from memory, then check it against the boxes above.">
      <div style={{display:'flex',gap:8,justifyContent:'center',padding:'12px 0'}}>{Array.from({ length: 7 }, (_, j) => <span key={j} style={{width:46,height:46,border:'2px solid ' + BK.coral,borderRadius:8}}/>)}</div>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Major or harmonic minor?")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Major or harmonic minor?" how="Two clues: the 3rd note (a major or a minor third from the bottom) and the wide step just under the top. Write M for major, H for harmonic minor.">
      <BkGrid cols={2} gap="6px 10px">{W.kind.map((x, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:6,padding:'16px 2px 4px'}}>{mswBoxes(mswKindLetters(x), { size: 30 })}
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>M or H {nvBox(i === 0, x[1] === 'maj' ? 'M' : 'H', 40, 28)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Listen this week" how="Ask someone to play you a scale, up and down. Is it major or harmonic minor? Tick a box when you get it right.">
      <PhLog rows={['C major, then A harmonic minor', 'G major, then E harmonic minor', 'F major, then D harmonic minor', 'Mixed: someone picks, you say']} label={300}/>
    </Part>
    <Part kind="play" title="Code breaker" how="Each code is a scale's seven steps. Which one is major, and which is harmonic minor?">
      <div style={{display:'grid',gap:12,justifyItems:'center',padding:'12px 0'}}>{W.code.map((c, i) => <span key={c} style={{display:'inline-flex',alignItems:'center',gap:12,fontSize:15,fontWeight:900,color:BK.ink}}>{nvNum(5 + i)}<span style={{letterSpacing:'0.12em'}}>{c}</span>{bkBox(110, 32)}</span>)}</div>
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (faces My five checks)
  P(<MsPaperCheck/>);
  return <>{pages}</>;
}
function MsPaperCheck() {
  const C = MS_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Major or minor third? Count the half steps.')}
    <BkGrid cols={4} gap="6px 8px">{C.third.map(([r, q], i) => { const K = msThirdKeys(r, q), top = r + (q === 'maj' ? 4 : 3); return <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>
      <SpKb lo={r - 1} hi={r + 7} W={15} H={40} lit={K.lit} names={{ [r]: mswThirdName(r), [top]: mswThirdName(top) }} k={1}/><div style={{display:'flex',justifyContent:'center'}}>{bkBox(58, 24)}</div></div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Which minor key has this key signature?')}
    <BkGrid cols={4} gap="6px 8px">{C.sig.map((M, i) => <BkCell key={M} n={i + 5}><div style={{display:'grid',gap:3,padding:'14px 0 0'}}>{mswSig(M, 110)}<div style={{display:'flex',justifyContent:'center',alignItems:'center',gap:5,fontSize:10.5,fontWeight:900,color:BK.muted}}>{bkBox(40, 24)} minor</div></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Write the harmonic minor\'s 7th.')}
    <BkGrid cols={2} gap="6px 8px">{C.raise.map((m, i) => <BkCell key={m} n={i + 9}><div style={{padding:'14px 2px 2px'}}>{mswBoxes(msNames(m, 'natural').map((x, j) => (j === 6 ? '?' : x)), { size: 24, gap: 3 })}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'T, S or T½? Write the step in the coral box.')}
    <BkGrid cols={2} gap="6px 8px">{C.gap.map(([m, j], i) => <BkCell key={i} n={i + 13}><div style={{padding:'14px 2px 2px'}}><MswGapRow m={m} only={j} size={22}/></div></BkCell>)}</BkGrid>
    {bkSec('E', 'Major (M) or harmonic minor (H)?')}
    <BkGrid cols={2} gap="6px 8px">{C.kind.map((x, i) => <BkCell key={i} n={i + 17}><div style={{display:'flex',alignItems:'center',gap:6,padding:'14px 2px 2px'}}><div style={{flex:1}}>{mswBoxes(mswKindLetters(x), { size: 22, gap: 3 })}</div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
function MsTeacher() {
  const W = MS_WB, C = W.chk, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="minor-scales" teacher>{content}</WbPage>);
  const third = ([r, q]) => mswThirdName(r) + '–' + mswThirdName(r + (q === 'maj' ? 4 : 3)) + ': ' + (q === 'maj' ? '4, major' : '3, minor');
  const gapRow = (m) => MS_GAPS.map(mswGapAns).join(' ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('minor-scales')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. Grade 1 theory needs four minor keys: A, E, D and G, with their key signatures, the harmonic minor written up or down on either staff, and the tones, semitones and the tone and a half marked. The two checks by ear (a major or a minor third; a major or a harmonic minor scale) are done at the piano.</div>
    <TcBlock page={2} title="Major or minor third?" answers={<>{tcAns('TRY IT', W.third.map(third))}{tcAns('PLAY', ['C–E: B', 'D–F: D', 'F–A: B', 'E–G: D'], 7)}</>}
      watch="Counting the keys instead of the half steps between them (C to E is four half steps, five keys). Count the moves, not the keys."
      say="“Start on the first key and count each step to the next key, black or white: one, two, three…”"/>
    <TcBlock page={3} title="The minor key's key signature" answers={<>{tcAns('TRY IT', W.sig.map(M => prettyNote(M) + ' major, ' + msMinOf(M) + ' minor'))}{tcAns('YOUR TURN', W.down.map(M => prettyNote(M) + ' → ' + msMinOf(M)), 5)}{tcAns('PLAY', ['C–A, G–E, F–D, B♭–G'])}</>}
      watch="Counting up instead of down (C up three half steps is E♭), or naming the minor on the same note (C major, C minor): that key has a different key signature. A key signature alone does not say major or minor: the piece's first and last notes do."
      say="“Same key signature: the minor is three half steps down.”"/>
    <TcBlock page={4} title="The harmonic minor" answers={<>{tcAns('TRY IT', W.raise.map(m => m + ' minor: ' + msNames(m, 'harmonic')[6]))}{tcAns('YOUR TURN', ['A B C D E F G♯ A, from the second space up to the A above the staff, the sharp in front of G'])}{tcAns('PLAY', W.wrong.map(([m, j, w]) => m + ' minor: ' + w + ' should be ' + msNames(m, 'harmonic')[j]), 5)}</>}
      watch="Writing the raised 7th in the key signature, or putting the sharp after the note. In G minor the F♯ comes with two flats in the key signature; in D minor the C♯ with one flat."
      say="“Harmonic minor: raise the 7th, beside the note.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Tone, semitone, tone and a half" answers={<>{tcAns('TRY IT', W.gaps.map(m => m + ': ' + gapRow(m)))}{tcAns('YOUR TURN', W.count.map(([a, b, n]) => a + '–' + b + ': ' + n), 5)}{tcAns('PLAY', ['T S T T S T½ S'])}</>}
      watch="Calling the tone and a half a tone, because the two letters are next to each other (F to G♯). Count the half steps, not the letters."
      say="“Harmonic minor: T S T T S T½ S. The wide step is between the 6th and the raised 7th.”"/>
    <TcBlock page={6} title="Major or harmonic minor?" answers={<>{tcAns('TRY IT', W.kind.map(([x, q]) => (q === 'maj' ? 'M' : 'H') + ' (' + (q === 'maj' ? prettyNote(x) + ' major' : x + ' harmonic minor') + ')'))}{tcAns('PLAY', ['major', 'harmonic minor'], 5)}</>}
      watch="By ear: playing the scale fast. Play it at a walking pace, up and down; the darker third comes at once, the wide step near the top."
      say="“A darker third and a wide step near the top: harmonic minor.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', C.third.map(([, q]) => (q === 'maj' ? 'major' : 'minor')))}{tcAns('B', C.sig.map(M => msMinOf(M) + ' minor'), 5)}{tcAns('C', C.raise.map(m => msNames(m, 'harmonic')[6]), 9)}{tcAns('D', C.gap.map(([m, j]) => mswGapAns(MS_GAPS[j])), 13)}{tcAns('E', C.kind.map(([, q]) => (q === 'maj' ? 'M' : 'H')), 17)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5 · E p.6. The two checks by ear stay at the piano.</div></>}/>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['minor-scales'] = MsWorkbook;
TEACHER_COPIES['minor-scales'] = MsTeacher;
'''
rep("""function MinorScalesLessonBook() { return <>{msLbPages(false)}</>; }""",
    """function MinorScalesLessonBook() { return <>{msLbPages(false)}</>; }""" + CODE)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
