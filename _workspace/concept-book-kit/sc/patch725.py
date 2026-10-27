# Build BF (2026-10-27): counting her way (her 15:04). The bottom number names the note that is one beat:
# 8 on the bottom, the quaver is one beat and every note counts double (crotchet 2, dotted crotchet 3, dotted minim 6);
# 2 on the bottom, the minim is one beat and every note counts half. "Big beats" leave the student's words; the
# groups of three stay (1 and 4 strong), and the exam's names (compound duple and the like) stay only where a
# theory step names time signatures. The time-signatures chapter's own toy (BeatDoubler, "The bottom number changes
# the beat") already teaches this; it now also opens the 6/8 chapter (4 or 8) and the minim beat step (4 or 2).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

# ── the toy: which bottom numbers it offers, and where it starts ──
rep("function BeatDoubler() {\n  const [bot, setBot] = useState(8); // 2, 4 or 8 on the bottom",
    "function BeatDoubler({ bots = [2, 4, 8], start = 8 } = {}) {   // Build BF: the 6/8 chapter offers 4 or 8, the minim beat step 4 or 2\n  const [bot, setBot] = useState(start); // 2, 4 or 8 on the bottom")
rep("<div style={{display:'flex',gap:3,flexWrap:'wrap'}}>{[2, 4, 8].map(v => <button key={v} className={'chip' + (bot === v ? ' active' : '')}",
    "<div style={{display:'flex',gap:3,flexWrap:'wrap'}}>{bots.map(v => <button key={v} className={'chip' + (bot === v ? ' active' : '')}")
rep("<div style={actNote}>{t('Flip between them. With 8 every number doubles; with 2 every number is cut in half: the opposite direction.', '눌러서 바꿔 보세요. 8이면 모든 숫자가 두 배, 2이면 모든 숫자가 절반: 반대 방향이에요.')}</div>",
    "<div style={actNote}>{!bots.includes(2) ? t('Flip between them. With 8 on the bottom the quaver is one beat, so every number doubles.', '눌러서 바꿔 보세요. 아래가 8이면 8분음표가 1박이라 모든 숫자가 두 배.') : !bots.includes(8) ? t('Flip between them. With 2 on the bottom the minim is one beat, so every number is cut in half.', '눌러서 바꿔 보세요. 아래가 2면 2분음표가 1박이라 모든 숫자가 절반.') : t('Flip between them. With 8 every number doubles; with 2 every number is cut in half: the opposite direction.', '눌러서 바꿔 보세요. 8이면 모든 숫자가 두 배, 2이면 모든 숫자가 절반: 반대 방향이에요.')}</div>")
rep("""t('Only two BIG beats in a bar: 1 and 2. Each minim beat holds two crotchets: "1 &" and "2 &". Unlike 6/8, nothing is grouped in threes: every note is cut in half.', '한 마디에 큰 박은 딱 두 개: 1과 2. 2분음표 한 박에 4분음표가 두 개 들어가요: "1 &", "2 &". 6/8과 달리 3개씩 묶지 않아요: 모든 음표가 그냥 반으로 잘려요.')""",
    """t('Two beats in a bar: 1 and 2. The minim is one beat, so a crotchet is half a beat: "1 +", "2 +". Unlike 6/8, nothing is grouped in threes: every note is cut in half.', '한 마디에 2박: 1과 2. 2분음표가 1박이라서 4분음표는 반 박: "1 +", "2 +". 6/8과 달리 셋씩 묶지 않아요: 모든 음표가 그냥 반으로 줄어요.')""")

# ── common time and cut time (the time-signatures chapter) ──
rep("{cut ? t('2 big beats, each a minim', '큰 박 2개, 각각 2분음표') : t('4 beats, each a crotchet', '박 4개, 각각 4분음표')}",
    "{cut ? t('2 beats, each a minim', '2박, 각각 2분음표') : t('4 beats, each a crotchet', '4박, 각각 4분음표')}")
rep("""t('Same four crotchets of music in the bar as 4/4, but you feel only TWO beats ("1 + 2 +"), so the beat is the minim and the music moves along twice as fast as when you count four.', '한 마디 안의 음은 4/4와 같은 4분음표 네 개 길이지만, 박은 "두 개"만 느껴요 ("1 + 2 +"). 그래서 음악이 두 배 빨리 흘러가요. 한 박이 2분음표 하나예요.')""",
    """t('The bar holds the same four crotchets as 4/4, but the minim is one beat: every note counts half, so a crotchet is half a beat. Count only two: "1 + 2 +".', '한 마디는 4/4와 같은 4분음표 네 개 길이지만, 2분음표가 1박이에요: 모든 음표가 반으로 줄어서 4분음표는 반 박. 둘만 세요: "1 + 2 +".')""")
