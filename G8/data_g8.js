// ─── AMEB Grade 8 Piano — General Syllabus Data ──────────────────────────────
// Exam code: 9948 (Solo) | Source: Piano Syllabus 2026, manual pages 74–75
// Lists A, B, C, D — Series 19 / 18 / 17 / Manual

const DATA_G8 = [

  // ── LIST A ── Series 19 ────────────────────────────────────────────────────
  { "l": "A", "s": "S19", "c": "BACH, J.S.", "t": "Fantasia from Fantasia and fugue BWV 906", "nat": "German", "era": "Baroque", "key": "C minor", "focus": ["Fantasia form", "Contrapuntal texture", "Dramatic expression"] },
  { "l": "A", "s": "S19", "c": "BOWMAN, C.", "t": "Little prelude after the master", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Neo-Baroque style", "Australian music", "Imitative texture"] },
  { "l": "A", "s": "S19", "c": "CHOPIN, F.", "t": "Andantino No 1 from Trois nouvelles études KK IIb/3", "nat": "Polish", "era": "Romantic", "key": "F minor", "focus": ["Étude technique", "Legato melody", "Romantic lyricism"] },
  { "l": "A", "s": "S19", "c": "SCARLATTI, D.", "t": "Sonata K 13", "nat": "Italian", "era": "Baroque", "key": "G major", "focus": ["Baroque binary form", "Ornamentation", "Keyboard texture"] },

  // ── LIST A ── Series 18 ────────────────────────────────────────────────────
  { "l": "A", "s": "S18", "c": "BACH, J.S.", "t": "Presto 3rd movement from Concerto nach italienischen Gusto BWV 971", "nat": "German", "era": "Baroque", "key": "F major", "focus": ["Concerto style", "Technical dexterity", "Rhythmic drive"] },
  { "l": "A", "s": "S18", "c": "CZERNY, C.", "t": "Molto vivace con velocità No 24 from Op. 740", "nat": "Austrian", "era": "Romantic", "key": "Variable", "focus": ["Velocity étude", "Finger independence", "Technical brilliance"] },
  { "l": "A", "s": "S18", "c": "JENSEN, A.", "t": "Andante con sentimento No 7 from Op. 32", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Romantic lyricism", "Song without words", "Expressive playing"] },
  { "l": "A", "s": "S18", "c": "SCARLATTI, D.", "t": "Sonata K 484", "nat": "Italian", "era": "Baroque", "key": "D major", "focus": ["Binary form", "Ornamentation", "Baroque texture"] },

  // ── LIST A ── Series 17 ────────────────────────────────────────────────────
  { "l": "A", "s": "S17", "c": "BACH, J.S.", "t": "Capriccio 6th movement of Partita No 2 BWV 826", "nat": "German", "era": "Baroque", "key": "C minor", "focus": ["Dance form", "Counterpoint", "Baroque style"] },
  { "l": "A", "s": "S17", "c": "HANDEL, G.", "t": "Allegro 3rd movement of Suite HWV 431", "nat": "German", "era": "Baroque", "key": "Variable", "focus": ["Suite character", "Articulation", "Rhythmic precision"] },
  { "l": "A", "s": "S17", "c": "MOSZKOWSKI, M.", "t": "Etude No 2 from Op. 72", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Étude", "Velocity", "Technical brilliance"] },
  { "l": "A", "s": "S17", "c": "SCARLATTI, D.", "t": "Sonata K 209", "nat": "Italian", "era": "Baroque", "key": "A major", "focus": ["Binary form", "Ornamentation", "Leaps"] },

  // ── LIST A ── Manual ────────────────────────────────────────────────────────
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Gigue 7th movement from French Suite No 5 in G major BWV 816", "nat": "German", "era": "Baroque", "key": "G major", "focus": ["Gigue dance", "Counterpoint", "Baroque style"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Courante 3rd movement and Sarabande 4th movement from Partita No 1 in B♭ major BWV 825", "nat": "German", "era": "Baroque", "key": "B♭ major", "focus": ["Dance suite", "Ornamentation", "Baroque character"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Prelude and Fugue in E major BWV 854 from Das wohltemperierte Clavier Book 1", "nat": "German", "era": "Baroque", "key": "E major", "focus": ["Fugal writing", "WTC Book 1", "Voice leading"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Prelude and Fugue in B major BWV 868 from Das wohltemperierte Clavier Book 1", "nat": "German", "era": "Baroque", "key": "B major", "focus": ["Fugal writing", "WTC Book 1", "Counterpoint"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Prelude and Fugue in G♯ minor BWV 863 from Das wohltemperierte Clavier Book 1", "nat": "German", "era": "Baroque", "key": "G♯ minor", "focus": ["Fugal writing", "WTC Book 1", "Voice leading"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Prelude and Fugue in F minor BWV 881 from Das wohltemperierte Clavier Book 2", "nat": "German", "era": "Baroque", "key": "F minor", "focus": ["Fugal writing", "WTC Book 2", "Counterpoint"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "Prelude and Fugue in B minor BWV 893 from Das wohltemperierte Clavier Book 2", "nat": "German", "era": "Baroque", "key": "B minor", "focus": ["Fugal writing", "WTC Book 2", "Voice leading"] },
  { "l": "A", "s": "Manual", "c": "BACH, J.S.", "t": "1st movement from Concerto nach italienischen Gusto (Italienisches Konzert) BWV 971", "nat": "German", "era": "Baroque", "key": "F major", "focus": ["Concerto style", "Cantabile", "Baroque virtuosity"] },
  { "l": "A", "s": "Manual", "c": "CRAMER, J.", "t": "Study (Allegro) in E minor No 20 from 84 studies Op. 50", "nat": "German", "era": "Classical", "key": "E minor", "focus": ["Étude", "Finger equality", "Legato playing"] },
  { "l": "A", "s": "Manual", "c": "HENSELT, A.", "t": "Repos d'amour [Love's repose] No 4 from Douze études caractéristiques Op. 2", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Étude", "Romantic lyricism", "Cantabile"] },
  { "l": "A", "s": "Manual", "c": "HINDEMITH, P.", "t": "Interludium (Pastorale, moderato) and Fuga tertia in F from Ludus Tonalis", "nat": "German", "era": "Modern", "key": "F major", "focus": ["Modern counterpoint", "Fugal writing", "20th-century style"] },
  { "l": "A", "s": "Manual", "c": "MOSCHELES, A.", "t": "Etude (Allegro brillante) in G major No 3 from 24 études Op. 70", "nat": "German", "era": "Romantic", "key": "G major", "focus": ["Étude", "Brilliance", "Virtuosity"] },
  { "l": "A", "s": "Manual", "c": "MOSCHELES, A.", "t": "Etude (Lentamente con tranquilezza) in E major No 4 from 24 études Op. 70", "nat": "German", "era": "Romantic", "key": "E major", "focus": ["Étude", "Cantabile", "Tone control"] },
  { "l": "A", "s": "Manual", "c": "MOSZKOWSKI, M.", "t": "Etude (Allegro energico) in G minor No 16 from 20 petites études Op. 91 Book 2", "nat": "German", "era": "Romantic", "key": "G minor", "focus": ["Étude", "Energy", "Technical fluency"] },
  { "l": "A", "s": "Manual", "c": "SCARLATTI, D.", "t": "Sonata in A major K 342", "nat": "Italian", "era": "Baroque", "key": "A major", "focus": ["Binary form", "Ornamentation", "Keyboard style"] },
  { "l": "A", "s": "Manual", "c": "SCARLATTI, D.", "t": "Sonata in G major K 427", "nat": "Italian", "era": "Baroque", "key": "G major", "focus": ["Binary form", "Texture", "Ornamentation"] },
  { "l": "A", "s": "Manual", "c": "SCARLATTI, D.", "t": "Sonata in C major K 513", "nat": "Italian", "era": "Baroque", "key": "C major", "focus": ["Binary form", "Articulation", "Baroque style"] },

  // ── LIST B ── Series 19 ────────────────────────────────────────────────────
  { "l": "B", "s": "S19", "c": "CLEMENTI, M.", "t": "Allegro con brio First movement of Sonata Op. 24 No 2", "nat": "Italian", "era": "Classical", "key": "G major", "focus": ["Sonata form", "Articulation", "Virtuosity"] },
  { "l": "B", "s": "S19", "c": "GALUPPI, B.", "t": "Allegro Second movement of Sonata T 12", "nat": "Italian", "era": "Classical", "key": "Variable", "focus": ["Galant style", "Melody", "Classical elegance"] },
  { "l": "B", "s": "S19", "c": "HAYDN, J.", "t": "Moderato First movement of Sonata Hob XVI:44", "nat": "Austrian", "era": "Classical", "key": "G minor", "focus": ["Sonata form", "Classical style", "Ornamentation"] },
  { "l": "B", "s": "S19", "c": "MOZART, W.A.", "t": "Allegro First movement of Sonata K 281", "nat": "Austrian", "era": "Classical", "key": "B♭ major", "focus": ["Sonata form", "Mozartian grace", "Singing tone"] },

  // ── LIST B ── Series 18 ────────────────────────────────────────────────────
  { "l": "B", "s": "S18", "c": "CLEMENTI, M.", "t": "Allegro con spirito 1st movement of Sonata Op. 7 No 3", "nat": "Italian", "era": "Classical", "key": "G minor", "focus": ["Sonata form", "Articulation", "Dramatic energy"] },
  { "l": "B", "s": "S18", "c": "HAYDN, J.", "t": "Allegro moderato 1st movement of Sonata Hob XVI:22", "nat": "Austrian", "era": "Classical", "key": "E major", "focus": ["Classical style", "Transparency", "Ornamentation"] },
  { "l": "B", "s": "S18", "c": "KOZELUCH, L.", "t": "Allegro 1st movement of Sonata Op. 30 No 1", "nat": "Czech", "era": "Classical", "key": "Variable", "focus": ["Classical sonata", "Elegance", "Clarity"] },
  { "l": "B", "s": "S18", "c": "MÉHUL, E.-N.", "t": "Fièrement 1st movement of Sonata Op. 1 No 2", "nat": "French", "era": "Classical", "key": "Variable", "focus": ["French Classical", "Character", "Articulation"] },

  // ── LIST B ── Series 17 ────────────────────────────────────────────────────
  { "l": "B", "s": "S17", "c": "HAYDN, J.", "t": "Allegro 1st movement of Sonata Hob XVI:49", "nat": "Austrian", "era": "Classical", "key": "E♭ major", "focus": ["Classical form", "Ornamentation", "Haydn wit"] },
  { "l": "B", "s": "S17", "c": "KOZELUCH, L.", "t": "Allegro con brio 1st movement of Sonata Op. 1 No 3", "nat": "Czech", "era": "Classical", "key": "Variable", "focus": ["Classical sonata", "Drive", "Articulation"] },
  { "l": "B", "s": "S17", "c": "MOZART, W.", "t": "Allegro con spirito 1st movement of Sonata K 311 (284c)", "nat": "Austrian", "era": "Classical", "key": "D major", "focus": ["Sonata form", "Energy", "Ornaments"] },
  { "l": "B", "s": "S17", "c": "SCHUBERT, F.", "t": "Allegro moderato 1st movement of Sonata D 459", "nat": "Austrian", "era": "Romantic", "key": "E major", "focus": ["Romantic sonata", "Lyricism", "Harmonic colour"] },

  // ── LIST B ── Manual ────────────────────────────────────────────────────────
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Rondo – Grazioso 4th movement from Sonata in A major Op. 2 No 2", "nat": "German", "era": "Classical", "key": "A major", "focus": ["Rondo form", "Classical wit", "Lightness"] },
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Rondo – Poco allegretto e grazioso 4th movement from Sonata in E♭ major Op. 7", "nat": "German", "era": "Classical", "key": "E♭ major", "focus": ["Rondo form", "Grace", "Long-range phrasing"] },
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Allegro con brio 1st movement from Sonata in B♭ major Op. 22", "nat": "German", "era": "Classical", "key": "B♭ major", "focus": ["Sonata form", "Virtuosity", "Development"] },
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Allegro 1st movement from Sonata in D major Op. 28", "nat": "German", "era": "Classical", "key": "D major", "focus": ["Sonata form", "Pastoral character", "Development"] },
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Allegro vivace 1st movement from Sonata in G major Op. 31 No 1", "nat": "German", "era": "Classical", "key": "G major", "focus": ["Sonata form", "Humor", "Development"] },
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Polonaise in C major Op. 89", "nat": "German", "era": "Classical", "key": "C major", "focus": ["Dance character", "Clarity", "Elegance"] },
  { "l": "B", "s": "Manual", "c": "BEETHOVEN, L. van.", "t": "Rondo a Capriccio ('Rage over a lost penny') Op. 129", "nat": "German", "era": "Classical", "key": "G major", "focus": ["Rondo form", "Humor", "Technical brilliance"] },
  { "l": "B", "s": "Manual", "c": "CLEMENTI, M.", "t": "Rondo – Spiritoso 2nd movement from Sonata in C major Op. 2 No 1", "nat": "Italian", "era": "Classical", "key": "C major", "focus": ["Rondo form", "Energy", "Articulation"] },
  { "l": "B", "s": "Manual", "c": "CLEMENTI, M.", "t": "Presto 1st movement from Sonata in D major Op. 25 No 6", "nat": "Italian", "era": "Classical", "key": "D major", "focus": ["Sonata form", "Velocity", "Virtuosity"] },
  { "l": "B", "s": "Manual", "c": "CLEMENTI, M.", "t": "Rondo – Allegro assai 3rd movement from Sonata in D major Op. 25 No 6", "nat": "Italian", "era": "Classical", "key": "D major", "focus": ["Rondo form", "Velocity", "Brilliance"] },
  { "l": "B", "s": "Manual", "c": "HAYDN, J.", "t": "Moderato 1st movement from Sonata in F major Hob XVI:29", "nat": "Austrian", "era": "Classical", "key": "F major", "focus": ["Classical form", "Elegance", "Humor"] },
  { "l": "B", "s": "Manual", "c": "HAYDN, J.", "t": "Sonata in G major [complete] Hob XVI:40", "nat": "Austrian", "era": "Classical", "key": "G major", "focus": ["Complete sonata", "Classical style", "Ornamentation"] },
  { "l": "B", "s": "Manual", "c": "HAYDN, J.", "t": "Allegro 1st movement from Sonata in B♭ major Hob XVI:41", "nat": "Austrian", "era": "Classical", "key": "B♭ major", "focus": ["Classical form", "Wit", "Articulation"] },
  { "l": "B", "s": "Manual", "c": "HAYDN, J.", "t": "Fantasia in C major Hob XVII:4", "nat": "Austrian", "era": "Classical", "key": "C major", "focus": ["Fantasy form", "Harmonic exploration", "Improvisation"] },
  { "l": "B", "s": "Manual", "c": "MOZART, W.", "t": "Rondeau – Allegro 3rd movement from Sonata in B♭ major K 281 (189f)", "nat": "Austrian", "era": "Classical", "key": "B♭ major", "focus": ["Rondo form", "Grace", "Melody"] },
  { "l": "B", "s": "Manual", "c": "MOZART, W.", "t": "Allegro 1st movement from Sonata in D major K 284 (205b)", "nat": "Austrian", "era": "Classical", "key": "D major", "focus": ["Sonata form", "Brilliance", "Development"] },
  { "l": "B", "s": "Manual", "c": "MOZART, W.", "t": "Allegro assai 3rd movement from Sonata in F major K 332 (300k)", "nat": "Austrian", "era": "Classical", "key": "F major", "focus": ["Sonata form", "Energy", "Clarity"] },

  // ── LIST C ── Series 19 ────────────────────────────────────────────────────
  { "l": "C", "s": "S19", "c": "COLERIDGE-TAYLOR, S.", "t": "Andante No 2 from Three-fours (Valse suite) Op. 71", "nat": "British", "era": "Romantic", "key": "Variable", "focus": ["Waltz character", "Lyricism", "Tone colour"] },
  { "l": "C", "s": "S19", "c": "LYADOV, A.", "t": "Prelude No 1 from 3 pieces Op. 57", "nat": "Russian", "era": "Romantic", "key": "Variable", "focus": ["Miniature form", "Atmosphere", "Harmony"] },
  { "l": "C", "s": "S19", "c": "MENDELSSOHN, F.", "t": "Presto agitato No 2 from Two musical sketches WoO 15", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Character piece", "Energy", "Agitation"] },
  { "l": "C", "s": "S19", "c": "SCHUMANN, C.", "t": "Un poco agitato No 2 from Quatre pièces fugitives Op. 15", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Character piece", "Women composers", "Agitation"] },

  // ── LIST C ── Series 18 ────────────────────────────────────────────────────
  { "l": "C", "s": "S18", "c": "MACDOWELL, E.", "t": "Hexentanz No 2 from Op. 17", "nat": "American", "era": "Romantic", "key": "Variable", "focus": ["Character piece", "Brilliance", "Imagery"] },
  { "l": "C", "s": "S18", "c": "SCHUMANN, C.", "t": "Mazurka No 3 from Op. 6", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Dance character", "Women composers", "Rhythm"] },
  { "l": "C", "s": "S18", "c": "SMETANA, B.", "t": "Polka No 1 from Op. 8", "nat": "Czech", "era": "Romantic", "key": "Variable", "focus": ["Dance character", "Czech music", "Rhythm"] },
  { "l": "C", "s": "S18", "c": "TCHAIKOVSKY, P.I.", "t": "Humoresque No 2 from Op. 10", "nat": "Russian", "era": "Romantic", "key": "G major", "focus": ["Humor", "Character piece", "Elegance"] },

  // ── LIST C ── Series 17 ────────────────────────────────────────────────────
  { "l": "C", "s": "S17", "c": "CHADWICK, G.", "t": "Scherzino No 3 from Op. 7", "nat": "American", "era": "Romantic", "key": "Variable", "focus": ["Character piece", "Scherzo humor", "Lightness"] },
  { "l": "C", "s": "S17", "c": "CHOPIN, F.", "t": "Lento con gran espressione KK IVa/16", "nat": "Polish", "era": "Romantic", "key": "C♯ minor", "focus": ["Nocturne style", "Deep expression", "Lyricism"] },
  { "l": "C", "s": "S17", "c": "SCHUMANN, R.", "t": "Intermezzo No 4 from Op. 26", "nat": "German", "era": "Romantic", "key": "Variable", "focus": ["Character piece", "Introspection", "Voice leading"] },
  { "l": "C", "s": "S17", "c": "SIBELIUS, J.", "t": "Romance No 9 from Op. 24", "nat": "Finnish", "era": "Romantic", "key": "D♭ major", "focus": ["Nordic character", "Lyricism", "Atmosphere"] },

  // ── LIST C ── Manual ────────────────────────────────────────────────────────
  { "l": "C", "s": "Manual", "c": "ALBÉNIZ, I.", "t": "Prelude No 1 from Cantos de España Op. 232", "nat": "Spanish", "era": "Romantic", "key": "D major", "focus": ["Spanish character", "Atmosphere", "Rhythm"] },
  { "l": "C", "s": "Manual", "c": "CHOPIN, F.", "t": "Nocturne in F major Op. 15 No 1", "nat": "Polish", "era": "Romantic", "key": "F major", "focus": ["Nocturne", "Cantabile melody", "Ornamentation"] },
  { "l": "C", "s": "Manual", "c": "CHOPIN, F.", "t": "Mazurka in B♭ minor Op. 24 No 4", "nat": "Polish", "era": "Romantic", "key": "B♭ minor", "focus": ["Mazurka", "Polish character", "Rhythm"] },
  { "l": "C", "s": "Manual", "c": "CHOPIN, F.", "t": "Prelude in A♭ major Op. 28 No 17", "nat": "Polish", "era": "Romantic", "key": "A♭ major", "focus": ["Prelude", "Atmosphere", "Texture"] },
  { "l": "C", "s": "Manual", "c": "CHOPIN, F.", "t": "Nocturne in B major Op. 32 No 1", "nat": "Polish", "era": "Romantic", "key": "B major", "focus": ["Nocturne", "Cantabile", "Introspection"] },
  { "l": "C", "s": "Manual", "c": "CHOPIN, F.", "t": "Waltz in F minor Op. 70 No 2 (arr. FONTANA)", "nat": "Polish", "era": "Romantic", "key": "F minor", "focus": ["Waltz", "Elegance", "Character"] },
  { "l": "C", "s": "Manual", "c": "FAURÉ, G.", "t": "Andante, quasi allegretto No 1 from 3 romances sans paroles Op. 17", "nat": "French", "era": "Romantic", "key": "A♭ major", "focus": ["Song without words", "French elegance", "Flowing line"] },
  { "l": "C", "s": "Manual", "c": "GADE, N.", "t": "Scherzo (Allegro vivacissimo) No 10 from Aquarellen Op. 19", "nat": "Danish", "era": "Romantic", "key": "Variable", "focus": ["Scherzo", "Energy", "Lightness"] },
  { "l": "C", "s": "Manual", "c": "GRIEG, E.", "t": "Albumblatt [Album leaf] No 2 from Lyrische Stücken Op. 47", "nat": "Norwegian", "era": "Romantic", "key": "Variable", "focus": ["Lyric piece", "Nordic character", "Atmosphere"] },
  { "l": "C", "s": "Manual", "c": "HENSEL, F.", "t": "Lento appassionato No 4 from Six mélodies pour le piano Op. 5", "nat": "German", "era": "Romantic", "key": "B major", "focus": ["Lyricism", "Women composers", "Deep expression"] },
  { "l": "C", "s": "Manual", "c": "LISZT, F.", "t": "Klavierstück in F♯ major S 193", "nat": "Hungarian", "era": "Romantic", "key": "F♯ major", "focus": ["Character piece", "Harmonic richness", "Romanticism"] },
  { "l": "C", "s": "Manual", "c": "MACDOWELL, E.", "t": "Schattentanz [Shadow dance] No 8 from 12 Etiiden Op. 39", "nat": "American", "era": "Romantic", "key": "Variable", "focus": ["Étude", "Imagery", "American music"] },
  { "l": "C", "s": "Manual", "c": "MACDOWELL, E.", "t": "Ungarisch [Hungarian] No 12 from 12 Etiiden Op. 39", "nat": "American", "era": "Romantic", "key": "Variable", "focus": ["Étude", "Hungarian character", "Brilliance"] },
  { "l": "C", "s": "Manual", "c": "MELARTIN, E.", "t": "Elegie No 3 from 4 Klavierstücke Op. 67", "nat": "Finnish", "era": "Romantic", "key": "Variable", "focus": ["Elegy", "Lyricism", "Nordic character"] },
  { "l": "C", "s": "Manual", "c": "SCHUBERT, F.", "t": "Moment musical in A♭ major No 2 from Moments musicaux Op. 94/D780", "nat": "Austrian", "era": "Romantic", "key": "A♭ major", "focus": ["Moment musical", "Simplicity", "Lyricism"] },
  { "l": "C", "s": "Manual", "c": "SCHUBERT, F.", "t": "Moment musical in C♯ minor No 4 from Moments musicaux Op. 94/D780", "nat": "Austrian", "era": "Romantic", "key": "C♯ minor", "focus": ["Moment musical", "Urgency", "Character"] },
  { "l": "C", "s": "Manual", "c": "SCHUMANN, C.", "t": "Pièce fugitive (Andante espressivo) No 3 from Quatre pièces fugitives Op. 15", "nat": "German", "era": "Romantic", "key": "D major", "focus": ["Character piece", "Women composers", "Expression"] },
  { "l": "C", "s": "Manual", "c": "SCHUMANN, C.", "t": "Romance in B major No 3 from Quatre pièces caractéristiques Op. 5", "nat": "German", "era": "Romantic", "key": "B major", "focus": ["Romance", "Women composers", "Song style"] },
  { "l": "C", "s": "Manual", "c": "SCHUMANN, R.", "t": "Des Abends [Evening] No 1 from Fantasiestücke Op. 12", "nat": "German", "era": "Romantic", "key": "D♭ major", "focus": ["Intimate character", "Night music", "Texture"] },
  { "l": "C", "s": "Manual", "c": "SCHUMANN, R.", "t": "Romance in F♯ major No 2 from Drei Romanzen Op. 28", "nat": "German", "era": "Romantic", "key": "F♯ major", "focus": ["Romance", "Lyricism", "Counterpoint"] },
  { "l": "C", "s": "Manual", "c": "SCHUMANN, R.", "t": "Vogel als Prophet No 7 from Waldscenen Op. 82", "nat": "German", "era": "Romantic", "key": "G minor", "focus": ["Nature imagery", "Atmosphere", "Subtle touch"] },
  { "l": "C", "s": "Manual", "c": "SCHUMANN, R.", "t": "Schlummerlied [Slumber song] No 16 from Albumblätter Op. 124", "nat": "German", "era": "Romantic", "key": "E major", "focus": ["Gentle character", "Lullaby", "Voice leading"] },
  { "l": "C", "s": "Manual", "c": "SKRYABIN, A.", "t": "Andante No 1 from Two nocturnes Op. 5", "nat": "Russian", "era": "Romantic", "key": "F♯ major", "focus": ["Nocturne", "Lyricism", "Harmonic richness"] },
  { "l": "C", "s": "Manual", "c": "SZYMANOWSKA, M.", "t": "Nocturne", "nat": "Polish", "era": "Romantic", "key": "B♭ major", "focus": ["Nocturne", "Women composers", "Polish Romanticism"] },
  { "l": "C", "s": "Manual", "c": "WIDOR, C.", "t": "Valse-impromptu No 6 from 6 morceaux de salon Op. 15", "nat": "French", "era": "Romantic", "key": "Variable", "focus": ["Waltz", "French salon music", "Elegance"] },
  { "l": "C", "s": "Manual", "c": "WILCHER, P.", "t": "A rose in water", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Imagery", "Contemporary style"] },

  // ── LIST D ── Series 19 ────────────────────────────────────────────────────
  { "l": "D", "s": "S19", "c": "BOULANGER, L.", "t": "Cortège", "nat": "French", "era": "Modern", "key": "Variable", "focus": ["French music", "Processional character", "Atmosphere"] },
  { "l": "D", "s": "S19", "c": "BREWSTER-JONES, H.", "t": "Rosella's wooing No 28 from Australian bird call impressions", "nat": "Australian", "era": "Romantic", "key": "Variable", "focus": ["Australian music", "Nature imagery", "Character piece"] },
  { "l": "D", "s": "S19", "c": "CAWRSE, A.", "t": "Nightshade from Studies in odd times", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Irregular metre", "Atmosphere"] },
  { "l": "D", "s": "S19", "c": "MUNRO, I.", "t": "Banksy No 1 from Blue rags", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Ragtime influence", "Character piece"] },
  { "l": "D", "s": "S19", "c": "TURINA, J.", "t": "Trapecios volantes (Flying trapezes) No 6 from El circo Op. 68", "nat": "Spanish", "era": "Modern", "key": "Variable", "focus": ["Spanish music", "Imagery", "Rhythmic energy"] },

  // ── LIST D ── Series 18 ────────────────────────────────────────────────────
  { "l": "D", "s": "S18", "c": "BARTÓK, B.", "t": "Allegretto 1st movement from Suite Op. 14", "nat": "Hungarian", "era": "Modern", "key": "Variable", "focus": ["Modern style", "Rhythmic precision", "Economy of means"] },
  { "l": "D", "s": "S18", "c": "GLANVILLE-HICKS, P.", "t": "Prelude for a pensive pupil", "nat": "Australian", "era": "Modern", "key": "Variable", "focus": ["Australian music", "Women composers", "Reflective character"] },
  { "l": "D", "s": "S18", "c": "GRIFFES, C.", "t": "The lake at evening No 1 from Op. 5", "nat": "American", "era": "Modern", "key": "Variable", "focus": ["Impressionism", "Tone painting", "Atmosphere"] },
  { "l": "D", "s": "S18", "c": "TURINA, J.", "t": "Sacro-monte No 5 from Op. 55", "nat": "Spanish", "era": "Modern", "key": "Variable", "focus": ["Spanish music", "Flamenco influence", "Atmosphere"] },

  // ── LIST D ── Series 17 ────────────────────────────────────────────────────
  { "l": "D", "s": "S17", "c": "BARTÓK, B.", "t": "From the diary of a fly No 142 from Mikrokosmos Volume VI", "nat": "Hungarian", "era": "Modern", "key": "Variable", "focus": ["Modern style", "Tone clusters", "Character"] },
  { "l": "D", "s": "S17", "c": "EDWARDS, R.", "t": "Frangipani No 2 from Mantras and night flowers", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Imagery", "Contemporary style"] },
  { "l": "D", "s": "S17", "c": "NAZARETH, E.", "t": "Odeon", "nat": "Brazilian", "era": "Modern", "key": "Variable", "focus": ["Brazilian music", "Choro style", "Syncopation"] },
  { "l": "D", "s": "S17", "c": "RAVEL, M.", "t": "Rigaudon No 4 from Le tombeau de Couperin", "nat": "French", "era": "Modern", "key": "C major", "focus": ["Neo-classical", "French music", "Dance character"] },

  // ── LIST D ── Manual ────────────────────────────────────────────────────────
  { "l": "D", "s": "Manual", "c": "HOLLAND, D.", "t": "The lake from AMEB Piano Australian anthology (Fifth–Eighth grades)", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Tone painting", "Imagery"] },
  { "l": "D", "s": "Manual", "c": "PARKER, K.", "t": "Down Longford way from AMEB Piano Australian anthology (Fifth–Eighth grades)", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Character piece", "Landscape"] },
  { "l": "D", "s": "Manual", "c": "BARRATT, C.", "t": "Capriccio No 6 from Fantasy preludes", "nat": "British", "era": "Modern", "key": "Variable", "focus": ["Capriccio", "Humor", "Contemporary style"] },
  { "l": "D", "s": "Manual", "c": "BARTÓK, B.", "t": "Dance in Bulgarian rhythm No 153 from Mikrokosmos BB 105", "nat": "Hungarian", "era": "Modern", "key": "Variable", "focus": ["Bulgarian rhythm", "Asymmetric metre", "Modernity"] },
  { "l": "D", "s": "Manual", "c": "BENJAMIN, A.", "t": "Jamaican rumba from Piano music by British and American composers", "nat": "British", "era": "Modern", "key": "Variable", "focus": ["Caribbean influence", "Rhythm", "Character piece"] },
  { "l": "D", "s": "Manual", "c": "BUTTERLEY, N.", "t": "Il Gubbo", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Contemporary style", "Character"] },
  { "l": "D", "s": "Manual", "c": "CARR-BOYD, A.", "t": "Prelude", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Women composers", "Contemporary style"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "Danseuses de Delphie [Dancers of Delphi] No 1 from Préludes Book 1 L 117", "nat": "French", "era": "Modern", "key": "B♭ major", "focus": ["Impressionism", "Atmosphere", "Timbre"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "Voiles [Veils/Sails] No 2 from Préludes Book 1 L 117", "nat": "French", "era": "Modern", "key": "Variable", "focus": ["Whole-tone scale", "Impressionism", "Colour"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "Des pas sur la neige [Footsteps in the snow] No 6 from Préludes Book 1 L 117", "nat": "French", "era": "Modern", "key": "D minor", "focus": ["Atmosphere", "Impressionism", "Pedal technique"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "La sérénade interrompue [Interrupted serenade] No 9 from Préludes Book 1 L 117", "nat": "French", "era": "Modern", "key": "Variable", "focus": ["Spanish influence", "Impressionism", "Humor"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "La cathédrale engloutie [The submerged cathedral] No 10 from Préludes Book 1 L 117", "nat": "French", "era": "Modern", "key": "C major", "focus": ["Impressionism", "Texture", "Sonority"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "Bruyères No 5 from Préludes Book 2 L 123", "nat": "French", "era": "Modern", "key": "A♭ major", "focus": ["Impressionism", "Gentle atmosphere", "Lyricism"] },
  { "l": "D", "s": "Manual", "c": "DEBUSSY, C.", "t": "Canope [Canopic jar] No 10 from Préludes Book 2 L 123", "nat": "French", "era": "Modern", "key": "Variable", "focus": ["Impressionism", "Ancient imagery", "Restraint"] },
  { "l": "D", "s": "Manual", "c": "GERSHWIN, G.", "t": "Fascinating rhythm from Gershwin at the keyboard", "nat": "American", "era": "Modern", "key": "Variable", "focus": ["Jazz style", "Syncopation", "Rhythmic energy"] },
  { "l": "D", "s": "Manual", "c": "GERSHWIN, G.", "t": "I got rhythm from Gershwin at the keyboard", "nat": "American", "era": "Modern", "key": "Variable", "focus": ["Jazz style", "Rhythm", "Character"] },
  { "l": "D", "s": "Manual", "c": "GERSHWIN, G.", "t": "Prelude No 1 from Three preludes", "nat": "American", "era": "Modern", "key": "B♭ major", "focus": ["Blues influence", "Jazz style", "Rhythmic drive"] },
  { "l": "D", "s": "Manual", "c": "HYDE, M.", "t": "Reflected reeds from Piano works of Miriam Hyde", "nat": "Australian", "era": "Modern", "key": "Variable", "focus": ["Australian music", "Women composers", "Tone painting"] },
  { "l": "D", "s": "Manual", "c": "JANÁČEK, L.", "t": "Naše večery [Our evenings] No 1 from Po zarostlém chodníčku JW VIII/17", "nat": "Czech", "era": "Modern", "key": "Variable", "focus": ["Czech music", "Intimate character", "Speech rhythm"] },
  { "l": "D", "s": "Manual", "c": "KODÁLY, Z.", "t": "Allegretto grazioso No 8 from Nine piano pieces Op. 3", "nat": "Hungarian", "era": "Modern", "key": "Variable", "focus": ["Hungarian style", "Folk influence", "Character"] },
  { "l": "D", "s": "Manual", "c": "LIGETI, G.", "t": "Allegro con spirito No 3 from Music ricercata", "nat": "Hungarian", "era": "Contemporary", "key": "Variable", "focus": ["Contemporary style", "Motivic development", "Energy"] },
  { "l": "D", "s": "Manual", "c": "MOMPOU, F.", "t": "Jeune filles au jardin from Scènes d'enfants", "nat": "Spanish", "era": "Modern", "key": "Variable", "focus": ["Imagery", "Simplicity", "Spanish character"] },
  { "l": "D", "s": "Manual", "c": "POULENC, F.", "t": "Nocturne No 1 in C major (1929)", "nat": "French", "era": "Modern", "key": "C major", "focus": ["Nocturne", "French style", "Simplicity"] },
  { "l": "D", "s": "Manual", "c": "POULENC, F.", "t": "Mouvement perpétuel No 3 from Trois mouvements perpétuels Schmidt 14", "nat": "French", "era": "Modern", "key": "Variable", "focus": ["Ostinato", "French wit", "Perpetual motion"] },
  { "l": "D", "s": "Manual", "c": "POULENC, F.", "t": "Novelette in B♭ minor No 2 from Deux novelettes Schmidt 47", "nat": "French", "era": "Modern", "key": "B♭ minor", "focus": ["Character piece", "French style", "Wit"] },
  { "l": "D", "s": "Manual", "c": "PROKOFIEV, S.", "t": "Allegretto No 13 and Feroce No 14 from Visions fugitives Op. 22", "nat": "Russian", "era": "Modern", "key": "Variable", "focus": ["Visions fugitives", "Contrasting moods", "Modernity"] },
  { "l": "D", "s": "Manual", "c": "PROKOFIEV, S.", "t": "Presto agitatissimo e molto accentuato No 19 and Lento No 20 from Visions fugitives Op. 22", "nat": "Russian", "era": "Modern", "key": "Variable", "focus": ["Visions fugitives", "Contrasting moods", "Technical control"] },
  { "l": "D", "s": "Manual", "c": "RAVEL, M.", "t": "Menuet No 5 from Le tombeau de Couperin", "nat": "French", "era": "Modern", "key": "D major", "focus": ["Neo-classical", "Elegance", "French music"] },
  { "l": "D", "s": "Manual", "c": "RAVEL, M.", "t": "Mouvement de menuet 2nd movement from Sonatine", "nat": "French", "era": "Modern", "key": "C♯ minor", "focus": ["Neo-classical", "Delicacy", "French music"] },
  { "l": "D", "s": "Manual", "c": "SATIE, E.", "t": "Sonatine bureaucratique", "nat": "French", "era": "Modern", "key": "Variable", "focus": ["Humor", "Parody", "French music"] },
  { "l": "D", "s": "Manual", "c": "SCHOENBERG, A.", "t": "Leicht, zart No 1, Langsam No 2 and Sehr langsam Viertel No 3 from 6 kleine Klavierstücke Op. 19", "nat": "Austrian", "era": "Modern", "key": "Variable", "focus": ["Atonality", "Aphorism", "Expressionism"] },
  { "l": "D", "s": "Manual", "c": "SCHOENBERG, A.", "t": "Rasch, aber leicht No 4, Etwas rasch No 5 and Sehr langsam No 6 from 6 kleine Klavierstücke Op. 19", "nat": "Austrian", "era": "Modern", "key": "Variable", "focus": ["Atonality", "Aphorism", "Expressionism"] },
  { "l": "D", "s": "Manual", "c": "SHOSTAKOVICH, D.", "t": "Three fantastic dances Op. 5", "nat": "Russian", "era": "Modern", "key": "Variable", "focus": ["Character pieces", "Humor", "Russian style"] },
  { "l": "D", "s": "Manual", "c": "SITSKY, L.", "t": "Nocturne canonique No 154 from Century Volume 3", "nat": "Australian", "era": "Contemporary", "key": "Variable", "focus": ["Australian music", "Nocturne", "Contrapuntal writing"] },
  { "l": "D", "s": "Manual", "c": "TOCH, E.", "t": "Der Jongleur [The juggler] No 3 from Burlesken Op. 31", "nat": "Austrian", "era": "Modern", "key": "Variable", "focus": ["Humor", "Character piece", "Energy"] },
  { "l": "D", "s": "Manual", "c": "VILLA-LOBOS, H.", "t": "Senhora Dona Viúva No 5 from Guia prático Volume 2", "nat": "Brazilian", "era": "Modern", "key": "Variable", "focus": ["Brazilian music", "Folk influence", "Character"] },

];
