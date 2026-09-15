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
  \time 4/4
  \tempo "Romanze"
  e''2\mf dis''4. e''16( bis''16) |
  cis''4. dis''16( cis''8 cis''8 a'16) gis'4 |
  bis''2 cis''8( bis''16 a'8 dis''8 e''16) |
  a'4 gis'4 a'2 |
  \break
  bis''16( cis''8 dis''16 cis''8 bis''8) dis''2 |
  cis''4 bis''8( a'16 gis'16 a'8 fis'8) e'4 |
  gis'8( fis'16 e'8 fis'8 fis'8 gis'8 a'8 gis'8 gis'16) |
  R1 |
  \break
  gis'4 gis'2 fis'4 |
  e'4 fis'2 gis'8( cis''8) |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 4/4
  cis2 e2 |
  cis2 e2 |
  gis2 bis'2 |
  fis2 a2 |
  \break
  gis2 bis'2 |
  fis2 a2 |
  cis2 e2 |
  fis2 a2 |
  \break
  gis2 bis'2 |
  cis2 e2 |
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
  \midi { \tempo 4 = 96 }
}
