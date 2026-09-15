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
  a'2 f''4 g''4 |
  f''2 e''2 |
  R1 |
  R1 |
  c''2 d''4 e''4 |
  f''2 a''2 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  R1 |
  f2 e4 f4 |
  e2 f2 |
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
