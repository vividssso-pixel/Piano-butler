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
  \key bes \major
  \time 3/4
  \tempo "Daintily"
  bes'4.\(\pp d''8 c''4 |
  f'4 ees'4 ees'4 |
  d'4 ees'2 |
  f'2 g'4\) |
  \break
  a'2\( a'4 |
  a'4 bes'4 c''4 |
  d''16[ ees''16 d''16 d''16] c''2 |
  bes'4 bes'2\) |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 3/4
  bes2. |
  bes,4. d8 c4 |
  f4 ees4 ees4 |
  d4 ees2 |
  \break
  f2 g4 |
  a2 a4 |
  a4 bes,4 c4 |
  bes2. |
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
