import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
for a,b in [
 ("In the small house, the Dog lives in the middle, in his doghouse between the two black keys: that is D. The Cat sits at the left door (C) and the Elephant at the right door (E).",
  "In the small house lives Princess Clara, at the left door (C), with her Dog in his doghouse between the two black keys (D); the right door is the Exit (E)."),
 ("put a dot on the key where the Dog, the Cat, the Elephant, Grandma, the Apple garden and the two doors live,", "put a dot on the key where Princess Clara, her Dog, the Exit, Grandma, the Apple garden and the two doors live,"),
 ("then draw the Cat, the Dog, the Elephant, Grandma and her Apple garden on their keys.", "then draw Princess Clara, her Dog, Grandma and her Apple garden on their keys."),
]:
    assert s.count(a)==1,(a[:40]); s=s.replace(a,b)
assert 'Elephant' not in s and 'Cat' not in s.replace('Category','')
open(p,'w',encoding='utf-8').write(s); print('guide ok')
