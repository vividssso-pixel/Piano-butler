#!/usr/bin/env python3
# Phase 413: chapter 3's Workbook, bigger keyboards and pictures, and every task set (her Phase-410 rule):
# the residents' keyboards and the letter star grow; the word search's free bonus becomes two set riddles;
# the check-up fills its own page (big keys, letter rows one to a line).
#   python3 patch413.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# LetterRow and UpDownCell get a big size (the check-up page)
rep("""function LetterRow({ cells, n, ex }) {
  return (
    <div style={{display:'flex',alignItems:'center',gap:6,border:ex ? '1.5px solid ' + BK.coral : '1px solid #ece6d8',background:ex ? '#fff8f5' : '#fff',borderRadius:8,padding:'7px 10px'}}>
      <span style={{fontSize:10,fontWeight:900,color:BK.coral,minWidth:ex ? 54 : 16,letterSpacing:ex ? '0.06em' : 0}}>{ex ? 'EXAMPLE' : n}</span>
      {cells.map((c, i) => <span key={i} style={{width:32,height:34,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:17,fontWeight:900,""",
    """function LetterRow({ cells, n, ex, big }) {
  return (
    <div style={{display:'flex',alignItems:'center',gap:big ? 9 : 6,border:ex ? '1.5px solid ' + BK.coral : '1px solid #ece6d8',background:ex ? '#fff8f5' : '#fff',borderRadius:8,padding:big ? '9px 12px' : '7px 10px'}}>
      <span style={{fontSize:big ? 11 : 10,fontWeight:900,color:BK.coral,minWidth:ex ? 54 : big ? 40 : 16,letterSpacing:ex ? '0.06em' : 0}}>{ex ? 'EXAMPLE' : n}</span>
      {cells.map((c, i) => <span key={i} style={{width:big ? 42 : 32,height:big ? 44 : 34,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:big ? 21 : 17,fontWeight:900,""", 'LetterRow big')
rep("""function UpDownCell({ it, n, ex }) {
  return (
    <ExCell n={n} ex={ex}>
      <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,padding:'16px 4px 8px'}}>
        <span style={{fontSize:24,fontWeight:900,color:BK.ink}}>{it.l}</span>""",
    """function UpDownCell({ it, n, ex, big }) {
  return (
    <ExCell n={n} ex={ex}>
      <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,padding:big ? '20px 4px 12px' : '16px 4px 8px'}}>
        <span style={{fontSize:big ? 30 : 24,fontWeight:900,color:BK.ink}}>{it.l}</span>""", 'UpDownCell big')
rep("""        {ex ? bkHand(it.a, 40, 38) : bkBox(40, 38)}
      </div>
    </ExCell>""", """        {ex ? bkHand(it.a, 40, 38) : bkBox(big ? 48 : 40, big ? 46 : 38)}
      </div>
    </ExCell>""", 'UpDownCell box')

# p3: the octave keyboard taller
rep("""      <PaperKeys start="C" whites={22} w={26} h={96} fills={{ 0: '#fdeee8' }} arrows={<g>""",
    """      <PaperKeys start="C" whites={22} w={26} h={196} fills={{ 0: '#fdeee8' }} arrows={<g>""", 'p3 octave keys')
rep("""<div style={{display:'flex',gap:28,justifyContent:'center',marginTop:10,fontSize:13,color:BK.ink,alignItems:'center'}}><span>Cs on this keyboard: {bkBox(36, 28)}</span><span>Octave hops: {bkBox(36, 28)}</span></div>""",
    """<div style={{display:'flex',gap:36,justifyContent:'center',marginTop:16,fontSize:15,color:BK.ink,alignItems:'center'}}><span style={{display:'inline-flex',alignItems:'center',gap:8}}>Cs on this keyboard: {bkBox(46, 38)}</span><span style={{display:'inline-flex',alignItems:'center',gap:8}}>Octave hops: {bkBox(46, 38)}</span></div>""", 'p3 count boxes')

