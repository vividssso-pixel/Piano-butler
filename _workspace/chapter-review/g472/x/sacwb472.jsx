// ─── Phase 472: chapter 17's Workbook (pages 2 to 6 face Lesson Book pages 2 to 6: sharp and flat; the natural; until the
// bar line; its own line or space; reading a tune; page 7 the check-up on paper) and its Teacher copy. English, like every
// Workbook. Every task set (rule 3) and done alone (rule 4); no note, bar or tune copied from the facing book page;
// nothing on a page gives away another task on it; the check-up repeats no practice item; answers vary (rule 7).
const sacQ = (spec) => spec.map(x => x === '|' ? ['|'] : x === '||' ? ['||'] : typeof x === 'number' ? ['q', 1, x] : x.length === 2 && typeof x[1] === 'string' ? ['q', 1, x[0], x[1]] : x);
const sacT = (spec, top = 4) => [['ts', top], ...sacQ(spec)];
// a staff to write on, one size for a set (ref: the reference width; the staff is drawn at its width / ref of the space)
const sacPaper = (items, o = {}, ref = 460, box) => <div style={{width:'100%'}}>{box ? sacInSet(box, ref, <SacStaff items={items} width={box} left o={{ boxS: 28, ...o }}/>) : <SacStaff items={items} width={ref} o={{ boxS: 28, ...o }}/>}</div>;
// a note's key on a keyboard (C to B): the staff the same height in every cell, every key with a ring for the dot
const sacKeyCell = (d, s, ex) => { const m = ivMidi({ d, acc: SAC_ACC[s] }); return <div style={{display:'grid',gridTemplateColumns:'1fr 1.5fr',alignItems:'center',gap:12,padding:'20px 10px 12px'}}><SacStaff items={[['w', 4, d, s], ['||']]} width={120} full pad={[22, 30]} o={{ D: 16 }}/>
  <TnPKeys start="C" whites={7} w={28} h={100} slots wslots dots={ex ? [TN_KEY[m - 60]] : []}/></div>; };
const sacNamesOf = (items) => sacRead(items).map(sacNameTxt);
const sacChanged = (items) => sacRead(items).map((n, j) => n.carried ? j : -1).filter(j => j >= 0);
const sacTicks = (ws) => <div style={{display:'flex',justifyContent:'center',gap:30,flexWrap:'wrap',fontSize:15,fontWeight:800,color:BK.ink}}>{ws.map(w => sprTickW(w))}</div>;
const sacCircleHow = 'Circle every later note the sign still changes: not the note with the sign.';

