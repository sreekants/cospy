#!/usr/bin/python
# Filename: Lexer.py
# Description: Lexer for the Legata(Maritime) vocabulary

import ply.lex as lex

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
    'otherwise'	: 'OTHERWISE',
    'clear'	    : 'CLEAR',
    'continue'	: 'CONTINUE',
    'abort'	    : 'ABORT',
    'default'	: 'DEFAULT',
    'description'	    : 'DESCRIPTION',

    'range'     : 'RANGE',

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
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        return

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
        r'["\'](?:\\.|[^\'\\])*["\']'
        t.value = t.value[1:len(t.value)-1]    
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