\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 2 — Reading" }
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
  \key a \minor
  \time 2/4
  R2 |
  R2 |
  R2 |
  a'8 b'8 c''4 |
  \break
  R2 |
  R2 |
  R2 |
  R2 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 2/4
  c8_\markup { \italic "loudly" } c8 c4 |
  a,4 b,8 a,8 |
  b,4 a,4 |
  R2 |
  \break
  a4. a8 |
  a8 g8 g4 |
  f8 gis8 a8 a8 |
  a2 |
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
  \midi { \tempo 4 = 84 }
}