rep("t('blue line = the big beats (1, 2, 3, 4…)', '파란 선 = 큰 박 (1, 2, 3, 4…)')", "t('blue line = the beats (1, 2, 3, 4…)', '파란 선 = 박 (1, 2, 3, 4…)')")
rep('watch="Keeping the 4/4 values (crotchet = 1) when the bottom number is 8. Mixing up the six quaver COUNTS with the 2 big beats you FEEL."',
    'watch="Keeping the 4/4 values (crotchet = 1) when the bottom number is 8: in 6/8 the quaver is one beat, so every note counts double."')
rep('say="“With 8 on the bottom, count in quavers, so everything counts double. Six counts, two big beats.”"/>',
    'say="“8 on the bottom: the quaver is one beat, so everything counts double. Six beats, 1 and 4 strong.”"/>')
rep("means: 'six quavers in two groups of three.', play: 'count 1 2 3 4 5 6. Feel 2 big beats.' }",
    "means: 'the quaver is one beat: six beats, in two groups of three.', play: 'count 1 2 3 4 5 6, leaning on 1 and 4.' }")
rep("'six-eight': '6/8 six eight compound time dotted crotchet big beats quavers in threes 3/4 or 6/8 count clap',",
    "'six-eight': '6/8 six eight compound time quaver one beat everything doubles dotted crotchet three beats quavers in threes 3/4 or 6/8 count clap',")

# ── the 6/8 chapter: the pads ──
rep("t('Two big beats', '큰 박 둘')", "t('The quaver is one beat', '8분음표가 1박')", 3)
rep("LANG === 'ko' ? <>8분음표 여섯을 <b>1 2 3 4 5 6</b>으로 세요. 셋씩 묶여서 <b>1과 4가 센박</b>: 큰 박 둘이에요(하트). 먼저 듣고, 그다음 센박에서만 쳐요.</> : <>Count the six quavers <b>1 2 3 4 5 6</b>. They go in threes, so <b>1 and 4 are strong</b>: two big beats (the hearts). Listen first, then tap only the strong beats.</>",
    "LANG === 'ko' ? <>아래 숫자 8: <b>8분음표가 1박</b>. 위 숫자 6: 한 마디에 <b>6박</b>. <b>1 2 3 4 5 6</b>으로 세요. 셋씩 묶여서 <b>1과 4가 센박</b>(하트). 먼저 듣고, 그다음 센박에서만 쳐요.</> : <>The 8 on the bottom: <b>the quaver is one beat</b>. The 6 on top: <b>six beats</b> in a bar. Count <b>1 2 3 4 5 6</b>. They go in threes, so <b>1 and 4 are strong</b> (the hearts). Listen first, then tap only the strong beats.</>")
rep("<span style={{fontSize:15,fontWeight:900,color:BK.coral}}>{t(n + (n === 1 ? ' quaver' : ' quavers'), '8분음표 ' + n)}</span>",
    "<span style={{fontSize:15,fontWeight:900,color:BK.coral}}>{t(n + (n === 1 ? ' beat' : ' beats'), n + '박')}</span>")
rep("LANG === 'ko' ? <>점4분음표 하나가 <b>8분음표 셋</b>, 곧 <b>큰 박 하나</b>예요. 1 (2 3), 4 (5 6): 누르고 있는 동안 속으로 세어요.</> : <>One dotted crotchet lasts <b>three quavers</b>: <b>one big beat</b>. 1 (2 3), 4 (5 6): keep counting inside while you hold it.</>",
    "LANG === 'ko' ? <>6/8에서는 모든 음표가 두 배: 4분음표가 2박이니까 점4분음표는 <b>3박</b>(8분음표 셋)이에요. 1 (2 3), 4 (5 6): 누르고 있는 동안 속으로 세어요.</> : <>In 6/8 every note counts double: a crotchet is 2 beats, so a dotted crotchet is <b>3 beats</b> (three quavers). 1 (2 3), 4 (5 6): keep counting inside while you hold it.</>")
