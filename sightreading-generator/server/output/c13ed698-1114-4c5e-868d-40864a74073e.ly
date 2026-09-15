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
  \key e \minor
  \time 3/4
  \tempo "Sarabande"
  e''2\(\mf d''4 |
  e''4. d''8( c''16[ c''8 d''16)] |
  g'4. a'8( c''8[ d''8)] |
  c''4 a'4 b'4 |
  \break
  d''8([ d''8] e''8[ d''8)] c''4\) |
  d''2\( e''8([ a'8)] |
  g'4 a'4 a'4 |
  c''4 d''4 c''4 |
  \break
  b'4 c''2 |
  dis''2 e''4\) |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 3/4
  e4 <e g b>2 |
  a4 <a c' e>2 |
  a4 <a c' e>2 |
  a4 <a c' e>2 |
  \break
  b4 <b dis' fis>2 |
  b4 <b dis' fis>2 |
  e4 <e g b>2 |
  a4 <a c' e>2 |
  \break
  b4 <b dis' fis>2 |
  e4 <e g b>2 |
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
