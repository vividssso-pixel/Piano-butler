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
  \tempo "Moderato, flowing"
  a'2\f b'4 |
  c''4 b'4 c''8[ c''8] |
  R2. |
  c''4. d''16[ d''16] f''4 |
  \break
  e''4 f''4 \tuplet 3/2 { e''8( d''8 e''8) } |
  d''2 r4 |
  e''2 f''8[ a'16 b'16] |
  c''4. d''8 e''4 |
  \break
  d''2 c''4 |
  b'4 a'8[ b'16 a'16] b'4 |
  a'4 b'4. a'8 |
  b'4 a'4. c''8 |
  \break
  b'4 c''8[ c''8] b'4 |
  a'2 a'4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 3/4
  a2. |
  a2. |
  d2. |
  d2. |
  \break
  e2. |
  d2. |
  e2. |
  a2. |
  \break
  d2. |
  e2. |
  a2. |
  a2. |
  \break
  e2. |
  a2. |
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
