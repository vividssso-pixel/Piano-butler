\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 2 (Flame) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key f \major
  \time 4/4
  bes'4 a'2 c'4 |
  d'2 c'4 d'4 |
  e'8 f''8 c'4 f''2 |
  d'8 f''8 d'8 e'4 d'8 c'4 |
  d'8 e'8 f''8 e'2 f''8 |
  d'4 f''8 e'8 f''4 e'4 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  bes4 f'4 bes4 f'4 |
  bes4 f'4 bes4 f'4 |
  c4 g'4 c4 g'4 |
  bes4 f'4 bes4 f'4 |
  bes4 f'4 bes4 f'4 |
  bes4 f'4 bes4 f'4 |
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
  \midi { \tempo 4 = 84 }
}
