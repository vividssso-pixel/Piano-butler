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
  \key e \minor
  \time 4/4
  g'4-._\markup { \italic "cheerfully" } a'4-. b'4.-. a'8-. |
  a'4-. g'2-. fis'4-. |
  e'8-. fis'8-. e'8-. fis'8-. e'2-. |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 4/4
  R1 |
  R1 |
  R1 |
  a4-. g4-. fis8-. g8-. fis8-. g8-. |
  \break
  fis4.-. e8-. e4.-. e8-. |
  e2 e4. e8 |
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
