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
  \key aes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Not too fast"
  c''8(\f des''8\( des''8 c''8) des''4 |
  c''8 c''8 des''8 des''4 ees''8 |
  f''8 ees''4 f''8 ees''4 |
  des''4 des''8 des''8 ees''4\) |
  \break
  ees''4.\( f''4 f''8 |
  ees''8 des''4 des''16 c''16 des''8 ees''8 |
  f''8 ees''16 ees''16 f''8 des''4. |
  c''8 c''4 c''4.\) |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  aes2. |
  aes2. |
  des'2. |
  R2. |
  \break
  ees'2. |
  aes2. |
  des'2. |
  aes2. |
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
  \midi { \tempo 4. = 61 }
}
