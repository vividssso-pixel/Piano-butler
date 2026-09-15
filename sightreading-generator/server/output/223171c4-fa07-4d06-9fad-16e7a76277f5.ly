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
  \tempo "Not too fast"
  ees''2\(\p d''16( g'16 aes'8 aes'8 g'8) |
  aes'4 c''2 bes'4 |
  bes'4 aes'8( ees''16 f''8 ees''16 ees''8) d''4 |
  c''4 f''4. ees''8 d''4~\) |
  \break
  d''4\( bes'4. c''8 ees''4 |
  ees''8( f''8) ees''4 ees''4. d''16( f''16) |
  f''8( ees''16 f''8 ees''8 f''8 ees''8 f''8 ees''8 d''16) |
  ees''8 d''8 ees''16 ees''8 d''8 ees''8 ees''8 ees''8 ees''16\) |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  ees4 bes4 ees4 bes4 |
  aes4 ees4 aes4 ees4 |
  ees4 bes4 ees4 bes4 |
  aes4 ees4 aes4 ees4 |
  \break
  aes4 ees4 aes4 ees4 |
  aes4 ees4 aes4 ees4 |
  bes4 f4 bes4 f4 |
  ees4 bes4 ees4 bes4 |
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
