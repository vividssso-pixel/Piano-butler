#!/usr/bin/env python3
"""Build DJ (on t784 -> t785): the split, part 4 (her 14:39, 2b: a room of its own). Scales Further keeps its id and the
Grade 2 floor as Scales, Grade 2: its five skills in the Grade 2 keys only (the Grade 3 lines leave its piano steps; the
teacher's notes keep both grades). A new room on the Grade 3 floor, Scales, Grade 3 (scales-3), three steps for what
Grade 3 adds: C melodic minor hands together; contrary motion in the Grade 3 keys (D and B flat major, B and G harmonic
minor); the chromatic scale from A and from E flat, hands together. Its drill is the base's melodic-minor, contrary-motion
and chromatic levels; its Workbook is the check-up only, with the parts whose keys are Grade 3's (B, C, D), until it
has pages of its own.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# ── Scales, Grade 2: the old room, its Grade 3 lines gone ──
R("""const SCALES_23_DRILL = { id: 'scales-23', label: 'Scales Further' };""", """const SCALES_23_DRILL = { id: 'scales-23', label: 'Scales, Grade 2' };   // Build DJ: was Scales Further; Grade 3 has scales-3
const SCALES_3_DRILL = { id: 'scales-3', label: 'Scales, Grade 3' };   // Build DJ""")
R("""  { id: 'scales-23', label: 'Scales Further', concept: SCALES_23_DRILL, track: 'start' },   // Build AK""",
  """  { id: 'scales-23', label: 'Scales, Grade 2', concept: SCALES_23_DRILL, track: 'start' },   // Build AK; Build DJ: Grade 2 only
  { id: 'scales-3', label: 'Scales, Grade 3', concept: SCALES_3_DRILL, track: 'start' },   // Build DJ""")
R("""'scales-23': '스케일 한 걸음 더'""", """'scales-23': '스케일, Grade 2', 'scales-3': '스케일, Grade 3'""")
R("""'scales-23': ['Scales further', '스케일 더']""", """'scales-23': ['Scales 2', '스케일 2'], 'scales-3': ['Scales 3', '스케일 3']""")
R("""'scales-23': ['scale-play', 'minor-scales']""", """'scales-23': ['scale-play', 'minor-scales'], 'scales-3': ['scales-23']""")
R("""'scales-23': 'k-play',""", """'scales-23': 'k-play', 'scales-3': 'k-play',""")
R("""  'scales-23': 'scales grade 2 grade 3 black key start""", """  'scales-3': 'scales grade 3 C melodic minor hands together contrary motion D B flat major B G harmonic minor chromatic from A E flat hands together two octaves 92',
  'scales-23': 'scales grade 2 black key start""")
R("""  { ids: ['listen-3', 'melody-3', 'harmony-3', 'rhythm-3'], en: ['Grade 3',""", """  { ids: ['listen-3', 'melody-3', 'scales-3', 'harmony-3', 'rhythm-3'], en: ['Grade 3',""")
R("""'scales-23': [1, 2, 3, 4, 5],""", """'scales-23': [1, 2, 3, 4, 5], 'scales-3': [3, 4, 5],""")
R("""{ id: 'kpl-23', en: 'Scales further', ko: '스케일 한 걸음 더',""", """{ id: 'kpl-23', en: 'Scales, Grades 2 and 3', ko: '스케일, Grade 2와 3',""")
R("""<div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales Further', '스케일 한 걸음 더')}</div>""",
  """<div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales, Grade 2', '스케일, Grade 2')}</div>""")
R("""<LbSay size={18}>{t('Scales for Grades 2 and 3: black-key starts, two hands that turn at different times, the melodic minor, contrary motion in new keys, and the chromatic scale from any note.', '2·3급 스케일: 검은건반에서 시작하기, 따로 넘어가는 두 손, 가락 단음계, 새 조의 반대 방향, 어느 음에서든 반음계.')}</LbSay>""",
  """<LbSay size={18}>{t('Scales for Grade 2: black-key starts, two hands that turn at different times, the melodic minor, contrary motion in new keys, and the chromatic scale from any note.', '2급 스케일: 검은건반에서 시작하기, 따로 넘어가는 두 손, 가락 단음계, 새 조의 반대 방향, 어느 음에서든 반음계.')}</LbSay>""")
