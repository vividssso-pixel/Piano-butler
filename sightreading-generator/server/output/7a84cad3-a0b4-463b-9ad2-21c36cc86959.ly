\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  \key c \major
  \time 2/4
  \tempo "Espressivo"
  <c''\f a'>2-. |
  <d'' b'>4-. <d'' b'>8 <a' f'>8 |
  <g' e'>4-. <f' d'>4-. |
  <g' e'>4.-. <b' g'>8 |
  \break
  <a' f'>4-. <g' e'>4-. |
  <a' f'>8 <a' f'>8 <g' e'>4-. |
  <a' f'>4-. <g' e'>4-. |
  <a' f'>8 <b' g'>8 <c'' a'>4-. |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 2/4
  c4 g4 |
  g4 d4 |
  g4 d4 |
  g4 d4 |
  \break
  f4 c4 |
  f4 c4 |
  f4 c4 |
  f4 c4 |
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
  \midi { \tempo 4 = 88 }
}
