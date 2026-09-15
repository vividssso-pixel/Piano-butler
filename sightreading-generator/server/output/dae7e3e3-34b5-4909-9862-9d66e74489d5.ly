\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 8 — Reading" }
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
  \time 9/8
  \tempo "Moderato cantabile"
  f''8\pp d''4 ees''4. c''8 bes'16 c''16 ees''8 |
  d''16 ees''16 d''8 ees''8 d''4. c''4. |
  d''8 d''8 d''8 ees''8 f''4 r4 d''8 |
  c''4. bes'8 c''8 bes'8 c''4 d''8 |
  \break
  c''4. bes'8( c''16 ees''16 d''8 ees''8) c''4 |
  bes'8( c''8 d''8 ees''8 ees''8 d''16 ees''16) f''4 ees''8 |
  d''4. d''4. ees''4 f''8 |
  ees''4. f''8 ees''8 ees''8 d''8 c''8 bes'8 |
  \break
  c''8 d''4 c''16 d''16 ees''8 d''8 ees''4. |
  f''4. ees''4 f''8 ees''4 f''8 |
  f''4 ees''8( d''8) c''4 d''16 c''16 bes'8 c''8 |
  bes'8( bes'16 bes'16 c''8) d''4 d''8 ees''8 f''4 |
  \break
  ees''8 d''4 c''8 d''4 ees''4 d''8 |
  c''4. d''4. c''4 d''8 |
  c''4. bes'8 c''16 ees''16 d''8 d''4 c''8 |
  bes'4 c''8 d''4 c''8 bes'4 bes'8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 9/8
  bes1~ bes8 |
  f8 d4 ees4. c8 bes,16 c16 ees8 |
  d16 ees16 d8 ees8 d4. c4. |
  d8 d8 d8 ees8 f4 ees4 d8 |
  \break
  c4. bes,8 c8 bes,8 c4 d8 |
  c4. bes,8 c16 ees16 d8 ees8 c4 |
  bes,8 c8 d8 ees8 ees8 d16 ees16 f4 ees8 |
  d4. d4. ees4 f8 |
  \break
  ees4. f8 ees8 ees8 d8 c8 bes,8 |
  c8 d4 c16 d16 ees8 d8 ees4. |
  f4. ees4 f8 ees4 f8 |
  f4 ees8 d8 c4 d16 c16 bes,8 c8 |
  \break
  bes,8 bes,16 bes,16 c8 d4 d8 ees8 f4 |
  ees8 d4 c8 d4 ees4 d8 |
  c4. d4. c4 d8 |
  bes1~ bes8 |
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
  \midi { \tempo 4. = 72 }
}
