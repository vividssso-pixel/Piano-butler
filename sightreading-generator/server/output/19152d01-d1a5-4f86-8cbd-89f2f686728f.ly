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
  \key ees \major
  \time 3/4
  <ees''\p_\markup { \italic "gentle" } c''>4 <ees'' c''>8 <d'' bes'>8 <c'' aes'>4 |
  <bes' g'>8 <aes' f'>8 <g' ees'>4 <c'' aes'>4 |
  <bes' g'>8 <aes' f'>8 <aes' f'>2 |
  <g' ees'>4. <bes' g'>8 <c'' aes'>4 |
  \break
  <ees'' c''>4 <f'' d''>4 <ees'' c''>8 <f'' d''>8 |
  <ees'' c''>8 <ees'' c''>8 <d'' bes'>4 <ees'' c''>8 <d'' bes'>8 |
  <c'' aes'>4. <d'' bes'>8 <c'' aes'>8 <d'' bes'>8 |
  <ees'' c''>2 <ees'' c''>8 <ees'' c''>8 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 3/4
  aes4 ees4 aes4 |
  ees4 bes4 ees4 |
  ees4 bes4 ees4 |
  ees4 bes4 ees4 |
  \break
  ees4 bes4 ees4 |
  ees4 bes4 ees4 |
  aes4 ees4 aes4 |
  aes4 ees4 aes4 |
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
