# The Butler's Music Box (her 10 Nov 22:29-22:32): both hands as letters in beat boxes, one song a page, no numbers,
# no extra songs. Right hand in C position (middle C = thumb), left hand one key a bar. Tunes and chord places are
# traditional and public domain, written from memory: for Sohyun to check by ear.
import json, copy
base = json.load(open('let1.json'))
B = lambda r, l, w='': {'r': r, 'l': l, 'w': w}
F = lambda b, f: dict(b, f=f)   # a bar with its own fingers
OOM = {'C': 'C G C G', 'G': 'G D G D', 'F': 'F C F C'}
O = lambda b: dict(b, lp=OOM[b['l']])
RK = {'C': 'C - G -', 'G': 'G - D -', 'F': 'F - C -'}
Rock = lambda b: dict(b, lp=RK[b['l']])
WZ = {'C': 'C G G', 'G': 'G D D', 'F': 'F C C'}
Waltz = lambda b: dict(b, lp=WZ[b['l']])   # oom-pah-pah: the root on ONE, the other key on two and three   # bottom, then top: a slow rocking left hand   # oom-pah: the root, then the other key, the hand never moves
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
         [B('E E F G', 'C', 'hearts un- fold like'), B('G F E D', 'G', 'flowers be- fore thee,'), B('C C D E', 'C', 'o- pening to the'), B('D C C -', 'C', 'sun a- bove -')]]),
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
         [B('r E E D', 'G', '- Oh Lord, I'), B('C - - C', 'C', 'want - - to'), B('E - G G', 'C', 'be - in that'), B('G F - -', 'F', 'num- ber - -')],
         [B('r C E F', 'F', '- Oh when the'), B('G - E -', 'C', 'saints - go -'), B('C - D -', 'G', 'march- - ing -'), B('C - - -', 'C', 'in - - -')]]),   # her 18 Nov 20:59: the last line's left hand starts on F
 dict(t='Are You Sleeping?', id='frere', job='A round: when you can play it, someone else starts it two bars after you.', lh=('C with 5. The thumb waits on G.', {'c': 5, 'g': 1}),
      rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5}, 'Finger 5 reaches to A again, then back to G.'),
      how='New: a tune note for the left hand. Where the right hand says L.H., your left thumb plays G.',
      g=[[B('C D E C', 'C', 'Are you sleep- ing'), B('C D E C', 'C', 'are you sleep- ing')], [B('E F G -', 'C', 'Bro- ther John -'), B('E F G -', 'C', 'Bro- ther John -')],
         [F(B('G.A G.F E C', 'C', 'Morn.ing bells.are ring- ing'), '4.5 4.3 2 1'), F(B('G.A G.F E C', 'C', 'morn.ing bells.are ring- ing'), '4.5 4.3 2 1')], [B('C <G C -', 'C', 'ding dang dong -'), B('C <G C -', 'C', 'ding dang dong -')]]),   # two bars a line: room for the split boxes
 dict(t='Camptown Races', id='camptown', job='A racing song: fast, bright and full of "doo-dah". Now every chord gets two keys.', lh=('C chord: C and G (5, 1). G chord: D and G (4, 1).', {'c': 5, 'd': 4, 'g': 1}),
      rf=({'C': 1, 'D': 1, 'E': 2, 'G': 4, 'A': 5}, {'d': 1, 'e': 2, 'g': 4, 'a': 5}, 'Thumb on D, 2 on E, 4 on G, 5 on A. At the end the thumb slides to C.'),
      how='The L.H. boxes now hold two keys: play the bottom and top together, once a bar.',
      g=[[B('G G E G', 'C+G', 'Camp- town la- dies'), B('A G E -', 'C+G', 'sing this song -'), B('E D - -', 'D+G', 'doo- dah - -'), B('E D - -', 'D+G', 'doo- dah - -')],
         [B('G G E G', 'C+G', 'Camp- town race- track'), B('A G E -', 'C+G', 'five miles long -'), F(B('D D E D', 'D+G', 'oh, doo- dah'), '1 1 3 2'), B('C - - -', 'C+G', 'day! - - -')]]),
 dict(t='Old MacDonald Had a Farm', id='oldmac', job='Everyone knows it, so everyone joins in. Make the animal noises too.', lh=('C with 5, F with 2, G with the thumb. For A, finger 2 crosses over the thumb.', {'c': 5, 'f': 2, 'g': 1, 'a': 2}),
      how='When the left hand has the tune (L.H.), it plays no chord in that bar: one job at a time.',
      g=[[B('C C C <G', 'C', 'Old Mac- Don- ald'), dict(B('<A <A <G -', '', 'had a farm -'), lf='2 2 1 -'), B('E E D D', 'G', 'E I E I'), B('C - - <G', 'C', 'O - - and')],
         [B('C C C <G', 'C', 'on his farm he'), dict(B('<A <A <G -', '', 'had a cow -'), lf='2 2 1 -'), B('E E D D', 'G', 'E I E I'), B('C - - -', 'C', 'O - - -')]]),
 dict(t='Happy Birthday', id='birthday', meter='3/4', job='The song for every birthday, in three: ONE two three. Both thumbs share middle C.', lh=('Thumb on middle C, with the right thumb. 2 on B, 3 on A, 4 on G.', {'g': 4, 'a': 3, 'b': 2}),
      rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5}, 'Thumb on middle C too: the two thumbs take turns.'),
      how='New: a song in three. The tune walks from hand to hand; L.H. means the left hand plays it.',
      g=[[B('r r <G.G', '', '- - Hap.py'), B('<A <G C', '', 'birth- day to'), B('<B - <G.G', '', 'you, - hap.py')],
         [B('<A <G D', '', 'birth- day to'), B('C - <G.G', '', 'you, - hap.py'), B('G E C', '', 'birth- day dear')],
         [B('<B <A F.F', '', 'Sam- my, hap.py'), B('E C D', '', 'birth- day to'), B('C - -', '', 'you! - -')]]),   # three bars a line
 dict(t='Yankee Doodle', id='yankee', job='A marching song from 1700s America. March on the spot while you sing it.', lh=('Thumb on middle C again. 2 on B, 3 on A, 4 on G.', {'g': 4, 'a': 3, 'b': 2}),
      rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5}, 'Thumb on middle C: both thumbs share it.'),
      how='Both thumbs on middle C. Count 1 2 3 4 and keep marching: the hands take turns.',
      g=[[B('C C D E', '', 'Yan- kee Doo- dle'), B('C E D <G', '', 'went to town a-'), B('C C D E', '', 'rid- ing on a'), B('C - <B -', '', 'po- - ny -')],
         [B('C C D E', '', 'stuck a fea- ther'), B('F E D C', '', 'in his cap and'), B('<B <G <A <B', '', 'called it ma- ca-'), B('C - C -', '', 'ro- - ni -')]]),
 dict(t='Amazing Grace', id='amazing', meter='3/4', job='A slow song in three, sung all over the world for two hundred years. Let every long note ring.', lh=('Thumb on middle C too. 3 on A, 4 on G.', {'g': 4, 'a': 3}),
      rf=({'C': 1, 'D': 2, 'E': 3, 'G': 5}, {'c': 1, 'd': 2, 'e': 3, 'g': 5}, 'Thumb on middle C, 5 on G. No F in this song.'),
      how='Slow, in three. A line holds the note; it can carry on into the next bar.',
      g=[[B('r r <G', '', '- - A-'), B('C - E.C', '', 'maz- - ing.'), B('E - D', '', 'grace - how'), B('C - <A', '', 'sweet - the')],
         [B('<G - <G', '', 'sound - that'), B('C - E.C', '', 'saved - a.'), B('E - D.E', '', 'wretch - like.'), B('G - -', '', 'me - -')],
         [B('- - E.G', '', '- - I.'), B('G - E.C', '', 'once - was.'), B('E - D', '', 'lost - but'), B('C - <A', '', 'now - am')],
         [B('<G - <G', '', 'found - was'), B('C - E.C', '', 'blind - but.'), B('E - D', '', 'now - I'), B('C - -', '', 'see - -')]]),
 dict(t='Goin\u2019 Home', id='goinhome', job='A tune from Dvo\u0159\u00e1k\u2019s New World Symphony, 1893. Play it slowly, like a long way home.', lh=('C: C then G (5, 1). G: G then D (1, 4). The hand stays.', {'c': 5, 'd': 4, 'g': 1}),
      how='New: the left hand rocks in the song. The box names the chord; then its other key, on beat 3.',
      g=[[Rock(B('E G G -', 'C', 'Go- in\u2019 home -')), Rock(B('E D C -', 'C', 'go- in\u2019 home -')), Rock(B('D E G E', 'G', 'I\u2019m a go- in\u2019')), dict(B('D - - -', 'G', 'home - - -'), lp='G - D -')],
         [Rock(B('E G G -', 'C', 'Qui- et- like -')), Rock(B('E D C -', 'C', 'some still day -')), Rock(B('D E D C', 'G', 'I\u2019m jes\u2019 go- in\u2019')), dict(B('C - - -', 'C', 'home - - -'), lp='C - - -')]]),
 dict(t='This Old Man', id='oldman', job='A counting song: verse 1 is \u201cthumb\u201d, then shoe, knee, door\u2026 Sing as many verses as you can.', lh=('C: C then G (5, 1). F: F then C (2, 5). G: G then D (1, 4).', {'c': 5, 'd': 4, 'f': 2, 'g': 1}),
      rf=({'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5}, 'Thumb on middle C. Finger 5 reaches to A, then back to G.'),
      how='New: oom-pah in the song. The box names the chord; then its keys in turn, one a beat.',
      g=[[O(B('G E G -', 'C', 'This old man, -')), O(B('G E G -', 'C', 'he played one, -'))], [O(B('A G F E', 'F', 'he played knick- knack')), O(B('D E F -', 'G', 'on my thumb, -'))],
         [O(B('E.F G C C.C', 'C', 'with.a knick knack pad.dy')), O(B('C D.E F G', 'C', 'whack, give.a dog a'))], [O(B('G D D F', 'G', 'bone, this old man')), dict(B('E.E D C -', 'C', 'came.roll ing home -'), lp='C - - -')]]),   # two bars a line: room for the split boxes
 dict(t='The Blue Danube', id='danube', meter='3/4', job='Johann Strauss\u2019s most famous waltz, 1867. The left hand is the dance: ONE two three.', lh=('C: C then G, G (5, 1, 1). G: G then D, D (1, 4, 4).', {'c': 5, 'd': 4, 'g': 1}),
      how='New: the waltz. The box names the chord: play it on ONE, then its other key twice. Oom-pah-pah.',
      g=[[B('r r C', '', '- - -'), Waltz(B('C E G', 'C', '- - -')), Waltz(B('G - -', 'C', '- - -')), Waltz(B('r G G', 'C', '- - -'))],
         [Waltz(B('r E E', 'C', '- - -')), Waltz(B('r r C', 'C', '- - -')), Waltz(B('C E G', 'C', '- - -')), Waltz(B('G - -', 'C', '- - -'))],
         [Waltz(B('r G G', 'C', '- - -')), Waltz(B('r F F', 'G', '- - -')), Waltz(B('E - -', 'C', '- - -')), dict(B('C - -', 'C', '- - -'), lp='C - -')]]),
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
    if s.get('meter'): d['meter'], d['beats'] = s['meter'], int(s['meter'][0])
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
 'camptown': ('Back to one key a chord, and now the left hand finds the "&" between the beats.',
          [('Way 1|tap, lift', 'C.r C.r C.r C.r'), ('Way 2|skip', 'C - C.C -'), ('Way 3|the push', 'C - r.C -'), ('Way 4|on the &', 'r.C r.C r.C r.C')],
          'Count "1 & 2 & 3 & 4 &". The dot is a lift. Play each chord\u2019s bottom key: C, or G.'),
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

# Music Box 1 (her 18 Nov 15:19: 'The Piano Butler's Music Box 1 / 2 / 3', numbers only). Song 19 is the book's last page,
# Twinkle again with the left hand the child has now (her 18 Nov 13:57: every book ends with Twinkle, so the growth shows).
RK = {'C': 'C - G -', 'G': 'G - D -', 'F': 'F - C -'}
t = json.load(open('mb7.json')); g = t['gig']
t.update({'title': 'Twinkle, Now', 'label': 'End of Music Box 1', 'lesson': 19})
g['job'] = 'You played Twinkle as Song 7, with one key a chord. Play it again with the left hand you have now. Same tune, bigger left hand.'
g['fmap'] = {'c': 5, 'd': 4, 'f': 2, 'g': 1}; g['tool_cap'] = 'C then G (5, 1). F then C (2, 5). G then D (1, 4).'
g['song_how'] = '<b>Then</b> (Song 7): one key a bar. <b>Now</b>: two keys a bar, steady as a rock.'
for line in g['song_grid']:
    for b in line: b['lp'] = RK[b['l']]
g.pop('ways', None); json.dump(t, open('mb19.json', 'w'), ensure_ascii=False)
for i in range(1, 20):
    d = json.load(open(f'mb{i}.json')); d['book'] = "THE PIANO BUTLER'S MUSIC BOX 1"; json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)
# Note shapes from the middle of Music Box 1 (her 18 Nov 18:12-18:13: '1 중간쯤부터'; Book 2 then writes the letter
# inside the note head): from Song 10 each letter shows the shape of its length, just to look at.
for i in range(10, 20):
    d = json.load(open(f'mb{i}.json')); d['gig']['shapes'] = 1
    if i == 10 and 'Look:' not in d['gig']['song_how']: d['gig']['song_how'] = d['gig']['song_how'].rstrip() + ' <b>Look:</b> behind each letter is a faint note. Its shape shows how long the note is.'
    json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)

