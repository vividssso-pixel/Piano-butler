import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
# Build CU (her 12:51: the joke is not it, and not funny; the two opener lists look alike: make 'what you learn' and
# 'what you can do after' plainly different, with tick boxes; the turtle and the bird can both walk on the ground, so
# middle C is where they meet; then the next chapters):
#  1. LbJoke goes. In its place 'Guess first!': a question the chapter answers, a box to write the guess in and the page
#     with the answer (online: one tap shows it).
#  2. Every opener (all 59 books, and the two whole-book openers): 'By the end, you can' becomes 'After this chapter, I can'
#     in a raised panel with green tick boxes; 'In this chapter' stays the contents with page numbers.
#  3. Chapter 2, step 3: middle C is the ground where the turtle and the bird both walk; the picture shows them meeting there.
#  4. The challenges and the guess for the first half of the Beginner floor: chapters 1, 3, 4, 5, 6 and 7.
i = s.index('// The butler\'s joke: one per chapter, on the opener.')
j = s.index('\n}\n', i) + 3
s = s[:i] + r"""// 'Guess first!' (Build CU): a question the chapter answers, on the opener. Printed: a line for the guess and the page
// with the answer; online: one tap shows it.
function LbGuess({ q, a, page }) {
  const scr = lbScreen(); const [open, setOpen] = useState(false);
  return <div className="lb-guess" style={{display:'flex',alignItems:'center',gap:'6px 12px',flexWrap:'wrap',borderTop:'0.8px solid ' + BK.ink,borderBottom:'0.8px solid ' + BK.ink,padding:'6px 2px'}}>
    <span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS,whiteSpace:'nowrap'}}>{t('Guess first!', '먼저 맞혀 봐요!')}</span>
    <span style={{flex:'1 1 240px',fontSize:14.5,lineHeight:1.42,color:BK.ink,minWidth:0}}>{q}</span>
    {scr ? (open ? <b style={{fontSize:14,color:BK.ink}}>{a}</b> : <button className="chip" onClick={() => setOpen(true)} style={{fontSize:12.5,padding:'2px 10px'}}>{t('Answer', '정답')}</button>)
         : <span style={{display:'inline-flex',alignItems:'flex-end',gap:8,fontSize:11.5,color:BK.muted,flex:'0 0 auto'}}><span style={{display:'inline-block',width:72,height:20,borderBottom:'1.2px solid ' + BK.ink}}/>{t('answer on page ' + page, '정답은 ' + page + '쪽에')}</span>}
  </div>;
}
// 'After this chapter, I can' (Build CU): the opener's second list in a raised panel with green tick boxes, so it never
// looks like the contents beside it. The heading carries lb-can-h; the panel and boxes are drawn here, print and online.
const LB_CAN_CSS = `
  div:has(> .lb-can-h) { border: 0.8px solid rgba(38,41,107,0.55); box-shadow: inset 0 0 0 4px #fff, inset 0 0 0 4.7px rgba(38,41,107,0.45); background: #fff; padding: 10px 14px 8px; }
  div:has(> .lb-can-h) > div:not(.lb-can-h) { border-bottom: none !important; }
  div:has(> .lb-can-h) > div:not(.lb-can-h) svg { display: none !important; }
  div:has(> .lb-can-h) > div:not(.lb-can-h) > span:has(> svg:only-child) { display: none !important; }
  div:has(> .lb-can-h) > div:not(.lb-can-h)::before { content: ''; flex: 0 0 auto; width: 15px; height: 15px; margin-top: 3px; border: 1.6px solid #2e8a6e; border-radius: 2px; background: #fff; }
`;
try { const el = document.createElement('style'); el.setAttribute('data-lb-can', ''); el.textContent = LB_CAN_CSS; document.head.appendChild(el); } catch (e) {}
""" + s[j:]
rep("""      <LbJoke q={t('Why do the piano keys never get lost?', '건반들은 왜 길을 잃지 않을까요?')} a={t('They always know which house they live in.', '자기가 어느 집에 사는지 늘 알거든요.')}/>""",
    """      <LbGuess q={t('How many small houses does a real piano have?', '진짜 피아노에는 작은 집이 몇 채 있을까요?')} a={t('Seven, and seven big ones.', '일곱 채, 큰 집도 일곱 채예요.')} page={4}/>""")
# 2. the can-do list
n1 = s.count("""className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}""")
n2 = s.count("""className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 책을 마치면')}""")
assert n1 == 58 and n2 == 2, (n1, n2)
s = s.replace("""className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}""",
              """className="lb-toc-h lb-can-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('After this chapter, I can', '이 챕터를 마치면')}""")
