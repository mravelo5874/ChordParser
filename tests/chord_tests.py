#!/usr/bin/env python3

# Tests are organized in a dictionary:
#   'input' : 'expected-output'

chord_tests = {
# --------------------------------
#   C CHORDS
# --------------------------------
    # C major
    'C':        [0, 4, 7], 
    'Cmajor':   [0, 4, 7],
    'Cmaj':     [0, 4, 7],
    'CM':       [0, 4, 7],
    'CΔ':       [0, 4, 7],
    # C minor
    'Cminor':   [0, 3, 7],
    'Cm':       [0, 3, 7],
    'C-':       [0, 3, 7],
    'Cmin':     [0, 3, 7],
    # C augmented
    'C+':       [0, 3, 6],
    'Caug':     [0, 3, 6],
    'CM#5':     [0, 3, 6],
    'CM+5':     [0, 3, 6],
    # C diminished
    'Co':       [0, 4, 8],
    'Cdim':     [0, 4, 8],
    'Cmb5':     [0, 4, 8],
    'Cmo5':     [0, 4, 8],
    # C dominant seventh
    'C7':       [ 0, 4, 7, 10 ],
    'Cdom':     [ 0, 4, 7, 10 ],
    'Cdom7':    [ 0, 4, 7, 10 ],
    'C7dim5':   [ 0, 4, 7, 10 ],
    # C dominant seventh flat five
    'C7b5':     [ 0, 4, 6, 10 ],
    'C7-5':      [ 0, 4, 6, 10 ],
    'Cdom7b5':   [ 0, 4, 6, 10 ],
    'Cdom7-5':   [ 0, 4, 6, 10 ],
    # C major seventh
    'CM7':      [ 0, 4, 7, 11 ],
    'Cmaj7':    [ 0, 4, 7, 11 ],
    'CΔ7':      [ 0, 4, 7, 11 ],
    'Cmajor7':  [ 0, 4, 7, 11 ],
    # C major seventh flat five
    'CM7b5':    [ 0, 4, 6, 11 ],
    'CΔ7b5':    [ 0, 4, 6, 11 ],
    'Cmaj7b5':  [ 0, 4, 6, 11 ],
    'Cmajor7b5':    [ 0, 4, 6, 11 ],
    'CM7-5':    [ 0, 4, 6, 11 ],
    'CΔ7-5':    [ 0, 4, 6, 11 ],
    'Cmaj7-5':  [ 0, 4, 6, 11 ],
    'Cmajor7-5':    [ 0, 4, 6, 11 ],
    # C minor major seventh
    'Cminormajor7':  [ 0, 3, 7, 11 ], 
    'Cminormaj7':    [ 0, 3, 7, 11 ],
    'CminorM7':      [ 0, 3, 7, 11 ],
    'CminorΔ7':      [ 0, 3, 7, 11 ],
    'Cmmajor7':      [ 0, 3, 7, 11 ],
    'Cmmaj7':        [ 0, 3, 7, 11 ],
    'CmM7':          [ 0, 3, 7, 11 ],
    'CmΔ7':          [ 0, 3, 7, 11 ],
    'C-major7':      [ 0, 3, 7, 11 ],
    'C-maj7':        [ 0, 3, 7, 11 ],
    'C-M7':          [ 0, 3, 7, 11 ],
    'C-Δ7':          [ 0, 3, 7, 11 ],
    'Cminmajor7':    [ 0, 3, 7, 11 ],
    'Cminmaj7':      [ 0, 3, 7, 11 ],
    'CminM7':        [ 0, 3, 7, 11 ],
    'CminΔ7':        [ 0, 3, 7, 11 ],
    # C minor seventh
    'Cm7':      [ 0, 3, 7, 10 ],
    'C-7':      [ 0, 3, 7, 10 ],
    'Cmin7':    [ 0, 3, 7, 10 ],
    # C augmented major seventh
    'C+M7':     [ 0, 4, 8, 11 ],
    'Caugmaj7': [ 0, 4, 8, 11 ],
    'Caug-maj7':    [ 0, 4, 8, 11 ],
    'CM7#5':    [ 0, 4, 8, 11 ],
    'CM7+5':    [ 0, 4, 8, 11 ],
    'CΔ7#5':    [ 0, 4, 8, 11 ],
    'CΔ7+5':    [ 0, 4, 8, 11 ],
    # C augmented seventh
    'C+7':      [ 0, 4, 8, 10 ],
    'Caug7':    [ 0, 4, 8, 10 ],
    'C7#5':     [ 0, 4, 8, 10 ],
    'C7+5':     [ 0, 4, 8, 10 ],
    # C half-diminished seventh
    'Cø':       [ 0, 3, 6, 10 ],
    'Cø7':      [ 0, 3, 6, 10 ],
    'Cmin7dim5':    [ 0, 3, 6, 10 ],
    'Cm7b5':    [ 0, 3, 6, 10 ],
    'Cm7o5':    [ 0, 3, 6, 10 ],
    'C-7b5':    [ 0, 3, 6, 10 ],
    'C-7o5':    [ 0, 3, 6, 10 ],
    # C diminished seventh
    'Co7':      [ 0, 3, 6,  9 ],
    'Cdim7':    [ 0, 3, 6,  9 ],
    # C diminished major seventh
    'CmM7b5':   [ 0, 3, 6, 11 ],
    'C-Δ7b5':   [ 0, 3, 6, 11 ],
    'CoM7':     [ 0, 3, 6, 11 ],
}