# 26 Nov, her '마지막 두곡': The Blue Danube rewritten from the open score (Mutopia, Strauss Op. 314, first sixteen bars).
# The two answering chords are written as their top note, an octave lower, and in their real rhythm: on beat 3, held into the next bar.
d = json.load(open('mb18.json')); g = d['gig']
def DB(r, c): return {'r': r, 'l': c, 'w': '- - -', **({'lp': {'C': 'C G G', 'G': 'G D D', 'Ce': 'C - -'}[c]} if c else {})}
g['song_grid'] = [[DB('r r C', ''), DB('C E G', 'C'), DB('G - G', 'C'), DB('G - E', 'C')],
                  [DB('E - C', 'C'), DB('C E G', 'C'), DB('G - G', 'C'), DB('G - F', 'G')],
                  [DB('F - B,', 'G'), DB('B, D A', 'G'), DB('A - A', 'G'), DB('A - F', 'G')],
                  [DB('F - B,', 'G'), DB('B, D A', 'G'), DB('A - A', 'G'), DB('A - E', 'C')],
                  [dict(DB('E - -', 'Ce'), l='C')]]
g['song_how'] = 'New: the waltz. The box names the chord: play it on ONE, then its other key twice. Oom-pah-pah. In the tune, a rising call is answered by two bell notes: each answer starts on beat 3 and rings on into the next bar.'
g['r_cap'] = 'Thumb on middle C. B↓ is the key just below it: the thumb steps down. Finger 5 reaches up to A.'
g['song_how'] = 'The waltz: the box names the chord. Play it on ONE, then its other key twice. In the tune, a rising call is answered by two bell notes that start on beat 3 and ring on.'
flat = [b for ln in g['song_grid'] for b in ln]; g['song_grid'] = [flat[:5], flat[5:9], flat[9:13], flat[13:]]
json.dump(d, open('mb18.json', 'w'), ensure_ascii=False)