rep("LANG === 'ko' ? <>큰 박 하나를 <b>4분음표(8분음표 둘)와 8분음표 하나</b>로 나눠요: 길게, 짧게. 1 (2) 3, 4 (5) 6.</> : <>Split one big beat into <b>a crotchet (two quavers) and a quaver</b>: long, short. 1 (2) 3, 4 (5) 6.</>",
    "LANG === 'ko' ? <>셋 묶음 하나를 <b>4분음표(2박)와 8분음표(1박)</b>로 나눠요: 길게, 짧게. 1 (2) 3, 4 (5) 6.</> : <>Split a group of three into <b>a crotchet (2 beats) and a quaver (1 beat)</b>: long, short. 1 (2) 3, 4 (5) 6.</>")
rep("LANG === 'ko' ? <>둘 다 한 마디에 8분음표 여섯. <b>3/4</b>는 둘씩 묶어 <b>세 박</b>, <b>6/8</b>은 셋씩 묶어 <b>큰 박 둘</b>. 센 클릭이 어디 오는지 들어 봐요.</> : <>Both hold six quavers in a bar. <b>3/4</b> groups them in twos: <b>three beats</b>. <b>6/8</b> in threes: <b>two big beats</b>. Listen for where the strong clicks fall.</>",
    "LANG === 'ko' ? <>둘 다 한 마디에 8분음표 여섯. <b>3/4</b>는 4분음표가 1박이라 둘씩 묶어 <b>세 박</b>, <b>6/8</b>은 8분음표가 1박이라 <b>6박</b>을 셋씩 묶어요. 센 클릭이 어디 오는지 들어 봐요.</> : <>Both hold six quavers in a bar. <b>3/4</b>: the crotchet is the beat, so the quavers go in twos: <b>three beats</b>. <b>6/8</b>: the quaver is the beat, <b>six beats</b> in threes. Listen for where the strong clicks fall.</>")
rep("t('6/8: two big beats, 3 3', '6/8: 큰 박 둘, 3 3')", "t('6/8: six beats, 3 3', '6/8: 6박, 3 3')", 2)
rep("t('6/8: two big beats', '6/8: 큰 박 둘')", "t('6/8: six beats in threes', '6/8: 6박, 셋씩')", 2)
rep("t('I count 6/8 in six and feel two big beats, 1 and 4', '6/8을 여섯으로 세고 큰 박 둘(1과 4)을 느껴요')",
    "t('I count 6/8 with the quaver as one beat: six beats, 1 and 4 strong', '6/8을 8분음표 1박으로 세요: 6박, 1과 4가 센박')")
rep("t('I hold a dotted crotchet for one big beat', '점4분음표를 큰 박 하나만큼 눌러요')", "t('I hold a dotted crotchet for 3 beats', '점4분음표를 3박 동안 눌러요')")

# ── the 6/8 Lesson Book ──
rep("Count every quaver (1 2 3 4 5 6) while learning, and feel the two big beats (1 and 4) once it is easy: the clicks here are quavers, the strong click on 1 and 4.",
    "The 8 on the bottom makes the quaver one beat, so every note counts double: crotchet 2, dotted crotchet 3, dotted minim 6. Count 1 2 3 4 5 6, leaning on 1 and 4: the clicks here are quavers, the strong click on 1 and 4. The theory papers call 6/8 compound duple (two groups of three).")
rep("배울 때는 8분음표마다 세고(1 2 3 4 5 6), 익숙해지면 큰 박 둘(1과 4)을 느껴요: 여기 클릭은 8분음표마다, 센 클릭은 1과 4.",
    "아래 숫자 8이 8분음표를 1박으로 만들어서 모든 음표가 두 배예요: 4분음표 2박, 점4분음표 3박, 점2분음표 6박. 1 2 3 4 5 6으로 세고 1과 4에 힘을 줘요: 여기 클릭은 8분음표마다, 센 클릭은 1과 4. 이론 시험에서는 6/8을 겹두박자(셋씩 두 묶음)라고 불러요.")
rep("t('Six quavers in a bar, in two groups of three: two big beats. Count 1 2 3 4 5 6; 1 and 4 are strong.', '한 마디에 8분음표 여섯, 셋씩 두 묶음: 큰 박 둘. 1 2 3 4 5 6으로 세고, 1과 4가 세요.')",
    "t('8 on the bottom: the quaver is one beat, and every note counts double. Six beats in a bar, in two groups of three: count 1 2 3 4 5 6; 1 and 4 are strong.', '아래 숫자 8: 8분음표가 1박, 모든 음표가 두 배. 한 마디에 6박, 셋씩 두 묶음: 1 2 3 4 5 6으로 세고, 1과 4가 세요.')")
