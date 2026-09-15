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
  \key g \major
  \time 4/4
  g'4-._\markup { \italic "brightly" } a'8-. g'8-. g'4-. a'8-. b'8-. |
  a'2-. g'8-. g'8-. a'4-. |
  R1 |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 4/4
  R1 |
  R1 |
  a4.-. fis8-. e2-. |
  e8-. g8-. fis4-. g4.-. g8-. |
  \break
  a8-. g8-. g4-. g2-. |
  g4. g8 g4. g8 |
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