R("""<>티-티를 고르게: 메트로놈 60, 그다음 84(2급), 92(3급).</>]""", """<>티-티를 고르게: 메트로놈 60, 그다음 84.</>]""")
R("""<>Even run-ning: metronome 60, then 84 (Grade 2), 92 (Grade 3).</>]""", """<>Even run-ning: metronome 60, then 84.</>]""")
R("""<>두 옥타브, 한 손씩. 3급은 C 가락 단음계를 양손 함께.</>]""", """<>두 옥타브, 한 손씩.</>]""")
R("""<>Two octaves, each hand. Grade 3: C melodic minor hands together.</>]""", """<>Two octaves, each hand.</>]""")
R("""<>메트로놈 66(2급), 80(3급). 한 박에 두 음.</>]""", """<>메트로놈 66. 한 박에 두 음.</>]""")
R("""<>Metronome 66 (Grade 2), 80 (Grade 3). Two notes a beat.</>]""", """<>Metronome 66. Two notes a beat.</>]""")
R("""<>두 옥타브. 3급은 A와 E♭에서, 양손 함께: 3번이 같이 떨어져요.</>]""", """<>두 옥타브, 한 손씩.</>]""")
R("""<>Two octaves. Grade 3: from A and E♭, hands together: the 3s land together.</>]""", """<>Two octaves, each hand.</>]""")
R("""function ScfLearn({ onStart }) {
  const pages = scfLbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-23" title={t('Scales Further', '스케일 한 걸음 더')} onStart={onStart} noArt""",
  """function ScfLearn({ onStart }) {
  const pages = scfLbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-23" title={t('Scales, Grade 2', '스케일, Grade 2')} onStart={onStart} noArt""")

