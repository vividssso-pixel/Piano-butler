# Audio for drills.html

- `piano/` -- grand piano samples (every minor third, A1 and C2-C7), trimmed to 3.5 s, mono 64 kbps.
  Source: tonejs-instruments piano samples, npm package `tonejs-instrument-piano-mp3` 1.1.2
  (Makefully-Studios/tonejs-instruments), MIT licence.
- `count/` -- counting voice: `1.wav` ... `8.wav` and `and.wav` (22 kHz mono WAV, ~20 KB each).
  Generated with the Kokoro-82M text-to-speech model (voice `af_heart`, Apache 2.0 licence) via
  `kokoro-onnx`. Each file is trimmed so the vowel -- where the ear hears the beat -- is ~80 ms in;
  drills.html measures that point at load time and starts the file early by that much, so the
  spoken count lands exactly on the beat. To use your own recordings, replace these files
  (`.wav`, or `.mp3` with the same names); the timing adjusts itself.
