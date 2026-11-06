#!/usr/bin/env python3
# Phase 474 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 19, Key Signatures,
# the first room of Level 4, built in full: the Lesson Book (dictionary entries), its screen lesson (the book with a pad on
# pages 2 to 6), a 9-level drill, the Workbook and the Teacher copy (both replace the Phase 299 ones).
#   skgbook474.jsx: the staff with a key signature (SkgStaff), reading a tune in a key (skgRead), the Lesson Book
#   skgapp474.jsx:  the pads of pages 2 to 6, SkgLearn, the drill (Object.assign on KEYSIG_DRILL)
#   skgwb474.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 473 (chapter 17's SacStaff, SacKeys and sacRead are the models; chapter 11's tnAcc draws the signs).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['skgbook474.jsx', 'skgapp474.jsx', 'skgwb474.jsx'])

# 1. the new code before the Lesson Book registry; key-signatures joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("'piano-story': PianoStoryLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", 'key-signatures': KeySigLessonBook };") + s[j:]
rep("accidentals: sacLbPages, 'piano-story': spsLbPages };", "accidentals: sacLbPages, 'piano-story': spsLbPages, 'key-signatures': skgLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'sharps-order', ch: 'key-signatures',", """  { id: 'skg-every', ch: 'key-signatures', title: 'Every F', blurb: 'One sharp on the top line: every F is F♯, high or low. Hear it with and without the key signature.', C: () => <SkgPad page={2}/> },
  { id: 'skg-g', ch: 'key-signatures', title: 'G major', blurb: 'G major written with its key signature: listen, then play it, every F as F♯.', C: () => <SkgPad page={3}/> },
  { id: 'skg-f', ch: 'key-signatures', title: 'F major', blurb: 'F major written with its key signature: listen, then play it, every B as B♭.', C: () => <SkgPad page={4}/> },
  { id: 'skg-acc', ch: 'key-signatures', title: 'Key signature and accidental', blurb: 'A natural lasts until the bar line; then the key signature holds again.', C: () => <SkgPad page={5}/> },
  { id: 'skg-five', ch: 'key-signatures', title: 'Name the key', blurb: 'C, G, D, F and B♭ major: each key signature and its scale.', C: () => <SkgFivePad/> },
  { id: 'sharps-order', ch: 'key-signatures',""")
rep("  'sharps-order': ['샤프의 순서', '번호를 붙여 하나씩 더해요.'],", """  'skg-every': ['모든 F', '맨 윗줄의 샤프 하나: 높은 F도 낮은 F도 모두 F♯. 조표대로 한 번, 조표 없이 한 번 들어 봐요.'],
  'skg-g': ['G장조', '조표로 쓴 G장조: 듣고, F는 모두 F♯로 쳐 봐요.'],
  'skg-f': ['F장조', '조표로 쓴 F장조: 듣고, B는 모두 B♭으로 쳐 봐요.'],
  'skg-acc': ['조표와 임시표', '내추럴은 세로줄까지, 그다음에는 다시 조표대로예요.'],
  'skg-five': ['조 이름', 'C, G, D, F, B♭장조: 조마다 조표와 음계.'],
  'sharps-order': ['샤프의 순서', '번호를 붙여 하나씩 더해요.'],""")
rep("'sharps-order': ['scales', 1, 3, 'game'],", "'skg-every': ['scales', 1, 2, 'game ear'], 'skg-g': ['scales', 1, 2, 'game ear'], 'skg-f': ['scales', 1, 2, 'game ear'], 'skg-acc': ['scales', 1, 2, 'game ear'], 'skg-five': ['scales', 1, 2, 'show ear'], 'sharps-order': ['scales', 1, 3, 'game'],")
rep("['sps-sound', 'keyboard-ancestors'],", "['skg-every', 'place-it'], ['skg-g', 'sharps-order'], ['skg-f', 'flats-order'], ['skg-acc', 'sharp-flat'], ['skg-five', 'circle-fifths'], ['sps-sound', 'keyboard-ancestors'],")
rep("  'key-signatures': ['sharps-order', 'flats-order', 'place-it', 'relative-minor', 'circle-fifths', 'transpose', 'all-keys'],",
    "  'key-signatures': ['skg-every', 'skg-g', 'skg-f', 'skg-acc', 'skg-five', 'sharps-order', 'flats-order', 'place-it', 'relative-minor', 'circle-fifths', 'transpose', 'all-keys'],")
