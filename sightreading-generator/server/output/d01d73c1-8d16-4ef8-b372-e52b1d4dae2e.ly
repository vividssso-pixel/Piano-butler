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
  \key d \minor
  \time 3/4
  \tempo "Valse lente"
  f''2\f a'4 |
  bes'8.[ c''16] d''4 d''4 |
  bes'4. c''8 d''16[ c''16 d''8] |
  e''4. d''16[ d''16] e''4 |
  \break
  f''4 \tuplet 3/2 { e''8( e''8 f''8 } f''8. e''16) |
  f''4. e''16([ f'16)] g'4 |
  c''2 bes'4 |
  a'8[ g'8] f'4 \tuplet 3/2 { g'8( f'8 g'8) } |
  \break
  f''2. |
  e''4 d''4. f''8 |
  e''4 c''2 |
  bes'2 a'4 |
  \break
  g'2 f'4 |
  g'4 a'8[ bes'8] d''4 |
  \bar "|."
}

bassLine = {
  \key d \minor
  \time 3/4
  d4 a4 a4 |
  g4 d4 d4 |
  g4 d4 d4 |
  a4 e4 e4 |
  \break
  d4 a4 a4 |
  d4 a4 a4 |
  a4 e4 e4 |
  d4 a4 a4 |
  \break
  d4 a4 a4 |
  d4 a4 a4 |
  a4 e4 e4 |
  g4 d4 d4 |
  \break
  g4 d4 d4 |
  d4 a4 a4 |
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
