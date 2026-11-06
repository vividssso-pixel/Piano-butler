#!/usr/bin/env python3
# Phase 399 (part b): songs out of the chapters (Sohyun 2026-10-09: "make the repertoire separately -- first the lesson and the
# concept, then Hot Cross Buns and so on"; she chose: take out only the songs, keep the concept play; the song book comes after
# the chapter review). Chapter 2's play page keeps fingers 2 3 4 on the roofs, legato (the relay baton), the echo game and the
# Black-key jam, with a roof walk (a finger pattern, like chapter 1's finger walks) where Hot Cross Buns was. Chapter 3's play
# page reads letters onto the keys: a read-and-play letter pattern on C D E, Spell and play, the letter chain; on screen,
# Spell it on the keys (WordKeys) where the Hot Cross Buns player was. Five checks, paper checks, Workbook pages and Teacher
# copies follow. The songs stay in the code for the song book: BLACK_SONGS + BlackKeySong (also still in the toolbox),
# FS_SONG + SongRow, NN_SONG + LetterSong, NN_SONG_L.
#   python3 patch399b.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()

def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# ── chapter 2 ──
rep("""  const hcb = ['4', '3', '2', '-', '|', '4', '3', '2', '-', '|', '2', '2', '2', '2', '3', '3', '3', '3', '|', '4', '3', '2', '-'];""",
    """  const roofWalk = ['2', '3', '4', '-', '|', '4', '3', '2', '-', '|', '2', '3', '4', '3', '|', '2', '-', '-', '-'];   // up and back, then the little hill (Phase 399)""", 'fs seq')
rep("""{t('Fingers 2 3 4 only, in both hands -- 1 and 5 wait for C position. The legato tip:""",
    """{t('Fingers 2 3 4 only, in both hands -- 1 and 5 wait for C position. No songs here: the tunes live in the song book. The legato tip:""", 'fs teacher en')
rep("""'양손 모두 2 3 4번만 써요 -- 1번과 5번은 C 포지션에서 만나요. 레가토 팁:""", """'양손 모두 2 3 4번만 써요 -- 1번과 5번은 C 포지션에서 만나요. 여기에는 노래가 없어요: 곡은 노래책에 있어요. 레가토 팁:""", 'fs teacher ko')
rep("""<>이제 지도가 보답할 차례예요. 첫 튠에는 악보가 필요 없어요: <b>검은건반 지붕</b>과 양손의 <b>2, 3, 4번</b> 손가락이면 돼요.""",
    """<>이제 지도가 보답할 차례예요. 악보 없이도 칠 수 있어요: <b>검은건반 지붕</b>과 양손의 <b>2, 3, 4번</b> 손가락이면 돼요.""", 'fs say ko')
rep("""<>Now the map pays you back. Your first tunes need no written notes: just the <b>black-key roofs</b> and fingers <b>2, 3, 4</b> of both hands.""",
    """<>Now the map pays you back. You can play without any written notes: just the <b>black-key roofs</b> and fingers <b>2, 3, 4</b> of both hands.""", 'fs say en')
