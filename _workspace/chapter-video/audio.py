import json, numpy as np, wave
tl=json.load(open('timeline.json')); SR=44100; dur=tl['duration']
out=np.zeros(int(SR*dur)+SR)
def midi_of(s):
    o=s//7; d=s%7; return 60+o*12+[0,2,4,5,7,9,11][d]
def tone(m, length=2.6, vel=0.8):
    f=440*2**((m-69)/12); t=np.arange(int(SR*length))/SR
    y=np.zeros_like(t); B=0.0004
    for k in range(1,10):
        fk=f*k*np.sqrt(1+B*k*k)
        if fk>SR/2.2: break
        a=(1/k**1.1)*(1 if k<4 else 0.6)
        dec=0.9+0.45*k+ (f/600)
        y+=a*np.sin(2*np.pi*fk*t)*np.exp(-t*dec)
    att=np.minimum(1,t/0.004); rel=np.minimum(1,(length-t)/0.25)
    y*=att*rel
    # low notes a bit louder for balance
    return y*vel*(1.25 if m<48 else 1.0)
def add(t0,m,vel=0.8,length=2.6):
    y=tone(m,length,vel); i=int(t0*SR); out[i:i+len(y)]+=y
for sc in tl['scenes']:
    for n in sc.get('notes',[]): add(n[0], midi_of(n[1]))
# title: a little climb out of the staff
for t0,m in [(1.2,72),(1.55,76),(1.9,79),(2.4,84)]: add(t0,m,0.45)
mid=[x for x in tl['scenes'] if x['id']=='middle'][0]; add(mid['arrowAt'],60,0.35)
# end: soft C major chord
end=[x for x in tl['scenes'] if x['id']=='end'][0]
for m in (48,60,64,67,72): add(end['ctaAt']+1.2,m,0.3,3.2)
out=out/np.max(np.abs(out))*0.32
import soundfile as sf, os
if os.path.exists('voice.wav'):
    v,vsr=sf.read('voice.wav'); from scipy.signal import resample_poly
    v=resample_poly(v,147,80)  # 24000 -> 44100
    v=v/np.max(np.abs(v))*0.85
    out[:len(v)]+=v[:len(out)]
out=out/max(1,np.max(np.abs(out))/0.95)
# fade out the last 0.6 s
n=int(SR*dur); out=out[:n]; out[-int(SR*0.6):]*=np.linspace(1,0,int(SR*0.6))
pcm=(out*32767).astype(np.int16); st=np.column_stack([pcm,pcm]).ravel()
w=wave.open('audio.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
print('ok')
