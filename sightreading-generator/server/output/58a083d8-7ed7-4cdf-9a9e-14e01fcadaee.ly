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
  \key f \major
  \time 2/4
  R2 |
  R2 |
  R2 |
  f'2-. |
  \break
  bes'4-. c''8-. c''8-. |
  f''2 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 2/4
  c4-._\markup { \italic "soft" } bes,8-. c8-. |
  a,8-. g,8-. a,4-. |
  bes,4-. a,8-. bes,8-. |
  R2 |
  \break
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
  \midi { \tempo 4 = 84 }
}