# p5: the residents' keyboards bigger (and their pictures); the big keyboards below give a little back
rep("""    <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:3}}>{nnResIcon(L, 42)}<span style={{fontSize:12.5,fontWeight:900,color:BK.ink}}>{NN_RES[L][0]}</span></div>
    <PaperKeys start="C" whites={7} w={20} h={50} dots={ex ? [NN_L7.indexOf(L)] : []} dotR={0.2}/>""",
    """    <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:4}}>{nnResIcon(L, 46)}<span style={{fontSize:13,fontWeight:900,color:BK.ink}}>{NN_RES[L][0]}</span></div>
    <PaperKeys start="C" whites={7} w={20} h={70} dots={ex ? [NN_L7.indexOf(L)] : []} dotR={0.2}/>""", 'p5 res cell')
rep("""<PaperKeys start="C" whites={14} w={36} h={134} dots={W.gl.kb} boxes={W.gl.kb}""",
    """<PaperKeys start="C" whites={14} w={36} h={116} dots={W.gl.kb} boxes={W.gl.kb}""", 'p5 glance keys')
rep("""      <div style={{maxWidth:560,margin:'0 auto',width:'100%'}}><PaperKeys start="C" whites={7} w={78} h={170} roofs/></div>""",
    """      <div style={{maxWidth:540,margin:'0 auto',width:'100%'}}><PaperKeys start="C" whites={7} w={78} h={150} roofs/></div>""", 'p5 draw keys')

# p6: the letter star bigger, its boxes bigger
rep("""        <LetterRing size={185} star start="A"/>""", """        <LetterRing size={310} star start="A"/>""", 'p6 ring')
rep("""{['A', '', '', '', '', '', '', 'A'].map((l, i) => <span key={i} style={{width:30,height:34,borderRadius:6,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:17,""",
    """{['A', '', '', '', '', '', '', 'A'].map((l, i) => <span key={i} style={{width:42,height:46,borderRadius:7,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:21,""", 'p6 boxes')
rep("""          <div style={{display:'flex',gap:5,flexWrap:'wrap'}}>{['A', '', '', '', '', '', '', 'A']""", """          <div style={{display:'flex',gap:8,flexWrap:'wrap',maxWidth:4 * 42 + 3 * 8}}>{['A', '', '', '', '', '', '', 'A']""", 'p6 boxes 4 a row')
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:20,alignItems:'center'}}>
        <LetterRing size={310} star start="A"/>""", """      <div style={{display:'grid',gridTemplateColumns:'1.15fr 1fr',gap:20,alignItems:'center',flex:1}}>
        <LetterRing size={310} star start="A"/>""", 'p6 grid')

# p7: the bonus is set -- two riddles in music letters
rep("""          <div style={{fontSize:12,color:BK.muted,marginTop:4,lineHeight:1.45}}>Bonus: make up your own music word<br/><span style={{display:'inline-block',width:150,borderBottom:'1px solid ' + BK.ink,marginTop:4}}>&nbsp;</span></div>""",
    """          <div style={{fontSize:12.5,color:BK.ink,marginTop:6,lineHeight:1.5}}><b>Bonus riddles</b> -- unscramble the music letters:
            {NN_RIDDLES.map(([clue, mix]) => <div key={mix} style={{display:'flex',alignItems:'center',gap:8,marginTop:6}}><span style={{minWidth:104}}>{clue}</span><b style={{letterSpacing:'0.14em'}}>{mix}</b> → {bkBox(64, 28)}</div>)}</div>""", 'p7 bonus')
rep("""const NN_WORDS = ['BAG', 'CAFE', 'EGG', 'FACE', 'BADGE', 'CAGE', 'BEAD'];""",
    """const NN_WORDS = ['BAG', 'CAFE', 'EGG', 'FACE', 'BADGE', 'CAGE', 'BEAD'];
