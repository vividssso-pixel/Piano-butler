\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Preliminary — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 4/4
  d'4 e'4 e'4 f'4 |
  e'4 f'2 e'4 |
  R1 |
  R1 |
  d'4 c'4 c'4 d'4 |
  c'4 d'2 e'4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  R1 |
  d4 e4 d4 c4 |
  b4 b2 c4 |
  R1 |
  R1 |
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
  \midi { \tempo 4 = 76 }
}
