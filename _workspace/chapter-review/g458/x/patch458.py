#!/usr/bin/env python3
# Phase 458 (her 2026-10-13 20:45 '전체적으로 american 북은 이렇게 부른다는 내용은 빼고 다른 이름으로는 이렇게 부른다라고
# 하는게 좋겠어'): a second name is 'its other name', never whose books use it. Chapter 11's book (pages 2 and 3), its two
# old tool tips and its Teacher copy.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
rep("이 걸음의 이름이 <b>반음</b>이에요. 영어로는 <b>semitone</b>(호주·영국 책)이라고도, <b>half step</b>(미국 책)이라고도 해요. 같은 걸음이에요. ",
    "이 걸음의 다른 이름은 <b>반음</b>이에요. ")
rep("Its other name is a <b>semitone</b> (<i>semi</i> means half): Australian and British books say semitone, American books say half step. The same step. ",
    "Its other name is a <b>semitone</b> (<i>semi</i> means half). ")
rep("이 걸음의 이름이 <b>온음</b>이에요. 영어로는 <b>tone</b>, 미국 책에서는 <b>whole step</b>이라고 해요. ",
    "이 걸음의 다른 이름은 <b>온음</b>이에요. ")
rep("Its other name is a <b>tone</b>; American books say whole step. ", "Its other name is a <b>tone</b>. ")
rep("C to C♯ is a semitone. In American books it’s called a half step.', '검은건반이든 흰건반이든, 바로 옆에 있는 건반이에요. C에서 C♯까지가 반음이에요. 미국 책에서는 half step이라고도 해요.'",
    "C to C♯ is a semitone. Its other name is a half step.', '검은건반이든 흰건반이든, 바로 옆에 있는 건반이에요. C에서 C♯까지가 반음이에요. 다른 이름은 반 걸음이에요.'", 2)
rep("The book teaches both pairs of names: semitone and tone (Australian and British books, AMEB), half step and whole step (American books); either is right.",
    "The book teaches both pairs of names, semitone and tone, half step and whole step; either is right.")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