// Phase 413: the word search's bonus is set, not free -- two riddles in music letters
const NN_RIDDLES = [['It buzzes:', 'E B E', 'BEE'], ['You sleep in it:', 'D B E', 'BED']];""", 'riddles data')

# Nothing twice (her Phase-409 rule): the Workbook does not re-teach what the facing book page shows --
# the four explanation panels go (the book's own pictures teach the doors, the wheel, up/down and skips)
import re
for key in ['<KeyScene start="C" whites={7} w={40} h={84} houses doors/>', '<LetterWheel size={118}/>', '<Staircase size={230}/>', '<LetterWheel size={110} mode="skip"/>']:
    pat = re.compile(r'^      <ArtLead pic=\{' + re.escape(key) + r'\}.*\n', re.M)
    if len(pat.findall(s)) != 1: raise SystemExit('artlead ' + key)
    s = pat.sub('', s)
# ... and the room they leave goes to bigger keys and letter boxes
rep("""      <KeysCell ex><PaperKeys start="E" whites={15} w={40} h={120} boxes={cf} labels={{ 1: 'F' }} ex={{ 1: true }}/></KeysCell>""",
    """      <KeysCell ex><PaperKeys start="E" whites={15} w={40} h={150} boxes={cf} labels={{ 1: 'F' }} ex={{ 1: true }}/></KeysCell>""", 'p2 C and F keys')
rep("""<PaperKeys start={kb.start} whites={10} w={30} h={110} dots={kb.dots}""", """<PaperKeys start={kb.start} whites={10} w={30} h={132} dots={kb.dots}""", 'p2 dotted keys')
rep("""      <KeyScene start="C" whites={14} w={40} h={110} houses={false} lost={['D', 'G', 'B', 'C', 'A']}/>""",
    """      <KeyScene start="C" whites={14} w={40} h={200} houses={false} lost={['D', 'G', 'B', 'C', 'A']}/>""", 'p2 lost letters')
rep("""      <div style={{display:'grid',gap:8}}>{W.s2.tog.map((r, i) => <LetterRow key={i} n={i + 1} ex={i === 0} cells={rowCells(r, i === 0)}/>)}</div>""",
    """      <div style={{display:'grid',gap:10}}>{W.s2.tog.map((r, i) => <LetterRow key={i} big n={i + 1} ex={i === 0} cells={rowCells(r, i === 0)}/>)}</div>""", 'p3 tog rows')
rep("""      <BkGrid cols={4} gap="10px 12px">{W.s3.tog.map((it, i) => <UpDownCell key={i} it={it} n={i + 1} ex={i === 0}/>)}</BkGrid>""",
    """      <BkGrid cols={4} gap="10px 12px">{W.s3.tog.map((it, i) => <UpDownCell key={i} big it={it} n={i + 1} ex={i === 0}/>)}</BkGrid>""", 'p4 tog cells')
rep("""      <PaperKeys start="C" whites={hk} w={42} h={110} stars={[hstart]}""", """      <PaperKeys start="C" whites={hk} w={42} h={178} stars={[hstart]}""", 'p4 hunt keys')
rep("""      <div style={{display:'grid',gap:8}}>{W.sk.tog.map((r, i) => <LetterRow key={i} n={i + 1} ex={i === 0} cells={rowCells(r, i === 0)}/>)}</div>""",
    """      <div style={{display:'grid',gap:10}}>{W.sk.tog.map((r, i) => <LetterRow key={i} big n={i + 1} ex={i === 0} cells={rowCells(r, i === 0)}/>)}</div>""", 'p6 tog rows')
# the practice log: things a child can do alone (the letter chain with a partner stays in the lesson)
rep("""'Letter chain with someone: forwards', 'Letter chain: backwards'""", """'Letter chain out loud: forwards', 'Letter chain out loud: backwards'""", 'p7 log')

# p4: 'in my head' on its own line, the seven day boxes in a row under it (it wrapped mid-row)
rep("""      <div style={{display:'flex',alignItems:'center',gap:8,marginTop:9,fontSize:12.5,color:BK.ink,flexWrap:'wrap'}}><b>In my head, no piano:</b><span>the letters backwards, from a different letter each day. Tick a day:</span>{BK_DAYS.map(d => <span key={d} style={{display:'inline-flex',alignItems:'center',gap:3,fontSize:10.5,color:BK.muted,fontWeight:700}}>{d}<span style={{width:18,height:18,border:'1.5px solid ' + BK.line,borderRadius:4}}/></span>)}</div>""",
    """      <div style={{marginTop:10,fontSize:13,color:BK.ink}}><b>In my head, no piano:</b> say the letters backwards, from a different letter each day. Tick a day:</div>
      <div style={{display:'flex',justifyContent:'space-between',marginTop:6,padding:'0 4px'}}>{BK_DAYS.map(d => <span key={d} style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:11.5,color:BK.muted,fontWeight:700}}>{d}<span style={{width:22,height:22,border:'1.5px solid ' + BK.line,borderRadius:5}}/></span>)}</div>""", 'p4 in my head')

# p4: the treasure hunt has 8 clues (two rows of four) -- the page's room goes to more of the game, not to blank
rep("""const hunt = withSeed(k('hunt'), () => { let pos = 3; const moves = []; while (moves.length < 6) {""",
    """const hunt = withSeed(k('hunt'), () => { let pos = 3; const moves = []; while (moves.length < 8) {""", 'hunt 8 clues')
rep("""      <div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',gap:8,marginTop:10}}>{W.hunt.moves.map((mv, i) =>""",
    """      <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:10,marginTop:12}}>{W.hunt.moves.map((mv, i) =>""", 'hunt grid')

rep("""function NnSpellCell({ w, n, ex, kw = 140 }) {""", """function NnSpellCell({ w, n, ex, kw = 140, kh = 46 }) {""", 'spell cell kh')
rep("""    <div style={{flex:1,maxWidth:kw}}><PaperKeys start="C" whites={7} w={18} h={46} dots={ex ? nnSpellDots(w) : []} dotR={0.2}/></div>""",
    """    <div style={{flex:1,maxWidth:kw}}><PaperKeys start="C" whites={7} w={18} h={kh} dots={ex ? nnSpellDots(w) : []} dotR={0.2}/></div>""", 'spell cell keys')

# the check-up on paper: on its own page now -- big keys, letter rows one to a line, big step cells
rep("""    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px',width:'62%'}}><PaperKeys start="G" whites={10} w={30} h={66} dots={W.chk.nm}""",
    """    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px',width:'72%'}}><PaperKeys start="G" whites={10} w={30} h={150} dots={W.chk.nm}""", 'chk A')
rep("""    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{W.chk.ab.map((r, i) => <LetterRow key={i} n={(5 + 2 * i) + '-' + (6 + 2 * i)} cells={rowCells(r, false)}/>)}</div>""",
    """    <div style={{display:'grid',gap:8}}>{W.chk.ab.map((r, i) => <LetterRow key={i} big n={(5 + 2 * i) + '-' + (6 + 2 * i)} cells={rowCells(r, false)}/>)}</div>""", 'chk B')
rep("""    <BkGrid cols={4} gap="6px 10px">{W.chk.ud.map((it, i) => <UpDownCell key={i} it={it} n={i + 9}/>)}</BkGrid>""",
    """    <BkGrid cols={4} gap="6px 10px">{W.chk.ud.map((it, i) => <UpDownCell key={i} big it={it} n={i + 9}/>)}</BkGrid>""", 'chk C')
rep("""    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{W.chk.ch.map((r, i) => <LetterRow key={i} n={(13 + 2 * i) + '-' + (14 + 2 * i)} cells={rowCells(r, false)}/>)}</div>""",
    """    <div style={{display:'grid',gap:8}}>{W.chk.ch.map((r, i) => <LetterRow key={i} big n={(13 + 2 * i) + '-' + (14 + 2 * i)} cells={rowCells(r, false)}/>)}</div>""", 'chk D')
rep("""    <BkGrid cols={2} gap="6px 10px">{NN_CHK_WORDS.map((w, i) => <NnSpellCell key={w} w={w} n={17 + i}/>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="6px 10px">{NN_CHK_WORDS.map((w, i) => <NnSpellCell key={w} w={w} n={17 + i} kw={290} kh={66}/>)}</BkGrid>""", 'chk E')

# the Teacher copy: the riddles' answers; the check-up's page title
rep("""{tcAns('PLAY', W.search.placed.map(p => p.w + ' ' + (p.hz ? 'across' : 'down') + ' from row ' + (p.r + 1) + ' col ' + (p.c + 1)))}</>}""",
    """{tcAns('PLAY', W.search.placed.map(p => p.w + ' ' + (p.hz ? 'across' : 'down') + ' from row ' + (p.r + 1) + ' col ' + (p.c + 1)))}{tcAns('BONUS', NN_RIDDLES.map(([, mix, a]) => mix + ' = ' + a))}</>}""", 'tc riddles')
rep('    <TcBlock page={8} title="My five checks · the check-up on paper"', '    <TcBlock page={8} title="The check-up on paper (the Workbook\'s last page)"', 'tc p8 title')

open(src, 'w', encoding='utf-8').write(s); print('patch413 ok')