# ---- 27 Nov: one song at a time, each finished and checked (PLAN.md). Song 1.
# Hot Cross Buns: checked against the Kodály Center song collection (song 845, from Heritage Songster, 1966):
# tone set do re mi, form a a b a, motives "mi re do rest" and "do do re re" in quick pairs. So the fourth beat is a rest, not a held note.
d = json.load(open('mb1.json')); g = d['gig']
for ln in g['song_grid']:
    for b in ln:
        if b['r'] == 'E D C -': b['r'] = 'E D C r'
g['today'] = 'Roots'
g['song_how'] = 'Count out loud, 1 2 3 4. One letter, one box. A small circle is a rest: lift, and say the number without playing. A box split in two: two quick notes, “one-a, pen-ny”.'
json.dump(d, open('mb1.json', 'w'), ensure_ascii=False)

# Song 2, Mary Had a Little Lamb: bars 1-3 and 5-8 agree note for note with the Musica Viva transcription (via folktunefinder 174581).
# Bar 4 there is E E E (an English three-note version); this book keeps the usual E G G, the version with G that pianochord.org describes (notes C D E G, 8 bars).
d = json.load(open('mb2.json')); d['gig']['today'] = 'Roots'; json.dump(d, open('mb2.json', 'w'), ensure_ascii=False)

