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
  c'4 a'4 b'2 |
  c''2 b'4 b'4 |
  R1 |
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  R1 |
  R1 |
  f4 d4 c2 |
  c2 d4 c4 |
  c1 |
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
