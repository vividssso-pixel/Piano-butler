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
  R1 |
  b'2\(\p_\markup { \italic "lilting" } d''4 e''8( d''8) |
  R1 |
  d''8 c''8 d''4 c''2\) |
  \break
  d''4\( c''4 e''8( d''8) e''4 |
  r2 d''4 c''4 |
  b'8 c''8 c''2 e''4 |
  d''4 e''8 e''8 e''2\) |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 4/4
  R1 |
  g1 |
  g1 |
  g1 |
  \break
  g1 |
  g1 |
  c'1 |
  g1 |
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
