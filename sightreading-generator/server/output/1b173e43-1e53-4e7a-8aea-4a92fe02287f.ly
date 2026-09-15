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
  d''4\f d''4 |
  e''2 |
  cis''8([ d''8] cis''8[ a'8)] |
  R2 |
  \break
  b'8[ b'8] r4 |
  b'8([^\markup { \italic "dim." } g'8)] fis'4 |
  g'8([ fis'8] g'8[ a'8)] |
  d''2 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 2/4
  d4 r4 |
  a4 e4 |
  a4 e4 |
  g4 d4 |
  \break
  R2 |
  g4 d4 |
  g4 d4 |
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
  \midi { \tempo 4 = 88 }
}
