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
  \key d \major
  \time 3/4
  d'2\f_\markup { \italic "playfully" } e'4 |
  a'4 g'4 a'4 |
  R2. |
  d'4 e'4 fis'4 |
  \break
  g'4 a'4 g'4 |
  R2. |
  d'4 g'8 a'8 cis''4 |
  b'4 a'4 d''4 |
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
  a8 fis8 g4 fis4 |
  R2. |
  \break
  R2. |
  a4. g8 g4 |
  R2. |
  R2. |
  \break
  a4 g4 a4 |
  g4 fis8 e8 d4 |
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
