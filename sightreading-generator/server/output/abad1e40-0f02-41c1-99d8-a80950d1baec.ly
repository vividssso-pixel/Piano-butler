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
  e''1\pp |
  dis''4 a'4 gis'4 a'4 |
  gis'2 a'2 |
  gis'2 a'4 b'4 |
  \break
  a'4 gis'4 a'2~ |
  a'2 dis''4 e''4 |
  e''4 dis''4 e''4 e''4 |
  e''1 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  e1 |
  e,1 |
  dis4 a,4 gis,4 a,4 |
  gis,2 a,2 |
  \break
  gis,2 a,4 b,4 |
  a,4 gis,4 a,2 |
  gis,2 dis4 e,4 |
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
