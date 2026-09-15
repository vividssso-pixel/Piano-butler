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
  \key f \major
  \time 4/4
  f''2.\f f''8( e''8) |
  d''4 d''4 c''4 d''8 c''8 |
  d''2. a'8 bes'8 |
  d''4 c''2 f''4 |
  \break
  e''4 e''2. |
  e''4^\markup { \italic "rall." } f''8( e''8 e''8 d''8) c''4 |
  c''4 bes'8( c''8) bes'4 c''4 |
  c''4 d''4 e''4 f''4 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  R1 |
  g1 |
  g1 |
  bes1 |
  \break
  R1 |
  c1 |
  f1 |
  f1 |
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