rep("""      <LbOnly print><div style={{zoom:0.85}}><LbTune name="Hot Cross Buns" how={t('right hand 2 3 4 on the big roof; one circle = one steady beat', '오른손 2 3 4를 큰 지붕에; 동그라미 하나 = 일정한 박 하나')} seq={hcb}/></div></LbOnly>
      <LbOnly screen><BlackKeySong/></LbOnly>
      <LbOnly screen><BlackKeyJam/></LbOnly>
      <div style={{border:'1px solid #ece6d8',borderRadius:12,padding:'7px 12px',fontSize:13.5,lineHeight:1.5,color:BK.ink}}>
        <b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('More tunes in the online lesson', '온라인 레슨에서 더 치기')}</b> — {t('left hand 2 3 on the small roof, right hand 2 3 4 on the big one:', '왼손 2 3은 작은 지붕에, 오른손 2 3 4는 큰 지붕에:')} <b>Mary Had a Little Lamb</b>{LANG === 'ko' ? ' (떴다 떴다 비행기)' : ''}, <b>Old MacDonald</b>, <b>Rain Rain Go Away</b>. {t('All famous, all free to use -- play them with their finger numbers in the online lesson.', '모두 유명하고 저작권 걱정 없는 곡이에요 -- 손가락 번호와 함께 온라인 레슨에서 쳐 봐요.')}</div>""",
    """      <div style={{zoom:0.85}}><LbTune name={t('Roof walk', '지붕 걷기')} how={t('right hand 2 3 4 on a big roof: up and back, then a little hill; legato; one circle = one steady beat', '오른손 2 3 4를 큰 지붕에: 올라갔다 내려오고, 작은 언덕; 레가토; 동그라미 하나 = 일정한 박 하나')} seq={roofWalk}/></div>
      <LbOnly screen><BlackKeyJam/></LbOnly>
      <div style={{border:'1px solid #ece6d8',borderRadius:12,padding:'7px 12px',fontSize:13.5,lineHeight:1.5,color:BK.ink}}>
        <b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('Make up your own', '나만의 가락')}</b> — {t('any black keys, in any order, smooth and joined: a roof walk of your own. In the online lesson, jam on the black keys with the band.', '아무 검은건반이나, 아무 순서로, 매끄럽게 이어서: 나만의 지붕 걷기. 온라인 레슨에서는 밴드와 함께 검은건반 잼을 해 봐요.')}</div>""", 'fs play parts')
rep("""        <>가운데쯤의 큰 지붕에 오른손 <b>2, 3, 4</b>를 올리고, 노래하면서 천천히: <b>4 - 3 - 2...</b></>,
        <>한 지붕 위의 큰 지붕에서 다시 쳐요 -- 더 높은 목소리! 그다음 왼손 <b>2, 3</b>을 작은 지붕에 올려 봐요.</>,
        <><b>에코:</b> 누가 검은건반 두세 개를 치면 똑같이 바로 따라 쳐요. 그다음 나만의 튠!</>,""",
    """        <>가운데쯤의 큰 지붕에 오른손 <b>2, 3, 4</b>를 올리고, 천천히 레가토로 올라갔다 내려와요: <b>2 - 3 - 4 - 3 - 2</b>.</>,
        <>한 지붕 위의 큰 지붕에서 다시 쳐요 -- 더 높은 목소리! 그다음 왼손 <b>2, 3</b>을 작은 지붕에 올려 봐요.</>,
        <><b>에코:</b> 누가 검은건반 두세 개를 치면 똑같이 바로 따라 쳐요. 그다음 나만의 가락!</>,""", 'fs piano ko')
rep("""        <>Right-hand <b>2, 3, 4</b> on a big roof near the middle; sing and play slowly: <b>4 - 3 - 2...</b></>,
        <>Play it again one big roof higher -- a higher voice! Then try left-hand <b>2, 3</b> on a small roof.</>,
        <><b>Echo:</b> someone plays two or three black keys; you play them straight back. Then make up your own tune!</>,""",
    """        <>Right-hand <b>2, 3, 4</b> on a big roof near the middle; walk up and back, slowly and legato: <b>2 - 3 - 4 - 3 - 2</b>.</>,
        <>Play it again one big roof higher -- a higher voice! Then try left-hand <b>2, 3</b> on a small roof.</>,
        <><b>Echo:</b> someone plays two or three black keys; you play them straight back. Then make up your own!</>,""", 'fs piano en')
rep("""    ['song', [0, 0, 92, 40], t('I can play Hot Cross Buns legato with 2 3 4', '2 3 4로 핫 크로스 번을 레가토로 칠 수 있어요')],""",
    """    ['song', [0, 0, 92, 40], t('I can play legato with 2 3 4 on a big roof', '큰 지붕에서 2 3 4로 레가토로 칠 수 있어요')],""", 'fs check row')
