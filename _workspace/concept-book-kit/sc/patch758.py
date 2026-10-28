import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CM (her 09:38: the couplet and the stanza become Melody Lesson Book steps with Workbook pages). Step 8 (Grade 4):
# a melody for a couplet; step 9 (Grade 5): a melody for a four-line stanza. Each a Lesson Book page (its still picture is
# the pad's own example), a Workbook page facing it, its check, its Teacher copy answers. The check-up becomes nine checks.

# ── the Lesson Book: two stills, two pages, two checks ──
rep("""  // the check icons
  const dots = (pts, col, hiI) =>""", """  // p9, p10 (Build CM): the couplet and the stanza, each with its example melody, the words under the notes, a phrase mark a line
  const cR = MW_CPL.kites, sR = MW_STZ_R[MW_STZ_IDS[0]];
  const p9 = stack([lab8('A melody for the couplet, in F major', '두 줄 시에 붙인 F장조 선율', 'l1'), <div key="m" style={{maxWidth:640,margin:'0 auto',width:'100%'}}><MwStaff k="F" rh={cR} notes={mwModelC('F', cR)} phr="lines" words={cR.words} hl={[cR.qi, cR.words.length - 1]} per={4} label={t('The couplet set to an eight-bar melody in F major, the words under the notes, a phrase mark over each line; line 1 ends away from the tonic, line 2 on it.', '두 줄 시에 붙인 F장조 8마디 선율: 음표 아래에 가사, 줄마다 프레이즈 표시; 첫 줄은 으뜸음이 아닌 음에서, 둘째 줄은 으뜸음에서 끝나요.')}/></div>,
    <div key="k" style={{display:'grid',gap:4,maxWidth:560,margin:'0 auto',width:'100%'}}>{mark8('1', 'The words set the rhythm: a note for every syllable.', '가사가 리듬을 정해요: 음절마다 음 하나.')}{mark8('2', 'Line 1 ends away from the tonic: a question.', '첫 줄은 으뜸음이 아닌 음에서 끝나요: 질문.')}{mark8('3', 'Line 2 comes home to the tonic: the answer.', '둘째 줄은 으뜸음으로 돌아와요: 대답.')}</div>], 330, 10, 660);
  const p10 = stack([lab8('A melody for the stanza, in D major', '네 줄 시에 붙인 D장조 선율', 'l1'), <div key="m" style={{maxWidth:500,margin:'0 auto',width:'100%'}}><MwStaff k="D" rh={sR} notes={sR.model.map(dg => MW_KEYS.D.t + dg - 1)} phr="lines" words={sR.words} hl={sR.ends} per={4} label={t('The stanza set to a sixteen-bar melody in D major, a line of words a row; lines 1 to 3 end away from the tonic, line 4 on it.', '네 줄 시에 붙인 D장조 16마디 선율, 한 줄에 가사 한 줄; 1~3줄은 으뜸음이 아닌 음에서, 4줄은 으뜸음에서 끝나요.')}/></div>,
    cap(t('Coral: where each line rests. Lines 1, 2 and 3 rest away from the tonic; line 4 comes home.', '산호색: 줄마다 쉬는 음. 1, 2, 3줄은 으뜸음이 아닌 음에서 쉬고, 4줄은 으뜸음으로 돌아와요.'), 'c10')], 440, 6, 660);

  // the check icons
  const dots = (pts, col, hiI) =>""")
