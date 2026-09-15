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
  \key gis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gigue"
  b'16\p e''16 dis''8 e''8 b'4. |
  R2. |
  cis''4. dis''4. |
  e''8( cis''8 b'8 cis''8) dis''4 |
  \break
  e''4. dis''8( e''8 e''8) |
  cis''4 b'8 dis''8 e''8 b'8 |
  cis''8( dis''8 e''16 b'16) cis''4. |
  b'16 cis''16 b'8 b'8 b'4. |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  gis4. dis'4. |
  e'4. gis4. |
  cis'4. gis4. |
  e'4. gis4. |
  \break
  cis'4. gis4. |
  e'4. gis4. |
  cis'4. gis4. |
  b4. dis'4. |
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
