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
#   <quality>   ::=  

# --------------------------------
#   CHAR LISTS / DICTIONARIES
# --------------------------------
whitespace = ' \n\t\r\v\f'
valid_chars = "abcdefgb#0123456789/majmindimaugsus"

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
natural_chars = { 'a', 'b', 'c', 'd', 'e', 'f', 'g' }
mod_chars = { '#', 'b' }


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


    def number_to_note(self, num):
        for key, value in notes.items():
            if (value == num):
                return key        


    def ignore_whitespace(self):
        # skip any whitespace chars
        while (self.pos < self.length and self.text[self.pos] in whitespace):
            self.pos += 1
        return

    def get_next_char(self):
        # ignore any whitespace
        self.ignore_whitespace()
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


