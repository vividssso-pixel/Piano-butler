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
  e''16\mp dis''16 gis'16 a'16 b'4 a'4 a'4 |
  b'2. a'4 |
  gis'4 a'2 b'4 |
  a'2 cis''2 |
  \break
  dis''2 cis''2 |
  a'4 b'4 a'4 gis'4 |
  a'16( b'16 dis''16 cis''16) dis''4 cis''16 cis''16 b'16 a'16 b'4 |
  cis''2 dis''4 e''4 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 4/4
  a1 |
  e1 |
  e1 |
  a1 |
  \break
  b1 |
  a1 |
  a1 |
  e1 |
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