rep("""    seq: [{ k: 'raw', svg: dots([[8, 30], [16, 24], [24, 28], [32, 22]], PEN_N) + dots([[38, 24], [46, 18], [54, 22], [62, 16]], PEN_N) + dots([[68, 18], [76, 12], [84, 16], [90, 10]], PEN_C) }],
  };""", """    seq: [{ k: 'raw', svg: dots([[8, 30], [16, 24], [24, 28], [32, 22]], PEN_N) + dots([[38, 24], [46, 18], [54, 22], [62, 16]], PEN_N) + dots([[68, 18], [76, 12], [84, 16], [90, 10]], PEN_C) }],
    couplet: [{ k: 'raw', svg: '<path d="M6 12 Q26 0 46 12" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/><path d="M48 12 Q68 0 88 12" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/>' + [10, 22, 34].map(x => '<rect x="' + x + '" y="28" width="8" height="3" rx="1.5" fill="' + PEN_N + '"/>').join('') + [52, 64, 76].map(x => '<rect x="' + x + '" y="28" width="8" height="3" rx="1.5" fill="' + PEN_N + '"/>').join('') + '<circle cx="84" cy="22" r="3.4" fill="' + PEN_C + '"/>' }],   // Build CM
    stanza: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => '<path d="M' + (4 + i * 22) + ' 14 Q' + (14 + i * 22) + ' 4 ' + (24 + i * 22) + ' 14" fill="none" stroke="' + PEN_N + '" stroke-width="1.6"/><rect x="' + (8 + i * 22) + '" y="28" width="12" height="3" rx="1.5" fill="' + PEN_N + '"/>').join('') + '<circle cx="86" cy="22" r="3.4" fill="' + PEN_C + '"/>' }],   // Build CM
  };""")
rep("""    ['write', t('I can write a four-bar melody on a rhythm', '주어진 리듬에 4마디 선율을 쓸 수 있어요')],   // Build AO
  ]""", """    ['write', t('I can write a four-bar melody on a rhythm', '주어진 리듬에 4마디 선율을 쓸 수 있어요')],   // Build AO
    ['couplet', t('I can write a melody for a couplet: line 1 asks, line 2 answers', '두 줄 시에 선율을 쓸 수 있어요: 첫 줄은 묻고, 둘째 줄은 대답해요')],   // Build CM
    ['stanza', t('I can write a melody for a four-line stanza that comes home in line 4', '네 줄 시에 4줄에서 집으로 돌아오는 선율을 쓸 수 있어요')],   // Build CM
  ]""")
rep("""[t('Writing a melody', '선율 쓰기'), 8], [t('My seven checks', '나의 일곱 가지 확인'), 9]]""", """[t('Writing a melody', '선율 쓰기'), 8], [t('A couplet, a stanza (Grades 4, 5)', '두 줄 시, 네 줄 시(4·5급)'), '9, 10'], [t('My nine checks', '나의 아홉 가지 확인'), 11]]""")
rep("""    <LbPage key="9" no={9} chId={ch} kicker={t('Check-up', '점검')} title={t('My seven checks', '나의 일곱 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (1 to 4, and 6 to 8). The check-up on paper is in the Workbook.', '1~4쪽과 6~8쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>""", """    <LbPage key="9" no={9} chId={ch} kicker={t('Step 8 · Grade 4', '8단계 · 4급')} title={t('A melody for a couplet', '두 줄 시에 선율 붙이기')}>
      {live(p9, <MwCoupletPad/>)}
      <LbPiano steps={[
        X('Play the example and sing the words with it. Point to where line 1 asks and where line 2 answers.', '보기를 치면서 가사를 함께 불러요. 첫 줄이 묻는 곳과 둘째 줄이 대답하는 곳을 짚어요.'),
        X('Write a melody for another couplet, in a minor key. Mark the strong syllables first, as on page 7.', '다른 두 줄 시에 단조로 선율을 써요. 먼저 7쪽처럼 센 음절에 표시해요.'),
      ]}/>
      <LbRemember>{X('The words set the rhythm. Line 1 asks; line 2 answers on the tonic.', '가사가 리듬을 정해요. 첫 줄은 묻고, 둘째 줄은 으뜸음으로 대답해요.')}</LbRemember>
    </LbPage>,

    <LbPage key="10" no={10} chId={ch} kicker={t('Step 9 · Grade 5', '9단계 · 5급')} title={t('A melody for a four-line stanza', '네 줄 시에 선율 붙이기')}>
      {live(p10, <MwStanzaPad/>)}
      <LbPiano steps={[
        X('Play the example and sing it. Where does each line rest?', '보기를 치고 노래해요. 줄마다 어디에서 쉬나요?'),
        X('Write a melody for another stanza, in a key with up to three sharps or flats. A phrase mark over each line.', '다른 네 줄 시에 샵이나 플랫 세 개까지의 조로 선율을 써요. 줄마다 프레이즈 표시.'),
      ]}/>
      <LbRemember>{X('Four lines, one way home: lines 1 to 3 rest away; line 4 comes home.', '네 줄, 집으로 가는 한 길: 1~3줄은 밖에서 쉬고, 4줄이 집으로 돌아와요.')}</LbRemember>
    </LbPage>,

    <LbPage key="11" no={11} chId={ch} kicker={t('Check-up', '점검')} title={t('My nine checks', '나의 아홉 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (1 to 4, and 6 to 10). The check-up on paper is in the Workbook.', '1~4쪽과 6~10쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>""")
