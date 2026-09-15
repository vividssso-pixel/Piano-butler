\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 1 (Ember) — Rhythm"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key f \major
  \time 4/4
  bes'4 c'2 c'8 bes'8 |
  a'2 g'8 a'4 g'8 |
  a'4 a'4 a'4 bes'4 |
  c'2 a'4 bes'4 |
  c'8 bes'8 a'4 a'2 |
  a'8 g'4 a'2 g'8 |
  a'8 bes'4 a'4 bes'4 c'8 |
  bes'4 a'4 bes'4 a'8 g'8 |
}

bassLine = {
  \key f \major
  \time 4/4
  bes2 f'2 |
  f2 c2 |
  f2 c2 |
  f2 c2 |
  f2 c2 |
  f2 c2 |
  f2 c2 |
  bes2 f'2 |
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