rep("""t('play your first tune on the black keys', '검은건반으로 첫 튠을 칠 수 있어요')""",
    """t('play legato on the black keys with 2 3 4', '검은건반에서 2 3 4로 레가토로 칠 수 있어요')""", 'fs by the end')
rep("""    {bkSec('E', 'Hot Cross Buns: which finger plays the dotted key?')}""",
    """    {bkSec('E', 'Right hand on the big roof: which finger plays the dotted key?')}""", 'fs paper E')
rep("""// Phase 394: chapter 2's check-up on paper, in the order of the five checks (houses, 3 and 4, names, middle C, Hot Cross Buns)""",
    """// Phase 394: chapter 2's check-up on paper, in the order of the five checks (houses, high and low, whose house, middle C, fingers on the roof)""", 'fs paper comment')
rep("""    { id: 'sg', name: 'Hot Cross Buns', step: '4', page: '5' },""", """    { id: 'sg', name: 'Fingers on the roofs', step: '4', page: '5' },""", 'fs concept')
rep("""    <Part kind="home" title="Hot Cross Buns" how="The song in finger numbers. Fill in the missing numbers, then tick each one you do this week.">
      <SongRow gaps={FS_SONG_GAPS} ex/>
      <div style={{marginTop:8}}><PhLog rows={['Hot Cross Buns, right hand', 'Hot Cross Buns, one big roof higher', 'Echo game with someone at home', 'My own black-key tune']} label={190}/></div>""",
    """    <Part kind="home" title="Roof walks" how="The roof walk in finger numbers: fill in the missing numbers, then tick each one you do this week.">
      <NnTuneRow seq={FS_ROOF_WALK} ex/>
      <div style={{marginTop:8}}><PhLog rows={['Roof walk, right hand 2 3 4', 'The same, one big roof higher', 'Left hand 2 3 on a small roof', 'Echo game with someone at home', 'My own black-key tune']} label={190}/></div>""", 'fs wb home')
rep("""const FS_SONG_GAPS = [1, 4, 7, 11, 14, 16];""",
    """const FS_SONG_GAPS = [1, 4, 7, 11, 14, 16];
// Phase 399: the Workbook's roof walk (a finger pattern, not a song); ? = a box to fill, the first one is the worked example
const FS_ROOF_WALK = ['2', '?3', '4', '-', '|', '4', '?3', '2', '-', '|', '2', '3', '?4', '3', '|', '?2', '-', '-', '-'];""", 'fs roof data')
rep("""{tcAns('YOUR TURN', [FS_SONG.join(' ')])}<div style={{fontSize:12,color:BK.ink}}>PLAY: one unbroken line through all six pots. Then hear Hot Cross Buns legato.</div>""",
    """{tcAns('YOUR TURN', FS_ROOF_WALK.filter(x => x[0] === '?').map(x => x.slice(1)))}<div style={{fontSize:12,color:BK.ink}}>PLAY: one unbroken line through all six pots. Then play the roof walk legato.</div>""", 'fs tc p5')
rep("""(find the houses, high and low, say 3 and 4, find middle C, Hot Cross Buns legato); you only correct.""",
    """(find the houses, high and low, say 3 and 4, find middle C, legato with 2 3 4 on a big roof); you only correct.""", 'fs tc p6')

# ── chapter 3 ──
rep("""  const hcbL = ['E', 'D', 'C', '-', '|', 'E', 'D', 'C', '-', '|', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', '|', 'E', 'D', 'C', '-'];""",
    """  const readPlay = ['C', 'D', 'E', '-', '|', 'E', 'D', 'C', '-', '|', 'C', 'E', 'D', 'C', '|', 'E', '-', 'C', '-'];   // a letter pattern, not a song (Phase 399)""", 'nn seq')
rep("""{t('Same tune, new house: Chapter 2 played it by finger numbers on the black roof; now it is read by letter names on C D E. The legato is still the relay baton.""",
    """{t('Same fingers, new house: Chapter 2 played 2 3 4 by finger numbers on the black roof; now 2 3 4 read letter names on C D E. No songs here: the tunes live in the song book. The legato is still the relay baton.""", 'nn teacher en')
