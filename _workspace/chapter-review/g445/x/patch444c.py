#!/usr/bin/env python3
# Phase 444c: sentences the dash rewrite left with two colons, in the finished books (read aloud, one colon each).
import sys
p_in, p_out = sys.argv[1], sys.argv[2]
s = open(p_in, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
rep("<><b>C hop:</b> your teacher points to a ledger note: nearest C → a step or a skip → name it → play it.</>", "<><b>C hop:</b> your teacher points to a ledger note. Nearest C → a step or a skip → name it → play it.</>")
rep("<><b>C에서 뛰기:</b> 선생님이 덧줄 음 하나를 짚으면: 가장 가까운 C →", "<><b>C에서 뛰기:</b> 선생님이 덧줄 음 하나를 짚으면 가장 가까운 C →")
rep("<><b>Landmark hop:</b> your teacher points to a note: crown check →", "<><b>Landmark hop:</b> your teacher points to a note. Crown check →")
rep("<><b>랜드마크 뛰기:</b> 선생님이 음표 하나를 짚으면: 왕관 확인 →", "<><b>랜드마크 뛰기:</b> 선생님이 음표 하나를 짚으면 왕관 확인 →")
rep("{t('At the piano: before you play, every time, tick how each one is going: not yet, nearly, or got it!", "{t('At the piano, before you play, every time, tick how each one is going: not yet, nearly, or got it!")
rep("'피아노 앞에서: 칠 때마다, 치기 전에 먼저, 하나씩 어떤지 표시해요: 아직, 거의, 됐어요!", "'피아노 앞에서, 칠 때마다, 치기 전에 먼저, 하나씩 어떤지 표시해요: 아직, 거의, 됐어요!")
rep("hold one hand out sideways, fingers spread: 5 fingers = 5 lines", "hold one hand out sideways, fingers spread. 5 fingers = 5 lines")
rep("한 손을 옆으로 눕혀 손가락을 벌려요: 손가락 5개 = 줄 5개", "한 손을 옆으로 눕혀 손가락을 벌려요. 손가락 5개 = 줄 5개")
rep('or "whole step, tone": C D, E F, B C, F G, then two black-key pairs:', 'or "whole step, tone": C D, E F, B C, F G. Then two black-key pairs:')
rep('"온 걸음, 온음"이라고 말해요: C D, E F, B C, F G, 그리고 검은건반 짝 둘:', '"온 걸음, 온음"이라고 말해요: C D, E F, B C, F G. 그리고 검은건반 짝 둘:')
rep("black or white, nothing in between: its <b>nearest neighbour</b>, the closest key there is.", "black or white, with nothing in between. It is the key's <b>nearest neighbour</b>, the closest key there is.")
open(p_out, 'w', encoding='utf-8').write(s); print('444c applied')