rep("t('count 6/8 and feel its two big beats', '6/8을 세고 큰 박 둘을 느낄 수 있어요'), t('hold a dotted crotchet for one big beat', '점4분음표를 큰 박 하나만큼 누를 수 있어요')",
    "t('count 6/8 with the quaver as one beat', '6/8을 8분음표 1박으로 셀 수 있어요'), t('hold a dotted crotchet for 3 beats', '점4분음표를 3박 동안 누를 수 있어요')")
rep("Clap all six quavers, then only 1 and 4; then walk the big beats round the room while you clap the quavers.",
    "Start from the bottom number: 8, so the quaver is one beat and every note doubles (the toy at the top). Clap all six quavers, then only 1 and 4; then the child walks on 1 and 4 round the room while you clap every quaver.")
rep("8분음표 여섯을 모두 손뼉 치고, 그다음 1과 4만 쳐요. 그다음 선생님이 8분음표를 치는 동안 아이는 큰 박에 맞춰 방을 걸어요.",
    "아래 숫자부터 봐요: 8이니까 8분음표가 1박이고 모든 음표가 두 배(맨 위의 교구). 8분음표 여섯을 모두 손뼉 치고, 그다음 1과 4만 쳐요. 그다음 선생님이 8분음표마다 치는 동안 아이는 1과 4에 맞춰 방을 걸어요.")
# step 1: the toy first (4 or 8 on the bottom), and on paper the same notes with their beats doubled
rep("      <LbLive still={still('big')} live={<E8BigPad/>}/>",
    "      <LbLive still={<LbPic h={230}><div style={{width:'100%',maxWidth:600,margin:'0 auto',display:'grid',gap:6}}>{e8ValRow()}{e8El('big')}</div></LbPic>} live={<><BeatDoubler bots={[4, 8]} start={8}/><div style={{height:12}}/><E8BigPad/></>}/>")
rep("// a note and the quavers it lasts: = and the quavers drawn as small beamed groups",
    "// Build BF: the five notes with their beats in 6/8 (the quaver is one beat, every note doubled), for the page\n"
    "const e8ValRow = () => <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:8,maxWidth:560,width:'100%',margin:'0 auto'}}>{DOUBLE_ROWS.map((f, i) => { const it = f(), v = it.beats * 2;\n"
    "  return <div key={i} style={{textAlign:'center'}}><div style={{display:'flex',justifyContent:'center'}}><Glyph item={it} size={54}/></div><div style={{fontSize:24,fontWeight:900,color:BK.coral,lineHeight:1.1}}>{fmtNum(v)}</div><div style={{fontSize:12,fontWeight:800,color:BK.muted}}>{v > 1 ? t('beats', '박') : t('beat', '박')}</div></div>; })}</div>;\n"
    "// a note and the quavers it lasts: = and the quavers drawn as small beamed groups")
rep("LANG === 'ko' ? <>6/8: 한 마디에 <b>8분음표 여섯</b>. 셋씩 묶어서 <b>1 2 3, 4 5 6</b>으로 세고, <b>1과 4가 센박</b>이에요. 그래서 6/8은 <b>큰 박 둘</b>로 느껴요.</> : <>6/8: <b>six quavers</b> in a bar. Count them in threes, <b>1 2 3, 4 5 6</b>, and <b>1 and 4 are strong</b>. So 6/8 feels like <b>two big beats</b>.</>",
    "LANG === 'ko' ? <>6/8: 아래 8은 <b>8분음표가 1박</b>, 위 6은 <b>한 마디에 6박</b>. 그래서 모든 음표가 <b>두 배</b>예요(4분음표 2박, 점4분음표 3박). 셋씩 묶어 <b>1 2 3, 4 5 6</b>으로 세고, <b>1과 4가 센박</b>.</> : <>6/8: the 8 means <b>the quaver is one beat</b>; the 6 means <b>six beats</b> in a bar. So every note counts <b>double</b> (crotchet 2, dotted crotchet 3). Count in threes, <b>1 2 3, 4 5 6</b>: <b>1 and 4 are strong</b>.</>")
rep("t('Six quavers, two big beats: 1 and 4.', '8분음표 여섯, 큰 박 둘: 1과 4.')", "t('8 on the bottom: the quaver is one beat. Everything doubles.', '아래 8: 8분음표가 1박. 모두 두 배.')")
rep("In 6/8 the dotted crotchet is the big beat (in 2/4, 3/4 and 4/4 it was a beat and a half).",
    "In 6/8 the dotted crotchet is 3 beats (in 2/4, 3/4 and 4/4 it was a beat and a half: everything doubles).")
