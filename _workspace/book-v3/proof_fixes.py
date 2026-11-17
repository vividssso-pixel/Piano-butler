# Her 17 Nov ("a": proofread both books end to end). Fixes from the seven-reader proofread, applied to the built book
# HTML (the part generators were lost with the old workspace; the built HTML is now the source). Every replacement must
# match exactly the expected number of times, or the script stops.
import re, sys
S = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/rb/src'
done = []
def rep(f, old, new, n=1):
    p = f'{S}/{f}'; h = open(p).read(); c = h.count(old)
    for sp in ('\xa0', '\u2009', '\u200a'):   # the books print "p." with a no-break or thin space before the number
        if c != n and h.count(old.replace('p. ', 'p.' + sp)) == n:
            old, new = old.replace('p. ', 'p.' + sp), new.replace('p. ', 'p.' + sp); c = n
    if c != n: raise SystemExit(f'{f}: expected {n}, found {c}: {old[:70]}')
    open(p, 'w').write(h.replace(old, new)); done.append((f, old[:50]))
def resub(f, pat, new, n=1, flags=0):
    p = f'{S}/{f}'; h = open(p).read(); h2, c = re.subn(pat, new, h, flags=flags)
    if c != n: raise SystemExit(f'{f}: regex expected {n}, found {c}: {pat[:70]}')
    open(p, 'w').write(h2); done.append((f, pat[:50]))

# ---------- Handbook: front matter and Before you play ----------
rep('before.html', 'Fingering p. 163 · Practising well p. 165', 'Piano finger numbers and fingering p. 127 · How to practise piano p. 129')
rep('before.html', 'Workbook pp. 5–6 · Online: Posture & Hand Shape', 'Workbook · Before you play · Posture and hand shape · drills in the app')
rep('before.html', 'The worked examples, the tunes to play and the games are in', 'Most worked examples, the tunes to play and the games are in')
resub('before.html', r'<text[^>]*>elbow leads</text>', '')                       # printed at about 4 px: unreadable
resub('before.html', r'<text[^>]*>sitting back: room for the arm to travel</text>', '')
rep('front.html', '<b>Before you play</b>, p. 18,', '<b>Before you play</b>, p. 17,')
rep('front.html', 'Seventh chords and slash chords, and cadences by ear.', 'Seventh chords and slash chords.')
rep('front.html', 'Ask one question.</b> "What do you remember?"', 'Ask one question.</b> “What do you remember?”')
rep('front.html', 'Ask: "Show me."', 'Ask: “Show me.”')

# ---------- Handbook: Parts I to III ----------
rep('pitch-pilot.html', '<b>bar lines</b> (Bar lines).', '<b>bar lines</b> (Bar lines, p. 55).')
rep('pitch-pilot.html', 'it lasts the whole piece (Key signatures).', 'it lasts until it is changed, usually the whole piece (Key signatures, p. 78).')
rep('pitch-pilot.html', 'Interval numbers from C</h3>\n<figure class="vx px">', 'Interval numbers from C</h3>\n<figure class="vx px nogrow">')   # the auto-grow made this stave wider than its frame
rep('time-pilot.html', 'are explained in Speed words.</p>', 'are explained in Speed words, p. 64.</p>')
rep('time-pilot.html', 'Notes shorter than one beat also have a <b>flag</b>', 'Quavers and shorter notes also have a <b>flag</b>')
rep('time-pilot.html', 'it holds until the next one.', 'it holds until the next time signature.')
rep('time-pilot.html', 'felt as a long group and a short one.', 'felt in uneven groups of twos and threes.')
rep('time-pilot.html', 'Five or seven counts, felt in uneven groups: 3 + 2, or 4 + 3.', 'Five or seven counts, felt in uneven groups: 3 + 2, or 2 + 2 + 3.')
rep('time-pilot.html', '<p class="hcap">Five counts: one long group and one short</p>', '<p class="hcap">Uneven groups: 3 + 2 in five, 2 + 2 + 3 in seven</p>')
rep('time-pilot.html', 'first time play the 1. bar; after the repeat skip it and play the 2. bar', 'first time, play the 1st-time bar; after the repeat, skip it and play the 2nd-time bar')
rep('time-pilot.html', '<span><b>One beam, one beat.</b></span>', '<span><b>Beams show the beats. Never beam across the middle of a 4/4 bar.</b></span>')
rep('time-pilot.html', '<p class="hcap">One beam, one beat</p>', '<p class="hcap">Beams show the beats</p>')

