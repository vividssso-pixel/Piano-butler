# The Butler's Music Box (her 10 Nov 22:29-22:32): both hands as letters in beat boxes, one song a page, no numbers,
# no extra songs. Right hand in C position (middle C = thumb), left hand one key a bar. Tunes and chord places are
# traditional and public domain, written from memory: for Sohyun to check by ear.
import json, copy
base = json.load(open('let1.json'))
B = lambda r, l, w='': {'r': r, 'l': l, 'w': w}
LH2 = ('C with finger 5, G with the thumb.', {'c': 5, 'g': 1})
LH3 = ('C with 5, F with 2, G with the thumb.', {'c': 5, 'f': 2, 'g': 1})
S = [
 dict(t='Hot Cross Buns', id='buns', job='Three notes, both hands, from today. An old London street song.', lh=('Only C: finger 5. Let it ring.', {'c': 5}),
      how='Count out loud, 1 2 3 4. One letter, one box. A box split in two: two quick notes, \u201cone-a, pen-ny\u201d.',
      g=[[B('E D C -', 'C', 'Hot cross buns -'), B('E D C -', 'C', 'hot cross buns -')], [B('C.C C.C D.D D.D', 'C', 'one.a pen.ny two.a pen.ny'), B('E D C -', 'C', 'hot cross buns -')]]),   # a short song: two bars a line, big
 None,  # Song 2: Mary, let1.json as she approved it
 dict(t='Au Clair de la Lune', id='auclair', job='A French song by moonlight. Play it softly, at bedtime.', lh=LH2,
      how='Some notes last two boxes. Count both, and keep holding through the line.',
      g=[[B('C C C D', 'C', 'Au clair de la'), B('E - D -', 'G', 'lu- - ne -'), B('C E D D', 'C', 'mon a- mi Pier-'), B('C - - -', 'C', 'rot - - -')],
         [B('C C C D', 'C', 'Prê- te- moi ta'), B('E - D -', 'G', 'plu- - me -'), B('C E D D', 'C', 'pour é- crire un'), B('C - - -', 'C', 'mot - - -')]]),
 dict(t='Lightly Row', id='lightly', job='A boat song. Play it smoothly, like rowing on still water.', lh=LH2,
      how='Count out loud, 1 2 3 4. One letter, one box. A line means keep holding.',
      g=[[B('G E E -', 'C', 'Light- ly row -'), B('F D D -', 'G', 'light- ly row -'), B('C D E F', 'C', 'o’er the glass- y'), B('G G G -', 'C', 'waves we go -')],
         [B('G E E -', 'C', 'Smooth- ly glide -'), B('F D D -', 'G', 'smooth- ly glide -'), B('C E G G', 'C', 'on the si- lent'), B('C - - -', 'C', 'tide - - -')]]),
 dict(t='Ode to Joy', id='ode', job='Beethoven’s most famous tune, and now it is yours. Play it after dinner.', lh=LH2,
      how='A big tune made of small steps. Look for the line that comes back.',
      g=[[B('E E F G', 'C', 'Joy- ful, joy- ful,'), B('G F E D', 'G', 'we a- dore thee,'), B('C C D E', 'C', 'God of glo- ry,'), B('E D D -', 'G', 'Lord of love; -')],
         [B('E E F G', 'C', 'hearts un- fold like'), B('G F E D', 'G', 'flowers be- fore thee,'), B('C C D E', 'C', 'o- pening to the'), B('D C C -', 'C', 'sun a- bove. -')]]),
 dict(t='Jingle Bells', id='jingle', job='December’s favourite. Play it, and the whole room sings.', lh=LH3,
      how='New for the left hand: F, with finger 2. It comes twice, in the same place each time.',
      g=[[B('E E E -', 'C', 'Jin- gle bells -'), B('E E E -', 'C', 'jin- gle bells -'), B('E G C D', 'C', 'jin- gle all the'), B('E - - -', 'C', 'way - - -')],
         [B('F F F F', 'F', 'oh what fun it'), B('F E E E.E', 'C', 'is to ride in.a'), B('E D D E', 'G', 'one- horse o- pen'), B('D - G -', 'G', 'sleigh, - hey! -')],
         [B('E E E -', 'C', 'Jin- gle bells -'), B('E E E -', 'C', 'jin- gle bells -'), B('E G C D', 'C', 'jin- gle all the'), B('E - - -', 'C', 'way - - -')],
         [B('F F F F', 'F', 'oh what fun it'), B('F E E E.E', 'C', 'is to ride in.a'), B('G G F D', 'G', 'one- horse o- pen'), B('C - - -', 'C', 'sleigh! - - -')]]),
 dict(t='Twinkle, Twinkle, Little Star', id='twinkle', job='The first song most people ever learn. Play it at bedtime, under the stars.', lh=LH3, rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5}, 'New: A. Finger 5 reaches up from G, then comes back.'),
      how='The right hand meets a new key, A. Find it before you start.',
      g=[[B('C C G G', 'C', 'Twin- kle twin- kle'), B('A A G -', 'F', 'lit- tle star -'), B('F F E E', 'G', 'how I won- der'), B('D D C -', 'C', 'what you are -')],
         [B('G G F F', 'C', 'Up a- bove the'), B('E E D -', 'G', 'world so high -'), B('G G F F', 'C', 'like a dia- mond'), B('E E D -', 'G', 'in the sky -')],
         [B('C C G G', 'C', 'Twin- kle twin- kle'), B('A A G -', 'F', 'lit- tle star -'), B('F F E E', 'G', 'how I won- der'), B('D D C -', 'C', 'what you are -')]]),
 dict(t='London Bridge', id='london', job='A game song: two people make the bridge, everyone else runs under. You are the music.', lh=LH2, rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5}, 'New: A. Finger 5 reaches up from G, then comes back.'),
      how='A comes back. The song starts on G, the top of the hand.',
      g=[[B('G A G F', 'C', 'Lon- don bridge is'), B('E F G -', 'C', 'fall- ing down -'), B('D E F -', 'G', 'fall- ing down -'), B('E F G -', 'C', 'fall- ing down -')],
         [B('G A G F', 'C', 'Lon- don bridge is'), B('E F G -', 'C', 'fall- ing down -'), B('D - G -', 'G', 'my - fair -'), B('E C - -', 'C', 'la- dy - -')]]),
 dict(t='When the Saints Go Marching In', id='saints', job='A parade song from New Orleans. March around the room to it first.', lh=LH3,
      how='New: an empty box with a dot is a rest. Count it, but stay quiet.',
      g=[[B('r C E F', 'C', '- Oh when the'), B('G - - -', 'C', 'saints - - -'), B('r C E F', 'C', '- go march- ing'), B('G - - -', 'C', 'in - - -')],
         [B('r C E F', 'C', '- Oh when the'), B('G - E -', 'C', 'saints - go -'), B('C - E -', 'C', 'march- - ing -'), B('D - - -', 'G', 'in - - -')],
         [B('r E E D', 'C', '- Oh Lord, I'), B('C - - C', 'C', 'want - - to'), B('E - G G', 'C', 'be - in that'), B('F - F -', 'F', 'num- - ber -')],
         [B('r C E F', 'C', '- Oh when the'), B('G - E -', 'C', 'saints - go -'), B('C - D -', 'G', 'march- - ing -'), B('C - - -', 'C', 'in - - -')]]),
]
for i, s in enumerate(S, 1):
    if not s:
        d = json.load(open('let1.json')); d.update({'label': f'Song {i}', 'lesson': i, 'id': 'mary'}); d['gig']['job'] = 'A song for a little brother, sister or cousin. New: G, with the left thumb.'; json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False); continue
    d = copy.deepcopy(base)
    d.update({'title': s['t'], 'label': f'Song {i}', 'lesson': i, 'id': s['id']})
    if s.get('rf'): d['gig']['rfing'], d['gig']['rmap'], d['gig']['r_cap'] = s['rf']
    d['gig'].update({'job': s['job'], 'tool_cap': s['lh'][0], 'fmap': s['lh'][1], 'song_how': s['how'], 'song_grid': s['g']})
    json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)
