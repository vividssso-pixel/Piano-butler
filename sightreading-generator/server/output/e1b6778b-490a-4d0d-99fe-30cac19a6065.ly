\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 6 — Reading" }
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
  \key f \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Barcarolle"
  f''8\p d''8 c''8 f''8 e''8 f''8 |
  e''4. f''16( bes'16 c''8 d''8) |
  c''8( d''8 c''8 d''16 e''16 d''8 e''8) |
  d''4. c''8 d''4 |
  \break
  e''8 d''4 e''8 f''4 |
  e''4 f''8 e''4. |
  f''4 e''8 f''8 e''8 d''8 |
  c''8 bes'4 a'16( bes'16 a'8 bes'8) |
  \break
  bes'4 c''8( bes'8) c''4 |
  d''8( c''8 c''8 bes'8) a'4 |
  bes'16( bes'16 c''8 bes'8) c''4. |
  bes'16( a'16 bes'8 c''8) d''4. |
  \break
  c''4 d''8( c''8 bes'8 c''8) |
  bes'8 a'4 bes'8 c''4 |
  d''8 c''4 bes'4 a'8 |
  bes'8 c''4 bes'8 a'4 |
  \break
  bes'8 c''4 bes'8 a'8 bes'16 a'16 |
  bes'4 a'8( bes'8) a'4 |
  bes'8 c''4 bes'4 a'8 |
  bes'8( bes'8 a'8 bes'8 c''8 d''16 f''16) |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  f4. a4. |
  bes4. d4. |
  c4. e4. |
  g4. bes4. |
  \break
  c4. e4. |
  c4. e4. |
  bes4. d4. |
  f4. a4. |
  \break
  g4. bes4. |
  c4. e4. |
  g4. bes4. |
  g4. bes4. |
  \break
  c4. e4. |
  g4. bes4. |
  g4. bes4. |
  g4. bes4. |
  \break
  bes4. d4. |
  bes4. d4. |
  bes4. d4. |
  f4. a4. |
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
  \midi { \tempo 4. = 67 }
}
