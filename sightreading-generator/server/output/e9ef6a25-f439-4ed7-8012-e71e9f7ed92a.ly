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
  \key c \minor
  \time 2/4
  \tempo "Espressivo"
  r4\f bes'4 |
  c''2 |
  R2 |
  ees''8([ d''8] ees''8[ bes'8)] |
  \break
  R2 |
  b'8([ ees''8)] d''4 |
  d''8([ c''8] d''8[ c''8)] |
  c''4 c''4 |
  \bar "|."
}

bassLine = {
  \key c \minor
  \time 2/4
  c4 g4 |
  R2 |
  g4 d4 |
  c4 g4 |
  \break
  R2 |
  g4 r4 |
  g4 d4 |
  c4 g4 |
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