# ---------- Handbook: Parts IV to VI ----------
rep('chords-pilot.html', 'the chord names over a song are all triads.', 'the chord names over a song are mostly built from triads.')
rep('scales-pilot.html', 'Now the same three forms on A, the first minor scale with no sharps or flats.', 'Now the same three forms on A, the one minor scale with no sharps or flats.')
rep('expression-pilot.html', 'six ways are shown below.', 'six ways are shown on p. 69.')
rep('expression-pilot.html', 'is explained in Pulse and tempo.</p>', 'is explained in Pulse and tempo, p. 43.</p>')
rep('expression-pilot.html', '(Rhythm: off the beat) <span class="ex">', '(Rhythm: off the beat, p. 52) <span class="ex">')
rep('chords-pilot.html', '(Major, minor and perfect).</p>', '(Major, minor and perfect, p. 37).</p>')
rep('chords-pilot.html', 'Which ones belong to a key: Chords in a key.', 'Which ones belong to a key: Chords in a key, p. 89.')
rep('chords-pilot.html', 'More on the bass note in Slash chords.', 'More on the bass note in Slash chords, p. 100.')
rep('chords-pilot.html', 'nothing else (9th, 11th and 13th chords).', 'nothing else (9th, 11th and 13th chords, p. 98).')
rep('chords-pilot.html', 'smoother changes (Inversions)', 'smoother changes (Inversions, p. 91)')
rep('chords-pilot.html', ' The chords change while the C stays.', '')
rep('chords-pilot.html', '<figcaption>On the staff: three lines in a row (or three spaces).</figcaption>', '<figcaption>Root, 3rd, 5th</figcaption>')
rep('chords-pilot.html', '“Like a wedding chord for a giant.”', '“Like a wedding cake for a giant.”')

# ---------- Handbook: glossary and index ----------
rep('glossary.html', 'leans on the beat (p. 175)', 'leans on the beat (p. 139)')
resub('glossary.html', r'(<b>Alberti bass</b> a broken chord in the left hand: low, high, middle, high \(C G E G\) <i>p\.&#8202;)119', r'\g<1>111')
rep('glossary.html', '<b>Alberti bass</b> 119, 110, 124', '<b>Alberti bass</b> 111, 119, 124')
rep('glossary.html', '<b>cantabile</b> in a singing style <i>p.&#8202;61</i>', '<b>cantabile</b> in a singing style <i>p.&#8202;67</i>')
rep('glossary.html', '<b>dolce</b> sweetly <i>p.&#8202;61</i>', '<b>dolce</b> sweetly <i>p.&#8202;67</i>')
rep('glossary.html', '<b>cantabile</b> 61, 62', '<b>cantabile</b> 67')
rep('glossary.html', '<b>dolce</b> 61, 62', '<b>dolce</b> 67')
rep('glossary.html', '<b>mood words</b> 61, 62', '<b>mood words</b> 67')
rep('glossary.html', 'one key below home <i>p.&#8202;75</i>', 'one key below home <i>p.&#8202;89</i>')
rep('glossary.html', 'the 1st note of the scale: home <i>p.&#8202;75</i>', 'the 1st note of the scale: home <i>p.&#8202;89</i>')
rep('glossary.html', '<b>degree names</b> 75', '<b>degree names</b> 89')
rep('glossary.html', '<b>leading note</b> 75, 89', '<b>leading note</b> 89')
rep('glossary.html', '<b>tonic</b> 75, 89', '<b>tonic</b> 85, 89')
rep('glossary.html', '<b>thumb under</b> 127', '<b>thumb under</b> 128')
rep('glossary.html', '<b>sonata form</b> 122', '<b>sonata form</b> 123')
rep('glossary.html', '<p><b>duplet</b> two notes in the time of three <i>p.&#8202;51</i></p>', '')     # not taught in the book
rep('glossary.html', '<p><b>duplet</b> 51, 49</p>', '')
rep('glossary.html', '<b>triplet</b> 51, 49, 50', '<b>triplet</b> 51, 52, 53')
rep('glossary.html', '<b>metronome</b> 129, 43, 65', '<b>metronome</b> 43, 64, 130')
rep('glossary.html', '<b>semiquaver</b> 39, 44, 50, 129', '<b>semiquaver</b> 39, 40, 44, 51')
rep('glossary.html', 'given back, for expression <i>p.&#8202;52</i>', 'given back, for expression <i>p.&#8202;53</i>')
rep('glossary.html', '<b>rubato</b> 52', '<b>rubato</b> 53, 65')
rep('glossary.html', 'I I I I · IV IV I I · V IV I I (or V in the last bar', 'I I I I · IV IV I I · V IV I V (or I in the last bar')
rep('glossary.html', 'the major scale on the same note with 3, 6 and 7 one key lower', 'the major scale on the same note with 3, 6 and 7 one key lower (natural minor); the harmonic and melodic minors raise the 7th again')

