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
  \time 4/4
  \tempo "Lively"
  <d''\p bes'>4. <f'' d''>8 <f'' d''>4 <ees'' c''>8 <f'' d''>8 |
  <d'' bes'>2 <ees'' c''>4 <f'' d''>4 |
  <d'' bes'>2 <ees'' c''>4 <d'' bes'>4 |
  <ees'' c''>4 <f'' d''>4 <ees'' c''>4 <f'' d''>4 |
  \break
  <ees'' c''>4. <f'' d''>8 <f'' d''>4 <d'' bes'>8 <ees'' c''>8 |
  <f'' d''>2 <ees'' c''>8 <ees'' c''>4 <f'' d''>8 |
  <ees'' c''>8 <d'' bes'>4 <ees'' c''>4 <ees'' c''>4 <d'' bes'>8 |
  <ees'' c''>8 <f'' d''>4 <f'' d''>4 <f'' d''>4 <f'' d''>8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 4/4
  bes4 f'4 bes4 f'4 |
  bes4 f'4 bes4 f'4 |
  bes4 f'4 bes4 f'4 |
  ees'4 bes4 ees'4 bes4 |
  \break
  ees'4 bes4 ees'4 bes4 |
  bes4 f'4 bes4 f'4 |
  ees'4 bes4 ees'4 bes4 |
  bes4 f'4 bes4 f'4 |
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
