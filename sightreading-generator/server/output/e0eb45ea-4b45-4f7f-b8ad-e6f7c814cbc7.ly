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
  \tempo "Canon"
  R2. |
  a'16(\mf d''16 c''8 d''8 a'8 a'8 b'8) |
  b'8 g'8 a'8 b'8 a'8 d'8 |
  r4 d'8 e'4. |
  \break
  d'4 e'8 e'8 fis'8 e'8 |
  d'8 a'8 g'8 a'4 b'8 |
  c''4. b'4 a'8 |
  g'4. g'4. |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  g2. |
  d4. c8 b,8 g,8 |
  a,16 d16 c8 d8 a,8 a,8 b,8 |
  b,8 g,8 a,8 b,8 a,8 d8 |
  \break
  c4 d8 e4. |
  d4 e8 e8 fis8 e8 |
  d8 a,8 g,8 a,4 b,8 |
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
