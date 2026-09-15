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
  d''4\mf cis''4 |
  b'8([ fis'8)] g'4 |
  fis'8[ g'8] a'8[ b'8] |
  cis''2 |
  \break
  cis''8[ cis''8] b'4~ |
  b'2~ |
  b'8([ a'8)] fis'4 |
  g'4 a'8([ d''8)] |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 2/4
  d4 r4 |
  R2 |
  d4 fis4 |
  a4 cis'4 |
  \break
  R2 |
  a4 cis'4 |
  d4 fis4 |
  d4 fis4 |
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
