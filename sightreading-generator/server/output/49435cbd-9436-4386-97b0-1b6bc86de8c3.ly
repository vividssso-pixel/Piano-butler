\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Preliminary — Reading" }
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
  \key c \major
  \time 4/4
  c2 d4 c4 |
  d4 e4 d4 d4 |
  c4 d2 e4 |
  d4 c4 c2 |
  \bar "|."
}

\score {
  \new Staff \with { instrumentName = "Piano" } {
    \clef bass
    \melody
  }
  \layout {}
  \midi { \tempo 4 = 76 }
}
