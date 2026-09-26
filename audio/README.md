# Audio for drills.html

- `piano/` -- grand piano samples (every minor third, A1 and C2-C7), trimmed to 3.5 s, mono 64 kbps.
  Source: tonejs-instruments piano samples, npm package `tonejs-instrument-piano-mp3` 1.1.2
  (Makefully-Studios/tonejs-instruments), MIT licence.
- `count/` (optional) -- recorded counting voice: `1.mp3` ... `8.mp3` and `and.mp3`. If these files
  exist, "Count: Voice" uses them (sample-accurate); otherwise it uses the device's speech voice.
