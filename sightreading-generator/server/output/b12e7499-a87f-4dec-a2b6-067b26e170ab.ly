\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 4 (Blaze) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key ees \major
  \time 2/2
  \tempo "Minuet tempo"
  aes'4.\mf bes'8 ees'4 f'4 |
  aes'8 aes'2 aes'4. |
  d'8. c'4. c'4 aes'8 bes'8 |
  aes'8 g'8 aes'4 d'8 ees''4 c'8 |
  d'8. d'4 ees''4 d'8 ees''8 ees''8 |
  d'4. ees''8 d'4. ees''8 |
  d'4 ees''4. d'8 ees''8. ees''8 |
  d'8. c'4. bes'4 bes'8. |
  c'4 d'4 bes'8 bes'4. |
  aes'4 aes'8 g'8 aes'4. g'8 |
  aes'8 bes'8 bes'8 c'2 d'8 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/2
  aes4 ees'4 c4 ees'4 |
  aes4 ees'4 c4 ees'4 |
  bes1~ bes16 |
  aes4 ees'4 c4 ees'4 |
  bes1~ bes16 |
  bes4 f'4 d4 f'4 |
  bes1~ bes16 |
  bes4 f'4 d4 f'4 |
  aes4 ees'4 c4 ees'4 |
  aes4 ees'4 c4 ees'4 |
  aes4 ees'4 c4 ees'4 |
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
  \midi { \tempo 4 = 92 }
}
