\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  \time 3/4
  \tempo "Lively"
  d''8([\f cis''8)] b'4 g'8([ a'8)] |
  g'4 g'2~ |
  g'8[ g'8] fis'8[ a'8] g'4 |
  g'2 a'4 |
  \break
  g'4 a'2 |
  g'4 g'4 g'8([ a'8)] |
  fis'2 g'8([ g'8)] |
  a'4 b'8([ cis''8)] d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  g4 b2 |
  g4 b2 |
  r4 fis2 |
  R2. |
  \break
  g4 b2 |
  g4 r2 |
  g4 b2 |
  d4 fis2 |
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
  \midi { \tempo 4 = 88 }
}
