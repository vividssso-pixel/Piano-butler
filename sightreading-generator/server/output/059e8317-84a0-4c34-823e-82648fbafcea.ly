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
  \key bes \major
  \time 3/4
  \tempo "Espressivo"
  <d''\p bes'>4.-. <ees'' c''>8 <f'' d''>4-. |
  <ees'' c''>8 <ees'' c''>8 <f'' d''>4.-. <ees'' c''>8 |
  <d'' bes'>4.-. <f'' d''>8 <ees'' c''>4-. |
  <f'' d''>4.-. <d'' bes'>8 <ees'' c''>4-. |
  \break
  <d'' bes'>2-. <ees'' c''>4-. |
  <f'' d''>4-. <ees'' c''>4.-. <d'' bes'>8 |
  <ees'' c''>8 <ees'' c''>8 <f'' d''>4.-. <f'' d''>8 |
  <ees'' c''>4-. <d'' bes'>8 <d'' bes'>8 <d'' bes'>4-. |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 3/4
  bes2. |
  d4. ees8 f4 |
  ees8 ees8 f4. ees8 |
  d4. f8 ees4 |
  \break
  f4. d8 ees4 |
  d2 ees4 |
  f4 ees4. d8 |
  ees8 ees8 f4. f8 |
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
