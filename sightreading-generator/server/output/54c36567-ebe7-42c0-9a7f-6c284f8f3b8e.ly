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
  R2 |
  ees''4\mf d''8([ c''8)] |
  d''2 |
  d''2 |
  \break
  d''8([ c''8)] g'4 |
  aes'2 |
  aes'4 bes'4 |
  c''4 d''8[ ees''8] |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  ees4 bes4 |
  aes4 ees4 |
  bes4 f4 |
  bes4 f4 |
  \break
  bes4 f4 |
  aes4 ees4 |
  aes4 r4 |
  ees4 bes4 |
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
