# The Butler's Music Box (her 10 Nov 22:29-22:32): both hands as letters in beat boxes, one song a page, no numbers,
# no extra songs. Right hand in C position (middle C = thumb), left hand one key a bar. Tunes and chord places are
# traditional and public domain, written from memory: for Sohyun to check by ear.
import json, copy
base = json.load(open('let1.json'))
B = lambda r, l, w='': {'r': r, 'l': l, 'w': w}
F = lambda b, f: dict(b, f=f)   # a bar with its own fingers
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
 dict(t='Twinkle, Twinkle, Little Star', id='twinkle', job='The first song most people ever learn. Play it at bedtime, under the stars.', lh=LH3, rf=({'C': 1, 'D': 1, 'E': 2, 'F': 3, 'G': 4, 'A': 5}, {'c': 1, 'e': 2, 'f': 3, 'g': 4, 'a': 5}, '4 on G, 5 on A. Later the thumb slides up to D, then back to C.'),
      how='The right hand meets a new key, A. Find it before you start.',
      g=[[F(B('C C G G', 'C', 'Twin- kle twin- kle'), '1 1 4 4'), F(B('A A G -', 'F', 'lit- tle star -'), '5 5 4 -'), F(B('F F E E', 'G', 'how I won- der'), '4 4 3 3'), F(B('D D C -', 'C', 'what you are -'), '2 2 1 -')],
         [F(B('G G F F', 'C', 'Up a- bove the'), '5 5 4 4'), F(B('E E D -', 'G', 'world so high -'), '3 3 2 -'), F(B('G G F F', 'C', 'like a dia- mond'), '5 5 4 4'), F(B('E E D -', 'G', 'in the sky -'), '3 3 2 -')],
         [F(B('C C G G', 'C', 'Twin- kle twin- kle'), '1 1 4 4'), F(B('A A G -', 'F', 'lit- tle star -'), '5 5 4 -'), F(B('F F E E', 'G', 'how I won- der'), '4 4 3 3'), F(B('D D C -', 'C', 'what you are -'), '2 2 1 -')]]),
 dict(t='London Bridge', id='london', job='A game song: two people make the bridge, everyone else runs under. You are the music.', lh=LH2, rf=({'C': 1, 'D': 1, 'E': 2, 'F': 3, 'G': 4, 'A': 5}, {'d': 1, 'e': 2, 'f': 3, 'g': 4, 'a': 5}, 'Thumb on D. At the very end it slides down to C.'),
      how='A comes back. The song starts on G, the top of the hand.',
      g=[[B('G A G F', 'C', 'Lon- don bridge is'), B('E F G -', 'C', 'fall- ing down -'), B('D E F -', 'G', 'fall- ing down -'), B('E F G -', 'C', 'fall- ing down -')],
         [B('G A G F', 'C', 'Lon- don bridge is'), B('E F G -', 'C', 'fall- ing down -'), B('D - G -', 'G', 'my - fair -'), B('E C - -', 'C', 'la- dy - -')]]),
 dict(t='When the Saints Go Marching In', id='saints', job='A parade song from New Orleans. March around the room to it first.', lh=LH3,
      how='New: an empty box with a dot is a rest. Count it, but stay quiet.',
      g=[[B('r C E F', 'C', '- Oh when the'), B('G - - -', 'C', 'saints - - -'), B('r C E F', 'C', '- go march- ing'), B('G - - -', 'C', 'in - - -')],
         [B('r C E F', 'C', '- Oh when the'), B('G - E -', 'C', 'saints - go -'), B('C - E -', 'C', 'march- - ing -'), B('D - - -', 'G', 'in - - -')],
         [B('r E E D', 'C', '- Oh Lord, I'), B('C - - C', 'C', 'want - - to'), B('E - G G', 'C', 'be - in that'), B('G F - -', 'F', 'num- ber - -')],
         [B('r C E F', 'C', '- Oh when the'), B('G - E -', 'C', 'saints - go -'), B('C - D -', 'G', 'march- - ing -'), B('C - - -', 'C', 'in - - -')]]),
 dict(t='Are You Sleeping?', id='frere', job='A round: when you can play it, someone else starts it two bars after you.', lh=('C with 5. The thumb waits on G.', {'c': 5, 'g': 1}),
      rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5}, 'Finger 5 reaches to A again, then back to G.'),
      how='New: a tune note for the left hand. Where the right hand says L.H., your left thumb plays G.',
      g=[[B('C D E C', 'C', 'Are you sleep- ing'), B('C D E C', 'C', 'are you sleep- ing')], [B('E F G -', 'C', 'Bro- ther John -'), B('E F G -', 'C', 'Bro- ther John -')],
         [F(B('G.A G.F E C', 'C', 'Morn.ing bells.are ring- ing'), '4.5 4.3 2 1'), F(B('G.A G.F E C', 'C', 'morn.ing bells.are ring- ing'), '4.5 4.3 2 1')], [B('C <G C -', 'C', 'ding dang dong -'), B('C <G C -', 'C', 'ding dang dong -')]]),   # two bars a line: room for the split boxes
 dict(t='Camptown Races', id='camptown', job='A racing song: fast, bright and full of "doo-dah". Now every chord gets two keys.', lh=('C chord: C and G (5, 1). G chord: D and G (4, 1).', {'c': 5, 'd': 4, 'g': 1}),
      rf=({'C': 1, 'D': 1, 'E': 2, 'G': 4, 'A': 5}, {'d': 1, 'e': 2, 'g': 4, 'a': 5}, 'Thumb on D, 2 on E, 4 on G, 5 on A. At the end the thumb slides to C.'),
      how='The L.H. boxes now hold two keys: play the bottom and top together, once a bar.',
      g=[[B('G G E G', 'C+G', 'Camp- town la- dies'), B('A G E -', 'C+G', 'sing this song -'), B('E D - -', 'C+G', 'doo- dah - -'), B('E D - -', 'C+G', 'doo- dah - -')],
         [B('G G E G', 'C+G', 'Camp- town race- track'), B('A G E -', 'C+G', 'five miles long -'), B('D D E D', 'D+G', 'oh, doo- dah'), B('C - - -', 'C+G', 'day! - - -')]]),
 dict(t='Old MacDonald Had a Farm', id='oldmac', job='Everyone knows it, so everyone joins in. Make the animal noises too.', lh=('C with 5, F with 2, G with the thumb. The thumb also plays A, one key up.', {'c': 5, 'f': 2, 'g': 1, 'a': 1}),
      how='When the left hand has the tune (L.H.), it plays no chord in that bar: one job at a time.',
      g=[[B('C C C <G', 'C', 'Old Mac- Don- ald'), B('<A <A <G -', '', 'had a farm -'), B('E E D D', 'G', 'E I E I'), B('C - - <G', 'C', 'O - - and')],
         [B('C C C <G', 'C', 'on his farm he'), B('<A <A <G -', '', 'had a cow -'), B('E E D D', 'G', 'E I E I'), B('C - - -', 'C', 'O - - -')]]),
]
def mary4(i):
    d = json.load(open('let1.json')); d.update({'title': 'Mary, Four Ways', 'label': f'Song {i}', 'lesson': i, 'id': 'mary'})
    d['gig'].update({'job': 'You know this one. Now the left hand plays it four new ways.',
        'song_how': 'The L.H. boxes show which key. The ways below show four new rhythms for it.',
        'ways': [('Way 1|twice', 'C - C -'), ('Way 2|play, lift', 'C r C r'), ('Way 3|march', 'C C C C'), ('Way 4|long short short', 'C - C C')],   # her 23:25: not the basic one; each way one step on from the last
        'ways_how': 'One way at a time, the whole song. On G bars, the same rhythm on G.',
        'ticks': ['Way 1', 'Way 2', 'Way 3', 'Way 4']})
    json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)
