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
  \tempo "Legato"
  e''4\mp dis''2 |
  cis''4 e''16([ dis''16 dis''16 cis''16)] dis''4 |
  e''4 a'2 |
  b'2. |
  \break
  cis''4 dis''16[ cis''16 a'16 gis'16] a'4 |
  b'2. |
  cis''4 dis''2 |
  e''2. |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 3/4
  e4 b2 |
  a4 e2 |
  a4 e2 |
  b4 fis2 |
  \break
  fis4 cis2 |
  R2. |
  fis4 cis2 |
  e4 b2 |
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