# 3. the old lesson's ticks (Phase 299: 7 steps, keys 0 to 6, under the same id) are not this lesson's steps: the new
#    steps keep theirs as k1 to k6 (Step storeAs), and the counts skip the old ones (synced by union: ignored, not deleted)
rep("function stepsDone(id) { const d = loadDone()[id] || {}; return Object.values(d).filter(Boolean).length; }",
    "function stepsDone(id) { const d = loadDone()[id] || {}; return Object.keys(d).filter(k => d[k] && !skgOldStep(id, k)).length; }")
rep("const d = done[k] || {}; n += Object.keys(d).filter(i => d[i]).length;",
    "const d = done[k] || {}; n += Object.keys(d).filter(i => d[i] && !skgOldStep(k, i)).length;")
# 4. the shared Korean level names go by the English label: chapter 16's level 6 had taken note-values' 'Name the note'
#    (음표 이름 맞히기); it gets a label of its own
rep("  { n: 6, label: 'Name the note', kind: 'name', time: 9 },", "  { n: 6, label: 'Name the scale note', kind: 'name', time: 9 },")
rep("'Which degree?': '몇 번 음?', 'Name the note': '음이름 맞히기',", "'Which degree?': '몇 번 음?', 'Name the scale note': '음계의 음이름 맞히기',")
# 5. the chapter's grade tag and search words follow the new chapter
rep("'key-signatures': 'Prelim–G3'", "'key-signatures': 'Prelim–G1'")
rep("  'key-signatures': 'key signature sharps flats circle of fifths relative minor transpose',",
    "  'key-signatures': 'key signature sharps flats G major F major D major B flat major order of sharps flats circle of fifths relative minor transpose',")
# 6. 'easier after' in Korean: '..., 아니면 여기서 계속해도 돼요' (the 'or' was missing)
rep("t(', or carry on here.', ', 여기서 계속해도 돼요.')", "t(', or carry on here.', '. 아니면 여기서 계속해도 돼요.')")
# 7. the spread (Lesson Book + Workbook): every page its own key (lesson and workbook pages both began at 1)
rep("""    const out = [lp[0]];
    for (let k = 1; k <= steps; k++) out.push(lp[k], wf[k - 1] || blank('w' + k));
    wf.slice(steps, -1).forEach((pg, j) => out.push(blank('x' + j), pg));
    out.push(lp[lp.length - 1], paper);
    return <>{out}</>;""", """    const kk = (el, k) => el && React.cloneElement(el, { key: k });
    const out = [kk(lp[0], 'l0')];
    for (let k = 1; k <= steps; k++) out.push(kk(lp[k], 'l' + k), wf[k - 1] ? kk(wf[k - 1], 'w' + k) : blank('w' + k));
    wf.slice(steps, -1).forEach((pg, j) => out.push(blank('x' + j), kk(pg, 'wx' + j)));
    out.push(kk(lp[lp.length - 1], 'lz'), kk(paper, 'wz'));
    return <>{out}</>;""")
