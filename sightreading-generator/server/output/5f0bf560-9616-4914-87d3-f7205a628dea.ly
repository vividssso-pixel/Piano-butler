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
  \key g \minor
  \time 3/4
  \tempo "Valse lente"
  g'2\p d''4 |
  ees''2-. f''4-. |
  g'2. |
  a'4-. ees''4 fis''8[ ees''8] |
  \break
  ees''2 ees''8[ ees''8] |
  fis''4 d''4. ees''8 |
  c''2.-. |
  d''4 bes'4 c''4 |
  \break
  d''4 c''4 d''4 |
  bes'2 a'4 |
  bes'4-. a'4. bes'8 |
  c''8([ f''8] ees''16[ f''16 ees''8)] ees''4-. |
  \break
  ees''8[ f''8] ees''2 |
  fis''8([ ees''8] d''8[ c''8)] bes'4-. |
  a'4 c''4 bes'4-. |
  d''2 c''4 |
  \break
  bes'2. |
  \tuplet 3/2 { a'8 g'8 a'8 } bes'4-. a'16 g'16[ g'8] |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 3/4
  g4 d4 d4 |
  c4 g4 g4 |
  c4 g4 g4 |
  d4 a4 a4 |
  \break
  c4 g4 g4 |
  d4 a4 a4 |
  c4 g4 g4 |
  g4 d4 d4 |
  \break
  d4 a4 a4 |
  g4 d4 d4 |
  g4 d4 d4 |
  c4 g4 g4 |
  \break
  c4 g4 g4 |
  d4 a4 a4 |
  d4 a4 a4 |
  g4 d4 d4 |
  \break
  g4 d4 d4 |
  g4 d4 d4 |
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
