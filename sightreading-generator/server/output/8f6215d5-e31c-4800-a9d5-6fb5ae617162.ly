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
  \tempo "Dolce"
  e''2.\(\p dis''4 |
  b'4 a'4 b'4 b'4~ |
  b'2. b'4 |
  a'2. b'4\) |
  \break
  a'4\( a'4 gis'2 |
  gis'2 a'4 b'4 |
  a'4 b'4 \tuplet 3/2 { cis''8 e''8 dis''8 } e''4 |
  e''2. e''4\) |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  R1 |
  R1 |
  a2 cis'2 |
  a2 cis'2 |
  \break
  a2 cis'2 |
  R1 |
  R1 |
  e2 gis2 |
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
