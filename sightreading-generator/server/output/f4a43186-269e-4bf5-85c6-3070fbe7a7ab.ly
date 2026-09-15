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
  \time 4/4
  R1 |
  R1 |
  c'4 e'8 d'8 e'4. f'8 |
  R1 |
  \break
  R1 |
  c'8 c'4 d'4. d'4 |
  e'2 d'8 c'8 c'4 |
  c'4 c'4 c'8 c'4. |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  g4\p_\markup { \italic "gentle" } f4. e4. |
  e8 f4. c2 |
  R1 |
  a8 f4 g4 f8 e4 |
  \break
  f8 g4 d2 c8 |
  R1 |
  R1 |
  R1 |
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
