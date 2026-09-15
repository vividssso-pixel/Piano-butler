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
  \time 4/4
  \tempo "Hymn"
  ees''4\mf d''4. ees''8 f''4 |
  ees''16( f''8 bes'8 c''8 d''8 c''8 bes'8 f''8 ees''16) |
  f''4 bes'4 aes'2 |
  bes'2 c''4 c''4 |
  \break
  d''4. d''16( ees''8 f''8 ees''16) d''4 |
  ees''4 d''4 d''4 ees''8( c''8) |
  d''4 ees''2 d''8( c''8) |
  bes'4 c''4. bes'16( bes'8 bes'16 bes'8) |
  \break
  aes'8.( c''16) bes'2 aes'4 |
  g'4 ees''4 f''4 ees''4 |
  d''2 c''4 bes'4 |
  c''16( d''8 d''8 c''8 c''8 bes'8 c''8 d''8 ees''16) |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  <ees g bes>4 <ees g bes>4 <ees g bes>4 <ees g bes>4 |
  <ees g bes>4 <ees g bes>4 <ees g bes>4 <ees g bes>4 |
  <bes d' f>4 <bes d' f>4 <bes d' f>4 <bes d' f>4 |
  <ees g bes>4 <ees g bes>4 <ees g bes>4 <ees g bes>4 |
  \break
  <bes d' f>4 <bes d' f>4 <bes d' f>4 <bes d' f>4 |
  <aes c' ees>4 <aes c' ees>4 <aes c' ees>4 <aes c' ees>4 |
  <bes d' f>4 <bes d' f>4 <bes d' f>4 <bes d' f>4 |
  <ees g bes>4 <ees g bes>4 <ees g bes>4 <ees g bes>4 |
  \break
  <aes c' ees>4 <aes c' ees>4 <aes c' ees>4 <aes c' ees>4 |
  <ees g bes>4 <ees g bes>4 <ees g bes>4 <ees g bes>4 |
  <bes d' f>4 <bes d' f>4 <bes d' f>4 <bes d' f>4 |
  <ees g bes>4 <ees g bes>4 <ees g bes>4 <ees g bes>4 |
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
