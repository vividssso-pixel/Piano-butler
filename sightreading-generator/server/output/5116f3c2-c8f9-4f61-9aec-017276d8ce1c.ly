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
  \time 4/4
  \tempo "Allegretto"
  e''4\pp dis''4 b'4 a'4 |
  gis'4 cis''4 b'4 a'4 |
  gis'4 dis''2 dis''4 |
  cis''4. dis''8 e''4 dis''4 |
  \break
  e''4 cis''4 b'4 b'4 |
  a'2 b'2 |
  b'4. b'8 \tuplet 3/2 { cis''8 cis''8 dis''8 } cis''4 |
  b'16( a'16 a'16 b'16) cis''2 e''4 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 4/4
  e,2 b,2 |
  e,2 b,2 |
  e,2 r2 |
  a,2 e,2 |
  \break
  e,2 b,2 |
  fis,2 r2 |
  b,2 fis,2 |
  e,2 b,2 |
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
