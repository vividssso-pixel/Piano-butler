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
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Daintily"
  d''4.\pp e''4 d''8 |
  e''4 e''8 cis''4 b'8 |
  cis''8( cis''8 d''8 e''8 d''8 cis''8) |
  d''8 cis''4 cis''4. |
  \break
  cis''8( d''16 cis''16 b'8 cis''8) b'4 |
  a'4 g'8 fis'8 g'4 |
  a'8 g'8 fis'16 g'16 a'4. |
  b'8 cis''4 d''4 d''8 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  d4. a4. |
  a4. a4. |
  a4. d4. |
  R2. |
  \break
  a4. d4. |
  R2. |
  d4. g4. |
  d4. d4. |
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
  \midi { \tempo 4. = 61 }
}
