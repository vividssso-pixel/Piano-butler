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
  d'4 c'2 d'4 |
  c'4 d'2 d'4 |
  R1 |
  R1 |
  d'4 d'2 c'4 |
  d'4 e'2 a''4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  R1 |
  d4 c2 c4 |
  d4 e2 f4 |
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