rep("""'같은 노래, 새 집: 2챕터에서는 검은 지붕 위에서 손가락 번호로 쳤고, 이제는 C D E 위에서 음이름을 읽고 쳐요. 레가토는 여전히 릴레이 바통.""",
    """'같은 손가락, 새 집: 2챕터에서는 검은 지붕 위에서 손가락 번호로 2 3 4를 쳤고, 이제는 C D E 위에서 음이름을 읽고 2 3 4로 쳐요. 여기에는 노래가 없어요: 곡은 노래책에 있어요. 레가토는 여전히 릴레이 바통.""", 'nn teacher ko')
rep("""<>지난 챕터에서 핫 크로스 번은 큰 검은 지붕 위에 살았어요. 이제 <b>작은 집</b>으로 이사해요: 오른손 <b>2 3 4</b>를 <b>C D E</b>에 올리고, 이번에는 손가락 번호가 아니라 <b>글자</b>를 읽어요. 그다음 왼손으로, 작은 집 하나 아래에서 쳐 봐요.</>""",
    """<>이제 글자를 읽고 바로 쳐요. 오른손 <b>2 3 4</b>를 <b>작은 집</b>의 <b>C D E</b>에 올려요: 글자를 읽고, 자리를 보고, 쳐요 -- 이번에는 손가락 번호가 아니라 <b>글자</b>를 읽어요. 그다음 왼손으로, 작은 집 하나 아래에서 쳐 봐요.</>""", 'nn say ko')
rep("""<>Last chapter, Hot Cross Buns lived on the big black roof. Now it moves into the <b>small house</b>: right-hand <b>2 3 4</b> on <b>C D E</b>, and this time you read the <b>letters</b>, not the finger numbers. Then try the left hand, one small house lower.</>""",
    """<>Now read the letters and play them. Right-hand <b>2 3 4</b> sit on <b>C D E</b> in the <b>small house</b>: read each letter, see its place, play -- this time you read the <b>letters</b>, not the finger numbers. Then try the left hand, one small house lower.</>""", 'nn say en')
rep("""      <LbOnly print><div style={{zoom:0.85}}><LbTune name="Hot Cross Buns" how={t('right hand 2 3 4 on C D E; read the letters; one circle = one steady beat', '오른손 2 3 4를 C D E에; 글자를 읽어요; 동그라미 하나 = 일정한 박 하나')} seq={hcbL}/></div></LbOnly>
      <LbOnly screen><LetterSong/></LbOnly>""",
    """      <div style={{zoom:0.85}}><LbTune name={t('Read and play', '읽고 치기')} how={t('right hand 2 3 4 on C D E; read the letters; one circle = one steady beat', '오른손 2 3 4를 C D E에; 글자를 읽어요; 동그라미 하나 = 일정한 박 하나')} seq={readPlay}/></div>
      <LbOnly screen><WordKeys/></LbOnly>""", 'nn play parts')
rep("""        <>가운데 도 근처의 <b>C D E</b>에 오른손 <b>2, 3, 4</b>. 치면서 글자를 노래해요: <b>E D C...</b></>,""",
    """        <>가운데 도 근처의 <b>C D E</b>에 오른손 <b>2, 3, 4</b>. 글자를 말하면서 읽고 쳐요: <b>C D E -- E D C</b>.</>,""", 'nn piano ko')
rep("""        <>Right-hand <b>2, 3, 4</b> on <b>C D E</b> near middle C. Sing the letters as you play: <b>E D C...</b></>,""",
    """        <>Right-hand <b>2, 3, 4</b> on <b>C D E</b> near middle C. Read and play, saying the letters: <b>C D E -- E D C</b>.</>,""", 'nn piano en')
rep("""    ['song', [0, 0, 92, 40], t('I can play Hot Cross Buns from its letters, legato', '핫 크로스 번을 글자를 보고 레가토로 칠 수 있어요')],""",
    """    ['song', [0, 0, 92, 40], t('I can read letters and play them: C D E, BAG, CAFE', '글자를 읽고 바로 칠 수 있어요: C D E, BAG, CAFE')],""", 'nn check row')
