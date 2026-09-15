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
  \key fis \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Flowing"
  fis'4.\f gis'8 d''4.-. e''8 |
  a'2. b'4-. |
  cis''2 b'4 eis''4 |
  d''8 gis'4-. fis'16( cis''16) d''2-. |
  \break
  eis''2-. d''4-. cis''8( b'16 cis''16) |
  d''16( cis''16 d''8 cis''16 b'8 b'16) b'2 |
  cis''4 a'16 gis'16 gis'8 a'4 a'16 b'16 cis''16 cis''16 |
  d''4-. e''16 d''16 d''8 e''2-. |
  \break
  eis''8( eis''8 d''16 cis''16 d''8) eis''4. d''8 |
  cis''8 b'4 cis''8( a'16 gis'16 fis'8) gis'4 |
  fis'4 gis'4 gis'8 a'8 b'4-. |
  a'2-. fis'8 fis'4-. fis'16( fis'16) |
  \bar "|."
}

bassLine = {
  \key fis \minor
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  b,4 fis,4 b,4 fis,4 |
  fis,4 cis4 fis,4 cis4 |
  cis4 gis,4 cis4 gis,4 |
  b,4 fis,4 b,4 fis,4 |
  \break
  cis4 gis,4 cis4 gis,4 |
  b,4 fis,4 b,4 fis,4 |
  fis,4 cis4 fis,4 cis4 |
  b,4 fis,4 b,4 fis,4 |
  \break
  cis4 gis,4 cis4 gis,4 |
  fis,4 cis4 fis,4 cis4 |
  fis,4 cis4 fis,4 cis4 |
  fis,4 cis4 fis,4 cis4 |
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