# ── Scales, Grade 3: its own book (three steps), on the base's pictures and pads ──
R("""function Scales23LessonBook() { return <>{scfLbPages(false)}</>; }""", """function Scales23LessonBook() { return <>{scfLbPages(false)}</>; }
// Build DJ: Scales, Grade 3 (her 14:39: a room of its own, so the grades never mix)
function s3LbPages(scr = false) {
  const ch = 'scales-3', s2 = bkChapterNo('scales-23');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const kbW = scr ? 30 : 40, kbH = scr ? 80 : 104;
  const chromStill = (s0, names, cor) => { const K = Array.from({ length: 13 }, (_, j) => s0 + j), up = {}, dn = {}, lit = {}; K.forEach((x, j) => { up[x] = scfChF(x, 'R', j === 0 || j === 12); dn[x] = scfChF(x, 'L', j === 0 || j === 12); if (spIsW(x)) lit[x] = 'pale'; });
    cor.forEach(x => { lit[x] = 'cor'; }); return <SpKb lo={s0} hi={s0 + 12} W={kbW} H={kbH} lit={lit} names={names} up={up} dn={dn}/>; };
  const checks3 = [[scfPicMel(), t('I play C melodic minor hands together, two octaves', 'C 가락 단음계를 양손 함께 두 옥타브로 쳐요')], [scfPicMirror(), t('I play contrary motion in D and B♭ major, B and G harmonic minor', 'D·B♭장조와 B·G 화성 단음계를 반대 방향으로 쳐요')], [scfPicChrom(), t('I play the chromatic scale from A and from E♭, hands together', 'A와 E♭에서 반음계를 양손 함께 쳐요')]];
  const toc = [[t('C melodic minor, hands together', 'C 가락 단음계, 양손 함께'), 2], [t('Contrary motion, the Grade 3 keys', '반대 방향, 3급의 조'), 3], [t('Chromatic from A and E♭', 'A와 E♭에서 반음계'), 4], [t('My three checks', '나의 세 가지 확인'), 5]];
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 3 technical work that goes past chapter ' + s2 + ': C melodic minor hands separately and together, two octaves, two notes a beat at ♩ = 92; contrary motion over two octaves in D and B♭ major and B and G harmonic minor at ♩ = 80; the chromatic scale from A and from D♯/E♭ (written with sharps going up, flats coming down) at 92, hands separately and together. The A and E♭ major and F♯ and C minor scales use chapter ' + s2 + '\\'s rules (a black-key start on finger 2; the thumbs meet, or never). mf, legato, from memory.', '3급 테크닉 중 ' + s2 + '장을 넘어가는 것: C 가락 단음계를 한 손씩, 그리고 양손 함께 두 옥타브, 한 박에 두 음, ♩ = 92; D·B♭장조와 B·G 화성 단음계의 반대 방향 두 옥타브, ♩ = 80; A와 D♯/E♭에서 반음계(올라갈 때 샵, 내려올 때 플랫으로 적어요), 92, 한 손씩과 양손 함께. A·E♭장조와 F♯·C단조 스케일은 ' + s2 + '장의 규칙대로(검은건반 시작은 2번, 엄지는 만나거나 안 만나거나). mf, 레가토, 외워서.'))}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales, Grade 3', '스케일, Grade 3')}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:6,width:'100%',maxWidth:520,margin:'0 auto'}}><ScfMelRow m="Cm" dir="up"/><ScfMelRow m="Cm" dir="down"/></div></LbPic>
      <LbSay size={18}>{t('Scales for Grade 3: the melodic minor with both hands, mirror twins in new keys, and the chromatic scale from two new notes, hands together.', '3급 스케일: 양손으로 가락 단음계, 새 조의 거울 쌍둥이, 그리고 새 두 음에서 양손 함께 반음계.')}</LbSay>
      <LbGuess q={t('C melodic minor going up: which two notes rise?', 'C 가락 단음계 올라갈 때: 어느 두 음이 올라갈까요?')} a={t('The 6th and the 7th: A and B. Coming down, A♭ and B♭.', '6도와 7도: A와 B. 내려올 때는 A♭과 B♭.')} page={2}/>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h lb-can-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('After this chapter, I can', '이 챕터를 마치면')}</div>
          {[t('play C melodic minor hands together', 'C 가락 단음계를 양손 함께 칠 수 있어요'), t('play contrary motion in D and B♭ major, B and G harmonic minor', 'D·B♭장조와 B·G 화성 단음계를 반대 방향으로 칠 수 있어요'), t('play the chromatic scale from A and from E♭, hands together', 'A와 E♭에서 반음계를 양손 함께 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('C melodic minor, hands together', 'C 가락 단음계, 양손 함께')}
      teacher={<>{t('C melodic minor: up C D E♭ F G A B C, down C B♭ A♭ G F E♭ D C. The fingering is C major\\'s in both hands, so the thumbs meet on every C. Hands separately first, then together, two octaves, ♩ = 92 two notes a beat.', 'C 가락 단음계: 올라갈 때 C D E♭ F G A B C, 내려올 때 C B♭ A♭ G F E♭ D C. 손가락은 양손 모두 C장조와 같아서 엄지가 C마다 만나요. 한 손씩 먼저, 그다음 양손 함께 두 옥타브, ♩ = 92에 한 박에 두 음.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:6,width:'100%',maxWidth:520,margin:'0 auto'}}><ScfMelRow m="Cm" dir="up"/><ScfMelRow m="Cm" dir="down"/></div></LbPic>} live={<ScfMelPad/>}/>
      <LbSay>{LANG === 'ko' ? <>C 가락 단음계: 올라갈 때 <b>A와 B</b>(6도와 7도를 올려서), 내려올 때 <b>B♭과 A♭</b>(자연 단음계). 손가락은 <b>C장조와 같아요</b>: 두 엄지가 C마다 만나요. 그래서 양손 함께가 쉬워요.</> : <>C melodic minor: going up <b>A and B</b> (the 6th and 7th raised), coming down <b>B♭ and A♭</b> (the natural minor). The fingers are <b>C major\\'s</b>: both thumbs meet on every C. That is what makes hands together easy.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>오른손 두 옥타브, 올라갔다 내려와요. 올라갈 때 A, B. 내려올 때 B♭, A♭.</>, <>왼손도. 엄지가 C마다 닿는지 봐요.</>, <>양손 함께, 아주 천천히. 엄지가 함께 C에 닿아요. 메트로놈 60, 그다음 92.</>]
        : [<>Right hand, two octaves, up and back: A and B going up, B♭ and A♭ coming down.</>, <>Left hand too. Check that the thumb lands on every C.</>, <>Hands together, very slowly: both thumbs land on C together. Metronome 60, then 92.</>]}/>
      <LbChallenge>{t('C melodic minor hands together, two octaves, while someone listens for the two notes that change: up and down with no slip.', 'C 가락 단음계 양손 함께 두 옥타브, 누가 바뀌는 두 음을 들어요: 올라갔다 내려오기, 틀리지 않고.')}</LbChallenge>
      <LbRemember>{t('Up: A and B. Down: B♭ and A♭. The thumbs meet on C.', '올라갈 때 A와 B. 내려올 때 B♭과 A♭. 엄지는 C에서 만나요.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Contrary motion, the Grade 3 keys', '반대 방향, 3급의 조')}
      teacher={<>{spTx(t('Contrary motion over two octaves, ♩ = 80 two notes a beat: D major and G harmonic minor are mirror twins (1 2 3 1 2 3 4 both ways); B harmonic minor is not (RH 1 2 3 1 2 3 4, LH 1 2 3 4 1 2 3: they part at the fourth note); B♭ major is not (RH 2 1 2 3 1 2 3 4, LH 2 1 2 3 4 1 2 3: they part at the fifth note). Both hands start on one note, as the book prints them.', '반대 방향 두 옥타브, ♩ = 80에 한 박에 두 음: D장조와 G 화성 단음계는 거울 쌍둥이(양쪽 1 2 3 1 2 3 4); B 화성 단음계는 아니에요(오른손 1 2 3 1 2 3 4, 왼손 1 2 3 4 1 2 3: 넷째 음에서 갈라져요); B♭장조도 아니에요(오른손 2 1 2 3 1 2 3 4, 왼손 2 1 2 3 4 1 2 3: 다섯째 음에서 갈라져요). 두 손이 한 음에서 시작해요, 책대로.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:16,width:'100%',maxWidth:scr ? 440 : 560,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('Bmh')} · {t('not twins: they part at the fourth note', '쌍둥이가 아니에요: 넷째 음에서 갈라져요')}</div><ScfCmKb k="Bmh" W={scr ? 20 : 26} H={scr ? 56 : 70}/></div><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('Bb')} · {t('not twins: they part at the fifth note', '쌍둥이가 아니에요: 다섯째 음에서 갈라져요')}</div><ScfCmKb k="Bb" W={scr ? 20 : 26} H={scr ? 56 : 70}/></div></div></LbPic>} live={<ScfMirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>3급의 반대 방향 네 가지: <b>D장조와 G 화성 단음계</b>는 거울 쌍둥이. <b>B 화성 단음계</b>는 왼손 4가 일찍 와요(넷째 음에서 갈라져요). <b>B♭장조</b>는 다섯째 음에서 갈라져요. 갈라지는 곳만 알면 나머지는 쌍둥이처럼 쳐요.</> : <>Four contrary-motion scales at Grade 3: <b>D major and G harmonic minor</b> are mirror twins. In <b>B harmonic minor</b> the left hand's 4 comes early (they part at the fourth note). <b>B♭ major</b> parts at the fifth note. Know where they part, and the rest plays like twins.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D장조, 두 손을 D에. 번호를 소리 내어: 1 2 3 1 2 3 4, 양손 같이. G 화성 단음계도.</>, <>B 화성 단음계: 오른손 1 2 3 1, 왼손 1 2 3 4. 넷째 음에서 멈춰 번호를 확인해요.</>, <>B♭장조: 오른손 2 1 2 3 1, 왼손 2 1 2 3 4. 다섯째 음에서 멈춰요. 메트로놈 60, 그다음 80, 한 박에 두 음.</>]
        : [<>D major, both hands on D. Say the numbers: 1 2 3 1 2 3 4, both hands the same. G harmonic minor too.</>, <>B harmonic minor: right hand 1 2 3 1, left hand 1 2 3 4. Stop at the fourth note and check the numbers.</>, <>B♭ major: right hand 2 1 2 3 1, left hand 2 1 2 3 4. Stop at the fifth note. Metronome 60, then 80, two notes a beat.</>]}/>
      <LbChallenge>{t('Someone names one of the four: say "twins!" or "not twins!" before they count to 3, then play it in contrary motion, two octaves.', '누가 넷 중 하나를 말하면 셋 세기 전에 "쌍둥이!" 또는 "아니!", 그다음 반대 방향 두 옥타브.')}</LbChallenge>
      <LbRemember>{t('D and G minor: twins. B minor parts at the fourth note, B♭ at the fifth.', 'D와 G단조: 쌍둥이. B단조는 넷째 음, B♭은 다섯째 음에서 갈라져요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Chromatic from A and E♭', 'A와 E♭에서 반음계')}
      teacher={<>{spTx(t('The chromatic scale from A and from D♯/E♭, two octaves, ♩ = 92 two notes a beat, hands separately and together. The same rule as chapter ' + s2 + ': 3 on every black key, 1 on white keys, 2 where two white keys sit together (RH on F and C, LH on E and B). Hands together an octave apart the 3s land on the same black keys, so the hands feel each other.', 'A와 D♯/E♭에서 반음계, 두 옥타브, ♩ = 92에 한 박에 두 음, 한 손씩과 양손 함께. ' + s2 + '장과 같은 규칙: 검은건반마다 3, 흰건반 1, 흰건반 둘이 붙은 곳 2(오른손 F와 C, 왼손 E와 B). 양손 함께 한 옥타브 떨어져 치면 3번이 같은 검은건반에 떨어져서 두 손이 서로를 느껴요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={160}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:600,margin:'0 auto'}}>{chromStill(-3, { '-3': 'A', 0: 'C', 5: 'F', 9: 'A', '-1': 'B', 4: 'E' }, [0, 5])}{chromStill(3, { 3: 'E♭', 5: 'F', 12: 'C', 15: 'E♭', 4: 'E', 11: 'B' }, [5, 12])}</div></LbPic>} live={<ScfChromPad/>}/>
      <LbSay>{LANG === 'ko' ? <>같은 규칙, 새 출발점: <b>검은건반 3, 흰건반 1, 흰건반 둘이 붙은 곳 2</b>. A에서는 첫 음이 흰건반이라 1로 시작해요. E♭에서는 검은건반이라 <b>3으로 시작</b>해요. 양손 함께: 두 3번이 <b>같은 검은건반</b>에 떨어져요.</> : <>The same rule, two new starts: <b>3 on black, 1 on white, 2 where two whites sit together</b>. From A the first key is white, so start on 1. From E♭ it is black, so <b>start on 3</b>. Hands together, both 3s land on <b>the same black key</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>A에서 오른손 한 옥타브, 그다음 왼손. 3번이 검은건반만 치는지 봐요.</>, <>E♭에서: 3으로 시작해요. 한 손씩.</>, <>양손 함께, 한 옥타브 떨어져서, 아주 천천히: 3번이 같이 떨어져요. 메트로놈 60, 그다음 92.</>]
        : [<>From A, right hand, one octave, then the left. Check that 3 only ever plays a black key.</>, <>From E♭: start on 3. Each hand.</>, <>Hands together, an octave apart, very slowly: the 3s land together. Metronome 60, then 92.</>]}/>
      <LbChallenge kind="time" tid="beat22">{t('The chromatic scale from E♭, hands together, one octave up and down: how fast with both 3s landing together every time?', 'E♭에서 반음계 양손 함께 한 옥타브 올라갔다 내려오기: 두 3번이 매번 같이 떨어지면서 얼마나 빨리?')}</LbChallenge>
      <LbRemember>{t('From a black key, start on 3. Hands together, the 3s land together.', '검은건반에서는 3으로 시작. 양손 함께면 3번이 같이 떨어져요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Check-up', '점검')} title={t('My three checks', '나의 세 가지 확인')}
      teacher={<>{t('Each one played to you from memory at the Grade 3 speeds: ♩ = 92 (hands together), 80 (contrary motion), 92 (chromatic). Listen for the turns and for the thumbs landing together.', '하나씩 외워서, 3급 빠르기로 들려줘요: ♩ = 92(양손 함께), 80(반대 방향), 92(반음계). 넘기는 곳과 엄지가 함께 닿는지 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks3.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks3} storeKey="pb_s3_five"/>}/>
    </LbPage>,
  ];
}
function Scales3LessonBook() { return <>{s3LbPages(false)}</>; }
function S3Learn({ onStart }) {
  const pages = s3LbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-3" title={t('Scales, Grade 3', '스케일, Grade 3')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-3"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}""")
