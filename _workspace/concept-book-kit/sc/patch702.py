import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AI-4: the teacher's copies for the two listening rooms, Listen and Sing and Listen, Clap, Write. No Workbook: every
# step is by ear. Each block faces its Lesson Book page and gives the material to play (taken from the room's own lists, so
# the copy and the app use the same phrases), what to watch for and what to say. Her words: walk, run-ning, hold; the bird
# and the turtle for higher and lower.
CODE_LS = r'''
// ─── Chapter: Listen and Sing, the teacher's copy (Build AI-4; no Workbook: every step is by ear) ───
const lstWord = (x) => ({ w: 'walk', r: 'run-ning', '-': '(hold)', '.': '(rest)' })[x] || x;
const lstEchoText = (seq) => seq.slice(0, 4).map(lstWord).join(' ') + '  |  ' + seq.slice(4).map(lstWord).join(' ');
const lstDegLetters = (s) => s.split(' ').map(g => 'CDEFG'[+g - 1]).join(' ');
function LsTeacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-sing" teacher>{content}</WbPage>);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-sing')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. The app scores taps; whether a child sang in tune is your ear. Sing on "la" at a comfortable pitch; C position only, no staff yet.</div>
    <TcBlock page={2} title="Keep the beat" answers={<>{tcAns('PLAY', ['chords in two, slow (60), then stop: the clapping carries on', 'the same in three, moderate (84)', 'then quick (108), in two or three'])}</>}
      watch="Slowing down or speeding up when the music stops. Come back in after a bar or two to check you are still together."
      say="“The beat keeps going, even when the music stops.”"/>
    <TcBlock page={3} title="Echo the rhythm" answers={<>{tcAns('CLAP', LS_ECHO.map(lstEchoText))}</>}
      watch="Starting the echo late, so the beat has a gap. Call and echo on the same beat, no pause between."
      say="“Listen to the end, then echo it on the beat.”"/>
    <TcBlock page={4} title="Higher or lower" answers={<>{tcAns('PLAY', ['two notes wide apart (C, then a high G); then closer, but always a third or more', 'one soft and higher, one loud and lower: up is not louder'])}</>}
      watch="“Up” heard as “louder”. Mix the dynamics so only the pitch gives the answer."
      say="“Higher: up to the bird. Lower: down to the turtle.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Find your note" answers={<>{tcAns('PLAY', ['one note from C position (C to G); the child sings it, then finds it'])}</>}
      watch="Hunting along the keys. Ask “higher or lower?” before the next try."
      say="“Sing it, then find it: higher or lower?”"/>
    <TcBlock page={6} title="Sing it back" answers={<>{tcAns('THREE NOTES', LS_SING[3].map(lstDegLetters))}{tcAns('FIVE NOTES', LS_SING[5].map(lstDegLetters), 7)}{tcAns('SIX NOTES', LS_SING[6].map(lstDegLetters), 13)}</>}
      watch="Playing before singing. Sing back first, every time: the ear leads and the hand follows. If the playing goes wrong, sing it again rather than hunting on the keys."
      say="“Listen, sing, play.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one shown with you, at the piano or away from it: you play, the child claps, sings or plays. You only correct. Use material the child has not heard this week.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-sing'] = LsTeacher;
'''
CODE_LW = r'''
// ─── Chapter: Listen, Clap, Write, the teacher's copy (Build AI-4; no Workbook: every step is by ear) ───
const lwtDLet = (d) => 'CDEFGAB'[(d - 28 + 70) % 7];
const lwtPhText = (ph) => { const out = []; for (let j = 0; j < ph.length; j++) { const [d, b] = ph[j];
  if (b === 0.5 && ph[j + 1] && ph[j + 1][1] === 0.5) { out.push(lwtDLet(d) + '-' + lwtDLet(ph[j + 1][0]) + ' run-ning'); j++; } else out.push(lwtDLet(d) + ' ' + (b === 2 ? 'hold' : 'walk')); }
  return out.join(' · '); };
function LwTeacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-write" teacher>{content}</WbPage>);
  const homes = LW_HOME.slice(0, 6).map((degs, i) => { const pos = i % 2 ? 'G' : 'C'; return pos + ' position: ' + lwKeysOf(pos, degs).map(lwLet).join(' ') + ' → home ' + pos; });
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-write')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 1 aural tests and the listening part of the Grade 1 theory ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. The dictation on page 6 is written on paper: any staff paper will do.</div>
    <TcBlock page={2} title="The home note" answers={<>{tcAns('PLAY', homes)}</>}
      watch="Humming the last note heard instead of the home note. If it is hard, sing down the scale to it (5 4 3 2 1) and let the voice fall home, then find it on the keys."
      say="“The tune stops; your ear goes home.”"/>
    <TcBlock page={3} title="Two or three?" answers={<>{tcAns('PLAY', ['oom-pah: the low note on 1, the chord on 2 (two)', 'oom-pah-pah: the low note on 1, the chord on 2 and 3 (three)', 'then a tune with no accompaniment: count from each strong note'])}</>}
      watch="Counting every note instead of feeling where the strong one comes back. Sway or step on 1."
      say="“Oom-pah: two. Oom-pah-pah: three.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Clap it back" answers={<><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',marginBottom:4}}>{spTx('PLAY TWICE, THEN THE CHILD CLAPS (♩ = ' + LW_CLAP_BPM + ')')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{LW_CLAP.map((row, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{rqStaffEl(row, { counts: false, hearts: false })}</div></div>)}</div></>}
      watch="Clapping along the first time. Listen both times without clapping, count inside, then clap at the same speed."
      say="“Listen twice, count inside, then clap.”"/>
    <TcBlock page={5} title="Sing it with its rhythm" answers={<>{tcAns('PLAY TWICE, THEN THE CHILD SINGS', LW_PH.map(lwtPhText))}</>}
      watch="The right notes in the wrong rhythm, usually the held note cut short. Clap it first, then sing."
      say="“The notes and the rhythm, both.”"/>
    <TcBlock page={6} title="Write the rhythm" answers={<><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',marginBottom:4}}>{spTx('GIVE THE TIME SIGNATURE AND THE BEAT, PLAY UP TO FIVE TIMES (♩ = 76)')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:'4px 14px'}}>{LW_DICTS.map((D, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0,maxWidth:200}}>{rqStaffEl(lwDictItems(D), { counts: false, hearts: false })}</div></div>)}</div></>}
      watch="Writing notes before counting the beats. Clap the beat lightly while listening; write the beats first as small strokes, then the notes. Each bar must add up."
      say="“Count the beats, then choose the notes.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen: you play, the child hums, says, claps, sings or writes. You only correct. Use material the child has not heard this week.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-write'] = LwTeacher;
'''
rep("""function ListenSingLessonBook() { return <>{lsLbPages(false)}</>; }""", """function ListenSingLessonBook() { return <>{lsLbPages(false)}</>; }""" + CODE_LS)
rep("""function ListenWriteLessonBook() { return <>{lwLbPages(false)}</>; }""", """function ListenWriteLessonBook() { return <>{lwLbPages(false)}</>; }""" + CODE_LW)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
