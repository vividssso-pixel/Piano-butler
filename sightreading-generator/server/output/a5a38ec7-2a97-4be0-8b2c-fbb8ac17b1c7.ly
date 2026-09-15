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
  \key fis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Moderato Pastorale"
  a'4\mf b'8( a'8) b'4 |
  cis''8( d''8 cis''8 cis''16 d''16 e''8 d''8) |
  d''8 cis''4 b'8 a'4 |
  d''4. e''8 a'4 |
  \break
  b'4. d''16( cis''16 d''8 cis''8) |
  d''8 r4 d''4. |
  e''4. d''8( cis''8 d''8) |
  cis''8( b'8 cis''8) d''4. |
  \break
  cis''4. d''8( e''8 d''8) |
  e''4 cis''8( b'8) r4 |
  b'8( cis''8 b'8) a'4. |
  a'4. a'8 a'4 |
  \bar "|."
}

bassLine = {
  \key fis \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  fis4. cis'4. |
  eis'4. gis4. |
  b4. fis4. |
  d'4. fis4. |
  \break
  b4. fis4. |
  d'4. fis4. |
  cis'4. gis4. |
  a4. cis'4. |
  \break
  cis'4. gis4. |
  eis'4. gis4. |
  b4. fis4. |
  a4. cis'4. |
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