rep("6/8에서는 점4분음표가 큰 박 하나예요(2/4, 3/4, 4/4에서는 한 박 반이었어요).", "6/8에서는 점4분음표가 3박이에요(2/4, 3/4, 4/4에서는 한 박 반: 모두 두 배).")
rep("점4분음표 하나 = <b>8분음표 셋</b> = <b>큰 박 하나</b>.", "점4분음표 하나 = <b>8분음표 셋</b> = <b>3박</b>.")
rep("One dotted crotchet = <b>three quavers</b> = <b>one big beat</b>.", "One dotted crotchet = <b>three quavers</b> = <b>3 beats</b>.")
rep("t('Dotted crotchet: three quavers, one big beat.', '점4분음표: 8분음표 셋, 큰 박 하나.')", "t('Dotted crotchet in 6/8: 3 beats.', '6/8의 점4분음표: 3박.')")
rep("A crotchet in 6/8 lasts two quavers, not one beat.", "A crotchet in 6/8 is 2 beats, not 1.")
rep("6/8에서 4분음표는 한 박이 아니라 8분음표 둘이에요.", "6/8에서 4분음표는 1박이 아니라 2박이에요.")
rep("큰 박 하나를 <b>4분음표 + 8분음표</b>로 나눠요: 길게, 짧게. 4분음표는 8분음표 둘.", "셋 묶음 하나를 <b>4분음표 + 8분음표</b>로 나눠요: 길게, 짧게. 4분음표 2박, 8분음표 1박.")
rep("Split a big beat into <b>a crotchet and a quaver</b>: long, short. The crotchet lasts two quavers.", "Split a group of three into <b>a crotchet and a quaver</b>: long, short. The crotchet is 2 beats, the quaver 1.")
rep("t('Crotchet + quaver = one big beat: long, short.', '4분음표 + 8분음표 = 큰 박 하나: 길게, 짧게.')", "t('Crotchet 2 + quaver 1 = 3: long, short.', '4분음표 2 + 8분음표 1 = 3: 길게, 짧게.')")
rep("3/4 beams them in twos (three crotchet beats), 6/8 in threes (two dotted-crotchet beats).", "3/4 beams them in twos (three crotchet beats), 6/8 in threes (six quaver beats, 1 and 4 strong; the theory papers call it compound duple).")
rep("6/8은 셋씩(점4분음표 두 박).", "6/8은 셋씩(8분음표 6박, 1과 4가 센박; 이론 시험에서는 겹두박자).")
rep("<b>6/8</b>은 <b>셋씩</b> 묶어서 큰 박 둘.", "<b>6/8</b>은 8분음표가 1박, <b>셋씩</b> 묶어서 6박.")
rep("<b>6/8</b> <b>in threes</b>: two big beats.", "<b>6/8</b>: the quaver is the beat, six beats <b>in threes</b>.")
rep("t('3/4: in twos, three beats. 6/8: in threes, two big beats.', '3/4: 둘씩, 세 박. 6/8: 셋씩, 큰 박 둘.')", "t('3/4: in twos, three beats. 6/8: in threes, six beats.', '3/4: 둘씩, 세 박. 6/8: 셋씩, 6박.')")
rep("A dotted minim fills the whole bar: 1 to 6.", "A dotted minim fills the whole bar: 6 beats, 1 to 6.")

# ── the 6/8 Workbook and teacher's copy ──
rep('<Part kind="together" title="Find the big beats" how="The counts are under the notes. Circle every note that falls on 1 or 4: the two big beats in each bar.">',
    '<Part kind="together" title="Find the strong beats" how="The counts are under the notes. Circle every note that falls on 1 or 4: the strong beats in each bar.">')
rep('<Part kind="home" title="Two big beats this week"', '<Part kind="home" title="Six beats this week"')
rep("'Walk the big beats while someone claps the quavers'", "'Walk on 1 and 4 while someone claps every quaver'")
rep('<Part kind="together" title="How many quavers?" how="In 6/8 we count quavers. Write how many quavers each note lasts.">',
    '<Part kind="together" title="How many beats?" how="In 6/8 the quaver is one beat, so every note counts double. Write how many beats each note lasts.">')
