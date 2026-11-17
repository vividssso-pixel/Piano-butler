# Her 17 Nov ("a"): the second round after the whole-book proofread. Two notation errors, the sus labels, the
# interval-song wording, anticipation in the Part X title, 8va (never taught in the book) out of the glossary, index and
# Workbook, and the first Workbook key filled in. Runs on the already fixed sources (outputs/pilot).
import re, sys
S = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/outputs/pilot'
P = {'harmony': f'{S}/harmony-pilot.html', 'play': f'{S}/play-pilot.html', 'chords': f'{S}/chords-pilot.html', 'further': f'{S}/further-pilot.html',
     'front': f'{S}/full/front.html', 'gloss': f'{S}/full/glossary.html', 'wbpitch': f'{S}/wb/pitch.html', 'wbscales': f'{S}/wb/scales.html', 'pitch': f'{S}/pitch-pilot.html'}
def edit(k, fn):
    h = open(P[k]).read(); h2 = fn(h); assert h2 != h, k; open(P[k], 'w').write(h2)
def rep(k, a, b, n=1):
    def f(h):
        assert h.count(a) == n, (k, a[:60], h.count(a)); return h.replace(a, b)
    edit(k, f)

# p. 111: the block chord was a minim alone in a 4/4 bar (2 beats short): make it a semibreve chord (no stem)
semi = re.search(r'<symbol id="E0A2-1ggprgx".*?</symbol>', open(P['pitch']).read(), re.S).group(0).replace('E0A2-1ggprgx', 'E0A2-ed3j1m')
def block(h):
    i = h.index('Same chord, three shapes'); j = h.index('<svg', i); k = h.index('</svg></div>', j); s = h[j:k]
    s = s.replace('</defs>', semi + '</defs>', 1)
    c0 = s.index('class="chord"'); c1 = s.index('class="note"', c0); c2 = s.index('</g>\n                     </g>', c1) if '</g>\n                     </g>' in s[c1:] else None
    seg = s[c0:c0 + 2400]
    seg2 = re.sub(r'<g id="[^"]+" class="stem">\s*<path [^>]*/>\s*</g>', '', seg, count=1)
    seg2 = seg2.replace('#E0A3-ed3j1m', '#E0A2-ed3j1m', 3)
    assert seg2 != seg and seg2.count('#E0A2-ed3j1m') == 3
    return h[:j] + s[:c0] + seg2 + s[c0 + 2400:] + h[k:]
edit('harmony', block)

# p. 128: eight crotchets under 4/4 with no bar line in between: a scale shown without a time signature
def nometer(h):
    i = h.index('Thumb under, finger over</h3>')
    for _ in range(2):
        m = re.search(r'<g id="[^"]+" class="meterSig">.*?</g>', h[i:], re.S); h = h[:i + m.start()] + h[i + m.end():]; i += m.start()
    return h
edit('play', nometer)

# p. 94: the sus2 / sus4 labels sat on the keyboard's bottom line: below it, with room in the picture
def sus(h):
    h = h.replace('y="118" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#e4572e">sus2</text>', 'y="134" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#e4572e">sus2</text>')
    h = h.replace('y="118" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#e4572e">sus4</text>', 'y="134" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#e4572e">sus4</text>')
    i = h.index('>sus2</text>'); j = h.rfind('<svg', 0, i)
    return h[:j] + h[j:i].replace('<svg viewBox="-2 -2 284 124" style="display:block;margin:0 auto;max-width:100%;height:116px">', '<svg viewBox="-2 -2 284 142" style="display:block;margin:0 auto;max-width:100%;height:133px">', 1) + h[i:]
edit('chords', sus)

# p. 133: Twinkle's 5th is from its 2nd note to its 3rd, so "the first two notes" was not true for every song
rep('play', '<th>The first two notes of…</th>', '<th>The opening of…</th>')
rep('play', 'Naming the interval from the song’s whole tune: only the first two notes count.', 'Naming the interval from the song’s whole tune: only its opening leap counts.')

# Part X teaches five non-chord notes: the title and contents name all five
for k, n in (('front', 2), ('further', 3)):
    rep(k, 'passing, auxiliary, appoggiatura, suspension<', 'passing, auxiliary, appoggiatura, suspension, anticipation<', n)

# 8va is never explained in the book: out of the glossary, the index and the Workbook check
rep('gloss', '<p><b>8va (ottava)</b> play the notes under the dotted line an octave higher <i>p.&#8202;30</i></p>', '')
rep('gloss', '<p><b>8va (ottava)</b> 30</p>', '')
rep('wbpitch', '8va over the notes means play them an octave higher.', 'A ledger line is a short line added above or below the staff.')   # still true: the key stays T

# Workbook p. 73: "The first is done" now shows both answers
edit('wbscales', lambda h: re.sub(r'(<b class="done2">G</b></span>)(\s+minor\s+)<span class="wl"></span>', r'\1\2<span class="wl"><b class="done2">E</b></span>', h, count=1))
print('round 2 applied')
