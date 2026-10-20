import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("ko: '나란한조인 장조와 음이 똑같아요: A 단조는 C 장조의 흰건반을 써요. 어떤 단음계일까요?' },", "ko: '조표대로 쳐요: D 단조는 플랫 하나(B♭)만 있고 따로 올리는 음이 없어요. 어떤 단음계일까요?' },")
rep("en: 'The very same notes as its relative major: A minor uses C major’s white keys. Which minor is that?'", "en: 'It follows the key signature: D minor has one flat, B♭, and no note is raised. Which minor is that?'")
rep("en: 'Which minor has the wide T+S step, with a G♯ in it?', ko: 'G♯이 있고, 넓은 T+S 간격이 생기는 단음계는 어느 것일까요?' },",
    "en: 'Which minor has the wide T+S step, with a C♯ in it?', ko: 'C♯이 있고, 넓은 T+S 간격이 생기는 단음계는 어느 것일까요?' },\n  { ans: 'harmonic', staff: 'harmonic', en: 'Read the staff. Which minor is this?', ko: '오선을 읽어 보세요. 어떤 단음계일까요?' },\n  { ans: 'melodic', staff: 'melodic', en: 'Read the staff. Which minor is this?', ko: '오선을 읽어 보세요. 어떤 단음계일까요?' },\n  { ans: 'natural', staff: 'natural', en: 'Read the staff. Which minor is this?', ko: '오선을 읽어 보세요. 어떤 단음계일까요?' },")
rep("const M = SC_MINQ[q.i], K = isDone ? MINOR_FORMS[q.answer].steps.map(x => 9 + x).concat([21]) : null, marks = {}, names = {};\n    if (K) { const N = spellMinor('A', q.answer).map(prettyAny).concat(['A']);",
    "const M = SC_MINQ[q.i], K = isDone ? MINOR_FORMS[q.answer].steps.map(x => 2 + x).concat([14]) : null, marks = {}, names = {};\n    if (K) { const N = spellMinor('D', q.answer).map(prettyAny).concat(['D']);")
rep("{big(t('Three kinds of minor', '세 가지 단음계'))}{prompt(t(M.en, M.ko))}\n",
    "{big(t('Three kinds of minor', '세 가지 단음계'))}{prompt(t(M.en, M.ko))}\n      {M.staff && paper(<div>{scDirTag(false)}<SkgStaff items={scMinItems(M.staff, 'up')} k=\"F\" width={330} o={{ boxS: 26, D: 30 }}/>{scDirTag(true)}<SkgStaff items={scMinItems(M.staff, 'down')} k=\"F\" width={330} o={{ boxS: 26, D: 30 }}/></div>)}\n")
open(sys.argv[2],'w',encoding='utf-8').write(s)
