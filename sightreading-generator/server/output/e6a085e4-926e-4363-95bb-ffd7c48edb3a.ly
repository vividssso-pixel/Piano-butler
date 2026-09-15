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
  \tempo "Daintily"
  ees''16(\mf d''8.) f''4 ees''2 |
  f''16( c''8 c''16) bes'4 aes'8( d''8) ees''4 |
  f''4 ees''16( aes'8 g'16) aes'4 bes'16( aes'8.) |
  g'2 aes'2 |
  \break
  bes'16( c''8 bes'8 f''16 ees''8) d''4 ees''8( d''16 ees''16) |
  d''4. d''16( ees''8 d''8 c''16) bes'4 |
  c''16( bes'8 c''16) d''4 ees''4 ees''4 |
  ees''2 ees''2 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  ees1 |
  aes1 |
  aes1 |
  ees1 |
  \break
  ees1 |
  bes1 |
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
  \midi { \tempo 4 = 92 }
}
