// ─── Phase 474: chapter 19's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: the key signature; G major; F major;
// key signature and accidental; D major and B♭ major; page 7 the check-up on paper) and its Teacher copy. English, like every
// Workbook. Every task set (rule 3) and done alone (rule 4); no tune copied from the facing book page; nothing on a page
// gives away another task on it; the check-up repeats no practice item; answers vary (rule 7).
const skgQ = (spec) => spec.map(x => x === '|' ? ['|'] : x === '||' ? ['||'] : typeof x === 'number' ? ['q', 1, x] : x.length === 2 && typeof x[1] === 'string' ? ['q', 1, x[0], x[1]] : x);
const skgT = (spec, top = 4) => [['ts', top], ...skgQ(spec)];
// a staff to write on, one size for a set (chapter 17's sacPaper, with a key)
const skgPaper = (items, k, o = {}, ref = 460, box, clef = 'treble') => <div style={{width:'100%'}}>{box ? sacInSet(box, ref, <SkgStaff items={items} k={k} clef={clef} width={box} left o={{ boxS: 28, ...o }}/>) : <SkgStaff items={items} k={k} clef={clef} width={ref} o={{ boxS: 28, ...o }}/>}</div>;
const skgChanged = (items, k) => skgOf(items, k, n => n.byKey);
const skgTicks = (ws) => <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{ws.map(w => sprTickW(w))}</div>;
// a key signature to draw on (room for two signs, none drawn), or the done one in coral: one size everywhere (about
// 5 mm between the lines), both clefs from one origin with one pad
const SKG_DRAW = [['sp', 34]];
const skgDrawCell = (k, clef, ex, pd = '8px 8px 4px') => <div style={{padding:pd}}><div style={{maxWidth:skgAloneW(SKG_DRAW),width:'100%',margin:'0 auto'}}><SkgStaff items={SKG_DRAW} k={k} clef={clef} width={200} full pad={[26, 20]} o={ex ? { ...SKG_AL, ksCol: PEN_C } : { ...SKG_AL, ks: [] }}/></div></div>;
// a key signature to read (to name it, or to write its signs): one size for both clefs
const skgReadKs = (k, clef, w = 140) => <div style={{maxWidth:w,width:'100%',margin:'0 auto'}}><SkgStaff items={SKG_ALONE} k={k} clef={clef} width={w} full pad={[30, 20]} o={{ ...SKG_AL }}/></div>;
// a note's key on a keyboard (C to B) with the key signature before it (one size for both clefs)
const skgKeyCell = (d, k, clef, ex) => { const items = [['w', 4, d], ['sp', 8]], n = skgRead(items, k)[0], m = sacMidi(n), pc = (((m - 60) % 12) + 12) % 12, vb = skgVbw(items, k, { base: 54 }, clef);
  return <div style={{display:'grid',gridTemplateColumns:'205px 240px',justifyContent:'center',alignItems:'center',gap:40,padding:'6px 10px 2px'}}><div style={{width:'100%'}}><SkgStaff items={items} k={k} clef={clef} width={vb} full pad={[22, 16]} o={{ D: 16, base: 54 }}/></div>
    <TnPKeys start="C" whites={7} w={30} h={84} slots wslots dots={ex ? [TN_KEY[pc]] : []}/></div>; };

