# Her 18 Nov ("힌트를 하나씩"): find the numbered hint steps (orange 1 2 3 circles) and the answer strip on every pop-up picture,
# so Read & listen can hide the hints and reveal them one at a time during "Pause and try", and keep the answer line back until it is said.
import glob, json, os, numpy as np
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); P=os.path.join(D,'../../books/read/pops')
def blobs(mask):
    H,W=mask.shape; seen=np.zeros_like(mask); out=[]
    ys,xs=np.nonzero(mask)
    for y,x in zip(ys,xs):
        if seen[y,x]: continue
        st=[(y,x)]; seen[y,x]=1; pts=[]
        while st:
            cy,cx=st.pop(); pts.append((cy,cx))
            for ny,nx in ((cy+1,cx),(cy-1,cx),(cy,cx+1),(cy,cx-1)):
                if 0<=ny<H and 0<=nx<W and mask[ny,nx] and not seen[ny,nx]: seen[ny,nx]=1; st.append((ny,nx))
        a=np.array(pts); y0,x0=a.min(0); y1,x1=a.max(0); out.append((x0,y0,x1-x0+1,y1-y0+1,len(pts)))
    return out
R={}
for f in sorted(glob.glob(P+'/*.webp')):
    im=np.asarray(Image.open(f).convert('RGB')).astype(int); H,W,_=im.shape
    r,g,b=im[...,0],im[...,1],im[...,2]
    org=(r>190)&(g>60)&(g<130)&(b<90)
    cs=[c for c in blobs(org) if 16<=c[2]<=48 and 16<=c[3]<=48 and abs(c[2]-c[3])<=4 and c[4]>0.45*c[2]*c[3] and c[1]>H*0.35]
    # a row of 2-4 circles at the same height
    rows={}; cl=[]
    for c in sorted(cs,key=lambda c:c[1]+c[3]/2):
        if cl and abs((c[1]+c[3]/2)-(cl[-1][-1][1]+cl[-1][-1][3]/2))<=8: cl[-1].append(c)
        else: cl.append([c])
    rows=dict(enumerate(cl))
    good=[v for v in rows.values() if len(v)>=2 and min(c[0] for c in v)<0.045*W]   # the hint row starts at the left margin
    row=max(good,key=lambda v:min(c[1] for c in v)) if good else []
    row=sorted(row,key=lambda c:c[0])
    if len(row)<2: continue
    ink=(im.sum(2)<600)   # non-white
    cy0=min(c[1] for c in row)-6
    # a light rule across the picture below the hints = the answer strip's top
    rule=None
    for y in range(cy0+30,H):
        line=(np.abs(im[y]-im[y].mean(0)).sum(1)<30)&(im[y].sum(1)<735)&(im[y].sum(1)>500)
        if line.sum()>W*0.6: rule=y; break
    bot=(rule-3) if rule else H-1
    rows_ink=np.nonzero(ink[cy0:bot].any(1))[0]; y1=cy0+(rows_ink.max() if len(rows_ink) else bot-cy0)+6
    hints=[]
    for k,c in enumerate(row):
        x0=c[0]-6; x1=(row[k+1][0]-8) if k+1<len(row) else W-4
        hints.append([round(x0/W,4),round(cy0/H,4),round((x1-x0)/W,4),round((min(y1,bot)-cy0)/H,4)])
    ans=None
    if rule and not f.endswith('-q.webp'):
        ai=np.nonzero(ink[rule+3:].any(1))[0]
        if len(ai): ans=[0,round((rule+2)/H,4),1,round((ai.max()+10)/H,4)]
    R[os.path.basename(f)[:-5]]={'h':hints,'a':ans}
json.dump(R,open(os.path.join(D,'pophints.json'),'w'))
print(len(R),'pictures with hints;',sum(1 for v in R.values() if v['a']),'with an answer strip')
