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
  \key g \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Flowing"
  g'4.\f a'4. |
  f''8 ees''16 f''16 ees''8 bes'8 c''4 |
  bes'4. c''4. |
  ees''8 ees''4 c''4. |
  \break
  d''4. c''4. |
  g'8 a'8 ees''8 d''4. |
  c''8( c''8 f''16 ees''16) d''4. |
  ees''4. fis''8 fis''4 |
  \break
  ees''4. d''8 ees''4 |
  fis''4 ees''8 ees''8 d''4 |
  d''4 c''8 d''8 c''4 |
  bes'4. c''8 d''4 |
  \break
  fis''4. ees''8( fis''8 ees''8) |
  f''8( d''8 c''8 bes'8) g'4 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  g,4. d4. |
  ees4. g,4. |
  g,4. d4. |
  ees4. g,4. |
  \break
  d4. a,4. |
  bes,4. d4. |
  c4. g,4. |
  fis4. a,4. |
  \break
  c4. g,4. |
  fis4. a,4. |
  g,4. d4. |
  bes,4. d4. |
  \break
  d4. a,4. |
  bes,4. d4. |
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
