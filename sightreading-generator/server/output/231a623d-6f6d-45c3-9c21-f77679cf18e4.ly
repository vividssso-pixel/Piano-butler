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
  \time 3/4
  \tempo "Legato"
  f''4\f e''16([ e''16 d''16 c''16)] a'4 |
  bes'2. |
  d''2. |
  e''4 d''4 \tuplet 3/2 { bes'8 a'8 a'8 } |
  \break
  a'2 a'4 |
  bes'4 bes'4 a'4 |
  \tuplet 3/2 { bes'8 bes'8 c''8 } d''2 |
  f''2. |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 3/4
  f4 c2 |
  g4 d2 |
  g4 d2 |
  c4 g2 |
  \break
  R2. |
  g4 d2 |
  g4 d2 |
  f4 c2 |
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
