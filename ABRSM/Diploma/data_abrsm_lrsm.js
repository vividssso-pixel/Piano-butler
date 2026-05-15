// ABRSM LRSM Piano Repertoire List
// Source: Piano LRSM Repertoire [7 Nov 2023] FINAL.pdf
// Valid from November 2023 until further notice
// Open repertoire pool — candidates programme from this list per qualification spec
// Total: 91 entries

const DATA_ABRSM_LRSM = [
  // A
  { "c": "ADÈS, Thomas", "t": "Darknesse Visible", "nat": "English", "era": "Contemporary", "focus": ["Textural complexity", "Extended harmony", "Expressive depth"] },
  { "c": "ALBÉNIZ", "t": "Any one of the 12 pieces from 'Iberia', except No. 1 'Evocación'", "nat": "Spanish", "era": "Romantic", "focus": ["Spanish idiom", "Colouristic writing", "Rhythmic vitality"] },

  // B
  { "c": "BACH, C.P.E.", "t": "Fantasia in F# minor, H. 300, Wq. 67", "nat": "German", "era": "Classical", "focus": ["Fantasy style", "Expressive freedom", "Ornamentation"] },
  { "c": "BACH, J.S.", "t": "Chromatic Fantasia and Fugue in D minor, BWV 903", "nat": "German", "era": "Baroque", "focus": ["Contrapuntal mastery", "Fantasy and fugue contrast", "Baroque ornamentation"] },
  { "c": "BACH, J.S.", "t": "Partita No. 2 in C minor, BWV 826: complete", "nat": "German", "era": "Baroque", "focus": ["Suite structure", "Baroque dance forms", "Contrapuntal texture"] },
  { "c": "BACH, J.S.", "t": "Partita No. 5 in G, BWV 829: complete", "nat": "German", "era": "Baroque", "focus": ["Suite structure", "Baroque style", "Keyboard clarity"] },
  { "c": "BACH, J.S.", "t": "Any one or two Preludes and Fugues from 'The Well-Tempered Clavier' (selected)", "nat": "German", "era": "Baroque", "focus": ["Contrapuntal mastery", "Key variety", "Preludes and fugues"] },
  { "c": "BARTÓK, B.", "t": "Suite, Op. 14: complete", "nat": "Hungarian", "era": "Modern", "focus": ["Percussive texture", "Folk-influenced modality", "Rhythmic drive"] },
  { "c": "BEACH, A.", "t": "Four Sketches, Op. 15: complete", "nat": "American", "era": "Romantic", "focus": ["Late-Romantic harmony", "Character pieces", "Lyrical expression"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in C, Op. 2 No. 3: complete", "nat": "German", "era": "Classical", "focus": ["Classical sonata form", "Virtuosic writing", "Dynamic contrast"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in E♭, Op. 7: complete", "nat": "German", "era": "Classical", "focus": ["Classical sonata form", "Lyrical slow movement", "Scale and balance"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in D, Op. 10 No. 3: complete", "nat": "German", "era": "Classical", "focus": ["Classical sonata form", "Slow movement pathos", "Motivic development"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in G, Op. 31 No. 1: complete", "nat": "German", "era": "Classical", "focus": ["Wit and humour", "Classical form", "Textural variety"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in D minor ('Tempest'), Op. 31 No. 2: complete", "nat": "German", "era": "Classical", "focus": ["Dramatic contrasts", "Recitative style", "Motivic unity"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in E♭, Op. 31 No. 3: complete", "nat": "German", "era": "Classical", "focus": ["Scherzo character", "Classical wit", "Structural clarity"] },
  { "c": "BEETHOVEN, L.", "t": "Sonata in E♭ ('Les Adieux'), Op. 81a: complete", "nat": "German", "era": "Classical", "focus": ["Programmatic expression", "Farewell character", "Late Classical style"] },
  { "c": "BENNETT, R.R.", "t": "Any two of the 'Five Studies'", "nat": "English", "era": "Contemporary", "focus": ["Technical study", "Contemporary idiom", "Varied articulation"] },
  { "c": "BERG, A.", "t": "Sonata, Op. 1: complete", "nat": "Austrian", "era": "Modern", "focus": ["Late Romantic harmony", "Expressionist style", "Organic form"] },
  { "c": "BONDS, M.", "t": "Troubled Water", "nat": "American", "era": "Modern", "focus": ["Jazz influences", "Spiritual character", "Expressive lyricism"] },
  { "c": "BORTKIEWICZ, S.", "t": "Any one of the 'Four Piano Pieces', Op. 65", "nat": "Ukrainian", "era": "Romantic", "focus": ["Late-Romantic style", "Lyrical expression", "Keyboard colour"] },
  { "c": "BRAHMS, J.", "t": "Capriccio in B minor, Op. 76 No. 2", "nat": "German", "era": "Romantic", "focus": ["Passionate character", "Rhythmic energy", "Late-Romantic harmony"] },
  { "c": "BRAHMS, J.", "t": "Capriccio in C# minor, Op. 76 No. 5", "nat": "German", "era": "Romantic", "focus": ["Passionate character", "Rhythmic energy", "Motivic development"] },
  { "c": "BRAHMS, J.", "t": "Capriccio in C, Op. 76 No. 8", "nat": "German", "era": "Romantic", "focus": ["Brilliant writing", "Rhythmic vitality", "Late-Romantic idiom"] },
  { "c": "BRAHMS, J.", "t": "Capriccio in D minor, Op. 116 No. 1", "nat": "German", "era": "Romantic", "focus": ["Stormy character", "Late-Romantic harmony", "Expressive depth"] },
  { "c": "BRAHMS, J.", "t": "Capriccio in G minor, Op. 116 No. 3", "nat": "German", "era": "Romantic", "focus": ["Passionate intensity", "Rhythmic drive", "Late-Romantic style"] },
  { "c": "BRAHMS, J.", "t": "Capriccio in D minor, Op. 116 No. 7", "nat": "German", "era": "Romantic", "focus": ["Closing character", "Dense texture", "Late-Romantic idiom"] },
  { "c": "BRAHMS, J.", "t": "Intermezzo in E♭ minor, Op. 118 No. 6", "nat": "German", "era": "Romantic", "focus": ["Dark introspection", "Late-Romantic harmony", "Expressive depth"] },
  { "c": "BRAHMS, J.", "t": "Rhapsody in B minor, Op. 79 No. 1", "nat": "German", "era": "Romantic", "focus": ["Passionate sweep", "Dramatic contrast", "Motivic development"] },
  { "c": "BRAHMS, J.", "t": "Rhapsody in E♭, Op. 119 No. 4", "nat": "German", "era": "Romantic", "focus": ["Brilliant writing", "Rhythmic energy", "Late-Romantic style"] },
  { "c": "BRAHMS, J.", "t": "11 Variations in D on an Original Theme, Op. 21 No. 1", "nat": "German", "era": "Romantic", "focus": ["Theme and variations", "Contrapuntal texture", "Late-Romantic harmony"] },

  // C
  { "c": "CASELLA, A.", "t": "Toccata, Op. 6", "nat": "Italian", "era": "Modern", "focus": ["Toccata style", "Percussive texture", "Rhythmic drive"] },
  { "c": "CHAMINADE, C.", "t": "Any two of the 'Six études de concert', Op. 35", "nat": "French", "era": "Romantic", "focus": ["Technical study", "Salon style", "Lyrical expression"] },
  { "c": "CHAMINADE, C.", "t": "Sonata in C minor, Op. 21: complete", "nat": "French", "era": "Romantic", "focus": ["Sonata form", "Romantic lyricism", "Dramatic contrast"] },
  { "c": "CHOPIN, F.", "t": "Any one of the 4 Ballades (G minor Op. 23 / F Op. 38 / A♭ Op. 47 / F minor Op. 52)", "nat": "Polish", "era": "Romantic", "focus": ["Narrative sweep", "Romantic expression", "Technical demands"] },
  { "c": "CHOPIN, F.", "t": "Barcarolle in F#, Op. 60", "nat": "Polish", "era": "Romantic", "focus": ["Singing tone", "Rocking rhythm", "Romantic lyricism"] },
  { "c": "CHOPIN, F.", "t": "Any two Études from '12 Études', Op. 10 or '12 Études', Op. 25", "nat": "Polish", "era": "Romantic", "focus": ["Technical study", "Expressive depth", "Musical poetry"] },
  { "c": "CHOPIN, F.", "t": "Fantaisie in F minor, Op. 49", "nat": "Polish", "era": "Romantic", "focus": ["Fantasia form", "Romantic sweep", "Dramatic contrast"] },
  { "c": "CHOPIN, F.", "t": "Polonaise-Fantaisie in A♭, Op. 61", "nat": "Polish", "era": "Romantic", "focus": ["Late style", "Structural ambiguity", "Expressive depth"] },
  { "c": "CHOPIN, F.", "t": "Any one of the 4 Scherzi (B minor Op. 20 / B♭ minor Op. 31 / C# minor Op. 39 / E Op. 54)", "nat": "Polish", "era": "Romantic", "focus": ["Brilliant writing", "Contrasting sections", "Romantic passion"] },
  { "c": "COPLAND, A.", "t": "Sonata: complete", "nat": "American", "era": "Modern", "focus": ["American modernism", "Sparse texture", "Structural clarity"] },
  { "c": "COREA, Chick", "t": "Children's Songs: any six", "nat": "American", "era": "Contemporary", "focus": ["Jazz harmony", "Simplicity and beauty", "Contemporary idiom"] },

  // D
  { "c": "DALLAPICCOLA, L.", "t": "Sonatina Canonica in E♭: complete", "nat": "Italian", "era": "Modern", "focus": ["Twelve-tone technique", "Canon writing", "Structural rigour"] },
  { "c": "DEBUSSY, C.", "t": "Any one or more of the 3 pieces from 'Estampes' (Pagodes / La soirée dans Grenade / Jardins sous la pluie)", "nat": "French", "era": "Modern", "focus": ["Impressionist colour", "Evocative imagery", "Tonal ambiguity"] },
  { "c": "DEBUSSY, C.", "t": "Any one, two or three of the '12 Études'", "nat": "French", "era": "Modern", "focus": ["Technical study", "Impressionist texture", "Pianistic innovation"] },
  { "c": "DEBUSSY, C.", "t": "Any one, two or three of the 6 pieces from 'Images', 1st and 2nd Sets (selected)", "nat": "French", "era": "Modern", "focus": ["Impressionist colour", "Tonal ambiguity", "Evocative imagery"] },
  { "c": "DEBUSSY, C.", "t": "L'Isle joyeuse", "nat": "French", "era": "Modern", "focus": ["Brilliant writing", "Impressionist colour", "Rhythmic energy"] },
  { "c": "DEBUSSY, C.", "t": "Any two selected Préludes from Books 1 and 2", "nat": "French", "era": "Modern", "focus": ["Character sketches", "Impressionist colour", "Tonal ambiguity"] },
  { "c": "DOHNÁNYI, E.", "t": "Rhapsody in C, Op. 11 No. 3", "nat": "Hungarian", "era": "Romantic", "focus": ["Romantic sweep", "Virtuosic writing", "Late-Romantic idiom"] },
  { "c": "DUTILLEUX, H.", "t": "Le jeu des contraires: No. 3 from 'Trois Préludes'", "nat": "French", "era": "Contemporary", "focus": ["Contrasting characters", "Contemporary harmony", "Tonal ambiguity"] },

  // F
  { "c": "FARRENC, L.", "t": "Air russe varié, Op. 17", "nat": "French", "era": "Romantic", "focus": ["Theme and variations", "Early Romantic style", "Lyrical expression"] },
  { "c": "FAURÉ, G.", "t": "Barcarolle No. 5 in F# minor, Op. 66", "nat": "French", "era": "Romantic", "focus": ["Singing tone", "Rocking rhythm", "Late-Romantic harmony"] },
  { "c": "FAURÉ, G.", "t": "Impromptu No. 3 in A♭, Op. 34", "nat": "French", "era": "Romantic", "focus": ["Impromptu character", "Flowing melody", "Textural elegance"] },
  { "c": "FAURÉ, G.", "t": "Nocturne No. 4 in E♭, Op. 36", "nat": "French", "era": "Romantic", "focus": ["Nocturne style", "Singing tone", "Late-Romantic harmony"] },
  { "c": "FAURÉ, G.", "t": "Theme and Variations in C# minor, Op. 73", "nat": "French", "era": "Romantic", "focus": ["Theme and variations", "Motivic development", "Late-Romantic harmony"] },
  { "c": "FERGUSON, H.", "t": "Sonata in F minor, Op. 8: complete", "nat": "Irish", "era": "Modern", "focus": ["Sonata form", "Expressive depth", "20th-century idiom"] },
  { "c": "FINNISSY, Michael", "t": "Yvaropera 5", "nat": "English", "era": "Contemporary", "focus": ["Extended technique", "Contemporary idiom", "Complexity and density"] },
  { "c": "FRICKER, P.R.", "t": "Study No. 2 and No. 4 from '12 Studies', Op. 38", "nat": "English", "era": "Modern", "focus": ["Technical study", "20th-century idiom", "Rhythmic precision"] },

  // G
  { "c": "GINASTERA, A.", "t": "Any one or more of the 3 'Danzas Argentinas', Op. 2", "nat": "Argentine", "era": "Modern", "focus": ["Argentine folk idiom", "Rhythmic vitality", "National character"] },
  { "c": "GINASTERA, A.", "t": "Sonata No. 1, Op. 22: complete", "nat": "Argentine", "era": "Modern", "focus": ["Toccata energy", "National idiom", "Structural ambition"] },
  { "c": "GRANADOS, E.", "t": "Any one of the 6 pieces from 'Goyescas', Vols 1 and 2", "nat": "Spanish", "era": "Romantic", "focus": ["Spanish idiom", "Romantic expression", "Colouristic writing"] },
  { "c": "GRIFFES, C.", "t": "The White Peacock and The Fountain of the Acqua Paola from 'Roman Sketches', Op. 7", "nat": "American", "era": "Modern", "focus": ["Impressionist colour", "Evocative imagery", "Tonal ambiguity"] },
  { "c": "GUBAIDULINA, Sofia", "t": "Musical Toys: complete", "nat": "Russian", "era": "Contemporary", "focus": ["Character pieces", "Contemporary idiom", "Imaginative writing"] },

  // H
  { "c": "HAYDN, J.", "t": "Sonata in C, Hob.XVI/50: complete", "nat": "Austrian", "era": "Classical", "focus": ["Classical sonata form", "Wit and humour", "Structural clarity"] },
  { "c": "HAYDN, J.", "t": "Sonata in E♭, Hob.XVI/52: complete", "nat": "Austrian", "era": "Classical", "focus": ["Classical sonata form", "Lyrical writing", "Structural mastery"] },
  { "c": "HENSEL, F.", "t": "Ostersonate: complete", "nat": "German", "era": "Romantic", "focus": ["Sonata form", "Romantic lyricism", "Expressive depth"] },
  { "c": "HINDEMITH, P.", "t": "Selected Interludes and Fugues from 'Ludus Tonalis'", "nat": "German", "era": "Modern", "focus": ["Contrapuntal mastery", "Neo-classical idiom", "Structural rigour"] },
  { "c": "HINDEMITH, P.", "t": "Sonata No. 2 in G: complete", "nat": "German", "era": "Modern", "focus": ["Neo-classical style", "Linear writing", "Structural clarity"] },
  { "c": "HINDEMITH, P.", "t": "Sonata No. 3 in B♭: complete", "nat": "German", "era": "Modern", "focus": ["Neo-classical style", "Rhythmic energy", "Contrapuntal texture"] },
  { "c": "HOUGH, Stephen", "t": "Fanfare Toccata", "nat": "English", "era": "Contemporary", "focus": ["Toccata style", "Brilliant writing", "Contemporary idiom"] },

  // I
  { "c": "IRELAND, J.", "t": "Amberley Wild Brooks", "nat": "English", "era": "Modern", "focus": ["Landscape evocation", "English pastoral", "Impressionist influence"] },
  { "c": "IRELAND, J.", "t": "April", "nat": "English", "era": "Modern", "focus": ["Lyrical expression", "English pastoral", "Impressionist influence"] },
  { "c": "IRELAND, J.", "t": "Chelsea Reach: No. 1 from 'London Pieces'", "nat": "English", "era": "Modern", "focus": ["Urban character", "English idiom", "Impressionist colour"] },
  { "c": "IRELAND, J.", "t": "Ragamuffin: No. 2 from 'London Pieces'", "nat": "English", "era": "Modern", "focus": ["Character sketch", "English idiom", "Rhythmic wit"] },

  // K
  { "c": "KABALEVSKY, D.", "t": "Sonata No. 3 in F, Op. 46: complete", "nat": "Russian", "era": "Modern", "focus": ["Sonata form", "Soviet modernism", "Rhythmic vitality"] },
  { "c": "KAZHLAYEV, Murad", "t": "Romantic Sonatina: complete", "nat": "Russian", "era": "Modern", "focus": ["Sonatina form", "Romantic lyricism", "Accessible modernism"] },
  { "c": "KELLY, Bryan", "t": "Sonata: complete", "nat": "English", "era": "Modern", "focus": ["Sonata form", "20th-century idiom", "Structural clarity"] },
  { "c": "KNUSSEN, O.", "t": "Sonya's Lullaby, Op. 16", "nat": "English", "era": "Contemporary", "focus": ["Lullaby character", "Contemporary harmony", "Expressive simplicity"] },

  // L
  { "c": "LEIGHTON, K.", "t": "Conflicts (Fantasy on Two Themes), Op. 51", "nat": "English", "era": "Modern", "focus": ["Fantasy form", "Thematic conflict", "20th-century idiom"] },
  { "c": "LISZT, F.", "t": "Any one of the 'Five Concert Studies'", "nat": "Hungarian", "era": "Romantic", "focus": ["Virtuosic writing", "Poetic character", "Technical demands"] },
  { "c": "LISZT, F.", "t": "Any one of the 'Six Paganini Studies'", "nat": "Hungarian", "era": "Romantic", "focus": ["Virtuosic transcription", "Technical demands", "Brilliant writing"] },
  { "c": "LISZT, F.", "t": "Any one of the '12 Études d'exécution transcendante', except No. 1", "nat": "Hungarian", "era": "Romantic", "focus": ["Virtuosic writing", "Programmatic character", "Technical demands"] },
  { "c": "LISZT, F.", "t": "Funérailles", "nat": "Hungarian", "era": "Romantic", "focus": ["Funeral march character", "Romantic grandeur", "Expressive depth"] },
  { "c": "LISZT, F.", "t": "Les jeux d'eaux à la Villa d'Este: No. 4 from 'Années de Pèlerinage: 3ème Année'", "nat": "Hungarian", "era": "Romantic", "focus": ["Water imagery", "Impressionist foreshadowing", "Technical demands"] },
  { "c": "LISZT, F.", "t": "St François d'Assise ('La Prédication aux oiseaux'): No. 1 from 'Deux Légendes'", "nat": "Hungarian", "era": "Romantic", "focus": ["Programmatic expression", "Lyrical writing", "Romantic spirituality"] },
  { "c": "LISZT, F.", "t": "St François de Paule ('Marchant sur les flots'): No. 2 from 'Deux Légendes'", "nat": "Hungarian", "era": "Romantic", "focus": ["Programmatic expression", "Technical demands", "Romantic spirituality"] },

  // M
  { "c": "MENDELSSOHN, F.", "t": "Rondo Capriccioso, Op. 14: complete", "nat": "German", "era": "Romantic", "focus": ["Brilliant writing", "Early Romantic style", "Technical demands"] },
  { "c": "MENDELSSOHN, F.", "t": "Selected Preludes and Fugues from 'Six Preludes and Fugues', Op. 35", "nat": "German", "era": "Romantic", "focus": ["Contrapuntal mastery", "Romantic idiom", "Structural clarity"] },
  { "c": "MENDELSSOHN, F.", "t": "Variations Sérieuses, Op. 54", "nat": "German", "era": "Romantic", "focus": ["Theme and variations", "Contrapuntal texture", "Dramatic depth"] },
  { "c": "MESSIAEN, O.", "t": "Selected Préludes from '8 Préludes' (No. 3 / No. 4)", "nat": "French", "era": "Modern", "focus": ["Modes of limited transposition", "Spiritual expression", "Colouristic harmony"] },
  { "c": "MESSIAEN, O.", "t": "Selected pieces from '20 Regards sur l'Enfant Jésus' (Nos. 8/11/14/15/16)", "nat": "French", "era": "Modern", "focus": ["Spiritual expression", "Modes of limited transposition", "Meditative depth"] },
  { "c": "MOZART, W.A.", "t": "Rondo in A minor, K. 511", "nat": "Austrian", "era": "Classical", "focus": ["Rondo form", "Expressive lyricism", "Classical elegance"] },
  { "c": "MOZART, W.A.", "t": "Sonata in A minor, K. 310: complete", "nat": "Austrian", "era": "Classical", "focus": ["Classical sonata form", "Dramatic intensity", "Minor key expression"] },
  { "c": "MOZART, W.A.", "t": "Sonata in C minor, K. 457: complete", "nat": "Austrian", "era": "Classical", "focus": ["Classical sonata form", "Dramatic contrast", "Minor key expression"] },
  { "c": "MOZART, W.A.", "t": "Sonata in F, K. 533: complete", "nat": "Austrian", "era": "Classical", "focus": ["Contrapuntal texture", "Classical form", "Mature style"] },
  { "c": "MOZART, W.A.", "t": "Sonata in D, K. 576: complete", "nat": "Austrian", "era": "Classical", "focus": ["Contrapuntal texture", "Classical elegance", "Late style"] },
  { "c": "MUCZYNSKI, R.", "t": "Desperate Measures (Paganini Variations), Op. 48", "nat": "American", "era": "Modern", "focus": ["Theme and variations", "Virtuosic writing", "Contemporary idiom"] },

  // N
  { "c": "NICOLSON, Alasdair", "t": "42nd Street Stomp", "nat": "Scottish", "era": "Contemporary", "focus": ["Jazz idiom", "Rhythmic energy", "Contemporary style"] },

  // P
  { "c": "POULENC, F.", "t": "'Napoli' Suite: complete", "nat": "French", "era": "Modern", "focus": ["Wit and humour", "French neoclassicism", "Character suite"] },
  { "c": "POULENC, F.", "t": "Nos. 2 and 7 from 'Eight Nocturnes', FP. 56", "nat": "French", "era": "Modern", "focus": ["Nocturne character", "Harmonic ambiguity", "French lyrical style"] },
  { "c": "PRICE, F.", "t": "Fantasie nègre No. 1 in E minor", "nat": "American", "era": "Modern", "focus": ["African-American idiom", "Spiritual themes", "Romantic expression"] },
  { "c": "PROKOFIEV, S.", "t": "Sonata No. 2 in D minor, Op. 14: complete", "nat": "Russian", "era": "Modern", "focus": ["Sonata form", "Russian modernism", "Rhythmic vitality"] },
  { "c": "PROKOFIEV, S.", "t": "Sonata No. 3 in A minor, Op. 28: complete", "nat": "Russian", "era": "Modern", "focus": ["One-movement sonata", "Russian modernism", "Concentrated energy"] },
  { "c": "PROKOFIEV, S.", "t": "Sonata No. 4 in C minor, Op. 29: complete", "nat": "Russian", "era": "Modern", "focus": ["Sonata form", "Lyrical writing", "Russian modernism"] },
  { "c": "PROKOFIEV, S.", "t": "Sonata No. 5 in C, Op. 38: complete", "nat": "Russian", "era": "Modern", "focus": ["Sonata form", "Neo-classical style", "Russian modernism"] },
  { "c": "PROKOFIEV, S.", "t": "Sonata No. 9 in C, Op. 103: complete", "nat": "Russian", "era": "Modern", "focus": ["Sonata form", "Late style", "Lyrical expression"] },

  // R
  { "c": "RACHMANINOFF, S.", "t": "Any one of the 9 'Etudes-tableaux', Op. 39", "nat": "Russian", "era": "Romantic", "focus": ["Expressive depth", "Technical demands", "Late-Romantic idiom"] },
  { "c": "RACHMANINOFF, S.", "t": "Selected Preludes from Op. 23 and Op. 32", "nat": "Russian", "era": "Romantic", "focus": ["Singing tone", "Late-Romantic harmony", "Technical demands"] },
  { "c": "RAVEL, M.", "t": "Jeux d'eau", "nat": "French", "era": "Modern", "focus": ["Water imagery", "Impressionist texture", "Technical demands"] },
  { "c": "RAVEL, M.", "t": "Selected movts from 'Miroirs' (Nos. 1/3/4)", "nat": "French", "era": "Modern", "focus": ["Impressionist colour", "Evocative imagery", "Technical demands"] },
  { "c": "RAVEL, M.", "t": "Ondine: No. 1 from 'Gaspard de la Nuit'", "nat": "French", "era": "Modern", "focus": ["Water imagery", "Technical virtuosity", "Impressionist colour"] },
  { "c": "RAVEL, M.", "t": "Toccata: No. 6 from 'Le Tombeau de Couperin'", "nat": "French", "era": "Modern", "focus": ["Toccata style", "Neo-classical idiom", "Technical demands"] },
  { "c": "REDGATE, Roger", "t": "Trace", "nat": "English", "era": "Contemporary", "focus": ["Extended technique", "Contemporary notation", "Sonic exploration"] },

  // S
  { "c": "SATIE, E.", "t": "Any five pieces from 'Sports et Divertissements'", "nat": "French", "era": "Modern", "focus": ["Wit and irony", "Miniature form", "French eccentricity"] },
  { "c": "SAY, Fazıl", "t": "Black Earth", "nat": "Turkish", "era": "Contemporary", "focus": ["Extended technique", "Folk-inspired writing", "Percussive texture"] },
  { "c": "SAY, Fazıl", "t": "Paganini Jazz ('extra' variations optional)", "nat": "Turkish", "era": "Contemporary", "focus": ["Jazz fusion", "Virtuosic writing", "Cross-cultural style"] },
  { "c": "SCARLATTI, D.", "t": "Selected pairs of Sonatas from specified list", "nat": "Italian", "era": "Baroque", "focus": ["Baroque keyboard style", "Binary form", "Ornamentation"] },
  { "c": "SCHOENBERG, A.", "t": "Any two of the 'Five Pieces', Op. 23", "nat": "Austrian", "era": "Modern", "focus": ["Twelve-tone technique", "Expressionist style", "Structural rigour"] },
  { "c": "SCHOENBERG, A.", "t": "Suite, Op. 25: any two movts", "nat": "Austrian", "era": "Modern", "focus": ["Twelve-tone technique", "Suite structure", "Expressionist style"] },
  { "c": "SCHUBERT, F.", "t": "Sonata in A minor, Op. 143, D. 784: complete", "nat": "Austrian", "era": "Romantic", "focus": ["Sonata form", "Lyrical expression", "Romantic depth"] },
  { "c": "SCHUBERT, F.", "t": "Sonata in C minor, D. 958: complete", "nat": "Austrian", "era": "Romantic", "focus": ["Sonata form", "Late style", "Dramatic intensity"] },
  { "c": "SCHUBERT, F.", "t": "Sonata in A, D. 959: complete", "nat": "Austrian", "era": "Romantic", "focus": ["Sonata form", "Late style", "Lyrical grandeur"] },
  { "c": "SCHUMANN, C.", "t": "Any one of the 6 'Soirées musicales', Op. 6", "nat": "German", "era": "Romantic", "focus": ["Character piece", "Early Romantic style", "Lyrical expression"] },
  { "c": "SCHUMANN, R.", "t": "Any one of the following from 'Novelletten', Op. 21 (No. 2 / No. 8)", "nat": "German", "era": "Romantic", "focus": ["Character piece", "Romantic expression", "Extended form"] },
  { "c": "SCHUMANN, R.", "t": "Sonata in G minor, Op. 22: complete", "nat": "German", "era": "Romantic", "focus": ["Sonata form", "Romantic passion", "Structural ambition"] },
  { "c": "SCHUMANN, R.", "t": "Variations on the name 'Abegg', Op. 1", "nat": "German", "era": "Romantic", "focus": ["Theme and variations", "Cryptic programme", "Early Romantic style"] },
  { "c": "SCRIABIN, A.", "t": "Etude No. 10 in D♭ from '12 Etudes', Op. 8", "nat": "Russian", "era": "Romantic", "focus": ["Singing tone", "Late-Romantic harmony", "Technical demands"] },
  { "c": "SCRIABIN, A.", "t": "Etude No. 12 in D♯ minor from '12 Etudes', Op. 8", "nat": "Russian", "era": "Romantic", "focus": ["Technical demands", "Passionate intensity", "Late-Romantic idiom"] },
  { "c": "SCRIABIN, A.", "t": "Sonata No. 4 in F#, Op. 30: complete", "nat": "Russian", "era": "Romantic", "focus": ["Mystical character", "Late-Romantic harmony", "Sonata form"] },
  { "c": "SCRIABIN, A.", "t": "Sonata No. 5 in F#, Op. 53", "nat": "Russian", "era": "Modern", "focus": ["One-movement sonata", "Atonal foreshadowing", "Concentrated intensity"] },
  { "c": "SEIBER, M.", "t": "Scherzando capriccioso", "nat": "Hungarian", "era": "Modern", "focus": ["Scherzo character", "Wit and humour", "20th-century idiom"] },
  { "c": "SHOSTAKOVICH, D.", "t": "Selected Preludes and Fugues from '24 Preludes and Fugues', Op. 87 (selected)", "nat": "Russian", "era": "Modern", "focus": ["Contrapuntal mastery", "Soviet modernism", "Structural clarity"] },
  { "c": "STILL, W.G.", "t": "Mystic Pool or Out of the Silence: No. 2 or No. 4 from 'Seven Traceries'", "nat": "American", "era": "Modern", "focus": ["Impressionist colour", "African-American idiom", "Evocative imagery"] },
  { "c": "STRAVINSKY, I.", "t": "Serenade in A: complete", "nat": "Russian", "era": "Modern", "focus": ["Neo-classical style", "Suite structure", "Tonal clarity"] },

  // T
  { "c": "TAKEMITSU, T.", "t": "Rain Tree Sketch I (1982) or II (1992)", "nat": "Japanese", "era": "Contemporary", "focus": ["Impressionist influence", "Japanese aesthetic", "Evocative imagery"] },
  { "c": "TIPPETT, M.", "t": "Sonata No. 2", "nat": "English", "era": "Modern", "focus": ["Sonata form", "Rhythmic energy", "20th-century idiom"] },

  // W
  { "c": "WEBERN, A.", "t": "Variations, Op. 27: complete", "nat": "Austrian", "era": "Modern", "focus": ["Twelve-tone technique", "Pointillist texture", "Extreme concentration"] },
  { "c": "WEIR, Judith", "t": "The King of France", "nat": "Scottish", "era": "Contemporary", "focus": ["Narrative character", "Contemporary idiom", "Wit and clarity"] },
  { "c": "WILD, E.", "t": "Any one or two of the 'Seven Virtuoso Etudes based on Gershwin Songs'", "nat": "American", "era": "Contemporary", "focus": ["Jazz transcription", "Virtuosic writing", "Technical demands"] },
  { "c": "WILLIAMS, M.L.", "t": "Any two or three of the following, arr. MacGregor (Aries / Miss D.D. / Scorpio)", "nat": "American", "era": "Modern", "focus": ["Jazz idiom", "Swing character", "African-American tradition"] }
];