# ---- Songs 3 to 7, finished and checked as one batch (her 27 Nov 00:56: five at a time)
def _bars(rows): return [[{'r': r, 'l': l, 'w': w} for r, l, w in ln] for ln in rows]
def _save(n, **kw):
    d = json.load(open(f'mb{n}.json')); g = d['gig']
    for k, v in kw.items(): g[k] = v
    g['today'] = 'Roots'; json.dump(d, open(f'mb{n}.json', 'w'), ensure_ascii=False)
# 3 Au Clair de la Lune: the whole song, A A B A. Checked against the analysis at bethsnotesplus.com (metre 4, form AABA,
# A uses do re mi only, B uses so, la, ti, do re; half and whole notes). In B the tune walks below middle C: the left hand takes those notes.
A3 = lambda w: [('C C C D', 'C', w[0]), ('E - D -', 'G', w[1]), ('C E D D', 'C', w[2]), ('C - - -', 'C', w[3])]
_save(3, song_grid=_bars([A3(['Au clair de la', 'lu- - ne - ', 'mon a- mi Pier-', 'rot - - -']), A3(['Prê- te- moi ta', 'plu- - me -', 'pour é- crire un', 'mot - - -']),
    [('D D D D', '', 'Ma chan- delle est'), ('<A - <A -', '', 'mor- - te -'), ('D C <B <A', '', 'je n’ai plus de'), ('<G - - -', '', 'feu - - -')],
    A3(['Ou- vre- moi ta', 'por- - te -', 'pour l’a- mour de', 'Dieu - - -'])]))
