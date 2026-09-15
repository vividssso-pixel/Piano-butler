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
  e''4\f e''8 d''8 c''4. b'8 |
  a'2 b'8 c''8 d''4 |
  d''8 c''4. b'8 b'4 b'8 |
  f'2 e'4 f'8 a'8 |
  \break
  b'2 c''4 a'8 g'8 |
  f'4. g'2 a'8 |
  g'4 a'8 d''4. c''4 |
  e''4 d''4 c''2 |
  \break
  d''2 c''4. d''8 |
  e''4 d''4 c''8 c''4. |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  c1 |
  f1 |
  g1 |
  f1 |
  \break
  g1 |
  f1 |
  c1 |
  c1 |
  \break
  g1 |
  c1 |
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
