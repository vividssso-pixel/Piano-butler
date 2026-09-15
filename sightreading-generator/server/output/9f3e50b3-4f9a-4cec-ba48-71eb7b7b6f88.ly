\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  \time 2/4
  r2\mp |
  d''4 aes'8([ bes'8)] |
  bes'4 bes'4 |
  bes'2 |
  \break
  aes'2 |
  aes'2 |
  bes'8[ aes'8] g'8[ aes'8] |
  bes'8[ c''8] ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  r4 g4 |
  bes4 d'4 |
  R2 |
  bes4 d'4 |
  \break
  R2 |
  aes4 c'4 |
  R2 |
  ees4 g4 |
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
  \layout {
    \context {
      \Score
      \override SpacingSpanner.uniform-stretching = ##t
    }
  }
  \midi { \tempo 4 = 88 }
}
