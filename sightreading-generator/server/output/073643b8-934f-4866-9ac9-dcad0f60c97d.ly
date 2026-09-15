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
  \key a \major
  \time 2/4
  \tempo "Andante religioso"
  a'4.\mf b'16([ a'16)] |
  b'8([ cis''8] d''8[ a'16 b'16)] |
  d''4 e''16([ d''16 e''16 cis''16)] |
  b'8([ a'8)] d''4 |
  \break
  e''2 |
  d''8([ a'16 b'16)] a'4 |
  b'8.([ a'16)] b'4 |
  a'2 |
  \break
  b'16([ cis''16 b'8)] d''4 |
  e''8([ d''16 e''16)] d''4 |
  e''16([ d''16 d''16 e''16)] d''4 |
  b'4 a'8([ b'8)] |
  \break
  cis''2 |
  cis''4. a'8 |
  b'4 cis''16([ b'16 a'16 a'16)] |
  a'2 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 2/4
  a4 e4 |
  d4 fis4 |
  b4 fis4 |
  d4 fis4 |
  \break
  e4 b4 |
  fis4 a4 |
  e4 b4 |
  cis4 e4 |
  \break
  b4 fis4 |
  gis4 b4 |
  a4 e4 |
  d4 fis4 |
  \break
  a4 e4 |
  cis4 e4 |
  a4 e4 |
  cis4 e4 |
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
