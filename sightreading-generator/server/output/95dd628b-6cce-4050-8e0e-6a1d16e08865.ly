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
  \time 3/4
  bes'4 d'4 d'4 |
  e'2 c'4 |
  bes'8 a'4 g'8 a'4 |
  a'8 a'4 g'4 g'8 |
}

bassLine = {
  \key f \major
  \time 3/4
  bes4. f'4. |
  c4. g'4. |
  bes4. f'4. |
  f4. c4. |
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
