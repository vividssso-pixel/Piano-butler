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
  \key d \major
  \time 3/4
  d'8_\markup { \italic "loudly" } e'8 e'2 |
  d'8 e'8 e'8 fis'8 g'4 |
  a'8 a'8 g'8 a'8 b'4 |
  R2. |
  \break
  R2. |
  R2. |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  R2. |
  R2. |
  R2. |
  a4 fis4. g8 |
  \break
  a4. g8 fis8 d8 |
  d4 cis8 d8 d8 d8 |
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
