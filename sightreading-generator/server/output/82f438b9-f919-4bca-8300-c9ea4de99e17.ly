\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \key d \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Cheekily"
  d''4.\(\pp cis''8 d''16 cis''4. d''16 |
  cis''2 d''16( cis''8) b'4 b'16 |
  b'4 b'8 cis''4. b'8 a'16 b'16 |
  a'4. b'16( a'8.) b'4\) a'16( b'16) |
  \break
  e''8( d''8) d''4\( cis''8 d''4. |
  d''4 e''4. d''8( e''8 d''8) |
  d''4 d''16 cis''4. fis'16( g'16 fis'8 fis'16) |
  g'8. b'4 cis''4. d''8 d''16\) |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  d2 a2 |
  g2 d2 |
  g2 d2 |
  d2 a2 |
  \break
  d2 a2 |
  d2 a2 |
  d2 a2 |
  d2 a2 |
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
  \midi { \tempo 4 = 92 }
}
