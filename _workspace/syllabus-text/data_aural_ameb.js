// AMEB Aural Test Requirements (Preliminary to Grade 8).
// Source: "2026 AMEB Manual of Syllabuses (Music)", General Requirements for
// Practical Examinations, section "21. Aural Test Requirements". The Piano and
// Piano for Leisure syllabuses both defer to this section rather than listing
// aural tests themselves, so this one table serves both subjects.
//
// Notes carried over from the source section:
//   - Comprehensive practical examinations only.
//   - Aural tests in grades other than Preliminary are played twice.
//   - Where a test appears in more than one grade, the difficulty of the examples
//     is adjusted to the standard of that grade.
//   - Candidates whose voices are breaking may whistle instead of humming/singing.
//   - Interval naming: Grade 3 names them as the second/third/fourth/fifth of the
//     scale; Grades 4-6 name them as major second, major third, perfect fourth, etc.
//
// Structure per grade:
//   label  - display name
//   tests  - the grade's aural tests in syllabus order, each with the test category
//            (TIME / RHYTHM / PITCH / MELODY / HARMONY / MEMORY) and its full wording.

const DATA_AURAL_AMEB = {
  Prelim: {
    label: 'Preliminary',
    tests: [
      { type: 'TIME', text: 'To clap the beats of simple chord passages played in two- or three-beat time by the examiner at varying speeds - slow, moderate and quick, and to continue clapping or beating after the examiner ceases to play.' },
      { type: 'RHYTHM', text: 'To hum, sing, clap or tap the note values of a simple rhythmical two-bar passage played by the examiner.' },
      { type: 'PITCH', text: 'To sing or hum the notes of a short melodic phrase of five or six notesof one beat length. The examiner plays the phrase then repeats it, waiting on each note for the candidate to sing the note.' },
      { type: 'PITCH', text: 'To state which is the higher or lower of any two notes, not less than a third apart, that the examiner has played separately.' },
    ],
  },
  G1: {
    label: 'Grade 1',
    tests: [
      { type: 'PITCH', text: 'To hum or sing the tonic at the end of a short unfinished phrase playedby the examiner.' },
      { type: 'RHYTHM', text: 'The examiner will play twice a passage in duple or triple time. The candidate will then tap or clap the passage.' },
      { type: 'PITCH', text: 'To hum or sing a short phrase played twice by the examiner, combining melody and time.' },
    ],
  },
  G2: {
    label: 'Grade 2',
    tests: [
      { type: 'RHYTHM', text: 'The examiner will play twice a passage in duple or triple time. The candidate will then tap or clap the passage.' },
      { type: 'PITCH', text: 'To hum or sing a short phrase played twice by the examiner, combining melody and time.' },
      { type: 'PITCH', text: 'To hum or sing the higher or lower of two notes a major third or a perfect fifth apart within the limits of an octave from middle C played simultaneously by the examiner.' },
    ],
  },
  G3: {
    label: 'Grade 3',
    tests: [
      { type: 'RHYTHM', text: 'The examiner will play twice a passage in duple or triple time. The candidate will then tap or clap the passage and state whether it is duple or triple time.' },
      { type: 'MELODY', text: 'To hum or sing a short phrase played twice by the examiner, combining melody and time.' },
      { type: 'PITCH', text: 'To hum or sing the higher or lower of any two notes within the limits of an octave from middle C played simultaneously by the examiner.' },
      { type: 'PITCH', text: 'The examiner having sounded on the piano a note to be regarded as the keynote of the scale, the candidate will hum or sing and afterwards name the interval of the second, third, fourth or fifth of the major scale as played by the examiner, in succession to the keynote.' },
    ],
  },
  G4: {
    label: 'Grade 4',
    tests: [
      { type: 'RHYTHM', text: 'The examiner will play twice a passage in duple or triple time. The candidate will then tap or clap the passage and state whether it is in duple or triple time.' },
      { type: 'PITCH', text: 'The examiner having sounded on the piano a note, to be regarded as the keynote of the scale, the candidate will hum or sing and afterwards name any interval of the major scale as played by the examiner immediately after the keynote.' },
      { type: 'PITCH', text: 'To hum or sing from memory the higher or lower part of a two-part progression of two successive intervals within the compass of an octave from middle C as played by the examiner.' },
      { type: 'PITCH', text: 'The examiner having sounded any major or minor triad either in root position or an inversion played within the limits of an octave, the candidate will hum or sing the middle note.' },
    ],
  },
  G5: {
    label: 'Grade 5',
    tests: [
      { type: 'RHYTHM', text: 'The examiner will play twice a passage in duple or triple time. The candidate will then tap or clap the passage and state whether it is in duple or triple time.' },
      { type: 'PITCH', text: 'The examiner having sounded on the piano a note to be regarded as a keynote of the scale, the candidate will hum or sing and afterwards name any interval of the major scale as played by the examiner immediately in succession to the keynote.' },
      { type: 'PITCH', text: 'To hum or sing from memory the higher or lower part of a two-part progression of three successive intervals within the limits of an octave from middle C as played slowly by the examiner.' },
      { type: 'HARMONY', text: 'The examiner having sounded any major or minor triad either in root position or an inversion played within the limits of an octave, the candidate will hum or sing all three notes,ascending or descending as required.' },
    ],
  },
  G6: {
    label: 'Grade 6',
    tests: [
      { type: 'PITCH', text: 'The examiner having sounded on the piano a note to be regarded as the keynote of the scale, the candidate will hum or sing and afterwards name any interval of the major or harmonic minor scale as played by the examiner immediately in succession to the keynote.' },
      { type: 'HARMONY', text: 'The examiner having sounded any major triad either in root position or an inversion played within the limits of an octave, the candidate will recognise the position of the triad.' },
      { type: 'PITCH', text: 'To hum or sing from memory the higher or lower part of a two-part progression of four successive intervals within the limits of an octave from middle C.' },
      { type: 'HARMONY', text: 'To recognise Perfect and Plagal cadences in a major key as they occur in a short piece played by the examiner, the tonic chord being first sounded.' },
    ],
  },
  G7: {
    label: 'Grade 7',
    tests: [
      { type: 'PITCH', text: 'The examiner having sounded any major or minor triad either in root position or an inversion played within the limits of an octave, the candidate will recognise the major or minortriad, stating its position.' },
      { type: 'HARMONY', text: 'To recognise Perfect, Plagal and Interrupted cadences in a major key as they occur in a short piece played by the examiner, the tonic chord being first sounded.' },
      { type: 'MEMORY', text: 'Approximately one minute being allowed to memorise a two-bar melodic phrase from a printed copy away from the instrument, the candidate will then play or sing the phrase from memory. The examiner will sound the keynote before the phrase is memorised.' },
      { type: 'PITCH', text: 'To hum or sing from memory the higher or lower part of a two-part phrase of not more than six notes, note against note within the compass of an octave from middle C played slowlyby the examiner.' },
    ],
  },
  G8: {
    label: 'Grade 8',
    tests: [
      { type: 'HARMONY', text: 'The examiner having sounded any major or minor triad either in root position or an inversion, or any diminished triad in root position played within the limits of an octave,the candidate will recognise the major, minor or diminished triad, stating its position (in the case of a majoror minor triad).' },
      { type: 'HARMONY', text: 'To recognise any of the four principal cadences in a major key as they occur in a short piece played by the examiner, the tonic chord being first sounded.' },
      { type: 'MEMORY', text: 'Approximately one and a half minutes being allowed to memorise a three- or four-bar melodic phrase from a printed copy away from the instrument, the candidate will then play orsing the phrase from memory. The examiner will sound the keynote before the phrase is memorised.' },
      { type: 'PITCH', text: 'The examiner will play on a piano a two-part phrase with a few passing notes, and the candidate will hum, sing or play from memory, the lower part.' },
    ],
  },
};