const SKG_WB = {
  circ2: [['G', skgT([32, 31, 33, 34, '|', 38, 37, ['h', 2, 36], '||'])],          // G F♯ A B | F♯ E D: 2, 5 (done)
          ['G', skgT([34, 38, 36, 31, '|', 33, 38, ['h', 2, 39], '||'])]],         // B F♯ D F♯ | A F♯ G: 2, 4, 6
  names2: [['G', skgT([31, 33, 38, 36, '|', 37, 31, ['h', 2, 32], '||'])],         // F♯ A F♯ D | E F♯ G
           ['G', skgT([35, 38, 33, 31, '|', 32, 38, ['h', 2, 36], '||'])]],        // C F♯ A F♯ | G F♯ D
  play2: skgT([36, 38, 37, 38, '|', 36, 31, ['h', 2, 32], '||']),                   // G major: D F♯ E F♯ | D F♯ G
  draw3: [['treble', true], ['bass'], ['bass'], ['treble']],
  bass3: skgT([22, 24, 23, 21, '|', 20, 17, ['h', 2, 18], '||']),                   // on the bass staff: D F♯ E C | B F♯ G
  play3: skgT([32, 34, 36, 34, '|', 33, 31, ['h', 2, 32], '||']),                   // G B D B | A F♯ G
  draw4: [['treble', true], ['bass']],
  keys4: [[34, 'treble'], [20, 'bass'], [33, 'treble']],                            // B♭ (done), B♭, A
  play4: skgT([31, 33, 35, 34, '|', 33, 32, ['h', 2, 31], '||']),                   // F A C B♭ | A G F
  name5: [['G', skgQ([[31, 'n'], 32, 31, '||']), 2],                                // F (the natural holds: done)
          ['F', skgQ([[34, 'n'], 33, '|', 34, '||']), 2],                           // B♭ (a new bar)
          ['G', skgQ([38, 36, [38, 'n'], '||']), 0],                                // F♯ (before the natural)
          ['F', skgQ([32, [34, 'n'], 34, '||']), 2]],                               // B (the natural holds)
  names5: [['F', skgT([[34, 'n'], 35, 34, 33, '|', 34, 32, ['h', 2, 31], '||'])],  // B C B A | B♭ G F
           ['G', skgT([36, [38, 'n'], 37, 38, '|', 37, 38, ['h', 2, 39], '||'])]], // D F E F | E F♯ G
  play5: skgT([32, 33, [31, 'n'], 31, '|', 31, 33, ['h', 2, 32], '||']),            // G A F F | F♯ A G
  name6: [['D', 'treble'], ['Bb', 'bass'], ['G', 'treble'], ['F', 'bass'], ['C', 'treble'], ['D', 'bass']],   // the first done
  draw6: [['D', 'treble'], ['Bb', 'bass']],
  play6: [29, 30, 31, 32, 33, 34, 35, 36].map(d => ['q', 1, d]).concat([['||']]),   // D major
};
const SKG_WORDS = ['C', 'G', 'D', 'F', 'B♭'];
// the five key names to circle (chapter 13's row, the signs in the music font)
const skgCircle = (on, gx) => <div style={{display:'flex',justifyContent:'center',flexWrap:'wrap',gap:'4px ' + gx + 'px',fontSize:13,fontWeight:800,color:BK.ink,marginTop:'auto',paddingTop:4}}>{SKG_WORDS.map(w => <span key={w} style={{border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:14,padding:'0 7px',color:on === w ? BK.coral : BK.ink,whiteSpace:'nowrap'}}>{sscSx(w)}</span>)}</div>;
// the Teacher copy's answers (tcAns, with each number kept with its answer)
const skgTcAns = (label, list, n0 = 1) => <div style={{fontSize:12,color:BK.ink,lineHeight:1.65,marginBottom:2}}><b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>{label}</b>{'  '}{list.map((a, i) => <React.Fragment key={i}><span style={{marginRight:10,whiteSpace:String(a).length > 14 ? 'normal' : 'nowrap'}}>{n0 != null && <span style={{color:BK.muted}}>{i + n0}.</span>}{'\u00a0'}<b style={{color:BK.green}}>{a}</b></span>{' '}</React.Fragment>)}</div>;
const SKG_CHK = {
  name: [['G', 'bass'], ['F', 'treble'], ['Bb', 'treble']],
  which: [['D', 'bass'], ['F', 'bass']],
  note: [['F', skgQ([33, 34, 32, '||']), 1], ['F', skgQ([32, 31, 30, '||']), 1],                                                   // B♭, F
         ['D', skgQ([[35, 'n'], 36, 35, '||']), 2], ['Bb', skgQ([37, [37, 'n'], '|', 36, 37, '||']), 3]],                               // C, E♭
  draw: [['Bb', 'treble'], ['D', 'bass']],
};

