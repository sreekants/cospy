#!/usr/bin/python
# Filename: Lexer.py
# Description: Lexer for the Legata(Maritime) vocabulary

import ply.lex as lex
import re

class IllegalCharacter(TypeError):
    def __init__(self, char:str, lineno:int):
        """ Constructor
        Arguments
            char -- The character no token matches
            lineno -- Physical line it is on
        """
        TypeError.__init__(self, f"line {lineno}: Illegal character '{char}'")
        self.char       = char
        self.lineno     = lineno
        return

class Lexer:
    reserved = {
    'define'	: 'DEFINE',
    'import'	: 'IMPORT',
    'line'	    : 'LINE',
    'condition'	: 'CONDITION',
    'exclude'   : 'EXCLUDE',
    'precedent'	: 'PRECEDENT',
    'clause'	: 'CLAUSE',
    'assure'	: 'ASSURE',
    'apply'	    : 'APPLY',
    'otherwise'	: 'OTHERWISE',

    'clear'	    : 'CLEAR',
    'continue'	: 'CONTINUE',
    'abort'	    : 'ABORT',
    'fail'	    : 'FAIL',
    
    'default'	: 'DEFAULT',
    'description'	    : 'DESCRIPTION',

    'range'     : 'RANGE',
    'angle'     : 'ANGLE',

    'true'	    : 'TRUE',
    'false'	    : 'FALSE',

    'is'	    : 'IS',
    'not'	    : 'NOT',
    'and'	    : 'AND',
    'or'	    : 'OR',
    'in'	    : 'IN',
    'has'	    : 'HAS',
    'all'	    : 'ALL',
    'any'	    : 'ANY',
    'empty'     : 'EMPTY',

    'abs'       : 'MATH_ABS',
    'min'       : 'MATH_MIN',
    'max'       : 'MATH_MAX',
    'floor'     : 'MATH_FLOOR',
    'mean'      : 'MATH_MEAN',
    'std'       : 'MATH_STD',

    'count'     : "FN_COUNT",
    'add'       : "FN_ADD",
    'del'       : "FN_DEL",
    'set'       : "FN_SET",
    'isset'     : "FN_ISSET",
    'meters'    : 'FN_METERS',
    'miles'     : 'FN_MILES',
    'feets'     : 'FN_FEETS',
    'kmph'      : 'FN_KMPH',
    'knot'      : 'FN_KNOT',
    'nmphtokmph'    : 'FN_NMPHTOKMPH'
    }

    # List of token names.   This is always required
    tokens = [                                                     # OPERATORS #
    'PLUS' ,        # +
    'MINUS' ,       # -
    'MULTIPLY',     # *
    'DIVIDE',       # /
    'MODULO',       # %


    'OP_NOT',       # ~
    'OP_EQUALS',    # =

    # COMPARATORS #
    'LT',           # <
    'GT',           # >
    'LTE',          # <=
    'GTE',          # >=
    'EQ',           # ==
    'NEQ',          # !=
    'OP_AND',       # &
    'OP_OR' ,       # |                                                

    # BRACKETS #
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # [
    'RBRACE',       # ]
    'BLOCKSTART',   # {
    'BLOCKEND',     # }

    # SCOPE #
    'DOT',     		# .
    'COLON',     	# :
    'AMPERSAND',    # @
    'COMMA',        # ,

    # DATA TYPES#
    'INTEGER',      # int
    'FLOAT',		# floating point numbers
    'STRING',		# strings

    'COMMENT',  	# #

    'IDENTIFIER'	# Identifiers

    ] + list(reserved.values())

    # Regular expression rules for simple tokens

    t_PLUS		= r'\+'
    t_MINUS		= r'-'
    t_MULTIPLY	= r'\*'
    t_DIVIDE	= r'/'
    t_MODULO	= r'%'
    t_LPAREN 	= r'\('
    t_RPAREN	= r'\)'
    t_LBRACE	= r'\['
    t_RBRACE	= r'\]'
    t_BLOCKSTART = r'\{'
    t_BLOCKEND	= r'\}'
    t_OP_NOT	= r'\~'
    t_OP_EQUALS	= r'\='
    t_GT		= r'\>'
    t_LT		= r'\<'
    t_LTE		= r'\<\='
    t_GTE		= r'\>\='
    t_EQ        = r'\=\='
    t_NEQ		= r'\!\='
    t_OP_AND	= r'\&'
    t_OP_OR		= r'\|'
    t_COLON		= r'\:'
    t_DOT		= r'\.'
    t_AMPERSAND	= r'@'
    t_COMMA 	= r','
    t_ignore 	= ' \t'		# A string containing ignored characters (spaces and tabs)


    # Error handling rule
    def t_error(self, t):
        # Skipping would drop the character silently and compile what is left of the clause
        raise IllegalCharacter( t.value[0], t.lexer.lineno )

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return
    
    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok: 
                 break
             print(tok)
        return

    # A regular expression rule with some action code
    def t_FLOAT(self, t):
        r'(\d*\.\d+)|(\d+\.\d*)'
        t.value = float(t.value)
        return t        
    
    def t_INTEGER(self, t):
        r'\d+'
        t.value = int(t.value)    
        return t

    def t_STRING(self, t):
        r'"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\''
        # Each quote style closes only on its own quote; a backslash escapes the next character
        t.value = re.sub( r'\\(.)', r'\1', t.value[1:-1] )
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass
        # No return value. Token discarded
        
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9@\.\*]*'
        t.type = self.reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        numCR       = len(t.value)
        t.lexer.lineno += numCR
        t.lexer.charpos = t.lexer.lexpos+numCR

if __name__ == "__main__":
    # Build the lexer
    lexer = Lexer()