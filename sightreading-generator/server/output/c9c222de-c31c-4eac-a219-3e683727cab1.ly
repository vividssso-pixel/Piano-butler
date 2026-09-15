\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 5 (Blaze) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key bes \major
  \time 6/8
  \tempo "Not fast but sharp"
  ees'16\mf f'4 bes''16 bes''8. bes''8 a'16 |
  g'8. f'4 f'16 ees'8 c''8 |
  c''2 c''4 |
  c''8 c''8 ees'4. f'8 |
  ees'16 f'4 ees'8 bes'8 c'16 c'8 |
  d'4 c'8 d'8 c'16 d'8 ees'16 |
  d'4 c'2 |
  bes'16 d'2 c'16 bes'8 |
  c'8 bes'16 a8 bes'16 c'16 c'4 d'16 |
  c'8 c'4. d'8 c'16 d'16 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 6/8
  ees4 bes'4 g4 |
  ees4 bes'4 g4 |
  f4 c'4 a4 |
  f4 c'4 a4 |
  ees4 bes'4 g4 |
  bes4 f4 d4 |
  bes4 f4 d4 |
  bes4 f4 d4 |
  f4 c'4 a4 |
  f4 c'4 a4 |
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
  \midi { \tempo 4. = 64 }
}
