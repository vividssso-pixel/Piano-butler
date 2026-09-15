\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 7 — Reading" }
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
  \key bes \minor
  \time 3/4
  \tempo "Andante religioso"
  f''4.\pp ees''8( ees''8[ ees''8)] |
  des''8([ des''8] ees''8[ f''8)] ees''4 |
  c''4 bes'4 c''4 |
  bes'8.([ c''16)] des''2 |
  \break
  c''8([ des''8)] c''4 des''4 |
  ees''4 ees''4 f''4 |
  ees''4. f''16([ bes'16] bes'8[ c''8)] |
  c''16([ ees''16 ees''16 f''16)] ees''4. des''8 |
  \break
  c''4. c''8 bes'4 |
  c''2 f''4 |
  ees''2 ees''4 |
  f''2. |
  \break
  ees''4. des''8 c''4 |
  bes'4. bes'8( bes'8[ bes'8)] |
  \bar "|."
}

bassLine = {
  \key bes \minor
  \time 3/4
  ees4 bes,4 ees4 |
  bes,4 f4 bes,4 |
  f4 c4 f4 |
  bes,4 f4 bes,4 |
  \break
  f4 c4 f4 |
  ees4 bes,4 ees4 |
  ees4 bes,4 ees4 |
  f4 c4 f4 |
  \break
  f4 c4 f4 |
  f4 c4 f4 |
  ees4 bes,4 ees4 |
  f4 c4 f4 |
  \break
  ees4 bes,4 ees4 |
  bes,4 f4 bes,4 |
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
  \midi { \tempo 4 = 104 }
}
