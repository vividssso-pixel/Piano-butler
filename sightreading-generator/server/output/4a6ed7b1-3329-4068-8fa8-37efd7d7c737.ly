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
  \key f \major
  \time 6/8
  \tempo "Legato"
  f''8(\pp e''16 f''16 e''8) a'4. |
  bes'16 a'16 e''8 d''8 e''4. |
  f''4. e''8 e''16 d''8 f''16 |
  e''8( d''16 c''16 bes'8) c''4. |
  \break
  e''16( f''16 e''16 f''8 e''8 f''8 e''8 f''16) |
  e''16 e''16 d''8 c''8 d''4. |
  d''8( c''8 bes'16 a'8 a'8 bes'8 c''16) |
  bes'16 c''8 bes'8 d''8 e''8 f''8 f''16 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 6/8
  f4. c'4. |
  bes4. f4. |
  bes4. f4. |
  c'4. g4. |
  \break
  c'4. g4. |
  c'4. g4. |
  f4. c'4. |
  f4. c'4. |
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