# 4 Lightly Row: all sixteen bars. Identical to the Essen collection's "Alles neu macht der Mai" (the same tune); bar 8 ends on E, the last bar on C.
A4 = [('G E E -', 'C'), ('F D D -', 'G')]
_save(4, song_grid=_bars([[(r, l, w) for (r, l), w in zip(A4 + [('C D E F', 'C'), ('G G G -', 'C')], ['Light- ly row -', 'light- ly row -', 'o’er the glass- y', 'waves we go -'])],
    [(r, l, w) for (r, l), w in zip(A4 + [('C E G G', 'C'), ('E - r r', 'C')], ['Smooth- ly glide -', 'smooth- ly glide -', 'on the si- lent', 'tide - - -'])],
    [('D D D D', 'G', 'Let the winds and'), ('D E F -', 'G', 'wa- ters be -'), ('E E E E', 'C', 'min- gled with our'), ('E F G -', 'C', 'mel- o- dy -')],
    [(r, l, w) for (r, l), w in zip(A4 + [('C E G G', 'C'), ('C - r r', 'C')], ['Sing and float -', 'sing and float -', 'in our lit- tle', 'boat - - -'])]]))
# 5 Ode to Joy: all sixteen bars, with the dotted rhythm at the end of each line. Identical to the Mutopia score (BeethovenLv/ode, hymn form), moved from G to C.
# In bar 12 the tune dips to the G below middle C: the left hand plays it.
_save(5, song_grid=_bars([[('E E F G', 'C', 'Joy- ful, joy- ful,'), ('G F E D', 'G', 'we a- dore thee,'), ('C C D E', 'C', 'God of glo- ry,'), ('E -.D D -', 'G', 'Lord -.of love; -')],
    [('E E F G', 'C', 'hearts un- fold like'), ('G F E D', 'G', 'flowers be- fore thee,'), ('C C D E', 'C', 'o- pening to the'), ('D -.C C -', 'C', 'sun -.a- bove. -')],
    [('D D E C', 'G', 'Melt the clouds of'), ('D E.F E C', 'G', 'sin and.- sad- ness;'), ('D E.F E D', 'G', 'drive the.- dark of'), ('C D <G -', 'C', 'doubt a- way; -')],
    [('E E F G', 'C', 'Giv- er of im-'), ('G F E D', 'G', 'mor- tal glad- ness,'), ('C C D E', 'C', 'fill us with the'), ('D -.C C -', 'C', 'light -.of day! -')]]))
