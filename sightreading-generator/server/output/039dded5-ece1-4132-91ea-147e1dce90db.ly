\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Preliminary (Spark) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 4/4
  d'2 e'4 d'4 |
  d'2 c'4 b'4 |
  d'4 e'2 d'4 |
}

bassLine = {
  \key a \minor
  \time 4/4
  d1 |
  d1 |
  d1 |
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
}
