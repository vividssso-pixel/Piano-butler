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
  \key d \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gigue"
  d''4\mp b'8 cis''8 d''4 |
  a'4 g'8 a'8 a'4 |
  b'8 a'4 g'4 b'8 |
  a'4. g'8 fis'4 |
  \break
  g'8 fis'8 g'16 fis'16 g'8 fis'8 g'16 fis'16 |
  g'4. g'4 a'8 |
  g'4 fis'8( g'8) fis'4 |
  g'4 a'8 d''4. |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  g4. d4. |
  cis'4. e4. |
  g4. d4. |
  cis'4. e4. |
  \break
  g4. d4. |
  b4. d4. |
  g4. d4. |
  fis4. a4. |
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
