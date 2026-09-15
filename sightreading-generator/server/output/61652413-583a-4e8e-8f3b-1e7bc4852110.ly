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
  \key a \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gigue"
  cis''16(\mf cis''16 d''8 e''8) d''4. |
  cis''4. d''4. |
  cis''8 d''8 cis''8 e''8 d''4 |
  cis''8( d''16 cis''16 cis''8 d''8) cis''4 |
  \break
  cis''4. d''8 e''4 |
  d''8 cis''16 d''16 cis''8 d''8 cis''16 d''16 e''8 |
  e''4 d''8( d''8 cis''16 d''16 e''8) |
  d''8 e''16 e''16 e''8 e''4. |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  a4. e'4. |
  cis'4. e'4. |
  a4. e'4. |
  cis'4. e'4. |
  \break
  a4. e'4. |
  fis'4. a4. |
  a4. e'4. |
  cis'4. e'4. |
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
