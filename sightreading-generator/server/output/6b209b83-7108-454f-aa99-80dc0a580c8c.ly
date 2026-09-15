\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \tempo "Allegretto"
  d''4\(\mp e''2 |
  d''4. b'8 a'4 |
  b'2. |
  e''2 d''4\) |
  \break
  c''16[\( b'16 e'16 fis'16] g'4 fis'4 |
  g'2. |
  g'4. fis'8 \tuplet 3/2 { g'8 a'8 b'8 } |
  a'16[ g'16 e'16 fis'16] g'4 g'4\) |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 3/4
  g4 d2 |
  g4 d2 |
  R2. |
  a4 e2 |
  \break
  R2. |
  R2. |
  g4 d2 |
  g4 d2 |
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
  \midi { \tempo 4 = 92 }
}
