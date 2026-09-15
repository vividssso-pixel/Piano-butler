\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \key a \minor
  \time 3/4
  \tempo "Waltz"
  c''2\mf d''4 |
  d''4. e''16[ f''16] e''16[ e''16 b'8] |
  b'4 e''4 f''8[ a'8] |
  a'4 b'8([ d''8)] e''4 |
  \break
  f''4. e''8 d''4 |
  c''4. b'16[ a'16] b'4 |
  a'4 a'4. b'8 |
  b'2 a'4 |
  \break
  b'2 a'4 |
  b'4 a'2 |
  b'2 b'8.[ a'16] |
  a'4. a'8 a'4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 3/4
  a4 e4 e4 |
  e4 b4 b4 |
  e4 b4 b4 |
  a4 e4 e4 |
  \break
  d4 a4 a4 |
  e4 b4 b4 |
  a4 e4 e4 |
  e4 b4 b4 |
  \break
  e4 b4 b4 |
  e4 b4 b4 |
  e4 b4 b4 |
  a4 e4 e4 |
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
  \midi { \tempo 4 = 96 }
}
