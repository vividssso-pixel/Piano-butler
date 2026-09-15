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
  \key fis \minor
  \time 3/4
  R2. |
  R2. |
  gis'8[\p a'8] b'4 a'4 |
  b'4 cis''8([ d''8)] e''4 |
  \break
  cis''2 b'8([ a'8)] |
  b'8([ b'8] cis''8[ a'8)] gis'4 |
  a'8([ gis'8)] fis'4 fis'8[ fis'8] |
  fis'2. |
  \bar "|."
}

bassLine = {
  \key fis \minor
  \time 3/4
  fis4 cis2 |
  b4 fis2 |
  cis4 gis2 |
  b4 fis2 |
  \break
  fis4 cis2 |
  R2. |
  fis4 cis2 |
  fis4 cis2 |
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
