#!/usr/bin/env python3

# --------------------------------
#   RESOURCES
# --------------------------------

#   - https://www.researchgate.net/publication/220723539_Symbolic_Representation_of_Musical_Chords_A_Proposed_Syntax_for_Text_Annotations
#   - https://www.stringkick.com/blog-lessons/chord-names-symbols/

# --------------------------------
#   CHAR LIST
# --------------------------------
whitespace = ' \n\t\r\v\f'
valid_chars = "abcdefgb#0123456789/majmindimaugsus"

# --------------------------------
#   BNF GRAMMAR
# --------------------------------

#   <chord>     ::=  <note> (other stuff goes here)
#   <note>      ::=  <natural> | <natural> <mod>
#   <natural>   ::=  a | b | c | d | e | f | g
#   <mod>       ::=  b | #

# --------------------------------
#   ERROR CLASS
# --------------------------------
class ParseError:
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

        try:
            chord()
        except ParseError as error:
            print(error)
        
    def chord(self):
        token = get_next_token()

    def ignore_whitespace(self):
        # skip any whitespace chars
        while (self.pos < self.length and self.text[self.pos] in whitespace):
            self.pos += 1
        return

    def get_next_token(self):


