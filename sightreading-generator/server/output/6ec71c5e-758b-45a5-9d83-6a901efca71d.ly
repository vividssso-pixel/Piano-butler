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
  \time 3/4
  \tempo "Waltz"
  e''8([\mf dis''8)] dis''4. e''8 |
  dis''4 e''4 dis''4 |
  a'16([ b'16 a'8] fis'8[ fis'8)] fis'4 |
  gis'8([ fis'8)] gis'2 |
  \break
  a'4 gis'4 cis''8([ dis''8)] |
  cis''2 dis''4 |
  gis'8.([ a'16)] cis''4 dis''8([ cis''8)] |
  dis''4. cis''8 fis'4 |
  \break
  gis'4. gis'8( a'8[ b'8)] |
  cis''8([ b'16 a'8] gis'16[ a'8)] gis'4 |
  R2. |
  cis''16([ b'16 cis''8)] b'2 |
  \break
  cis''2 dis''4 |
  cis''4 dis''8([ cis''8] cis''8[ cis''16 cis''16)] |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 3/4
  cis4 gis4 gis4 |
  gis4 dis4 dis4 |
  fis4 cis4 cis4 |
  gis4 dis4 dis4 |
  \break
  fis4 cis4 cis4 |
  fis4 cis4 cis4 |
  gis4 dis4 dis4 |
  gis4 dis4 dis4 |
  \break
  gis4 dis4 dis4 |
  cis4 gis4 gis4 |
  cis4 gis4 gis4 |
  cis4 gis4 gis4 |
  \break
  cis4 gis4 gis4 |
  cis4 gis4 gis4 |
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
