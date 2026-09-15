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
  \key b \minor
  \time 2/4
  \tempo "Moderato"
  b'4\mf b'8([ cis''8)] |
  b'4 b'8[ e''8] |
  d''8([ e''8] d''8[ cis''8)] |
  b'4 r4 |
  \break
  cis''4 d''4 |
  cis''4^\markup { \italic "rall." } b'8([ e''8)] |
  d''4 cis''4 |
  b'8([ b'8)] b'4 |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 2/4
  b2 |
  e2 |
  b2 |
  r2 |
  \break
  fis2 |
  fis2 |
  R2 |
  b2 |
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
