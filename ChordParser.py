#!/usr/bin/env python3

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
#                    M7 | maj7 | Δ7 |       (major seventh)
#                    mM7 | m#7 | -M7 | -Δ7 | minmaj7 | min-maj7 | (minor-major seventh)
#                    m7 | -7 | min7 |       (minor seventh)
#                    +M7 | augmaj7 | aug-maj7 | M7#5 | M7+5 | Δ7#5 | Δ7+5 | (augmented-major seventh)
#                    +7 | aug7 | 7#5 | 7+5 | (augmented seventh)
#                    ø | ø7 | min7dim5 | m7b5 | m7o5 | -7b5 | -7o5 | (half-diminished seventh)
#                    o7 | dim7 |            (diminished seventh)
#                    7b5 | 7dim5            (seventh flat five)

# --------------------------------
#   TOKENS / DICTIONARIES
# --------------------------------
valid_chars = "AaBbCcDdEeFfGg0123456789#bmajminaugdimΔ-+oMø"

notes = { 
    'c':        0,
    'c#/db':    1,
    'd':        2,
    'd#/eb':    3,
    'e':        4,
    'f':        5,
    'f#/gb':    6,
    'g':        7,
    'g#/ab':    8,
    'a':        9,
    'a#/bb':    10,
    'b':        11 
    }
triad_tokens = {
    'maj':      12,
    'min':      13,
    'aug':      14,
    'dim':      15
}
seventh_tokens = {
    'dom7':     16,
    'maj7':     17,
    'min-maj7': 18,
    'min7':     19,
    'aug-maj7': 20,
    'aug7':     21,
    'halfdim7': 22,
    'dim7':     23,
    '7b5':      24
}
natural_chars = { 'a', 'b', 'c', 'd', 'e', 'f', 'g' }
mod_chars = { '#', 'b' }

major_triad_id = { 'maj', 'M', 'Δ' }
minor_triad_id = { 'm', '-', 'min' }
aug_triad_id = { '+', 'aug', 'M#5', 'M+5' }
dim_triad_id = { 'o', 'dim', 'mb5', 'mo5' }

#   <seventh>   ::=  7 | dom7 |             (dominant seventh)
#                    M7 | maj7 | Δ7 |       (major seventh)
#                    mM7 | m#7 | -M7 | -Δ7 | minmaj7 | min-maj7 | (minor-major seventh)
#                    m7 | -7 | min7 |       (minor seventh)
#                    +M7 | augmaj7 | aug-maj7 | M7#5 | M7+5 | Δ7#5 | Δ7+5 | (augmented-major seventh)
#                    +7 | aug7 | 7#5 | 7+5 | (augmented seventh)
#                    ø | ø7 | min7dim5 | m7b5 | m7o5 | -7b5 | -7o5 | (half-diminished seventh)
#                    o7 | dim7 |            (diminished seventh)
#                    7b5 | 7dim5            (seventh flat five)


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

        try:
            self.chord()
        except ParseError as error:
            print(error)
        
    def chord(self):
        # root note of the chord
        self.note()
        # quality of the chord
        self.quality()

        print (self.stack)

    def note(self):
        self.natural()
        # mod is optional
        self.mod()

    def natural(self):
        char = self.get_next_char()
        if (char not in natural_chars):
            raise ParseError(self.pos, "SYNTAX", "\'%s\' is not a valid natural char" % char)
        # add note to stack
        self.stack.append(notes.get(char))

    def mod(self):
        char = self.get_next_char()
        if (char in mod_chars):
            # pop note off the stack and replace with respective #/b
            if (char == '#'):
                num = self.stack.pop()
                # make sure note is not b or e (don't have #'s)
                if (num == notes.get('b') or num == notes.get('e')):
                    raise ParseError(self.pos, "SYNTAX", "\'%s#\' is not a vaild note" % self.number_to_note(num))
                # increament note index by 1 to get respective #
                num += 1
                self.stack.append(num)
            elif (char == 'b'):
                num = self.stack.pop()
                # make sure note is not c or f (don't have b's)
                if (num == notes.get('c') or num == notes.get('f')):
                    raise ParseError(self.pos, "SYNTAX", "\'%sb\' is not a vaild note" % self.number_to_note(num))
                # decrement note index by 1 to get respective #
                num -= 1
                self.stack.append(num)

    def quality(self):
        # check for triad ids
        self.triad()

    def triad(self):
        # check for each type of triad
        # major triad
        for n in major_triad_id:
            if (self.look_ahead(n)):
                self.pos += len(n)
                self.stack.append(triad_tokens.get('maj'))
                return
        # minor triad
        for n in minor_triad_id:
            if (self.look_ahead(n)):
                self.pos += len(n)
                self.stack.append(triad_tokens.get('min'))
                return
        # augmented triad
        for n in aug_triad_id:
            if (self.look_ahead(n)):
                self.pos += len(n)
                self.stack.append(triad_tokens.get('aug'))
                return
        # diminished triad
        for n in dim_triad_id:
            if (self.look_ahead(n)):
                self.pos += len(n)
                self.stack.append(triad_tokens.get('dim'))
                return

    def seventh(self):
        pass

    def number_to_note(self, num):
        for key, value in notes.items():
            if (value == num):
                return key        

    def get_next_char(self):
        # make sure pos is not out of bounds
        if (self.pos >= self.length):
            return
        # check if char is valid
        char = self.text[self.pos]
        if (char not in valid_chars):
            raise ParseError(self.pos, "INVALID CHAR", "\'%s\' is not a valid char" % char)
        # return char
        self.pos += 1
        return char

    def look_ahead(self, value):
        # get the substring from pos to end
        sub_str = self.text[self.pos - 1:]
        # print ("sub_str: %s value: %s" % (sub_str, value))
        if (value in sub_str):
            return True
        return False