rep("{bkSec('A', 'In 6/8, how many quavers does each note last?')}", "{bkSec('A', 'In 6/8, how many beats does each note last?')}")
rep("in twos is 3/4 (three beats), in threes is 6/8 (two big beats). Write the time signature.", "in twos is 3/4 (three beats), in threes is 6/8 (six beats). Write the time signature.")
rep("In each box (one big beat) draw three quavers, a dotted crotchet, or a crotchet and a quaver.", "In each box (three beats) draw three quavers, a dotted crotchet, or a crotchet and a quaver.")
rep("Count every quaver while learning; feel the two big beats once it is easy.", "The quaver is one beat (8 on the bottom), so every note counts double; 1 and 4 are strong.")
rep('<TcBlock page={2} title="Two big beats"', '<TcBlock page={2} title="The quaver is one beat"')
rep('say="“Six quavers, two big beats: 1 and 4.”"/>', 'say="“8 on the bottom: the quaver is one beat. 1 and 4 are strong.”"/>')
rep('watch="Holding the dotted crotchet for one count only: in 6/8 it is a whole big beat (three quavers). In 2/4, 3/4 and 4/4 it was a beat and a half."',
    'watch="Holding the dotted crotchet for one count only: in 6/8 it is 3 beats (three quavers). In 2/4, 3/4 and 4/4 it was a beat and a half: everything doubles."')
rep('say="“Dotted crotchet: three quavers, one big beat.”"/>', 'say="“Dotted crotchet in 6/8: 3 beats.”"/>')
rep('watch="Giving the crotchet one count: in 6/8 it lasts two quavers (1, 3; 4, 6)."', 'watch="Giving the crotchet one beat: in 6/8 it is 2 beats (1, 3; 4, 6)."')
rep('say="“Crotchet and quaver make one big beat: long, short.”"/>', 'say="“Crotchet 2, quaver 1: long, short.”"/>')
rep('say="“3/4: in twos, three beats. 6/8: in threes, two big beats.”"/>', 'say="“3/4: in twos, three beats. 6/8: in threes, six beats.”"/>')

# ── the 6/8 drill and Home lessons ──
rep("{ n: 2, label: 'How many quavers?', kind: 'len', time: 8 },", "{ n: 2, label: 'How many beats?', kind: 'len', time: 8 },")
rep("'How many quavers?': '8분음표 몇 개?'", "'How many beats?': '몇 박?'")
rep("title = t('In 6/8, how many quavers does this note last?', '6/8에서 이 음표는 8분음표 몇 개만큼일까요?');", "title = t('In 6/8 the quaver is one beat. How many beats is this note?', '6/8에서는 8분음표가 1박. 이 음표는 몇 박일까요?');")
rep("t(q.answer === '3/4' ? '3/4: quavers in twos, three beats.' : '6/8: quavers in threes, two big beats.', q.answer === '3/4' ? '3/4: 8분음표 둘씩, 세 박.' : '6/8: 8분음표 셋씩, 큰 박 둘.')",
    "t(q.answer === '3/4' ? '3/4: quavers in twos, three beats.' : '6/8: the quaver is the beat, six beats in threes.', q.answer === '3/4' ? '3/4: 8분음표 둘씩, 세 박.' : '6/8: 8분음표가 1박, 6박을 셋씩.')")
rep("['Three: one big beat.', '셋: 큰 박 하나.']", "['Three beats.', '3박.']")
rep("e8HomeAdd('e8-big', 1, 'Two big beats', '큰 박 둘', 'Six quavers; 1 and 4 are strong.', '8분음표 여섯, 1과 4가 센박.', e8BigQ);",
    "e8HomeAdd('e8-big', 1, 'The quaver is one beat', '8분음표가 1박', 'Six beats; 1 and 4 are strong.', '6박, 1과 4가 센박.', e8BigQ);")
rep("e8HomeAdd('e8-dot', 2, 'The dotted crotchet', '점4분음표', 'Three quavers: one big beat.', '8분음표 셋: 큰 박 하나.', e8DotQ);",
    "e8HomeAdd('e8-dot', 2, 'The dotted crotchet', '점4분음표', 'Three quavers: 3 beats.', '8분음표 셋: 3박.', e8DotQ);")

# ── the time-signatures drill: compound time in groups of three ──
rep("{ n: 9, label: 'Compound time: big beats', kind: 'six8', time: 10 },", "{ n: 9, label: 'Compound time: groups of three', kind: 'six8', time: 10 },")
rep("'Compound time: big beats': '겹박자: 큰 박'", "'Compound time: groups of three': '겹박자: 셋씩 묶음'")
rep("six8: () => t('6/8, 9/8, 12/8: the quavers go in threes. Three quavers make one big beat.', '6/8, 9/8, 12/8: 8분음표가 셋씩 묶여요. 8분음표 셋이 큰 박 하나예요.'),",
    "six8: () => t('6/8, 9/8, 12/8: the quaver is one beat, and the beats go in threes. Three quavers make one group: a dotted crotchet.', '6/8, 9/8, 12/8: 8분음표가 1박이고, 박이 셋씩 묶여요. 8분음표 셋이 한 묶음: 점4분음표.'),")
