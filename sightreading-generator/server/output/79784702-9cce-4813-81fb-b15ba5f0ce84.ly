\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 7 — Reading" }
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
  \tempo "Allegretto"
  bes'2.\mf c''4 |
  d''2 bes'8 a'4 bes'8 |
  bes'2 a'4. c''16( bes'16) |
  bes'4. a'8( c''16 bes'16 f''16) ees''4 f''16 |
  \break
  ees''2. f''8( f''8) |
  ees''2 ees''4 bes'4 |
  c''16( d''16) c''4. bes'4. a'8 |
  g'4 c''8( d''8 ees''8) d''4 bes'16( bes'16) |
  \break
  d''4. c''16( bes'16) a'2 |
  bes'2 c''8( bes'16 c''16 bes'8 c''8) |
  ees''8 d''4 d''8 ees''2 |
  d''8 fis''4 ees''16( d''16 c''8) bes'4 a'16( bes'16) |
  \break
  a'4 g'8( bes'8 a'16 bes'16) a'4 g'16( g'16) |
  g'2. g'4 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  g4 d4 bes4 d4 |
  g4 d4 bes4 d4 |
  g4 d4 bes4 d4 |
  ees4 bes4 g4 bes4 |
  \break
  c4 g4 ees4 g4 |
  ees4 bes4 g4 bes4 |
  c4 g4 ees4 g4 |
  g4 d4 bes4 d4 |
  \break
  g4 d4 bes4 d4 |
  g4 d4 bes4 d4 |
  c4 g4 ees4 g4 |
  d4 a4 fis4 a4 |
  \break
  g4 d4 bes4 d4 |
  g4 d4 bes4 d4 |
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
  \midi { \tempo 4 = 104 }
}
