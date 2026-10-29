import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
# Build CU, part 2 (her 12:51 'then the next ones'): the challenges and the guess for the second half of the Beginner floor:
# chapters 8 Dynamics & Articulation, 9 The Staff & the Two Clefs, 10 Steps & Skips, 11 Line and Space Names,
# 12 Time Signatures, 13 Tones & Semitones. Same shape as chapters 1 to 7 (patch768).
G = {
 'sdyLbPages': (['Which one means loud: piano or forte?', '피아노와 포르테 중 어느 게 "세게"일까요?'], ['Forte. Piano means soft.', '포르테예요. 피아노는 "여리게".'], 2),
 'sfLbPages': (['Clara can be written in two places on paper. How many keys is that on the piano?', '클라라는 종이에서 두 자리에 쓸 수 있어요. 피아노에서는 건반 몇 개일까요?'], ['One: the same middle C.', '하나예요. 같은 가운데 도.'], 6),
 'sskLbPages': (['On the staff, does a skip go from a line to the next line, or to the next space?', '오선에서 건너뛰기는 줄에서 다음 줄로 갈까요, 다음 칸으로 갈까요?'], ['To the next line (space to space too): one letter jumped over.', '다음 줄이에요(칸에서는 다음 칸): 글자 하나를 넘어가요.'], 3),
 'wsLbPages': (['Line 2 is G in the treble clef. What is it in the bass clef?', '2번 줄은 높은음자리표에서 G예요. 낮은음자리표에서는?'], ['B. So check the clef first.', 'B예요. 그래서 음자리표부터 봐요.'], 2),
 'tsLbPages': (['In 3/4, how many beats are in every bar?', '3/4에서는 마디마다 몇 박일까요?'], ['Three: the top number.', '세 박: 위의 숫자예요.'], 3),
 'tnLbPages': (['Is there always a black key between two white keys?', '흰건반 두 개 사이에는 늘 검은건반이 있을까요?'], ['No: E F and B C have none, only a half step.', '아니요. E F와 B C 사이에는 없어요: 반음뿐.'], 4),
}
C = {
 'sdyLbPages': [
  ("soft, {dm('f')} loud.", 'row', 'Someone calls "p!" or "f!": play middle C that loud before they count to 3.', '누가 "p!" 또는 "f!" 하면 셋 세기 전에 그 셈여림으로 가운데 도를 쳐요.'),
  ('m means medium. The same letter twice means very.', 'row', 'pp, p, mf, f on one key: four loudnesses, no two the same.', '건반 하나로 pp, p, mf, f: 네 가지 크기, 같은 것 둘 없이.'),
  ('Opening: louder. Closing: softer.', 'row', 'C D E F G getting louder, G F E D C getting softer, with no sudden jump.', 'C D E F G는 점점 세게, G F E D C는 점점 여리게, 갑자기 튀는 음 없이.'),
  ('Legato joins. Staccato bounces.', 'row', 'Someone calls "legato!" or "staccato!" while you play: change on the very next note.', '치는 중에 누가 "레가토!"나 "스타카토!"를 외치면 바로 다음 음부터 바꿔요.'),
  ('Different notes: a slur. The same note: a tie.', 'row', 'Someone points to a curve: say "slur!" or "tie!" before they count to 3.', '누가 곡선을 가리키면 셋 세기 전에 "이음줄!" 또는 "붙임줄!".'),
 ],
 'sfLbPages': [
  ('On a line: the line runs through it.', 'row', 'The hand staff with no slip: line or space, and which number.', '손 오선 게임을 틀리지 않고: 줄인지 칸인지, 몇 번인지.'),
  ('Line to space: a step.', 'time', 'C D E F G and back, then the skips C E G E C: how fast with no wrong key?', 'C D E F G 갔다 오고, 이어서 건너뛰기 C E G E C: 틀린 건반 없이 얼마나 빨리?'),
  ('The curl wraps round G', 'row', 'Someone points to one of the Queen\'s five: name it and play it before they count to 3.', '누가 여왕의 다섯 음 중 하나를 가리키면, 셋 세기 전에 이름을 말하고 쳐요.'),
  ('The two dots guard F', 'row', 'Someone points to one of the King\'s five: name it and play it before they count to 3.', '누가 왕의 다섯 음 중 하나를 가리키면, 셋 세기 전에 이름을 말하고 쳐요.'),
  ('Clara lives between the Queen and the King', 'row', 'Someone writes Clara under the top staff or over the bottom one: play middle C with the right hand for the Queen\'s, the left for the King\'s.', '누가 클라라를 위 오선 아래나 아래 오선 위에 쓰면, 여왕네면 오른손, 왕네면 왼손으로 가운데 도를 쳐요.'),
 ],
 'sskLbPages': [
  ('Higher on the staff, further right on the keys.', 'row', 'Say each move before you play it, up, down or the same, through a whole tune with no slip.', '치기 전에 움직임을 먼저 말하기: 위, 아래, 같은 음. 곡 하나를 틀리지 않고.'),
  ('The next white key: a step. Jump one: a skip.', 'row', 'Someone points to two notes on the staff: step or skip, before they count to 3.', '누가 오선의 두 음을 가리키면, 셋 세기 전에 한 걸음인지 건너뛰기인지.'),
  ('In a position, a step is the next finger', 'time', 'C D E F G and back with each hand, saying the finger numbers, with no slip.', '양손 각각 C D E F G 갔다 오기, 손가락 번호를 말하며, 틀리지 않고.'),
  ('Same fingers, same shape, a new place.', 'row', '1 2 3 1 3 5 3 1 in C position, then straight on in G position, with no stop.', 'C 자리에서 1 2 3 1 3 5 3 1, 이어서 멈춤 없이 G 자리에서.'),
  ('First note, rhythm, moves, then play.', 'row', 'A new tune: first note, rhythm, moves, then play it through with no stop.', '새 곡: 첫 음, 리듬, 움직임, 그다음 멈춤 없이 끝까지.'),
 ],
 'wsLbPages': [
  ('Clef check first: treble or bass?', 'row', 'The clef check game: the clef first, then the note. Five cards in a row.', '음자리표 확인 게임: 음자리표 먼저, 그다음 음 이름. 카드 다섯 장 연속.'),
  ('Treble clef: Every Good Boy', 'time', 'All nine treble notes out loud: the lines, then the Queen\'s FACE.', '높은음자리 아홉 음을 소리 내어: 줄 먼저, 그다음 여왕의 FACE.'),
  ('Bass clef: the King', 'time', 'All nine bass notes out loud: the dragon\'s lines, then the cows\' spaces.', '낮은음자리 아홉 음을 소리 내어: 용의 줄 먼저, 그다음 소들의 칸.'),
  ('Fold at Clara: G meets F', 'row', 'The mirror walk from middle C: both hands land together on every note.', '가운데 도에서 거울 걷기: 음마다 두 손이 함께 닿게.'),
  ('Find the nearest landmark, then step or skip.', 'row', 'Landmark hop: clef, nearest landmark, step or skip, name, play.', '랜드마크 뛰기: 음자리표, 가장 가까운 랜드마크, 걸음이나 건너뛰기, 이름, 연주.'),
 ],
 'tsLbPages': [
  ('Bar lines make bars.', 'row', 'The bars with the repeat, counting 1 2 3, back to the start with no stop.', '도돌이표까지 1 2 3을 세며 치고, 멈춤 없이 처음으로.'),
  ('Top: beats in a bar.', 'row', 'Someone names a time signature: pat two bars of it, counting, with no wrong number.', '누가 박자표를 말하면 두 마디를 무릎 치며 세요, 틀린 숫자 없이.'),
  ('Beat 1 is strong.', 'row', 'Four bars of 3/4, beat 1 a little louder every time.', '3/4 네 마디, 1박을 매번 조금 더 세게.'),
  ('Notes and rests fill each bar exactly.', 'row', 'Someone points to a bar: add up its notes and rests to the top number.', '누가 마디를 가리키면 음표와 쉼표를 더해 위의 숫자가 되는지 말해요.'),
  ('A tie: play once, hold for both.', 'row', 'Someone plays two bars: thumbs up for a tie (held), thumbs down for no tie (played again).', '누가 두 마디를 치면: 이어서 누르면 엄지 위(붙임줄), 다시 치면 엄지 아래.'),
 ],
 'tnLbPages': [
  ('A semitone is a half step: the very next key', 'time', 'The half-step walk from middle C to the next C, counting the 12 half steps out loud.', '가운데 도에서 다음 C까지 반음 걷기, 반음 12개를 소리 내어 세며.'),
  ('A tone is a whole step: two half steps', 'row', 'Someone plays two keys: half step or whole step?', '누가 건반 두 개를 치면: 반음일까요, 온음일까요?'),
  ('No black key between E F and B C', 'time', 'Every E F and every B C on the piano, bottom to top.', '피아노의 모든 E F와 B C를 아래에서 위로.'),
  ('up a half step, ', 'row', 'Someone names a black key one way (C♯): say its other name (D♭) before they count to 3.', '누가 검은건반 이름 하나(C♯)를 말하면, 셋 세기 전에 다른 이름(D♭)을 말해요.'),
  ('The sign goes just before the note', 'row', 'A note with a sharp or a flat: say the letter, then the sign, then play it.', '샵이나 플랫이 붙은 음: 글자 먼저, 그다음 기호, 그리고 연주.'),
 ],
}
def esc(x): return x.replace('\\', '\\\\').replace("'", "\\'")
def nb(x): return re.sub(r'(?<=(?:^|(?<=[\s(]))[0-9A-G]) (?=[0-9A-G](?:[\s,.:)+]|$))', ' ', x)
def norm(x): return x.replace(' ', ' ')
L = s.split('\n')
for fn in G:
    st = [i for i, l in enumerate(L) if l.startswith('function ' + fn + '(')][0]
    en = next(i for i in range(st + 1, len(L)) if L[i].startswith('function ') and 'LessonBook' in L[i])
    k1 = next(i for i in range(st, en) if '<LbPage key="1"' in L[i])
    sy = next(i for i in range(k1, en) if '</LbSay>' in L[i])
    (qe, qk), (ae, ak), page = G[fn]
    ins = {sy + 1: ["      <LbGuess q={t('%s', '%s')} a={t('%s', '%s')} page={%d}/>" % (esc(nb(qe)), esc(nb(qk)), esc(nb(ae)), esc(nb(ak)), page)]}
    for (m, kind, e, k) in C[fn]:
        hits = [i for i in range(st, en) if '<LbRemember>' in L[i] and m in norm(L[i])]
        assert len(hits) == 1, (fn, m, len(hits))
        ins.setdefault(hits[0], []).append("      <LbChallenge%s>{t('%s', '%s')}</LbChallenge>" % (' kind="time"' if kind == 'time' else '', esc(nb(e)), esc(nb(k))))
    for at in sorted(ins, reverse=True):
        L[at:at] = ins[at]
s = '\n'.join(L)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
