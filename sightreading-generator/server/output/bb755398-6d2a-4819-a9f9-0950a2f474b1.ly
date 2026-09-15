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
  \key cis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gigue"
  cis''8\f dis''4 e''8( dis''8 e''8) |
  dis''4. cis''4 e''8 |
  dis''8( a'8 bis''16 fis'16 gis'8) fis'4 |
  gis'8 a'4 gis'4. |
  \break
  fis'8( e'8 fis'8 gis'8 a'8 dis''16 e''16) |
  bis''4 a'8( fis'8 gis'16 a'16 fis'8) |
  gis'4. fis'8( e'8 fis'16 e'16) |
  fis'4 gis'8( bis''8 a'16 gis'16 fis'8) |
  \break
  gis'8 fis'4 gis'4. |
  fis'8( gis'16 fis'16 e'8) fis'4 e'8 |
  fis'8 e'4 e'4. |
  fis'8 e'4 fis'8 gis'4 |
  \break
  R2. |
  e'4 fis'8 gis'4 cis''8 |
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
  cis4. gis4. |
  \break
  fis4. cis4. |
  fis4. cis4. |
  cis4. gis4. |
  fis4. cis4. |
  \break
  gis4. dis4. |
  fis4. cis4. |
  fis4. cis4. |
  fis4. cis4. |
  \break
  fis4. cis4. |
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
  \midi { \tempo 4. = 64 }
}
