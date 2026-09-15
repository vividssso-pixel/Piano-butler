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
  \key d \major
  \time 4/4
  b,4 b,2 cis4 |
  b,4 cis4 b,2 |
  cis4 a,4 b,4 a,4 |
  b,2 cis4 cis4 |
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
