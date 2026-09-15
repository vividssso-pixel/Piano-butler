\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \key bes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Moderato Pastorale"
  d''4\mp c''8( c''8 d''16 c''16 d''8) |
  ees''8 bes'4 bes'4. |
  c''4. d''4. |
  c''8 r4 bes'16 bes'16 c''8 c''8 |
  \break
  d''4. c''8 bes'4 |
  c''8( ees''8 f''8 ees''8 d''16 ees''16 f''8) |
  ees''4. ees''4 f''8 |
  f''4 ees''8 d''8 bes'4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  bes4. f4. |
  g4. bes4. |
  f4. c4. |
  a4. c4. |
  \break
  bes4. f4. |
  ees4. g4. |
  c4. g4. |
  d4. f4. |
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
  \midi { \tempo 4. = 64 }
}