for i, s in enumerate(S, 1):
    if s == 'mary4': mary4(i); continue
    if not s:
        d = json.load(open('let1.json')); d.update({'label': f'Song {i}', 'lesson': i, 'id': 'mary'}); d['gig']['job'] = 'A song for a little brother, sister or cousin. New: G, with the left thumb.'; json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False); continue
    d = copy.deepcopy(base)
    d.update({'title': s['t'], 'label': f'Song {i}', 'lesson': i, 'id': s['id']})
    if s.get('rf'): d['gig']['rfing'], d['gig']['rmap'], d['gig']['r_cap'] = s['rf']
    d['gig'].update({'job': s['job'], 'tool_cap': s['lh'][0], 'fmap': s['lh'][1], 'song_how': s['how'], 'song_grid': s['g']})
    json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)

# Left hand, four ways, step by step (her 23:13, 23:25, 23:29, 23:33 easy to hard, 23:35 big beats first, quavers later): the root alone, new rhythms; a page of their own straight
# after the song, not the song drawn again. Mary: halves, crotchets, long-short-short, a rest. Lightly Row: split beats and
# beats 2 and 4. Ode to Joy: the '&' -- off-beats and a push. Then: root and fifth.
WAYS = {
 'mary': ('You know the song. Now the left hand plays it four new ways: the same keys, a new rhythm each time.',
          [('Way 1|twice', 'C - C -'), ('Way 2|play, lift', 'C r C r'), ('Way 3|march', 'C C C C'), ('Way 4|long short short', 'C - C C')],
          'Bar by bar, play the key from the song (C or G) in the rhythm of the way. A dot means lift and wait.'),
 'lightly': ('Lightly Row again. The left hand learns to wait, and to come in late.',
          [('Way 1|wait for it', 'C - - C'), ('Way 2|on 2 and 4', 'r C r C'), ('Way 3|short long short', 'C C - C'), ('Way 4|rest, go', 'r C C C')],
          'Still one box, one beat. A dot means lift and wait. On beats 2 and 4, the left hand is the drummer.'),
 'london': ('Two keys together now. For C: C and G, fingers 5 and 1. For G: the thumb stays on G and finger 4 takes D.',
          [('Way 1|together', 'C+G - - -'), ('Way 2|twice', 'C+G - C+G -'), ('Way 3|bottom, top', 'C - G -'), ('Way 4|oom-pah', 'C G C G')],
          'The hand stays where it is: only one finger moves, 5 on C or 4 on D. The thumb lives on G.'),
 'saints': ('Two keys on every chord, and F joins in. The hand still stays put: C and G, C and F, D and G.',
          [('Way 1|together', 'C+G - - -'), ('Way 2|twice', 'C+G - C+G -'), ('Way 3|bottom, top', 'C - G -'), ('Way 4|oom-pah', 'C G C G')],
          'C chord: C and G (5 and 1). F chord: C and F (5 and 2). G chord: D and G (4 and 1).'),
 'oldmac': ('The split box again, and now the left hand finds the "&" between the beats.',
          [('Way 1|tap, lift', 'C.r C.r C.r C.r'), ('Way 2|skip', 'C - C.C -'), ('Way 3|the push', 'C - r.C -'), ('Way 4|on the &', 'r.C r.C r.C r.C')],
          'Count "1 & 2 & 3 & 4 &". The dot is a lift. Play the ways in the bars that have a chord box.'),
 'ode': ('Ode to Joy again. Rests in new places: the left hand starts to talk back to the tune.',
          [('Way 1|hold, lift, go', 'C - r C'), ('Way 2|play, lift, two', 'C r C C'), ('Way 3|late start', 'r r C -'), ('Way 4|the answer', 'r C - C')],
          'Big beats only. Count out loud; the dot is a lift. On G bars, the same rhythm on G.'),
 'frere': ('Now a beat can split in two for the left hand too: two quick keys in one box.',
          [('Way 1|march, run-ning', 'C C C C.C'), ('Way 2|walk, run-ning', 'C C.C C C.C'), ('Way 3|run-ning, walk', 'C.C C C.C C'), ('Way 4|running', 'C.C C.C C.C C.C')],
          'Say "run-ning" for a split box. On G bars, the same rhythm on G; in the last two bars, keep your thumb free for the tune.'),
}
for i in range(1, 20):
    try: d = json.load(open(f'mb{i}.json'))
    except FileNotFoundError: break
    if d.get('id') in WAYS and 'Ways' not in d['title']:
        j, w, h = WAYS[d['id']]; d['gig'].update({'ways': w, 'ways_job': j, 'ways_how': h, 'ways_title': d['title'].split(',')[0].replace(' Go Marching In', '') + (', Two Keys' if d['id'] == 'london' else ', Three Shapes' if d['id'] == 'saints' else ', Four Ways')})
        if d['id'] == 'saints': d['gig']['ways_roots'] = ['C', 'F', 'G']
        json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)