R("""Object.assign(SCALES_23_DRILL, { levels: SCF_LEVELS, generate: genScfQuestion,""", """splitDrill(SCALES_3_DRILL, SCALES_23_DRILL, [3, 4, 5], S3Learn);   // Build DJ
Object.assign(SCALES_23_DRILL, { levels: SCF_LEVELS, generate: genScfQuestion,""")
# the Workbook: the check-up only (its parts B, C, D ask the Grade 3 keys); the Teacher copy: the base's blocks for those steps
R("""function ScfWorkbook({ startNo = 1 }) {
  const W = SCF_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-23">{content}</WbPage>);""",
  """function ScfWorkbook({ startNo = 1, g = 2 }) {   // Build DJ: g = 3 is Scales, Grade 3: the check-up only, until it has pages of its own
  const W = SCF_WB, pages = [], ch = g === 3 ? 'scales-3' : 'scales-23';
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId={ch}>{content}</WbPage>);""")
R("""  P(<ScfPaperCheck/>);
  return <>{pages}</>;
}""", """  P(<ScfPaperCheck/>);
  return <>{g === 3 ? splitWb(pages, [], ['B', 'C', 'D'], startNo) : pages}</>;
}""")
# finish() before ScfTeacher's return (the line right above TEACHER_COPIES['scales-23'])
_k = s.index("TEACHER_COPIES['scales-23'] = ScfTeacher;"); _r = s.rindex('  return <>{pages}</>;\n}', 0, _k)
s = s[:_r] + '  finish();   // Build DJ\n' + s[_r:]
R("""function ScfTeacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-23" teacher>{content}</WbPage>);""",
  """function ScfTeacher({ g = 2 }) {   // Build DJ: g = 3 is Scales, Grade 3 (the melodic minor, contrary motion and chromatic blocks, and the check-up's parts B to D)
  const pages = [], ch = g === 3 ? 'scales-3' : 'scales-23', one = [];
  const P = (content) => g === 3 ? one.push(content) : pages.push(<WbPage key={pages.length} no={pages.length + 1} chId={ch} teacher>{content}</WbPage>);
  const finish = () => { if (one.length) pages.push(<SplitCtx.Provider key="one" value={{ steps: [3, 4, 5], secs: ['B', 'C', 'D'], pages: { 1: 1, 4: 2, 5: 3, 6: 4, 7: 5 } }}><WbPage no={1} chId={ch} teacher>{one.map((c, i) => <React.Fragment key={i}>{c}</React.Fragment>)}</WbPage></SplitCtx.Provider>); };""")
