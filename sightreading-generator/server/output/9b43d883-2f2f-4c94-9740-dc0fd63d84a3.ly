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
  \key ees \major
  \time 4/4
  R1 |
  ees'8-. ees'8-. g'8-. f'8-. f'2-. |
  ees'2-. ees'4.-. f'8-. |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  ees2-._\markup { \italic "brightly" } d4-. d4-. |
  R1 |
  R1 |
  aes8-. g8-. aes4-. f4-. ees4-. |
  \break
  aes8-. g8-. aes8-. g8-. aes4-. aes8-. g8-. |
  aes8-. f8-. ees4-. ees4-. ees8-. ees8-. |
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
