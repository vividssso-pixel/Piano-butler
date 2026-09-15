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
  \key c \major
  \time 2/4
  \tempo "Lively"
  R2 |
  c'2 |
  R2 |
  R2 |
  \break
  c'2 |
  d'4. e'8 |
  R2 |
  R2 |
  \break
  c'4. c'8 |
  c'4 c'4 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 2/4
  g2\p_\markup { \italic "gentle" } |
  R2 |
  a4 f4 |
  g4 g8 d8 |
  \break
  R2 |
  R2 |
  a2 |
  g8 f4 e8 |
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
  \midi { \tempo 4 = 88 }
}
