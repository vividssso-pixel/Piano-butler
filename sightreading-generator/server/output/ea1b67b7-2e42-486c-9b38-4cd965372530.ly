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
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Moderato"
  e''2\(\mf e''4 b'4 |
  cis''1 |
  cis''2 dis''4 e''4 |
  e''4 dis''4 cis''4 dis''4\) |
  \break
  gis'4\( a'4 b'2 |
  a'2 a'2 |
  gis'4 b'4 a'4 cis''4 |
  dis''4 e''4 e''2\) |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  e2 b2 |
  a2 e2 |
  a2 e2 |
  a2 e2 |
  \break
  e2 b2 |
  a2 e2 |
  e2 b2 |
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
