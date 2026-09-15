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
  \key e \minor
  \time 3/4
  \tempo "Not fast but sharp"
  e''4.\p g'16[ a'16] b'4 |
  a'4. d''8( e''16[ d''16 e''8)] |
  R2. |
  b'8[ c''8] c''2 |
  \break
  c''2 b'4 |
  c''4 d''2 |
  e''4. d''8 c''4 |
  R2. |
  \break
  c''4. d''8 c''4 |
  b'2 a'4 |
  g'16([ a'16 b'16 a'16)] a'2 |
  R2. |
  \break
  dis''8[ dis''8] c''4. b'8 |
  a'4. b'8( c''8[ e''8)] |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 3/4
  e,4 b,4 g,4 |
  e,4 a,4 e,4 |
  e,4 g,4 c4 |
  e,4 c4 e,4 |
  \break
  a,4 e,4 c4 |
  e,4 a,4 e,4 |
  e,4 g,4 c4 |
  b,4 g,4 b,4 |
  \break
  a,4 e,4 c4 |
  fis,4 b,4 fis,4 |
  g,4 b,4 e,4 |
  b,4 g,4 b,4 |
  \break
  b,4 fis,4 dis4 |
  b,4 e,4 b,4 |
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
