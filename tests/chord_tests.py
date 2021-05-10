#!/usr/bin/env python3

# Tests are organized in a dictionary:
#   'input' : 'expected-output'

chord_tests = {
# --------------------------------
#   C CHORDS
# --------------------------------
    # C major
    'C':        [0, 4, 7],
    'Cmaj':     [0, 4, 7],
    'CM':       [0, 4, 7],
    'CΔ':       [0, 4, 7],
    # C minor
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
}