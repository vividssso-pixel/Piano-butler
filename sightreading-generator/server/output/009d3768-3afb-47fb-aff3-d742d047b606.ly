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
  \tempo "Cantabile"
  e''4\pp dis''4 e''4 dis''4 |
  cis''2 b'4 a'4 |
  a'4 gis'4 a'2 |
  gis'2 a'2 |
  \break
  e''4 dis''4 cis''2~ |
  cis''4 b'4 cis''4 cis''4 |
  b'2 a'2 |
  gis'4 cis''4 \tuplet 3/2 { b'8( cis''8 dis''8) } e''4 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  e4 e4 fis4 fis4 |
  fis4 fis4 fis4 fis4 |
  r4 fis4 e4 e4 |
  e4 fis4 gis4 a4 |
  \break
  R1 |
  b4 a4 fis4 e4 |
  e4 dis4 dis4 cis4 |
  e4 e4 e4 e4 |
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
