p='drills.src.html'; s=open(p).read()
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
# 1. table rows line up: every cell of a row stretches to the row's height, its content centred (her 2 Nov 'line these up')
rep("""  return <div data-ref-table={k} style={{display:'grid',gridTemplateColumns:cols,alignItems:'center',columnGap:8,""",
    """  return <div data-ref-table={k} style={{display:'grid',gridTemplateColumns:cols,alignItems:'stretch',columnGap:8,""")
rep("""    {head && head.map((h, i) => <div key={'h' + i} style={{fontSize:10.5,""", """    {head && head.map((h, i) => <div key={'h' + i} style={{display:'flex',alignItems:'flex-end',fontSize:10.5,""")
rep("""    {rows.map((r, j) => r.map((c, i) => <div key={j + '-' + i} style={{padding:'5px 0',minWidth:0,""", """    {rows.map((r, j) => r.map((c, i) => <div key={j + '-' + i} style={{display:'flex',alignItems:'center',padding:'5px 0',minWidth:0,""")
# 2. the staff and the clefs: four clefs in one row on a wide page; lines and spaces; octave signs
rep("""    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(150px,1fr))',gap:6,marginTop:8}}>{REF_CLEFS.map(""",
    """    <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(130px,1fr))',gap:6,marginTop:8}}>{REF_CLEFS.map(""")
rep("""        <RefDoor room={room} g={g}/>
      </div>)}</div>
  </div>;
}""", """        <RefDoor room={room} g={g}/>
      </div>)}</div>
    <RefLab>{t('Lines and spaces, bottom to top', '줄과 칸, 아래에서 위로')}</RefLab>
    <RefTable k="staff-names" cols="minmax(0,0.9fr) minmax(0,0.9fr) minmax(0,1.6fr)" head={[t('Staff', '보표'), t('Notes', '음'), t('To remember', '외우기')]}
      rows={[[t('Treble lines', '높은음 줄'), <b style={{letterSpacing:'0.12em'}}>E G B D F</b>, <i>Every Good Boy Deserves Fruit</i>], [t('Treble spaces', '높은음 칸'), <b style={{letterSpacing:'0.12em'}}>F A C E</b>, <i>{t('spells FACE', 'FACE (얼굴)')}</i>],
        [t('Bass lines', '낮은음 줄'), <b style={{letterSpacing:'0.12em'}}>G B D F A</b>, <i>Good Boys Deserve Fruit Always</i>], [t('Bass spaces', '낮은음 칸'), <b style={{letterSpacing:'0.12em'}}>A C E G</b>, <i>All Cows Eat Grass</i>]]}/>
    <RefLab>{t('Octave signs', '옥타브 기호')}</RefLab>
    <RefTable k="octave-signs" cols="64px minmax(0,1fr)" rows={[[<b>8va</b>, t('play an octave higher than written (a dotted line shows how long)', '적힌 것보다 한 옥타브 위로 (점선이 끝나는 곳까지)')], [<b>8vb</b>, t('play an octave lower than written', '적힌 것보다 한 옥타브 아래로')],
      [<b>15ma</b>, t('play two octaves higher', '두 옥타브 위로')], [<b><i>loco</i></b>, t('back where it is written', '적힌 자리로 돌아와요')]]}/>
    <RefNote>{t('Notes above or below the staff sit on short ledger lines; an octave sign saves writing many of them.', '보표 위나 아래의 음은 짧은 덧줄 위에 적어요. 옥타브 기호를 쓰면 덧줄을 많이 쓰지 않아도 돼요.')}</RefNote>
    <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'flex-end',marginTop:6}}><RefDoor room="whole-staff"/><RefDoor room="ledger-lines"/><RefDoor room="signs"/></div>
  </div>;
}""")
open(p,'w').write(s); print('ok')
