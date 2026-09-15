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
  \time 3/4
  \tempo "Sweetly"
  e''4\mf dis''4 e''4~ |
  e''2 dis''4~ |
  dis''16 cis''16 b'16 cis''16 dis''2 |
  e''4 dis''2 |
  \break
  b'4 a'2 |
  gis'2. |
  a'2. |
  \tuplet 3/2 { e''8( e''8 e''8) } e''2 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 3/4
  e2. |
  b2. |
  b2. |
  e2. |
  \break
  e2. |
  e2. |
  a2. |
  e2. |
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
