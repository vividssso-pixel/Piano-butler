import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
blk = open('/home/claude/pbtest/sc/ks1.jsx', encoding='utf-8').read()
rep("\nconst KS_ROWS = [", blk + "\nconst KS_ROWS = [")
# keyboard patterns: her three lessons rebuilt, the whole piano and the song are her tools as they are
def swap(id_, comp):
    global s
    i = s.index("    ['" + id_ + "', "); j = s.index("\n", i)
    line = s[i:j]
    k = line.index("ksL(")
    s = s[:i] + line[:k] + comp + "],"+ s[j:]
swap('kp-hear', "() => <KpHear/>")
swap('kp-houses', "() => <KpHouses/>")
swap('kp-white', "() => <KpWhite/>")
swap('kp-piano', "() => <WholePiano/>")
swap('kp-song', "() => <BlackKeySong/>")
open(bb, 'w', encoding='utf-8').write(s)
