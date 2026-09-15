\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 2 — Reading" }
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
  \key g \minor
  \time 3/4
  d''8_\markup { \italic "soft" } c''8 d''8 c''8 c''4 |
  R2. |
  R2. |
  g'8 a'8 bes'2 |
  \break
  a'8 g'8 g'2 |
  g'4 g'8 g'8 g'8 g'8 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 3/4
  R2. |
  a2 g4 |
  a4. a8 a8 g8 |
  R2. |
  \break
  R2. |
  R2. |
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
  \midi { \tempo 4 = 84 }
}
