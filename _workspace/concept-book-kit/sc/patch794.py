#!/usr/bin/env python3
"""Build DQ, two of her 01:42 and 01:44 asks (on t793 -> t794). (1) Stacked noteheads on lines now touch like the ones in spaces:
SfStaff's hollow head (and its twins) grows from 0.9 of a space to one space tall (6.3x4.5 -> 6.9x4.95; the line still shows
through the hole). (2) The melodic minor is one mountain: up the left slope with the raised 6th and 7th in coral, down the right
slope as the natural minor, in the book's pictures, the pad and the drill (ScfMelHill replaces the two rows)."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
# (1) the hollow head fills its space
R('''rx="6.3" ry="4.5"''', '''rx="6.9" ry="4.95"''', 5)
# (2) the mountain
R('''function ScfMelRow({ m, dir, show = true }) {''', '''// Build DQ (her 01:44): one mountain, up the left slope and down the right; the raised notes coral going up, the natural ones outlined coming down
function ScfMelHill({ m, show = true, w = 494 }) {
  const c = SCF_MEL[m], seq = c.up.map((x, j) => [x, j, 'up', j === 5 || j === 6]).concat(c.dn.slice(1).map((x, j) => [x, 6 - j, 'dn', j === 0 || j === 1]));
  const st = (w - 40) / 14, dy = 13, r = 13, base = 7 * dy + 18, h = base + r + 26;
  const pt = (i) => [20 + i * st, base - seq[i][1] * dy];
  return <svg viewBox={'0 0 ' + w + ' ' + h} style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t(c.en, c.ko)} data-mel-hill={m}>
    <path d={seq.map((_, i) => (i ? 'L' : 'M') + pt(i).join(' ')).join(' ')} fill="none" stroke={BK.ink} strokeOpacity="0.35" strokeWidth="1.4"/>
    <text x={pt(2)[0]} y={base + r + 20} textAnchor="middle" fontSize="11.5" fontWeight="900" fill={BK.muted}>{t('up ↗', '올라갈 때 ↗')}</text>
    <text x={pt(12)[0]} y={base + r + 20} textAnchor="middle" fontSize="11.5" fontWeight="900" fill={BK.muted}>{t('down ↘', '내려올 때 ↘')}</text>
    {seq.map(([x, , dir, ch], i) => { const [cx, cy] = pt(i), hide = !show && dir === 'up' && ch; return <g key={i}>
      <circle cx={cx} cy={cy} r={r} fill={ch && !hide ? (dir === 'up' ? BK.coral : '#fff') : '#fff'} stroke={ch && !hide ? BK.coral : BK.ink} strokeWidth="1.5"/>
      <text x={cx} y={cy + 4.5} textAnchor="middle" fontSize="12.5" fontWeight="900" fill={ch && !hide && dir === 'up' ? '#fff' : BK.ink} fontFamily="Inter, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif">{hide ? '?' : x}</text></g>; })}
  </svg>;
}
function ScfMelRow({ m, dir, show = true }) {''')
for m in ['Gm', 'Cm', 'Cm']:
    pass
R('''<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:6,width:'100%',maxWidth:520,margin:'0 auto'}}><ScfMelRow m="Gm" dir="up"/><ScfMelRow m="Gm" dir="down"/></div></LbPic>''',
  '''<LbPic h={150}><ScfMelHill m="Gm"/></LbPic>''')
R('''<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:6,width:'100%',maxWidth:520,margin:'0 auto'}}><ScfMelRow m="Cm" dir="up"/><ScfMelRow m="Cm" dir="down"/></div></LbPic>''',
  '''<LbPic h={150}><ScfMelHill m="Cm"/></LbPic>''', 2)
R('''      <ScfMelRow m={m} dir="up" show={done}/>
      <ScfMelRow m={m} dir="down"/>''', '''      <ScfMelHill m={m} show={done}/>''')
R('''body = <>{done && <><ScfMelRow m={q.m} dir="up"/><ScfMelRow m={q.m} dir="down"/></>}''', '''body = <>{done && <ScfMelHill m={q.m}/>}''')
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))

# (3) her 01:46: the triplet is counted 1 + a (2 + a), not 1 trip let -- the words under the beat, the labels, the books' lines
s2 = s
R("""3: ['trip', 'let']""", """3: ['+', 'a']""")
R("""  if (Math.abs(f - 0.333) < 0.01) return 'trip';
  if (Math.abs(f - 0.667) < 0.01) return 'let';""", """  if (Math.abs(f - 0.333) < 0.01) return '+';
  if (Math.abs(f - 0.667) < 0.01) return 'a';""")
R("""  if (sub === 3) return Math.abs(f - TRI) < 0.01 ? 'trip' : 'let';""", """  if (sub === 3) return Math.abs(f - TRI) < 0.01 ? '+' : 'a';""")
R("""return Math.abs(f - 1 / 3) < 0.02 ? 'trip' : Math.abs(f - 2 / 3) < 0.02 ? 'let' : srhCount(p)""", """return Math.abs(f - 1 / 3) < 0.02 ? '+' : Math.abs(f - 2 / 3) < 0.02 ? 'a' : srhCount(p)""")
i = s.index("const rqTripCount = (pos) =>"); j = s.index('\n', i); line = s[i:j]
assert line.count("'trip'") == 1 and line.count("'let'") == 1
s = s[:i] + line.replace("'trip'", "'+'").replace("'let'", "'a'") + s[j:]
n1 = s.count('1-trip-let'); s = s.replace('1-trip-let', '1 + a')
n2 = s.count('1 trip-let'); s = s.replace('1 trip-let', '1 + a')
n3 = s.count('1 trip let'); s = s.replace('1 trip let', '1 + a')
n4 = s.count("b + ' trip-let'"); s = s.replace("b + ' trip-let'", "b + ' + a'")
assert (n1, n2, n3, n4) == (4, 3, 21, 1), (n1, n2, n3, n4)
assert "trip let" not in s and "trip-let" not in s
open(dst, 'w', encoding='utf-8').write(s)
print('ok triplet', len(s))

# (4) her 01:48: the twins picture shows the two hands going together, note by note: a strip of eight note columns under the keyboard,
# right-hand finger over left-hand finger, joined while they match, coral from the note where they part
R("""    {!bare && <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 4px 0'}}><span>{t('← left hand: down', '← 왼손: 아래로')}</span><span>{t('right hand: up →', '오른손: 위로 →')}</span></div>}</>;
}""", """    {!bare && <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 4px 0'}}><span>{t('← left hand: down', '← 왼손: 아래로')}</span><span>{t('right hand: up →', '오른손: 위로 →')}</span></div>}
    {!bare && <ScfTwinStrip k={k}/>}</>;
}
// Build DQ (her 01:48): note by note, do the hands go together? Right-hand finger over left-hand finger; a navy link while they match, coral from the note where they part
function ScfTwinStrip({ k }) {
  const c = scfCm(k), d = scfFirstDiff(k);
  return <div data-twin-strip={k} style={{display:'grid',gridTemplateColumns:'auto repeat(8, minmax(0, 1fr))',gap:'2px 4px',alignItems:'center',maxWidth:420,margin:'6px auto 0',fontSize:11.5,fontWeight:900}}>
    <span style={{color:BK.muted,fontSize:10,textAlign:'right',paddingRight:4}}>{t('note', '음')}</span>{c.R.map((_, j) => <span key={j} style={{textAlign:'center',color:BK.muted,fontSize:10}}>{j + 1}</span>)}
    <span style={{color:BK.muted,fontSize:10,textAlign:'right',paddingRight:4}}>{t('RH', '오른손')}</span>{c.R.map((f, j) => { const same = d < 0 || j < d; return <span key={j} style={{textAlign:'center',padding:'3px 0 0',borderRadius:'10px 10px 0 0',background:same ? 'rgba(38,41,107,0.08)' : '#fbe3da',color:same ? BK.ink : BK.coral}}>{c.fR[j]}</span>; })}
    <span style={{color:BK.muted,fontSize:10,textAlign:'right',paddingRight:4}}>{t('LH', '왼손')}</span>{c.L.map((f, j) => { const same = d < 0 || j < d; return <span key={j} style={{textAlign:'center',padding:'0 0 3px',borderRadius:'0 0 10px 10px',background:same ? 'rgba(38,41,107,0.08)' : '#fbe3da',color:same ? BK.ink : BK.coral}}>{c.fL[j]}</span>; })}
  </div>;
}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok twins', len(s))

