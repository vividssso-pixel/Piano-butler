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
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gently rocking"
  f''4\p des''8( c''8 bes'8 bes'16 ges'16) |
  f'8 ges'4 f'8 aes'4 |
  aes'8( ges'8 f'8) bes'4. |
  aes'4 bes'8 aes'4. |
  \break
  aes'8 bes'4 aes'8 ges'4 |
  r4 aes'8 bes'4. |
  bes'8 aes'4 ges'8( aes'8 bes'16 c''16) |
  bes'8 c''4 des''4. |
  \break
  c''8( bes'8 c''16 des''16 c''8) des''4 |
  c''8( bes'8 c''8) des''4 des''8 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  ges4. des4. |
  f4. aes4. |
  des4. aes4. |
  f4. aes4. |
  \break
  aes4. ees4. |
  bes4. des4. |
  ges4. des4. |
  bes4. des4. |
  \break
  aes4. ees4. |
  f4. aes4. |
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
  \midi { \tempo 4. = 64 }
}
