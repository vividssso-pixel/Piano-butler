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
  \key e \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Allegretto"
  e''4.\mp dis''8 gis'4 |
  a'4. gis'4. |
  a'8 e''4 dis''8 e''4 |
  a'8 b'8 cis''8 b'4 b'8 |
  \break
  cis''4 b'8( a'8 b'16 a'16 b'8) |
  cis''8 dis''8 e''8 dis''4. |
  cis''4. dis''8 e''4 |
  dis''8 e''4 e''4 e''8 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  e2. |
  a2. |
  a2. |
  a2. |
  \break
  a2. |
  a2. |
  a2. |
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
  \midi { \tempo 4. = 61 }
}
