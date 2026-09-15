\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 6 — Reading" }
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
  \time 3/4
  \tempo "Moderato grazioso"
  b'4\mf c''4 a'4 |
  b'4 c''8.[ b'16] c''4 |
  b'8[ c''8] d''4 g'4 |
  a'4 b'8.([ b'16)] c''4 |
  \break
  d''4. c''8 b'4 |
  a'2 b'4 |
  d''2. |
  e''4 d''4 c''4 |
  \break
  c''2. |
  b'2 c''4 |
  e''2. |
  d''4. e''8 d''4 |
  \break
  c''16([ b'16 c''8)] b'4 g'4 |
  g'8([ g'16 a'16)] g'2 |
  a'4 g'2 |
  g'4 g'4. g'8 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 3/4
  g4 d4 g4 |
  g4 d4 g4 |
  g4 d4 g4 |
  a4 e4 a4 |
  \break
  g4 d4 g4 |
  a4 e4 a4 |
  d4 a4 d4 |
  a4 e4 a4 |
  \break
  a4 e4 a4 |
  g4 d4 g4 |
  a4 e4 a4 |
  d4 a4 d4 |
  \break
  c4 g4 c4 |
  c4 g4 c4 |
  d4 a4 d4 |
  g4 d4 g4 |
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
  \midi { \tempo 4 = 100 }
}
