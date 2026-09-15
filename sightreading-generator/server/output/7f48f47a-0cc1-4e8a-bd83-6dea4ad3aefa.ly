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
  \key b \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gently rocking"
  d''4.\mf r4 e''8 |
  b'8( b'8 cis''8) cis''4. |
  e''4. d''8 r4 |
  b'4. cis''4. |
  \break
  b'8 e''16 d''16 e''8 e''8 cis''16 cis''16 d''8 |
  e''4 d''8( cis''8) d''4 |
  cis''8 b'4 cis''16( cis''16 d''8 cis''8) |
  b'4 b'8 b'8 b'4 |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  b,4. fis4. |
  d4. fis4. |
  e4. b,4. |
  ais4. cis4. |
  \break
  e4. b,4. |
  g4. b,4. |
  fis4. cis4. |
  d4. fis4. |
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
