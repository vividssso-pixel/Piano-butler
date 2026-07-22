// AMEB Piano Syllabus 2026 — Technical Work (Preliminary to Grade 8)
// Source: "Piano Syllabus 2026.pdf" (AMEB), Technical Work sections, pp.13-61.
// Transcribed directly from the syllabus PDF on 2026-07-22 (Piano Butler Phase 60).
// Each grade's item count matches the syllabus's own numbering range exactly
// (e.g. Grade 6 = items 6.1-6.23 = 23 scale/arpeggio/chord entries below), which
// was used as an internal consistency check while transcribing.
//
// Structure per grade:
//   label      — display name
//   exercises  — named Technical Exercises (A/B/C), each with a pedagogical purpose
//                and the piece name(s) candidates must prepare
//   sections   — scale/arpeggio/chord requirement groups, in syllabus order
//
// AMEB only. Not applicable to ABRSM or Trinity syllabuses (different technical
// requirements) or to AMEB Diploma grades (CertP/AMusA/LMusA — no fixed technical
// exercise list in the same format).

const DATA_TECHNICAL_AMEB = {
  Prelim: {
    label: 'Preliminary',
    exercises: [
      { code: 'PA', purpose: 'for the development of a stable hand shape', pieces: ['Hide and seek (right hand)', 'Gone again! (left hand)'] },
      { code: 'PB', purpose: 'for smooth passing of the thumb', pieces: ['This little piggy (right hand)', 'Off to market (left hand)'] },
    ],
    sections: [
      { title: 'Scales', items: ['C major - one octave', 'A natural minor - one octave', 'A harmonic minor - one octave', 'G major - one octave', 'E natural minor - one octave', 'E harmonic minor - one octave'] },
      { title: 'Scales in contrary motion', items: ['C major - one octave', 'A harmonic minor - one octave'] },
    ],
  },
  G1: {
    label: 'Grade 1',
    exercises: [
      { code: '1A', purpose: 'for broken triads', pieces: ['A flying leap (right hand)', 'A running jump (left hand)'] },
      { code: '1B', purpose: 'for contrapuntal playing', pieces: ['Waiting for the bell'] },
      { code: '1C', purpose: 'for flexibility (rotation of the forearm)', pieces: ['Running on empty (right hand)', 'Tanking it up! (left hand)'] },
    ],
    sections: [
      { title: 'Scales', items: ['G major - two octaves', 'E natural minor - two octaves', 'E harmonic minor - two octaves', 'F major - two octaves', 'D natural minor - two octaves', 'D harmonic minor - two octaves'] },
      { title: 'Scales in contrary motion', items: ['C major - two octaves', 'A harmonic minor - two octaves', 'G major - two octaves', 'E harmonic minor - two octaves'] },
      { title: 'Chromatic scale', items: ['Commencing on G - one octave'] },
    ],
  },
  G2: {
    label: 'Grade 2',
    exercises: [
      { code: '2A', purpose: 'for thumb passing', pieces: ['Thumb driving (right hand)', 'Bass driver (left hand)'] },
      { code: '2B', purpose: 'for contrapuntal playing', pieces: ['Too tame to tango'] },
      { code: '2C', purpose: 'for broken chords', pieces: ['Take the slow train (right hand)', 'Back track (left hand)'] },
    ],
    sections: [
      { title: 'Scales', items: ['D major - two octaves', 'B natural minor - two octaves', 'B harmonic minor - two octaves', 'B♭ major - two octaves', 'G natural minor - two octaves', 'G harmonic minor - two octaves', 'G melodic minor - two octaves'] },
      { title: 'Scales in contrary motion', items: ['G major - two octaves', 'E harmonic minor - two octaves', 'F major - two octaves', 'D harmonic minor - two octaves'] },
      { title: 'Chromatic scale', items: ['Commencing on D - two octaves'] },
    ],
  },
  G3: {
    label: 'Grade 3',
    exercises: [
      { code: '3A', purpose: 'for the preparation of arpeggios', pieces: ['Whirlygig (right hand)', 'Wind whipper (left hand)'] },
      { code: '3B', purpose: 'for tonal balance', pieces: ['Alone'] },
      { code: '3C', purpose: 'for wrist flexibility', pieces: ['My special place'] },
    ],
    sections: [
      { title: 'Scales', items: ['A major - two octaves', 'F♯ natural minor - two octaves', 'F♯ harmonic minor - two octaves', 'E♭ major - two octaves', 'C natural minor - two octaves', 'C harmonic minor - two octaves', 'C melodic minor - two octaves'] },
      { title: 'Scales in contrary motion', items: ['D major - two octaves', 'B harmonic minor - two octaves', 'B♭ major - two octaves', 'G harmonic minor - two octaves'] },
      { title: 'Chromatic scale', items: ['Commencing on A - two octaves', 'Commencing on D♯/E♭ - two octaves'] },
    ],
  },
  G4: {
    label: 'Grade 4',
    exercises: [
      { code: '4A', purpose: 'for agility through changing hand shapes', pieces: ['Winter winds'] },
      { code: '4B', purpose: 'for broken chords', pieces: ['Catch me if you can (right hand)', 'Skater chaser (left hand)'] },
      { code: '4C', purpose: 'for finger staccato', pieces: ['Finger picker (right hand)', 'Ticky tacky (left hand)'] },
    ],
    sections: [
      { title: 'Scales', items: ['E major - four octaves', 'C♯ natural minor - four octaves', 'C♯ harmonic minor - four octaves', 'C♯ melodic minor - four octaves', 'A♭ major - four octaves', 'F natural minor - four octaves', 'F harmonic minor - four octaves', 'F melodic minor - four octaves'] },
      { title: 'Scales (staccato)', items: ['A♭ major - four octaves', 'F melodic minor - four octaves'] },
      { title: 'Scales in contrary motion', items: ['A major - two octaves', 'F♯ harmonic minor - two octaves', 'E♭ major - two octaves', 'C harmonic minor - two octaves'] },
      { title: 'Chromatic scales', items: ['Commencing on E - four octaves', 'Commencing on G♯/A♭ - four octaves'] },
      { title: 'Arpeggios', items: ['E major - four octaves', 'E minor - four octaves', 'A♭ major - four octaves', 'A♭ minor - four octaves'] },
    ],
  },
  G5: {
    label: 'Grade 5',
    exercises: [
      { code: '5A', purpose: 'for hand extensions and contractions', pieces: ['Ins and outs (part 1)', 'Ins and outs (part 2)'] },
      { code: '5B', purpose: 'for confidence with skips', pieces: ['Leaps and bounds (right hand)', 'Leaps and bounds (left hand)'] },
      { code: '5C', purpose: 'for pulse control through changing rhythmic subdivisions', pieces: ['Positive pulse'] },
    ],
    sections: [
      { title: 'Scales', items: ['B major - four octaves', 'G♯ harmonic minor - four octaves', 'G♯ melodic minor - four octaves', 'D♭ major - four octaves', 'B♭ harmonic minor - four octaves', 'B♭ melodic minor - four octaves'] },
      { title: 'Scales (staccato)', items: ['D♭ major - four octaves', 'B♭ melodic minor - four octaves'] },
      { title: 'Scales in contrary motion', items: ['E major - two octaves', 'C♯ harmonic minor - two octaves', 'A♭ major - two octaves', 'F harmonic minor - two octaves'] },
      { title: 'Chromatic scales', items: ['Commencing on B - four octaves', 'Commencing on C♯/D♭ - four octaves'] },
      { title: 'Arpeggios', items: ['B major - four octaves', 'B minor - four octaves', 'D♭ major - four octaves', 'D♭ minor - four octaves'] },
    ],
  },
  G6: {
    label: 'Grade 6',
    exercises: [
      { code: '6A', purpose: 'for equality of transfer between the hands', pieces: ['Closing the gaps'] },
      { code: '6B', purpose: 'for polyrhythmic playing (three against two)', pieces: ['Perfect polyrhythms'] },
      { code: '6C', purpose: 'for double-note staccato', pieces: ['Short \'n sweet (right hand)', 'Short \'n sweet (left hand)'] },
    ],
    sections: [
      { title: 'Scales', items: ['F♯ major - four octaves', 'D♯ harmonic minor - four octaves', 'D♯ melodic minor - four octaves'] },
      { title: 'Abbreviated grand scale format', items: ['E♭ major - four octaves', 'C harmonic minor - four octaves'] },
      { title: 'Scales (legato and staccato combination)', items: ['F♯ major - four octaves', 'D♯ melodic minor - four octaves'] },
      { title: 'Scales in contrary motion', items: ['B major - two octaves', 'G♯ harmonic minor - two octaves', 'D♭ major - two octaves', 'B♭ harmonic minor - two octaves'] },
      { title: 'Chromatic scale', items: ['Commencing on F♯/G♭ - four octaves'] },
      { title: 'I-V-I chord progressions', items: ['G major', 'F major', 'A major'] },
      { title: 'Arpeggios (root position and inversions)', items: ['F♯ major - four octaves', 'F♯ minor - four octaves', 'E♭ major - four octaves', 'E♭ minor - four octaves'] },
      { title: 'Dominant 7th arpeggios', items: ['of F♯ - four octaves', 'of E♭ - four octaves'] },
      { title: 'Diminished 7th arpeggios', items: ['of F♯ - four octaves', 'of E♭ - four octaves'] },
    ],
  },
  G7: {
    label: 'Grade 7',
    exercises: [
      { code: '7A', purpose: 'for hand/arm coordination', pieces: ['Flying high'] },
      { code: '7B', purpose: 'for two voices played by one hand', pieces: ['Two-part retention (right hand)', 'Two-part retention (left hand)'] },
      { code: '7C', purpose: 'for clean, light octaves in Lydian mode', pieces: ['Octave activation'] },
    ],
    sections: [
      { title: 'Abbreviated grand scale format', items: ['D major - four octaves', 'B harmonic minor - four octaves', 'A♭ major - four octaves', 'F harmonic minor - four octaves'] },
      { title: 'Polyrhythmic scales (three against two)', items: ['D major - three/two octaves', 'B harmonic minor - three/two octaves'] },
      { title: 'Scales in contrary motion', items: ['F♯ major - two octaves', 'D♯ harmonic minor - two octaves'] },
      { title: 'Chromatic scales', items: ['Commencing on D - four octaves', 'Commencing on G♯/A♭ - four octaves', 'Commencing on E♭ - two octaves'] },
      { title: 'I-IV-V-I chord progressions', items: ['G major', 'F major', 'E major'] },
      { title: 'Arpeggios (root position and inversions)', items: ['D major - four octaves', 'D minor - four octaves', 'A♭ major - four octaves', 'A♭ minor - four octaves'] },
      { title: 'Dominant 7th arpeggios (root position and inversions)', items: ['of D - four octaves', 'of A♭ - four octaves'] },
      { title: 'Diminished 7th arpeggios', items: ['of D - four octaves', 'of A♭ - four octaves'] },
    ],
  },
  G8: {
    label: 'Grade 8',
    exercises: [
      { code: '8A', purpose: 'for legato double notes', pieces: ['Double digits'] },
      { code: '8B', purpose: 'for freedom of movement across the keyboard', pieces: ['Clean sweeps'] },
      { code: '8C', purpose: 'for clean diatonic and chromatic octaves', pieces: ['Active octavation'] },
    ],
    sections: [
      { title: 'Abbreviated grand scale format', items: ['E major - four octaves', 'C♯ harmonic minor - four octaves', 'B♭ major - four octaves', 'G harmonic minor - four octaves'] },
      { title: 'Polyrhythmic scale (two against three)', items: ['E major - two/three octaves'] },
      { title: 'Hands together a third apart', items: ['E major - four octaves', 'C♯ harmonic minor - four octaves', 'B♭ major - four octaves', 'G harmonic minor - four octaves'] },
      { title: 'Hands together a sixth apart', items: ['E major - four octaves', 'C♯ harmonic minor - four octaves', 'B♭ major - four octaves', 'G harmonic minor - four octaves'] },
      { title: 'Chromatic scales', items: ['Commencing on E - three octaves', 'Commencing on A♯/B♭ - three octaves'] },
      { title: 'Chromatic scale in double thirds', items: ['Commencing on C and E♭ - two octaves'] },
      { title: 'I-IV-I⁶₄-V-I chord progressions', items: ['C major', 'D major', 'E♭ major'] },
      { title: 'Arpeggios (root position and inversions)', items: ['E major - four octaves', 'E minor - four octaves', 'B♭ major - four octaves', 'B♭ minor - four octaves'] },
      { title: 'Dominant 7th arpeggios (root position and inversions)', items: ['of E - four octaves', 'of B♭ - four octaves'] },
      { title: 'Diminished 7th arpeggios', items: ['of E - four octaves', 'of B♭ - four octaves'] },
    ],
  },
};
