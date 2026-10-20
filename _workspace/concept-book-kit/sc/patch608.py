import sys, re
s=open(sys.argv[1],encoding='utf-8').read()
s_count = lambda p: s.count(p)
IDS=['ssc-steps','ssc-fingers','ssc-degrees','ssc-g','ssc-f','major-shape','build-major','degree-names','minor-forms']
L=s.split('\n'); out=[]; removed={'entry':0,'ko':0,'badge':0}
i=0
while i<len(L):
    l=L[i]
    m=re.match(r"^  \{ id: '([a-z-]+)', hidden: true, ch: 'scales',", l)
    if m and m.group(1) in IDS:
        assert l.rstrip().endswith('},'),l[:80]; removed['entry']+=1; i+=1; continue
    m=re.match(r"^  '([a-z-]+)': \['[^\n]*'\],?\s*$", l)
    if m and m.group(1) in IDS:
        removed['ko']+=1; i+=1; continue
    m=re.match(r"^  '([a-z-]+)': \(\) => \($", l)
    if m and m.group(1) in IDS:
        assert L[i+2].strip()=='),',(L[i+2][:60]); removed['badge']+=1; i+=3; continue
    out.append(l); i+=1
s='\n'.join(out)
print(removed)
# maps and lists on single lines
for i_ in IDS:
    s=re.sub(r"'%s': \['scales', \d, \d, '[a-z ]+'\],? ?" % re.escape(i_), '', s)           # tool metadata
    s=re.sub(r"'%s': 'p-scales',? ?" % re.escape(i_), '', s)                                   # TOOL_CONCEPT
    s=re.sub(r"'%s', " % re.escape(i_), "\x00", s) if False else s
# chapter list of 'scales'
a=s.index("  'scales': ['ssc-steps'"); b=s.index("],", a)
seg=s[a:b]
for i_ in IDS: seg=seg.replace("'%s', "%i_,'')
s=s[:a]+seg+s[b:]
# related-tool pairs
for p in ["['major-shape', 'build-major'], ","['minor-fingering', 'minor-forms'], "]:
    assert s.count(p)==1,p; s=s.replace(p,'')
p5 = "['ssc-steps', 'major-shape'], ['ssc-fingers', 'major-fingering'], ['ssc-degrees', 'degree-names'], ['ssc-g', 'build-major'], ['ssc-f', 'scale-finder'], "
assert s_count(p5) == 1; s = s.replace(p5, '')
x = "'ssc-fingers': 'k-play', "; assert s_count(x) == 1; s = s.replace(x, '')
x = "scales: 'build-major', "; assert s_count(x) == 1; s = s.replace(x, "scales: 'scale-finder', ")
# the old concept book page "Every key" now embeds the lesson 9 tool
x="{live(p3, cbTool('build-major'))}"; assert s.count(x)==1; s=s.replace(x,"{live(p3, cbTool('sc-all'))}")
# any id still named anywhere (outside of component code) is reported
for i_ in IDS: print(i_, len(re.findall(r"'%s'"%re.escape(i_), s)))
open(sys.argv[2],'w',encoding='utf-8').write(s)
