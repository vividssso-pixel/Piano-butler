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
  \key g \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Legato"
  g'4\mp a'4 bes'4 c''4 |
  a'4 bes'4 c''4 bes'4 |
  c''2 ees''2 |
  ees''2 ees''4 f''4 |
  \break
  ees''2 d''4 d''4 |
  a'4 bes'4 a'2 |
  bes'2. bes'4 |
  a'4 g'4 g'4 g'4 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  g1 |
  g,4 a,4 bes,4 c4 |
  a,4 bes,4 c4 bes,4 |
  c2 ees2 |
  \break
  ees2 ees4 f4 |
  ees2 d4 d4 |
  a,4 bes,4 a,2 |
  g1 |
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
