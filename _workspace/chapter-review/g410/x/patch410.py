#!/usr/bin/env python3
# Phase 410 (Sohyun 2026-10-10 00:23):
#   1. 'skewer', not 'kebab' -- the line IS the skewer through the note (and in Australia a kebab is a wrap)
#   2. activities say exactly what to do ('자유를 주는 것보다 뭘 하라고 지정해서'): the Queen's tunes come with
#      their letters; the plates say which lines and which spaces
#   python3 patch410.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. skewer
rep("""      <text x={44} y={10} fontSize="10" fontWeight="900" fill={BK.ink}>LINE note = a kebab</text>""",
    """      <text x={44} y={10} fontSize="10" fontWeight="900" fill={BK.ink}>LINE note = on a skewer</text>""", 'picture label')
rep("""// Line note = a kebab (the line goes through the middle). Space note = sandwich filling (between two lines).""",
    """// Line note = on a skewer (the line goes through the middle). Space note = sandwich filling (between two lines).""", 'picture comment')
rep("""Every note lives either <b>on a line</b> -- the line runs straight through its middle, like a kebab -- or""",
    """Every note lives either <b>on a line</b> -- the line runs straight through its middle, like a skewer -- or""", 'book p2 en')
rep("""how="Kebab = on a line, write L. Sandwich = in a space, write S. Count from the bottom.\"""",
    """how="Skewer = on a line, write L. Sandwich = in a space, write S. Count from the bottom.\"""", 'wb how', n=2)
rep("""how="A line note is a kebab: the line goes through the middle.""", """how="A line note is on a skewer: the line goes through the middle.""", 'old wb how')

# 2a. the plates say where: skewers on lines 1, 3 and 5; sandwiches in spaces 1, 2 and 4
rep("""    <Part kind="play" title="Kebab plate, sandwich plate" how="Cook! Draw three kebabs on the kebab plate -- notes ON a line -- and three sandwiches on the sandwich plate -- notes IN a space.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>
        {sfPlate('Kebab plate · line notes', <PaperStaff clefOn={false} notes={[]} width={170} minSpan={[29, 39]}/>)}
        {sfPlate('Sandwich plate · space notes', <PaperStaff clefOn={false} notes={[]} width={170} minSpan={[29, 39]}/>)}
      </div>
    </Part>""",
    """    <Part kind="play" title="Skewer plate, sandwich plate" how="Cook! Draw each note where its label says -- skewers ON the lines, sandwiches IN the spaces. Count from the bottom.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>
        {sfPlate('Skewer plate · line notes', <SfRow width={170} notes={[]} minSpan={[29, 39]} items={[[44, 'line 1'], [86, 'line 3'], [128, 'line 5']].map(([x, label]) => ({ x, label }))}/>)}
        {sfPlate('Sandwich plate · space notes', <SfRow width={170} notes={[]} minSpan={[29, 39]} items={[[44, 'space 1'], [86, 'space 2'], [128, 'space 4']].map(([x, label]) => ({ x, label }))}/>)}
      </div>
    </Part>""", 'plates')
rep("""{tcAns('PLATES', ['kebabs: three notes with a line through the middle', 'sandwiches: three notes filling a space'])}""",
    """{tcAns('PLATES', ['skewers on lines 1, 3, 5 (E, B, F)', 'sandwiches in spaces 1, 2, 4 (F, A, E)'])}""", 'tc plates')

# 2b. the Queen's tunes come with their letters: draw each note above its letter, then play
rep("""    <Part kind="play" title="Make a tune for the Queen" how="Draw any FOUR of her five notes -- C D E F G -- your own tune! Write the letters in the boxes, then play it to someone with your right hand.">
      <SfRow clef="treble" width={400} notes={[]} minSpan={[27, 34]} items={sfXs(4, 400, true).map((x, i) => ({ x, n: i + 1 }))}/>
      <div style={{fontSize:12.5,color:BK.muted,textAlign:'center',marginTop:8}}>The name of my tune: ______________________</div>
    </Part>""",
    """    <Part kind="play" title="Write the Queen's tunes" how="Draw each note above its letter -- on the line or in the space where it lives. Then play both tunes with your right hand.">
      {SF_QUEEN_TUNES.map((tu, k) => { const xs = sfXs(tu.notes.length, 400, true); return <div key={k} style={{marginTop:k ? 8 : 0}}>
        <div style={{fontSize:13.5,fontWeight:800,color:BK.ink,margin:'0 0 2px'}}>{tu.name}</div>
        <SfRow clef="treble" width={400} notes={[]} minSpan={[27, 34]} items={xs.map((x, i) => ({ x, ex: true, ans: dName(tu.notes[i]), w: 34 }))}/>
      </div>; })}
    </Part>""", 'queen tunes')
rep("""const SF_MOVE = { 1: 'step up', 2: 'skip up', '-1': 'step down', '-2': 'skip down' };""",
    """const SF_MOVE = { 1: 'step up', 2: 'skip up', '-1': 'step down', '-2': 'skip down' };
// the Queen's two tunes (Phase 410: set, not free) -- skips up and back, then down her five-step stairs
const SF_QUEEN_TUNES = [
  { name: '1 · Good morning, Queen!', notes: [28, 30, 32, 30] },
  { name: '2 · Down the palace stairs', notes: [32, 31, 30, 29, 28] },
];""", 'tunes data')
rep("""{tcAns('COMPOSE', ['any four of C D E F G -- check each drawn note against the letter under it; then they play it'])}""",
    """{tcAns('TUNES', SF_QUEEN_TUNES.map(tu => tu.notes.map(d => dName(d) + ' ' + (d === 28 ? '(ladder rung)' : d === 29 ? '(under line 1)' : (d - 30) % 2 === 0 ? '(line ' + ((d - 30) / 2 + 1) + ')' : '(space ' + ((d - 29) / 2) + ')')).join(', ')))}""", 'tc tunes')

# the SfRow example boxes are filled with the letter -- for the tunes they are the prompt, so show them navy
rep("""      : <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,width:it.w || boxW,height:boxH,border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:7,background:it.ex ? '#fdf3ef' : '#fff',display:'flex',alignItems:'center',justifyContent:'center',fontSize:it.w ? 13 : 16,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? it.ans : ''}</span>))}</div>}""",
    """      : <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,width:it.w || boxW,height:boxH,border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:7,background:it.ex ? '#fdf3ef' : '#fff',display:'flex',alignItems:'center',justifyContent:'center',fontSize:it.w && it.w > 40 ? 13 : 16,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? it.ans : ''}</span>))}</div>}""", 'box font')

open(src, 'w', encoding='utf-8').write(s); print('patch410 ok')
