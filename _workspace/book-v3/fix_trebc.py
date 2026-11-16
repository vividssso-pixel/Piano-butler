# Her 16 Nov: "Find Bass C and Treble C" ended on Treble C, so its pair of black keys was off the picture.
# Two more white keys (C# D# on top) after Treble C, so the pair you walk to is there to see.
import sys
W = '<rect x="{x}" y="0" width="48" height="176" fill="#fff" stroke="#26296b" stroke-width="1.4"></rect>'
def fix(s):
    tail = '<rect x="610.1" y="0" width="27.8" height="105.6" rx="1.5" fill="#26296b"></rect><rect x="0" y="0" width="720" height="176" fill="none"'
    if tail not in s: return s, 0
    n = s.count(tail)
    add = W.format(x=720) + W.format(x=768)
    s = s.replace('<rect x="672" y="0" width="48" height="176" fill="#fff" stroke="#26296b" stroke-width="1.4"></rect><rect x="34.1"', '<rect x="672" y="0" width="48" height="176" fill="#fff" stroke="#26296b" stroke-width="1.4"></rect>' + add + '<rect x="34.1"')
    s = s.replace(tail, '<rect x="610.1" y="0" width="27.8" height="105.6" rx="1.5" fill="#26296b"></rect><rect x="706.1" y="0" width="27.8" height="105.6" rx="1.5" fill="#26296b"></rect><rect x="754.1" y="0" width="27.8" height="105.6" rx="1.5" fill="#26296b"></rect><rect x="0" y="0" width="816" height="176" fill="none"')
    s = s.replace('viewBox="-32.0 -2 784.0 208.0"', 'viewBox="-32.0 -2 880.0 208.0"')
    return s, n
for f in sys.argv[1:]:
    s, n = fix(open(f).read()); open(f, 'w').write(s); print(f, n)
# JSON files (pitch-pilot.json, lvl/blocks*.json) were patched by walking their strings with fix().
