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
  b'2\mp_\markup { \italic "sweetly" } e''8( d''8) a'4 |
  b'8 c''8 r4 e''8( d''8 a'8 b'8) |
  a'2 b'8( a'8 g'8 a'8) |
  \break
  b'2 c''8( b'8 a'8 g'8) |
  g'8( g'8) b'4 a'2 |
  b'8 a'8 g'4 a'2 |
  g'4 a'8( g'8) g'4 g'4 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 4/4
  a2 c2 |
  g2 b2 |
  g2 b2 |
  d2 fis2 |
  \break
  g2 b2 |
  g2 b2 |
  r2 b2 |
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
