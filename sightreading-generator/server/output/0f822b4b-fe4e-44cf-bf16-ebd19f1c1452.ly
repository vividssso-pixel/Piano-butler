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
  \key ees \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Sweetly"
  ees''2\mf ees''2~ |
  ees''2 g'4 g'4~ |
  g'4 \tuplet 3/2 { d''8 d''8 ees''8 } f''2 |
  ees''2 f''4 c''4~ |
  \break
  c''2 bes'2 |
  c''2. bes'4 |
  d''2 ees''4 ees''4 |
  ees''2. ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  ees2 bes2 |
  ees2 bes2 |
  aes2 ees2 |
  aes2 ees2 |
  \break
  aes2 ees2 |
  R1 |
  aes2 ees2 |
  ees2 bes2 |
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
