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
  \key d \minor
  \time 4/4
  \tempo "Moderato grazioso"
  d''4.-.\p e''8 d''2 |
  bes'2 bes'4 c''4 |
  d''4.-. f''16 e''16 d''4-. c''4 |
  d''2 e''8 f''8 g'4 |
  \break
  f'4-. g'4-. a'2-. |
  cis''8 d''8 cis''4 bes'4. cis''16 bes'16 |
  a'4-. bes'4 f'8.( g'16) a'4 |
  bes'4 d''4.-. c''8 d''8 e''8 |
  \break
  e''4 cis''4. bes'8 cis''4-. |
  d''16 c''16 d''8 e''4 f''4-. f''4-. |
  e''2 d''4-. f''8. e''16 |
  d''2 d''4.-. d''8 |
  \bar "|."
}

bassLine = {
  \key d \minor
  \time 4/4
  d4-. a4-. f4-. a4-. |
  g4-. d4 bes4-. d4 |
  d4-. a4 f4 a4 |
  d4 a4 f4 a4-. |
  \break
  d4 a4 f4 a4-. |
  a4 e4 cis4-. e4-. |
  d4 a4 f4-. a4 |
  g4 d4-. bes4-. d4-. |
  \break
  a4 e4 cis4-. e4-. |
  d4 a4-. f4 a4 |
  a4 e4-. cis4-. e4 |
  d4 a4-. f4 a4-. |
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
