\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \key g \major
  \time 2/4
  \tempo "Slow march"
  b'4.\mp c''8 |
  b'4 c''16[ b'16 c''8] |
  b'4 c''8([ e''8)] |
  d''16[ d''16 c''8] b'4 |
  \break
  d''4 d''8([ e''16 c''16)] |
  c''4. b'16[ c''16] |
  b'8[ c''8] b'8[ b'8] |
  b'2 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 2/4
  g4 d'4 |
  g4 d'4 |
  g4 d'4 |
  g4 d'4 |
  \break
  g4 d'4 |
  c'4 g4 |
  g4 d'4 |
  g4 d'4 |
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
  \midi { \tempo 4 = 96 }
}
