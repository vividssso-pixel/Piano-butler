\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 7 — Reading" }
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
  \key b \minor
  \time 3/4
  \tempo "Allegretto"
  b'2\pp cis''4 |
  b'2. |
  e''2. |
  d''2 b'4 |
  \break
  cis''2 e''4 |
  d''4 e''4 d''4 |
  d''2 d''8([ d''8)] |
  e''2. |
  \break
  cis''2 b'8([ cis''8)] |
  cis''2 b'4 |
  cis''4 b'2 |
  cis''4 b'2 |
  \break
  d''2 e''8([ b'8)] |
  cis''4 d''8([ cis''8)] b'4 |
  b'2. |
  b'4 b'2 |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 3/4
  b4 fis4 b4 |
  b4 fis4 b4 |
  e4 b4 e4 |
  b4 fis4 b4 |
  \break
  fis4 cis4 fis4 |
  b4 fis4 b4 |
  b4 fis4 b4 |
  e4 b4 e4 |
  \break
  fis4 cis4 fis4 |
  fis4 cis4 fis4 |
  fis4 cis4 fis4 |
  b4 fis4 b4 |
  \break
  b4 fis4 b4 |
  fis4 cis4 fis4 |
  b4 fis4 b4 |
  b4 fis4 b4 |
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
  \midi { \tempo 4 = 104 }
}