rep("""t('play Hot Cross Buns from its letter names', '음이름을 보고 핫 크로스 번을 칠 수 있어요')""",
    """t('read letters and play them, word by word', '글자를 읽고 단어처럼 칠 수 있어요')""", 'nn by the end')
rep("""    {bkSec('E', 'Hot Cross Buns: write the letters under the beats.')}
    <NnTuneRow seq={NN_CHK_SONG} n0={17}/>""",
    """    {bkSec('E', 'Put a dot on the key of each letter.')}
    <BkGrid cols={2} gap="6px 10px">{NN_CHK_WORDS.map((w, i) => <NnSpellCell key={w} w={w} n={17 + i}/>)}</BkGrid>""", 'nn paper E')
rep("""const NN_CHK_SONG = ['E', 'D', '?C', '-', '|', 'E', '?D', 'C', '-'];""",
    """const NN_CHK_SONG = ['E', 'D', '?C', '-', '|', 'E', '?D', 'C', '-'];
// Phase 399: spelling words on the keys (the play page, the Workbook and the check-up's part E)
const NN_CHK_WORDS = ['BAG', 'FACE'];
const NN_SPELL = ['BAG', 'CAFE', 'FACE', 'EGG'];
const nnSpellDots = (w) => [...new Set(w.split('').map(l => NN_L7.indexOf(l)))];
function NnSpellCell({ w, n, ex, kw = 140 }) {
  return <ExCell n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:10,padding:'10px 4px 0'}}>
    <span style={{fontSize:17,fontWeight:900,letterSpacing:'0.12em',color:BK.ink,minWidth:52}}>{w}</span>
    <div style={{flex:1,maxWidth:kw}}><PaperKeys start="C" whites={7} w={18} h={46} dots={ex ? nnSpellDots(w) : []} dotR={0.2}/></div>
  </div></ExCell>;
}""", 'nn spell data')
rep("""    { id: 'pl', name: 'Hot Cross Buns by letters', step: '6', page: '7' },""", """    { id: 'pl', name: 'Reading letters onto the keys', step: '6', page: '7' },""", 'nn concept')
rep("""  const songSeq = NN_SONG_L.map((x, i) => NN_SONG_GAPS.includes(i) ? '?' + x : x);
""", "", 'nn wb seq')
rep("""    <Part kind="together" title="Hot Cross Buns in letters" how="Fill in the missing letters, then play it: right hand 2 3 4 on C D E, reading the letters.">
      <div style={{border:'1.5px solid ' + BK.coral,background:'#fff8f5',borderRadius:8,padding:'10px 12px 8px'}}><NnTuneRow seq={songSeq} ex/></div>
    </Part>""",
    """    <Part kind="together" title="Spell it on the keys" how="Put a dot on the key of each letter, then play the word, saying the letters. The first one is done.">
      <BkGrid cols={2} gap="8px 12px">{NN_SPELL.map((w, i) => <NnSpellCell key={w} w={w} n={i + 1} ex={i === 0} kw={230}/>)}</BkGrid>
    </Part>""", 'nn wb try')
rep("""      <PhLog rows={['Hot Cross Buns, right hand, reading the letters', 'Hot Cross Buns, left hand, one small house lower', 'Letter chain with someone: forwards', 'Letter chain: backwards', 'Spell and play: BAG, CAFE, FACE']} days={7} label={250}/>""",
    """      <PhLog rows={['Read and play: C D E, E D C, right hand', 'The same, left hand, one small house lower', 'Letter chain with someone: forwards', 'Letter chain: backwards', 'Spell and play: BAG, CAFE, FACE']} days={7} label={250}/>""", 'nn wb log')
rep("""answers={<>{tcAns('TRY IT', NN_SONG_GAPS.map(i => NN_SONG_L[i]))}""",
    """answers={<>{tcAns('TRY IT', NN_SPELL.map(w => w + ': ' + [...new Set(w.split(''))].join(' ') + ' keys'))}""", 'nn tc p7')
