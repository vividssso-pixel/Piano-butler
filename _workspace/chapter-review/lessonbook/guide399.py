# Phase 399: songs out of the chapter guide pages too (chapters 2 and 3), and the house front page's cards
import sys
root = sys.argv[1]
def edit(p, pairs):
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        assert s.count(a) == 1, (p, a[:60], s.count(a)); s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('ok', p)
edit(root + '/tools/lessons/src/first-steps.html', [
 ('middle C. A first black-key tune and a free printable worksheet."', 'middle C. First legato playing on the black keys, and a free printable worksheet."'),
 ('the whole keyboard and middle C, and a first tune on the black keys"', 'the whole keyboard and middle C, and first legato playing on the black keys"'),
 ('<p>The first tunes need no written notes at all: just the black-key roofs and fingers 2, 3 and 4.', '<p>Playing needs no written notes at all: just the black-key roofs and fingers 2, 3 and 4.'),
 ('<li><div><b>Hot Cross Buns</b>Right hand 2 3 4 on the big roof. One circle is one steady beat.</div>{{beats:4 3 2 - | 4 3 2 - | 2 2 2 2 3 3 3 3 | 4 3 2 -}}</li>',
  '<li><div><b>Roof walk</b>Right hand 2 3 4 on a big roof: up and back, then a little hill, smooth and joined. One circle is one steady beat.</div>{{beats:2 3 4 - | 4 3 2 - | 2 3 4 3 | 2 - - -}}</li>'),
 ('<p style="margin-top:10px">More tunes to play by finger numbers in the online lesson: Mary Had a Little Lamb, Old MacDonald, and Rain Rain Go Away.</p>',
  '<p style="margin-top:10px">Then the echo game: someone plays two or three black keys, and you play them straight back. And make up your own: any black keys, in any order, smooth and joined.</p>'),
 ('\n    <p>For first tunes I reach for Hot Cross Buns, Mary Had a Little Lamb and Old MacDonald: famous, free to use, and everybody already knows how they go.</p>', ''),
 ('<li>I can play Hot Cross Buns legato with 2 3 4</li>', '<li>I can play legato with 2 3 4 on a big roof</li>'),
 ('and play Hot Cross Buns, Mary Had a Little Lamb, Old MacDonald and Rain Rain Go Away by finger numbers.</p>', 'and jam on the black keys with the band.</p>'),
])
edit(root + '/tools/lessons/src/note-names.html', [
 ('skipping a letter, and a first tune read by its letter names. With a free printable worksheet."', 'skipping a letter, and words spelled on the keys. With a free printable worksheet."'),
 ('skipping a letter, and playing a tune by its letter names"', 'skipping a letter, and reading letters straight onto the keys"'),
 ('<p>In the last chapter, Hot Cross Buns lived on the black keys. Now it moves into the small house: right-hand fingers 2, 3 and 4 on C, D and E, and this time the student reads the letters, not the finger numbers. Then the left hand, one small house lower.</p>',
  '<p>Now the letters go straight onto the keys. Right-hand fingers 2, 3 and 4 sit on C, D and E in the small house: read each letter, see its place, play. This time the student reads the letters, not the finger numbers. Then the left hand, one small house lower.</p>'),
 ('<li><div><b>Hot Cross Buns</b>Right hand 2 3 4 on C D E. One circle is one steady beat.</div>{{beats:E D C - | E D C - | C C C C D D D D | E D C -}}</li>',
  '<li><div><b>Read and play</b>Right hand 2 3 4 on C D E, saying the letters. One circle is one steady beat.</div>{{beats:C D E - | E D C - | C E D C | E - C -}}</li>'),
 ('<li>I can play Hot Cross Buns from its letters, legato</li>', '<li>I can read letters and play them: C D E, BAG, CAFE</li>'),
 ('step and skip round the letter chain, and play Hot Cross Buns by its letter names.</p>', 'step and skip round the letter chain, and spell words like BAG and CAFE on the keys.</p>'),
])
edit(root + '/tools/lessons/src/index.html', [
 ('high and low, middle C and a first black-key tune. With a free worksheet.</p>', 'high and low, middle C and first legato playing on the black keys. With a free worksheet.</p>'),
 ('skipping a letter, and a first tune by letter names. With a free worksheet.</p>', 'skipping a letter, and words spelled on the keys. With a free worksheet.</p>'),
])
