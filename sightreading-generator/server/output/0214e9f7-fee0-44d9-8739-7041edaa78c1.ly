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
  \key cis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Allegretto"
  cis''16\mp b'16 b'8 dis''8 e''16 e''16 e''8 dis''8 |
  e''4 dis''8 dis''4 cis''8 |
  dis''4 cis''8( dis''8 cis''8 bis''8) |
  cis''4. dis''8 dis''4 |
  \break
  e''8 dis''4 dis''4. |
  dis''4 cis''8( cis''8 bis''8 bis''8) |
  cis''4 b'8( b'8 cis''16 cis''16 dis''8) |
  e''16 b'16 a'8 bis''8 cis''8 cis''4 |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  cis4. gis4. |
  cis4. gis4. |
  gis4. dis4. |
  gis4. dis4. |
  \break
  cis4. gis4. |
  gis4. dis4. |
  r8 cis4 gis4. |
  cis4. gis4. |
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
