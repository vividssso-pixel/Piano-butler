"""Build EF (her 31 Oct 23:05 and 23:22: the Workbooks, fun first, the Beginner floor, starting with one page): chapter 7's
Workbook page 4, YOUR TURN 'Draw the sound lines' (the same task as page 3's) becomes 'The hidden note': colour every
note that lasts 3 beats and a big dotted minim appears; circle its name, write its beats. PLAY renumbered 10 and 11; the
Teacher copy's answers follow. Code in sc/wbf44.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
CODE = open(os.path.join(here, 'wbf44.code.js'), encoding='utf-8').read()
R("""function NvWorkbook({ startNo = 1 }) {""", CODE + """function NvWorkbook({ startNo = 1 }) {""")
# chapter 7, page 4: the hidden note in place of the second 'Draw the sound lines'
R("""  lines4: [[['hd', 3], ['q', 1]], [['w', 4]], [['q', 1], ['hd', 3]], [['h', 2], ['h', 2]]],
""", """  // (the hidden note, NV_HIDE, is YOUR TURN here)
""")
R("""    <Part kind="home" title="Draw the sound lines" how="Draw each note's sound line on the dotted line, as long as its beats.">
      <BkGrid cols={2} gap="8px 12px">{W.lines4.map((row, i) => nvBarCell(row, i, 9, false, () => ({ lines: 'guide', count: 'none' })))}</BkGrid>
    </Part>""", """    <Part kind="home" title="The hidden note" how="Colour every note that lasts 3 beats. A note appears: circle its name and write its beats.">
      <NvHidden/>
    </Part>""")
R("""{W.count4.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{nvNum(13 + r)}""",
  """{W.count4.map((row, r) => <div key={r} style={{display:'grid',gridTemplateColumns:'24px 1fr',alignItems:'center',gap:6}}>{nvNum(10 + r)}""")
R("""{tcAns('YOUR TURN', W.lines4.map(lineTxt), 9)}{tcAns('PLAY', W.count4.map(cnt), 13)}""",
  """{tcAns('YOUR TURN', ['the 14 dotted minims coloured: a big dotted minim appears (hollow head, stem, dot); dotted minim circled, 3 beats'], 9)}{tcAns('PLAY', W.count4.map(cnt), 10)}""")
R("""      watch="Mixing up the dotted minim (stem, dot) and the semibreve (no stem). Letting a semibreve go after two or three beats."
""", """      watch="Mixing up the dotted minim (stem, dot) and the semibreve (no stem). In the hidden note, colouring the minims too: look for the dot. Letting a semibreve go after two or three beats."
""")
# ── chapter 5, Hand positions ──
R("""      <div style={{display:'flex',gap:10,justifyContent:'center',padding:'10px 0'}}>{['G', '', 'B', '', 'D'].map((l, i) => <span key={i} style={{width:52,height:52,border:'2px solid ' + (l ? BK.ink : BK.coral),borderRadius:8,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:26,fontWeight:800,color:BK.ink}}>{l}</span>)}</div>""",
  """      <HpLadder/>""")
R("""    <Part kind="play" title="The letter ladder" how="Write the missing letters of G position. Then say them up and down, without the piano: G A B C D, D C B A G.">""",
  """    <Part kind="play" title="The letter ladder" how="Write the missing letters of G position, from G at the bottom. Then say them up and down, without the piano: G A B C D, D C B A G.">""")
R("""      <svg viewBox="0 0 600 150" style={{width:'100%',display:'block'}}>
        {[[40, 'C position'], [360, 'G position']].map(([x, l]) => <g key={l}>{[0, 1, 2, 3, 4].map(k => <rect key={k} x={x + k * 40} y="92" width="40" height="44" fill={k === 0 ? '#fbe3da' : '#fff'} stroke={BK.ink} strokeWidth="1.6"/>)}<text x={x + 100} y="84" textAnchor="middle" fontSize="13" fontWeight="900" fill={BK.ink}>{l}</text></g>)}
        <path d="M60 92 C90 10 400 10 380 92" fill="none" stroke={BK.coral} strokeWidth="2.4" strokeDasharray="2 7" strokeLinecap="round"/>
        {[[118, 40], [220, 22], [330, 40]].map(([x, y], i) => <line key={i} x1={x - 26} x2={x + 26} y1={y + 18} y2={y + 18} stroke={BK.line} strokeWidth="1.4"/>)}
      </svg>""",
  """      <svg viewBox="0 0 600 236" style={{width:'100%',display:'block'}}>
        {[[40, 'C position'], [360, 'G position']].map(([x, l]) => <g key={l}>{[0, 1, 2, 3, 4].map(k => <rect key={k} x={x + k * 40} y="160" width="40" height="70" fill={k === 0 ? '#fbe3da' : '#fff'} stroke={BK.ink} strokeWidth="1.6"/>)}<text x={x + 100} y="150" textAnchor="middle" fontSize="14" fontWeight="900" fill={BK.ink}>{l}</text></g>)}
        <path d="M60 160 C90 6 400 6 380 160" fill="none" stroke={BK.coral} strokeWidth="2.6" strokeDasharray="2 7" strokeLinecap="round"/>
        {[[112, 92], [220, 66], [328, 92]].map(([x, y], i) => <line key={i} x1={x - 30} x2={x + 30} y1={y} y2={y} stroke={BK.line} strokeWidth="1.4"/>)}
      </svg>""")
R("""    <Part kind="play" title="Draw the mirror" how="Put both hands flat, thumbs touching, and draw round them. Write the finger numbers: the same numbers face each other, like a mirror.">
      <div style={{display:'flex',flex:1}}>{area('Left hand · thumbs touching · right hand', 110)}</div>
    </Part>""",
  """    <Part kind="play" title="Fill in the mirror" how="The thumbs meet at the dashed line. Write the missing finger numbers: each number faces its twin. Then colour the two 3s.">
      <HpMirrorFill/>
    </Part>""")
R("""    <Part kind="play" title="Make your own echo" how="Write a call for the right hand in the first four circles. Write the left hand's answer, with the same letters, in the next four. Play it with someone at home: you call, they answer.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,padding:'8px 4px'}}>{['Right hand calls', 'Left hand answers'].map((l, k) => <div key={l}><div style={{fontSize:10.5,fontWeight:900,color:k ? BK.coral : BK.muted,marginBottom:4}}>{l}</div><PhCircles seq={['?', '?', '?', '?']} size={40}/></div>)}</div>
    </Part>""",
  """    <Part kind="play" title="The finger code" how="Write the letter each finger plays. Every row spells a word! The first one is done.">
      <BkGrid cols={2} gap="8px 12px">{HP_CODE.map((row, i) => <HpCodeCell key={i} row={row} n={5 + i} ex={i === 0}/>)}</BkGrid>
    </Part>""")
R("""    <Part kind="play" title="Write your own tune" how="Right hand, C position. Write a finger number in each circle; a dashed circle holds one more beat. End on 1. Then play it, and give it a name.">
      <div style={{display:'grid',gap:8,padding:'4px 0'}}><PhCircles seq={['?', '?', '?', '?', '|', '?', '?', '?', '?', '|', '?', '?', '?', '?', '|', '?', '-', '-', '-']} size={27}/>
        <div style={{fontSize:12,color:BK.muted,display:'flex',alignItems:'center',gap:8}}>Name of my tune <span style={{display:'inline-block',flex:1,borderBottom:'1.5px solid ' + BK.line,height:18}}/></div></div>
    </Part>""",
  """    <Part kind="play" title="The same tune, higher" how="Right hand. Write the letter each finger plays, in C position and then in G position. Play both: the same tune, higher.">
      <HpSameTune/>
    </Part>""")
R("""{tcAns('PLAY', ['two hands drawn thumbs touching, the same numbers facing each other'])}""",
  """{tcAns('PLAY', ['left hand 5 4 3 2 1, right hand 1 2 3 4 5; the two 3s coloured, one each side of the line'])}""")
R("""{tcAns('PLAY', ['any call; the answer uses the same letters, so right 1 2 3 is left 5 4 3'])}""",
  """{tcAns('PLAY', HP_CODE.map(([h, pos, fs], i) => fs.map(f => hpLetter(pos, h, f)).join('') + (i ? '' : ' (done)')), 5)}""")
R("""{tcAns('PLAY', ['any tune of finger numbers 1 to 5, ending on 1'])}""",
  """{tcAns('PLAY', MT_SONGS.map(([name, , seq]) => name + ': C position ' + seq.map(f => hpLetter('C', 'R', f)).join(' ') + '; G position ' + seq.map(f => hpLetter('G', 'R', f)).join(' ')))}""")

# ── chapter 8, Dynamics & Articulation, page 3 ──
R("""    <Part kind="home" title="Number them, then the louder one" how="Row 2: number them 1 to 4, softest first. Boxes 3 to 6: circle the louder sign.">
      <div style={{display:'grid',gap:10}}>{sskRowN(2, order(W.order2))}
        <BkGrid cols={4} gap="8px 10px">{W.louder.map((pr, i) => <BkCell key={i} n={i + 3}><div style={{padding:'14px 2px 6px',display:'flex',justifyContent:'center',gap:40}}>{pr.map(s => <span key={s}>{sdyBig(s, 32, BK.ink)}</span>)}</div></BkCell>)}</BkGrid></div>
    </Part>
    <Part kind="play" title="Mark it, then play it" how={sdyHow('Write pp, p, mf and f, one in each box. Tune 7: each bar a little softer than the one before. Tune 8: each bar a little louder. Then right hand in C position: play each.')}>
      <div style={{display:'grid',gap:12}}>{sskRowN(7, <SdyPaper mm={5} items={W.softer} o={{ D: 26 }} k={{ dynBox: [0, 2, 4, 6] }}/>)}
        {sskRowN(8, <SdyPaper mm={4.8} items={W.louder8} o={{ D: 20 }} k={{ dynBox: [0, 4, 8, 12] }}/>)}</div>""",
  """    <Part kind="home" title="The voice ladder" how="How loud is each voice? Write its sign: pp, p, mf or f.">
      <SdyVoices/>
    </Part>
    <Part kind="play" title="Mark it, then play it" how={sdyHow('Write pp, p, mf and f, one in each box. Tune 6: each bar a little softer than the one before. Tune 7: each bar a little louder. Then right hand in C position: play each.')}>
      <div style={{display:'grid',gap:12}}>{sskRowN(6, <SdyPaper mm={5} items={W.softer} o={{ D: 26 }} k={{ dynBox: [0, 2, 4, 6] }}/>)}
        {sskRowN(7, <SdyPaper mm={4.8} items={W.louder8} o={{ D: 20 }} k={{ dynBox: [0, 4, 8, 12] }}/>)}</div>""")
R("""{tcAns('YOUR TURN', [sdyOrderOf(W.order2).join(' '), ...W.louder.map(louder)], 2)}{tcAns('PLAY', ['f mf p pp', 'pp p mf f'], 7)}""",
  """{tcAns('YOUR TURN', SDY_VOICES.map(([w, sgn]) => w + ': ' + sgn), 2)}{tcAns('PLAY', ['f mf p pp', 'pp p mf f'], 6)}""")

# ── chapter 10, Steps & Skips, page 3 ──
R("""    <Part kind="play" title="Draw it, then play it" how="Draw the second note: a step or a skip from the first. Then right hand, thumb on middle C: play the two notes.">
      <BkGrid cols={2} gap="8px 14px">{W.ss3.map(([d, mv], i) => <ExCell key={i} n={i + 7}><div style={{padding:'10px 2px 2px'}}><SskPaper mm={3.5} items={[['w', 4, d], ['sp', 50]]} o={{ D: 12, x0: 42 }}/>
        <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.ink}}>{(Math.abs(mv) === 1 ? 'a step ' : 'a skip ') + (mv > 0 ? 'up' : 'down')}</div></div></ExCell>)}</BkGrid>""",
  """    <Part kind="play" title="The secret word" how="Start on the red note. Follow the moves and draw each next note. Write every letter: they spell a word! Then right hand, thumb on middle C: play it.">
      <BkGrid cols={2} gap="8px 14px">{SSK_WORDS.map(([d, mv], i) => <SskWordPath key={i} start={d} moves={mv} n={i + 7}/>)}</BkGrid>""")
R("""{tcAns('PLAY', W.ss3.map(([d, mv]) => dName(d) + ' → ' + dName(d + mv)), 7)}""",
  """{tcAns('PLAY', SSK_WORDS.map(([d, mv]) => { const ds = [d]; mv.forEach(m => ds.push(ds[ds.length - 1] + m)); return ds.map(dName).join(' '); }), 7)}""")

# ── chapter 12, Time Signatures, page 3 ──
R("""    <Part kind="home" title="More time signatures" how="Write the time signature for each bar.">
      <BkGrid cols={2} gap="8px 14px">{W.sig2.map((r, i) => <ExCell key={i} n={i + 3}><div style={{padding:'10px 4px 0'}}><TsPaper mm={4.5} items={tsPaperItems({ ...r, sig: 'blank' })} o={{ D: 30, hearts: false }}/></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="Write it, then play it" how="Write the time signature. Then right hand, finger 3 on G: play it, counting out loud.">
      <div style={{display:'grid',gap:5}}>{W.sig3.map((r, i) => tsRowN(7 + i, <TsPaper""",
  """    <Part kind="home" title="Spot the wrong bar" how="Each tune has one bar with a beat too many. Count every bar, then cross out the wrong one.">
      <div style={{display:'grid',gap:8}}>{TS_WRONG.map((r, i) => <ExCell key={i} n={i + 3}><div style={{padding:'12px 4px 2px'}}><TsPaper mm={4.4} items={tsPaperItems(r)} o={{ D: 26, hearts: false }}/></div></ExCell>)}</div>
    </Part>
    <Part kind="play" title="Write it, then play it" how="Write the time signature. Then right hand, finger 3 on G: play it, counting out loud.">
      <div style={{display:'grid',gap:5}}>{W.sig3.map((r, i) => tsRowN(5 + i, <TsPaper""")
R("""{tcAns('YOUR TURN', W.sig2.map(sigTxt), 3)}{tcAns('PLAY', W.sig3.map(sigTxt), 7)}""",
  """{tcAns('YOUR TURN', TS_WRONG.map(r => 'bar ' + r.wrong + ' (' + r.bars[r.wrong - 1].reduce((a, k) => a + NV_ROOM[k].b, 0) + ' beats in ' + r.top + '/4)'), 3)}{tcAns('PLAY', W.sig3.map(sigTxt), 5)}""")

# ── chapter 13, Tones & Semitones, page 3 ──
R("""    <Part kind="play" title="Half or whole?" how="The two red keys: a half step or a whole step apart? Circle one.">
      <BkGrid cols={4} gap="8px 8px">{W.pairs.map((pr, i) => <ExCell key={i} n={i + 9} ex={i === 0}><div style={{padding:'14px 2px 3px'}}>
        <TnPKeys whites={8} w={26} h={72} you={pr}/>
        <div style={{display:'flex',justifyContent:'center',marginTop:4}}>{wsChoose(['half', 'whole'], i === 0 ? tnPairStep(pr) : null)}</div></div></ExCell>)}</BkGrid>""",
  """    <Part kind="play" title="The step trail" how="From the star, write each move's number on the key it lands on. Move 7 ends on the flag!">
      <TnTrail/>""")

R("""{tcAns('PLAY', W.pairs.map(p => nm(p[0]) + ' ' + nm(p[1]) + ': ' + tnPairStep(p)), 9)}""",
  """{tcAns('PLAY', [tnTrailKeys().map((k, i) => (i + 1) + ' ' + nm(k)).join(', ') + ': move 7 on the flag'], 9)}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok EF', len(s))
