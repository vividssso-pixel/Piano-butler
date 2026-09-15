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
  \key d \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Daintily"
  d''4\pp cis''4 b'4 a'4 |
  a'2 a'4 fis'4 |
  fis'4 g'4 fis'2 |
  g'2 g'4 a'4 |
  \break
  g'2 d''4 e''4 |
  e''4 cis''4 b'4 b'4 |
  cis''4 b'4 cis''2 |
  d''2 d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  d2 fis2 |
  d2 fis2 |
  R1 |
  e2 g2 |
  \break
  e2 g2 |
  e2 g2 |
  R1 |
  d2 fis2 |
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
