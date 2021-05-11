#!/usr/bin/env python3

# Tests are organized in a dictionary:
#   'input' : 'expected-output'

seventh_tests = {
# --------------------------------
#   C SEVENTHS
# --------------------------------
    # C dominant seventh
    'C7':       [0, 16],
    'Cdom7':    [0, 16],
    'Cdom':     [0, 16],
    'C7dim5':   [0, 16],

    # C dominant flat seventh
    'C7b5':     [0, 17],
    'C7-5':     [0, 17],
    'Cdom7b5':  [0, 17],
    'Cdom7-5':  [0, 17],

    # C major seventh
    'CM7':      [0, 18],
    'Cmaj7':    [0, 18],
    'CΔ7':      [0, 18],
    'Cmajor7':  [0, 18],

    # C major seventh flat five
    'CM7b5':    [0, 19],
    'CΔ7b5':    [0, 19],
    'Cmaj7b5':  [0, 19],
    'Cmajor7b5':    [0, 19],
    'CM7-5':    [0, 19],
    'CΔ7-5':    [0, 19],
    'Cmaj7-5':  [0, 19],
    'Cmajor7-5':    [0, 19],

    # C minor-major seventh
    'Cminormajor7':  [ 0, 20 ], 
    'Cminormaj7':    [ 0, 20 ], 
    'CminorM7':      [ 0, 20 ], 
    'CminorΔ7':      [ 0, 20 ], 
    'Cmmajor7':      [ 0, 20 ], 
    'Cmmaj7':        [ 0, 20 ], 
    'CmM7':          [ 0, 20 ], 
    'CmΔ7':          [ 0, 20 ], 
    'C-major7':      [ 0, 20 ], 
    'C-maj7':        [ 0, 20 ], 
    'C-M7':          [ 0, 20 ], 
    'C-Δ7':          [ 0, 20 ], 
    'Cminmajor7':    [ 0, 20 ], 
    'Cminmaj7':      [ 0, 20 ], 
    'CminM7':        [ 0, 20 ], 
    'CminΔ7':        [ 0, 20 ], 

    # C minor seventh
    'Cm7':      [0, 21],
    'C-7':      [0, 21],
    'Cmin7':    [0, 21],

    # C augmented-major seventh
    'C+M7':     [0, 22],
    'Caugmaj7':     [0, 22],
    'Caug-maj7':    [0, 22],
    'CM7#5':     [0, 22],
    'CM7+5':     [0, 22],
    'CΔ7#5':     [0, 22],
    'CΔ7+5':     [0, 22],

    # C augmented seventh
    'C+7':      [0, 23],
    'Caug7':    [0, 23],
    'C7#5':     [0, 23],
    'C7+5':     [0, 23],

    # C half-diminished seventh
    'Cø':       [0, 24],
    'Cø7':      [0, 24],
    'Cmin7dim5':    [0, 24],
    'Cm7b5':    [0, 24],
    'Cm7o5':    [0, 24],
    'C-7b5':    [0, 24],
    'C-7o5':    [0, 24],

    # C diminished seventh
    'Co7':       [0, 25],
    'Cdim7':     [0, 25],

    # C diminished major seventh
    'CmM7b5':     [0, 26],
    'C-Δ7b5':     [0, 26],
    'CoM7':       [0, 26],
# --------------------------------
#   C# SEVENTHS
# --------------------------------
    # C# dominant seventh
    'C#7':       [1, 16],
    'C#dom7':    [1, 16],
    'C#dom':     [1, 16],
    'C#7dim5':   [1, 16],

    # C# dominant flat seventh
    'C#7b5':     [1, 17],
    'C#7-5':     [1, 17],
    'C#dom7b5':  [1, 17],
    'C#dom7-5':  [1, 17],

    # C# major seventh
    'C#M7':      [1, 18],
    'C#maj7':    [1, 18],
    'C#Δ7':      [1, 18],
    'C#major7':  [1, 18],

    # C# major seventh flat five
    'C#M7b5':    [1, 19],
    'C#Δ7b5':    [1, 19],
    'C#maj7b5':  [1, 19],
    'C#major7b5':    [1, 19],
    'C#M7-5':    [1, 19],
    'C#Δ7-5':    [1, 19],
    'C#maj7-5':  [1, 19],
    'C#major7-5':    [1, 19],

    # C# minor-major seventh
    'C#minormajor7':  [ 1, 20 ], 
    'C#minormaj7':    [ 1, 20 ], 
    'C#minorM7':      [ 1, 20 ], 
    'C#minorΔ7':      [ 1, 20 ], 
    'C#mmajor7':      [ 1, 20 ], 
    'C#mmaj7':        [ 1, 20 ], 
    'C#mM7':          [ 1, 20 ], 
    'C#mΔ7':          [ 1, 20 ], 
    'C#-major7':      [ 1, 20 ], 
    'C#-maj7':        [ 1, 20 ], 
    'C#-M7':          [ 1, 20 ], 
    'C#-Δ7':          [ 1, 20 ], 
    'C#minmajor7':    [ 1, 20 ], 
    'C#minmaj7':      [ 1, 20 ], 
    'C#minM7':        [ 1, 20 ], 
    'C#minΔ7':        [ 1, 20 ], 
    'C#minΔ7':        [ 1, 20 ], 

    # C# minor seventh
    'C#m7':      [1, 21],
    'C#-7':      [1, 21],
    'C#min7':    [1, 21],

    # C# augmented-major seventh
    'C#+M7':     [1, 22],
    'C#augmaj7':     [1, 22],
    'C#aug-maj7':    [1, 22],
    'C#M7#5':     [1, 22],
    'C#M7+5':     [1, 22],
    'C#Δ7#5':     [1, 22],
    'C#Δ7+5':     [1, 22],

    # C# augmented seventh
    'C#+7':      [1, 23],
    'C#aug7':    [1, 23],
    'C#7#5':     [1, 23],
    'C#7+5':     [1, 23],

    # C# half-diminished seventh
    'C#ø':       [1, 24],
    'C#ø7':      [1, 24],
    'C#min7dim5':    [1, 24],
    'C#m7b5':    [1, 24],
    'C#m7o5':    [1, 24],
    'C#-7b5':    [1, 24],
    'C#-7o5':    [1, 24],

    # C# diminished seventh
    'C#o7':       [1, 25],
    'C#dim7':     [1, 25],

    # C# diminished major seventh
    'C#mM7b5':     [1, 26],
    'C#-Δ7b5':     [1, 26],
    'C#oM7':       [1, 26],
# --------------------------------
#   Db SEVENTHS
# --------------------------------
    # Db dominant seventh
    'Db7':       [1, 16],
    'Dbdom7':    [1, 16],
    'Dbdom':     [1, 16],
    'Db7dim5':   [1, 16],

    # Db dominant flat seventh
    'Db7b5':     [1, 17],
    'Db7-5':     [1, 17],
    'Dbdom7b5':  [1, 17],
    'Dbdom7-5':  [1, 17],

    # Db major seventh
    'DbM7':      [1, 18],
    'Dbmaj7':    [1, 18],
    'DbΔ7':      [1, 18],
    'Dbmajor7':  [1, 18],

    # Db major seventh flat five
    'DbM7b5':    [1, 19],
    'DbΔ7b5':    [1, 19],
    'Dbmaj7b5':  [1, 19],
    'Dbmajor7b5':    [1, 19],
    'DbM7-5':    [1, 19],
    'DbΔ7-5':    [1, 19],
    'Dbmaj7-5':  [1, 19],
    'Dbmajor7-5':    [1, 19],

    # Db minor-major seventh
    'Dbminormajor7':  [ 1, 20 ], 
    'Dbminormaj7':    [ 1, 20 ], 
    'DbminorM7':      [ 1, 20 ], 
    'DbminorΔ7':      [ 1, 20 ], 
    'Dbmmajor7':      [ 1, 20 ], 
    'Dbmmaj7':        [ 1, 20 ], 
    'DbmM7':          [ 1, 20 ], 
    'DbmΔ7':          [ 1, 20 ], 
    'Db-major7':      [ 1, 20 ], 
    'Db-maj7':        [ 1, 20 ], 
    'Db-M7':          [ 1, 20 ], 
    'Db-Δ7':          [ 1, 20 ], 
    'Dbminmajor7':    [ 1, 20 ], 
    'Dbminmaj7':      [ 1, 20 ], 
    'DbminM7':        [ 1, 20 ], 
    'DbminΔ7':        [ 1, 20 ], 

    # Db minor seventh
    'Dbm7':      [1, 21],
    'Db-7':      [1, 21],
    'Dbmin7':    [1, 21],

    # Db augmented-major seventh
    'Db+M7':     [1, 22],
    'Dbaugmaj7':     [1, 22],
    'Dbaug-maj7':    [1, 22],
    'DbM7#5':     [1, 22],
    'DbM7+5':     [1, 22],
    'DbΔ7#5':     [1, 22],
    'DbΔ7+5':     [1, 22],

    # Db augmented seventh
    'Db+7':      [1, 23],
    'Dbaug7':    [1, 23],
    'Db7#5':     [1, 23],
    'Db7+5':     [1, 23],

    # Db half-diminished seventh
    'Dbø':       [1, 24],
    'Dbø7':      [1, 24],
    'Dbmin7dim5':    [1, 24],
    'Dbm7b5':    [1, 24],
    'Dbm7o5':    [1, 24],
    'Db-7b5':    [1, 24],
    'Db-7o5':    [1, 24],

    # Db diminished seventh
    'Dbo7':       [1, 25],
    'Dbdim7':     [1, 25],

    # Db diminished major seventh
    'DbmM7b5':     [1, 26],
    'Db-Δ7b5':     [1, 26],
    'DboM7':       [1, 26],
# --------------------------------
#   D SEVENTHS
# --------------------------------
    # D dominant seventh
    'D7':       [2, 16],
    'Ddom7':    [2, 16],
    'Ddom':     [2, 16],
    'D7dim5':   [2, 16],

    # D dominant flat seventh
    'D7b5':     [2, 17],
    'D7-5':     [2, 17],
    'Ddom7b5':  [2, 17],
    'Ddom7-5':  [2, 17],

    # D major seventh
    'DM7':      [2, 18],
    'Dmaj7':    [2, 18],
    'DΔ7':      [2, 18],
    'Dmajor7':  [2, 18],

    # D major seventh flat five
    'DM7b5':    [2, 19],
    'DΔ7b5':    [2, 19],
    'Dmaj7b5':  [2, 19],
    'Dmajor7b5':    [2, 19],
    'DM7-5':    [2, 19],
    'DΔ7-5':    [2, 19],
    'Dmaj7-5':  [2, 19],
    'Dmajor7-5':    [2, 19],

    # D minor-major seventh
    'Dminormajor7':  [ 2, 20 ], 
    'Dminormaj7':    [ 2, 20 ], 
    'DminorM7':      [ 2, 20 ], 
    'DminorΔ7':      [ 2, 20 ], 
    'Dmmajor7':      [ 2, 20 ], 
    'Dmmaj7':        [ 2, 20 ], 
    'DmM7':          [ 2, 20 ], 
    'DmΔ7':          [ 2, 20 ], 
    'D-major7':      [ 2, 20 ], 
    'D-maj7':        [ 2, 20 ], 
    'D-M7':          [ 2, 20 ], 
    'D-Δ7':          [ 2, 20 ], 
    'Dminmajor7':    [ 2, 20 ], 
    'Dminmaj7':      [ 2, 20 ], 
    'DminM7':        [ 2, 20 ], 
    'DminΔ7':        [ 2, 20 ], 

    # D minor seventh
    'Dm7':      [2, 21],
    'D-7':      [2, 21],
    'Dmin7':    [2, 21],

    # D augmented-major seventh
    'D+M7':     [2, 22],
    'Daugmaj7':     [2, 22],
    'Daug-maj7':    [2, 22],
    'DM7#5':     [2, 22],
    'DM7+5':     [2, 22],
    'DΔ7#5':     [2, 22],
    'DΔ7+5':     [2, 22],

    # D augmented seventh
    'D+7':      [2, 23],
    'Daug7':    [2, 23],
    'D7#5':     [2, 23],
    'D7+5':     [2, 23],

    # D half-diminished seventh
    'Dø':       [2, 24],
    'Dø7':      [2, 24],
    'Dmin7dim5':    [2, 24],
    'Dm7b5':    [2, 24],
    'Dm7o5':    [2, 24],
    'D-7b5':    [2, 24],
    'D-7o5':    [2, 24],

    # D diminished seventh
    'Do7':       [2, 25],
    'Ddim7':     [2, 25],

    # D diminished major seventh
    'DmM7b5':     [2, 26],
    'D-Δ7b5':     [2, 26],
    'DoM7':       [2, 26],
# --------------------------------
#   D# SEVENTHS
# --------------------------------
    # D# dominant seventh
    'D#7':       [3, 16],
    'D#dom7':    [3, 16],
    'D#dom':     [3, 16],
    'D#7dim5':   [3, 16],

    # D# dominant flat seventh
    'D#7b5':     [3, 17],
    'D#7-5':     [3, 17],
    'D#dom7b5':  [3, 17],
    'D#dom7-5':  [3, 17],

    # D# major seventh
    'D#M7':      [3, 18],
    'D#maj7':    [3, 18],
    'D#Δ7':      [3, 18],
    'D#major7':  [3, 18],

    # D# major seventh flat five
    'D#M7b5':    [3, 19],
    'D#Δ7b5':    [3, 19],
    'D#maj7b5':  [3, 19],
    'D#major7b5':    [3, 19],
    'D#M7-5':    [3, 19],
    'D#Δ7-5':    [3, 19],
    'D#maj7-5':  [3, 19],
    'D#major7-5':    [3, 19],

    # D# minor-major seventh
    'D#minormajor7':  [ 3, 20 ], 
    'D#minormaj7':    [ 3, 20 ], 
    'D#minorM7':      [ 3, 20 ], 
    'D#minorΔ7':      [ 3, 20 ], 
    'D#mmajor7':      [ 3, 20 ], 
    'D#mmaj7':        [ 3, 20 ], 
    'D#mM7':          [ 3, 20 ], 
    'D#mΔ7':          [ 3, 20 ], 
    'D#-major7':      [ 3, 20 ], 
    'D#-maj7':        [ 3, 20 ], 
    'D#-M7':          [ 3, 20 ], 
    'D#-Δ7':          [ 3, 20 ], 
    'D#minmajor7':    [ 3, 20 ], 
    'D#minmaj7':      [ 3, 20 ], 
    'D#minM7':        [ 3, 20 ], 
    'D#minΔ7':        [ 3, 20 ], 

    # D# minor seventh
    'D#m7':      [3, 21],
    'D#-7':      [3, 21],
    'D#min7':    [3, 21],

    # D# augmented-major seventh
    'D#+M7':     [3, 22],
    'D#augmaj7':     [3, 22],
    'D#aug-maj7':    [3, 22],
    'D#M7#5':     [3, 22],
    'D#M7+5':     [3, 22],
    'D#Δ7#5':     [3, 22],
    'D#Δ7+5':     [3, 22],

    # D# augmented seventh
    'D#+7':      [3, 23],
    'D#aug7':    [3, 23],
    'D#7#5':     [3, 23],
    'D#7+5':     [3, 23],

    # D# half-diminished seventh
    'D#ø':       [3, 24],
    'D#ø7':      [3, 24],
    'D#min7dim5':    [3, 24],
    'D#m7b5':    [3, 24],
    'D#m7o5':    [3, 24],
    'D#-7b5':    [3, 24],
    'D#-7o5':    [3, 24],

    # D# diminished seventh
    'D#o7':       [3, 25],
    'D#dim7':     [3, 25],

    # D# diminished major seventh
    'D#mM7b5':     [3, 26],
    'D#-Δ7b5':     [3, 26],
    'D#oM7':       [3, 26],
# --------------------------------
#   Eb SEVENTHS
# --------------------------------
    # Eb dominant seventh
    'Eb7':       [3, 16],
    'Ebdom7':    [3, 16],
    'Ebdom':     [3, 16],
    'Eb7dim5':   [3, 16],

    # Eb dominant flat seventh
    'Eb7b5':     [3, 17],
    'Eb7-5':     [3, 17],
    'Ebdom7b5':  [3, 17],
    'Ebdom7-5':  [3, 17],

    # Eb major seventh
    'EbM7':      [3, 18],
    'Ebmaj7':    [3, 18],
    'EbΔ7':      [3, 18],
    'Ebmajor7':  [3, 18],

    # Eb major seventh flat five
    'EbM7b5':    [3, 19],
    'EbΔ7b5':    [3, 19],
    'Ebmaj7b5':  [3, 19],
    'Ebmajor7b5':    [3, 19],
    'EbM7-5':    [3, 19],
    'EbΔ7-5':    [3, 19],
    'Ebmaj7-5':  [3, 19],
    'Ebmajor7-5':    [3, 19],

    # Eb minor-major seventh
    'Ebminormajor7':  [ 3, 20 ], 
    'Ebminormaj7':    [ 3, 20 ], 
    'EbminorM7':      [ 3, 20 ], 
    'EbminorΔ7':      [ 3, 20 ], 
    'Ebmmajor7':      [ 3, 20 ], 
    'Ebmmaj7':        [ 3, 20 ], 
    'EbmM7':          [ 3, 20 ], 
    'EbmΔ7':          [ 3, 20 ], 
    'Eb-major7':      [ 3, 20 ], 
    'Eb-maj7':        [ 3, 20 ], 
    'Eb-M7':          [ 3, 20 ], 
    'Eb-Δ7':          [ 3, 20 ], 
    'Ebminmajor7':    [ 3, 20 ], 
    'Ebminmaj7':      [ 3, 20 ], 
    'EbminM7':        [ 3, 20 ], 
    'EbminΔ7':        [ 3, 20 ], 

    # Eb minor seventh
    'Ebm7':      [3, 21],
    'Eb-7':      [3, 21],
    'Ebmin7':    [3, 21],

    # Eb augmented-major seventh
    'Eb+M7':     [3, 22],
    'Ebaugmaj7':     [3, 22],
    'Ebaug-maj7':    [3, 22],
    'EbM7#5':     [3, 22],
    'EbM7+5':     [3, 22],
    'EbΔ7#5':     [3, 22],
    'EbΔ7+5':     [3, 22],

    # Eb augmented seventh
    'Eb+7':      [3, 23],
    'Ebaug7':    [3, 23],
    'Eb7#5':     [3, 23],
    'Eb7+5':     [3, 23],

    # Eb half-diminished seventh
    'Ebø':       [3, 24],
    'Ebø7':      [3, 24],
    'Ebmin7dim5':    [3, 24],
    'Ebm7b5':    [3, 24],
    'Ebm7o5':    [3, 24],
    'Eb-7b5':    [3, 24],
    'Eb-7o5':    [3, 24],

    # Eb diminished seventh
    'Ebo7':       [3, 25],
    'Ebdim7':     [3, 25],

    # Eb diminished major seventh
    'EbmM7b5':     [3, 26],
    'Eb-Δ7b5':     [3, 26],
    'EboM7':       [3, 26],
# --------------------------------
#   E SEVENTHS
# --------------------------------
    # E dominant seventh
    'E7':       [4, 16],
    'Edom7':    [4, 16],
    'Edom':     [4, 16],
    'E7dim5':   [4, 16],

    # E dominant flat seventh
    'E7b5':     [4, 17],
    'E7-5':     [4, 17],
    'Edom7b5':  [4, 17],
    'Edom7-5':  [4, 17],

    # E major seventh
    'EM7':      [4, 18],
    'Emaj7':    [4, 18],
    'EΔ7':      [4, 18],
    'Emajor7':  [4, 18],

    # E major seventh flat five
    'EM7b5':    [4, 19],
    'EΔ7b5':    [4, 19],
    'Emaj7b5':  [4, 19],
    'Emajor7b5':    [4, 19],
    'EM7-5':    [4, 19],
    'EΔ7-5':    [4, 19],
    'Emaj7-5':  [4, 19],
    'Emajor7-5':    [4, 19],

    # E minor-major seventh
    'Eminormajor7':  [ 4, 20 ], 
    'Eminormaj7':    [ 4, 20 ], 
    'EminorM7':      [ 4, 20 ], 
    'EminorΔ7':      [ 4, 20 ], 
    'Emmajor7':      [ 4, 20 ], 
    'Emmaj7':        [ 4, 20 ], 
    'EmM7':          [ 4, 20 ], 
    'EmΔ7':          [ 4, 20 ], 
    'E-major7':      [ 4, 20 ], 
    'E-maj7':        [ 4, 20 ], 
    'E-M7':          [ 4, 20 ], 
    'E-Δ7':          [ 4, 20 ], 
    'Eminmajor7':    [ 4, 20 ], 
    'Eminmaj7':      [ 4, 20 ], 
    'EminM7':        [ 4, 20 ], 
    'EminΔ7':        [ 4, 20 ], 

    # E minor seventh
    'Em7':      [4, 21],
    'E-7':      [4, 21],
    'Emin7':    [4, 21],

    # E augmented-major seventh
    'E+M7':     [4, 22],
    'Eaugmaj7':     [4, 22],
    'Eaug-maj7':    [4, 22],
    'EM7#5':     [4, 22],
    'EM7+5':     [4, 22],
    'EΔ7#5':     [4, 22],
    'EΔ7+5':     [4, 22],

    # E augmented seventh
    'E+7':      [4, 23],
    'Eaug7':    [4, 23],
    'E7#5':     [4, 23],
    'E7+5':     [4, 23],

    # E half-diminished seventh
    'Eø':       [4, 24],
    'Eø7':      [4, 24],
    'Emin7dim5':    [4, 24],
    'Em7b5':    [4, 24],
    'Em7o5':    [4, 24],
    'E-7b5':    [4, 24],
    'E-7o5':    [4, 24],

    # E diminished seventh
    'Eo7':       [4, 25],
    'Edim7':     [4, 25],

    # E diminished major seventh
    'EmM7b5':     [4, 26],
    'E-Δ7b5':     [4, 26],
    'EoM7':       [4, 26],
# --------------------------------
#   F SEVENTHS
# --------------------------------
    # F dominant seventh
    'F7':       [5, 16],
    'Fdom7':    [5, 16],
    'Fdom':     [5, 16],
    'F7dim5':   [5, 16],

    # F dominant flat seventh
    'F7b5':     [5, 17],
    'F7-5':     [5, 17],
    'Fdom7b5':  [5, 17],
    'Fdom7-5':  [5, 17],

    # F major seventh
    'FM7':      [5, 18],
    'Fmaj7':    [5, 18],
    'FΔ7':      [5, 18],
    'Fmajor7':  [5, 18],

    # F major seventh flat five
    'FM7b5':    [5, 19],
    'FΔ7b5':    [5, 19],
    'Fmaj7b5':  [5, 19],
    'Fmajor7b5':    [5, 19],
    'FM7-5':    [5, 19],
    'FΔ7-5':    [5, 19],
    'Fmaj7-5':  [5, 19],
    'Fmajor7-5':    [5, 19],

    # F minor-major seventh
    'Fminormajor7':  [ 5, 20 ], 
    'Fminormaj7':    [ 5, 20 ], 
    'FminorM7':      [ 5, 20 ], 
    'FminorΔ7':      [ 5, 20 ], 
    'Fmmajor7':      [ 5, 20 ], 
    'Fmmaj7':        [ 5, 20 ], 
    'FmM7':          [ 5, 20 ], 
    'FmΔ7':          [ 5, 20 ], 
    'F-major7':      [ 5, 20 ], 
    'F-maj7':        [ 5, 20 ], 
    'F-M7':          [ 5, 20 ], 
    'F-Δ7':          [ 5, 20 ], 
    'Fminmajor7':    [ 5, 20 ], 
    'Fminmaj7':      [ 5, 20 ], 
    'FminM7':        [ 5, 20 ], 
    'FminΔ7':        [ 5, 20 ], 

    # F minor seventh
    'Fm7':      [5, 21],
    'F-7':      [5, 21],
    'Fmin7':    [5, 21],

    # F augmented-major seventh
    'F+M7':     [5, 22],
    'Faugmaj7':     [5, 22],
    'Faug-maj7':    [5, 22],
    'FM7#5':     [5, 22],
    'FM7+5':     [5, 22],
    'FΔ7#5':     [5, 22],
    'FΔ7+5':     [5, 22],

    # F augmented seventh
    'F+7':      [5, 23],
    'Faug7':    [5, 23],
    'F7#5':     [5, 23],
    'F7+5':     [5, 23],

    # F half-diminished seventh
    'Fø':       [5, 24],
    'Fø7':      [5, 24],
    'Fmin7dim5':    [5, 24],
    'Fm7b5':    [5, 24],
    'Fm7o5':    [5, 24],
    'F-7b5':    [5, 24],
    'F-7o5':    [5, 24],

    # F diminished seventh
    'Fo7':       [5, 25],
    'Fdim7':     [5, 25],

    # F diminished major seventh
    'FmM7b5':     [5, 26],
    'F-Δ7b5':     [5, 26],
    'FoM7':       [5, 26],
# --------------------------------
#   F# SEVENTHS
# --------------------------------
    # F# dominant seventh
    'F#7':       [6, 16],
    'F#dom7':    [6, 16],
    'F#dom':     [6, 16],
    'F#7dim5':   [6, 16],

    # F# dominant flat seventh
    'F#7b5':     [6, 17],
    'F#7-5':     [6, 17],
    'F#dom7b5':  [6, 17],
    'F#dom7-5':  [6, 17],

    # F# major seventh
    'F#M7':      [6, 18],
    'F#maj7':    [6, 18],
    'F#Δ7':      [6, 18],
    'F#major7':  [6, 18],

    # F# major seventh flat five
    'F#M7b5':    [6, 19],
    'F#Δ7b5':    [6, 19],
    'F#maj7b5':  [6, 19],
    'F#major7b5':    [6, 19],
    'F#M7-5':    [6, 19],
    'F#Δ7-5':    [6, 19],
    'F#maj7-5':  [6, 19],
    'F#major7-5':    [6, 19],

    # F# minor-major seventh
    'F#minormajor7':  [ 6, 20 ], 
    'F#minormaj7':    [ 6, 20 ], 
    'F#minorM7':      [ 6, 20 ], 
    'F#minorΔ7':      [ 6, 20 ], 
    'F#mmajor7':      [ 6, 20 ], 
    'F#mmaj7':        [ 6, 20 ], 
    'F#mM7':          [ 6, 20 ], 
    'F#mΔ7':          [ 6, 20 ], 
    'F#-major7':      [ 6, 20 ], 
    'F#-maj7':        [ 6, 20 ], 
    'F#-M7':          [ 6, 20 ], 
    'F#-Δ7':          [ 6, 20 ], 
    'F#minmajor7':    [ 6, 20 ], 
    'F#minmaj7':      [ 6, 20 ], 
    'F#minM7':        [ 6, 20 ], 
    'F#minΔ7':        [ 6, 20 ], 

    # F# minor seventh
    'F#m7':      [6, 21],
    'F#-7':      [6, 21],
    'F#min7':    [6, 21],

    # F# augmented-major seventh
    'F#+M7':     [6, 22],
    'F#augmaj7':     [6, 22],
    'F#aug-maj7':    [6, 22],
    'F#M7#5':     [6, 22],
    'F#M7+5':     [6, 22],
    'F#Δ7#5':     [6, 22],
    'F#Δ7+5':     [6, 22],

    # F# augmented seventh
    'F#+7':      [6, 23],
    'F#aug7':    [6, 23],
    'F#7#5':     [6, 23],
    'F#7+5':     [6, 23],

    # F# half-diminished seventh
    'F#ø':       [6, 24],
    'F#ø7':      [6, 24],
    'F#min7dim5':    [6, 24],
    'F#m7b5':    [6, 24],
    'F#m7o5':    [6, 24],
    'F#-7b5':    [6, 24],
    'F#-7o5':    [6, 24],

    # F# diminished seventh
    'F#o7':       [6, 25],
    'F#dim7':     [6, 25],

    # F# diminished major seventh
    'F#mM7b5':     [6, 26],
    'F#-Δ7b5':     [6, 26],
    'F#oM7':       [6, 26],
# --------------------------------
#   Gb SEVENTHS
# --------------------------------
    # Gb dominant seventh
    'Gb7':       [6, 16],
    'Gbdom7':    [6, 16],
    'Gbdom':     [6, 16],
    'Gb7dim5':   [6, 16],

    # Gb dominant flat seventh
    'Gb7b5':     [6, 17],
    'Gb7-5':     [6, 17],
    'Gbdom7b5':  [6, 17],
    'Gbdom7-5':  [6, 17],

    # Gb major seventh
    'GbM7':      [6, 18],
    'Gbmaj7':    [6, 18],
    'GbΔ7':      [6, 18],
    'Gbmajor7':  [6, 18],

    # Gb major seventh flat five
    'GbM7b5':    [6, 19],
    'GbΔ7b5':    [6, 19],
    'Gbmaj7b5':  [6, 19],
    'Gbmajor7b5':    [6, 19],
    'GbM7-5':    [6, 19],
    'GbΔ7-5':    [6, 19],
    'Gbmaj7-5':  [6, 19],
    'Gbmajor7-5':    [6, 19],

    # Gb minor-major seventh
    'Gbminormajor7':  [ 6, 20 ], 
    'Gbminormaj7':    [ 6, 20 ], 
    'GbminorM7':      [ 6, 20 ], 
    'GbminorΔ7':      [ 6, 20 ], 
    'Gbmmajor7':      [ 6, 20 ], 
    'Gbmmaj7':        [ 6, 20 ], 
    'GbmM7':          [ 6, 20 ], 
    'GbmΔ7':          [ 6, 20 ], 
    'Gb-major7':      [ 6, 20 ], 
    'Gb-maj7':        [ 6, 20 ], 
    'Gb-M7':          [ 6, 20 ], 
    'Gb-Δ7':          [ 6, 20 ], 
    'Gbminmajor7':    [ 6, 20 ], 
    'Gbminmaj7':      [ 6, 20 ], 
    'GbminM7':        [ 6, 20 ], 
    'GbminΔ7':        [ 6, 20 ], 

    # Gb minor seventh
    'Gbm7':      [6, 21],
    'Gb-7':      [6, 21],
    'Gbmin7':    [6, 21],

    # Gb augmented-major seventh
    'Gb+M7':     [6, 22],
    'Gbaugmaj7':     [6, 22],
    'Gbaug-maj7':    [6, 22],
    'GbM7#5':     [6, 22],
    'GbM7+5':     [6, 22],
    'GbΔ7#5':     [6, 22],
    'GbΔ7+5':     [6, 22],

    # Gb augmented seventh
    'Gb+7':      [6, 23],
    'Gbaug7':    [6, 23],
    'Gb7#5':     [6, 23],
    'Gb7+5':     [6, 23],

    # Gb half-diminished seventh
    'Gbø':       [6, 24],
    'Gbø7':      [6, 24],
    'Gbmin7dim5':    [6, 24],
    'Gbm7b5':    [6, 24],
    'Gbm7o5':    [6, 24],
    'Gb-7b5':    [6, 24],
    'Gb-7o5':    [6, 24],

    # Gb diminished seventh
    'Gbo7':       [6, 25],
    'Gbdim7':     [6, 25],

    # Gb diminished major seventh
    'GbmM7b5':     [6, 26],
    'Gb-Δ7b5':     [6, 26],
    'GboM7':       [6, 26],
# --------------------------------
#   G SEVENTHS
# --------------------------------
    # G dominant seventh
    'G7':       [7, 16],
    'Gdom7':    [7, 16],
    'Gdom':     [7, 16],
    'G7dim5':   [7, 16],

    # G dominant flat seventh
    'G7b5':     [7, 17],
    'G7-5':     [7, 17],
    'Gdom7b5':  [7, 17],
    'Gdom7-5':  [7, 17],

    # G major seventh
    'GM7':      [7, 18],
    'Gmaj7':    [7, 18],
    'GΔ7':      [7, 18],
    'Gmajor7':  [7, 18],

    # G major seventh flat five
    'GM7b5':    [7, 19],
    'GΔ7b5':    [7, 19],
    'Gmaj7b5':  [7, 19],
    'Gmajor7b5':    [7, 19],
    'GM7-5':    [7, 19],
    'GΔ7-5':    [7, 19],
    'Gmaj7-5':  [7, 19],
    'Gmajor7-5':    [7, 19],

    # G minor-major seventh
    'Gminormajor7':  [ 7, 20 ], 
    'Gminormaj7':    [ 7, 20 ], 
    'GminorM7':      [ 7, 20 ], 
    'GminorΔ7':      [ 7, 20 ], 
    'Gmmajor7':      [ 7, 20 ], 
    'Gmmaj7':        [ 7, 20 ], 
    'GmM7':          [ 7, 20 ], 
    'GmΔ7':          [ 7, 20 ], 
    'G-major7':      [ 7, 20 ], 
    'G-maj7':        [ 7, 20 ], 
    'G-M7':          [ 7, 20 ], 
    'G-Δ7':          [ 7, 20 ], 
    'Gminmajor7':    [ 7, 20 ], 
    'Gminmaj7':      [ 7, 20 ], 
    'GminM7':        [ 7, 20 ], 
    'GminΔ7':        [ 7, 20 ], 

    # G minor seventh
    'Gm7':      [7, 21],
    'G-7':      [7, 21],
    'Gmin7':    [7, 21],

    # G augmented-major seventh
    'G+M7':     [7, 22],
    'Gaugmaj7':     [7, 22],
    'Gaug-maj7':    [7, 22],
    'GM7#5':     [7, 22],
    'GM7+5':     [7, 22],
    'GΔ7#5':     [7, 22],
    'GΔ7+5':     [7, 22],

    # G augmented seventh
    'G+7':      [7, 23],
    'Gaug7':    [7, 23],
    'G7#5':     [7, 23],
    'G7+5':     [7, 23],

    # G half-diminished seventh
    'Gø':       [7, 24],
    'Gø7':      [7, 24],
    'Gmin7dim5':    [7, 24],
    'Gm7b5':    [7, 24],
    'Gm7o5':    [7, 24],
    'G-7b5':    [7, 24],
    'G-7o5':    [7, 24],

    # G diminished seventh
    'Go7':       [7, 25],
    'Gdim7':     [7, 25],

    # G diminished major seventh
    'GmM7b5':     [7, 26],
    'G-Δ7b5':     [7, 26],
    'GoM7':       [7, 26],
# --------------------------------
#   G# SEVENTHS
# --------------------------------
    # G# dominant seventh
    'G#7':       [8, 16],
    'G#dom7':    [8, 16],
    'G#dom':     [8, 16],
    'G#7dim5':   [8, 16],

    # G# dominant flat seventh
    'G#7b5':     [8, 17],
    'G#7-5':     [8, 17],
    'G#dom7b5':  [8, 17],
    'G#dom7-5':  [8, 17],

    # G# major seventh
    'G#M7':      [8, 18],
    'G#maj7':    [8, 18],
    'G#Δ7':      [8, 18],
    'G#major7':  [8, 18],

    # G# major seventh flat five
    'G#M7b5':    [8, 19],
    'G#Δ7b5':    [8, 19],
    'G#maj7b5':  [8, 19],
    'G#major7b5':    [8, 19],
    'G#M7-5':    [8, 19],
    'G#Δ7-5':    [8, 19],
    'G#maj7-5':  [8, 19],
    'G#major7-5':    [8, 19],

    # G# minor-major seventh
    'G#minormajor7':  [ 8, 20 ], 
    'G#minormaj7':    [ 8, 20 ], 
    'G#minorM7':      [ 8, 20 ], 
    'G#minorΔ7':      [ 8, 20 ], 
    'G#mmajor7':      [ 8, 20 ], 
    'G#mmaj7':        [ 8, 20 ], 
    'G#mM7':          [ 8, 20 ], 
    'G#mΔ7':          [ 8, 20 ], 
    'G#-major7':      [ 8, 20 ], 
    'G#-maj7':        [ 8, 20 ], 
    'G#-M7':          [ 8, 20 ], 
    'G#-Δ7':          [ 8, 20 ], 
    'G#minmajor7':    [ 8, 20 ], 
    'G#minmaj7':      [ 8, 20 ], 
    'G#minM7':        [ 8, 20 ], 
    'G#minΔ7':        [ 8, 20 ], 

    # G# minor seventh
    'G#m7':      [8, 21],
    'G#-7':      [8, 21],
    'G#min7':    [8, 21],

    # G# augmented-major seventh
    'G#+M7':     [8, 22],
    'G#augmaj7':     [8, 22],
    'G#aug-maj7':    [8, 22],
    'G#M7#5':     [8, 22],
    'G#M7+5':     [8, 22],
    'G#Δ7#5':     [8, 22],
    'G#Δ7+5':     [8, 22],

    # G# augmented seventh
    'G#+7':      [8, 23],
    'G#aug7':    [8, 23],
    'G#7#5':     [8, 23],
    'G#7+5':     [8, 23],

    # G# half-diminished seventh
    'G#ø':       [8, 24],
    'G#ø7':      [8, 24],
    'G#min7dim5':    [8, 24],
    'G#m7b5':    [8, 24],
    'G#m7o5':    [8, 24],
    'G#-7b5':    [8, 24],
    'G#-7o5':    [8, 24],

    # G# diminished seventh
    'G#o7':       [8, 25],
    'G#dim7':     [8, 25],

    # G# diminished major seventh
    'G#mM7b5':     [8, 26],
    'G#-Δ7b5':     [8, 26],
    'G#oM7':       [8, 26],
# --------------------------------
#   Ab SEVENTHS
# --------------------------------
    # Ab dominant seventh
    'Ab7':       [8, 16],
    'Abdom7':    [8, 16],
    'Abdom':     [8, 16],
    'Ab7dim5':   [8, 16],

    # Ab dominant flat seventh
    'Ab7b5':     [8, 17],
    'Ab7-5':     [8, 17],
    'Abdom7b5':  [8, 17],
    'Abdom7-5':  [8, 17],

    # Ab major seventh
    'AbM7':      [8, 18],
    'Abmaj7':    [8, 18],
    'AbΔ7':      [8, 18],
    'Abmajor7':  [8, 18],

    # Ab major seventh flat five
    'AbM7b5':    [8, 19],
    'AbΔ7b5':    [8, 19],
    'Abmaj7b5':  [8, 19],
    'Abmajor7b5':    [8, 19],
    'AbM7-5':    [8, 19],
    'AbΔ7-5':    [8, 19],
    'Abmaj7-5':  [8, 19],
    'Abmajor7-5':    [8, 19],

    # Ab minor-major seventh
    'Abminormajor7':  [ 8, 20 ], 
    'Abminormaj7':    [ 8, 20 ], 
    'AbminorM7':      [ 8, 20 ], 
    'AbminorΔ7':      [ 8, 20 ], 
    'Abmmajor7':      [ 8, 20 ], 
    'Abmmaj7':        [ 8, 20 ], 
    'AbmM7':          [ 8, 20 ], 
    'AbmΔ7':          [ 8, 20 ], 
    'Ab-major7':      [ 8, 20 ], 
    'Ab-maj7':        [ 8, 20 ], 
    'Ab-M7':          [ 8, 20 ], 
    'Ab-Δ7':          [ 8, 20 ], 
    'Abminmajor7':    [ 8, 20 ], 
    'Abminmaj7':      [ 8, 20 ], 
    'AbminM7':        [ 8, 20 ], 
    'AbminΔ7':        [ 8, 20 ], 

    # Ab minor seventh
    'Abm7':      [8, 21],
    'Ab-7':      [8, 21],
    'Abmin7':    [8, 21],

    # Ab augmented-major seventh
    'Ab+M7':     [8, 22],
    'Abaugmaj7':     [8, 22],
    'Abaug-maj7':    [8, 22],
    'AbM7#5':     [8, 22],
    'AbM7+5':     [8, 22],
    'AbΔ7#5':     [8, 22],
    'AbΔ7+5':     [8, 22],

    # Ab augmented seventh
    'Ab+7':      [8, 23],
    'Abaug7':    [8, 23],
    'Ab7#5':     [8, 23],
    'Ab7+5':     [8, 23],

    # Ab half-diminished seventh
    'Abø':       [8, 24],
    'Abø7':      [8, 24],
    'Abmin7dim5':    [8, 24],
    'Abm7b5':    [8, 24],
    'Abm7o5':    [8, 24],
    'Ab-7b5':    [8, 24],
    'Ab-7o5':    [8, 24],

    # Ab diminished seventh
    'Abo7':       [8, 25],
    'Abdim7':     [8, 25],

    # Ab diminished major seventh
    'AbmM7b5':     [8, 26],
    'Ab-Δ7b5':     [8, 26],
    'AboM7':       [8, 26],
# --------------------------------
#   A SEVENTHS
# --------------------------------
    # A dominant seventh
    'A7':       [9, 16],
    'Adom7':    [9, 16],
    'Adom':     [9, 16],
    'A7dim5':   [9, 16],

    # A dominant flat seventh
    'A7b5':     [9, 17],
    'A7-5':     [9, 17],
    'Adom7b5':  [9, 17],
    'Adom7-5':  [9, 17],

    # A major seventh
    'AM7':      [9, 18],
    'Amaj7':    [9, 18],
    'AΔ7':      [9, 18],
    'Amajor7':  [9, 18],

    # A major seventh flat five
    'AM7b5':    [9, 19],
    'AΔ7b5':    [9, 19],
    'Amaj7b5':  [9, 19],
    'Amajor7b5':    [9, 19],
    'AM7-5':    [9, 19],
    'AΔ7-5':    [9, 19],
    'Amaj7-5':  [9, 19],
    'Amajor7-5':    [9, 19],

    # A minor-major seventh
    'Aminormajor7':  [ 9, 20 ], 
    'Aminormaj7':    [ 9, 20 ], 
    'AminorM7':      [ 9, 20 ], 
    'AminorΔ7':      [ 9, 20 ], 
    'Ammajor7':      [ 9, 20 ], 
    'Ammaj7':        [ 9, 20 ], 
    'AmM7':          [ 9, 20 ], 
    'AmΔ7':          [ 9, 20 ], 
    'A-major7':      [ 9, 20 ], 
    'A-maj7':        [ 9, 20 ], 
    'A-M7':          [ 9, 20 ], 
    'A-Δ7':          [ 9, 20 ], 
    'Aminmajor7':    [ 9, 20 ], 
    'Aminmaj7':      [ 9, 20 ], 
    'AminM7':        [ 9, 20 ], 
    'AminΔ7':        [ 9, 20 ], 

    # A minor seventh
    'Am7':      [9, 21],
    'A-7':      [9, 21],
    'Amin7':    [9, 21],

    # A augmented-major seventh
    'A+M7':     [9, 22],
    'Aaugmaj7':     [9, 22],
    'Aaug-maj7':    [9, 22],
    'AM7#5':     [9, 22],
    'AM7+5':     [9, 22],
    'AΔ7#5':     [9, 22],
    'AΔ7+5':     [9, 22],

    # A augmented seventh
    'A+7':      [9, 23],
    'Aaug7':    [9, 23],
    'A7#5':     [9, 23],
    'A7+5':     [9, 23],

    # A half-diminished seventh
    'Aø':       [9, 24],
    'Aø7':      [9, 24],
    'Amin7dim5':    [9, 24],
    'Am7b5':    [9, 24],
    'Am7o5':    [9, 24],
    'A-7b5':    [9, 24],
    'A-7o5':    [9, 24],

    # A diminished seventh
    'Ao7':       [9, 25],
    'Adim7':     [9, 25],

    # A diminished major seventh
    'AmM7b5':     [9, 26],
    'A-Δ7b5':     [9, 26],
    'AoM7':       [9, 26],
# --------------------------------
#   A# SEVENTHS
# --------------------------------
    # A# dominant seventh
    'A#7':       [10, 16],
    'A#dom7':    [10, 16],
    'A#dom':     [10, 16],
    'A#7dim5':   [10, 16],

    # A# dominant flat seventh
    'A#7b5':     [10, 17],
    'A#7-5':     [10, 17],
    'A#dom7b5':  [10, 17],
    'A#dom7-5':  [10, 17],

    # A# major seventh
    'A#M7':      [10, 18],
    'A#maj7':    [10, 18],
    'A#Δ7':      [10, 18],
    'A#major7':  [10, 18],

    # A# major seventh flat five
    'A#M7b5':    [10, 19],
    'A#Δ7b5':    [10, 19],
    'A#maj7b5':  [10, 19],
    'A#major7b5':    [10, 19],
    'A#M7-5':    [10, 19],
    'A#Δ7-5':    [10, 19],
    'A#maj7-5':  [10, 19],
    'A#major7-5':    [10, 19],

    # A# minor-major seventh
    'A#minormajor7':  [ 10, 20 ], 
    'A#minormaj7':    [ 10, 20 ], 
    'A#minorM7':      [ 10, 20 ], 
    'A#minorΔ7':      [ 10, 20 ], 
    'A#mmajor7':      [ 10, 20 ], 
    'A#mmaj7':        [ 10, 20 ], 
    'A#mM7':          [ 10, 20 ], 
    'A#mΔ7':          [ 10, 20 ], 
    'A#-major7':      [ 10, 20 ], 
    'A#-maj7':        [ 10, 20 ], 
    'A#-M7':          [ 10, 20 ], 
    'A#-Δ7':          [ 10, 20 ], 
    'A#minmajor7':    [ 10, 20 ], 
    'A#minmaj7':      [ 10, 20 ], 
    'A#minM7':        [ 10, 20 ], 
    'A#minΔ7':        [ 10, 20 ], 

    # A# minor seventh
    'A#m7':      [10, 21],
    'A#-7':      [10, 21],
    'A#min7':    [10, 21],

    # A# augmented-major seventh
    'A#+M7':     [10, 22],
    'A#augmaj7':     [10, 22],
    'A#aug-maj7':    [10, 22],
    'A#M7#5':     [10, 22],
    'A#M7+5':     [10, 22],
    'A#Δ7#5':     [10, 22],
    'A#Δ7+5':     [10, 22],

    # A# augmented seventh
    'A#+7':      [10, 23],
    'A#aug7':    [10, 23],
    'A#7#5':     [10, 23],
    'A#7+5':     [10, 23],

    # A# half-diminished seventh
    'A#ø':       [10, 24],
    'A#ø7':      [10, 24],
    'A#min7dim5':    [10, 24],
    'A#m7b5':    [10, 24],
    'A#m7o5':    [10, 24],
    'A#-7b5':    [10, 24],
    'A#-7o5':    [10, 24],

    # A# diminished seventh
    'A#o7':       [10, 25],
    'A#dim7':     [10, 25],

    # A# diminished major seventh
    'A#mM7b5':     [10, 26],
    'A#-Δ7b5':     [10, 26],
    'A#oM7':       [10, 26],
# --------------------------------
#   Bb SEVENTHS
# --------------------------------
    # Bb dominant seventh
    'Bb7':       [10, 16],
    'Bbdom7':    [10, 16],
    'Bbdom':     [10, 16],
    'Bb7dim5':   [10, 16],

    # Bb dominant flat seventh
    'Bb7b5':     [10, 17],
    'Bb7-5':     [10, 17],
    'Bbdom7b5':  [10, 17],
    'Bbdom7-5':  [10, 17],

    # Bb major seventh
    'BbM7':      [10, 18],
    'Bbmaj7':    [10, 18],
    'BbΔ7':      [10, 18],
    'Bbmajor7':  [10, 18],

    # Bb major seventh flat five
    'BbM7b5':    [10, 19],
    'BbΔ7b5':    [10, 19],
    'Bbmaj7b5':  [10, 19],
    'Bbmajor7b5':    [10, 19],
    'BbM7-5':    [10, 19],
    'BbΔ7-5':    [10, 19],
    'Bbmaj7-5':  [10, 19],
    'Bbmajor7-5':    [10, 19],

    # Bb minor-major seventh
    'Bbminormajor7':  [ 10, 20 ], 
    'Bbminormaj7':    [ 10, 20 ], 
    'BbminorM7':      [ 10, 20 ], 
    'BbminorΔ7':      [ 10, 20 ], 
    'Bbmmajor7':      [ 10, 20 ], 
    'Bbmmaj7':        [ 10, 20 ], 
    'BbmM7':          [ 10, 20 ], 
    'BbmΔ7':          [ 10, 20 ], 
    'Bb-major7':      [ 10, 20 ], 
    'Bb-maj7':        [ 10, 20 ], 
    'Bb-M7':          [ 10, 20 ], 
    'Bb-Δ7':          [ 10, 20 ], 
    'Bbminmajor7':    [ 10, 20 ], 
    'Bbminmaj7':      [ 10, 20 ], 
    'BbminM7':        [ 10, 20 ], 
    'BbminΔ7':        [ 10, 20 ], 

    # Bb minor seventh
    'Bbm7':      [10, 21],
    'Bb-7':      [10, 21],
    'Bbmin7':    [10, 21],

    # Bb augmented-major seventh
    'Bb+M7':     [10, 22],
    'Bbaugmaj7':     [10, 22],
    'Bbaug-maj7':    [10, 22],
    'BbM7#5':     [10, 22],
    'BbM7+5':     [10, 22],
    'BbΔ7#5':     [10, 22],
    'BbΔ7+5':     [10, 22],

    # Bb augmented seventh
    'Bb+7':      [10, 23],
    'Bbaug7':    [10, 23],
    'Bb7#5':     [10, 23],
    'Bb7+5':     [10, 23],

    # Bb half-diminished seventh
    'Bbø':       [10, 24],
    'Bbø7':      [10, 24],
    'Bbmin7dim5':    [10, 24],
    'Bbm7b5':    [10, 24],
    'Bbm7o5':    [10, 24],
    'Bb-7b5':    [10, 24],
    'Bb-7o5':    [10, 24],

    # Bb diminished seventh
    'Bbo7':       [10, 25],
    'Bbdim7':     [10, 25],

    # Bb diminished major seventh
    'BbmM7b5':     [10, 26],
    'Bb-Δ7b5':     [10, 26],
    'BboM7':       [10, 26],
# --------------------------------
#   B SEVENTHS
# --------------------------------
    # B dominant seventh
    'B7':       [11, 16],
    'Bdom7':    [11, 16],
    'Bdom':     [11, 16],
    'B7dim5':   [11, 16],

    # B dominant flat seventh
    'B7b5':     [11, 17],
    'B7-5':     [11, 17],
    'Bdom7b5':  [11, 17],
    'Bdom7-5':  [11, 17],

    # B major seventh
    'BM7':      [11, 18],
    'Bmaj7':    [11, 18],
    'BΔ7':      [11, 18],
    'Bmajor7':  [11, 18],

    # B major seventh flat five
    'BM7b5':    [11, 19],
    'BΔ7b5':    [11, 19],
    'Bmaj7b5':  [11, 19],
    'Bmajor7b5':    [11, 19],
    'BM7-5':    [11, 19],
    'BΔ7-5':    [11, 19],
    'Bmaj7-5':  [11, 19],
    'Bmajor7-5':    [11, 19],

    # B minor-major seventh
    'Bminormajor7':  [ 11, 20 ], 
    'Bminormaj7':    [ 11, 20 ], 
    'BminorM7':      [ 11, 20 ], 
    'BminorΔ7':      [ 11, 20 ], 
    'Bmmajor7':      [ 11, 20 ], 
    'Bmmaj7':        [ 11, 20 ], 
    'BmM7':          [ 11, 20 ], 
    'BmΔ7':          [ 11, 20 ], 
    'B-major7':      [ 11, 20 ], 
    'B-maj7':        [ 11, 20 ], 
    'B-M7':          [ 11, 20 ], 
    'B-Δ7':          [ 11, 20 ], 
    'Bminmajor7':    [ 11, 20 ], 
    'Bminmaj7':      [ 11, 20 ], 
    'BminM7':        [ 11, 20 ], 
    'BminΔ7':        [ 11, 20 ], 

    # B minor seventh
    'Bm7':      [11, 21],
    'B-7':      [11, 21],
    'Bmin7':    [11, 21],

    # B augmented-major seventh
    'B+M7':     [11, 22],
    'Baugmaj7':     [11, 22],
    'Baug-maj7':    [11, 22],
    'BM7#5':     [11, 22],
    'BM7+5':     [11, 22],
    'BΔ7#5':     [11, 22],
    'BΔ7+5':     [11, 22],

    # B augmented seventh
    'B+7':      [11, 23],
    'Baug7':    [11, 23],
    'B7#5':     [11, 23],
    'B7+5':     [11, 23],

    # B half-diminished seventh
    'Bø':       [11, 24],
    'Bø7':      [11, 24],
    'Bmin7dim5':    [11, 24],
    'Bm7b5':    [11, 24],
    'Bm7o5':    [11, 24],
    'B-7b5':    [11, 24],
    'B-7o5':    [11, 24],

    # B diminished seventh
    'Bo7':       [11, 25],
    'Bdim7':     [11, 25],

    # B diminished major seventh
    'BmM7b5':     [11, 26],
    'B-Δ7b5':     [11, 26],
    'BoM7':       [11, 26],
}