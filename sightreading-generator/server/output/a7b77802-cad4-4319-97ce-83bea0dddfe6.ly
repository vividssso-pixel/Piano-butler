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
  \key d \major
  \time 2/4
  \tempo "Slow march"
  d''4.\p fis'16[ g'16] |
  a'2 |
  g'16[ a'16 a'8] g'4 |
  cis''2 |
  \break
  d''4 cis''16[ d''16 d''16 cis''16] |
  g'8([ fis'8)] g'4 |
  fis'16[ d''16 e''8] d''4 |
  r4 cis''8.[ cis''16] |
  \break
  cis''4 d''8([ e''16 d''16)] |
  e''4 d''16[ cis''16 b'8] |
  b'16([ a'16 g'8] \tuplet 3/2 { b'8 cis''8 d''8) } |
  cis''4 d''4 |
  \break
  cis''4 b'4 |
  cis''8([ d''8)] d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 2/4
  d4 a4 |
  d4 a4 |
  g4 d4 |
  a4 e4 |
  \break
  d4 a4 |
  g4 d4 |
  d4 a4 |
  d4 a4 |
  \break
  a4 e4 |
  a4 e4 |
  g4 d4 |
  a4 e4 |
  \break
  a4 e4 |
  d4 a4 |
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
