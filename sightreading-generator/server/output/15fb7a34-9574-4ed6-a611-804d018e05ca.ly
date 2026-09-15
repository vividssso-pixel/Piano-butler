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
  R1 |
  R1 |
  e'4-. fis'8-. g'8-. fis'8-. g'8-. g'4-. |
  a'4.-. b'8-. c''4-. b'4-. |
  \break
  c''4.-. d''8-. a'4-. g'4-. |
  R1 |
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 4/4
  e8-._\markup { \italic "soft" } d8-. c4.-. b,8-. c4-. |
  b,2-. c4.-. d8-. |
  R1 |
  R1 |
  \break
  R1 |
  a4-. a8-. g8-. a2-. |
  g8-. g8-. fis4-. e4-. fis8-. fis8-. |
  e8-. e8-. e8-. e8-. e2-. |
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
