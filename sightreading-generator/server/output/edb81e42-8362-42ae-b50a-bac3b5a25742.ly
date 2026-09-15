\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \time 2/4
  \tempo "Allegretto"
  ees''16([\mp ees''8 d''8] c''8[ d''16)] |
  ees''4. f''16([ c''16)] |
  d''2 |
  d''2 |
  \break
  ees''16([ f''16 d''8] ees''16[ d''8 c''16)] |
  bes'8.([ aes'16)] c''4 |
  d''4. f''16([ f''16)] |
  ees''4 c''16([ d''16 c''8)] |
  \break
  bes'8([ aes'8)] aes'4 |
  r4 bes'8([ aes'8)] |
  bes'8([ c''16 d''8] c''16[ bes'8)] |
  aes'4 bes'4 |
  \break
  c''8([ bes'16 c''8] ees''16[ d''8)] |
  bes'8([ c''16 d''8] ees''16[ ees''8)] |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  aes4 ees4 |
  aes4 ees4 |
  bes4 f4 |
  bes4 f4 |
  \break
  aes4 ees4 |
  bes4 f4 |
  bes4 f4 |
  aes4 ees4 |
  \break
  bes4 f4 |
  ees4 bes4 |
  bes4 f4 |
  aes4 ees4 |
  \break
  aes4 ees4 |
  ees4 bes4 |
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
  \midi { \tempo 4 = 96 }
}
