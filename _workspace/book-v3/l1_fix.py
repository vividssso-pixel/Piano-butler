# Her 17 Nov: "Piano finger numbers and fingering" jumped into scale fingering too soon. Here: the finger numbers, with a
# picture to hold them by (a mirror), the left/right mix-up, and how to plan fingering (a finger belongs to the music, not
# the key: follow printed fingering, otherwise plan it from the score before playing so the hand never has to twist).
# Thumb under and finger over stay only as an Extra pointer: scales come later. Same pages, same page count.
import re, sys
S = sys.argv[1]
def edit(f, fn):
    p = f'{S}/{f}'; h = open(p).read(); h2 = fn(h); assert h2 != h, f; open(p, 'w').write(h2)
def rep(f, a, b, n=1):
    def g(h):
        assert h.count(a) == n, (f, a[:70], h.count(a)); return h.replace(a, b)
    edit(f, g)

# ---------- Handbook p. 127: the mirror ----------
rep('play-pilot.html', '<p class="hcap">Thumbs are 1 in both hands</p>', '<p class="hcap">Thumbs are 1 in both hands: like a mirror, both count out from the thumbs</p>')

# ---------- Handbook p. 128: plan your fingering (was: thumb under, finger over) ----------
NEW128 = ('<h3>Plan your fingering</h3>'
 '<p>A finger number belongs to the <b>music</b>, not to the key. The same C can be finger 1 in one bar and finger 3 in the next: it depends on where the hand has to go after it.</p>'
 '<table class="ht"><colgroup><col style="width:36%"><col style="width:64%"></colgroup><thead><tr><th>On the page</th><th>What you do</th></tr></thead><tbody>'
 '<tr><td><b>Finger numbers printed</b></td><td>Follow them: the plan is already made for you.</td></tr>'
 '<tr><td><b>No numbers</b></td><td>Plan before you play. Look ahead: where must the hand be for the highest and the lowest notes? Choose fingers that get it there without twisting.</td></tr>'
 '<tr><td><b>More than five notes in a row</b></td><td>Plan where the hand moves: at a rest, a gap or a repeated note. Scales have their own pattern (Major scales, p.&#8202;75).</td></tr>'
 '<tr><td><b>A leap</b></td><td>Move the whole hand; do not stretch the fingers apart.</td></tr>'
 '</tbody></table>'
 '<p>Write your plan in pencil above the notes, then play it the same way every time, so the hand learns it.</p>'
 '<div class="xlate" data-cat="1"><div class="xbox"><p><b>Extra · thumb under, finger over.</b> In a scale the thumb passes under the hand to keep going: right hand up C major, 1 2 3, thumb under to F, then 1 2 3 4 5. You will meet it with the scales.</p></div></div>'
 '<div data-cat="4" class="watch"><div class="bh trapst">Trap</div>'
 '<div class="wr"><span class="x">✗</span><span>Mixing up the hands: both thumbs are 1, so from C up the left hand plays 5 4 3 2 1, not 1 2 3 4 5.</span></div>'
 '<div class="wr"><span class="x">✗</span><span>Changing fingering every time you play: choose one, write it in, keep it.</span></div></div>')
def p128(h):
    i = h.index('<h3>Thumb under, finger over</h3>'); j = h.index('<div data-cat="9" class="plinks">', i)
    return h[:i] + NEW128 + h[j:]
edit('play-pilot.html', p128)

# ---------- Workbook p. 128: Which hand? (was: C major, right hand) ----------
def wb128(h):
    i = h.index('<b>C major, right hand</b>'); a = h.rfind('<div class="ex2"', 0, i); b = h.index('</table></div>', i) + len('</table></div>')
    new = ('<div class="ex2" data-op="109" data-u="109-3"><div class="eh"><span class="en">3</span><b>Which hand?</b><span class="el">★★<span class="so">★</span></span></div>'
           '<p class="how">Five-finger position on C D E F G. Circle the hand that plays each note with that finger. The first is done.</p>'
           '<div class="row"><b>finger 1 on C</b><span class="tf"><b class="done2 ringd">right</b>  ·  left</span></div>'
           '<div class="row"><b>finger 5 on C</b><span class="tf">right  ·  left</span></div>'
           '<div class="row"><b>finger 1 on G</b><span class="tf">right  ·  left</span></div>'
           '<div class="row"><b>finger 5 on G</b><span class="tf">right  ·  left</span></div></div>')
    return h[:a] + new + h[b:]
edit('wb/play.html', wb128)

# ---------- Workbook p. 129: plan it (was: under or over; C major left hand; thumb landing; the scale) ----------
def wb129(h):
    i = h.index('<b>Under or over?</b>'); a = h.rfind('<div class="ex2"', 0, i)
    j = h.index('<b>C major, left hand</b>', i); b = h.index('</table></div>', j) + len('</table></div>')
    new = ('<div class="ex2" data-op="110" data-u="110-0"><div class="eh"><span class="en">1</span><b>What do you do?</b><span class="el">★★<span class="so">★</span></span></div>'
           '<p class="how">Circle what you do before you play. The first is done.</p>'
           '<div class="row"><b>The fingering is printed.</b><span class="tf"><b class="done2 ringd">follow it</b>  ·  make up your own</span></div>'
           '<div class="row"><b>No fingering is printed.</b><span class="tf">plan it first  ·  choose as you go</span></div>'
           '<div class="row"><b>The tune goes past five notes.</b><span class="tf">plan where the hand moves  ·  stretch</span></div>'
           '<div class="row"><b>The tune leaps a long way.</b><span class="tf">move the whole hand  ·  stretch</span></div></div>'
           '<div class="ex2" data-op="110" data-u="110-1"><div class="eh"><span class="en">2</span><b>Write it in</b><span class="el">★★<span class="so">★</span></span></div>'
           '<p class="how">Right hand in five-finger position on C. Write the finger for each note. The first is done.</p>'
           '<table class="ht bld"><colgroup><col style="width:16%"/><col style="width:14%"/><col style="width:14%"/><col style="width:14%"/><col style="width:14%"/><col style="width:14%"/><col style="width:14%"/></colgroup>'
           '<thead><tr><th></th><th>C</th><th>E</th><th>D</th><th>F</th><th>E</th><th>G</th></tr></thead><tbody><tr><td><b>finger</b></td><td><b class="done2">1</b></td>'
           + '<td><span class="ab"></span></td>' * 5 + '</tr></tbody></table></div>')
    h = h[:a] + new + h[b:]
    h = h.replace('The thumb should land heavily as it passes under.', 'A finger number always belongs to the same key.', 1)   # still F: the key stays F, T, F
    h = h.replace('Play the C major scale, one octave, each hand alone. Tick a circle each clean day.', 'Take a short piece you know: plan the fingering, pencil it in, then play it the same way three times. Tick a circle each day.', 1)
    return h
edit('wb/play.html', wb129)
rep('wb/play.html', 'C major up: 1 2 3 1 2 3 4 5.', 'Which hand: right, left, left, right.')
rep('wb/play.html', 'Under or over: thumb under, finger over, finger over, thumb under. Left hand up: 5 4 3 2 1 3 2 1.', 'What do you do: follow it, plan it first, plan where the hand moves, move the whole hand. Write it in: 1 3 2 4 3 5.')
rep('wb/play.html', '<td>scale fingering</td>', '<td>planning your fingering</td>')
print('L1 reworked')
