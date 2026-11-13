# appends "Behind the next door…" to each story track (her 14 Nov: make them want the next one)
import sys, os, subprocess
sys.argv = [sys.argv[0]]; sys.path.insert(0, '/tmp/claude-0/tts')
import numpy as np, audio as A
A.VOICE['N'] = ('bf_alice', 0.95)
G = {}; exec(open('/tmp/claude-0/lvl/tease.py').read(), G)
OUT = '/mnt/user-data/outputs/audio-stories'; SRC = '/tmp/claude-0/storyroom/audio'
for rid, t in G['TEASE'].items():
    w = A.render([('pause', 0.6), ('N', 'Behind the next door.'), ('N', t.replace('“', '').replace('”', '')), ('piano', 'pp:G4 pp:C5*2')], None)
    A.mp3(w, f'/tmp/claude-0/tts/tz-{rid}.mp3')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{SRC}/{rid}.mp3', '-i', f'/tmp/claude-0/tts/tz-{rid}.mp3', '-filter_complex', '[0:a][1:a]concat=n=2:v=0:a=1', '-codec:a', 'libmp3lame', '-qscale:a', '4', f'{OUT}/{rid}.mp3'], check=True)
    print(rid, flush=True)