const SAC_WB = {
  keys2: [[33, '#'], [29, 'b'], [32, '#'], [30, 'b']],                       // A♯ (done), D♭, G♯, E♭
  draw2: [[29, '#'], [32, 'b'], [38, '#'], [37, 'b']],                       // draw the sign: D♯, G♭, F♯ (top line), E♭ (top space)
  play2: sacQ([[28, '#'], 29, [30, 'b'], [31, '#'], 32, '||']),               // C♯ D E♭ F♯ G
  nat3: [[33, 'b', 32], [29, '#', 30], [37, 'b', 36], [32, '#', 31]],          // X sign, Y, X natural: name the third (A done; D, E, G)
  draw3: [sacQ([[31, '#'], 32, [31, 'n'], '||']), sacQ([[30, 'b'], 29, [30, 'n'], '||'])],   // F♯ G F♮; E♭ D E♮
  play3: sacT([[38, '#'], 37, [38, 'n'], 36, '|', [33, 'b'], 32, [33, 'n'], 35, '||']),        // F♯ E F D | A♭ G A C
  circ4: [sacT([[32, '#'], 30, 32, 33, '|', 32, 31, ['h', 2, 30], '||']),                       // G♯ E G♯ A | G F E: note 3 (done)
          sacT([[31, '#'], 32, 31, 31, '|', 30, [29, '#'], 29, 28, '||'])],                     // F♯ G F♯ F♯ | E D♯ D♯ C: notes 3, 4, 7
  names4: [sacT([[28, '#'], 30, 29, 28, '|', 30, 28, ['h', 2, 29], '||']),                      // C♯ E D C♯ | E C D
           sacT([[31, '#'], 30, [31, 'n'], 31, '|', 32, [31, '#'], ['h', 2, 30], '||'])],       // F♯ E F♮ F | G F♯ E: the natural holds too
  play4: sacT([[30, 'b'], 32, 31, 30, '|', 30, 29, ['h', 2, 28], '||']),                        // E♭ G F E♭ | E D C
  circ5: [sacT([[29, '#'], 31, 36, 29, '|', 36, 29, ['h', 2, 28], '||']),                       // D♯ F D(high) D♯ | D D C: note 4 (done)
          sacT([32, [39, '#'], 32, 39, '|', 39, [32, '#'], 39, 32, '||'])],                     // G G♯ G G♯ | G G♯ G G♯: notes 4, 8
  names5: [sacT([[31, '#'], 38, 31, 33, '|', 38, [38, '#'], ['h', 2, 31], '||']),               // F♯ F F♯ A | F F♯ F
           sacT([[35, '#'], 28, 35, 32, '|', 28, 35, ['h', 2, 32], '||'])],                     // C♯ C C♯ G | C C G
  play5: sacT([[30, 'b'], 37, 30, 32, '|', 37, 30, ['h', 2, 28], '||']),                        // E♭ E E♭ G | E E C
  try6: [sacT([33, [31, '#'], 32, 31, '|', [34, 'b'], 33, ['h', 2, 34], '||']), sacT([[29, '#'], 30, 29, 28, '|', [33, 'b'], 32, 33, 31, '||'])],   // A F♯ G F | B♭ A B; D♯ E D C | A♭ G A F
  tune6: sacT([32, [31, '#'], 30, 31, '|', 32, 31, ['h', 2, 30], '|', [30, 'b'], 31, 30, 32, '|', 31, 30, ['h', 2, 28], '||']),   // C position
};
const SAC_CHK = {
  signs: [[37, 'b'], [32, 'n'], [35, '#']],                                   // E♭, G♮, C♯: flat, natural, sharp
  keys: [[32, 'b'], [29, '#']],                                               // G♭ (a key no Workbook item uses), D♯
  names: [sacQ([[34, 'b'], 34, 33, 35, '||']), sacT([[28, '#'], 29, '|', 30, 28, '||'], 2), sacQ([[36, '#'], 35, 29, 37, '||']), sacQ([[32, '#'], 33, [32, 'n'], 32, '||'])],
  at: [1, 3, 2, 3],                                                           // the coral note of each: B♭, C, D, G
  draw: [[sacQ([[29, 'b'], 28, [29, 'n'], '||']), 2, 'D'], [sacQ([31, 32, [33, 'b'], '||']), 2, 'A♭']],   // natural; flat
  circ: sacT([[35, '#'], 34, 35, 36, '|', 35, [34, 'b'], 33, 34, '||']),       // C♯ held (3), B♭ held (8)
};

