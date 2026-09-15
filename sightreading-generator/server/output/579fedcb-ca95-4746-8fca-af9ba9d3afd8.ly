\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 6 — Reading" }
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
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Allegretto"
  b'16\mp cis''16 dis''4. e''16 dis''16 e''16 dis''16 dis''4 |
  e''4. cis''8 cis''4. dis''8 |
  e''4 dis''16( e''16 dis''8) e''4 dis''8 dis''16 e''16 |
  e''4. b'8( cis''16 dis''16) e''4. |
  \break
  cis''16( b'16 ais'8 b'8 ais'8) b'4 cis''16 dis''16 cis''8 |
  b'4. cis''8 e''4 e''8 dis''16 dis''16 |
  cis''16 cis''16 b'16 dis''16 e''4 dis''8( cis''16 b'16 ais'8 b'8) |
  cis''8 cis''4. dis''16( e''16 dis''8 e''8 dis''8) |
  \break
  cis''8.( cis''16) cis''4 b'16( ais'16) cis''4 b'8 |
  ais'4. gis'16 ais'16 gis'8 b'4 cis''8 |
  b'16( ais'16 b'16 dis''16) cis''4 b'8 ais'4. |
  gis'16( ais'16) b'4. cis''4 ais'4 |
  \break
  b'16 ais'16 ais'4 b'8 gis'2 |
  ais'8 cis''4 b'8 gis'16 ais'16 gis'16 ais'4 b'16 |
  cis''8 dis''4. e''4 dis''4 |
  e''16( dis''16) e''4 dis''8 cis''2 |
  \break
  b'8.( ais'16) gis'4 ais'8. gis'16 ais'4 |
  b'8 cis''4. b'4 cis''16( b'16 ais'8) |
  b'8 dis''8 dis''16 cis''16 dis''8 cis''4 b'8 cis''8 |
  b'2 cis''4 b'16( ais'16 gis'8) |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  gis4 dis4 b4 dis4 |
  cis4 gis4 e4 gis4 |
  cis4 gis4 e4 gis4 |
  cis4 gis4 e4 gis4 |
  \break
  gis4 dis4 b4 dis4 |
  gis4 dis4 b4 dis4 |
  gis4 dis4 b4 dis4 |
  cis4 gis4 e4 gis4 |
  \break
  cis4 gis4 e4 gis4 |
  dis4 ais4 fisis4 ais4 |
  gis4 dis4 b4 dis4 |
  gis4 dis4 b4 dis4 |
  \break
  gis4 dis4 b4 dis4 |
  dis4 ais4 fisis4 ais4 |
  cis4 gis4 e4 gis4 |
  cis4 gis4 e4 gis4 |
  \break
  gis4 dis4 b4 dis4 |
  gis4 dis4 b4 dis4 |
  gis4 dis4 b4 dis4 |
  gis4 dis4 b4 dis4 |
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
  \midi { \tempo 4 = 100 }
}
