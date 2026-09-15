\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 6 — Reading" }
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
  \key f \minor
  \time 3/4
  \tempo "Moderato scherzoso"
  f''4.\mf des''16([ ees''16] des''8[ ees''8)] |
  des''4 f''4. ees''8 |
  des''16([ ees''16 des''16 c''16)] bes'4 bes'4 |
  e''4 des''2 |
  \break
  bes'4 c''2 |
  des''4. ees''8( \tuplet 3/2 { aes'8 aes'8 bes'8) } |
  \tuplet 3/2 { bes'8( aes'8 bes'8) } bes'2 |
  c''4 e''4. f''16[ e''16] |
  \break
  des''2 c''8[ c''8] |
  des''8[ ees''8] f''4 ees''8[ f''8] |
  e''4 des''4. c''16[ bes'16] |
  aes'2 aes'8[ bes'8] |
  \break
  c''8.[ des''16] c''4 des''4 |
  e''4 f''4. e''16([ f''16)] |
  e''4 des''4. des''8 |
  c''2 bes'4 |
  \break
  aes'2 bes'4 |
  aes'4. bes'8( aes'16[ bes'16 aes'16 bes'16)] |
  c''16[ bes'16 aes'8] aes'4 bes'8.[ c''16] |
  des''2 f''4 |
  \bar "|."
}

bassLine = {
  \key f \minor
  \time 3/4
  bes2. |
  f,4. des16 ees16 des8 ees8 |
  des4 f,4. ees8 |
  des16 ees16 des16 c16 bes,4 bes,4 |
  \break
  ees4 des2 |
  bes,4 c2 |
  des4. ees8 aes,4 |
  bes,4 bes,2 |
  \break
  c4 ees4. f,16 ees16 |
  des2 c8 c8 |
  des8 ees8 f,4 ees8 f,8 |
  ees4 des4. c16 bes,16 |
  \break
  aes,2 aes,8 bes,8 |
  c8. des16 c4 des4 |
  ees4 f,4. ees16 f,16 |
  ees4 des4. des8 |
  \break
  c2 bes,4 |
  aes,2 bes,4 |
  aes,4. bes,8 aes,16 bes,16 aes,16 bes,16 |
  f2. |
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
  \midi { \tempo 4 = 100 }
}
