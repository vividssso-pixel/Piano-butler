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
  \tempo "Lively"
  c''4\p d''2 |
  d''4 e''8[ d''8] c''8[ b'8] |
  a'8[ b'8] c''8[ d''8] r4 |
  d''4 a'8([ b'8] a'8[ f'8)] |
  \break
  g'8[ b'8] a'4 e'8([ f'8)] |
  g'4 f'8([ e'8)] f'4 |
  e'8([ f'8)] g'2 |
  f'4 g'8([ a'8] b'8[ c''8)] |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 3/4
  c4 e2 |
  g4 r2 |
  R2. |
  g4 b2 |
  \break
  c4 e2 |
  c4 e2 |
  c4 e2 |
  c4 e2 |
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
