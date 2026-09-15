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
  \key d \major
  \time 3/4
  R2. |
  R2. |
  d'8 e'8 d'4 e'8 d'8 |
  e'8 d'8 e'4 fis'8 a'8 |
  \break
  R2. |
  R2. |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  b,8 a,8 b,4 b,8 cis8 |
  b,8 g,8 a,4 b,8 cis8 |
  R2. |
  R2. |
  \break
  a8 g8 a4 g8 fis8 |
  d8 e8 d4 d8 d8 |
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
