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
  ees''8(\mp f''8) d''2 c''4 |
  c''8( c''8) d''4 c''4 d''4 |
  c''4 d''2 f''4 |
  ees''8( f''8) d''4 ees''8( d''8 ees''8 c''8) |
  \break
  bes'2. r4 |
  aes'2. bes'4 |
  r4 f''2. |
  ees''4 ees''8( ees''8) ees''2 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  aes1 |
  ees,8 f,8 d2 c4 |
  c8 c8 d4 c4 d4 |
  c4 d2 f,4 |
  \break
  ees,8 f,8 d4 ees,8 d8 ees,8 c8 |
  bes,2. aes,4 |
  aes,2. bes,4 |
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
