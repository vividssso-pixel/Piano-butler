\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 8 — Reading" }
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
  \key fis \major
  \time 9/8
  \tempo "Andante (in 2)"
  ais'4\ff b'8 dis''4. eis''4. |
  dis''4 eis''8( gis'8 fis'8 gis'8 cis''8) cis''4 |
  cis''16( dis''16 cis''8 cis''8 dis''8 b'8 cis''8 b'8) b'4 |
  cis''4 dis''8 eis''4 gis'8 fis'8 dis''16 cis''16 dis''8 |
  \break
  r4 dis''8 dis''4 dis''8( cis''8 b'8 ais'8) |
  fis'4. gis'4. ais'4 ais'8 |
  b'8 cis''4 b'4. ais'8 b'8 ais'8 |
  b'8( cis''8 dis''16 cis''16) b'4 cis''8 b'8 cis''8 b'16 cis''16 |
  \break
  eis''8 eis''4 dis''8( eis''16 dis''16 eis''8 eis''8) dis''4 |
  eis''8 dis''4 eis''4 dis''8 cis''16 dis''16 cis''8 dis''8 |
  eis''8 dis''4 b'8 ais'8 ais'16 b'16 cis''4 dis''8 |
  cis''4. b'8( ais'16 gis'16 ais'8) b'4. |
  \break
  cis''4. b'8 cis''4 cis''8 eis''4 |
  dis''4. cis''8 dis''16 cis''16 cis''8 dis''8 eis''8 dis''8 |
  dis''8 eis''4 dis''16 cis''16 cis''8 b'8 cis''8 ais'4 |
  gis'4. fis'8 gis'4 fis'4 fis'8 |
  \break
  gis'4. ais'4 b'8 dis''4. |
  cis''8 dis''8 cis''8 r4 dis''8( dis''8 cis''8 b'8) |
  ais'8 gis'8 fis'8 fis'4. fis'4. |
  gis'8 ais'8 fis'8 gis'8 ais'8 gis'8 ais'8 gis'8 fis'16 gis'16 |
  \break
  b'4 ais'8 gis'4. fis'4. |
  gis'4 fis'8 fis'4. fis'4. |
  \bar "|."
}

bassLine = {
  \key fis \major
  \time 9/8
  dis4. ais4. fis4. |
  gis4. cis4. gis4. |
  ais4. cis4. fis4. |
  gis4. eis4. gis4. |
  \break
  fis4. cis4. ais4. |
  cis4. fis4. cis4. |
  b4. dis4. gis4. |
  dis4. b4. dis4. |
  \break
  cis4. gis4. eis4. |
  gis4. cis4. gis4. |
  b4. dis4. gis4. |
  cis4. ais4. cis4. |
  \break
  cis4. gis4. eis4. |
  dis4. gis4. dis4. |
  eis4. gis4. cis4. |
  cis4. ais4. cis4. |
  \break
  gis4. dis4. b4. |
  dis4. gis4. dis4. |
  ais4. cis4. fis4. |
  dis4. b4. dis4. |
  \break
  gis4. dis4. b4. |
  cis4. fis4. cis4. |
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
  \midi { \tempo 4. = 72 }
}