# ---------- Workbook ----------
W = 'wb/'
# Review answers: label each Review row with its own page; the Review pages point to the right answer page
for f, pg in (('time.html', 51), ('expression.html', 68), ('scales.html', 77), ('harmony.html', 108), ('shape.html', 125), ('play.html', 140)):
    rep(W + f, '<tr><td>p. 25</td>', f'<tr><td>p. {pg}</td>')
rep(W + 'pitch.html', 'Mark it with the answers on page 27.', 'Mark it with the answers on page 28.')
rep(W + 'harmony.html', 'Mark it with the answers on page 111:', 'Mark it with the answers on page 110:')
rep(W + 'pitch.html', 'Before you play: 1 thumb 1, index 2, middle 3, ring 4, little 5 · 2 B ·', 'Before you play: 1 thumb 1, index 2, middle 3, ring 4, little 5 · 2 C ·')
# answers filed under the wrong page
def move(f, frm, to, text):
    p = f'{S}/{W}{f}'; h = open(p).read()
    a = re.search(r'(<tr><td>' + re.escape(frm) + r'</td><td>)(.*?)(</td></tr>)', h); b = re.search(r'(<tr><td>' + re.escape(to) + r'</td><td>)(.*?)(</td></tr>)', h)
    assert a and b and text in a.group(2), (f, frm, to, text)
    h = h.replace(a.group(0), a.group(1) + a.group(2).replace(text, '').replace('  ', ' ').replace(' .', '.').strip() + a.group(3), 1)
    b = re.search(r'(<tr><td>' + re.escape(to) + r'</td><td>)(.*?)(</td></tr>)', h)
    h = h.replace(b.group(0), b.group(1) + text.strip() + ' ' + b.group(2) + b.group(3), 1)
    open(p, 'w').write(h); done.append((f, f'{frm}->{to}'))
move('pitch.html', 'p. 21', 'p. 20', 'S, T, S, T, T, T. ')
rep(W + 'pitch.html', '<td>S, T, S, T, T, T. Find them:', '<td>Tone or semitone: S, T, S, T, T, T. Find them:')
move('pitch.html', 'p. 16', 'p. 17', 'First ledger lines: Middle C, A, E. ')
move('time.html', 'p. 39', 'p. 41', '5/4: 1 2 3 1 2. 7/8: 1 2 1 2 1 2 3. ')
move('time.html', 'p. 40', 'p. 41', '3 + 3 + 2: 1 2 3 1 2 3 1 2. ')
move('expression.html', 'p. 63', 'p. 64', 'Clean or muddy: clean, muddy, a gap, clean. ')
move('scales.html', 'p. 74', 'p. 73', 'Sharps F C G D A E B; flats B E A D G C F. ')
move('harmony.html', 'p. 80', 'p. 81', 'Lines or spaces: lines, spaces, lines. ')
move('harmony.html', 'p. 82', 'p. 83', 'Draw: major D F♯ A, A C♯ E, E G♯ B; minor C E♭ G, G B♭ D, F A♭ C. ')
move('harmony.html', 'p. 84', 'p. 86', 'I IV V: G C D · F B♭ C · D G A. ')
rep(W + 'harmony.html', '<td>V and vii°: A C♯ E · B D F · F♯ A C.</td>', '<td>V and vii°: A C♯ E · B D F · F♯ A C. Check it: T, F, T, T.</td>')
move('harmony.html', 'p. 93', 'p. 94', 'With or without: C6, C13, Cadd9, C9. ')
move('harmony.html', 'p. 95', 'p. 96', 'Walk the bass: G/B, C/G. ')
move('play.html', 'p. 134', 'p. 136', 'Songs (or any that fit): Frère Jacques · Oh When the Saints · Amazing Grace · Somewhere over the Rainbow. ')
rep(W + 'harmony.html', 'Top floor: B, B♭, G, F, E.', 'Add the top layer: B, B♭, G, F, E.')
# progress tables: the Handbook column follows the new chapters
PROG = {'pitch.html': [22, 25, 27, 28, 30, 32, 34, 37],
        'time.html': [43, 55, 39, 41, 44, 46, 48, 49, 51, 50, 52, 52, 52, 56, 57],
        'expression.html': [59, 60, 61, 67, 64, 65, 68, 70],
        'scales.html': [75, 89, 76, 78, 80, 82],
        'harmony.html': [85, 87, 89, 91, 92, 94, 98, 100, 104, 108, 110, 112],
        'shape.html': [115, 116, 117, 119, 121, 122, 124],
        'play.html': [127, 128, 129, 129, 131, 133, 132, 134]}