s = s.replace("""className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 책을 마치면')}""",
              """className="lb-toc-h lb-can-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('After this book, I can', '이 책을 마치면')}""")
# 3. chapter 2: the turtle and the bird meet on the ground at middle C
rep("""Middle C is <b>the ground</b>: right goes <b>up into the sky</b>, left goes <b>down under the sea</b>.""",
    """Middle C is <b>the ground</b>, where the turtle and the bird can both walk: right goes <b>up into the sky</b>, left goes <b>down under the sea</b>.""")
rep("""가운데 도는 <b>땅</b>이에요: 오른쪽은 <b>하늘 위로</b>, 왼쪽은 <b>바다 아래로</b>.""",
    """가운데 도는 <b>땅</b>이에요. 거북이도 새도 걸어 다닐 수 있어요. 오른쪽은 <b>하늘 위로</b>, 왼쪽은 <b>바다 아래로</b>.""")
rep("""<LbRemember>{t('Middle C is the ground: up into the sky, down under the sea.', '가운데 도는 땅: 위로 가면 하늘, 아래로 가면 바다.')}</LbRemember>""",
    """<LbRemember>{t('Middle C is the ground, where the turtle and the bird meet: up is the sky, down is the sea.', '가운데 도는 땅, 거북이와 새가 만나는 곳: 위로 가면 하늘, 아래로 가면 바다.')}</LbRemember>""")
rep("""    s.push(...penPlace([...fsCloud(-24, 14, 0.8), ...fsBird(4, 0, 1)], 0.82, [0, 0], [548, 26]));
    return s;""", """    s.push(...penPlace([...fsCloud(-24, 14, 0.8), ...fsBird(4, 0, 1)], 0.82, [0, 0], [548, 26]));
    // Build CU (her 12:51): on the ground at middle C the turtle and the bird can both walk: they meet there
    s.push(penLine([mcX - 70, 186], [mcX + W + 70, 186], 1.6, 'rgba(38,41,107,0.45)'));
    s.push(...penPlace(fsTurtle(0, 0, 1), 0.95, [0, 0], [mcX - 26, 174]));
    s.push(...penPlace(fsBird(0, 0, 1), 1.05, [0, 0], [mcX + W + 24, 175]));
    return s;""")
rep("""<PenArt shapes={art5} vb={[0, 14, P_W, 140]} label={t('All 88 keys: 7 small and 7 big houses, the lighthouse on the lonely black key by the sea, and middle C, the ground between the sea and the sky', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 바닷가 외로운 검은건반 위의 등대, 그리고 바다와 하늘 사이의 땅인 가운데 도')}/>""",
    """<PenArt shapes={art5} vb={[0, 14, P_W, 180]} label={t('All 88 keys: 7 small and 7 big houses, the lighthouse on the lonely black key by the sea, and middle C, the ground between the sea and the sky, where the turtle and the bird meet', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 바닷가 외로운 검은건반 위의 등대, 그리고 바다와 하늘 사이의 땅인 가운데 도, 거북이와 새가 만나는 곳')}/>""")