# 6 Jingle Bells (the chorus): identical to the ABC transcription at pages.cpsc.ucalgary.ca once the two dotted notes are in (bars 3 and 5 of each half).
d = json.load(open('mb6.json'))
for ln in d['gig']['song_grid']:
    for b in ln:
        if b['r'] == 'E G C D': b['r'] = 'E G C -.D'; b['w'] = 'jin- gle all -.the'
        if b['r'] == 'F F F F': b['r'] = 'F F F -.F'; b['w'] = 'oh what fun -.it'
json.dump(d, open('mb6.json', 'w'), ensure_ascii=False); _save(6)
# 7 Twinkle: identical to the ABC in "LaTeX for musicians" (CTAN), twelve bars. Nothing to change.
_save(7)

# ---- Songs 8 to 12
def _tag(n, t):
    d = json.load(open(f'mb{n}.json')); d['gig']['today'] = t; json.dump(d, open(f'mb{n}.json', 'w'), ensure_ascii=False)
# 8 London Bridge: no open score reached yet (27 Nov); unchanged and NOT yet checked.
_tag(8, 'Roots')
# 9 When the Saints: checked against the transcription at folktunefinder 125223. One bar was wrong: after "number" the F is held and the pick-up is E F, not C E F.
d = json.load(open('mb9.json')); b = d['gig']['song_grid'][3][0]; assert b['r'] == 'r C E F'; b['r'] = '- - E F'; b['w'] = '- - when the'; json.dump(d, open('mb9.json', 'w'), ensure_ascii=False); _tag(9, 'Roots')
# 10 Are You Sleeping? (Frère Jacques): identical to the transcription at folktunefinder 143754. Nothing to change.
_tag(10, 'Roots')
# 11 Camptown Races: verse identical to folktunefinder 145383; the chorus added from the same source, so the song is whole (sixteen bars).
d = json.load(open('mb11.json')); g = d['gig']
g['song_grid'] += _bars([[('C -.C E G', 'C+G', 'Goin’ -.to run all'), ("C' - - -", 'C+G', 'night! - - -'), ("A -.A C' A", 'C+F', 'Goin’ -.to run all'), ('G - - -', 'C+G', 'day! - - -')],
                         [('G G E.E G.G', 'C+G', 'I’ll bet my.mon ey.on the'), ('A G E -', 'C+G', 'bob- tail nag, -'), ('D D E D', 'D+G', 'some- bo- dy bet on the'.replace('bet on the', 'bet')[:99]), ('C - - -', 'C+G', 'bay. - - -')]])
g['song_grid'][3][2]['w'] = 'some- bo- dy bet'
g['song_grid'][3][0]['w'] = 'I’ll bet my.mo ney.on'; g['song_grid'][3][1]['w'] = 'the bobtail nag -'; g['song_grid'][3][2]['w'] = 'some- bo- dy bet'; g['song_grid'][3][3]['w'] = 'on the bay. - -'.replace('on the bay.', 'bay.')
g['r_cap'] = 'Thumb on D. In line 3 the hand reaches up to the high C, marked C↑.'
json.dump(d, open('mb11.json', 'w'), ensure_ascii=False); _tag(11, 'Block chord')
# 12 Old MacDonald: identical to the Musica Viva transcription (trillian.mit.edu mirror) once the rests are in: "O" lasts two beats, then a rest.
d = json.load(open('mb12.json'))
for ln in d['gig']['song_grid']:
    for b in ln:
        if b['r'] == 'C - - <G': b['r'] = 'C - r <G'
        if b['r'] == 'C - - -': b['r'] = 'C - r r'
json.dump(d, open('mb12.json', 'w'), ensure_ascii=False); _tag(12, 'Roots')

# ---- 27 Nov, second sitting: Song 8 checked, Song 12 made whole, Songs 13 to 17
# 8 London Bridge: every pitch agrees with the letter notes at noobnotes.net; "Lon-don" is a long note and a short one, so bars 1 and 5 get their dot.
d = json.load(open('mb8.json'))
for ln in d['gig']['song_grid']:
    for b in ln:
        if b['r'] == 'G A G F': b['r'] = 'G -.A G F'; b['w'] = 'Lon- -.don bridge is'
