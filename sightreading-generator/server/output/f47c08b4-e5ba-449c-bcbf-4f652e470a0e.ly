\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \key e \major
  \time 3/4
  \tempo "Cheekily"
  e''2\mp dis''4 |
  dis''2. |
  b'2 cis''16[ dis''16 e''16 dis''16] |
  e''4 dis''16[ dis''16 dis''16 cis''16] b'4 |
  \break
  a'4 b'4 a'4 |
  b'4 b'2 |
  a'2. |
  b'16[ a'16 gis'16 a'16] b'4 e''4 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 3/4
  R2. |
  R2. |
  b2. |
  b2. |
  \break
  a2. |
  b2. |
  R2. |
  e2. |
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
  \midi { \tempo 4 = 92 }
}
