#!/usr/bin/env python3
"""Build DB (on t776 -> t777): the Grade 1 floor's Lesson Books, fun first, as Prelim (CZ) and Beginner (CU): one
'Guess first!' on each opener and one challenge above every step's Remember line. Eight rooms: listen-write, accidentals,
key-signatures, terms, six-eight, intervals, chords, form. Only what the pages teach; her metaphors where they fit (walk /
run-ning, home). Time challenges get their own ids (beat16 on). Also: the Form book's check-up page said 'on its page
(1 to 5)'; its steps are on pages 2 to 6.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
G = {
 'lwLbPages': (['When a tune stops before it gets home, which note does your ear want?', '선율이 집에 도착하기 전에 멈추면, 귀는 어느 음을 원할까요?'], ['The home note: the tonic.', '집 음, 으뜸음이에요.'], 2),
 'sacLbPages': (['A sharp in bar 1: is the same note still sharp in bar 2?', '1마디에 붙은 샵: 2마디의 같은 음도 아직 샵일까요?'], ['No: a sign lasts only until the bar line.', '아니요. 임시표는 세로줄까지만.'], 4),
 'skgLbPages': (['A sharp on F at the start of the line: does it change only the first F?', '줄 맨 앞 F 자리의 샵: 첫 F만 바꿀까요?'], ['No: every F, for the whole piece.', '아니요. 모든 F를 곡 끝까지.'], 2),
 'tmxLbPages': (['Which is faster: Lento or Presto?', '렌토와 프레스토 중 어느 게 더 빠를까요?'], ['Presto: near the top of the speed ladder.', '프레스토예요. 빠르기 사다리 위쪽.'], 2),
 'e8LbPages': (['In 6/8, how many beats does a dotted crotchet get?', '6/8에서 점4분음표는 몇 박일까요?'], ['Three: three quavers.', '3박이에요. 8분음표 셋.'], 3),
 'ivxLbPages': (['C up to E: a 2nd or a 3rd?', 'C에서 E까지는 2도일까요, 3도일까요?'], ['A 3rd: count both notes, C D E.', '3도예요. 두 음을 모두 세요: C D E.'], 2),
 'chxLbPages': (['C E G and C E♭ G: which one is minor?', 'C E G와 C E♭ G 중 어느 게 단3화음일까요?'], ['C E♭ G: 3 + 4 half steps.', 'C E♭ G예요. 반음 3 + 4.'], 3),
 'fmxLbPages': (['A piece goes A B A. Binary or ternary form?', '곡이 A B A로 가요. 2부 형식일까요, 3부 형식일까요?'], ['Ternary: three parts.', '3부 형식이에요. 세 부분.'], 5),
}
C = {
 'lwLbPages': [
  ('The tune stops; your ear goes home.', 'row', 'Your teacher stops a tune anywhere: hum the home note, then find it on the keys.', '선생님이 선율을 아무 데서나 멈춰요: 집 음을 흥얼거리고, 건반에서 찾아요.'),
  ('Listen twice, count inside, then clap.', 'row', 'Your teacher plays four bars twice: clap them back at the same speed, with no stop.', '선생님이 네 마디를 두 번 쳐요: 같은 빠르기로, 멈춤 없이 따라 쳐요.'),
  ('The notes and the rhythm, both.', 'row', 'Your teacher plays a short tune twice: sing it back on "la", the notes and the rhythm, then play it.', '선생님이 짧은 선율을 두 번 쳐요: "라"로 음도 리듬도 따라 부르고, 그다음 쳐요.'),
 ],
 'sacLbPages': [
  ('A sign sits just before its note', 'row', 'Someone calls "F sharp!", "B flat!" or "C sharp!": play it before they count to 3.', '누가 "F 샵!", "B 플랫!", "C 샵!"을 외치면 셋 세기 전에 쳐요.'),
  ('A natural cancels a sharp or flat.', 'row', 'Someone plays a sharp or a flat, then calls "natural!": play the white key it goes back to.', '누가 샵이나 플랫을 친 뒤 "내추럴!"을 외치면, 돌아갈 흰건반을 쳐요.'),
  ('A sign lasts until the bar line.', 'row', 'Someone points to a note after a sign: still changed, or not? Say it before they count to 3.', '누가 임시표 뒤의 음을 가리키면 셋 세기 전에: 아직 바뀐 음일까요, 아닐까요?'),
  ('A sign changes only its own line or space.', 'time', 'High F♯, low F, high F♯, low F, four times round: how fast with no slip?', '높은 F♯, 낮은 F, 높은 F♯, 낮은 F를 네 번: 틀리지 않고 얼마나 빨리?'),
  ('Find the signs, find the bar lines, then play.', 'row', 'A new tune: point to every sign and its bar line, then play it through with no wrong note.', '새 선율: 임시표와 그 세로줄을 모두 가리킨 다음, 틀린 음 없이 끝까지 쳐요.'),
 ],
 'skgLbPages': [
  ('A key signature changes every note of its letter', 'time', 'Every F♯ on the piano, from the lowest to the highest: how fast with no slip?', '피아노의 모든 F♯를 가장 낮은 것부터 가장 높은 것까지: 틀리지 않고 얼마나 빨리?'),
  ('one sharp, F♯.', 'row', 'G major with each hand from memory: F♯ under finger 4 (right) and 2 (left) every time.', 'G장조 음계를 양손 각각 외워서: 매번 F♯는 오른손 4번, 왼손 2번.'),
  ('one flat, B♭.', 'row', 'F major with each hand: B♭ under finger 4 (right) and 2 (left) every time.', 'F장조 음계를 양손 각각: 매번 B♭은 오른손 4번, 왼손 2번.'),
  ('Key signature: the whole piece. Accidental: until the bar line.', 'row', 'Someone points to an F in a G major tune: F♯ or F? Say it before they count to 3, then play it.', '누가 G장조 선율의 F를 가리키면 셋 세기 전에: F♯일까요, F일까요? 말하고 쳐요.'),
  ('Count the signs:', 'row', 'Someone covers the names and points to a key signature: say its key before they count to 3.', '누가 이름을 가리고 조표 하나를 가리키면 셋 세기 전에 조 이름을 말해요.'),
 ],
 'tmxLbPages': [
  ('Largo at the bottom, Prestissimo at the top.', 'row', 'Someone calls a speed word: play C D E F G at that speed.', '누가 빠르기말을 부르면 그 빠르기로 C D E F G를 쳐요.'),
  ('accel. faster, rit. slower, a tempo back.', 'row', 'Someone calls "accel.!", "rit.!" or "a tempo!" while you play Cs: change on the very next note.', 'C를 치는 중에 누가 "아첼레란도!", "리타르단도!", "아 템포!"를 외치면 바로 다음 음부터 바꿔요.'),
  ('pp p mp mf f ff.', 'row', 'Someone calls one of the six, pp to ff: play C that loud before they count to 3.', '누가 pp부터 ff까지 여섯 중 하나를 부르면 셋 세기 전에 그 셈여림으로 C를 쳐요.'),
  ('Dots: short. A slur: smooth.', 'row', 'Someone calls "legato!", "staccato!" or "mezzo staccato!" while you play: change on the very next note.', '치는 중에 누가 "레가토!", "스타카토!", "메조 스타카토!"를 외치면 바로 다음 음부터 바꿔요.'),
  ('A little word changes the term beside it', 'row', 'Someone says "poco rit." or "molto rit.": play C D E F G A B C slowing down a little, or a lot.', '누가 "포코 리타르단도"나 "몰토 리타르단도"를 말하면 C D E F G A B C를 조금, 또는 많이 느려지게 쳐요.'),
 ],
 'e8LbPages': [
  ('8 on the bottom: the quaver is one beat.', 'row', 'Six quavers clapped and counted, 1 2 3 4 5 6, louder on 1 and 4: four bars with no slip.', '8분음표 여섯을 1 2 3 4 5 6으로 세며 손뼉, 1과 4는 더 크게: 네 마디를 틀리지 않고.'),
  ('Dotted crotchet in 6/8: 3 beats.', 'row', 'Someone points to a note in 6/8: say how many beats before they count to 3.', '누가 6/8 악보의 음표를 가리키면 셋 세기 전에 몇 박인지 말해요.'),
  ('Crotchet 2 + quaver 1 = 3: long, short.', 'row', 'Long, short on middle C with a lilt, four bars, counting 1 (2) 3, 4 (5) 6.', '가운데 도로 길게-짧게를 흔들리듯이 네 마디, 1 (2) 3, 4 (5) 6으로 세며.'),
  ('3/4: in twos, three beats.', 'row', 'Your teacher plays six quavers grouped one way or the other: say 3/4 or 6/8.', '선생님이 8분음표 여섯을 한쪽 묶음으로 쳐요: 3/4일까요, 6/8일까요?'),
  ('Find the counts, say them, clap, play.', 'row', 'A new line in 6/8: say the counts, clap it, then play it on middle C, with no stop.', '6/8의 새 줄: 셈을 말하고, 손뼉 치고, 가운데 도로 쳐요. 멈춤 없이.'),
 ],
 'ivxLbPages': [
  ('Count both notes: the lower note is 1.', 'row', 'Someone plays two white keys: count both notes and say the interval before they count to 3.', '누가 흰건반 두 개를 치면 두 음을 모두 세어, 셋 세기 전에 몇 도인지 말해요.'),
  ('Thumb and finger 5: a 5th.', 'row', 'In C position, someone calls a number from 2 to 5: play that interval with the thumb and the right finger.', 'C 자리에서 누가 2에서 5 사이 숫자를 부르면, 엄지와 알맞은 손가락으로 그 음정을 쳐요.'),
  ('An octave: the same letter', 'row', 'Someone calls "6th!", "7th!" or "octave!": play it up from C before they count to 3.', '누가 "6도!", "7도!", "옥타브!"를 외치면 셋 세기 전에 C에서 위로 쳐요.'),
  ('Melodic: one after the other. Harmonic: together.', 'row', 'Someone plays an interval: say "melodic!" or "harmonic!" before they count to 3.', '누가 음정을 치면 셋 세기 전에 "선율적!" 또는 "화성적!"'),
  ('From the tonic: 2nd, 3rd, 6th, 7th major', 'time', 'G with each note of G major above it, naming each one, major 2nd to octave: how fast with no slip?', 'G와 그 위의 G장조 음을 하나씩, 장2도부터 완전8도까지 이름을 말하며: 틀리지 않고 얼마나 빨리?'),
 ],
 'chxLbPages': [
  ('Skip a letter, skip a letter', 'time', 'The triad on every white key from C up to B, saying its letters: how fast with no slip?', 'C부터 B까지 흰건반마다 3화음, 음이름을 말하며: 틀리지 않고 얼마나 빨리?'),
  ('Major: 4 + 3. Minor: 3 + 4.', 'row', 'Someone plays a triad: say "major!" or "minor!" before they count to 3.', '누가 3화음을 치면 셋 세기 전에 "장3화음!" 또는 "단3화음!"'),
  ('The tonic triad: the scale', 'row', 'Someone names C, G, D or F major: play its tonic triad before they count to 3.', '누가 C, G, D, F장조 중 하나를 말하면 셋 세기 전에 으뜸화음을 쳐요.'),
  ('I, IV, V: the triads on the 1st, 4th and 5th notes.', 'row', 'In C major, someone calls "I!", "IV!" or "V!": play that triad before they count to 3.', 'C장조에서 누가 "I!", "IV!", "V!"를 외치면 셋 세기 전에 그 3화음을 쳐요.'),
  ('Blocked: together. Broken: one after the other.', 'row', 'Left hand blocked, right hand broken: C, F, G, C, with no stop.', '왼손은 함께, 오른손은 펼쳐서 C, F, G, C, 멈춤 없이.'),
 ],
 'fmxLbPages': [
  ('A phrase ends on a resting note.', 'row', 'Someone plays a tune: lift a hand at each resting note, where a phrase ends.', '누가 선율을 치면, 프레이즈가 끝나는 쉬는 음마다 손을 들어요.'),
  ('Same music, same letter.', 'row', 'Someone plays two phrases: say "same!" or "different!" before they count to 3.', '누가 프레이즈 두 개를 치면 셋 세기 전에 "같아!" 또는 "달라!"'),
  ('Binary: A B.', 'row', 'The binary picture with both repeats, saying A A B B, with no wrong turn.', '2부 형식 그림을 도돌이표대로, A A B B를 말하며, 길을 틀리지 않고.'),
  ('Ternary: A B A.', 'row', 'Play A, make up a new B, then A again, with no stop between.', 'A를 치고, 새 B를 지어 치고, 다시 A를, 사이에 멈춤 없이.'),
  ('Find the sections, give the letters, name the form.', 'row', 'Someone plays a piece you know: call out each section\'s letter as it starts.', '누가 아는 곡을 치면, 부분이 시작될 때마다 글자를 외쳐요.'),
 ],
}
WRAP = {'sacLbPages': 'X', 'skgLbPages': 'X', 'tmxLbPages': 'X', 'ivxLbPages': 'X', 'chxLbPages': 'X', 'fmxLbPages': 'X'}   # these books write text with their own X()
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
# the Form book's check-up page: its steps are on pages 2 to 6
old = "<LbSay>{t('Show each one at the piano, on its page (1 to 5). The check-up on paper is in the Workbook.', '1~5쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>"
assert s.count(old) == 1
s = s.replace(old, old.replace('(1 to 5)', '(2 to 6)').replace('1~5쪽', '2~6쪽'))
# five openers (and the terms book's page 2 in Korean) were full before the guess: their pictures may shrink a little in
# print (the frame fits the drawing to the room it has; on screen nothing changes)
for old, new in [
    ("const p1 = <LbLive still={<LbPic h={360}><div role=\"img\" aria-label={t('The circle of fifths", "const p1 = <LbLive still={<LbPic h={scr ? 360 : 320}><div role=\"img\" aria-label={t('The circle of fifths"),
    ("], 380, 6)} live={<TmxMapPad/>}/>;", "], scr ? 380 : 296, 6)} live={<TmxMapPad/>}/>;"),
    ("))], 400, 10)} live={<IvxMapPad/>}/>;", "))], scr ? 400 : 340, 10)} live={<IvxMapPad/>}/>;"),
    ("))], 400, 10)} live={<ChxClockPad/>}/>;", "))], scr ? 400 : 340, 10)} live={<ChxClockPad/>}/>;"),
    ("))], 360, 10)} live={<FmxMapPad/>}/>;", "))], scr ? 360 : 340, 10)} live={<FmxMapPad/>}/>;"),
    ("곡마다 조금씩 달라요.'))}</>)], 380, 8, 560);", "곡마다 조금씩 달라요.'))}</>)], scr ? 380 : 366, 8, 560);"),
]:
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)

open(dst, 'w', encoding='utf-8').write(s)
print('ok', added, 'last beat id', beat)
