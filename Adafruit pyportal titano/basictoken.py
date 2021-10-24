#! /usr/bin/python

# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Class to represent a token for the BASIC
programming language. A token consists of
three items:

column      Column in which token starts
category    Category of the token
lexeme      Token in string form

"""


class BASICToken:

        """BASICToken categories"""

        EOF             = 0   # End of file
        LET             = 1   # LET keyword
        LIST            = 2   # LIST command
        PRINT           = 3   # PRINT command
        RUN             = 4   # RUN command
        FOR             = 5   # FOR keyword
        NEXT            = 6   # NEXT keyword
        IF              = 7   # IF keyword
        THEN            = 8   # THEN keyword
        ELSE            = 9   # ELSE keyword
        ASSIGNOP        = 10  # '='
        LEFTPAREN       = 11  # '('
        RIGHTPAREN      = 12  # ')'
        PLUS            = 13  # '+'
        MINUS           = 14  # '-'
        TIMES           = 15  # '*'
        DIVIDE          = 16  # '/'
        NEWLINE         = 17  # End of line
        UNSIGNEDINT     = 18  # Integer
        NAME            = 19  # Identifier that is not a keyword
        EXIT            = 20  # Used to quit the interpreter
        DIM             = 21  # DIM keyword
        GREATER         = 22  # '>'
        LESSER          = 23  # '<'
        STEP            = 24  # STEP keyword
        GOTO            = 25  # GOTO keyword
        GOSUB           = 26  # GOSUB keyword
        INPUT           = 27  # INPUT keyword
        REM             = 28  # REM keyword
        RETURN          = 29  # RETURN keyword
        SAVE            = 30  # SAVE command
        LOAD            = 31  # LOAD command
        NOTEQUAL        = 32  # '<>'
        LESSEQUAL       = 33  # '<='
        GREATEQUAL      = 34  # '>='
        UNSIGNEDFLOAT   = 35  # Floating point number
        STRING          = 36  # String values
        TO              = 37  # TO keyword
        NEW             = 38  # NEW command
        EQUAL           = 39  # '='
        COMMA           = 40  # ','
        STOP            = 41  # STOP keyword
        COLON           = 42  # ':'
        ON              = 43  # ON keyword
        POW             = 44  # Power function
        SQR             = 45  # Square root function
        ABS             = 46  # Absolute value function
        DIM             = 47  # DIM keyword
        RANDOMIZE       = 48  # RANDOMIZE keyword
        RND             = 49  # RND keyword
        ATN             = 50  # Arctangent function
        COS             = 51  # Cosine function
        EXP             = 52  # Exponential function
        LOG             = 53  # Natural logarithm function
        SIN             = 54  # Sine function
        TAN             = 55  # Tangent function
        DATA            = 56  # DATA keyword
        READ            = 57  # READ keyword
        INT             = 58  # INT function
        CHR             = 59  # CHR$ function
        ASC             = 60  # ASC function
        STR             = 61  # STR$ function
        MID             = 62  # MID$ function
        MODULO          = 63  # MODULO operator
        TERNARY         = 64  # TERNARY functions
        VAL             = 65  # VAL function
        LEN             = 66  # LEN function
        UPPER           = 67  # UPPER function
        LOWER           = 68  # LOWER function
        ROUND           = 69  # ROUND function
        MAX             = 70  # MAX function
        MIN             = 71  # MIN function
        INSTR           = 72  # INSTR function
        AND             = 73  # AND operator
        OR              = 74  # OR operator
        NOT             = 75  # NOT operator
        PI              = 76  # PI constant
        RNDINT          = 77  # RNDINT function
        OPEN            = 78  # OPEN keyword
        HASH            = 79  # "#"
        CLOSE           = 80  # CLOSE keyword
        FSEEK           = 81  # FSEEK keyword
        RESTORE         = 82  # RESTORE keyword
        APPEND          = 83  # APPEND keyword
        OUTPUT          = 84  # OUTPUT keyword
        TAB             = 85  # TAB function
        SEMICOLON       = 86  # SEMICOLON
        LEFT            = 87  # LEFT$ function
        RIGHT           = 88  # RIGHT$ function
        DIR             = 89  # directory .bas function by bebox
        NEOPIXEL        = 90  # neopixel of keyboard FeatherWing
        LIGHT           = 91  # light sensor value
        PAUSE           = 92  # pause program (time.sleep) in ms
        GETTOUCH        = 93  # WAIT for touch screen and return x,y
        TOUCHX          = 94  # return x coord , -1 if no data
        TOUCHY          = 95  # return y coord , -1 if no data
        CLS             = 96  # clear screen
        BEEP            = 97  # bip a sound BEEP Freq in Hz , duration in Sec to debug
        PLAY            = 98  # play note C1 to G6 to debug
        PRINTAT         = 99  # print at x y "text"
        WAV            = 100  # play a wav file : WAVE filename
        GSCREEN        = 101  # show/hide Graphic screen ON / OFF
        GCIRCLE        = 102  # draw a circle
        GLINE          = 103  # draw a line
        GRECT          = 104  # draw a rectangle
        GTRIANGLE      = 105  # draw a triangle
        GPRINT         = 106  # print text on graphic screen x,y,"text",size,color, bgcolor
        WHITE          = 107  # WHITE color table
        BLACK          = 108  # BLACK color table
        RED            = 109  # RED
        ORANGE         = 110  # ORANGE
        YELLOW         = 111  #
        GREEN          = 112  #
        BLUE           = 113  #
        PURPLE         = 114  #
        PINK           = 115  #
        GRAY           = 116  #
        GREY           = 117  #
        GCLS           = 118  # Graphic Clear Screen
        NONE           = 119  # return None
        GRRECT         = 120  # Graphic Round Rectangle
        
        

        # Displayable names for each token category
        catnames = ['EOF', 'LET', 'LIST', 'PRINT', 'RUN',
        'FOR', 'NEXT', 'IF', 'THEN', 'ELSE', 'ASSIGNOP',
        'LEFTPAREN', 'RIGHTPAREN', 'PLUS', 'MINUS', 'TIMES',
        'DIVIDE', 'NEWLINE', 'UNSIGNEDINT', 'NAME', 'EXIT',
        'DIM', 'GREATER', 'LESSER', 'STEP', 'GOTO', 'GOSUB',
        'INPUT', 'REM', 'RETURN', 'SAVE', 'LOAD',
        'NOTEQUAL', 'LESSEQUAL', 'GREATEQUAL',
        'UNSIGNEDFLOAT', 'STRING', 'TO', 'NEW', 'EQUAL',
        'COMMA', 'STOP', 'COLON', 'ON', 'POW', 'SQR', 'ABS',
        'DIM', 'RANDOMIZE', 'RND', 'ATN', 'COS', 'EXP',
        'LOG', 'SIN', 'TAN', 'DATA', 'READ', 'INT',
        'CHR', 'ASC', 'STR', 'MID', 'MODULO', 'TERNARY',
        'VAL', 'LEN', 'UPPER', 'LOWER', 'ROUND',
        'MAX', 'MIN', 'INSTR', 'AND', 'OR', 'NOT', 'PI',
        'RNDINT', 'OPEN', 'HASH', 'CLOSE', 'FSEEK', 'APPEND',
        'OUTPUT', 'RESTORE', 'RNDINT', 'TAB', 'SEMICOLON',
        'LEFT', 'RIGHT', 'DIR', 'NEOPIXEL', 'LIGHT', 'PAUSE', 'GETTOUCH', 'TOUCHX', 'TOUCHY',
        'CLS', 'BEEP', 'PLAY', 'PRINTAT', 'WAV','GSCREEN', 'GCIRCLE','GLINE','GRECT','GTRIANGLE',
        'GPRINT', 'WHITE','BLACK','RED','ORANGE','YELLOW','GREEN',
        'BLUE','PURPLE','PINK','GRAY','GREY', 'GCLS', 'NONE', 'GRRECT']

        smalltokens = {'=': ASSIGNOP, '(': LEFTPAREN, ')': RIGHTPAREN,
                       '+': PLUS, '-': MINUS, '*': TIMES, '/': DIVIDE,
                       '\n': NEWLINE, '<': LESSER,
                       '>': GREATER, '<>': NOTEQUAL,
                       '<=': LESSEQUAL, '>=': GREATEQUAL, ',': COMMA,
                       ':': COLON, '%': MODULO, '!=': NOTEQUAL, '#': HASH,
                       ';': SEMICOLON}


        # Dictionary of BASIC reserved words
        keywords = {'LET': LET, 'LIST': LIST, 'PRINT': PRINT,
                    'FOR': FOR, 'RUN': RUN, 'NEXT': NEXT,
                    'IF': IF, 'THEN': THEN, 'ELSE': ELSE,
                    'EXIT': EXIT, 'DIM': DIM, 'STEP': STEP,
                    'GOTO': GOTO, 'GOSUB': GOSUB,
                    'INPUT': INPUT, 'REM': REM, 'RETURN': RETURN,
                    'SAVE': SAVE, 'LOAD': LOAD, 'NEW': NEW,
                    'STOP': STOP, 'TO': TO, 'ON':ON, 'POW': POW,
                    'SQR': SQR, 'ABS': ABS,
                    'RANDOMIZE': RANDOMIZE, 'RND': RND,
                    'ATN': ATN, 'COS': COS, 'EXP': EXP,
                    'LOG': LOG, 'SIN': SIN, 'TAN': TAN,
                    'DATA': DATA, 'READ': READ, 'INT': INT,
                    'CHR$': CHR, 'ASC': ASC, 'STR$': STR,
                    'MID$': MID, 'MOD': MODULO,
                    'IF$': TERNARY, 'IFF': TERNARY,
                    'VAL': VAL, 'LEN': LEN,
                    'UPPER$': UPPER, 'LOWER$': LOWER,
                    'ROUND': ROUND, 'MAX': MAX, 'MIN': MIN,
                    'INSTR': INSTR, 'END': STOP,
                    'AND': AND, 'OR': OR, 'NOT': NOT,
                    'PI': PI, 'RNDINT': RNDINT, 'OPEN': OPEN,
                    'CLOSE': CLOSE, 'FSEEK': FSEEK,
                    'APPEND': APPEND, 'OUTPUT':OUTPUT,
                    'RESTORE': RESTORE, 'TAB': TAB,
                    'LEFT$': LEFT, 'RIGHT$': RIGHT, 'DIR':DIR, 'NEOPIXEL':NEOPIXEL,
                    'LIGHT':LIGHT, 'PAUSE':PAUSE, 'GETTOUCH':GETTOUCH, 'TOUCHX':TOUCHX,
                    'TOUCHY':TOUCHY, 'CLS':CLS, 'BEEP':BEEP, 'PLAY':PLAY, 'PRINTAT':PRINTAT,
                    'WAV':WAV,'GSCREEN':GSCREEN,'GCIRCLE':GCIRCLE,'GLINE':GLINE,'GRECT':GRECT,
                    'GTRIANGLE':GTRIANGLE,'GPRINT':GPRINT,
                    'WHITE':WHITE,'BLACK':BLACK,'RED':RED,'ORANGE':ORANGE,'YELLOW':YELLOW,
                    'GREEN':GREEN, 'BLUE':BLUE,'PURPLE':PURPLE,'PINK':PINK,'GRAY':GRAY,'GREY':GREY ,
                    'GCLS':GCLS, 'NONE':NONE,'GRRECT':GRRECT}


        # Functions
        functions = {ABS, ATN, COS, EXP, INT, LOG, POW, RND, SIN, SQR, TAN,
                     CHR, ASC, MID, TERNARY, STR, VAL, LEN, UPPER, LOWER,
                     ROUND, MAX, MIN, INSTR, PI, RNDINT, TAB, LEFT, RIGHT, LIGHT, GETTOUCH,
                     TOUCHX, TOUCHY,WHITE,BLACK,RED,ORANGE,YELLOW,GREEN,
                     BLUE,PURPLE,PINK,GRAY,GREY, NONE}

        def __init__(self, column, category, lexeme):

            self.column = column      # Column in which token starts
            self.category = category  # Category of the token
            self.lexeme = lexeme      # Token in string form

        def pretty_print(self):
            """Pretty prints the token

            """
            print('Column:', self.column,
                  'Category:', self.catnames[self.category],
                  'Lexeme:', self.lexeme)

        def print_lexeme(self):
            print(self.lexeme, end=' ')
        
        def value_lexeme(self):
            print(self.lexeme, end=' ')
            a=str(self.lexeme)
            return a
