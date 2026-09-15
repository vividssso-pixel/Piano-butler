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
  \key c \major
  \time 4/4
  c'2 e'2 |
  f'2 e'4 f'4 |
  R1 |
  R1 |
  e'2 f'2 |
  e'2 d'4 c'4 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  R1 |
  R1 |
  a2 g2 |
  f2 e4 d4 |
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
