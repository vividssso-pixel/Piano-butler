\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \time 4/4
  \tempo "Moderato"
  a'4\f cis''2. |
  b'4 fis'2. |
  e'4 \tuplet 3/2 { a'8( b'8 a'8) } cis''4 cis''4 |
  \tuplet 3/2 { b'8( d''8 e''8) } d''4 e''2 |
  \break
  d''2 cis''4 e''4 |
  d''2. b'4 |
  a'2. fis'4 |
  gis'2 a'4 a'4 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 4/4
  a2 e2 |
  b2 fis2 |
  a2 e2 |
  e2 b2 |
  \break
  a2 e2 |
  b2 fis2 |
  d2 a2 |
  a2 e2 |
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
  \midi { \tempo 4 = 92 }
}
