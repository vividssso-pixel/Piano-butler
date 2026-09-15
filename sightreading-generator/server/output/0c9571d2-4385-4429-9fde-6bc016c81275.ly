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
  \time 3/4
  \tempo "Minuet tempo"
  ees''8(\mp f''8) f''4. ees''8 |
  f''4. d''8( c''8 bes'8) |
  g'4. aes'8.( g'8.) |
  c''8( bes'8. aes'8 bes'8 aes'8.) |
  \break
  aes'4. bes'8( bes'8 c''8) |
  f''4 f''4 bes'4 |
  aes'8.( g'8 aes'8 g'8 aes'8.) |
  bes'4 aes'4 g'8( aes'8) |
  \break
  aes'4 bes'4 g'4 |
  g'8( g'8) aes'4 bes'8( ees''8) |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 3/4
  ees4. bes4. |
  bes4. f4. |
  ees4. bes4. |
  aes4. ees4. |
  \break
  aes4. ees4. |
  bes4. f4. |
  aes4. ees4. |
  ees4. bes4. |
  \break
  ees4. bes4. |
  ees4. bes4. |
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
