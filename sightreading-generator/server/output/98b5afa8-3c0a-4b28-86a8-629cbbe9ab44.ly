\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \time 2/4
  \tempo "Bourrée"
  e''16([\p dis''16 b'8)] r4 |
  dis''8[ cis''16 cis''16] dis''4-. |
  e''4 e''8.[ dis''16] |
  a'8([ b'16 e''16)] dis''4 |
  \break
  b'4 a'8.[ b'16] |
  a'8.[ b'16] a'4-. |
  gis'2-. |
  a'8[ b'16 cis''16] b'4 |
  \break
  a'4 gis'8([ a'8)] |
  b'4. a'16[ cis''16] |
  dis''8[ dis''16 cis''16] b'4 |
  R2 |
  \break
  a'4. cis''8 |
  dis''4 e''8([ e''8)] |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 2/4
  e4 b4 |
  b4 fis4 |
  e4 b4 |
  a4 e4 |
  \break
  b4 fis4 |
  fis4 cis4 |
  e4 b4 |
  fis4 cis4 |
  \break
  fis4 cis4 |
  b4 fis4 |
  b4 fis4 |
  fis4 cis4 |
  \break
  fis4 cis4 |
  e4 b4 |
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
  \midi { \tempo 4 = 96 }
}
