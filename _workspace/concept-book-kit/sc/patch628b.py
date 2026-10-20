import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
rep("\nconst KS_ROWS = [", open('/home/claude/pbtest/sc/ks2.jsx', encoding='utf-8').read() + "\nconst KS_ROWS = [")
rep("  ['p-keys', [\n", "  ['p-keys', [\n    ['kp-groups', 'Black keys in twos and threes', '검은건반은 두 개, 세 개씩', 'The black keys sit in groups of 2 and 3.', '검은건반은 두 개, 세 개씩 모여 있어요.', () => <KpGroups/>],\n")
rep("lessons: ['kp-hear', 'kp-houses'", "lessons: ['kp-groups', 'kp-hear', 'kp-houses'")
open(bb, 'w', encoding='utf-8').write(s)
