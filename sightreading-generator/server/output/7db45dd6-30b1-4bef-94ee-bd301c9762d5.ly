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
  c'4 e'4 f'2 |
  g'2 a'2 |
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  R1 |
  R1 |
  f4 e4 d2 |
  c2 c2 |
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
