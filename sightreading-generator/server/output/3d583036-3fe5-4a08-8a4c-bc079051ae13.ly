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
  \time 4/4
  b'8(\f c''8) c''2\( b'4 |
  e''4 d''4 c''4 c''4 |
  d''4 e''2 d''8 c''8 |
  d''4 c''4 d''8 e''8 d''8 c''8\) |
  \break
  c''2\( d''8( c''8 b'8 c''8) |
  d''2 e''8( b'8) b'4 |
  c''8( c''8 b'8 d''8) e''4 d''8( c''8) |
  b'2 b'4 b'4\) |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 4/4
  g2 b2 |
  R1 |
  g2 b2 |
  g2 b2 |
  \break
  c'2 e'2 |
  g2 b2 |
  c'2 e'2 |
  g2 b2 |
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
