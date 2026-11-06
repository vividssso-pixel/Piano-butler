import json, re, sys
B = '/home/claude/pbtest/g460/'
s = open(B + 'base.src.html').read()
chs = ['posture-hands', 'first-steps', 'pulse', 'note-names', 'staff', 'whole-staff', 'tones', 'ledger-lines']
guides = {'posture-hands': 'posture-hands', 'first-steps': 'first-steps', 'pulse': 'pulse', 'note-names': 'note-names', 'staff': 'staff', 'tones': 'tones', 'ledger-lines': 'ledger-lines'}
bad = 0
for ch in chs:
    d = json.load(open(B + ch + '.json'))
    for i, r in enumerate(d['book']):
        n = s.count(r['old'])
        if n != 1:
            print('BOOK FAIL', ch, i, n, r['old'][:80]); bad += 1; continue
        s = s.replace(r['old'], r['new'])
    if ch in guides:
        g = open(B + 'guide/' + guides[ch] + '.html').read()
        for i, r in enumerate(d['guide']):
            n = g.count(r['old'])
            if n != 1:
                print('GUIDE FAIL', ch, i, n, r['old'][:80]); bad += 1; continue
            g = g.replace(r['old'], r['new'])
        open(B + 'out/' + guides[ch] + '.html', 'w').write(g)
# one check-up sentence for every book
CIRC_EN = 'Show each one at the piano. Colour a circle: not yet, nearly, or got it! The check-up on paper is in the Workbook.'
CIRC_KO = '피아노 앞에서 하나씩 보여 줘요. 동그라미를 칠해요: 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.'
TICK_EN = 'Show each one at the piano. Tick: not yet, nearly, or got it! The check-up on paper is in the Workbook.'
TICK_KO = '피아노 앞에서 하나씩 보여 줘요. 표시해요: 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.'
pat = re.compile(r"<LbSay>\{t\('((?:Show each one|At the piano: show each one|At the piano, show each one)[^']*)', '([^']*)'\)\}</LbSay>")
def fix(m):
    tick = 'tick' in m.group(1).lower()
    return "<LbSay>{t('%s', '%s')}</LbSay>" % ((TICK_EN, TICK_KO) if tick else (CIRC_EN, CIRC_KO))
s, k = pat.subn(fix, s)
print('check-up sentences unified:', k)
assert s.count('The paper check-up is in the Workbook.') == 1
s = s.replace('The paper check-up is in the Workbook.', 'The check-up on paper is in the Workbook.')
open(B + 'out/t460a.src.html', 'w').write(s)
print('fails', bad)
