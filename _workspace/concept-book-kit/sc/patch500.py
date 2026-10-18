#!/usr/bin/env python3
# Phase 500: (her 2026-10-19 09:22) the staff moves with the zigzag (numbers over the sharps, the newest one stronger),
# and 'Free play' is renamed everywhere ('Explore' / '더 둘러보기').
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)
rep("<KSStaff count={lit} type={type} width={200}/>", "<KSStaff count={lit} type={type} width={200} numbers={ran} upto={ran && lit > 0 ? lit - 1 : undefined}/>")
rep("t('Free play', '자유롭게')", "t('Explore', '더 둘러보기')", 2)
rep("Free play for any scale, major or minor.", "Explore any scale, major or minor.")
rep("맨 아래 “자유롭게”에서는", "맨 아래 “더 둘러보기”에서는")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
