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
  \key g \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Moderato, flowing"
  g'4.\mp b'8 c''4 |
  d''4. e''16 d''16 e''8 d''8 |
  fis'4. e'4. |
  fis'8 e'4 d'4 e'8 |
  \break
  d'4. e'8( fis'8 d'8) |
  e'8( d'8 b'16 c''16) e'4. |
  d'8 a'4 g'8 a'8 g'16 fis'16 |
  g'8 g'8 fis'8 g'8 g'4 |
  \break
  a'4 a'8 g'4 g'8 |
  g'16( fis'16 g'8 g'8 g'8) g'4 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  g2. |
  g,4. b,8 c4 |
  d4. e16 d16 e8 d8 |
  fis4. e4. |
  \break
  fis8 e4 d4 e8 |
  d4. e8 fis8 d8 |
  e8 d8 b,16 c16 e4. |
  d8 a,4 g,8 a,8 g,16 fis16 |
  \break
  g,8 g,8 fis8 g,8 g,4 |
  g2. |
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
