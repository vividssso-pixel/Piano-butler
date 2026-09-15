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
  \tempo "Allegretto"
  ees''16\mf c''4 d''8.( ees''16) d''4. f''16 |
  ees''4 d''16( c''16) bes'4 c''8( bes'8 aes'8) |
  bes'8 c''4 d''8( c''16) bes'4. bes'16 |
  c''8. bes'4 bes'8( aes'16) g'4. |
  \break
  d''4. c''8 aes'2 |
  g'2 aes'8( c''16) d''4 d''16 |
  c''4 d''16 c''8 d''4 bes'4 bes'16 |
  aes'4 aes'4 bes'16 c''8. ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  aes2 ees2 |
  aes2 ees2 |
  bes2 f2 |
  ees2 bes2 |
  \break
  aes2 ees2 |
  aes2 ees2 |
  bes2 f2 |
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
