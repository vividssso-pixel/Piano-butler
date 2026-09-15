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
  \key e \minor
  \time 4/4
  \tempo "Espressivo"
  e''2\mf d''8 e''8 d''8 e''8 |
  e''8( b'8) b'4 c''2 |
  R1 |
  a'4 a'4 d''2~ |
  \break
  d''2 g'4 a'4 |
  g'8( a'8) g'4 b'8( c''8 c''8 b'8) |
  c''8( d''8) d''4 e''4 d''4 |
  e''2. e''8( e''8) |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 4/4
  e2 g2 |
  e2 g2 |
  b2 dis2 |
  r2 c2 |
  \break
  a2 c2 |
  e2 g2 |
  a2 c2 |
  e2 g2 |
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
