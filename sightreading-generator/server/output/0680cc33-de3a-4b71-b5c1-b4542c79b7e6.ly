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
  \key a \major
  \time 3/4
  \tempo "Allegretto"
  a'4\f b'8([ cis''8] b'8[ cis''8)] |
  a'8([ b'8] a'8[ b'8)] cis''4 |
  a'4 b'8([ b'8] cis''8[ d''8)] |
  cis''4 b'4 d''4 |
  \break
  d''4 a'4 b'4 |
  e''8[^\markup { \italic "dim." } d''8] cis''2 |
  d''4 cis''8[ d''8] cis''4 |
  b'8([ a'8)] a'2 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 3/4
  R2. |
  a4 cis2 |
  a4 cis2 |
  b4 d2 |
  \break
  b4 d2 |
  a4 cis2 |
  b4 d2 |
  a4 cis2 |
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
