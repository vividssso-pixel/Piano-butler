\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  ees''8(\p_\markup { \italic "lilting" } d''8) r4 d''8 ees''8 d''8 ees''8 |
  bes'2 c''8( c''8) bes'4 |
  aes'2 c''2 |
  bes'4 d''2 ees''4 |
  \break
  d''2 ees''8 f''8 r4 |
  R1^\markup { \italic "dim." } |
  R1 |
  bes'4 c''8( bes'8) c''4 d''8 ees''8 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  aes1 |
  bes1 |
  aes1 |
  bes1 |
  \break
  bes1 |
  R1 |
  aes1 |
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
  \midi { \tempo 4 = 88 }
}
