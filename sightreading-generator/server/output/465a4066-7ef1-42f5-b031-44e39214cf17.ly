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
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Risoluto"
  gis'16(\mf gis'16 dis''8 e''8 dis''8 e''8 ais'8) |
  b'8 cis''8 cis''16 dis''16 e''4. |
  ais'8( gis'8 dis''8 e''8 dis''8 cis''8) |
  b'8 cis''4 b'4 cis''8 |
  \break
  b'8 ais'8 gis'16 ais'16 ais'4 gis'8 |
  ais'4 gis'8( ais'8) gis'4 |
  ais'8( b'8 ais'8) b'4. |
  cis''4 b'8 cis''8 b'8 ais'8 |
  \break
  b'8( b'8 cis''8) b'4. |
  ais'8 gis'8 gis'8 ais'8 gis'8 ais'16 gis'16 |
  ais'8 b'4 ais'4 b'8 |
  cis''8 b'8 cis''8 cis''8 b'8 cis''8 |
  \break
  dis''8 e''4 dis''8 cis''4 |
  b'8 ais'4 ais'8 b'4 |
  ais'4. ais'4. |
  gis'8 gis'8 ais'8 gis'8 gis'16 gis'16 gis'8 |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  gis4. dis4. |
  gis4. dis4. |
  dis4. ais4. |
  gis4. dis4. |
  \break
  gis4. dis4. |
  dis4. ais4. |
  dis4. ais4. |
  cis4. gis4. |
  \break
  gis4. dis4. |
  gis4. dis4. |
  dis4. ais4. |
  cis4. gis4. |
  \break
  dis4. ais4. |
  gis4. dis4. |
  dis4. ais4. |
  gis4. dis4. |
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
  \midi { \tempo 4. = 67 }
}
