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
  \key b \minor
  \time 3/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1 1 1)
  \tempo "Andante religioso"
  d''8(\mf cis''16 e''16) d''4 cis''4 b'16( cis''16 b'16 b'16) e''2 |
  d''2. e''8( d''16 e''16) e''4. d''8 |
  e''4 b'16( cis''16 d''16 b'16) cis''4 d''4 e''4 d''4 |
  b'2 cis''4. b'16( e''16) d''4. e''16( d''16) |
  \break
  e''4. e''8( d''8 d''8) e''4 e''4. d''16( e''16) |
  d''8.( e''16) e''4 d''4 e''8( d''16 d''16) d''4 e''4 |
  d''4 e''8( e''8) d''2 e''8( d''8 e''16 d''16 e''8) |
  d''4. e''16( d''16 e''8) d''4 e''8 d''4. e''16( d''16) |
  \break
  e''4 d''16( e''16 d''8) cis''4. cis''16( b'16 b'16 cis''16) d''4 e''8 |
  d''4. e''16( d''16 e''16 d''16) cis''4 b'8 cis''4 b'4 |
  cis''4 d''8( e''16 e''16) cis''4 b'16( cis''16 cis''16 b'16) cis''4 d''8( cis''8) |
  b'4 cis''4 d''4 d''16( d''16 e''16 d''16) e''2 |
  \break
  d''8 e''4 cis''16( d''16 e''8 d''8) b'4 cis''2 |
  d''8 cis''4 b'16( cis''16) e''2 d''4 d''8( b'16 cis''16) |
  d''4. e''16( d''16) cis''4 d''4 cis''8( d''8 b'8 cis''8) |
  cis''4. d''8 cis''4. b'8 b'2 |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 3/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1 1 1)
  b4 fis4 d4 fis4 b4 fis4 |
  d4 fis4 b4 fis4 d4 fis4 |
  b4 fis4 d4 fis4 b4 fis4 |
  g4 b4 e4 b4 g4 b4 |
  \break
  e4 b4 g4 b4 e4 b4 |
  d4 fis4 b4 fis4 d4 fis4 |
  b4 fis4 d4 fis4 b4 fis4 |
  d4 fis4 b4 fis4 d4 fis4 |
  \break
  e4 b4 g4 b4 e4 b4 |
  d4 fis4 b4 fis4 d4 fis4 |
  fis4 cis4 ais4 cis4 fis4 cis4 |
  d4 fis4 b4 fis4 d4 fis4 |
  \break
  b4 fis4 d4 fis4 b4 fis4 |
  d4 fis4 b4 fis4 d4 fis4 |
  g4 d4 b4 d4 g4 d4 |
  d4 fis4 b4 fis4 d4 fis4 |
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
