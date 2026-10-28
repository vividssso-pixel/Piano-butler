import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
# Build CT (the book redo, prototype; her 28 Oct 09:56 'fun first, the How to Blitz way: its approach, never its content';
# 13:35 the books follow the checks): chapter 2's Lesson Book gets the two missing fun-first pieces, for her to judge before
# the other Beginner chapters: a quick challenge with a streak or a time to beat under each 'At the piano', and the butler's
# joke on the opener (answer upside down in print, a tap online). Both print and online (the Lesson Book is the online lesson).
CODE = r"""
// ─── Build CT: fun first on paper (the book redo; prototype in chapter 2) ───
// A challenge under 'At the piano': a streak of circles to colour (green: practised) or three times to beat.
function LbChallenge({ children, kind = 'row', n = 5 }) {
  const scr = lbScreen(); const [on, setOn] = useState(0);
  const slots = kind === 'time'
    ? [0, 1, 2].map(i => <span key={i} style={{display:'inline-flex',alignItems:'flex-end',gap:2}}><span style={{display:'inline-block',width:34,height:18,borderBottom:'1.2px solid ' + BK.ink}}/><span style={{fontSize:11,color:BK.muted}}>s</span></span>)
    : Array.from({ length: n }, (_, i) => scr
      ? <button key={i} onClick={() => setOn(i + 1 === on ? i : i + 1)} aria-label={t('In a row: ', '연속: ') + (i + 1)} aria-pressed={i < on} style={{width:28,height:28,padding:4,margin:-4,border:0,background:'none',cursor:'pointer'}}><span style={{display:'block',width:20,height:20,borderRadius:10,border:'1.8px solid ' + BK.green,background:i < on ? BK.green : '#fff'}}/></button>
      : <span key={i} style={{display:'inline-block',width:17,height:17,borderRadius:9,border:'1.6px solid ' + BK.green}}/>);
  return <div className="lb-challenge" data-kind={kind} style={{display:'flex',alignItems:'center',gap:'6px 12px',flexWrap:'wrap',borderTop:'0.8px solid ' + BK.ink,borderBottom:'0.8px solid ' + BK.ink,padding:'5px 2px'}}>
    <span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS,whiteSpace:'nowrap'}}>{kind === 'time' ? t('Beat your time', '기록 깨기') : t(n + ' in a row', n + '번 연속')}</span>
    <span style={{flex:'1 1 230px',fontSize:14,lineHeight:1.42,color:BK.ink,minWidth:0}}>{children}</span>
    <span style={{display:'inline-flex',gap:6,alignItems:'center',flex:'0 0 auto'}}>{slots}</span>
  </div>;
}
// The butler's joke: one per chapter, on the opener. Printed, the answer is upside down; online, one tap shows it.
function LbJoke({ q, a }) {
  const scr = lbScreen(); const [open, setOpen] = useState(false);
  return <div className="lb-joke" style={{display:'flex',alignItems:'center',gap:10,fontSize:14.5,lineHeight:1.45,color:BK.ink}}>
    <img src={VIC_CAMEO} alt="" style={{height:34,width:'auto',flex:'0 0 auto'}}/>
    <span style={{minWidth:0}}><span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS,marginRight:8}}>{t('The butler’s joke', '버틀러의 농담')}</span>{q}{' '}
      {scr ? (open ? <i style={{fontWeight:700}}>{a}</i> : <button className="chip" onClick={() => setOpen(true)} style={{fontSize:12,padding:'1px 9px',verticalAlign:'1px'}}>{t('Answer', '정답')}</button>)
           : <span style={{display:'inline-block',transform:'rotate(180deg)',fontStyle:'italic',color:BK.muted,whiteSpace:'nowrap'}}>{a}</span>}</span>
  </div>;
}
"""
rep("// Phase 394: the check-up page's paper part\nfunction LbPaperHead() {", CODE + "// Phase 394: the check-up page's paper part\nfunction LbPaperHead() {")
lines = s.split('\n')
def after(pred, new, lo=0, hi=None):
    global lines
    idx = [i for i, l in enumerate(lines) if (i >= lo and (hi is None or i < hi)) and pred(l)]
    assert len(idx) == 1, (len(idx), new[:60])
    lines[idx[0] + 1:idx[0] + 1] = [new]
start = [i for i, l in enumerate(lines) if l.startswith('function fsLbPages(')][0]
end = [i for i, l in enumerate(lines) if l.startswith('function FirstStepsLessonBook(')][0]
after(lambda l: "The piano\\'s 88 keys are one small pattern" in l and '<LbSay' in l,
      "      <LbJoke q={t('Why do the piano keys never get lost?', '건반들은 왜 길을 잃지 않을까요?')} a={t('They always know which house they live in.', '자기가 어느 집에 사는지 늘 알거든요.')}/>", start, end)
end += 1
# each 'At the piano' gets its challenge (inserted before the page's Remember)
def before(pred, new, lo, hi):
    global lines
    idx = [i for i, l in enumerate(lines) if lo <= i < hi and pred(l)]
    assert len(idx) == 1, (len(idx), new[:60])
    lines[idx[0]:idx[0]] = [new]
before(lambda l: "<LbRemember>{t('A 2-key roof = the small house." in l,
       "      <LbChallenge kind=\"time\">{t('House race: from the bottom of the piano to the top, touch every roof and say \"small, big, small...\" as fast as you can, with no slip.', '집 경주: 피아노 맨 아래부터 맨 위까지 지붕마다 짚으며 \"작은 집, 큰 집, 작은 집...\" 하고 최대한 빨리, 틀리지 않게.')}</LbChallenge>", start, end); end += 1
before(lambda l: "<LbRemember>{t('Every white key lives under a roof" in l,
       "      <LbChallenge>{t('Someone points to a white key. Say \"small house!\" or \"big house!\" before they count to 3.', '누가 흰건반 하나를 가리키면, 셋을 세기 전에 \"작은 집!\" 또는 \"큰 집!\" 하고 말해요.')}</LbChallenge>", start, end); end += 1
before(lambda l: "<LbRemember>{t('Middle C is the ground" in l,
       "      <LbChallenge>{t('Close your eyes, open them, and find middle C before someone counts to 3.', '눈을 감았다 뜨고, 누가 셋을 세기 전에 가운데 도를 찾아요.')}</LbChallenge>", start, end); end += 1
before(lambda l: "<LbRemember>{t('Legato: a relay baton" in l,
       "      <LbChallenge>{t('The roof walk with no gap and no bump between the notes.', '음과 음 사이에 틈도 쿵도 없이 지붕 걷기.')}</LbChallenge>", start, end); end += 1
s = '\n'.join(lines)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
