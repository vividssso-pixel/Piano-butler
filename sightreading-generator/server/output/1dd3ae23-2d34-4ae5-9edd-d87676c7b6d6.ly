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
  \key e \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Allegretto"
  e''4.\mp d''4 c''8 |
  b'8 c''8 b'16 c''16 d''8 e''4 |
  b'4 c''8 d''4. |
  e''8 a'4 g'4. |
  \break
  d''4 c''8 b'4. |
  g'4. a'4 a'8 |
  R2. |
  r4 b'8 c''8 b'8 b'8 |
  \break
  a'8 b'4 a'4. |
  b'8 c''4 b'8 a'4 |
  g'4 a'8 b'4 a'8 |
  b'16 a'16 b'8 c''8 e''4. |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  a2. |
  e,4. d4 c8 |
  b,8 c8 b,16 c16 d8 e,4 |
  b,4 c8 d4. |
  \break
  e,8 a,4 g,4. |
  d4 c8 b,4. |
  g,4. a,4 a,8 |
  g,8 a,8 g,8 a,8 g,4 |
  \break
  a,4 b,8 c8 b,8 b,8 |
  a,8 b,4 a,4. |
  b,8 c4 b,8 a,4 |
  e2. |
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