json.dump(d, open('mb8.json', 'w'), ensure_ascii=False)
# 12 Old MacDonald: the "moo moo here" middle added (pitches as at noobnotes.net: low so twice, then do; rhythm as it is sung), then the tune again: sixteen bars, the whole song.
d = json.load(open('mb12.json')); g = d['gig']; A = [dict(b) for b in g['song_grid'][0]]
g['song_grid'][1][3] = {'r': 'C - r <G.<G', 'l': 'C', 'w': 'O - - with.a'}
g['song_grid'] += _bars([[('C C C <G.<G', 'C', 'moo moo here and.a'), ('C C C r', 'C', 'moo moo there, -'), ('C.C C C.C C', 'C', 'here.a moo, there.a moo,'), ('C.C C.C C C', 'C', 'ev.’ry where.a moo moo.')]])
A[0]['w'] = 'Old Mac- Don- ald'; A[1]['w'] = 'had a farm -'; A[3] = {'r': 'C - r r', 'l': 'C', 'w': 'O - - -'}; g['song_grid'].append(A)
json.dump(d, open('mb12.json', 'w'), ensure_ascii=False)
# 13 Happy Birthday: every pitch agrees with the ABC example at kareiku.github.io (an octave lower here, shared between the hands). Unchanged.
# 14 Yankee Doodle: verse identical to folktunefinder 35660 (Chris Falt's transcription); the chorus added from the same source: sixteen bars.
d = json.load(open('mb14.json')); g = d['gig']
g['song_grid'] += _bars([[('A -.B A G', '', 'Yan- -.kee Doo- dle'), ("A B C' A", '', 'keep it up, -'), ('G -.A G F', '', 'Yan- -.kee Doo- dle'), ('E - G -', '', 'dan- - dy, -')],
                         [('A -.B A G', '', 'mind -.the mu- sic'), ("A B C' A", '', 'and the step and'), ("G C' B D'", '', 'with the girls be'), ("C' - C' -", '', 'han- - dy. -')]])
json.dump(d, open('mb14.json', 'w'), ensure_ascii=False)
# 15 Amazing Grace: pitches agree with the Mutopia score (a pipe setting, so its rhythm is freer). Unchanged.
# 16 Goin' Home: no open score found; unchanged and NOT yet checked.
# 17 This Old Man: rewritten from folktunefinder 3787. The "with a" pick-up belongs at the end of bar 4, and the last bar has three notes, not four.
d = json.load(open('mb17.json')); g = d['gig']
T = [[('G E G -', 'C', 'C G C G', 'This old man, -'), ('G E G -', 'C', 'C G C G', 'he played one, -')],
     [('A G F E', 'F', 'F C F C', 'he played knick- knack'), ('D E F E.F', 'G', 'G D G D', 'on my thumb; with.a')],
     [('G C C.C C', 'C', 'C G C G', 'knick- knack pad.dy whack,'), ('C.D E.F G -', 'C', 'C G C G', 'give.a dog.a bone, -')],
     [('G D D F', 'G', 'G D G D', 'this old man came'), ('E D C -', 'C', 'C - - -', 'roll- ing home. -')]]
g['song_grid'] = [[{'r': r, 'l': l, 'lp': lp, 'w': w} for r, l, lp, w in ln] for ln in T]
json.dump(d, open('mb17.json', 'w'), ensure_ascii=False)
for n, t in ((16, 'Roots'), (17, 'Zigzag')): _tag(n, t)
# Yankee Doodle chorus: the right hand moves up, so these bars carry their own fingers
d = json.load(open('mb14.json')); g = d['gig']
for b, f in zip(g['song_grid'][2] + g['song_grid'][3], ['2 -.3 2 1', '2 3 4 2', '3 -.4 3 2', '1 - 3 -', '2 -.3 2 1', '2 3 4 2', '1 4 3 5', '4 - 4 -']): b['f'] = f
g['r_cap'] = 'Thumb on middle C: both thumbs share it. For lines 3 and 4 the right hand moves up, thumb on G; a small arrow ↑ marks the high C and D.'
g['song_how'] = 'Both thumbs on middle C. Count 1 2 3 4 and keep marching: the hands take turns. Lines 3 and 4 are the chorus, all in the right hand, higher up: there B is the key above A.'
json.dump(d, open('mb14.json', 'w'), ensure_ascii=False)