function SacWorkbook({ startNo = 1 }) {
  const W = SAC_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="accidentals">{content}</WbPage>);
  const rows = (list, oOf, n0, ref = 460) => { const box = sacSetBox(list, ref, oOf); return <div style={{display:'grid',gap:8}}>{list.map((it, i) => sskRowN(n0 + i, sacPaper(it, oOf(it, i), ref, box)))}</div>; };
  const playRow = (n, items, ticks, ref = 520) => sskRowN(n, <div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{sacPaper(items, {}, ref)}{sacTicks(ticks)}</div>);

  // 2 (faces "Sharp and flat")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Find the key" how="Put a dot on the key of each note. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.keys2.map(([d, s], i) => <ExCell key={i} n={i + 1} ex={i === 0}>{sacKeyCell(d, s, i === 0)}</ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the sign" how="Draw the sign each note needs, just before it, on its line or space. Its name is under it.">
      {sskRowN(5, sacPaper(W.draw2.map(([d, s]) => ['w', 4, d, s]).concat([['||']]), { D: 15, room: 20, noSign: [0, 1, 2, 3], under: W.draw2.map(([d, s]) => sacNameRaw({ d, acc: SAC_ACC[s] }, 16)) }, 330))}
    </Part>
    <Part kind="play" title="Play the signs" how="Play these notes, saying each name. Then play them again with your eyes on the music. Tick each time.">
      {playRow(6, W.play2, ['saying the names', 'eyes on the music'], 335)}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "The natural")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Name the last note" how="Write the name of the coral note in its box. The first one is done.">
      <BkGrid cols={2} gap="8px 14px">{W.nat3.map(([x, s, y], i) => { const items = sacQ([[x, s], y, [x, 'n'], '||']);
        return <ExCell key={i} n={i + 1} ex={i === 0}>{sdyCol(sacPaper(items, { hl: [2], under: [undefined, undefined, i === 0 ? dName(x) : null], underCoral: i === 0 ? [2] : [], underBoxed: true }, 176), '14px 6px 4px')}</ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Make it plain" how="The coral note must be plain. Draw a natural just before it.">
      <BkGrid cols={2} gap="8px 14px">{W.draw3.map((items, i) => <BkCell key={i} n={i + 5}><div style={{padding:'12px 4px 4px'}}>{sacPaper(items, { hl: [2], noSign: [2], room: 20 }, 176)}</div></BkCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Play the naturals" how="Play this, saying “sharp”, “flat” and “natural” as you meet them. Tick each time.">
      {playRow(7, W.play3, ['once', 'twice', 'without stopping'])}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Until the bar line")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Circle the changed notes" how={sacCircleHow + ' The first line is done.'}>
      {rows(W.circ4, (items, i) => ({ ring: i === 0 ? sacChanged(items) : [] }), 1)}
    </Part>
    <Part kind="home" title="Write the names" how="Write each note’s name in its box: its letter, and ♯ or ♭ when it sounds sharp or flat.">
      {rows(W.names4, (items) => ({ under: sacRead(items).map(() => null) }), 3)}
    </Part>
    <Part kind="play" title="Play it" how="Play this, saying the names. Tick each time.">
      {playRow(5, W.play4, ['saying the names', 'just playing'], 470)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Its own line or space")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Circle the changed notes" how={sacCircleHow + ' Look at its line or space. The first line is done.'}>
      {rows(W.circ5, (items, i) => ({ ring: i === 0 ? sacChanged(items) : [] }), 1, 475)}
    </Part>
    <Part kind="home" title="Write the names" how="Write each note’s name in its box: its letter, and ♯ or ♭ when it sounds sharp or flat.">
      {rows(W.names5, (items) => ({ under: sacRead(items).map(() => null) }), 3, 475)}
    </Part>
    <Part kind="play" title="Play it" how="Play this, saying the names. Jump your hand for the notes an octave apart. Tick each time.">
      {playRow(5, W.play5, ['saying the names', 'just playing'])}
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Reading a tune")
  const t6 = sacRows(W.tune6);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="How far does it go?" how="Draw a bracket from each sign to the bar line where it stops. The first one is done.">
      {rows(W.try6, (items, i) => (i === 0 ? { bracket: { from: 1, bar: 0, label: '' } } : { bracketRoom: true }), 1, 450)}
    </Part>
    <Part kind="home" title="Write the names" how="Write each note’s name in its box, bar by bar.">
      {rows(t6, (row) => ({ under: sacRead(row).map(() => null) }), 3, 450)}
    </Part>
    <Part kind="play" title="Play the tune" how="Right hand in C position: play the tune you named three ways: saying the names, just playing, then with a steady beat. Tick each time.">
      {sskRowN(5, sacTicks(['saying the names', 'just playing', 'with a steady beat']))}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper
  P(<SacPaperCheck/>);
  return <>{pages}</>;
}
const sacChkNo = () => { const C = SAC_CHK, nB = C.signs.length + 1, nC = nB + C.keys.length, nD = nC + C.names.length; return { nB, nC, nD, nE: nD + C.draw.length }; };
function SacPaperCheck() {
  const C = SAC_CHK, { nB, nC, nD, nE } = sacChkNo();
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4,flex:'1 0 auto'}}>
    <LbPaperHead/>
    {bkSec('A', 'Circle the name of each sign.')}
    <BkGrid cols={3} gap="6px 8px">{C.signs.map(([d, s], i) => <BkCell key={i} n={i + 1}>{sdyCol(<><div style={{maxWidth:110,margin:'0 auto',width:'100%'}}><SacStaff items={[['w', 4, d, s], ['||']]} width={110} full o={{ D: 16 }}/></div>{sdyCircle(['sharp', 'flat', 'natural'], null, true, 10)}</>, '8px 2px 4px')}</BkCell>)}</BkGrid>
    {bkSec('B', 'Put a dot on the key of each note.')}
    <BkGrid cols={2} gap="6px 10px">{C.keys.map(([d, s], i) => <BkCell key={i} n={nB + i}><div style={{display:'grid',gridTemplateColumns:'1fr 1.5fr',alignItems:'center',gap:10,padding:'12px 8px 6px'}}><SacStaff items={[['w', 4, d, s], ['||']]} width={110} full pad={[22, 30]} o={{ D: 14 }}/><TnPKeys start="C" whites={7} w={28} h={72} slots wslots/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Write the name of the coral note.')}
    <BkGrid cols={2} gap="6px 10px">{C.names.map((items, i) => <BkCell key={i} n={nC + i}><div style={{padding:'4px 4px 2px'}}>{sacPaper(items, { hl: [C.at[i]], under: sacRead(items).map((_, j) => j === C.at[i] ? null : undefined), boxS: 30 }, 265)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Draw the sign the coral note needs, just before it.')}
    <BkGrid cols={2} gap="6px 10px">{C.draw.map(([items, at, want], i) => <BkCell key={i} n={nD + i}><div style={{padding:'5px 4px 2px'}}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{sscSx('It must sound ' + want + '.')}</div>{sacPaper(items, { hl: [at], noSign: [at], room: 20 }, 255)}</div></BkCell>)}</BkGrid>
    {bkSec('E', sacCircleHow)}
    <BkCell n={nE}><div style={{padding:'10px 4px 4px'}}>{sacPaper(C.circ, {}, 640)}</div></BkCell>
  </div>;
}

function SacTeacher() {
  const W = SAC_WB, C = SAC_CHK, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="accidentals" teacher>{content}</WbPage>);
  const nm = (d, s) => sacNm(d, SAC_ACC[s]);
  const keyOf = (d, s) => nm(d, s) + ': the black key just ' + (s === '#' ? 'above ' : 'below ') + dName(d);
  const names = (items) => { const r = sacNamesOf(items), bars = []; let k = 0; items.forEach(it => { if (it[0] === '|' || it[0] === '||') bars.push(k); else if (sacIsNote(it)) k++; });
    return r.map((x, j) => x + (bars.includes(j + 1) && j + 1 < r.length ? ' |' : '')).join(' '); };
  const changed = (items) => { const r = sacRead(items); return sacChanged(items).map(j => 'note ' + (j + 1) + ' (' + sacNameTxt(r[j]) + ')').join(', '); };
  const marks = { A: C.signs.length, B: C.keys.length, C: C.names.length, D: C.draw.length, E: 1 };
  const total = Object.values(marks).reduce((a, b) => a + b, 0);
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('accidentals')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Sharps, flats and naturals written in the music (chapter {bkChapterNo('tones')}: the half step, F♯ = G♭; chapter {bkChapterNo('time-signatures')}: bar lines and the tie; chapter {bkChapterNo('reading-steps')}: reading a tune). AMEB Preliminary reads sharps and flats; Grade 1 adds the natural. The rules: a sign lasts to the end of its bar, for its own line or space only; after the bar line the note is plain again, unless it is tied over. Not here: key signatures (chapter {bkChapterNo('key-signatures')}), double sharps and flats, reminder signs in brackets. The drill comes after page 6; level 9 (the bass clef) is extra.</div>
    <div style={{fontSize:12.5,color:BK.ink,margin:'0 0 12px',lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'7px 10px'}}><b style={{color:BK.coral}}>Lesson time: the sign’s journey.</b> Point to a sign; the child slides a finger along its line or space to the bar line, saying the note’s name at every note it passes.</div>
    <TcBlock page={2} title="Sharp and flat" answers={<>{sscLesson('Play D, G or A, then its sharp and its flat; the child names each. Then they show where each sign sits on the staff.')}{tcAns('TRY IT', W.keys2.map(([d, s], i) => keyOf(d, s) + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', [W.draw2.map(([d, s]) => nm(d, s)).join(', ') + ': each sign on its note’s line or space, just before it'], 5)}{tcAns('PLAY', [names(W.play2)], 6)}</>}
      watch="The sign drawn after the note, or a line or space too high. A sharp read as 'down'. The sign said before the letter ('sharp F')."
      say="“Sharp: up a half step. Flat: down a half step.”"/>
    <TcBlock page={3} title="The natural" answers={<>{sscLesson('Play B♭ then B♮, F♯ then F♮: the child says which is the natural each time.')}{tcAns('TRY IT', W.nat3.map(([x], i) => dName(x) + ' (or ' + dName(x) + '♮)' + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', ['a natural before F', 'a natural before E'], 5)}{tcAns('PLAY', [names(W.play3)], 7)}</>}
      watch="The natural read as 'sharp' (they look alike). A natural thought to raise or lower on its own. After B♭, B♮ played as B♭ again."
      say="“A natural cancels: back to the plain note.”"/>
    <TcBlock page={4} title="Until the bar line" answers={<>{sscLesson('Play a bar with a sign and the same note again later; the child stops you at the bar line.')}{tcAns('TRY IT', W.circ4.map((it, i) => changed(it) + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', W.names4.map(names), 3)}{tcAns('PLAY', [names(W.play4)], 5)}</>}
      watch="The sign forgotten after the first note. The sign carried over the bar line. A natural forgotten for the later notes of its bar. Every note of the bar changed, not only the same line or space."
      say="“A sign lasts until the bar line.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Its own line or space" answers={<>{sscLesson('Play F♯ high, then F low: the child hears that the low F is plain.')}{tcAns('TRY IT', W.circ5.map((it, i) => changed(it) + (i === 0 ? ' (done)' : '')))}{tcAns('YOUR TURN', W.names5.map(names), 3)}{tcAns('PLAY', [names(W.play5)], 5)}</>}
      watch="Every F changed because one F has a sharp. The octave note read on the wrong line."
      say="“A sign changes only its own line or space.”"/>
    <TcBlock page={6} title="Reading a tune" answers={<>{sscLesson('Before playing, the child points to each sign and to its bar line, then names every note.')}{tcAns('TRY IT', ['F♯ to the end of bar 1 (done); B♭ to the end of bar 2', 'D♯ to the end of bar 1; A♭ to the end of bar 2'])}{tcAns('YOUR TURN', sacRowNames(W.tune6), 3)}{tcAns('PLAY', ['the tune, three ways'], 5)}</>}
      watch="A held sign missed in the middle of a bar. The F of bar 2 or the E of bar 4 played with the sign of the bar before. The tune stopping at each sign."
      say="“Find the signs, find the bar lines, then play.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.signs.map(([, s]) => SAC_WORD[s]()))}
      {tcAns('B', C.keys.map(([d, s]) => keyOf(d, s)), sacChkNo().nB)}
      {tcAns('C', C.names.map((items, i) => { const n = sacRead(items)[C.at[i]]; return sacNameTxt(n) + (!n.acc ? ' (or ' + sacNameTxt(n) + '♮)' : ''); }), sacChkNo().nC)}
      {tcAns('D', ['a natural before D', 'a flat before A'], sacChkNo().nD)}
      {tcAns('E', [changed(C.circ)], sacChkNo().nE)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer; E is one mark if both notes are circled and nothing else: A {marks.A}, B {marks.B}, C {marks.C}, D {marks.D}, E {marks.E}; {total} in all. A section with any wrong answer is not passed yet: go back to its pages below. Also listen to the student (My five checks, Lesson Book page 7).</div>
    </>}
      goBack={[{ id: 'a', step: '1 and 2', page: '2 and 3' }, { id: 'b', step: 1, page: 2 }, { id: 'c', step: '2, 3 and 4', page: '3, 4 and 5' }, { id: 'd', step: '1 and 2', page: '2 and 3' }, { id: 'e', step: '3 and 4', page: '4 and 5' }]}/>
    <div style={{border:'0.8px solid ' + BK.hair,padding:'7px 12px',fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>My five checks (Lesson Book page 7): what to ask.</b> 1. Page 2: point to a sharp, a flat and a natural and say what each does. 2. Page 3: play B♭ then B♮. 3. Page 4: play page 4’s two bars, naming each note. 4. Page 5: play page 5’s bar, the low F plain. 5. Page 6: play the tune without stopping. Got it! means right without help.</div>
  </>);
  return <>{pages}</>;
}
// the tune's names, a row of two bars at a time (the Teacher copy's two answers)
const sacRowNames = (items) => sacRows(items).map(row => { const r = sacNamesOf(row), out = []; let k = 0; row.forEach(it => { if (it[0] === '|' && k < r.length) out.push('|'); else if (sacIsNote(it)) out.push(r[k++]); }); return out.join(' '); });
WORKBOOKS.accidentals = SacWorkbook;
TEACHER_COPIES.accidentals = SacTeacher;
