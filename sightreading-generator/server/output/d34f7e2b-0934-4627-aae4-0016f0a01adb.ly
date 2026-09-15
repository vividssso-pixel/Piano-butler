\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 7 — Reading" }
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
  \key dis \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Andante religioso"
  dis''8\mp eis''4 dis''16( dis''16) eis''4. dis''16( gis'16) |
  gis'4 b'4 cis''4 \tuplet 3/2 { dis''8( eis''8 ais'8) } |
  b'16( eis''16 dis''8) eis''4 dis''4 eis''16( dis''16 gis'8) |
  \tuplet 3/2 { ais'8( b'8 cisis''8 } b'16 ais'16 gis'16 dis''16) eis''4 dis''4 |
  \break
  eis''2. dis''4 |
  eis''4 dis''4 dis''16( cisis''16) b'4 ais'16( b'16) |
  ais'16( gis'16) ais'4 b'8 cis''2 |
  cis''4. b'8 ais'4. gis'16( b'16) |
  \break
  ais'4. gis'16( fis'16 gis'8 ais'16) gis'4 gis'16 |
  ais'2. gis'8( ais'8) |
  gis'2 ais'8( b'8 ais'8 gis'8) |
  ais'4. gis'16( gis'16) fis'4 gis'4 |
  \break
  fis'8 gis'4. ais'4 ais'8( gis'16 fis'16) |
  gis'16( fis'16 gis'8 fis'8 gis'8) ais'4 b'16( dis''16 eis''16 cis''16) |
  b'2 cis''16( b'16) cis''4 b'16( cis''16) |
  b'16( b'16) cis''4. b'4. b'8 |
  \break
  ais'8 b'4. b'4 ais'16( ais'16 gis'16 fis'16) |
  gis'4. fis'8( gis'8) fis'4 gis'8 |
  gis'4 ais'8( b'8 ais'8) gis'4. |
  ais'2 b'4 cisis''8( dis''16 dis''16) |
  \bar "|."
}

bassLine = {
  \key dis \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  gis4 dis4 gis4 dis4 |
  gis4 dis4 gis4 dis4 |
  gis4 dis4 gis4 dis4 |
  ais4 eis4 ais4 eis4 |
  \break
  ais4 eis4 ais4 eis4 |
  ais4 eis4 ais4 eis4 |
  dis4 ais4 dis4 ais4 |
  gis4 dis4 gis4 dis4 |
  \break
  gis4 dis4 gis4 dis4 |
  ais4 eis4 ais4 eis4 |
  gis4 dis4 gis4 dis4 |
  gis4 dis4 gis4 dis4 |
  \break
  dis4 ais4 dis4 ais4 |
  gis4 dis4 gis4 dis4 |
  gis4 dis4 gis4 dis4 |
  gis4 dis4 gis4 dis4 |
  \break
  dis4 ais4 dis4 ais4 |
  gis4 dis4 gis4 dis4 |
  gis4 dis4 gis4 dis4 |
  dis4 ais4 dis4 ais4 |
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
  \midi { \tempo 4 = 104 }
}
