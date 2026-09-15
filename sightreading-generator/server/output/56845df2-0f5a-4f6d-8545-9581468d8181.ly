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
  \time 2/4
  \tempo "Allegretto"
  d''2\mf |
  e''4 d''8([ d''8)] |
  e''2 |
  b'2~ |
  \break
  b'4 g'8([ fis'8)] |
  g'2 |
  fis'8([ b'8] cis''8[ d''8)] |
  d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 2/4
  d2 |
  r2 |
  r2 |
  R2 |
  \break
  d2 |
  g2 |
  d2 |
  d2 |
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
