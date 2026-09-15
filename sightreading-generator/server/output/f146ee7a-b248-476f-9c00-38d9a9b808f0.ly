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
  \key ees \major
  \time 3/4
  \tempo "Canon"
  ees''4.\f f''16([ ees''16] d''8[ c''16 d''16)] |
  R2. |
  R2. |
  d''2 d''8([ c''16 d''16)] |
  \break
  c''4 r4 d''8([ ees''8)] |
  d''4 r4 d''16([ ees''8 f''16)] |
  ees''4 d''4. aes'8 |
  g'16([ aes'8 bes'16)] ees''2 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 3/4
  aes2. |
  ees,4. f,16 ees,16 d8 c16 d16 |
  bes,2 aes,16 bes,8 bes,16 |
  bes,4 c2 |
  \break
  d2 d8 c16 d16 |
  c4 bes,4 d8 ees,8 |
  d4 ees,4 d16 ees,8 f,16 |
  ees2. |
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