# (5) her 01:49: the four-voice stems sit flush on their heads (the stem's outer edge on the head's outer edge, from the head's middle)
R("""      {stems && <line x1={up ? x + 6 : x - 6} x2={up ? x + 6 : x - 6} y1={y + (up ? -1 : 1)} y2={y + (up ? -32 : 32)} stroke={col} strokeWidth="1.6"/>}""",
  """      {stems && <line x1={up ? x + 4.8 : x - 4.8} x2={up ? x + 4.8 : x - 4.8} y1={y} y2={y + (up ? -32 : 32)} stroke={col} strokeWidth="1.6"/>}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok stems', len(s))

# (6) her 01:50: the degree names climb like the scale: a staircase from 1 to 8, the tonic and dominant in coral
R("""function H3DegPad({ fixed, onResult }) {""", """// Build DQ (her 01:50): the degrees as a staircase, in their order, the name under each step
function H3DegStairs({ w = 620, scr = false }) {
  const n = 8, sw = (w - 12) / n, rise = scr ? 11 : 14, base = 28 + rise * 7, h = base + 20 + (scr ? 26 : 30), fs = scr ? 9.5 : 11;
  return <svg viewBox={'0 0 ' + w + ' ' + h} style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('The degrees of the scale, in order', '음계 음의 이름, 차례대로')} data-h3-stairs>
    {[0, 1, 2, 3, 4, 5, 6, 7].map(j => { const x = 6 + j * sw, top = base - j * rise, cor = j === 0 || j === 4 || j === 7, nm = H3_DEGN[j % 7];
      return <g key={j}>
        <rect x={x} y={top} width={sw - 3} height={base + 20 - top} rx="4" fill={cor ? '#fbe3da' : '#fff'} stroke={cor ? BK.coral : BK.ink} strokeWidth="1.5"/>
        <text x={x + (sw - 3) / 2} y={top + 19} textAnchor="middle" fontSize="17" fontWeight="900" fill={cor ? BK.coral : BK.ink} fontFamily="Inter, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif">{j + 1}</text>
        <text x={x + (sw - 3) / 2} y={base + 20 + (scr ? 14 : 17)} textAnchor="middle" fontSize={fs} fontWeight="800" fill={cor ? BK.coral : BK.ink} fontFamily="Inter, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif">{t(nm[0], nm[1])}</text>
      </g>; })}
  </svg>;
}
function H3DegPad({ fixed, onResult }) {""")
R("""      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr 1fr' : 'repeat(4,minmax(0,1fr))',gap:8,width:'100%',maxWidth:620,margin:'0 auto'}}>{H3_DEGN.map((nm, j) => <div key={j} style={{border:'1.5px solid ' + (j === 0 || j === 4 ? BK.coral : BK.ink),borderRadius:10,padding:'6px 4px',textAlign:'center'}}><div style={{fontSize:20,fontWeight:900,color:j === 0 || j === 4 ? BK.coral : BK.ink}}>{j + 1}</div><div style={{fontSize:13,fontWeight:800,color:BK.ink}}>{t(nm[0], nm[1])}</div></div>)}</div></LbPic>} live={<H3DegPad/>}/>""",
  """      <LbLive still={<LbPic h={160}><H3DegStairs scr={scr}/></LbPic>} live={<H3DegPad/>}/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok stairs', len(s))

# (7) her 01:51: the four-voice chords sit in the middle of equal slots, not at the ends
R("""  const xOf = (i) => (n === 1 ? (x0 + width) / 2 + 6 : x0 + 30 + i * ((width - x0 - 54) / Math.max(1, n - 1)));""",
  """  const xOf = (i) => (n === 1 ? (x0 + width) / 2 + 6 : x0 + 8 + ((width - x0 - 14) / n) * (i + 0.5));   // Build DQ: in the middle of equal slots""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok slots', len(s))

# (8) her 01:48 'what is this?': a one-check page (Writing a Melody and the couplet and stanza rooms) no longer stretches its one row over
# an empty page: the row at its normal size, and under it 'Write it here', an empty staff on the room's own rhythm (and words)
R("""      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey={'pb_five_mlx_v1' + (g === 2 ? '' : g)} rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,""",
  """      <LbLive still={<LbStageRows big={checksRows.length > 2} rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey={'pb_five_mlx_v1' + (g === 2 ? '' : g)} rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
      {checksRows.length <= 2 && <LbOnly print><div data-write-here style={{display:'flex',flexDirection:'column',gap:10,marginTop:8}}>
        <div style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:19,fontWeight:700,color:BK.ink,borderBottom:'3px double ' + BK.ink,paddingBottom:4}}>{t('Write it here', '여기에 써요')}</div>
        <div style={{fontSize:12.5,color:BK.muted,fontWeight:700}}>{g === 3 ? t('A four-bar melody on this rhythm, in G major; then another in a key of your own.', '이 리듬에 G장조 4마디 선율; 그다음 내가 고른 조로 하나 더.') : g === 4 ? t('A melody for the couplet, in F major: line 1 asks, line 2 answers.', '두 줄 시에 F장조 선율: 첫 줄은 묻고, 둘째 줄은 대답해요.') : t('A melody for the stanza, in D major, home again in line 4.', '네 줄 시에 D장조 선율, 4줄에서 다시 집으로.')}</div>
        {(g === 3 ? [['G', 'r1', null, 1], ['G', 'r1', null, 1]] : g === 4 ? [['F', cR, cR.words, 1.25]] : [['D', sR, sR.words, 1.3]]).map(([k, R, words, sp], i) => <div key={i} style={{maxWidth:640,margin:'0 auto',width:'100%'}}><MwStaff k={k} rh={R} notes={Array(words ? words.length : mwModel(k, R).length).fill(null)} words={words} per={4} sp={sp} label={t('An empty staff to write on', '쓸 빈 오선')}/></div>)}
      </div></LbOnly>}
    </LbPage>,""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok write-here', len(s))

# (9) her 01:55: 12/8 comes earlier -- with 3/8 and 9/8 in Rhythm, Grade 3 (pieces meet it well before the theory paper names it at Grade 4)
R("""    pg(6, 5, t('3/8 and 9/8', '3/8과 9/8'), ['e38', 'e98'], <><b>3/8</b>: three quaver beats, simple triple. <b>9/8</b>: nine quaver beats in three groups of three: <b>compound triple</b>.</>, <><b>3/8</b>: 8분음표 세 박, 홑세박자. <b>9/8</b>: 8분음표 9박을 셋씩 세 묶음: <b>겹세박자</b>.</>,
      <>{t('Grade 3: 3/8 and 9/8, and compound triple time in general knowledge. Bottom number 8: quavers. Top 3: simple, each quaver a beat. Top 6 or 9: compound, the quavers in threes.', '3급: 3/8과 9/8, 일반 지식의 겹세박자. 아래 숫자 8: 8분음표. 위가 3: 홑박자, 8분음표마다 한 박. 위가 6이나 9: 겹박자, 8분음표를 셋씩.')}</>,""",
  """    pg(6, 5, t('3/8, 9/8 and 12/8', '3/8, 9/8, 12/8'), ['e38', 'e98', 'e128'], <><b>3/8</b>: three quaver beats, simple triple. <b>9/8</b>: nine quaver beats in three groups of three: <b>compound triple</b>. <b>12/8</b>: twelve, in four groups of three: <b>compound quadruple</b>.</>, <><b>3/8</b>: 8분음표 세 박, 홑세박자. <b>9/8</b>: 8분음표 9박을 셋씩 세 묶음: <b>겹세박자</b>. <b>12/8</b>: 12박을 셋씩 네 묶음: <b>겹네박자</b>.</>,
      <>{t('Grade 3: 3/8 and 9/8, and compound triple time in general knowledge. 12/8 is named in the Grade 4 paper, but pieces meet it earlier (her 01:55), so it sits here as the fourth of the family: 6, 9, 12 on top, the quavers in threes. Bottom number 8: quavers. Top 3: simple, each quaver a beat. Top 6, 9 or 12: compound.', '3급: 3/8과 9/8, 일반 지식의 겹세박자. 12/8은 4급 시험지에 나오지만 곡에서는 더 일찍 만나요(01:55 말씀), 그래서 여기에 가족의 넷째로: 위가 6, 9, 12, 8분음표를 셋씩. 아래 숫자 8: 8분음표. 위가 3: 홑박자, 8분음표마다 한 박. 위가 6, 9, 12: 겹박자.')}</>,""")
R("""      [<>Count 1 2 3 in 3/8, one quaver to each number.</>, <>9/8: count 1 to 9, leaning on 1, 4 and 7.</>, <>Clap line 2, leaning on 1, 4 and 7.</>], [<>3/8: 숫자마다 8분음표 하나, 1 2 3.</>, <>9/8: 1부터 9까지, 1, 4, 7에 힘을 줘요.</>, <>2번 줄을 1, 4, 7에 힘을 주며 쳐요.</>],
      t('9/8: nine beats, in threes.', '9/8: 9박, 셋씩.'), <R2Pad step="e98" keys={['e38', 'e98']} title={t('3/8 and 9/8', '3/8과 9/8')} note={t('Count every quaver. In 9/8 the strong ones are 1, 4 and 7.', '8분음표마다 세요. 9/8에서는 1, 4, 7이 세요.')} ask={R2_Q.e98}/>, 5),""",
  """      [<>Count 1 2 3 in 3/8, one quaver to each number.</>, <>9/8: count 1 to 9, leaning on 1, 4 and 7.</>, <>12/8: count 1 to 12, leaning on 1, 4, 7 and 10; clap line 3.</>], [<>3/8: 숫자마다 8분음표 하나, 1 2 3.</>, <>9/8: 1부터 9까지, 1, 4, 7에 힘을 줘요.</>, <>12/8: 1부터 12까지, 1, 4, 7, 10에 힘을 주고 3번 줄을 쳐요.</>],
      t('6, 9, 12 on top: threes.', '위가 6, 9, 12: 셋씩.'), <R2Pad step="e98" keys={['e38', 'e98', 'e128']} title={t('3/8, 9/8 and 12/8', '3/8, 9/8, 12/8')} note={t('Count every quaver. In 9/8 the strong ones are 1, 4 and 7; in 12/8, 1, 4, 7 and 10.', '8분음표마다 세요. 9/8에서는 1, 4, 7이, 12/8에서는 1, 4, 7, 10이 세요.')} ask={R2_Q.e98}/>, 5),""")
R("""    <TcBlock page={6} title="3/8 and 9/8" answers={<>{lines(['e38', 'e98'])}{tcAns('PLAY', ['S', 'C', 'C', 'S'], 3)}</>} watch="9/8 counted as three bars of 3/8 with equal weight. Lean on 1, 4 and 7." say="“9/8: nine beats, in threes.”"/>""",
  """    <TcBlock page={6} title="3/8, 9/8 and 12/8" answers={<>{lines(['e38', 'e98', 'e128'])}{tcAns('PLAY', ['S', 'C', 'C', 'S'], 3)}</>} watch="9/8 counted as three bars of 3/8 with equal weight. Lean on 1, 4 and 7 (in 12/8 on 1, 4, 7 and 10)." say="“6, 9, 12 on top: threes.”"/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok 12/8', len(s))
R("""Someone shows a bar in 3/8 or 9/8: say which, then count its quavers out loud, leaning on 1 (and on 4 and 7 in 9/8).""", """Someone shows a bar in 3/8, 9/8 or 12/8: say which, then count its quavers out loud, leaning on 1 (and on 4, 7 and 10 as the top number allows).""")
R("""3/8이나 9/8 마디를 보여 주면 어느 쪽인지 말하고 8분음표를 소리 내어 세요. 1에 힘을 주고(9/8은 4와 7에도).""", """3/8, 9/8, 12/8 마디를 보여 주면 어느 것인지 말하고 8분음표를 소리 내어 세요. 1에 힘을 주고(위 숫자만큼 4, 7, 10에도).""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok challenge', len(s))

# (10) her 02:09 (call 39): the scales rooms' pictures also show the scale on the staff. One helper reads a room's scale from its own
# data (SCF_CM / SCF / SCF_MEL: the key and whether it is a harmonic minor), builds the key signature and the notes with the dial's
# helpers, and draws the right hand on the treble staff going up and the left hand on the bass staff going the way it plays, with
# the finger numbers. Under every contrary-motion keyboard (Grades 2 to 7), the Grade 2 thumbs picture and the melodic-minor mountain.
R("""// Build DQ (her 01:48): note by note, do the hands go together?""", """// Build DQ (her 02:09, call 39): the same scale on the staff. en: 'G major' | 'E harmonic minor'; fR going up, fL in the left hand's own order (down for contrary motion)
const scfStaffKey = (en) => { const note = en.split(' ')[0].replace('♯', '#').replace('♭', 'b'), minor = /minor/.test(en); return { note, minor, sig: minor ? SFD_SIGKEY(note, 'minor') : note }; };
function ScfStaffPair({ en, fR, fL, lhDown = true, w = 330, label }) {
  const { note, minor, sig } = scfStaffKey(en), L = 'CDEFGAB', d0 = note[0] === 'B' ? 27 : 28 + L.indexOf(note[0]);
  const mk = (dd) => (minor ? sfdMinItems(note, 'harmonic', dd) : { items: sfdScaleItems(note, dd), coral: [] });
  const R0 = mk(d0), L0 = mk(sfdLD0(note));
  if (!R0 || !L0) return <div style={{textAlign:'center',fontSize:12,color:BK.muted,fontWeight:700,margin:'4px 0'}}>{t('This scale needs a double sharp, so the staff is left out here.', '이 스케일은 겹샵이 필요해서 오선은 여기 없어요.')}</div>;
  const rev = (it) => it.slice(0, -1).reverse().concat([it[it.length - 1]]);
  const Lit = lhDown ? rev(L0.items) : L0.items, Lcor = lhDown ? L0.coral.map(j => 7 - j) : L0.coral;
  const rows = [['treble', R0.items, R0.coral, fR, t('RH', '오른손')], ['bass', Lit, Lcor, fL, t('LH', '왼손')]];
  return <div data-scf-staff={en} style={{display:'grid',gap:2,width:'100%',maxWidth:w + 40,margin:'6px auto 0'}}>
    {rows.map(([cf, items, coral, fg, lb]) => <div key={cf} style={{display:'grid',gridTemplateColumns:'34px 1fr',alignItems:'center',gap:4}}><span style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'right'}}>{lb}</span>
      <SkgStaff items={items} k={sig} clef={cf} width={w} full o={{ boxS: 22, D: 26, hl: coral, signHl: coral, ksCol: '#2e8a6e', fingers: fg || undefined, ...skgUnder(items, sig, null, coral) }} label={label || en}/></div>)}
  </div>;
}
// Build DQ (her 01:48): note by note, do the hands go together?""")
R("""    {!bare && <ScfTwinStrip k={k}/>}</>;
}""", """    {!bare && <ScfTwinStrip k={k}/>}
    {!bare && <ScfStaffPair en={SCF_CM[k].en} fR={c.fR} fL={c.fL}/>}</>;
}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok staff', len(s))
# the pair side by side where there is room (print), one under the other on a phone; a single-hand line for the thumbs picture; the mountain on the staff
R("""  return <div data-scf-staff={en} style={{display:'grid',gap:2,width:'100%',maxWidth:w + 40,margin:'6px auto 0'}}>
    {rows.map(""", """  return <div data-scf-staff={en} style={{display:'grid',gridTemplateColumns:'repeat(auto-fit, minmax(250px, 1fr))',gap:'2px 10px',width:'100%',margin:'6px auto 0'}}>
    {rows.filter(r => r[3] !== false).map(""")
R("""    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{scfName(k)} · {spHand(h)}</div><SpKb lo={SCF[k].r} hi={SCF[k].r + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, scfNames(k, 1)[j]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };""",
  """    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{scfName(k)} · {spHand(h)}</div><SpKb lo={SCF[k].r} hi={SCF[k].r + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, scfNames(k, 1)[j]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/>
      <ScfStaffPair en={SCF[k].en} fR={h === 'R' ? F : false} fL={h === 'L' ? F : false} lhDown={false}/></div>; };   // Build DQ (call 39): the same scale on the staff""")
R("""function ScfMelHill({ m, show = true, w = 494 }) {""", """// Build DQ (call 39): the mountain on the staff: up the melodic minor, down the natural
function ScfMelStaff({ m, w = 520 }) {
  const c = SCF_MEL[m], note = c.en.split(' ')[0].replace('♯', '#').replace('♭', 'b'), sig = SFD_SIGKEY(note, 'minor'), d0 = note[0] === 'B' ? 27 : 28 + 'CDEFGAB'.indexOf(note[0]);
  const up = sfdMinItems(note, 'melodic', d0), nat = sfdMinItems(note, 'natural', d0); if (!up || !nat) return null;
  const dn = nat.items.slice(0, -1).reverse().slice(1), items = up.items.slice(0, -1).concat(dn, [['||']]), coral = up.coral.concat(nat.coral.map(j => 7 + (7 - j)));
  return <div data-scf-staff={c.en} style={{width:'100%',margin:'6px auto 0'}}><SkgStaff items={items} k={sig} clef="treble" width={w} full o={{ boxS: 20, D: 24, hl: coral, signHl: coral, ksCol: '#2e8a6e', ...skgUnder(items, sig, null, coral) }} label={c.en}/></div>;
}
function ScfMelHill({ m, show = true, w = 494 }) {""")
R("""<LbPic h={150}><ScfMelHill m="Gm"/></LbPic>""", """<LbPic h={150}><div style={{width:'100%'}}><ScfMelHill m="Gm"/><ScfMelStaff m="Gm"/></div></LbPic>""")
R("""<LbPic h={150}><ScfMelHill m="Cm"/></LbPic>""", """<LbPic h={150}><div style={{width:'100%'}}><ScfMelHill m="Cm"/><ScfMelStaff m="Cm"/></div></LbPic>""", 2)
open(dst, 'w', encoding='utf-8').write(s)
print('ok staff2', len(s))
# the strip and the staff only under a full-size keyboard (the small ones in the Workbook's grids stay bare); in the twins pictures the staff under the first scale only
R("""    {!bare && <ScfTwinStrip k={k}/>}
    {!bare && <ScfStaffPair en={SCF_CM[k].en} fR={c.fR} fL={c.fL}/>}</>;
}""", """    {!bare && W >= 18 && <ScfTwinStrip k={k}/>}
    {!bare && W >= 18 && staff && <ScfStaffPair en={SCF_CM[k].en} fR={c.fR} fL={c.fL}/>}</>;
}""")
R("""function ScfCmKb({ k, mark = -1, W = 22, H = 70, kk = 1.5, bare = false }) {""", """function ScfCmKb({ k, mark = -1, W = 22, H = 70, kk = 1.5, bare = false, staff = true }) {""")
R("""<ScfCmKb k="Bb" W={scr ? 20 : 30} H={scr ? 66 : 84} mark={scfFirstDiff(""", """<ScfCmKb k="Bb" W={scr ? 20 : 30} H={scr ? 66 : 84} staff={scr} mark={scfFirstDiff(""")
R("""<ScfCmKb k="Bb" W={scr ? 20 : 26} H={scr ? 56 : 70}/>""", """<ScfCmKb k="Bb" W={scr ? 20 : 26} H={scr ? 56 : 70} staff={scr}/>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok staff3', len(s))
# coming down, the notes the way up raised get their sign back (a natural or the flat), since the bar has no line to cancel them
R("""  const dn = nat.items.slice(0, -1).reverse().slice(1), items = up.items.slice(0, -1).concat(dn, [['||']]), coral = up.coral.concat(nat.coral.map(j => 7 + (7 - j)));""",
  """  const natN = spellMinor(note, 'natural'), dn = nat.items.slice(0, -1).reverse().slice(1).map((it, r) => { const j = 6 - r; return up.coral.includes(j) ? [it[0], it[1], it[2], natN[j].endsWith('b') ? 'b' : 'n'] : it; });
  const items = up.items.slice(0, -1).concat(dn, [['||']]), coral = up.coral.concat(up.coral.map(j => 8 + (6 - j)));""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok mel-staff', len(s))

# (11) her 02:11 'Call 38': the Scales map, one page on the Home's Quick line beside the Scale finder: floor by floor, that grade's keys as
# chips, the forms and the tempo, read from the rooms' own constants (SCF_CM, SCF, SCF_MEL, S4 to S8 lists; the Prelim and Grade 1
# keys as their rooms teach them); each floor is a door into its room
R("""function ToolView({ id, locked, onBack, onChapter, backLabel = '← Home', backAlways }) {""", """// Build DQ (call 38): the Scales map
const SMAP_NAME = (k, tbl) => { const c = tbl[k]; return c ? t(c.en, c.ko) : k; };
const smapRows = () => {
  const cm = (g) => Object.keys(SCF_CM).filter(k => SCF_CM[k].g === g).map(k => SMAP_NAME(k, SCF_CM));
  const sim = (g) => Object.keys(SCF).filter(k => SCF[k].g === g).map(k => SMAP_NAME(k, SCF));
  const N = { E: 'E major', Csm: 'C♯ harmonic minor', Csmel: 'C♯ melodic minor', Ab: 'A♭ major', Fm: 'F harmonic minor', B: 'B major', Gsm: 'G♯ harmonic minor', Gsmel: 'G♯ melodic minor', Db: 'D♭ major', Bbm: 'B♭ harmonic minor', Bbmel: 'B♭ melodic minor', Fs: 'F♯ major', Dsm: 'D♯ harmonic minor', Dsmel: 'D♯ melodic minor', Em: 'E minor', Abm: 'A♭ minor', Bm: 'B minor', Dbm: 'D♭ minor' };
  const KO = { 'major': '장조', 'harmonic minor': '화성 단음계', 'melodic minor': '가락 단음계', 'minor': '단조' };
  const nm = (id) => { const en = N[id] || id; return LANG === 'ko' ? en.replace(/ (harmonic minor|melodic minor|major|minor)$/, (m, w) => ' ' + KO[w]) : en; };
  const F = { sim: t('Similar motion', '같은 방향'), cm: t('Contrary motion', '반대 방향'), mel: t('Melodic minor', '가락 단음계'), chr: t('Chromatic', '반음계'), arp: t('Arpeggios', '아르페지오'), grand: t('Grand scale', '그랜드 스케일'), ls: t('Legato and staccato', '레가토와 스타카토'), poly: t('Three against two', '3 대 2'), apart: t('A third and a sixth apart', '3도·6도 간격') };
  return [
    { id: 'scales', floor: t('Prelim', 'Prelim'), rows: [[F.sim, ['C major', 'G major', 'F major'].map(nm), t('one octave, each hand', '한 옥타브, 한 손씩')], [F.sim, ['A minor', 'E minor'].map(nm), t('natural, then harmonic (Playing Scales)', '자연, 그다음 화성 (스케일 치기)')]] },
    { id: 'minor-scales', floor: t('Grade 1', 'Grade 1'), rows: [[t('Key signatures', '조표'), ['G major', 'F major', 'D major', 'B♭ major'].map(nm), t('Key Signatures', '조표 방')], [F.sim, [t('the harmonic minor: the 7th up a semitone', '화성 단음계: 7음을 반음 위로')], t('Minor Scales', '단음계 방')]] },
    { id: 'scales-23', floor: t('Grade 2', 'Grade 2'), rows: [[F.sim, sim(2), t('two octaves; black-key starts, where the thumbs meet', '두 옥타브; 검은건반 시작, 엄지가 만나는 곳')], [F.mel, [nm('G melodic minor')], ''], [F.cm, cm(2), '♩ = 66'], [F.chr, [t('from any note', '어느 음에서든')], '']] },
    { id: 'scales-3', floor: t('Grade 3', 'Grade 3'), rows: [[F.sim, sim(3), t('two octaves', '두 옥타브')], [F.mel, [nm('C melodic minor')], t('hands together', '양손 함께')], [F.cm, cm(3), '♩ = 80'], [F.chr, ['A', 'E♭'], '']] },
    { id: 'scales-4', floor: t('Grade 4', 'Grade 4'), rows: [[F.sim, S4_KEYS.map(nm), '♩ = 63 · ' + t('four notes a beat', '한 박에 네 음')], [F.cm, cm(4), '♩ = 52'], [F.chr, S4_CH.map(x => x[0]), '♩ = 63'], [F.arp, S4_AR_KEYS.map(nm), '♩ = 76']] },
    { id: 'scales-5', floor: t('Grade 5', 'Grade 5'), rows: [[F.sim, S5_KEYS.map(nm), '♩ = 84 · ' + t('one scale, four ways', '한 스케일, 네 가지로')], [F.cm, cm(5), '♩ = 60'], [F.chr, S5_CH.map(x => x[0]), '♩ = 84'], [F.arp, S5_AR_KEYS.map(nm), '♩ = 52 · ' + t('four notes a beat', '한 박에 네 음')]] },
    { id: 'scales-6', floor: t('Grade 6', 'Grade 6'), rows: [[F.sim, S6_KEYS.map(nm), '♩ = 92 · ' + t('three ways, four octaves', '세 가지로, 네 옥타브')], [F.grand, [t('abbreviated', '줄인 형태')], ''], [F.ls, S6_LS_KEYS.map(nm), ''], [F.cm, cm(6), '♩ = 72'], [F.poly, [t('as a scale', '스케일로')], ''], [F.arp, [t('Arpeggios, Grade 6 room', '아르페지오, Grade 6 방')], '']] },
    { id: 'scales-7', floor: t('Grade 7', 'Grade 7'), rows: [[F.grand, S7_GR_KEYS.map(k => SMAP_NAME(k, S6_GR)), '♩ = 80'], [F.poly, [t('as a scale', '스케일로')], ''], [F.cm, cm(7), '♩ = 80'], [F.chr, S7_CH.map(x => x[0]), '♩ = 104 · ' + t('hands together', '양손 함께')], [t('Two voices, the Lydian mode', '두 성부, 리디아 선법'), [], '']] },
    { id: 'scales-8', floor: t('Grade 8', 'Grade 8'), rows: [[F.grand, S8_GR_KEYS.map(k => SMAP_NAME(k, S6_GR)), '♩ = 92'], [F.poly, [t('two against three', '2 대 3')], ''], [F.apart, [], ''], [F.chr, [t('in sixes; in double minor thirds', '6도로; 겹단3도로')], '']] },
  ];
};
function ScalesMapView({ onChapter }) {
  const rows = smapRows();
  return <div data-scales-map style={{display:'flex',flexDirection:'column',gap:10}}>
    <div style={{fontSize:14,color:'#4a4d86',lineHeight:1.5}}>{t('Every scale in the house, floor by floor: the keys of each grade, the forms, and the speed. Tap a floor to go to its room.', '집 안의 모든 스케일을 층마다: 급마다 조, 형태, 빠르기. 층을 누르면 그 방으로 가요.')}</div>
    {rows.map(f => <div key={f.id} data-smap-floor={f.id} style={{border:'1.5px solid var(--navy-line)',borderRadius:12,padding:'8px 10px',background:'#fff'}}>
      <button type="button" onClick={() => onChapter && onChapter(f.id)} style={{display:'flex',alignItems:'center',gap:8,width:'100%',background:'none',border:'none',padding:'2px 0 6px',cursor:'pointer',textAlign:'left',fontFamily:'inherit'}}><span style={{fontFamily:LB_SERIF,fontSize:19,fontWeight:800,color:'var(--navy)'}}>{f.floor}</span><span style={{fontSize:12,fontWeight:800,color:'var(--muted)',marginLeft:'auto'}}>{t('go to the room →', '방으로 →')}</span></button>
      <div style={{display:'grid',gap:5}}>{f.rows.map(([form, keys, how], i) => <div key={i} style={{display:'grid',gridTemplateColumns:'96px 1fr',gap:6,alignItems:'baseline'}}>
        <span style={{fontSize:11.5,fontWeight:900,color:'var(--navy)',lineHeight:1.2}}>{form}</span>
        <span style={{display:'flex',flexWrap:'wrap',gap:4,alignItems:'baseline'}}>{keys.map((k, j) => <span key={j} className="chip" style={{minHeight:26,padding:'2px 8px',fontSize:12,fontWeight:800,cursor:'default'}}>{k}</span>)}{how && <span style={{fontSize:11.5,fontWeight:700,color:'var(--muted)'}}>{how}</span>}</span>
      </div>)}</div>
    </div>)}
  </div>;
}
function ToolView({ id, locked, onBack, onChapter, backLabel = '← Home', backAlways }) {""")
R("""  { id: 'scale-finder', ch: 'scales', title: 'Scale finder', blurb: 'Turn the circle of fifths to any major or minor key: the keyboard, both hands’ fingering, the key signature.', C: () => <ScaleFinderDial/> },""",
  """  { id: 'scale-finder', ch: 'scales', title: 'Scale finder', blurb: 'Turn the circle of fifths to any major or minor key: the keyboard, both hands’ fingering, the key signature.', C: () => <ScaleFinderDial/> },
  { id: 'scales-map', ch: 'scales', title: 'Scales map', blurb: 'Every scale in the house on one page: the keys of each grade, the forms and the speed.', C: (p) => <ScalesMapView onChapter={p && p.onChapter}/> },   // Build DQ (call 38)""")
R("""  'scale-finder': ['스케일 찾기', '5도권을 돌려서 어떤 장조·단조든 찾아요: 건반, 양손 손가락 번호, 조표.'],""", """  'scale-finder': ['스케일 찾기', '5도권을 돌려서 어떤 장조·단조든 찾아요: 건반, 양손 손가락 번호, 조표.'],
  'scales-map': ['스케일 지도', '집 안의 모든 스케일을 한 장에: 급마다 조, 형태, 빠르기.'],""")
R("""'scale-finder': ['scales', 0, 3, 'show game write ear home'],""", """'scale-finder': ['scales', 0, 3, 'show game write ear home'], 'scales-map': ['scales', 0, 3, 'show home'],""")
R("""  'scale-finder': () => (\n""", """  'scales-map': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[5, 9, 13, 17].map((y, i) => <rect key={y} x="4" y={y} width={16} height="2.4" rx="1.2" fill={i === 1 ? "#e9a83a" : "#fefbf3"}/>)}</svg>
  ),
  'scale-finder': () => (\n""")
R("""        {[['scale-finder', t('Scale finder', '스케일 찾기')], ['metronome', t('Metronome', '메트로놈')]].map(([id, l]) =>""", """        {[['scale-finder', t('Scale finder', '스케일 찾기')], ['scales-map', t('Scales map', '스케일 지도')], ['metronome', t('Metronome', '메트로놈')]].map(([id, l]) =>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok map', len(s))
# a tool may take the way to a chapter (the map's floors are doors)
R("""      <div className="card" data-home-lesson={t.ch === 'concept' ? '1' : undefined}>
        <div style={{fontSize:12,fontWeight:800,color:(TOOL_CATS.find(c => c.id === toolMeta(t.id).cat) || {}).color || 'var(--muted)',textTransform:'uppercase'""", """      <div className="card" data-home-lesson={t.ch === 'concept' ? '1' : undefined}>
        <div style={{fontSize:12,fontWeight:800,color:(TOOL_CATS.find(c => c.id === toolMeta(t.id).cat) || {}).color || 'var(--muted)',textTransform:'uppercase'""")
i = s.index("""      <div className="card" data-home-lesson={t.ch === 'concept' ? '1' : undefined}>""")
j = s.index("""        <t.C/>""", i)
s = s[:j] + """        <t.C onChapter={onChapter}/>""" + s[j + len("""        <t.C/>"""):]
R("""'scale-finder': 'p-scales'""", """'scale-finder': 'p-scales', 'scales-map': 'p-scales'""")
# (12) the staff pair under the contrary-motion keyboards is for the screen: in the lesson book two keyboards and a staff pair
# are taller than the page's picture frame (Grade 3 to 5 pages spilt past the frame); the thumb still and the mountain keep theirs
R("""  const c = scfCm(k), up = {}, dn = {}, lit = {}, nm = {};
  c.R.forEach((x, j) => { up[x] = c.fR[j]; lit[x] = 'pale'; nm[x] = c.nmR[j]; });""", """  const c = scfCm(k), up = {}, dn = {}, lit = {}, nm = {}, scr = lbScreen();
  c.R.forEach((x, j) => { up[x] = c.fR[j]; lit[x] = 'pale'; nm[x] = c.nmR[j]; });""")
R("""    {!bare && W >= 18 && staff && <ScfStaffPair en={SCF_CM[k].en} fR={c.fR} fL={c.fL}/>}</>;""", """    {!bare && W >= 18 && staff && scr && <ScfStaffPair en={SCF_CM[k].en} fR={c.fR} fL={c.fL}/>}</>;""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok map2', len(s))