# 8. the older key-signature and scale tools say 샤프 like every rebuilt chapter (they said 샵)
for a_, b_ in [("'샵이나 플랫이 몇 개?'", "'샤프나 플랫이 몇 개?'"), ("'샵과 플랫의 순서'", "'샤프와 플랫의 순서'"), ("'검은건반까지 (샵과 플랫)'", "'검은건반까지 (샤프와 플랫)'"),
               ("'검은건반 이름 (샵과 플랫)'", "'검은건반 이름 (샤프와 플랫)'"), ("'샵·플랫 없음'", "'샤프·플랫 없음'"),
               ("(q.idx + 1) + '번째 ' + (q.type === 'sharp' ? '샵' : '플랫') + '은…'", "(q.idx + 1) + '번째 ' + (q.type === 'sharp' ? '샤프는…' : '플랫은…')"),
               ("t('Order of sharps', '샵의 순서')", "t('Order of sharps', '샤프의 순서')"), ("'플랫의 순서: 샵의 거꾸로'", "'플랫의 순서: 샤프의 거꾸로'"),
               ("(type === 'sharp' ? '샵' : '플랫') + ' 없음", "(type === 'sharp' ? '샤프' : '플랫') + ' 없음"),
               ("{n + 1}번째 {type === 'sharp' ? '샵' : '플랫'}({prettyNote(order[n])})은", "{n + 1}번째 {type === 'sharp' ? '샤프' : '플랫'}({prettyNote(order[n])}){type === 'sharp' ? '는' : '은'}"),
               ("5도 올라가고 샵이 하나 늘어요", "5도 올라가고 샤프가 하나 늘어요"), ("t('sharps ↻', '샵 ↻')", "t('sharps ↻', '샤프 ↻')"),
               ("'새로 생긴 ' + (k.type === 'sharp' ? '샵' : '플랫')", "'새로 생긴 ' + (k.type === 'sharp' ? '샤프' : '플랫')"),
               ("'원의 맨 위: 샵도 플랫", "'원의 맨 위: 샤프도 플랫"), ("t('Walk the sharps ↻', '샵 쪽으로 돌기 ↻')", "t('Walk the sharps ↻', '샤프 쪽으로 돌기 ↻')"),
               ("'은(는) ' + (sh ? '샵' : '플랫') + '이 '", "'은(는) ' + (sh ? '샤프가 ' : '플랫이 ')"), ("'개나 필요하고 겹' + (sh ? '샵' : '플랫')", "'개나 필요하고 겹' + (sh ? '샤프' : '플랫')"),
               ("'C 장조: 샵도 플랫도 전혀 없어요.'", "'C 장조: 샤프도 플랫도 전혀 없어요.'")]:
    n_ = s.count(a_)
    if n_ < 1: raise SystemExit('found 0: ' + a_)
    s = s.replace(a_, b_)
# 9. her 2026-10-16 22:21 question (things shown all at once before seemed gone once the chapters were split by level):
#    every chapter's lesson ends with a row to its older tools in the toolbox, so nothing looks lost (the chapter's own
#    lesson pads, named s??- / ts- / nv-, are left out: they are the lesson's pictures)
rep("""      {onStart && <button className="primary-btn" style={{marginTop:16}} onClick={onStart}>{startLabel || t('Start the drill →', '드릴 시작하기 →')}</button>}
    </div>
  );
}""", """      <LessonMore id={id}/>
      {onStart && <button className="primary-btn" style={{marginTop:16}} onClick={onStart}>{startLabel || t('Start the drill →', '드릴 시작하기 →')}</button>}
    </div>
  );
}
function LessonMore({ id }) {
  const own = { 'posture-hands': ['sit-check', 'arm-moves', 'hand-shape'], 'whole-staff': ['rhymes'] }[id] || [];
  const list = (CHAPTER_TOOL_ORDER[id] || []).filter(x => !/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sac|ts|nv)-/.test(x) && !own.includes(x)).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean);
  if (!list.length) return null;
  return <div style={{margin:'14px 0 0',padding:'10px 12px',border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,background:'#fff'}}>
    <div style={{fontSize:14,fontWeight:900,color:'var(--text)',margin:'0 0 6px'}}>{t('More in the toolbox', '툴박스에 더 있어요')}</div>
    <div style={{display:'flex',flexWrap:'wrap',gap:6}}>{list.map(tl => <a key={tl.id} className="chip" href={'?tool=' + tl.id + (LANG === 'ko' ? '&lang=ko' : '')} style={{textDecoration:'none',minHeight:44,display:'inline-flex',alignItems:'center',fontSize:13.5,whiteSpace:'normal',textAlign:'left',maxWidth:'100%'}}>{sscSx(LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][0] : tl.title)}</a>)}</div>
  </div>;
}""")
# 10. the older tools' Korean names that the row now shows: rule 8's words (선율, never 튠; direction first, 한 걸음; 셈여림)
for a_, b_ in [("'튠 조옮김'", "'선율 조옮김'"), ("같은 튠, 다른 템포", "같은 선율, 다른 템포"), ("리듬 + 음높이 = 튠", "리듬 + 음높이 = 선율"), ("튠 그리기", "선율 그리기"),
               ("론도: 계속 돌아오는 튠", "론도: 계속 돌아오는 선율"), ("한 칸 위로, 한 칸 아래로", "위로 한 걸음, 아래로 한 걸음"), ("다이나믹 순서대로 놓기", "셈여림 순서대로 놓기")]:
    if s.count(a_) < 1: raise SystemExit('found 0: ' + a_)
    s = s.replace(a_, b_)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