_o = "{checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}"
_a = s.index('function mlxLbPages('); _b = s.index(_o, _a); assert _b - _a < 20000
s = s[:_b] + _o.replace('{checksRows.map(', '{checksRows.slice(0, 7).map(', 1) + s[_b + len(_o):]   # Build CM: page 1 keeps the room's own seven; the Grade 4 and 5 two are in the contents
rep("""const MLX_STORE = ['k1', 'k2', 'k3', 'k4', 'k5', 'k8', 'k9', 'k6'];""", """const MLX_STORE = ['k1', 'k2', 'k3', 'k4', 'k5', 'k8', 'k9', 'k10', 'k11', 'k6'];   // Build CM: pages 9 and 10 (the couplet, the stanza) are k10, k11""")

# ── the Workbook: two pages facing Lesson Book pages 9 and 10 ──
rep("""const MW_CHK_E = [['boat', 0], ['hills', 1]];""", """const MW_CHK_E = [['boat', 0], ['hills', 1]];
// Build CM: the couplet page (a melody to check, then one to write under given words) and the stanza page
const MW_WB_C = { chk: { id: 'snow', k: 'D' }, write: [{ id: 'hills', k: 'Am' }] };
const MW_WB_S = { write: { id: MW_STZ_IDS[1] || MW_STZ_IDS[0], k: 'Bb' } };
const mwPaperTicksC = (rows) => <div style={{display:'grid',gap:3,marginTop:6}}>{rows.map(([id, v, W]) => <div key={id} style={{display:'flex',gap:7,alignItems:'center',fontSize:11.5,fontWeight:700,color:BK.ink,lineHeight:1.25}}>
  <span style={{width:15,height:15,flex:'0 0 15px',border:'1.3px solid ' + BK.line,borderRadius:2,display:'inline-flex',alignItems:'center',justifyContent:'center',color:BK.coral,fontWeight:900,fontSize:13}}>{v === true ? '✓' : ''}</span>{W[id][0]}</div>)}</div>;
function MwWbCouplet() {
  const C = MW_WB_C, R0 = MW_CPL[C.chk.id], n0 = mwModelC(C.chk.k, R0);
  return <>
    <WbTop step={8}/>
    <Part kind="together" title="Check the melody" how="A melody for a couplet. Tick what it does. Then sing it with its words.">
      <ExCell n={1} ex>{sdyCol(<>
        <div style={{fontSize:11.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',margin:'0 0 2px'}}>{MW_KEYS[C.chk.k].en.toUpperCase()} · GRADE 4</div>
        <div style={{maxWidth:470,margin:'0 auto',width:'100%'}}><MwStaff k={C.chk.k} rh={R0} notes={n0} phr="lines" words={R0.words} per={4} label={MW_KEYS[C.chk.k].en + ': a melody for a couplet.'}/></div>
        {mwPaperTicksC(mwRulesC(n0, R0, C.chk.k, 'lines').map(([id, v]) => [id, v, MW_RULE_C]))}</>, '10px 8px 8px')}</ExCell>
    </Part>
    <Part kind="home" title="Write a melody for a couplet" how="The grey notes show the rhythm the words make: write each note at its pitch. Line 1 ends away from the tonic; line 2 ends on it. A phrase mark over each line.">
      <BkGrid cols={1} gap="8px">{C.write.map((w, i) => { const R = MW_CPL[w.id]; return <BkCell key={i} n={i + 2}>{sdyCol(<div style={{display:'flex',flexDirection:'column',gap:2,maxWidth:640,margin:'0 auto',width:'100%'}}>
        <div style={{fontSize:11,fontWeight:900,letterSpacing:'0.08em',color:BK.muted}}>{MW_KEYS[w.k].en.toUpperCase()}</div>
        <MwStaff k={w.k} rh={R} notes={Array(R.words.length).fill(null)} words={R.words} per={4} sp={1.25} label={'An empty staff in ' + MW_KEYS[w.k].en + ' with the words under it.'}/></div>, '8px 8px 10px')}</BkCell>; })}</BkGrid>
    </Part>
    <Part kind="play" title="Play and sing" how="Play your melodies. Then sing them with the words. Tick each.">
      {sskRowN(3, ivxTicks(['melody 2', 'sung with the words', 'one of my own']))}
    </Part>
    <Faces/>
  </>;
}
function MwWbStanza() {
  const w = MW_WB_S.write, R = MW_STZ_R[w.id];
  return <>
    <WbTop step={9}/>
    <Part kind="home" title="Write a melody for a stanza" how="The grey notes show the rhythm: write each note at its pitch. Lines 1, 2 and 3 rest away from the tonic; line 4 comes home. Start on note 1, 3 or 5; move mostly by step; a phrase mark over each line.">
      <BkCell n={1}>{sdyCol(<div style={{display:'flex',flexDirection:'column',gap:2,maxWidth:640,margin:'0 auto',width:'100%'}}>
        <div style={{fontSize:11,fontWeight:900,letterSpacing:'0.08em',color:BK.muted}}>{MW_KEYS[w.k].en.toUpperCase()} · GRADE 5</div>
        <MwStaff k={w.k} rh={R} notes={Array(R.words.length).fill(null)} words={R.words} per={4} sp={1.3} label={'An empty staff in ' + MW_KEYS[w.k].en + ' with the stanza under it.'}/></div>, '8px 8px 10px')}</BkCell>
    </Part>
    <Part kind="together" title="Check it" how="Tick each one your melody does.">
      {mwPaperTicksC(['start', 'steps', 'mid', 'end', 'phr'].map(id => [id, null, MW_RULE_S]))}
    </Part>
    <Part kind="play" title="Play and sing" how="Play your melody, then sing it with the words. Tick each.">
      {sskRowN(2, ivxTicks(['played', 'sung with the words']))}
    </Part>
    <Faces/>
  </>;
}""")
rep("""  P(<MwWbWrite/>);   // Build AO: faces page 8
  P(<MlxMyPiece/>);""", """  P(<MwWbWrite/>);   // Build AO: faces page 8
  P(<MwWbCouplet/>);   // Build CM: faces page 9
  P(<MwWbStanza/>);   // Build CM: faces page 10
  P(<MlxMyPiece/>);""")