rep("""      watch="Reading the finger numbers instead of the letters: have them sing the letter names while they play.""",
    """      watch="Reading the finger numbers instead of the letters: have them say the letter names while they play.""", 'nn tc p7 watch')
rep("""{tcAns('E', NN_CHK_SONG.filter(x => x[0] === '?').map(x => x.slice(1)))}""",
    """{tcAns('E', NN_CHK_WORDS.map(w => w + ': dots on ' + [...new Set(w.split(''))].join(' ')))}""", 'nn tc E')
rep("""(A to G on the keys, forwards and backwards, at a glance, skips, Hot Cross Buns by letters); you only correct. The paper part follows the same order: score each part on its own (A, B, C, D: 4 marks, pass 3+; E: 2 marks).""",
    """(A to G on the keys, forwards and backwards, at a glance, skips, reading letters onto the keys); you only correct. The paper part follows the same order: score each part on its own (A, B, C, D: 4 marks, pass 3+; E: 2 marks).""", 'nn tc p8')

# the app: Spell it on the keys (where the Hot Cross Buns player was)
rep("""// Hot Cross Buns read by letter names: right hand 2 3 4 on C D E (watch, then your turn)""",
    """// Spell it on the keys (Phase 399): a word of music letters; tap its letters' keys in order, in any octave
function WordKeys() {
  const WORDS = ['BAG', 'CAFE', 'FACE', 'BEAD', 'EGG', 'CAGE', 'BADGE', 'DEAF'];
  const PCS = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
  const [wi, setWi] = useState(0);
  const [i, setI] = useState(0);
  const [bad, setBad] = useState(null);
  const [hit, setHit] = useState({});
  const w = WORDS[wi], done = i >= w.length;
  function tap(k) {
    playKey(k, 0.35);
    if (done) return;
    if (k % 12 === PCS[w[i]]) { setHit(h => ({ ...h, [k]: 'good' })); setI(i + 1); setBad(null); }
    else { setBad(k); setTimeout(() => setBad(b => (b === k ? null : b)), 500); }
  }
  function next() { setWi((wi + 1) % WORDS.length); setI(0); setHit({}); setBad(null); }
  const marks = { ...hit }; if (bad !== null) marks[bad] = 'bad';
  return (
    <div className="try-box" data-word-keys style={actBox}>
      <div style={actTitle}>{t('Spell it on the keys', '건반으로 단어 치기')}</div>
      <div style={actNote}>{t('Read the word, then play its letters in order -- any octave. Say each letter as you play it.', '단어를 읽고 글자를 순서대로 쳐요 -- 어느 옥타브든 괜찮아요. 칠 때마다 글자를 말해요.')}</div>
      <div style={{display:'flex',justifyContent:'center',gap:6,margin:'2px 0 8px'}}>{w.split('').map((l, j) => <span key={j} style={{width:36,height:40,borderRadius:8,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:24,fontWeight:900,border:'2px solid ' + (j === i ? '#e4572e' : 'var(--navy-line)'),background:j < i ? '#26296b' : '#fff',color:j < i ? '#fff' : j === i ? '#e4572e' : 'var(--navy)'}}>{l}</span>)}</div>
      <TapKeyboard octaves={2} marks={marks} onTap={tap}/>
      <div style={{textAlign:'center',minHeight:24,marginTop:8,fontSize:15,fontWeight:900,color:'#2e8a6e'}}>{done ? t('You played ' + w + '!', w + '를 쳤어요!') : ''}</div>
      <div style={{textAlign:'center'}}><button className="ghost-btn" onClick={next}>{done ? t('Next word ▶', '다음 단어 ▶') : t('Another word ▶', '다른 단어 ▶')}</button></div>
    </div>
  );
}
// Hot Cross Buns read by letter names: right hand 2 3 4 on C D E (watch, then your turn) -- kept for the song book (Phase 399)""", 'word keys')

open(src, 'w', encoding='utf-8').write(s); print('patch399b ok')
