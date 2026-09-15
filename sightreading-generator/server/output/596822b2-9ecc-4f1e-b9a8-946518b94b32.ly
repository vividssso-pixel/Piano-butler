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
  \key bes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Sweetly"
  d''4.\p ees''8 bes'4 |
  bes'4. bes'4. |
  c''4. bes'4. |
  g'4 a'8 bes'4 c''8 |
  \break
  a'4. g'8( f'8 ees'8) |
  d'8( g'8 a'16 d'16 ees'8) d'4 |
  ees'8 d'4 ees'8( ees'8 d'8) |
  ees'8 f'4 g'4 bes'8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  bes4. d4. |
  bes4. d4. |
  c4. ees4. |
  R2. |
  \break
  R2. |
  g4. bes4. |
  R2. |
  bes4. d4. |
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
