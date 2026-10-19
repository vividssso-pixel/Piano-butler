import sys
s=open(sys.argv[1],encoding='utf-8').read().split('\n')
out=[];i=0;moved=0
# for every JSX block that has a titleStyle line and a lineStyle line, put the lineStyle line right after the title (and the Example caption, if any)
start=[k for k,l in enumerate(s) if l.startswith('function AcStep(')][0]
end=[k for k,l in enumerate(s) if l.startswith('// the Toolbox: a concept')][0]
region=s[start:end]
res=[];blk=[]
def flush(blk):
    global moved
    ti=[k for k,l in enumerate(blk) if '<div style={titleStyle}>' in l]
    li=[k for k,l in enumerate(blk) if '<div style={lineStyle}>' in l]
    if ti and li and li[0]>ti[0]:
        line=blk.pop(li[0]); at=ti[0]+1
        if at<len(blk) and 'Example ' in blk[at] and 'fontSize:12' in blk[at]: at+=1
        blk.insert(at,line); moved+=1
    return blk
for l in region:
    if l.strip().startswith('body = <>') or l.strip().startswith('} else {') or l.strip().startswith('} else if'):
        res+=flush(blk); blk=[l]
    else: blk.append(l)
res+=flush(blk)
s=s[:start]+res+s[end:]
print('moved',moved)
open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(s))
