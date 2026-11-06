#!/usr/bin/env python3
# Phase 408: her second batch on the v2 print (Sohyun 2026-10-09 23:37)
#   1. note bingo cells clipped the note over the bass staff -- every cell now reserves the same headroom
#   2. 'Circle every middle C' = ONE long staff with eight notes; the CABBAGE staff got longer too
#   3. 'Draw the Queen's notes' -> a creative one: COMPOSE a tune for the Queen (draw any four of her five, play it)
#   4. pages 2 and 3 don't leave empty middles: p2 gains 'draw your own kebabs and sandwiches',
#      p3 gains 'the staircase tune' (follow step/skip signs, draw the walk, play it)
#   5. the book's check page (p7) fills its bottom: 'The royal signs' recap + what comes next
#   python3 patch408.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. bingo cells: equal headroom either side, so the C over the bass staff is never shaved
rep("""<PaperStaff clef={d >= 28 ? 'treble' : 'bass'} notes={[{ d }]} width={56}/>""",
    """<PaperStaff clef={d >= 28 ? 'treble' : 'bass'} notes={[{ d }]} width={60} minSpan={d >= 28 ? [39, 27] : [29, 17]}/>""", 'bingo headroom')

# 2a. circle every middle C: one long staff, eight notes, three of them Clara's
rep("""    mid: [0, 1].map(() => { const cs = shuffle([0, 1, 2, 3, 4]).slice(0, 2); const rest = [24, 25, 26, 27, 29, 30, 31, 32]; return [0, 1, 2, 3, 4].map(i => cs.includes(i) ? { d: 28, staff: Math.random() < 0.5 ? 'treble' : 'bass' } : { d: rest[Math.floor(Math.random() * rest.length)] }); }),""",
    """    mid: [0].map(() => { const cs = shuffle([0, 1, 2, 3, 4, 5, 6, 7]).slice(0, 3); const rest = [24, 25, 26, 27, 29, 30, 31, 32]; return [0, 1, 2, 3, 4, 5, 6, 7].map(i => cs.includes(i) ? { d: 28, staff: Math.random() < 0.5 ? 'treble' : 'bass' } : { d: rest[Math.floor(Math.random() * rest.length)] }); }),""", 'mid gen')
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10}}>{W.s5.mid.map((row, i) => <div key={i} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><PaperStaff clef="grand" notes={row} width={330}/></div>)}</div>""",
    """      {W.s5.mid.map((row, i) => <div key={i} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 14px',maxWidth:620,margin:'0 auto',width:'100%'}}><PaperStaff clef="grand" notes={row} width={560}/></div>)}""", 'mid render')
# 2b. the seven-note CABBAGE staff runs long
rep("""        <div style={{flex:'1 1 auto',maxWidth:330}}><PaperStaff clef={m.clef} notes={m.notes.map(d => ({ d }))} width={330}/></div>""",
    """        <div style={{flex:'1 1 auto',maxWidth:440}}><PaperStaff clef={m.clef} notes={m.notes.map(d => ({ d }))} width={430}/></div>""", 'cabbage long')

# 3. p4: compose for the Queen instead of draw-the-letter cells
old = s[s.index("""    <Part kind="play" style={{justifyContent:'center'}} title="Draw the Queen's notes\""""):]
old = old[:old.index("</Part>") + len("</Part>")]
rep(old, """    <Part kind="play" title="Make a tune for the Queen" how="Draw any FOUR of her five notes on the staff -- your own tune! Write its letters in the boxes, then play it to someone with your right hand.">
      <div style={{maxWidth:500,margin:'0 auto',width:'100%'}}>
        <PaperStaff clef="treble" notes={[]} width={500} minSpan={[27, 34]}/>
        <div style={{display:'flex',gap:8,justifyContent:'center',marginTop:6}}>{[0, 1, 2, 3].map(i => <span key={i} style={{width:30,height:30,border:'1.4px solid ' + BK.ink,borderRadius:6,display:'inline-block'}}/>)}</div>
      </div>
      <div style={{fontSize:11.5,color:BK.muted,textAlign:'center',marginTop:6}}>Give your tune a name: ______________________</div>
    </Part>""", 'queen compose')

# 4a. p2: draw your own kebabs and sandwiches, inside the plates box
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10,marginTop:8}}>
        {[['Kebab plate (line notes)', true], ['Sandwich plate (space notes)', false]].map(([lbl]) => <div key={lbl} style={{border:'1.6px solid ' + BK.ink,borderRadius:40,minHeight:44,display:'flex',alignItems:'center',justifyContent:'center',fontSize:12,fontWeight:800,color:BK.muted}}>{lbl}</div>)}
      </div>
    </Part>""",
    """      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10,marginTop:8}}>
        {[['Kebab plate (line notes)', true], ['Sandwich plate (space notes)', false]].map(([lbl]) => <div key={lbl} style={{border:'1.6px solid ' + BK.ink,borderRadius:40,minHeight:44,display:'flex',alignItems:'center',justifyContent:'center',fontSize:12,fontWeight:800,color:BK.muted}}>{lbl}</div>)}
      </div>
      <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:16,fontWeight:800,color:BK.ink,margin:'12px 0 2px'}}>Now cook your own</div>
      <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 6px',lineHeight:1.45}}>Draw three kebabs (line notes) and three sandwiches (space notes) -- anywhere on this staff, any order. Ask someone to point at each one and say which it is.</div>
      <div style={{maxWidth:500,margin:'0 auto',width:'100%'}}><PaperStaff clefOn={false} notes={[]} width={500} minSpan={[29, 39]}/></div>
    </Part>""", 'p2 cook your own')

# 4b. p3: the staircase tune, under 'Which is higher?' in the same box (and the box may fill the page again)
rep("""const s2 = withSeed(k('s2'), () => ({ tog: Array.from({ length: 4 }, () => mkSS(30, 38)), home: Array.from({ length: 8 }, () => mkSS(30, 38)), hi: Array.from({ length: 4 }, () => mkSS(30, 38)) }));""",
    """const s2 = withSeed(k('s2'), () => ({ tog: Array.from({ length: 4 }, () => mkSS(30, 38)), home: Array.from({ length: 8 }, () => mkSS(30, 38)), hi: Array.from({ length: 4 }, () => mkSS(30, 38)),
    stair: (() => { let d = 31; const moves = []; for (let i = 0; i < 4; i++) { let m; do { m = [1, 2, -1, -2][Math.floor(Math.random() * 4)]; } while (d + m < 30 || d + m > 38); d += m; moves.push({ m, d }); } return { start: 31, moves }; })() }));""", 's2 stair gen')
rep("""    <Part kind="play" grow={false} title="Which is higher?" how="Circle the higher note in each pair -- then play both, low one first, and check with your ears.">
      <BkGrid cols={4} gap="5px 8px">{W.s2.hi.map((it, i) => <BkCell key={i} n={i + 1}><div style={{padding:'8px 4px 2px'}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={92}/></div></BkCell>)}</BkGrid>
    </Part>""",
    """    <Part kind="play" title="Which is higher?" how="Circle the higher note in each pair -- then play both, low one first, and check with your ears.">
      <BkGrid cols={4} gap="5px 8px">{W.s2.hi.map((it, i) => <BkCell key={i} n={i + 1}><div style={{padding:'8px 4px 2px'}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={92}/></div></BkCell>)}</BkGrid>
      <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:16,fontWeight:800,color:BK.ink,margin:'12px 0 2px'}}>The staircase tune</div>
      <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 6px',lineHeight:1.45}}>The first note is drawn. Follow the signs left to right, drawing each next note -- then play your staircase with one hand and hear it climb and fall.</div>
      <div style={{maxWidth:500,margin:'0 auto',width:'100%'}}>
        <PaperStaff clefOn={false} notes={[{ d: W.s2.stair.start, x: 50, color: BK.coral }]} width={500} minSpan={[29, 39]}/>
        <div style={{display:'flex',justifyContent:'space-between',padding:'4px 10px 0 70px',fontSize:11.5,fontWeight:800,color:BK.ink}}>
          {W.s2.stair.moves.map((mv, i) => <span key={i}>{i + 1} · {({ 1: 'step up', 2: 'skip up', '-1': 'step down', '-2': 'skip down' })[mv.m]}</span>)}
        </div>
      </div>
    </Part>""", 'p3 staircase')

# 5. the book's check page: the royal signs recap and what comes next (print only)
rep("""      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
    </LbPage>,""",
    """      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbOnly print><div style={{border:'1.4px solid #ece6d8',borderRadius:14,padding:'12px 16px'}}>
        <div style={{fontFamily:LB_SERIF,fontSize:19,fontWeight:800,color:BK.ink,marginBottom:8}}>{t('The royal signs', '왕실의 기호들')}</div>
        {[['treble', 32, t('the Queen sings high -- her curl holds the G line. The right hand reads her staff.', '여왕은 높은 목소리 -- 소용돌이가 G 줄을 감싸요. 보통 오른손이 읽어요.')],
          ['bass', 24, t('the King sings low -- his two dots guard the F line. The left hand reads his staff.', '왕은 낮은 목소리 -- 두 점이 F 줄을 지켜요. 보통 왼손이 읽어요.')]].map(([cl, ln, txt0]) => <div key={cl} style={{display:'flex',alignItems:'center',gap:14,padding:'5px 0',borderTop:'1px solid #f1ece0'}}>
          <div style={{width:108,flex:'0 0 auto'}}><SfStaff clef={cl} width={110} pad={[12, 12]} label="" extra={(yOf, layer) => layer === 'under' && <line x1="4" x2="106" y1={yOf(ln)} y2={yOf(ln)} stroke={BK.coral} strokeOpacity="0.55" strokeWidth="3"/>}/></div>
          <PenArt shapes={cl === 'treble' ? sfQueen(26, 28, 1) : sfKing(26, 28, 1)} vb={[2, 2, 48, 52]} style={{width:46,flex:'0 0 auto'}}/>
          <div style={{fontSize:13,color:BK.ink,lineHeight:1.45}}>{txt0}</div>
        </div>)}
        <div style={{display:'flex',alignItems:'center',gap:14,padding:'5px 0',borderTop:'1px solid #f1ece0'}}>
          <div style={{width:108,flex:'0 0 auto'}}><svg viewBox="0 0 110 36" style={{width:'100%',display:'block'}} aria-hidden="true"><line x1="36" x2="74" y1="18" y2="18" stroke={BK.ink} strokeOpacity="0.75" strokeWidth="1.3"/><ellipse cx="55" cy="18" rx="7.4" ry="5.2" fill={BK.coral}/><ellipse cx="55" cy="18" rx="3.4" ry="2.7" transform="rotate(-38 55 18)" fill="#fff"/><line x1="51" x2="59" y1="18" y2="18" stroke={BK.ink} strokeOpacity="0.75" strokeWidth="1.3"/></svg></div>
          <PenArt shapes={sfClara(26, 28, 1)} vb={[2, 2, 48, 52]} style={{width:46,flex:'0 0 auto'}}/>
          <div style={{fontSize:13,color:BK.ink,lineHeight:1.45}}>{t('Princess Clara -- middle C on her little ladder rung, the same key from either palace.', '클라라 공주 -- 작은 사다리 발판 위의 가운데 도, 어느 궁전에서 써도 같은 건반.')}</div>
        </div>
        <div style={{fontSize:13,color:BK.ink,marginTop:8}}><b style={{color:BK.coral}}>{t('Next: ', '다음: ')}</b>{t('Chapter 5 · The Whole Staff -- every line and space on both staves, and the rhymes that go with them.', '5챕터 · 오선 전체 읽기 -- 두 오선의 모든 줄과 칸, 그리고 외우는 문장들.')}</div>
      </div></LbOnly>
    </LbPage>,""", 'p7 recap')

# the Teacher copy follows: compose and staircase answers; the ghost DRAW lines go
rep("""{tcAns('DRAW', W.s3.draw.map(L => L + ': ' + { C: 'her ladder rung', D: 'just under line 1', E: 'line 1', F: 'space 1', G: 'line 2, the Queen\\u2019s' }[L]))}""",
    """{tcAns('COMPOSE', ['any four of C D E F G -- check each drawn note against the letter written under it; then they play it'])}""", 'tc p4')
rep("""{tcAns('DRAW', W.s4.draw.map(L => L + ': ' + { F: 'line 4, the King\\u2019s', G: 'space 4', A: 'line 5, the top line', B: 'just over the top line', C: 'her ladder rung above' }[L]))}""",
    "", 'tc p5 ghost draw')
rep("""{tcAns('HIGHER', W.s2.hi.map(it => it.a > it.b ? '1st' : '2nd'))}""",
    """{tcAns('HIGHER', W.s2.hi.map(it => it.a > it.b ? '1st' : '2nd'))}{tcAns('STAIRS', W.s2.stair.moves.map(mv => (mv.d - 30) % 2 === 0 ? 'line ' + ((mv.d - 30) / 2 + 1) : 'space ' + ((mv.d - 29) / 2)))}""", 'tc stairs')
rep("""{tcAns('PLATES', ['kebab: ' + W.s1.sort.map((it, i) => sfLS(it.d) === 'L' ? i + 1 : null).filter(Boolean).join(' ') , 'sandwich: ' + W.s1.sort.map((it, i) => sfLS(it.d) === 'S' ? i + 1 : null).filter(Boolean).join(' ')])}""",
    """{tcAns('PLATES', ['kebab: ' + W.s1.sort.map((it, i) => sfLS(it.d) === 'L' ? i + 1 : null).filter(Boolean).join(' '), 'sandwich: ' + W.s1.sort.map((it, i) => sfLS(it.d) === 'S' ? i + 1 : null).filter(Boolean).join(' '), 'own staff: any 3 line + 3 space notes, each checked against its own look'])}""", 'tc plates')

open(src, 'w', encoding='utf-8').write(s); print('patch408 ok')
