#!/usr/bin/env python3
# Phase 450 on the site: the posture guide's round-hand section gets the thumb in and out and one-plays-the-others-balance,
# and its thumb drawing shows where the thumb goes in (the Lesson Book's new picture).
#   python3 site450.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
p = os.path.join(root, 'tools/lessons/src/posture-hands.html'); s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('posture-hands.html: found %d: %s' % (s.count(a), a[:70]))
    s = s.replace(a, b)
rep('"updated": "2026-10-08"', '"updated": "2026-10-12"')
rep('Updated 8 October 2026</p>', 'Updated 12 October 2026</p>')
rep("""      <li><b>The thumb bends in</b> and plays on the side of its tip, like a tipped boat.</li>
    </ul>""", """      <li><b>The thumb bends in</b> and plays on the side of its tip, like a tipped boat.</li>
      <li><b>One plays, the others balance:</b> one finger at a time goes down into its key, and the others rest on their keys and keep the hand balanced.</li>
      <li><b>Thumb in and out:</b> check the thumb is free. It slides in under fingers 2, 3 and 4 and back out, while the hand stays round and still.</li>
    </ul>""")
rep("<p>The thumb seen from the front of the keyboard: it bends in, and the side of its tip touches the key.</p>",
    "<p>The thumb seen from the front of the keyboard: it bends in, and the side of its tip touches the key. In light coral, where it goes when it slides in under the fingers, before it comes back out.</p>")
rep("<li>The thumb plays on the side of its tip</li>", "<li>The thumb plays on the side of its tip, and slides in and out freely</li>")
open(p, 'w', encoding='utf-8').write(s); print('tools/lessons/src/posture-hands.html: thumb in and out, one plays the others balance')
shutil.copyfile(os.path.join(x, 'svg/posture-hands/thumb.svg'), os.path.join(root, 'tools/lessons/svg/posture-hands/thumb.svg')); print('copy tools/lessons/svg/posture-hands/thumb.svg')