R("""    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-23')}</div>""",
  """    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName(ch)}</div>""")
R("""TEACHER_COPIES['scales-23'] = ScfTeacher;""", """TEACHER_COPIES['scales-23'] = ScfTeacher;
TEACHER_COPIES['scales-3'] = () => <ScfTeacher g={3}/>;   // Build DJ""")
R("""WORKBOOKS['scales-23'] = ScfWorkbook;""", """WORKBOOKS['scales-23'] = ScfWorkbook;
WORKBOOKS['scales-3'] = () => <ScfWorkbook g={3}/>;   // Build DJ""")
R("""'scales-23': Scales23LessonBook,""", """'scales-23': Scales23LessonBook, 'scales-3': Scales3LessonBook,""")
R("""'scales-23': scfLbPages,""", """'scales-23': scfLbPages, 'scales-3': s3LbPages,""")
R("""  'scales-23': { secs: ['B', 'D'], back: { B: [2, 3], D: [5, 6] }, Paper: () => <ScfPaperCheck/> },""",
  """  'scales-23': { secs: ['A', 'D'], back: { A: [1, 2], D: [5, 6] }, Paper: () => <ScfPaperCheck/> },   // Build DJ: Grade 2 asks these
  'scales-3': { secs: ['B', 'C'], back: { B: [1, 2], C: [2, 3] }, Paper: () => <ScfPaperCheck/> },""")
R("""const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23', 'harmony-2', 'rhythm-2']], '4': [['listen-3', 'harmony-3'], ['rhythm-3']],""",
  """const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23', 'harmony-2', 'rhythm-2']], '4': [['listen-3', 'melody-3', 'harmony-3'], ['scales-3', 'rhythm-3']],""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
