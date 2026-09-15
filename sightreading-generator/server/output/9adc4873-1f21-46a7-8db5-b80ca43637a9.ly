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
  \key e \major
  \time 4/4
  \tempo "Not too fast"
  e''4\mp a'4 gis'2 |
  a'4 b'2 a'4 |
  a'4 b'2 cis''4 |
  b'2. gis'4 |
  \break
  a'2 gis'2 |
  a'2 a'4 cis''4 |
  b'16( a'16 b'16 cis''16) dis''2. |
  e''2 e''2 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 4/4
  r1 |
  r1 |
  a2 e2 |
  e2 b2 |
  \break
  a2 e2 |
  a2 e2 |
  b2 fis2 |
  e2 b2 |
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
