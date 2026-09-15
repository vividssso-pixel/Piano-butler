\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \key f \major
  \time 4/4
  \tempo "Cantabile"
  f''2\mp e''4 d''16( e''16 a'16 bes'16) |
  c''4 d''4 e''16 d''16 c''16 e''16 f''4 |
  e''4 d''2. |
  c''2. c''4 |
  \break
  d''2 e''2 |
  c''16( d''16 e''16 f''16) e''4 e''4 f''4 |
  c''4 bes'2 c''4 |
  d''4 f''2. |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  bes2 f2 |
  c'2 g2 |
  c'2 g2 |
  c'2 g2 |
  \break
  bes2 f2 |
  c'2 g2 |
  r1 |
  f2 c'2 |
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
  \midi { \tempo 4 = 92 }
}
