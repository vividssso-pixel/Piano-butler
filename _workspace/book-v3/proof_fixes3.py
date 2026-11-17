# Her 17 Nov ("a"): round three, the smaller points left after the proofread. Runs on the sources after rounds 1 and 2.
# Layout: a fuller, larger Contents; no one-word title lines; the step label off the staff; larger keyboard labels on
# pp. 32, 33 and 37. Content: "finished or not" on p. 132; the glossary's claim matches what it lists; the Workbook's
# Intervals page practises intervals (it repeated the Tones and semitones page); pointers where a page uses a sign or a
# rhythm taught in the next chapter.
import re, sys
S = sys.argv[1]
def edit(f, fn):
    p = f'{S}/{f}'; h = open(p).read(); h2 = fn(h); assert h2 != h, f; open(p, 'w').write(h2)
def rep(f, a, b, n=1):
    def g(h):
        assert h.count(a) == n, (f, a[:70], h.count(a)); return h.replace(a, b)
    edit(f, g)

# Contents: two half-empty pages of 12 px type become two fuller pages of 14.5 px type
rep('front.html', '.ftoc2 .ftr{font-size:12px;padding:1px 0;break-inside:avoid}', '.ftoc2 .ftr{font-size:14.5px;padding:3.5px 0;break-inside:avoid}')
rep('front.html', '.ftoc2 .ftp1{margin:9px 0 2px;break-after:avoid}', '.ftoc2 .ftp1{margin:16px 0 4px;break-after:avoid;font-size:12px}')
# titles: never one word alone on the second line
rep('expression-pilot.html', '<h1>Slowing down and speeding up</h1>', '<h1>Slowing down and speeding&nbsp;up</h1>')
rep('wb/play.html', '<h1>Common piano mistakes and how to fix them</h1>', '<h1>Common piano mistakes and how to fix&nbsp;them</h1>')
# p. 36: the "step" label sat on the top staff line
rep('pitch-pilot.html', 'text-anchor="middle" x="160.0" y="47.0">step</text>', 'text-anchor="middle" x="160.0" y="40.0">step</text>')
# pp. 32 and 37: keyboard key labels a quarter larger (p. 33's captions would run into each other)
def bigger(h):
    secs = re.findall(r'<section\b.*?</section>', h, re.S)
    for s in secs:
        m = re.search(r'class="foot"><span>(\d+)', s)
        if m and m.group(1) in ('32', '37'):
            s2 = re.sub(r'font-size="([0-9.]+)"', lambda x: f'font-size="{round(float(x.group(1)) * 1.25, 1)}"' if float(x.group(1)) <= 12.5 else x.group(0), s)
            h = h.replace(s, s2)
    return h
edit('pitch-pilot.html', bigger)
# p. 132: the chapter title promises "finished or not"
rep('play-pilot.html', '<div data-cat="4" class="watch"><div class="bh trapst">Trap</div><div class="wr"><span class="x">✗</span><span>Guessing from the hands', '<h3>Finished or not?</h3><p>Listen to the last chord. Music that comes home to I sounds finished, like a full stop; music that stops on V sounds like a question still waiting for its answer (Cadences, p.&#8202;108).</p><div data-cat="4" class="watch"><div class="bh trapst">Trap</div><div class="wr"><span class="x">✗</span><span>Guessing from the hands')
# glossary: it lists the main words, not every word
rep('glossary.html', 'Every musical word in the Handbook, in one line, with the page where it is explained.', 'The main musical words in the Handbook, in one line, with the page where each is explained.')

# Workbook p. 21 (Intervals): practise interval numbers, not semitones again
def intervals(h):
    i = h.index('<b>Up or down</b>'); j = h.index('<div class="ex2" data-op="20"', i)
    seg = h[i:j]
    seg2 = seg.replace('<b>Up or down</b>', '<b>Count the notes</b>')
    seg2 = seg2.replace('Start on the first key, move as asked, and write the key you land on. The first is done.', 'Count the letters, both ends included, and write the interval. The first is done.')
    for a, b in (('E up a semitone</b> <span class="ab hasdone"><b class="done2">F</b>', 'C up to E</b> <span class="ab hasdone"><b class="done2">3rd</b>'), ('F down a semitone', 'D up to A'), ('B up a semitone', 'E up to G'),
                 ('C down a semitone', 'F up to D'), ('D up a tone', 'G up to C'), ('A down a tone', 'A up to the next A'),
                 ('E to F is a semitone.', 'C to E is a 3rd.'), ('C to D is a semitone.', 'C to D is a 3rd.'), ('Two semitones make a tone.', 'An octave spans eight letters, both ends counted.'),
                 ('From every white key, play a semitone up, then a tone up. Say which keys are black. Tick a circle each day.', 'From C, play a 2nd, 3rd, 4th and 5th up, saying each number. Then do the same from G. Tick a circle each day.')):
        assert seg2.count(a) == 1, a; seg2 = seg2.replace(a, b)
    return h[:i] + seg2 + h[j:]
edit('wb/pitch.html', intervals)
rep('wb/pitch.html', 'Up or down: F, E, C, B, E, G. True or false: T, F, T, T. Story: three.', 'Count the notes: 3rd, 5th, 3rd, 6th, 4th, octave. True or false: T, F, T, T. Story: three.')
# Workbook p. 43 (Upbeats) and p. 48 (Repeats): say where the next chapter's signs are taught
rep('wb/time.html', '<p class="how">Triplets and semiquavers: clap with a metronome', '<p class="how">Triplets are taught next (Handbook p. 51); try them here first. Triplets and semiquavers: clap with a metronome')
def repeats(h):
    i = h.index('<h1>Repeats</h1>'); a = '<p class="how">Write what each sign tells you to do.</p>'; j = h.index(a, i)
    return h[:j] + '<p class="how">Write what each sign tells you to do. D.C., D.S., Fine and Coda are on Handbook p. 57, Road signs.</p>' + h[j + len(a):]
edit('wb/time.html', repeats)
print('round 3 applied')
