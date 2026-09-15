\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 1 (Ember) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key f \major
  \time 4/4
  bes'4 g'8 a'4 g'8 a'8 a'8 |
  g'8 bes'4 a'8 c'2 |
  c'2 bes'2 |
  c'2 d'4 d'4 |
  bes'8 bes'2 c'4 e'8 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  bes2 f'2 |
  c2 g'2 |
  f2 c2 |
  f2 c2 |
  bes2 f'2 |
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
  \midi { \tempo 4 = 80 }
}
