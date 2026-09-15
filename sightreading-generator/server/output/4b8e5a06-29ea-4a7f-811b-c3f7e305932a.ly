\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
  ragged-right = ##t
  top-margin = 6\mm
  bottom-margin = 6\mm
  left-margin = 8\mm
  right-margin = 8\mm
}

melody = {
  \key ees \major
  \time 2/2
  \tempo "Minuet tempo"
  ees''4.\mf f''8 bes'4. c''8 |
  d''2 ees''8 d''8 d''4 |
  d''4. c''4. aes'8 g'8 |
  aes'4 g'8 aes'2 bes'8 |
  c''4 d''2 c''4 |
  bes'4. ees''2 f''8 |
  ees''8 d''8 c''4 ees''4 f''4 |
  ees''8 d''2 c''4. |
  c''4 c''8 d''4. c''8 d''8 |
  ees''8 d''8 bes'4 bes'2 |
  aes'4. bes'8 c''4 ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/2
  ees2 bes2 |
  bes2 f2 |
  bes2 f2 |
  aes2 ees2 |
  aes2 ees2 |
  ees2 bes2 |
  ees2 bes2 |
  ees2 bes2 |
  aes2 ees2 |
  ees2 bes2 |
  aes2 ees2 |
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
