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
  \key bes \major
  \time 3/4
  ees'8 d'4 ees'4 d'8 |
  c'4. bes'4 c'8 |
  d'2 d'4 |
  c'8 d'8 c'4 bes'8 c'8 |
  d'4 c'2 |
  bes'2 c'4 |
  f'8 c'4 bes'4. |
  c'4 d'4. ees'8 |
  d'2 bes'8 c'8 |
  f'4 ees'4 d'4 |
  ees'4. f'4 f'8 |
  ees'4 d'4. d'8 |
}

bassLine = {
  \key bes \major
  \time 3/4
  ees4 bes'4 ees4 |
  f4 c'4 f4 |
  bes4 f4 bes4 |
  f4 c'4 f4 |
  bes4 f4 bes4 |
  bes4 f4 bes4 |
  bes4 f4 bes4 |
  f4 c'4 f4 |
  bes4 f4 bes4 |
  bes4 f4 bes4 |
  ees4 bes'4 ees4 |
  ees4 bes'4 ees4 |
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
