#!/usr/bin/env python3
# Phase 443: 'Clara', not 'Princess Clara' (her 15:59-16:02: '공주는 너무 좀 오글거려서' ... '공주인데 프린세스 클라라 라고 계속
# 안해도 되는거정도로 하자'). She is still a princess (the tiara stays, the royal family stays) -- the book says so once,
# where she first appears (the Musical Alphabet, 'Clara, a little princess'); everywhere else she is just Clara / 클라라.
# The student is always 'you': the week board without a linked name says 'My week' / '나의 일주일', not 'Clara's week'.
#   python3 patch443.py <in.src.html> <out.src.html>
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('found %d (want %d): %s' % (c, n, a[:100]))
    s = s.replace(a, b)
# her first appearance: said once
rep("In the small house lives <b>Princess Clara</b>, at the left door (<b>C</b>),", "In the small house lives <b>Clara</b>, a little princess, at the left door (<b>C</b>),")
rep("작은 집에는 왼쪽 문에 <b>클라라 공주(Princess Clara)</b>, <b>C</b>가 살고", "작은 집에는 왼쪽 문에 꼬마 공주 <b>클라라(Clara)</b>, <b>C</b>가 살고")
rep("'C -- 클라라 공주(Princess Clara): 작은 집의 왼쪽 문.'", "'C -- 클라라(Clara): 작은 집의 왼쪽 문.'")
# English: every other 'Princess Clara' -> 'Clara'
n_en = s.count('Princess Clara'); s = s.replace('Princess Clara', 'Clara')
# Korean: '클라라 공주' -> '클라라', then the bare '공주' that means her -> '클라라' (Scarlatti's Portuguese princess stays)
n_ko1 = s.count('클라라 공주'); s = s.replace('클라라 공주', '클라라')
keep = ['포르투갈 공주', '그 공주는 나중에', '꼬마 공주 <b>클라라']
for i, k in enumerate(keep): s = s.replace(k, '\u0002%d\u0002' % i)
n_ko2 = s.count('공주'); s = s.replace('공주', '클라라')
for i, k in enumerate(keep): s = s.replace('\u0002%d\u0002' % i, k)
# the week board: the student is 'you' (her 15:59: Clara would be a third person)
rep("const tx = bx + bw + 22, who = name || 'Clara';", "const tx = bx + bw + 22, who = name;")
rep("s += stT(tx, 24, t(who + '’s week', who + '의 일주일'),", "s += stT(tx, 24, who ? t(who + '’s week', who + '의 일주일') : t('My week', '나의 일주일'),")
rep("aria-label={t((name || 'Clara') + '’s week: '", "aria-label={t((name ? name + '’s week' : 'My week') + ': '")
rep("(name || '클라라') + '의 일주일: ", "(name ? name + '의 일주일' : '나의 일주일') + ': ")
assert 'Princess Clara' not in s and '클라라 공주' not in s
left = [m.group(0) for m in re.finditer(r'.{0,20}공주.{0,10}', s)]
open(dst, 'w', encoding='utf-8').write(s)
print('443 applied: en %d, ko %d + %d; 공주 left: %s' % (n_en, n_ko1, n_ko2, left))
