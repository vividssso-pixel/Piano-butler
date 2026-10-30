#!/usr/bin/env python3
"""Build DE (on t779 -> t780): the Grades 2 and 3 floors' Lesson Books, fun first, as Beginner (CU), Prelim (CZ) and
Grade 1 (DB): one 'Guess first!' on each opener and one challenge above every step's Remember line. Six rooms:
Ear Training Grade 2 and Grade 3 (one function, l2LbPages, with g = 2 or 3), Melody & Phrasing (9 steps), Scales
further, Intervals and chords further, Rhythm further (its pages come from a helper, pg: the challenge is looked up by
page number). Only what the pages teach; her metaphors where they fit (the bird and the turtle, home, walk / run-ning,
mirror twins). Time challenges get their own ids (beat20 on).
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def esc(x): return x.replace('\\', '\\\\').replace("'", "\\'")
def nb(x): return re.sub(r'(?<=(?:^|(?<=[\s(]))[0-9A-G]) (?=[0-9A-G](?:[\s,.:)+]|$))', ' ', x)
def norm(x): return x.replace(' ', ' ')
beat = max(int(n) for n in re.findall(r'tid="beat(\d+)"', s))
def chal(kind, e, k, w='t'):
    global beat
    if kind == 'time': beat += 1; attr = ' kind="time" tid="beat%d"' % beat
    else: attr = ''
    return "<LbChallenge%s>{%s('%s', '%s')}</LbChallenge>" % (attr, w, esc(nb(e)), esc(nb(k)))
def guess(qe, qk, ae, ak, page, w='t'):
    return "<LbGuess q={%s('%s', '%s')} a={%s('%s', '%s')} page={%d}/>" % (w, esc(nb(qe)), esc(nb(qk)), w, esc(nb(ae)), esc(nb(ak)), page)

G = {
 'mlxLbPages': (['A tune in C major stops on G. Is that a question or an answer?', 'C장조 선율이 G에서 멈춰요. 질문일까요, 대답일까요?'], ['A question: it has not come home to C.', '질문이에요. 아직 집인 C로 돌아오지 않았어요.'], 4, 'X'),
 'scfLbPages': (['B♭ major, right hand: which finger plays the first key?', 'B♭장조 오른손: 첫 건반은 몇 번 손가락일까요?'], ['Finger 2. The thumb takes the first white key.', '2번이에요. 엄지는 처음 나오는 흰건반에.'], 2, 't'),
 'h3LbPages': (['In a minor key, the 3rd above the tonic: major or minor?', '단조에서 으뜸음 위의 3도는 장3도일까요, 단3도일까요?'], ['Minor. The 6th too.', '단3도예요. 6도도 단음정.'], 2, 't'),
 'r2LbPages': (['Four semiquavers under two beams: how many beats?', '빔 두 개로 묶인 16분음표 넷: 몇 박일까요?'], ['One beat, shared four ways: 1 e + a.', '한 박을 넷이 나눠요: 1 e + a.'], 2, 't'),
}
C = {
 'mlxLbPages': [
  ('The line goes where the notes go.', 'row', 'Your teacher plays a tune: draw its line in the air and point to where the high point was, before they count to 3.', '선생님이 선율을 치면 셋 세기 전에 공중에 선율선을 그리고 가장 높은 음이 어디였는지 가리켜요.'),
  ('A phrase often gets louder to its high point', 'row', 'Someone plays a phrase shaped or flat: say "shaped!" or "flat!" before they count to 3.', '누가 프레이즈를 모양을 살려 치거나 밋밋하게 치면 셋 세기 전에 "모양!" 또는 "밋밋!"'),
  ('A question ends away from the tonic', 'row', 'Someone plays a phrase: say "question!" or "answer!" before they count to 3.', '누가 프레이즈를 치면 셋 세기 전에 "질문!" 또는 "대답!"'),
  ('A motif is a short idea that comes back.', 'row', 'Your teacher plays a tune: clap each time the motif comes back, with none missed.', '선생님이 선율을 치면 동기가 돌아올 때마다 손뼉, 하나도 놓치지 않고.'),
  ('Same notes: repetition. Same shape, new start: sequence.', 'row', 'Someone plays a motif twice: say "repetition!" or "sequence!" before they count to 3.', '누가 동기를 두 번 치면 셋 세기 전에 "반복!" 또는 "동형 진행!"'),
  ('Strong syllables on strong beats', 'row', 'Someone says a couplet you have not seen: clap on every strong syllable, with no slip.', '누가 처음 보는 두 줄 시를 말하면 센 음절마다 손뼉, 틀리지 않고.'),
  ('Bars 1 and 2 ask; bars 3 and 4 answer', 'row', 'Make up a four-bar tune on the spot: bars 1 and 2 ask, bars 3 and 4 come home. A new one each time.', '즉석에서 네 마디 선율 짓기: 1·2마디는 묻고, 3·4마디는 집으로. 매번 새로.'),
  ('The words set the rhythm. Line 1 asks', 'row', 'Someone says a new couplet: sing it to a tune of your own that comes home at the end of line 2.', '누가 새 두 줄 시를 말하면 나만의 선율로 불러요. 둘째 줄 끝에서 집으로.'),
  ('Four lines, one way home', 'row', 'Play your stanza tune: someone says where lines 1 to 3 rest, and that line 4 comes home.', '내가 쓴 네 줄 시 선율을 쳐요: 듣는 사람이 1~3줄이 쉬는 곳과 4줄이 집으로 오는 것을 말해요.'),
 ],
 'scfLbPages': [
  ('Black key first? Finger 2', 'time', 'B♭ major, right hand, two octaves up and down from memory: how fast with no wrong finger?', 'B♭장조 오른손 두 옥타브 올라갔다 내려오기, 외워서: 틀린 손가락 없이 얼마나 빨리?'),
  ('The thumbs never meet?', 'row', 'B♭ major, hands together, two octaves, while someone listens for a bump at a turn: even all the way.', 'B♭장조 양손 함께 두 옥타브, 누가 넘기는 곳의 덜컹을 들어요: 끝까지 고르게.'),
  ('Up: 6 and 7 rise. Down: natural.', 'row', 'Someone names G or C minor: play its melodic minor, one octave, the 6th and 7th rising only on the way up.', '누가 G단조나 C단조를 말하면 가락 단음계 한 옥타브: 6과 7은 올라갈 때만 올려요.'),
  ('Each hand keeps its own numbers.', 'row', 'Someone names D or B♭ major: contrary motion, one octave, then say "twins!" or "not twins!" for the numbers.', '누가 D장조나 B♭장조를 말하면 반대 방향 한 옥타브, 그다음 번호가 "쌍둥이!"인지 "아니!"인지.'),
  ('3 on black, 1 on white', 'time', 'The chromatic scale from any note someone calls, right hand, one octave up and down: how fast with 3 only ever on a black key?', '누가 부르는 음에서 반음계, 오른손 한 옥타브 올라갔다 내려오기: 3번이 검은건반만 치면서 얼마나 빨리?'),
 ],
 'h3LbPages': [
  ('Minor key: the 3rd and 6th go minor.', 'row', 'Someone plays a 3rd or a 6th above A: say "major!" or "minor!" before they count to 3.', '누가 A 위의 3도나 6도를 치면 셋 세기 전에 "장!" 또는 "단!"'),
  ('Dominant: 5 up. Subdominant: 5 down.', 'row', 'Someone calls a degree name, tonic to leading note: play that note of C major before they count to 3.', '누가 으뜸음부터 이끎음까지 이름 하나를 부르면 셋 세기 전에 C장조의 그 음을 쳐요.'),
  ('First inversion: the 3rd at the bottom.', 'row', 'Someone calls "root position!" or "first inversion!": play C major\'s I that way before they count to 3.', '누가 "기본 위치!" 또는 "제1전위!"를 외치면 셋 세기 전에 C장조 I을 그렇게 쳐요.'),
  ('Treble: soprano up, alto down.', 'row', 'Someone names a voice, soprano to bass: point to its staff and say "stems up" or "stems down" before they count to 3.', '누가 소프라노부터 베이스까지 성부 하나를 말하면 셋 세기 전에 그 오선을 가리키고 "기둥 위" 또는 "기둥 아래".'),
  ('V–I perfect, IV–I plagal.', 'row', 'Someone plays a cadence in C: say "perfect!" or "plagal!" before they count to 3.', '누가 C장조 종지를 치면 셋 세기 전에 "정격!" 또는 "변격!"'),
 ],
}
R2 = {   # the Rhythm further book builds its pages with pg(no, …): a challenge per page number
 2: ('row', 'Someone claps a slow beat: fit four even semiquavers inside each one, 1 e + a, four beats in a row.', '누가 느린 박을 치면 그 안에 고른 16분음표 넷, 1 e + a, 네 박 연속.'),
 3: ('row', 'Long, short, four bars in a row, counting 1 e + a: the short note on a, never early.', '길게 짧게를 네 마디 연속, 1 e + a를 세며: 짧은 음은 a에, 절대 일찍 치지 않게.'),
 4: ('row', 'Someone calls "two!" or "three!": clap that many even notes inside the next beat.', '누가 "둘!" 또는 "셋!"을 외치면 다음 박 안에 그만큼의 고른 음을 손뼉 쳐요.'),
 5: ('row', 'Someone shows a bar in 2/2 or 3/2: count it out loud with the minim as the beat, before they count to 3.', '누가 2/2나 3/2 마디를 보여 주면 셋 세기 전에 2분음표를 1박으로 소리 내어 세요.'),
 6: ('row', 'Someone shows a bar in 3/8 or 9/8: say which, then count its quavers out loud, leaning on 1 (and on 4 and 7 in 9/8).', '누가 3/8이나 9/8 마디를 보여 주면 어느 쪽인지 말하고 8분음표를 소리 내어 세요. 1에 힘을 주고(9/8은 4와 7에도).'),
}
L2 = {   # the ear rooms, Grade 2 (dyad, clap, sing) and Grade 3 (any, deg, metre, clap, sing)
 'Two at once: pick one out and hum it.': ('row', 'Your teacher plays two notes together: hum the one they ask for, the bird\'s or the turtle\'s.', '선생님이 두 음을 함께 치면 묻는 음을 흥얼거려요: 새 쪽이나 거북이 쪽.'),
 'Close or far: follow just one.': ('row', 'Your teacher plays any two notes together, close ones too: hum the one they ask for.', '선생님이 어떤 두 음이든 함께 쳐요, 가까운 음도: 묻는 음을 흥얼거려요.'),
 'Sing up from home until you meet it.': ('row', 'Your teacher plays the keynote and another note: sing up from home and name it, 2nd to 5th.', '선생님이 으뜸음과 다른 음을 치면 집에서부터 올라가며 불러 이름을 말해요: 2도부터 5도까지.'),
 'Oom-pah: two. Oom-pah-pah: three.': ('row', 'Your teacher plays an accompaniment: say "two!" or "three!" before the second bar ends.', '선생님이 반주를 치면 둘째 마디가 끝나기 전에 "두 박!" 또는 "세 박!"'),
 "Clap it back, then say two or three.": ('row', None, None),   # per grade, below
 'Longer, with skips: the notes and the rhythm, both.': ('row', 'Your teacher plays a longer tune twice: sing it back on "la", the skips and the rhythm too.', '선생님이 더 긴 선율을 두 번 치면 "라"로 따라 불러요, 건너뛰는 음도 리듬도.'),
}
L2_CLAP = ("g === 3 ? t('Your teacher claps four bars twice: clap them back, then say two or three.', '선생님이 네 마디를 두 번 치면 따라 치고, 두 박인지 세 박인지 말해요.')"
           " : t('Your teacher claps four bars twice: clap them back at the same speed, long and short in their places.', '선생님이 네 마디를 두 번 치면 같은 빠르기로 따라 쳐요, 길게 짧게도 제자리에.')")
L2_GUESS = ("{g === 3 ? " + guess('Two notes together, close or far apart: which pair is harder to pick one from?', '함께 울리는 두 음, 가까운 쌍과 먼 쌍: 어느 쪽에서 하나를 골라내기가 더 어려울까요?', 'The close ones.', '가까운 쌍이에요.', 2)
            + " : " + guess('Two notes sound together. Can you hum just one of them?', '두 음이 함께 울려요. 그중 하나만 흥얼거릴 수 있을까요?', 'Yes: the higher (the bird\'s) or the lower (the turtle\'s).', '네. 높은 음(새 쪽)이나 낮은 음(거북이 쪽).', 2) + "}")

L = s.split('\n')
def span(fn):
    st = [i for i, l in enumerate(L) if l.startswith('function ' + fn + '(')][0]
    en = next(i for i in range(st + 1, len(L)) if L[i].startswith('function ') and 'LessonBook' in L[i])
    return st, en
def first_say(st, en):
    k1 = next(i for i in range(st, en) if '<LbPage key="1"' in L[i])
    return next(i for i in range(k1, en) if '</LbSay>' in L[i])
added = []
for fn in G:
    st, en = span(fn)
    (qe, qk), (ae, ak), page, w = G[fn]
    ins = {first_say(st, en) + 1: ['      ' + guess(qe, qk, ae, ak, page, w)]}
    for (m, kind, e, k) in C.get(fn, []):
        hits = [i for i in range(st, en) if '<LbRemember>' in L[i] and m in norm(L[i])]
        assert len(hits) == 1, (fn, m, len(hits))
        ins.setdefault(hits[0], []).append('      ' + chal(kind, e, k, w))
    for at in sorted(ins, reverse=True): L[at:at] = ins[at]
    added.append((fn, len(C.get(fn, []))))
# Rhythm further: the challenge by page number, inside pg
st, en = span('r2LbPages')
i = next(i for i in range(st, en) if L[i].strip() == '<LbPiano steps={LANG === \'ko\' ? pianoKo : pianoEn}/>')
L[i + 1:i + 1] = ['    {R2_CHAL[no]}']
j = next(i for i in range(st, en) if L[i].strip().startswith('const pg = '))
L[j:j] = ['  const R2_CHAL = { ' + ', '.join('%d: %s' % (n, chal(k, e, ko)) for n, (k, e, ko) in R2.items()) + ' };   // Build DE']
added.append(('r2LbPages', len(R2)))
# the ear rooms
st, en = span('l2LbPages')
ins = {first_say(st, en) + 1: ['      ' + L2_GUESS]}
for m, (kind, e, k) in L2.items():
    hits = [i for i in range(st, en) if '<LbRemember>' in L[i] and m in norm(L[i])]
    assert len(hits) == 1, (m, len(hits))
    ins.setdefault(hits[0], []).append('      ' + ('<LbChallenge>{' + L2_CLAP + '}</LbChallenge>' if e is None else chal(kind, e, k)))
for at in sorted(ins, reverse=True): L[at:at] = ins[at]
added.append(('l2LbPages', len(L2)))
s = '\n'.join(L)
# the Melody opener was full: its map may shrink a little in print (on screen nothing changes)
old = "], 380, 10)} live={<MlxMapPad"
assert s.count(old) == 1
s = s.replace(old, "], scr ? 380 : 270, 10)} live={<MlxMapPad")

open(dst, 'w', encoding='utf-8').write(s)
print('ok', added, 'last beat id', beat)