function SkgWorkbook({ startNo = 1 }) {
  const W = SKG_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="key-signatures">{content}</WbPage>);
  const rows = (list, oOf, n0, ref = 460) => { const box = Math.min(ref, Math.max(...list.map(([k, it], i) => skgVbw(it, k, oOf(it, i, k))))); return <div style={{display:'grid',gap:8}}>{list.map(([k, it], i) => sskRowN(n0 + i, skgPaper(it, k, oOf(it, i, k), ref, box)))}</div>; };
  const playRow = (n, items, k, ticks, ref = 520, o = {}) => sskRowN(n, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{skgPaper(items, k, o, ref)}{skgTicks(ticks)}</div>);
  const draws = (list, k, n0) => <BkGrid cols={2} gap="6px 14px">{list.map(([clef, ex], i) => <ExCell key={i} n={n0 + i} ex={!!ex}>{skgDrawCell(k, clef, ex)}</ExCell>)}</BkGrid>;
  const names = (it, i, k) => ({ under: skgRead(it, k).map(() => null) });

  // 2 (faces "The key signature")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Circle the changed notes" how="Circle every note the key signature changes. The first line is done.">
      {rows(W.circ2, (it, i, k) => ({ ring: i === 0 ? skgChanged(it, k) : [] }), 1)}
    </Part>
    <Part kind="home" title="Write the names" how="Write each note’s name in its box: its letter, and ♯ when the key signature changes it.">
      {rows(W.names2, names, 3)}
    </Part>
    <Part kind="play" title="Play it" how="Play this with the right hand, saying the names. Tick each time.">
      {playRow(5, W.play2, 'G', ['saying the names', 'just playing'], 470)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "G major")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Draw the key signature" how="Draw G major’s sharp after each clef, on the F line. The first one is done.">
      {draws(W.draw3, 'G', 1)}
    </Part>
    <Part kind="home" title="On the bass staff" how="Write each note’s name in its box.">
      {sskRowN(5, skgPaper(W.bass3, 'G', { D: 33, boxS: 26, under: skgRead(W.bass3, 'G').map(() => null) }, 400, null, 'bass'))}
    </Part>
    <Part kind="play" title="Play it" how="Play this with the right hand, saying the names. Tick each time.">
      {playRow(6, W.play3, 'G', ['saying the names', 'just playing'], 470)}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "F major")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Draw the key signature" how="Draw F major’s flat after each clef, on the B line. The first one is done.">
      {draws(W.draw4, 'F', 1)}
    </Part>
    <Part kind="home" title="Find the key" how="Put a dot on the key of each note in F major. The first one is done.">
      <BkGrid cols={1} gap="4px">{W.keys4.map(([d, clef], i) => <ExCell key={i} n={i + 3} ex={i === 0}>{skgKeyCell(d, 'F', clef, i === 0)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play it" how="Play this with the right hand, saying the names. Tick each time.">
      {playRow(6, W.play4, 'F', ['saying the names', 'just playing'], 470)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Key signature and accidental")
  const box5 = Math.max(...W.name5.map(([k, it]) => skgVbw(it, k)));
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Name the coral note" how="Write the name of the coral note in its box. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.name5.map(([k, items, at], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(skgPaper(items, k, { hl: [at], boxS: 37, under: skgRead(items, k).map((n, j) => j === at ? (i === 0 ? sacNameTxt(n) : null) : undefined), underCoral: i === 0 ? [at] : [], underBoxed: true }, 300, box5), '4px 6px 2px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Write the names" how="Write each note’s name in its box.">
      {rows(W.names5, (it, i, k) => ({ D: 38, boxS: 31, ...names(it, i, k) }), 5, 560)}
    </Part>
    <Part kind="play" title="Play it" how="Play this, saying the names. Tick each time.">
      {playRow(7, W.play5, 'G', ['saying the names', 'just playing'], 470)}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "D major and B♭ major")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Name the key" how="Circle the major key of each key signature. The first one is done.">
      <BkGrid cols={3} gap="8px 10px">{W.name6.map(([k, clef], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(<>{skgReadKs(k, clef, 165)}{skgCircle(i === 0 ? prettyNote(k) : null, 9)}</>, '10px 4px 8px')}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the key signature" how="Draw each key signature after the clef: its signs in order, each on its line or space.">
      <BkGrid cols={2} gap="8px 14px">{W.draw6.map(([k, clef], i) => <BkCell key={i} n={i + 7}><div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,marginTop:8}}>{sscSx(prettyNote(k) + ' major')}</div>{skgDrawCell(k, clef, false, '2px 8px 6px')}</BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play D major" how="Right hand, with C major’s fingers. Tick each time.">
      {playRow(9, W.play6, 'D', ['up', 'down', 'up and down twice'], 470, { D: 30 })}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<SkgPaperCheck/>);
  return <>{pages}</>;
}
const skgChkNo = () => { const C = SKG_CHK, nB = C.name.length + 1, nC = nB + C.which.length, nD = nC + C.note.length; return { nB, nC, nD }; };
function SkgPaperCheck() {
  const C = SKG_CHK, { nB, nC, nD } = skgChkNo();
  // a set at one size (box: the widest of the set), the coral note's box about 10 mm
  const coral = (items, k, at, ref, box, boxS) => skgPaper(items, k, { hl: [at], under: skgRead(items, k).map((_, j) => j === at ? null : undefined), boxS }, ref, box);
  const boxC = Math.max(...C.note.map(([k, it]) => skgVbw(it, k)));
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Circle the major key of each key signature.')}
    <BkGrid cols={3} gap="6px 8px">{C.name.map(([k, clef], i) => <BkCell key={i} n={i + 1}>{sdyCol(<>{skgReadKs(k, clef, 165)}{skgCircle(null, 8)}</>, '6px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Write the sharps or flats of each key signature, in order.')}
    <BkGrid cols={2} gap="6px 10px">{C.which.map(([k, clef], i) => <BkCell key={i} n={nB + i}><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',alignItems:'center',gap:10,padding:'4px 10px 2px'}}>{skgReadKs(k, clef, 150)}<div style={{display:'flex',gap:8,justifyContent:'center'}}>{[0, 1].map(j => <span key={j}>{bkBox(46, 38)}</span>)}</div></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Write the name of the coral note.')}
    <BkGrid cols={2} gap="6px 10px">{C.note.map(([k, items, at], i) => <BkCell key={i} n={nC + i}><div style={{padding:'4px 6px 2px'}}>{coral(items, k, at, Math.round(boxC * 1.05), boxC, 34)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Draw each key signature after the clef, its signs in order.')}
    <BkGrid cols={2} gap="6px 10px">{C.draw.map(([k, clef], i) => <BkCell key={i} n={nD + i}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginTop:6}}>{sscSx(prettyNote(k) + ' major')}</div>{skgDrawCell(k, clef, false, '0 8px 4px')}</BkCell>)}</BkGrid>
  </div>;
}

function SkgTeacher() {
  const W = SKG_WB, C = SKG_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="key-signatures" teacher>{content}</WbPage>);
  const nb = (x) => String(x).replace(/ /g, ' ');   // an answer never breaks inside
  const names = (items, k) => { const r = skgNames(items, k), bars = []; let n = 0; items.forEach(it => { if (it[0] === '|' || it[0] === '||') bars.push(n); else if (sacIsNote(it)) n++; });
    return r.map((x, j) => x + (bars.includes(j + 1) && j + 1 < r.length ? ' |' : '')).join(' '); };
  const changed = (items, k) => { const r = skgRead(items, k); return skgChanged(items, k).map(j => 'note ' + (j + 1) + ' (' + sacNameTxt(r[j]) + ')').join(', '); };
  const where = (d, clef) => skgWhere(d, clef, true);
  const sig = (k, clef) => skgKs(k, clef).map(([s, d]) => nb(dName(d) + (s === '#' ? '♯' : '♭') + ' on ' + where(d, clef))).join(nb(', then '));
  const marks = { A: C.name.length, B: C.which.length, C: C.note.length, D: C.draw.length };
  const total = Object.values(marks).reduce((a, b) => a + b, 0), N = skgChkNo();
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('key-signatures')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{sscSx('Key signatures (chapter ' + bkChapterNo('scales') + ': the major scale, G major’s F♯ and F major’s B♭; chapter ' + bkChapterNo('accidentals') + ': accidentals last until the bar line). AMEB Music Craft: Preliminary, C, G and F major (treble staff only); Grade 1 adds D and B♭ major, the bass staff and the natural. ABRSM Theory: Grade 1, C, G, D and F major; Grade 2 adds B♭, A and E♭ major. A key signature lasts to the end of the piece (a key change comes later). Not here: minor keys and the relative minor, all seven sharps and flats, the circle of fifths (all in the toolbox); A and E♭ major are drill level 9 (extra).')}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12.5,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>Where the signs sit.</b> {sscSx(['treble', 'bass'].map(clef => (clef === 'treble' ? 'Treble staff: ' : 'Bass staff: ') + [['#', 'F'], ['#', 'C'], ['b', 'B'], ['b', 'E']].map(([g, l]) => l + (g === '#' ? '♯ ' : '♭ ') + where(skgSignD(g, l, clef), clef).replace(/^the /, '')).join('; ') + '.').join(' '))}</div>
    <TcBlock page={2} title="The key signature" answers={<>{sscLesson('The child points to the key signature on each line of a piece, names the line or space of each sign, and says which letter it changes.')}{skgTcAns('TRY IT', W.circ2.map(([k, it], i) => changed(it, k) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.names2.map(([k, it]) => names(it, k)), 3)}{skgTcAns('PLAY', [names(W.play2, 'G')], 5)}</>}
      watch="Only the F on the top line made sharp; the F in the bottom space forgotten. A sharp read as belonging to the first note after it. The key signature mistaken for a time signature."
      say="“Every F, every octave, the whole piece.”"/>
    <TcBlock page={3} title="G major" answers={<>{sscLesson('Play G major with and without F♯; the child says which one is G major.')}{skgTcAns('TRY IT', W.draw3.map(([clef], i) => nb('F♯ on ' + where(skgSignD('#', 'F', clef), clef)) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', [names(W.bass3, 'G')], 5)}{skgTcAns('PLAY', [names(W.play3, 'G')], 6)}</>}
      watch="The sharp drawn on the bottom space of the treble staff (also F, but not where a key signature puts it) or on the fifth line of the bass staff. On the bass staff, the notes read as if treble; the low F in the space under the staff left plain."
      say="“G major: one sharp, F♯, on the F line.”"/>
    <TcBlock page={4} title="F major" answers={<>{sscLesson('The child points to the flat after each clef and names its line: the middle line (treble), the second line (bass).')}{skgTcAns('TRY IT', W.draw4.map(([clef], i) => nb('B♭ on ' + where(skgSignD('b', 'B', clef), clef)) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.keys4.map(([d, clef], i) => sacNameTxt(skgRead([['w', 4, d]], 'F')[0]) + (i === 0 ? ' (done)' : '')), 3)}{skgTcAns('PLAY', [names(W.play4, 'F')], 6)}</>}
      watch="The flat drawn in the third space (C). On the bass staff, B played without its flat. A♯ named for B♭: in F major it is always B♭."
      say="“F major: one flat, B♭, on the B line.”"/>
  </>);
  P(<>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 10px',lineHeight:1.55,border:'0.8px solid ' + BK.hair,padding:'7px 12px'}}><b style={{color:BK.coral}}>Lesson time: the key-signature hunt.</b> {sscSx('Open a piece the child is learning in C, G, F, D or B♭ major. They find the key signature at the start of every line, name the key, play its scale, then point to every note the key signature changes on the first line. (A minor-key piece shares its key signature with a major key: not yet.)')}</div>
    <TcBlock page={5} title="Key signature and accidental" answers={<>{sscLesson('Play two bars of G major with F♮ in the first; the child says where F♯ comes back: after the bar line.')}{skgTcAns('TRY IT', W.name5.map(([k, items, at], i) => sacNameTxt(skgRead(items, k)[at]) + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.names5.map(([k, it]) => names(it, k)), 5)}{skgTcAns('PLAY', [names(W.play5, 'G')], 7)}</>}
      watch="The natural carried over the bar line. The note before the natural played plain too. A natural thought to last the whole piece, like the key signature."
      say="“Key signature: the whole piece. Accidental: until the bar line.”"/>
    <TcBlock page={6} title="D major and B♭ major" answers={<>{sscLesson('The child counts the signs and names the key, then plays D major with the right hand.')}{skgTcAns('TRY IT', W.name6.map(([k, clef], i) => prettyNote(k) + ' major' + (i === 0 ? ' (done)' : '')))}{skgTcAns('YOUR TURN', W.draw6.map(([k, clef]) => sig(k, clef)), 7)}{skgTcAns('PLAY', ['D major, fingers 1 2 3 1 2 3 4 5 up, 5 4 3 2 1 3 2 1 down'], 9)}</>}
      watch="C♯ written before F♯, or E♭ before B♭. B♭ major named 'E♭ major' (the last flat) or 'B major'. Two sharps called G major. An empty key signature not read as C major."
      say="“Count the signs: none C; one sharp G, two D; one flat F, two B♭.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {skgTcAns('A', C.name.map(([k]) => prettyNote(k) + ' major'))}
      {skgTcAns('B', C.which.map(([k]) => skgSignNames(k).join(' ')), N.nB)}
      {skgTcAns('C', C.note.map(([k, items, at]) => sacNameTxt(skgRead(items, k)[at])), N.nC)}
      {skgTcAns('D', C.draw.map(([k, clef]) => sig(k, clef)), N.nD)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}; {total} in all. B and D: every sign, in order, for the mark. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '2, 3 and 5', page: '3, 4 and 6' }, { id: 'b', step: '1, 3 and 5', page: '2, 4 and 6' }, { id: 'c', step: '1 to 5', page: '2 to 6' }, { id: 'd', step: '2, 3 and 5', page: '3, 4 and 6' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'6px 12px',margin:'0 0 8px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>The drill (after page 6).</b> {sscSx('1 C, G or F major · 2 the notes it changes · 3 the coral note in G and F · 4 with accidentals · 5 all five keys · 6 written right · 7 listening (screen only) · 8 the bass staff · 9 extra: A and E♭ major.')}</div>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: point to the key signature and say which notes it changes. 2. Page 3: play G major from the page, every F as F♯. 3. Page 4: play F major from the page, every B as B♭. 4. Page 5: say how long the key signature lasts and how long the natural lasts, then play the two bars. 5. Page 6: cover the names and name each key. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
WORKBOOKS['key-signatures'] = SkgWorkbook;
TEACHER_COPIES['key-signatures'] = SkgTeacher;
