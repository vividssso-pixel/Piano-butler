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
  c'4 d'4 c'2 |
  c'4 d'2 e'4 |
  R1 |
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  R1 |
  e'4 f'4 e'2 |
  f'4 e'2 e'4 |
  a'1 |
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
