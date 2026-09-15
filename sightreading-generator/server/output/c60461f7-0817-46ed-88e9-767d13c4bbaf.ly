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
  \tempo "Moderato"
  R1 |
  ees'8 f'8 ees'4. f'8 ees'4 |
  f'4. aes'8 g'2 |
  R1 |
  \break
  R1 |
  ees'4. f'4 g'4 aes'8 |
  bes'4. c''8 d''4. c''8 |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  c4\p_\markup { \italic "lilting" } d2 c4 |
  R1 |
  R1 |
  aes8 g4. aes8 g4 g8 |
  \break
  f8 g8 g4 aes8 g8 aes4 |
  R1 |
  R1 |
  aes8 g8 f4 ees4. f8 |
  \break
  f4 ees4 ees8 ees4. |
  ees2 ees2 |
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
