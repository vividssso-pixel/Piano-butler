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
  \key fis \minor
  \time 2/4
  \tempo "Slow march"
  a'4\p cis''4 |
  d''2 |
  e''4 b'4 |
  a'16([ a'16 b'8] cis''16[ cis''8 b'16)] |
  \break
  cis''4 cis''4 |
  d''4 a'16([ b'8 cis''16)] |
  b'4 a'4 |
  b'4 a'16([ a'8 a'16)] |
  \bar "|."
}

bassLine = {
  \key fis \minor
  \time 2/4
  fis4 cis'4 |
  b4 fis4 |
  cis'4 gis4 |
  fis4 cis'4 |
  \break
  fis4 cis'4 |
  b4 fis4 |
  b4 fis4 |
  fis4 cis'4 |
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
