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
  \key d \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Barcarolle"
  d''4\(\mf d''8( d''8) c''4 |
  bes'4. c''8 d''4 |
  e''4. bes'4 a'8 |
  bes'4. a'4. |
  \break
  bes'16 e''16 d''8 c''8 f'4 g'8 |
  bes'4 a'8 bes'8 f'4 |
  g'16( f'16 g'8 f'8) g'4. |
  a'4. bes'8( cis''8 bes'16 cis''16) |
  \break
  bes'4 a'8 bes'4 c''8\) |
  bes'16\( a'16 bes'8 a'8 g'4. |
  f'4 f'8 g'4 a'8 |
  g'16 a'16 g'8 f'8 g'4. |
  \break
  a'4. bes'8 a'8 a'16 g'16 |
  g'4. a'4 g'8 |
  a'4 g'8 f'8 g'8 a'8 |
  g'4. f'8 g'8 a'8 |
  \break
  g'8 f'4 g'8 g'4 |
  a'4. bes'8 d''4\) |
  \bar "|."
}

bassLine = {
  \key d \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  d4. f4. |
  g4. bes4. |
  a4. cis4. |
  g4. bes4. |
  \break
  g4. bes4. |
  bes4. d4. |
  g4. bes4. |
  a4. cis4. |
  \break
  g4. bes4. |
  g4. bes4. |
  d4. f4. |
  g4. bes4. |
  \break
  a4. cis4. |
  g4. bes4. |
  d4. f4. |
  g4. bes4. |
  \break
  g4. bes4. |
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
  \midi { \tempo 4. = 67 }
}
