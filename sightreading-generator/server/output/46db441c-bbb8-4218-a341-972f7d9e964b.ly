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
  \key bes \major
  \time 2/4
  \tempo "Bourrée"
  f''2\mp |
  ees''4. f''8 |
  d''4 c''16([ bes'16 f''16 ees''16)] |
  f''4 ees''4 |
  \break
  R2 |
  c''4 bes'4 |
  f''8([ ees''8] f''8[ f''16 ees''16)] |
  d''8[ c''16 d''16] c''4 |
  \break
  bes'4 c''16([ bes'16 c''16 d''16)] |
  c''4 bes'4 |
  c''4 bes'8([ c''16 d''16)] |
  c''16[ d''16 c''16 d''16] d''4 |
  \break
  c''4 bes'4 |
  c''8[ bes'16 bes'16] bes'4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 2/4
  bes4 f4 |
  c4 g4 |
  bes4 f4 |
  bes4 f4 |
  \break
  bes4 f4 |
  c4 g4 |
  f4 c4 |
  bes4 f4 |
  \break
  bes4 f4 |
  c4 g4 |
  f4 c4 |
  bes4 f4 |
  \break
  c4 g4 |
  bes4 f4 |
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