rep("q.v === 'beats' ? t('How many big beats are in a bar of ' + q.sig + '?', q.sig + '에서 한 마디는 큰 박 몇 개일까요?') : t('Which note is one big beat in ' + q.sig + '?', q.sig + '에서 큰 박 하나는 어떤 음표일까요?')",
    "q.v === 'beats' ? t('How many groups of three are in a bar of ' + q.sig + '?', q.sig + '에서 한 마디는 셋 묶음이 몇 개일까요?') : t('Which note fills one group of three in ' + q.sig + '?', q.sig + '에서 셋 묶음 하나를 채우는 음표는?')")
rep("q.v === 'beats' ? t(q.answer + ' big beats', '큰 박 ' + q.answer + '개')", "q.v === 'beats' ? t(q.answer + ' groups of three', '셋 묶음 ' + q.answer + '개')")

# ── Rhythm Further: triplets and duplets, the minim beat, 3/8 and 9/8 ──
rep("t('Three in a beat, two in a dotted beat', '한 박에 셋, 점 박에 둘')", "t('Triplets and duplets', '셋잇단음표와 2잇단음표')", 3)
rep('<TcBlock page={4} title="Three in a beat, two in a dotted beat"', '<TcBlock page={4} title="Triplets and duplets"')
rep("r2HomeAdd('r2-trip', 3, 'Three in a beat, two in a dotted beat', '한 박에 셋, 점 박에 둘',", "r2HomeAdd('r2-trip', 3, 'Triplets and duplets', '셋잇단음표와 2잇단음표',")
rep("t('I fit three into a beat, and two into a dotted beat', '한 박에 셋, 점 박에 둘을 넣어요')", "t('I fit three where two go, and two where three go', '둘 자리에 셋, 셋 자리에 둘을 넣어요')")
rep("t('fit three into a beat and two into a dotted beat', '한 박에 셋, 점 박에 둘을 넣을 수 있어요')", "t('fit three where two go, and two where three go', '둘 자리에 셋, 셋 자리에 둘을 넣을 수 있어요')")
rep("['a duplet: how many notes in one dotted-crotchet beat?', 4]", "['a duplet: how many notes in the time of three quavers?', 4]")
rep("<>When the bottom number is <b>2</b>, the <b>minim</b> is the beat: <b>2/2</b> (also written as a C with a line), <b>3/2</b>.</>, <>아래 숫자가 <b>2</b>이면 <b>2분음표</b>가 한 박: <b>2/2</b>(세로선 C로도 써요), <b>3/2</b>.</>,",
    "<>When the bottom number is <b>2</b>, the <b>minim</b> is one beat, so every note counts <b>half</b>: a crotchet is half a beat. <b>2/2</b> (also written as a C with a line), <b>3/2</b>.</>, <>아래 숫자가 <b>2</b>이면 <b>2분음표</b>가 1박이라서 모든 음표가 <b>반</b>: 4분음표는 반 박. <b>2/2</b>(세로선 C로도 써요), <b>3/2</b>.</>,")
rep("t('Bottom number 2: the minim is the beat.', '아래 숫자 2: 2분음표가 한 박.'), <R2Pad step=\"minim\"",
    "t('Bottom number 2: the minim is one beat. Everything halves.', '아래 숫자 2: 2분음표가 1박. 모두 절반.'), <><BeatDoubler bots={[4, 2]} start={2}/><div style={{height:12}}/><R2Pad step=\"minim\"")
rep("ask={R2_Q.minim}/>, 4),", "ask={R2_Q.minim}/></>, 4),")
rep("<><b>3/8</b>: three quaver beats, simple triple. <b>9/8</b>: nine quavers in threes, three dotted-crotchet beats: <b>compound triple</b>.</>",
    "<><b>3/8</b>: three quaver beats, simple triple. <b>9/8</b>: nine quaver beats in three groups of three: <b>compound triple</b>.</>")
