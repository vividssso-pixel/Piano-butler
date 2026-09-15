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
  \key e \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Dolce"
  e''8\(\p e''4 a'8 a'16 b'16 c''8 |
  dis''16 a'16 a'8 b'8 a'4. |
  g'4. c''4. |
  b'8 c''8 a'16 b'16 c''4.\) |
  \break
  b'4.\( c''4 b'8 |
  b'4. a'4. |
  b'8 a'8 b'8 c''8 dis''8 c''8 |
  b'4 a'8 b'8 c''8 e''8\) |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  a4. e4. |
  r8 b4 fis4. |
  c4. g4. |
  b4. fis4. |
  \break
  e4. r8 b4 |
  R2. |
  R2. |
  e4. b4. |
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