rep("""function MlxMyPiece() {
  const row = (label, node, h = 46) =>""", """function MlxMyPiece() {
  const row = (label, node, h = 46) =>""")
rep("""  return <>
    <WbTop step={9}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div>""", """  return <>
    <WbTop step={11}/>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-end',gap:12,margin:'0 0 2px'}}>
      <div style={{minWidth:0}}><div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>ANY PIECE</div>""")

# ── the Teacher copy ──
rep("""    <TcBlock page={9} title="Any piece: my piece’s melody (a fresh copy for each piece)" """, """    <TcBlock page={9} title="A melody for a couplet (Grade 4)" answers={<>{sscLesson('The example played and sung with its words; a melody for another couplet, in a minor key, its strong syllables marked first (page 7).')}{skgTcAns('TRY IT', ['all five: starts on note ' + mwDeg(mwModelC(MW_WB_C.chk.k, MW_CPL[MW_WB_C.chk.id])[0], MW_WB_C.chk.k) + ', mostly by step, line 1 ends away from the tonic, line 2 on it, a phrase mark a line (done)'])}<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>YOUR TURN: any melody with the five points. One answer:</div>{skgTcAns('', MW_WB_C.write.map(w => mwModelC(w.k, MW_CPL[w.id]).map(d => mwName(d, w.k)).join(' ')), 2)}
      <div style={{fontSize:12,color:BK.ink,marginTop:4,lineHeight:1.5}}>Theory of Music Grade 4, Creative: a melody for a couplet, the words written under the notes, in a major or minor key. The words set the rhythm as on page 7; the five points are the same textbook guidance as page 8, with the question at the end of line 1. In a minor key the 7th is raised (the harmonic minor), as the keyboard on the screen shows.</div></>}
      watch="Two notes on one syllable, or a syllable left without a note. A word split across a bar line at the wrong place (the bar line goes before the strong syllable). Line 1 ending on the tonic, so there is no question. In a minor key, the 7th left unraised."
      say="“The words set the rhythm. Line 1 asks; line 2 answers.”"/>
    <TcBlock page={10} title="A melody for a four-line stanza (Grade 5)" answers={<>{sscLesson('The example played and sung, each line’s resting note found; a melody for another stanza in a key up to three sharps or flats.')}<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>YOUR TURN: any melody with the five points. One answer:</div>{skgTcAns('', [MW_STZ_R[MW_WB_S.write.id].model.map(dg => mwName(MW_KEYS[MW_WB_S.write.k].t + dg - 1, MW_WB_S.write.k)).join(' ')], 1)}
      <div style={{fontSize:12,color:BK.ink,marginTop:4,lineHeight:1.5}}>Theory of Music Grade 5, Creative: a melody for a four-line stanza, the words under the notes, a phrase mark over each line. Lines 1 to 3 rest away from the tonic and line 4 comes home; a modulation is allowed, not needed. The stanzas are new, written for this book, and keep the three rules of page 7.</div></>}
      watch="Every line ending on the tonic, so the melody comes home four times. A line with no phrase mark. Long leaps where the words are quick."
      say="“Lines 1 to 3 rest away; line 4 comes home.”"/>
  </>);
  P(<>
    <TcBlock page={11} title="Any piece: my piece’s melody (a fresh copy for each piece)" """)
