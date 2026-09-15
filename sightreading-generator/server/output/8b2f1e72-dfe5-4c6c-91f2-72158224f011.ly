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
  \time 4/4
  \tempo "Hymn"
  dis''16\f cis''16 dis''8 cis''2 b'8( cis''8) |
  b'4 cis''2 dis''8( cis''16 b'16) |
  cis''4 b'8( cis''8 b'8 ais'16 b'16) cis''4 |
  b'4 cis''8 dis''8 cis''2 |
  \break
  gis'8( ais'8) gis'4 ais'16 b'16 ais'8 b'4 |
  cis''4. dis''8 cis''8 b'8 ais'4 |
  gis'2 ais'4. b'16( ais'16) |
  b'2 cis''4. gis'8 |
  \break
  ais'16 gis'16 fis'8 gis'4 gis'4 ais'4 |
  ais'2 gis'4 fis'4 |
  fis'2 gis'4 ais'8 ais'8 |
  gis'2 gis'8 gis'8 gis'4 |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 4/4
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
  <cis dis gis>4 <cis dis gis>4 <cis dis gis>4 <cis dis gis>4 |
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
  \break
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
  <cis dis gis>4 <cis dis gis>4 <cis dis gis>4 <cis dis gis>4 |
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
  \break
  <dis disis ais>4 <dis disis ais>4 <dis disis ais>4 <dis disis ais>4 |
  <dis disis ais>4 <dis disis ais>4 <dis disis ais>4 <dis disis ais>4 |
  <dis disis ais>4 <dis disis ais>4 <dis disis ais>4 <dis disis ais>4 |
  <gis b dis>4 <gis b dis>4 <gis b dis>4 <gis b dis>4 |
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
