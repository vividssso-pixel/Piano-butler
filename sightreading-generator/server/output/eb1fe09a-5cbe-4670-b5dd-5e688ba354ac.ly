\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 6 (Beacon) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key g \minor
  \time 4/4
  \tempo "Moderato scherzoso"
  c'8\f ais'8 d'16 c'16 d'4 c'4 ais'16 a'16 |
  a'16 ais'2 g''4 dis'16 f8 |
  c'8 c'8 ais'2 c'4 |
  c'2. g''8. f'16 |
  g''16 g''16 a''16 dis'8 f'8 g''16 a''16 g''8 a''16 g''16 a''16 g''16 a''16 |
  g''4 a''16 g''2 a''8 g''16 |
  g''4. f'8 d'16 dis'4 c'8 ais'16 |
  a'4. g'2 a'8 |
  g'4. f4 f4 g'8 |
  a'2. ais'4 |
  c'4 dis'4 dis'4 dis'4 |
  f'2 g''8 f'4. |
  g''16 a''8 a''4 g''16 dis'16 d'4 dis'16 dis'16 f'16 |
  dis'8 f'4. g''4 f'8. g''16 |
  f'8 dis'4 d'4 dis'4 d'16 c'16 |
  c'2 ais'4 c'16 ais'8 c'16 |
  d'8 c'16 c'8. d'2 f'8 |
  dis'2. f'4 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 4/4
  c4 g'4 dis4 g'4 |
  d4 a'4 f4 a'4 |
  c4 g'4 dis4 g'4 |
  c4 g'4 dis4 g'4 |
  g4 d4 ais4 d4 |
  g4 d4 ais4 d4 |
  g4 d4 ais4 d4 |
  d4 a'4 f4 a'4 |
  g4 d4 ais4 d4 |
  d4 a'4 f4 a'4 |
  c4 g'4 dis4 g'4 |
  d4 a'4 f4 a'4 |
  g4 d4 ais4 d4 |
  c4 g'4 dis4 g'4 |
  d4 a'4 f4 a'4 |
  c4 g'4 dis4 g'4 |
  g4 d4 ais4 d4 |
  c4 g'4 dis4 g'4 |
  \bar "|."
}

\score {
  \new PianoStaff <<
    \new Staff = "right" {
      \clef treble
      \melody
    }
    \new Staff = "left" {
      \clef bass
      \bassLine
    }
  >>
  \layout {}
  \midi { \tempo 4 = 100 }
}
