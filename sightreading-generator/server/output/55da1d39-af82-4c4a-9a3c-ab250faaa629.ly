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
  \key f \major
  \time 3/4
  \tempo "Risoluto"
  f''2.\f |
  e''4 c''4 d''4 |
  c''8[ c''8] d''4 e''4 |
  f''8[ e''16 a'16] bes'2 |
  \break
  d''2 c''4 |
  d''2 d''8[ c''8] |
  e''16[ d''16 d''16 c''16] bes'4 e''8[ d''8] |
  e''4 d''4. d''8 |
  \break
  c''2 bes'8[ c''8] |
  bes'2 c''8([ bes'8)] |
  c''4 d''4 c''4 |
  d''4 c''8[ bes'8] a'4 |
  \break
  bes'4 bes'4 a'8([ bes'8)] |
  c''8[ d''16 e''16] f''2 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 3/4
  f2. |
  f,2. |
  e4 c4 d4 |
  c8 c8 d4 e4 |
  \break
  f,8 e16 a,16 bes,2 |
  d2 c4 |
  d2 d8 c8 |
  e16 d16 d16 c16 bes,4 e8 d8 |
  \break
  e4 d4. d8 |
  c2 bes,8 c8 |
  bes,2 c8 bes,8 |
  c4 d4 c4 |
  \break
  d4 c8 bes,8 a,4 |
  f2. |
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
