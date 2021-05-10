#!/usr/bin/env python3

import sys

# --------------------------------
#   RESOURCES
# --------------------------------

#   - https://www.researchgate.net/publication/220723539_Symbolic_Representation_of_Musical_Chords_A_Proposed_Syntax_for_Text_Annotations
#   - https://www.stringkick.com/blog-lessons/chord-names-symbols/
#   - https://en.wikipedia.org/wiki/Chord_names_and_symbols_(popular_music)#:~:text=Chord%20qualities%20are%20related%20to,%2C%20diminished%2C%20and%20half%2Ddiminished

# --------------------------------
#   BNF GRAMMAR
# --------------------------------

#   <chord>     ::=  <note> <quality> (other stuff goes here) <slash>
#   <note>      ::=  <natural> | <natural> <mod>
#   <natural>   ::=  a | b | c | d | e | f | g
#   <mod>       ::=  b | #
#   <quality>   ::=  <triad> | <seventh>
#   <triad>     ::=  maj | M | Δ | ε |      (major triad)
#                    m | - | min |          (minor triad)
#                    + | aug | M#5 | M+5 |  (augmented triad)
#                    o | dim | mb5 | mo5    (diminished triad)  
# 
#   <seventh>   ::=  7 | dom7 |             (dominant seventh)
#                    7b5 | 7dim5            (dominant seventh flat five)
#                    M7 | maj7 | Δ7 |       (major seventh)
#                    M7b5 | Δ7b5            (major seventh flat five)
#                    mM7 | m#7 | -M7 | -Δ7 | minmaj7 | min-maj7 | (minor-major seventh)
#                    m7 | -7 | min7 |       (minor seventh)
#                    +M7 | augmaj7 | aug-maj7 | M7#5 | M7+5 | Δ7#5 | Δ7+5 | (augmented-major seventh)
#                    +7 | aug7 | 7#5 | 7+5 | (augmented seventh)
#                    ø | ø7 | min7dim5 | m7b5 | m7o5 | -7b5 | -7o5 | (half-diminished seventh)
#                    o7 | dim7 |            (diminished seventh)
#                    mM7b5 | -Δ7b5 | oM7 |  (diminished major seventh)

# --------------------------------
#   TOKENS / DICTIONARIES
# --------------------------------
valid_chars = "AaBbCcDdEeFfGg0123456789#bmajminaugdimΔ-+oMø/"

notes = { 
    'C':        0,
    'C#/Db':    1,
    'D':        2,
    'D#/Eb':    3,
    'E':        4,
    'F':        5,
    'F#/Gb':    6,
    'G':        7,
    'G#/Ab':    8,
    'A':        9,
    'A#/Bb':    10,
    'B':        11 
    }
quality_tokens = {
    # triads
    'maj':      12,
    'min':      13,
    'aug':      14,
    'dim':      15,
    # sevenths
    'dom7':     16,
    'dom7b5':   17,
    'maj7':     18,
    'maj7b5':   19,
    'min-maj7': 20,
    'min7':     21,
    'aug-maj7': 22,
    'aug7':     23,
    'halfdim7': 24,
    'dim7':     25,
    'dim-maj7': 26
}
natural_chars = { 'A', 'B', 'C', 'D', 'E', 'F', 'G' }
mod_chars = { '#', 'b' }

major_triad_id = { 'maj', 'M', 'Δ' }
minor_triad_id = { 'm', '-', 'min' }
aug_triad_id = { '+', 'aug', 'M#5', 'M+5' }
dim_triad_id = { 'o', 'dim', 'mb5', 'mo5' }

dom_seventh_id = { '7', 'dom7' }
dom_seventh_b5_id = { '7b5', '7dim5' }
major_seventh_id = { 'M7', 'maj7', 'Δ7' }
major_seventh_b5_id = { 'M7b5', 'Δ7b5' }
minor_major_seventh_id = { 'mM7', 'm#7', '-M7', '-Δ7', 'minmaj7', 'min-maj7' }
minor_seventh_id = { 'm7', '-7', 'min7' }
aug_major_seventh_id= { '+M7', 'augmaj7', 'aug-maj7', 'M7#5', 'M7+5', 'Δ7#5', 'Δ7+5' }
aug_seventh_id = { '+7', 'aug7', '7#5', '7+5' }
half_dim_seventh_id = { 'ø', 'ø7', 'min7dim5', 'm7b5', 'm7o5', '-7b5', '-7o5' }
dim_seventh_id = { 'o7', 'dim7' }
dim_major_seventh_id = { 'mM7b5', '-Δ7b5', 'oM7' }

triad_delimiters = ' /'
seventh_delimiters = ' /'

# --------------------------------
#   CHORD INTERVALS (SEMITONES)
# --------------------------------

major_triad_ints = [ 0, 4, 7 ] # R 3 5
minor_triad_ints = [ 0, 3, 7 ] # R b3 5
dim_triad_ints = [ 0, 3, 6 ] # R b3 b5
aug_triad_ints = [ 0, 4, 8 ] # R 3 #5

# --------------------------------
#   ERROR CLASS
# --------------------------------
class ParseError(Exception):
    def __init__(self, pos, err, msg):
        self.pos = pos
        self.err = err
        self.msg = msg

    def __str__(self):
        return 'ParseError[%s]: %s at pos: %i' % (self.err, self.msg, self.pos)

