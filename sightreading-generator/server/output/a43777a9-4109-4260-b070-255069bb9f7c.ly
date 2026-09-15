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
  \time 3/4
  \tempo "Moderato"
  c''4-.\mf b'4-. a'4-. |
  g'8 e'8 f'4-. g'4-. |
  a'4-. g'4.-. a'8 |
  g'4-. a'8 g'8 a'4-. |
  \break
  g'2-. f'4-. |
  g'4-. f'8 g'8 a'4-. |
  b'2-. c''4-. |
  c''4-. c''2-. |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 3/4
  f2.-. |
  c2.-. |
  f2.-. |
  c2.-. |
  \break
  c2.-. |
  c2.-. |
  g2.-. |
  c2.-. |
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
