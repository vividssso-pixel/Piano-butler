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
  \key g \major
  \time 2/4
  \tempo "Espressivo"
  b'4\(\f c''8( d''8) |
  c''2~ |
  c''4 c''4~ |
  c''8( c''8) d''4\) |
  \break
  c''4\( c''4~ |
  c''8( d''8) e''4 |
  d''4 d''8 e''8 |
  e''8( e''8) e''4\) |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 2/4
  g4 b4 |
  c'4 e'4 |
  g4 b4 |
  g4 b4 |
  \break
  c'4 e'4 |
  g4 b4 |
  g4 b4 |
  g4 b4 |
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
