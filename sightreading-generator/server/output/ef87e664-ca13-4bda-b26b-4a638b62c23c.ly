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
  \key ees \major
  \time 4/4
  \tempo "Allegretto"
  ees''4\f f''4 ees''4 d''4 |
  c''4 d''2. |
  ees''4. c''8 bes'4 bes'4 |
  aes'2. bes'4 |
  \break
  c''2. \tuplet 3/2 { c''8 bes'8 c''8 } |
  bes'16( d''16 c''16 bes'16) aes'4 g'4 aes'4 |
  aes'16( aes'16 g'16 g'16) aes'2. |
  g'16( aes'16 g'16 aes'16) bes'4 ees''2 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  ees1 |
  ees,4 f,4 ees,4 d4 |
  c4 d2. |
  ees,4. c8 bes,4 bes,4 |
  \break
  aes,2. bes,4 |
  c2. c4 |
  bes,16 d16 c16 bes,16 aes,4 g,4 aes,4 |
  ees1 |
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
