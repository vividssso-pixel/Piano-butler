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
  a'4.\f b'16([ e''16)] |
  d''4. cis''16([ b'16)] |
  cis''16([ cis''16 b'8)] cis''4 |
  d''16([ cis''16 d''16 cis''16)] a'4 |
  \break
  b'8([ d''16 cis''16)] b'4 |
  b'2 |
  b'16([ cis''16 b'16 cis''16)] cis''4 |
  d''4 cis''16([ d''16 e''16 b'16)] |
  \break
  cis''8([ b'16 cis''16)] d''4 |
  cis''4 d''16([ cis''16 b'16 cis''16)] |
  b'4. a'8 |
  b'2 |
  \break
  a'2 |
  b'16([ a'16 a'8)] a'4 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 2/4
  a,4 e4 |
  b,4 fis4 |
  a,4 e4 |
  d4 a,4 |
  \break
  b,4 fis4 |
  e4 b,4 |
  e4 b,4 |
  b,4 fis4 |
  \break
  a,4 e4 |
  a,4 e4 |
  b,4 fis4 |
  e4 b,4 |
  \break
  a,4 e4 |
  a,4 e4 |
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