# ---- 27 Nov 12:31-12:39, her '왼손에 치던거에 반주만 얹으면 되는거 아니었나' and '1': Songs 13 to 15 keep their layout (the tune shared between the hands,
# both thumbs on middle C). Only this is added: in a bar where the left hand has no tune on beat 1, it holds one key from its own hand position,
# G under a C or G chord, A under an F chord. (The version with the whole tune in the right hand is kept in mbox-rh-only-13-15.py for a later book.)
def _lay(n, notes, cap, how):
    d = json.load(open(f'mb{n}.json')); g = d['gig']; flat = [b for ln in g['song_grid'] for b in ln]; assert len(flat) == len(notes), (n, len(flat), len(notes))
    for b, x in zip(flat, notes):
        assert not (x and b['r'].split()[0].startswith('<')), (n, b['r'])
        b['l'] = x
    g['tool_cap'] = g['tool_cap'].rstrip() + ' ' + cap; g['song_how'] = how; g.pop('today', None)
    json.dump(d, open(f'mb{n}.json', 'w'), ensure_ascii=False)
CAP = 'When it has no tune to play, it holds G (or A).'
_lay(13, ['', '', '', '', 'G', 'G', '', 'G', 'G'], CAP, 'New: a song in three. The tune walks from hand to hand; L.H. means the left hand plays it. A boxed letter is a key the left hand holds under the tune.')
_lay(14, ['G', 'G', 'G', 'G', 'G', 'A', '', 'G', 'A', 'A', 'G', 'G', 'A', 'A', 'G', 'G'], CAP, 'Both thumbs on middle C; the hands take turns. A boxed letter is a key the left hand holds under the tune. Lines 3 and 4 are the chorus, higher up: there B is the key above A.')
# 15 Amazing Grace (her 27 Nov 14:05: a bass C with G and A, three keys): the left hand sits on low C, G and A. G and A are its tune notes, as before;
# C is the bass on beat 1 under the C and F bars, G under the G bars. The song ends on the bass C.
d = json.load(open('mb15.json')); g = d['gig']; flat = [b for ln in g['song_grid'] for b in ln]
for b, x in zip(flat, ['', 'C', 'C', 'C', '', 'C', 'C', 'G', 'G', 'C', 'C', 'C', '', 'C', 'G', 'C']):
    assert not (x and b['r'].split()[0].startswith('<')), b['r']
    b['l'] = x
assert len(flat) == 16
g['fmap'] = {'c': 5, 'g': 2, 'a': 1}; g['today'] = 'Roots'
g['tool_cap'] = 'Finger 5 on the low C, 2 on G, thumb on A. C is the bass; G and A join in the tune.'
g['r_cap'] = 'Thumb on middle C, 5 on G. No F in this song.'
g['song_how'] = 'Slow, in three. A line holds the note; it can carry on into the next bar. A boxed letter is the bass: play it on beat 1 and let it ring.'
json.dump(d, open('mb15.json', 'w'), ensure_ascii=False)
# 16 Goin' Home (27 Nov): pitches identical to two transcriptions (flutetree.org songbook, ABC, Largo theme; carvedculture letter notes).
# The rhythm was wrong: the book had four even notes where the theme is long-short (dotted crotchet, quaver). Fixed from the flutetree ABC:
# c3 e e4 | c3 B A4 | B3 c e3 c | B8 || c3 e e4 | c3 B A4 | B2 c2 B3 A | A8, moved to C. The left hand rocks bottom, top: a slow Zigzag.
d = json.load(open('mb16.json')); g = d['gig']
new = [[('E -.G G -', 'Go- -.in’ home -'), ('E -.D C -', 'go- -.in’ home -'), ('D -.E G -.E', 'I’m -.a go- -.in’'), ('D - - -', 'home - - -')],
       [('E -.G G -', 'Qui- -.et- like -'), ('E -.D C -', 'some -.still day -'), ('D E D -.C', 'I’m jes’ go- -.in’'), ('C - - -', 'home - - -')]]
for ln, nl in zip(g['song_grid'], new):
    assert len(ln) == len(nl)
    for b, (r, w) in zip(ln, nl): b['r'] = r; b['w'] = w
g['today'] = 'Zigzag'
json.dump(d, open('mb16.json', 'w'), ensure_ascii=False)
