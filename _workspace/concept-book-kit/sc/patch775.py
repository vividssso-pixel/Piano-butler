#!/usr/bin/env python3
"""Build CZ (on t774 -> t775). Sohyun 2026-10-30 00:36 'don't wait, make it now': the Prelim floor's Lesson Books get the
fun-first treatment the Beginner floor got in Build CU (patches 768 and 769): one 'Guess first!' on each opener and one
challenge ('5 in a row' or 'Beat your time') under each step's 'At the piano'. Eight rooms: listen-sing, tempo, rhythm,
ledger-lines, scales, scale-play, minor-scales, signs.
Only her metaphors (walk / run-ning, the bird and the turtle, ladders, mirror twins, thumb under and 3 over) and only facts
the pages already teach. Time challenges get their own ids (beat13 on), so a best time is kept in either language.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
G = {
 'lsLbPages': (['When the music stops, should your clapping stop too?', '음악이 멈추면 손뼉도 멈춰야 할까요?'], ['No: the beat keeps going, counting inside.', '아니요. 속으로 세면서 박은 계속 가요.'], 2),
 'stmLbPages': (['If you play louder, does the tempo get faster?', '세게 치면 빠르기도 빨라질까요?'], ['No. Tempo is how fast the beat goes; loud is not fast.', '아니요. 빠르기는 박이 얼마나 빠른지예요. 세게는 빠르게가 아니에요.'], 2),
 'srhLbPages': (['A dot after a crotchet: does the note get longer or shorter?', '4분음표 뒤에 점이 붙으면 음이 길어질까요, 짧아질까요?'], ['Longer: one and a half beats.', '길어져요. 한 박 반.'], 4),
 'llLbPages': (['From low C up to high C, counting both, how many Cs are there?', '낮은 도부터 높은 도까지, 둘 다 세면 C가 몇 개일까요?'], ['Five: low C, bass C, middle C, treble C, high C.', '다섯 개: 낮은 도, 낮은음자리표 도, 가운데 도, 높은음자리표 도, 높은 도.'], 6),
 'sscLbPages': (['How many black keys are in the C major scale?', 'C장조 음계에는 검은건반이 몇 개일까요?'], ['None: all white keys.', '하나도 없어요. 모두 흰건반.'], 2),
 'spLbPages': (['Both thumbs on middle C, one hand going up, one going down: do they play the same finger numbers?', '두 엄지를 가운데 도에 놓고 한 손은 위로, 한 손은 아래로: 두 손이 같은 번호를 칠까요?'], ['Yes: mirror twins, the same number every time.', '네. 거울 쌍둥이, 언제나 같은 번호.'], 5),
 'msLbPages': (['Which sounds darker: a major third or a minor third?', '장3도와 단3도 중 어느 게 더 어둡게 들릴까요?'], ['The minor third: three half steps.', '단3도예요. 반음 3개.'], 2),
 'sgnLbPages': (['D.C. al Fine: where do you go back to?', 'D.C. al Fine를 만나면 어디로 돌아갈까요?'], ['The beginning, then on to Fine.', '처음으로. 그다음 Fine까지.'], 4),
}
# (the LbRemember it goes before, kind, en, ko). The scales and signs books write their text with their own X().
C = {
 'lsLbPages': [
  ('The beat keeps going, even when the music stops.', 'row', 'Your teacher stops and starts the chords: keep clapping, and be right there when the music comes back.', '선생님이 화음을 멈췄다 다시 쳐요: 손뼉은 계속, 음악이 돌아올 때 딱 같이.'),
  ('Listen to the end, then echo it on the beat.', 'row', 'Your teacher claps two bars: echo them straight back, the same, with no stop in the beat.', '선생님이 두 마디를 치면 박을 멈추지 않고 바로 똑같이 메아리.'),
  ('Higher: up to the bird.', 'row', 'Eyes closed, two notes: say "bird!" if the second is higher, "turtle!" if it is lower.', '눈을 감고 두 음을 들어요: 두 번째가 더 높으면 "새!", 더 낮으면 "거북이!"'),
  ('Listen, sing, play.', 'row', 'Your teacher plays three notes: sing them back on "la", then play them in C position.', '선생님이 세 음을 치면 "라"로 따라 부르고, C 자리에서 쳐요.'),
 ],
 'stmLbPages': [
  ('Tempo: how fast the beat goes.', 'row', 'Someone calls "slow!" or "fast!" while you play C D E F G: change the tempo on the very next note, not the loudness.', '치는 중에 누가 "느리게!"나 "빠르게!"를 외치면 바로 다음 음부터 빠르기만 바꿔요. 셈여림은 그대로.'),
  ('Adagio, Andante, Moderato, Allegro: slow to fast.', 'row', 'Someone calls one of the four tempo words: play C eight times at that tempo.', '누가 빠르기말 네 개 중 하나를 부르면 그 빠르기로 C를 여덟 번 쳐요.'),
  ('Read the tempo word first. Count in, then play.', 'row', 'A new tune: read the tempo word, count in at that tempo, then play it through with no stop.', '새 곡: 빠르기말을 읽고, 그 빠르기로 미리 세고, 멈춤 없이 끝까지.'),
  (': 60 beats a minute, one every second.', 'row', 'Someone sets the metronome to 60 or 120 without showing you: listen and say which.', '누가 메트로놈을 몰래 60이나 120에 맞추면 듣고 어느 쪽인지 말해요.'),
  ('Keep the tempo steady: no rushing, no dragging.', 'row', 'Metronome on 90: someone turns the sound off for four beats, then on. Still on the tick?', '메트로놈 90: 누가 네 박 동안 소리를 껐다 켜요. 아직 똑딱에 맞나요?'),
 ],
 'srhLbPages': [
  ('Beams group quavers by the beat: 1 +, 2 +.', 'row', 'Someone points to a beamed pair or a crotchet: say "run-ning" or "walk", then clap it.', '누가 빔으로 묶인 두 음이나 4분음표를 가리키면 "티-티" 또는 "타"라고 말하고 손뼉을 쳐요.'),
  ('A flag: a quaver alone.', 'row', 'Line 1: the hand lifts on every rest, with no sound sneaking in.', '1번 줄: 쉼표마다 손을 들고, 소리가 새어 나오지 않게.'),
  ('A dotted crotchet: one and a half beats.', 'row', 'Someone claps long-short (1 2 +) or two walks (1 2): say "dotted!" or "walk walk!"', '누가 길게-짧게(1 2 +)나 타 타(1 2)를 치면 "점!" 또는 "타 타!"'),
  ('Before beat 1: count the missing beats, then start.', 'row', 'Line 1, then line 2: count in out loud and come in on the right beat, never early.', '1번 줄, 그다음 2번 줄: 소리 내어 미리 세고, 일찍 들어가지 않게 제 박에 들어가요.'),
  ('Count it, clap it, play it.', 'row', 'A new line of rhythm: count it, clap it, then play it on G, with no stop.', '새 리듬 한 줄: 세고, 손뼉 치고, G로 쳐요. 멈춤 없이.'),
 ],
 'llLbPages': [
  ('A ledger line is a little ladder for one note', 'row', 'Someone points to a note: say "ladder!" if it sits on a ledger line, "staff!" if not, before they count to 3.', '누가 음을 가리키면 셋 세기 전에, 덧줄 위면 "발판!", 아니면 "오선!"'),
  ('Up out of the treble staff', 'row', 'Up in the sky: someone calls a ladder over the treble staff, 1, 2 or 3. Name its note and play it before they count to 3.', '하늘에서: 누가 높은음자리표 오선 위 발판 번호(1, 2, 3)를 부르면 셋 세기 전에 그 음 이름을 말하고 쳐요.'),
  ('Down out of the bass staff', 'row', 'Down in the sea: someone calls a ladder under the bass staff, 1, 2 or 3. Name its note and play it with the left hand before they count to 3.', '바다에서: 누가 낮은음자리표 오선 아래 발판 번호(1, 2, 3)를 부르면 셋 세기 전에 그 음 이름을 말하고 왼손으로 쳐요.'),
  ('Between the staves, the ladders are borrowed', 'row', 'Someone points to an A, C or E between the staves: play it with the hand of the staff it is written on.', '누가 두 오선 사이의 A, C, E 중 하나를 가리키면, 그 음이 적힌 오선의 손으로 쳐요.'),
  ('Five Cs from the sea to the sky', 'time', 'The five Cs, low to high and back down, naming each one: how fast with no slip?', '다섯 C를 낮은 데서 높은 데로, 다시 내려오며 이름을 말해요: 틀리지 않고 얼마나 빨리?'),
 ],
 'sscLbPages': [
  ('A major scale: whole, whole, half', 'row', 'Someone plays two white keys side by side: say "whole" or "half" before they count to 3.', '누가 나란한 흰건반 두 개를 치면 셋 세기 전에 "온" 또는 "반".'),
  ('Going up: the right hand', 'row', 'C major up and down with each hand, saying "thumb under!" or "3 over!" at the very moment you do it.', '양손 각각 C장조 음계를 올라갔다 내려오며, 넘어가는 바로 그 순간 "엄지 밑으로!" 또는 "3번 넘기기!"'),
  ('Degrees 1 to 8. Degree 1, the tonic, is home.', 'row', 'Someone calls a number from 1 to 8: play that note of C major before they count to 3.', '누가 1에서 8 사이 번호를 부르면 셋 세기 전에 C장조 음계의 그 음을 쳐요.'),
  ('G major: one sharp, F♯.', 'time', 'G major’s letters up and down, out loud, saying the sharp every time: how fast with no slip?', 'G장조 음계의 글자를 올라갔다 내려오며 소리 내어, 샵도 매번 말해요: 틀리지 않고 얼마나 빨리?'),
  ('F major: one flat, B♭.', 'row', 'F major, right hand, up and down: 4 over onto B♭ every time, with no bump.', 'F장조 음계 오른손 올라갔다 내려오기: 매번 4번 넘기기로 B♭, 덜컹 없이.'),
 ],
 'spLbPages': [
  ('The thumb gets ready early: no bump.', 'row', 'C major up and back while someone listens: a bump at the turn, and you start again.', 'C장조 음계를 올라갔다 내려와요. 누가 들어요: 넘길 때 덜컹하면 처음부터.'),
  ('One note on every beat; the last one holds.', 'row', 'Metronome on 76: C major or G major from memory, one note a click, the last note held for two.', '메트로놈 76: C장조나 G장조를 외워서, 똑딱 하나에 한 음, 마지막 음은 두 박.'),
  ('Harmonic minor: the 7th goes up a half step.', 'row', 'Someone calls "natural!" or "harmonic!": play A minor that way. G or G♯ at the top?', '누가 "자연!" 또는 "화성!"을 외치면 A단조를 그렇게 쳐요. 꼭대기는 G일까요, G♯일까요?'),
  ('Same numbers, both ways: mirror twins.', 'row', 'Mirror twins from middle C: say each number as both hands play it, with no wrong finger.', '가운데 도에서 거울 쌍둥이: 두 손이 칠 때마다 번호를 말하며, 틀린 손가락 없이.'),
  ('Two notes a beat: run-ning.', 'row', 'G major, hands together, run-ning: the two thumbs land together on the middle G every time.', 'G장조 양손 함께, 티-티: 두 엄지가 매번 가운데 G에서 함께 닿게.'),
 ],
 'msLbPages': [
  ('Four half steps: major third. Three: minor third.', 'row', 'Someone plays a third: say "major!" or "minor!" before they count to 3.', '누가 3도를 치면 셋 세기 전에 "장3도!" 또는 "단3도!"'),
  ('Same key signature: the minor is three half steps down.', 'time', 'C, G, F, B♭: say each major with its minor out loud (“C major, A minor”…): how fast with no slip?', 'C, G, F, B♭: 장조마다 단조 짝을 소리 내어(“C장조, A단조”…): 틀리지 않고 얼마나 빨리?'),
  ('Harmonic minor: raise the 7th, beside the note.', 'row', 'Someone names A, E, D or G minor: play its raised 7th before they count to 3.', '누가 A, E, D, G단조 중 하나를 말하면 셋 세기 전에 올라간 7번째 음을 쳐요.'),
  ('Harmonic minor: T S T T S T½ S.', 'row', 'A harmonic minor, very slowly, naming each step (T, S or T½), with no wrong name.', 'A 화성 단음계를 아주 천천히, 걸음마다 이름(T, S, T½)을 틀리지 않고.'),
  ('A darker third and a wide step near the top', 'row', 'Someone plays a scale: say "major!" or "harmonic minor!" before it ends.', '누가 음계를 치면 끝나기 전에 "장음계!" 또는 "화성 단음계!"'),
 ],
 'sgnLbPages': [
  ('Go back to the start-repeat sign, or to the beginning.', 'row', 'Someone points to a repeat sign: say "start!" or "end!" before they count to 3.', '누가 도돌이표를 가리키면 셋 세기 전에 "시작!" 또는 "끝!"'),
  ('First time the 1. bar, second time the 2. bar.', 'row', 'These bars all the way through, the right way both times, with no stop.', '이 마디들을 처음부터 끝까지, 두 번 다 길을 틀리지 않고 멈춤 없이.'),
  ('D.C. al Fine: from the beginning to Fine.', 'row', 'Trace the road with a finger: from the start to D.C. al Fine, back to the beginning, and on to Fine, with no wrong turn.', '손가락으로 길 따라가기: 처음부터 D.C. al Fine까지, 처음으로 돌아가 Fine까지, 길을 틀리지 않고.'),
  ('D.C.: back to the beginning. D.S.: back to the sign.', 'row', 'Someone calls "D.C.!" or "D.S.!": point to where you go back to before they count to 3.', '누가 "D.C.!" 또는 "D.S.!"를 외치면 셋 세기 전에 돌아갈 곳을 가리켜요.'),
  ('A pause: hold it longer, then go on.', 'row', 'Someone plays two bars twice, once with a pause and once without: say which one had the pause.', '누가 두 마디를 두 번 쳐요, 한 번은 늘임표대로, 한 번은 없이: 어느 쪽에 늘임표가 있었는지 말해요.'),
 ],
}
WRAP = {'sscLbPages': 'X', 'sgnLbPages': 'X'}   # these two books write text with their own X() (sharps, flats, spacing)
def esc(x): return x.replace('\\', '\\\\').replace("'", "\\'")
def nb(x): return re.sub(r'(?<=(?:^|(?<=[\s(]))[0-9A-G]) (?=[0-9A-G](?:[\s,.:)+]|$))', ' ', x)
def norm(x): return x.replace(' ', ' ')
beat = max(int(n) for n in re.findall(r'tid="beat(\d+)"', s))
L = s.split('\n')
added = []
for fn in G:
    st = [i for i, l in enumerate(L) if l.startswith('function ' + fn + '(')][0]
    en = next(i for i in range(st + 1, len(L)) if L[i].startswith('function ') and 'LessonBook' in L[i])
    k1 = next(i for i in range(st, en) if '<LbPage key="1"' in L[i])
    sy = next(i for i in range(k1, en) if '</LbSay>' in L[i])
    (qe, qk), (ae, ak), page = G[fn]
    w = WRAP.get(fn, 't')
    ins = {sy + 1: ["      <LbGuess q={%s('%s', '%s')} a={%s('%s', '%s')} page={%d}/>" % (w, esc(nb(qe)), esc(nb(qk)), w, esc(nb(ae)), esc(nb(ak)), page)]}
    for (m, kind, e, k) in C[fn]:
        hits = [i for i in range(st, en) if '<LbRemember>' in L[i] and m in norm(L[i])]
        assert len(hits) == 1, (fn, m, len(hits))
        if kind == 'time':
            beat += 1; attr = ' kind="time" tid="beat%d"' % beat
        else:
            attr = ''
        ins.setdefault(hits[0], []).append("      <LbChallenge%s>{%s('%s', '%s')}</LbChallenge>" % (attr, w, esc(nb(e)), esc(nb(k))))
    for at in sorted(ins, reverse=True):
        L[at:at] = ins[at]
    added.append((fn, len(C[fn])))
s = '\n'.join(L)
# the scales opener: the keyboard clock's frame may now shrink a little to make room for the guess (print; it fits itself)
old = "  const p1 = <LbLive still={<LbPic h={410}><div role=\"img\" aria-label={t('The keyboard clock"
assert s.count(old) == 1
s = s.replace(old, "  const p1 = <LbLive still={<LbPic h={scr ? 410 : 340}><div role=\"img\" aria-label={t('The keyboard clock")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', added, 'last beat id', beat)