for f, pages in PROG.items():
    p = f'{S}/{W}{f}'; h = open(p).read(); i = h.index('My progress'); j = h.index('</table>', i)
    seg = h[i:j]; cells = re.findall(r'<td>p\.[ \xa0\u2009\u200a]\d+</td>', seg)
    assert len(cells) == len(pages), (f, len(cells), len(pages))
    it = iter(pages); seg2 = re.sub(r'<td>p\.([ \xa0\u2009\u200a])\d+</td>', lambda m: f'<td>p.{m.group(1)}{next(it)}</td>', seg)
    open(p, 'w').write(h[:i] + seg2 + h[j:]); done.append((f, 'progress pages'))
# references and wording
rep(W + 'time.html', 'Bars 3–4 of Beethoven’s Ode to Joy (Handbook p. 57).', 'Bars 3–4 of Beethoven’s Ode to Joy (Handbook p. 116).')
rep(W + 'time.html', '<p class="rem2"><span>Remember</span>One beam, one beat.</p>', '<p class="rem2"><span>Remember</span>Beams show the beats. Never beam across the middle of a 4/4 bar.</p>')
rep(W + 'time.html', 'Write the letters of map 3 above in the order you play them.', 'Write the letters of map 3 in exercise 4 on page 48 in the order you play them.')
rep(W + 'pitch.html', 'On the keyboard, find every semitone with no black key between', 'On the piano, find every semitone with no black key between')
rep(W + 'pitch.html', 'naming the treble notes on page 14 and the bass notes above, out loud.', 'naming the treble and bass notes on page 14, out loud.')
p = f'{S}/{W}expression.html'; h = open(p).read(); k = h.index('Staccato means loud.'); k2 = h.index('Staccato means loud.', k + 5)
h = h[:k2] + 'Legato means short and detached.' + h[k2 + len('Staccato means loud.'):]; open(p, 'w').write(h); done.append(('expression.html', 'second staccato T/F'))
rep(W + 'harmony.html', 'If the notes disagree, pick the cake that holds the notes on beats 1 and 3.', 'If the notes disagree, pick the chord that holds the note on beat 1.')
rep(W + 'harmony.html', 'Which cake holds it?', 'Which chord holds it?')
rep(W + 'harmony.html', 'Circle the cake that holds its notes.', 'Circle the chord that holds its notes.', 2)
rep(W + 'harmony.html', 'The three cakes of G major', 'The three chords of G major')
rep(W + 'harmony.html', 'Story: a plate.', 'Story: C over E.')
for f in ('chords.html', 'expression.html', 'harmony.html', 'pitch.html', 'play.html', 'scales.html', 'shape.html', 'time.html'):   # a Use page has no Remember line of its own
    h = open(f'{S}/{W}{f}').read(); open(f'{S}/{W}{f}', 'w').write(h.replace('The Remember line at the top of the page helps.', 'The Remember line in this chapter helps.')); done.append((f, 'remember hint'))
rep(W + 'chords.html', 'The Handbook says a slash chord is like a cake standing on what?', 'How does the Handbook say C/E out loud?')
rep(W + 'chords.html', 'Mark the notes of Fsus2: 1 on the root, 2 on the note above it, 5 on the 5th.', 'Mark the notes of Fsus2: 1 on the root, 2 on the next letter up (G), 5 on the 5th.')
rep(W + 'play.html', 'the finger for G, right hand, thumb on C', 'the finger for G, right hand, in five-finger position on C')
rep(W + 'shape.html', 'Play the four bars on Handbook p. 154 twice', 'Play the four bars on Handbook p. 121 twice')
rep(W + 'play.html', 'The Handbook’s ladder (p. 165)', 'The Handbook’s ladder (p. 129)')
rep(W + 'shape.html', 'How many times do you hear A altogether, counting the start?', 'How many times do you hear A altogether, counting the start? (Count a repeated section once.)')
print(len(done), 'fixes applied')
