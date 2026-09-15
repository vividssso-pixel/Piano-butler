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
  \tempo "Flowing"
  d''4.\p ees''8 fis''4 |
  ees''4 g'4 a'16([ c''16 bes'8)] |
  a'2. |
  g'4 a'4. bes'8 |
  \break
  c''8[ c''8] a'2 |
  bes'2 c''4 |
  d''8([ ees''8] ees''8[ d''8] \tuplet 3/2 { c''8 d''8 c''8) } |
  g'2. |
  \break
  a'4 g'4. ees''16[ fis''16] |
  ees''4 d''16[ c''16 d''8] d''4 |
  c''4. d''16[ d''16] \tuplet 3/2 { ees''8 d''8 d''8 } |
  ees''2. |
  \break
  d''2 d''4 |
  ees''16[ d''16 c''16 bes'16] a'4 g'4 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 3/4
  d4 a4 fis4 |
  g4 c4 g4 |
  fis4 a4 d4 |
  d4 bes4 d4 |
  \break
  c4 g4 ees4 |
  d4 g4 d4 |
  fis4 a4 d4 |
  d4 bes4 d4 |
  \break
  d4 a4 fis4 |
  d4 g4 d4 |
  bes4 d4 g4 |
  g4 ees4 g4 |
  \break
  d4 a4 fis4 |
  d4 g4 d4 |
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
