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
  e''16\(\mf b'16 cis''8 b'8 cis''4. |
  dis''8 dis''4 cis''4 b'8 |
  a'4 gis'8 a'8 e'8 fis'8 |
  fis'4. e'4. |
  \break
  fis'8( b'8 a'8) b'4.\) |
  a'4\( gis'8 fis'4. |
  gis'4 fis'8 e'8 fis'8 e'8 |
  fis'8 e'4 fis'4. |
  \break
  b'4 cis''8 b'4. |
  a'16 fis'16 e'8 fis'8 gis'8 a'8 cis''8\) |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  cis,4. gis,4. |
  gisis,4. dis,4. |
  fis,4. cis,4. |
  gis,4. cis,4. |
  \break
  gis,4. dis,4. |
  gis,4. cis,4. |
  cis,4. gis,4. |
  gis,4. cis,4. |
  \break
  gis,4. dis,4. |
  e,4. gis,4. |
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
