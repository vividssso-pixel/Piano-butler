\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 1 — Reading" }
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
  \key bes \major
  \time 2/4
  R2 |
  R2 |
  R2 |
  bes'2 |
  \break
  c''4 bes'8 c''8 |
  c''8 bes'8 c''4 |
  bes'2 |
  c''8 bes'8 bes'4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 2/4
  d2 |
  d4 c8 bes,8 |
  c8 c8 d4 |
  R2 |
  \break
  R2 |
  R2 |
  R2 |
  R2 |
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
  \midi { \tempo 4 = 80 }
}