# 4. the first half of the Beginner floor
G = {
 'postureLbPages': (['Which finger is number 1?', '1번 손가락은 어느 손가락일까요?'], ['The thumb, on both hands.', '엄지예요. 양손 모두.'], 5),
 'plLbPages': (['When the notes stop, does the beat stop too?', '음이 멈추면 박도 멈출까요?'], ['No: silent beats still count.', '아니요. 조용한 박도 세요.'], 4),
 'nnLbPages': (['How many letters does music use to name every white key?', '흰건반 전부에 이름을 붙이는 데 글자가 몇 개 필요할까요?'], ['Seven: A to G, round and round.', '일곱 개: A부터 G까지, 돌고 돌아요.'], 2),
 'hpLbPages': (['Both hands play the same finger numbers together. Do they move the same way, or opposite ways?', '두 손이 같은 번호를 함께 치면, 같은 쪽으로 갈까요, 반대쪽으로 갈까요?'], ['Opposite ways: mirror twins.', '반대쪽이에요. 거울 쌍둥이.'], 5),
 'epLbPages': (["Close your eyes. Is the piano's lowest note nearer your left hand or your right?", '눈을 감아요. 피아노의 가장 낮은 음은 왼손 쪽일까요, 오른손 쪽일까요?'], ['Your left: down with the turtle.', '왼손 쪽이에요. 거북이와 함께 아래로.'], 2),
 'nvLbPages': (['Which lasts longest: a crotchet, a minim or a semibreve?', '4분음표, 2분음표, 온음표 중 어느 게 가장 길까요?'], ['The semibreve: 4 beats.', '온음표예요. 4박.'], 4),
}
C = {
 'postureLbPages': [
  ('Front half of the stool, feet flat, sit tall', 'row', 'Ready in 5 seconds: front half of the stool, feet flat, sitting tall. Someone counts.', '5초 안에 준비: 의자 앞쪽 절반, 발바닥은 바닥에, 허리는 쭉. 누가 세어 줘요.'),
  ('The arm leads from above', 'row', 'All six movements in order, without looking at the book.', '책을 보지 않고 여섯 동작을 순서대로.'),
  ('A free wrist, as if on a roller', 'row', 'One key with each finger, on the tip, knuckles up: not one knuckle caves in.', '손가락마다 건반 하나씩, 손끝으로, 마디는 위로: 꺾이는 마디 하나 없이.'),
  ('Fingers are numbered 1 to 5 from the thumb', 'time', 'Number race: someone calls "Left hand, 4!" and you wiggle it. How fast can you answer ten calls?', '번호 경주: 누가 "왼손 4번!" 하고 부르면 꼼지락. 열 번 부르는 데 얼마나 빨리?'),
  ('A little rainbow from key to key', 'row', '1 2 3 4 5 and back: a little rainbow over every key, shoulders soft.', '1 2 3 4 5 갔다가 돌아오기: 건반마다 작은 무지개, 어깨는 편하게.'),
 ],
 'plLbPages': [
  ('A steady beat: the same gap every time.', 'row', 'Pat 8 beats with the same gap every time while someone listens for a hurry.', '무릎을 8번, 매번 같은 간격으로. 누가 서두르는지 들어 줘요.'),
  ('Count out loud: 1 2 3 4, then 1 again.', 'row', 'Pat and count 1 2 3 4, four times round, with no stop and no extra number.', '무릎을 치며 1 2 3 4를 네 바퀴, 멈춤도 덤 숫자도 없이.'),
  ('Silent beats still count.', 'row', 'Play only on 1, count the rest in your head, and come back in exactly on the next 1.', '1에서만 치고, 나머지는 머릿속으로 세다가 다음 1에 딱 맞춰 들어와요.'),
  ('The beat stays steady; the rhythm is the sounds on top.', 'row', 'Foot on the beat, clap the words: walk, run-ning, run-ning, walk. Change the order each time; the foot never changes.', '발은 박, 손뼉은 낱말: 타, 티-티, 티-티, 타. 순서를 매번 바꿔도 발은 그대로.'),
  ('A new finger on each beat; keep counting.', 'row', 'Each row twice, counting out loud, with no stop between the rows.', '줄마다 두 번, 소리 내어 세며, 줄 사이에 멈춤 없이.'),
 ],
 'nnLbPages': [
  ('A B C D E F G: C D E in the small house', 'time', 'Every C on the piano, bottom to top, as fast as you can. Then every F.', '피아노의 모든 C를 아래에서 위로 최대한 빨리. 그다음 모든 F.'),
  ('Seven letters, round and round', 'time', 'Round the wheel from E back to E, out loud. Then from B.', 'E에서 시작해 관람차 한 바퀴, 다시 E까지 소리 내어. 그다음 B에서.'),
  ('Up the piano: forwards. Down the piano: backwards.', 'time', 'The letters backwards from G down to A, then from C round to C.', 'G부터 A까지 거꾸로, 그다음 C부터 C까지 거꾸로.'),
  ('count from C: ask who lives there', 'row', 'The fast game with no slip: someone touches a key, you say who lives there and the letter.', '빠른 게임을 틀리지 않고: 누가 건반을 짚으면, 누가 사는지와 글자를 말해요.'),
  ('A skip jumps over a friend', 'time', 'Skip up from middle C to the next C and back down, saying only the letters you play.', '가운데 도에서 다음 C까지 건너뛰며 올라갔다 내려와요, 치는 글자만 말하면서.'),
  ('Read the letter, see its place, play.', 'row', 'C D E, E D C with your eyes on the letters, not on your fingers.', 'C D E, E D C를 손가락이 아니라 글자를 보며.'),
 ],
 'hpLbPages': [
  ('One finger, one key. Right thumb on middle C', 'row', 'Eyes closed, land in C position, open your eyes and check: every finger on its key?', '눈 감고 C 자리에 내려앉고, 눈 뜨고 확인: 손가락마다 제 건반에?'),
  ('The same shape on G: G A B C D', 'row', 'In G position, say the note under each finger without playing: right hand, then left.', 'G 자리에서 치지 않고 손가락마다 밑의 음 이름 말하기: 오른손, 그다음 왼손.'),
  ('Lift, travel, land: the arm carries the hand.', 'row', 'C position, G position, C position on a steady beat, with no stop.', '꾸준한 박으로 C 자리, G 자리, 다시 C 자리, 멈춤 없이.'),
  ('Same numbers together: mirror twins.', 'row', '1+1 up to 5+5 and back, both hands landing exactly together.', '1+1부터 5+5까지 갔다 오기, 두 손이 딱 함께 닿게.'),
  ('The waiting hand stays ready on its keys.', 'row', 'Call and answer with no gap: the other hand answers right on the next beat.', '부르고 대답하기를 틈 없이: 다른 손이 바로 다음 박에 대답해요.'),
  ('Round hand, one finger on each key, a steady beat.', 'row', 'One tune all the way through on a steady beat, with no stop.', '곡 하나를 꾸준한 박으로 끝까지, 멈춤 없이.'),
 ],
 'epLbPages': [
  ('Low, middle, high: turtle, Clara, bird.', 'row', 'Five notes, five right moves in a row.', '음 다섯 개, 맞는 동작 다섯 번 연속.'),
  ('Listen to the end of both.', 'row', 'Five pairs of rhythms, five right answers in a row.', '리듬 다섯 쌍, 맞는 대답 다섯 번 연속.'),
  ('Sing the first one inside.', 'row', 'Five pairs of tunes, five right answers in a row.', '선율 다섯 쌍, 맞는 대답 다섯 번 연속.'),
  ('Up to the bird, down to the turtle.', 'row', 'Five paths drawn right in a row.', '길 다섯 개를 연속으로 맞게 그리기.'),
  ('Sing it, then find it: higher or lower?', 'row', 'Five notes sung, then found, in a row.', '음 다섯 개를 부르고 찾기, 연속으로.'),
 ],
 'nvLbPages': [
  ('A crotchet: one beat.', 'row', 'Eight crotchets, counting out loud, every one the same length.', '4분음표 여덟 개, 소리 내어 세며, 모두 같은 길이로.'),
  ('A minim: two beats.', 'row', 'Hold every minim to the end of its second beat: no early lift.', '2분음표마다 둘째 박 끝까지 누르기: 일찍 떼지 않기.'),
  ('Dotted minim: 3 beats. Semibreve: 4 beats.', 'row', 'Someone points to a note in the picture: say its beats before they count to 3.', '누가 그림 속 음표를 가리키면, 셋을 세기 전에 박 수를 말해요.'),
  ('Two quavers: one beat.', 'row', 'walk, run-ning, run-ning, walk: say it, clap it, play it, with no stumble.', '타, 티-티, 티-티, 타: 말하고, 손뼉 치고, 쳐요, 더듬지 않고.'),
  ('A rest: count the silence.', 'row', 'At each rest, hand just above the key, counting: the next note comes in exactly on time.', '쉼표마다 손은 건반 바로 위, 세면서: 다음 음이 딱 제때 들어와요.'),
 ],
}
def esc(x): return x.replace('\\', '\\\\').replace("'", "\\'")
import re as _re
def nb(x): return _re.sub(r'(?<=(?:^|(?<=[\s(]))[0-9A-G]) (?=[0-9A-G](?:[\s,.:)+]|$))', '\u00a0', x)
def norm(x): return x.replace('\u00a0', ' ')
L = s.split('\n')
for fn in G:
    st = [i for i, l in enumerate(L) if l.startswith('function ' + fn + '(')][0]
    en = next(i for i in range(st + 1, len(L)) if L[i].startswith('function ') and 'LessonBook' in L[i])
    k1 = next(i for i in range(st, en) if '<LbPage key="1"' in L[i])
    sy = next(i for i in range(k1, en) if '</LbSay>' in L[i])
    (qe, qk), (ae, ak), page = G[fn]
    ins = {sy + 1: ["      <LbGuess q={t('%s', '%s')} a={t('%s', '%s')} page={%d}/>" % (esc(qe), esc(qk), esc(ae), esc(ak), page)]}
    for (m, kind, e, k) in C[fn]:
        hits = [i for i in range(st, en) if '<LbRemember>' in L[i] and m in norm(L[i])]
        assert len(hits) == 1, (fn, m, len(hits))
        line = "      <LbChallenge%s>{t('%s', '%s')}</LbChallenge>" % (' kind="time"' if kind == 'time' else '', esc(nb(e)), esc(nb(k)))
        ins.setdefault(hits[0], []).append(line)
    for at in sorted(ins, reverse=True):
        L[at:at] = ins[at]
s = '\n'.join(L)
assert 'LbJoke' not in s
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