class ChordParser:
    def __init__(self):
        pass

    def parse(self, text):
        self.text = text
        self.length = len(self.text)
        self.pos = 0
        self.stack = []
        self.validated = True
        self.curr_char = ''

        try:
            self.chord()
            return self.stack
        except ParseError as error:
            print(error)
            sys.exit(1)
            

    # --------------------------------
    #   GRAMMAR FUNCTIONS
    # --------------------------------
        
    def chord(self):
        # root note of the chord
        self.note()
        # quality of the chord
        self.quality()
        # other parts go here

        # slash
        self.slash()

    def note(self):
        self.natural()
        # mod is optional
        self.mod()

    def natural(self):
        char = self.get_next_char()
        char = char.upper()
        if (char not in natural_chars):
            raise ParseError(self.pos, "SYNTAX", "\'%s\' is not a valid natural char" % char)
        # add note to stack
        self.stack.append(notes.get(char))
        self.validated = True

    def mod(self):
        char = self.get_next_char()
        if (char in mod_chars):
            # pop note off the stack and replace with respective #/b
            if (char == '#'):
                num = self.stack.pop()
                # make sure note is not b or e (don't have #'s)
                if (num == notes.get('B') or num == notes.get('E')):
                    raise ParseError(self.pos, "SYNTAX", "\'%s#\' is not a vaild note" % self.number_to_note(num))
                # increament note index by 1 to get respective #
                num += 1
                self.stack.append(num)
                self.validated = True
            elif (char == 'b'):
                num = self.stack.pop()
                # make sure note is not c or f (don't have b's)
                if (num == notes.get('C') or num == notes.get('F')):
                    raise ParseError(self.pos, "SYNTAX", "\'%sb\' is not a vaild note" % self.number_to_note(num))
                # decrement note index by 1 to get respective #
                num -= 1
                self.stack.append(num)
                self.validated = True
        else:
            self.validated = True
            self.pos -= 1

    def quality(self):
        # check for seventh ids
        if not self.seventh():
            # check for triad ids
            self.triad()

    def slash(self):
        char = self.get_next_char()
        #print (char)
        if (char == '/'):
            self.validated = True
            # get the bass note
            char = self.get_next_char()
            self.note()
             
    def triad(self):
        # check for each type of triad
        # augmented triad
        for n in aug_triad_id:
            if (self.next_up(n, triad_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('aug'))
                return True
        # diminished triad
        for n in dim_triad_id:
            if (self.next_up(n, triad_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('dim'))
                return True
        # major triad
        for n in major_triad_id:
            if (self.next_up(n, triad_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('maj'))
                return True
        # minor triad
        for n in minor_triad_id:
            if (self.next_up(n, triad_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('min'))
                return True
        # if no quality symbol is given, chord is major by default
        self.stack.append(quality_tokens.get('maj'))
        return True

    def seventh(self):
        # check for each type of seventh
        # dominant seventh
        for n in dom_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('dom7'))
                return True
        # dominant seventh flat five
        for n in dom_seventh_b5_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('dom7b5'))
                return True
        # major seventh
        for n in major_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('maj7'))
                return True
        # major seventh flat five
        for n in major_seventh_b5_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('maj7b5'))
                return True
        # minor-major seventh
        for n in minor_major_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('min-maj7'))
                return True
        # minor seventh
        for n in minor_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('min7'))
                return True
        # augmented-major seventh
        for n in aug_major_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('aug-maj7'))
                return True
        # augmented seventh
        for n in aug_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('aug7'))
                return True
        # half-diminished seventh
        for n in half_dim_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('halfdim7'))
                return True
        # diminished seventh
        for n in dim_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('dim7'))
                return True
        # diminished major seventh
        for n in dim_major_seventh_id:
            if (self.next_up(n, seventh_delimiters)):
                self.pos += len(n)
                self.stack.append(quality_tokens.get('dim-maj7'))
                return True
        return False # no seventh quality found
    
    # --------------------------------
    #   UTILITY FUNCTIONS
    # --------------------------------

    def number_to_note(self, num):
        if (num < 0 or num > 11):
            return
        for key, value in notes.items():
            if (value == num):
                return key

    def number_to_quality(self, num):
        if (num < 11):
            return
        for key, value in quality_tokens.items():
            if (value == num):
                return key

    def get_next_char(self):
        # return if 
        if (not self.validated):
            return self.curr_char
        # make sure pos is not out of bounds
        if (self.pos >= self.length):
            return
        # check if char is valid
        char = self.text[self.pos]
        if (char not in valid_chars):
            raise ParseError(self.pos, "INVALID CHAR", "\'%s\' is not a valid char" % char)
        # return char
        self.pos += 1
        self.curr_char = char
        self.validated = False
        return char

    def next_up(self, value, delimiters = ['']):
        # get the substring from pos to end
        sub_str = self.text[self.pos:]
        #print ("sub_str: %s value: %s delim: %s" % (sub_str, value, delimiters))
        if (sub_str.startswith(value, 0)):
            after_next = sub_str[len(value):]
            #print ("after_next: " + after_next)
            if (len(after_next) == 0):
                return True
            next_char = after_next[0]
            if (next_char in delimiters):
                return True
        return False

    def print_chord(self, stack):
        root, quality, bass = self.translate_stack(stack)

        if (bass != None):
            print ("chord parsed: %s %s / %s" % (root, quality, bass))
        else:
            print ("chord parsed: %s %s" % (root, quality))

    def translate_stack(self, stack):
        # get the root of the chord
        root = self.number_to_note(stack.pop(0))
        
        # get the quality of the chord
        quality = self.number_to_quality(stack.pop(0))

        bass = None
        # get slash bass note (optional)
        if (len(stack) > 0):
            print ("bass!")
            bass = self.number_to_note(stack.pop(0))
        
        return root, quality, bass
        

    def stack_to_notes(self, stack):
        pass
