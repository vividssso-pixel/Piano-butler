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
  \key ees \major
  \time 4/4
  \tempo "Adagio"
  ees'4\mp aes'4. g'8 f'4 |
  R1 |
  R1 |
  ees'8 g'2 aes'4. |
  \break
  g'4 f'4. g'4. |
  R1 |
  ees'8 f'4 f'8 g'8 f'4 ees'8 |
  g'4. f'4 g'8 f'8 g'8 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  R1 |
  aes8 g8 f4. g4 f8 |
  g4 aes8 ees4. f4 |
  R1 |
  \break
  R1 |
  aes4 g8 aes4 g8 ees4 |
  R1 |
  R1 |
  \break
  aes2 g2 |
  aes8 g8 f2 ees4 |
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