rep("""    <TcBlock page={10} title="The check-up on paper (the Workbook’s last page)" answers={<>""", """    <TcBlock page={12} title="The check-up on paper (the Workbook’s last page)" answers={<>""")
rep("""Also listen to the student (My seven checks, Lesson Book page 9).</div>""", """Also listen to the student (My nine checks, Lesson Book page 11).</div>""")
rep("""<b style={{color:BK.coral}}>My seven checks (Lesson Book page 9).</b> 1. On page 1’s map, point to the question, the answer, the motif and the high point. 2. Draw the line of a tune the teacher plays. 3. Play page 3’s phrase shaped, with its breath. 4. Play page 4’s question and answer and say which is which. 5. Play page 6’s motif in sequence, a step higher each time. 6. Mark a couplet’s strong syllables and clap its rhythm (page 7). 7. Write a four-bar melody on a rhythm, with phrase marks, ending on the tonic, and play it (page 8). Got it! means right without help.""",
    """<b style={{color:BK.coral}}>My nine checks (Lesson Book page 11).</b> 1. On page 1’s map, point to the question, the answer, the motif and the high point. 2. Draw the line of a tune the teacher plays. 3. Play page 3’s phrase shaped, with its breath. 4. Play page 4’s question and answer and say which is which. 5. Play page 6’s motif in sequence, a step higher each time. 6. Mark a couplet’s strong syllables and clap its rhythm (page 7). 7. Write a four-bar melody on a rhythm, with phrase marks, ending on the tonic, and play it (page 8). 8. Write a melody for a couplet, line 1 a question and line 2 the answer, and sing it with the words (page 9, Grade 4). 9. Write a melody for a four-line stanza that comes home in line 4 (page 10, Grade 5). Got it! means right without help; checks 8 and 9 wait for their grade.""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
