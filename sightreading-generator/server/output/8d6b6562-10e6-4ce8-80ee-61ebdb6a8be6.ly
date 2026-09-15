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
  \key e \minor
  \time 3/4
  \tempo "Waltz"
  R2. |
  d''2\(\f e''4 |
  d''2 e''4 |
  d''2 c''4 |
  \break
  d''8[ e''16 d''16] c''4. d''8 |
  c''4. d''16([ b'16)] b'4 |
  c''8[ d''8] e''4. d''16([ c''16)]\) |
  b'8[\( c''8] c''2~ |
  \break
  c''2 a'4 |
  b'4 a'2 |
  c''4 b'4. c''8 |
  R2. |
  \break
  R2. |
  e''2 e''4\) |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 3/4
  e4 b4 b4 |
  b4 fis4 fis4 |
  b4 fis4 fis4 |
  b4 fis4 fis4 |
  \break
  b4 fis4 fis4 |
  b4 fis4 fis4 |
  a4 e4 e4 |
  b4 fis4 fis4 |
  \break
  e4 b4 b4 |
  e4 b4 b4 |
  a4 e4 e4 |
  a4 e4 e4 |
  \break
  e4 b4 b4 |
  e4 b4 b4 |
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