rep("<b>9/8</b>: 8분음표 아홉을 셋씩, 점4분음표 세 박: <b>겹세박자</b>.", "<b>9/8</b>: 8분음표 9박을 셋씩 세 묶음: <b>겹세박자</b>.")
rep("<>Clap line 2, feeling three big beats.</>", "<>Clap line 2, leaning on 1, 4 and 7.</>")
rep("<>2번 줄을 큰 박 셋으로 느끼며 쳐요.</>", "<>2번 줄을 1, 4, 7에 힘을 주며 쳐요.</>")
rep("t('9/8: three big beats of three.', '9/8: 셋씩 묶인 큰 박 셋.')", "t('9/8: nine beats, in threes.', '9/8: 9박, 셋씩.')")
rep('say="“9/8: three big beats of three.”"/>', 'say="“9/8: nine beats, in threes.”"/>')
rep("'Clap line 2, feeling three big beats'", "'Clap line 2, leaning on 1, 4 and 7'")
rep("yes: ['Compound triple: three dotted-crotchet beats, each of three quavers.', '겹세박자: 점4분음표 세 박, 한 박에 8분음표 셋.'], no: ['Nine quavers in threes: three dotted-crotchet beats, compound triple.', '8분음표 아홉을 셋씩: 점4분음표 세 박, 겹세박자.']",
    "yes: ['Compound triple: nine quaver beats in three groups of three.', '겹세박자: 8분음표 9박을 셋씩 세 묶음.'], no: ['Nine quaver beats in threes: three groups, compound triple.', '8분음표 9박을 셋씩: 세 묶음, 겹세박자.']")

# ── Rhythm, Grade 4: 6/4 and 12/8 ──
rep("note={t('6/4: two dotted-minim beats, each of three crotchets: compound duple. 12/8: four dotted-crotchet beats, each of three quavers: compound quadruple.', '6/4: 점2분음표 두 박, 한 박에 4분음표 셋: 겹두박자. 12/8: 점4분음표 네 박, 한 박에 8분음표 셋: 겹네박자.')}",
    "note={t('6/4: six crotchet beats in two groups of three: compound duple. 12/8: twelve quaver beats in four groups of three: compound quadruple.', '6/4: 4분음표 6박을 셋씩 두 묶음: 겹두박자. 12/8: 8분음표 12박을 셋씩 네 묶음: 겹네박자.')}")
rep("(12/8: four dotted-crotchet beats)", "(12/8: twelve quaver beats in four groups of three)")
rep("<><b>6/4</b>: 점2분음표 두 박(겹두박자). <b>12/8</b>: 점4분음표 네 박(<b>겹네박자</b>).</> : <><b>6/4</b>: two dotted-minim beats (compound duple). <b>12/8</b>: four dotted-crotchet beats (<b>compound quadruple</b>).</>",
    "<><b>6/4</b>: 4분음표 6박, 셋씩 두 묶음(겹두박자). <b>12/8</b>: 8분음표 12박, 셋씩 네 묶음(<b>겹네박자</b>).</> : <><b>6/4</b>: six crotchet beats, two groups of three (compound duple). <b>12/8</b>: twelve quaver beats, four groups of three (<b>compound quadruple</b>).</>")
rep("t('Clap 12/8: four big beats, each 1 + a… in threes.', '12/8: 큰 박 넷, 한 박에 셋씩.')", "t('Clap 12/8: count 1 to 12, accents on 1, 4, 7 and 10.', '12/8: 1부터 12까지, 1, 4, 7, 10에 강세.')")
rep('watch="Calling 6/4 simple triple (six crotchets in threes is two dotted-minim beats: compound duple)."', 'watch="Calling 6/4 simple triple (six crotchet beats in two groups of three: compound duple)."')
rep("6/4: two dotted-minim beats. 12/8: four dotted-crotchet beats. Then clap, leaning on each beat.", "6/4: six crotchet beats, in threes. 12/8: twelve quaver beats, in threes. Then clap, leaning on the first of each three.")
rep("'dotted-crotchet beats in a bar of 12/8'", "'groups of three in a bar of 12/8'")

# ── older tools: the beaming rule for 6/8 and the count-along's compound option ──
rep("t('Group quavers in threes: one group per dotted-crotchet beat. Never in pairs: that would look like 3/4.', '8분음표는 세 개씩: 점4분음표 한 박에 한 묶음. 두 개씩은 절대 안 돼요: 3/4처럼 보이거든요.')",
    "t('Group quavers in threes (one dotted crotchet each): 1 2 3, 4 5 6. Never in pairs: that would look like 3/4.', '8분음표는 세 개씩 묶어요(점4분음표 하나 길이): 1 2 3, 4 5 6. 두 개씩은 절대 안 돼요: 3/4처럼 보이거든요.')")
rep("compound: [[1, 'Dotted beats'], [3, 'Quavers'], [6, 'Semiquavers']],", "compound: [[1, 'Dotted crotchets'], [3, 'Quavers'], [6, 'Semiquavers']],")
rep("'Dotted beats': '점 박만' };", "'Dotted crotchets': '점4분음표만' };")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
