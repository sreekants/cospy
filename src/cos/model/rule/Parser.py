#!/usr/bin/python
# Filename: Parser.py
# Description: Parser for the Legata(Maritime) vocabulary

from cos.model.rule.Definition import Definition
from cos.model.rule.Lexer import Lexer
from cos.model.logic.Symbol import *
from cos.model.rule.Expression import *

from cos.model.rule.Lexer import Lexer

import ply.yacc as yacc


class Parser:
    def __init__(self, automata=None):
        self.parser     = None
        self.filename   = None
        self.automata   = automata
        self.debug      = False
        return

    def build(self,**kwargs):
        global tokens

        self.lexer          = Lexer()
        self.lexer.build()
        self.tokens	        = self.lexer.tokens

        self.parser         = yacc.yacc(module=self, **kwargs)

        # Initialize the state variables
        self.definitions    = {}
        self.defaults       = {}
        self.definitions    = {}
        self.conditions     = []
        self.clauses        = []

        return

    def parse(self, data, path:str=None):
        if path is not None:
            self.filename	= path

        # TODO: Preprocess file for imports
        self.parser.parse(data)
        self.__dump()
        self.__generate_automata()
        return
    
    def __dump(self):
        if self.debug == False:
            return
        
        print( f'Definitions {len(self.definitions)}')
        print( f'Conditions {len(self.conditions)}')
        print( f'Clauses {len(self.clauses)}')
        return

    def __generate_automata(self):
        if self.automata is not None:
            self.automata.generate( self.conditions, self.clauses )
        return

    # GRAMMAR
    def p_rule(self, p):
        """
        rule : blocks
        """
    
        # Consolidate all the blocks into variables.
        for block in p[1]:
            btype   = block[0]
            bvalue  = block[1]
            target  = None
            match btype:
                case 'conditions':
                    target  = self.conditions
                case 'clauses':
                    target  = self.clauses

            if target is not None:
                target.extend(bvalue)

        return

    def p_blocks(self, p):
        """
        blocks : declaration
        blocks : blocks declaration 
        """
        self.fold(p, 2)
        return

    def p_declaration(self, p):
        """
        declaration : global_definitions 
        declaration : global_defaults
        declaration : global_conditions
        declaration : global_clauses
        """
        self.move(p)
        return

    def p_global_conditions(self, p):
        """
        global_conditions : conditions
        """
        p[0]    = ('conditions', p[1])
        return

    def p_global_clauses(self, p):
        """
        global_clauses : clauses
        """
        p[0]    = ('clauses', p[1])
        return

    def p_global_definitions(self, p):
        """
        global_definitions : definitions
        """
        p[0]    = ('definitions', p[1])
        return

    def p_global_defaults(self, p):
        """
        global_defaults : defaults
        """
        p[0]    = ('defaults', p[1])
        return

    def p_clauses(self, p):
        """
        clauses : clause
        clauses : clauses clause 
        """
        self.fold(p, 2)
        return

    def p_clause(self, p):
        """
        clause : clause_keyword LBRACE STRING RBRACE COLON BLOCKSTART clause_statements BLOCKEND
        """
        self.move(p, {
            'location': p[1],
            'name': p[3], 
            'definition': p[7] 
            })
        
        return

    def p_clause_keyword(self, p):
        """
        clause_keyword : CLAUSE
        """
        p[0]    = self.here(p)
        return

    def p_clause_statements(self, p):
        """
        clause_statements : clause_statement
        clause_statements : clause_statements clause_statement
        """
        self.fold(p, 2)
        return

    def p_clause_statement(self, p):
        """
        clause_statement : COLON BLOCKSTART conditions assurances BLOCKEND
        """
        p[0]    = { 
                    'conditions': p[3], 
                    'assurances': p[4]
                    }
        
        return

    def p_assurances(self, p):
        """
        assurances :
        assurances : ASSURE COLON BLOCKSTART assurance_statements BLOCKEND 
        """
        match len(p):
            case 1:
                self.move(p, [])
            case 6:
                self.move(p, p[4])
        return

    def p_assurance_statements(self, p):
        """
        assurance_statements : assurance_statement
        assurance_statements : assurance_statements assurance_statement 
        """
        self.fold(p, 2)
        return

    def p_assurance_statement(self, p):
        """
        assurance_statement : COLON action_commands
        assurance_statement : COLON compound_action 
        """
        self.move(p, p[2])
        return

    def p_compound_action(self, p):
        """
        compound_action : action_expression
        compound_action : compound_action AND action_expression
        compound_action : compound_action OR action_expression
        """
        self.fold_logic_expression( p, 'compound action' )
        return

    def p_action_expression(self, p):
        """
        action_expression : expression
        """
        self.move(p, ('expression',p[1]))
        return

    def p_action_commands(self, p):
        """
        action_commands : ABORT
        action_commands : CLEAR
        action_commands : CONTINUE
        """
        self.move(p,  [('^', ('command',p[1]))])
        return

    def p_conditions(self, p):
        """
        conditions : CONDITION COLON BLOCKSTART condition_statements BLOCKEND 
        """
        self.move(p, p[4])
        return

    def p_condition_statements(self, p):
        """
        condition_statements : condition
        condition_statements : condition_statements condition 
        """
        self.fold(p, 2)     
        return

    def p_condition(self, p):
        """
        condition : COLON expression 
        """
        self.move(p, p[2])
        return

    def p_definitions(self, p):
        """
        definitions : DEFINE COLON BLOCKSTART pairs BLOCKEND 
        """
        # Iterate through the definitions and add them to the list
        self.to_map(p[4], self.definitions)
        return
    
    def p_defaults(self, p):
        """
        defaults : DEFAULT COLON BLOCKSTART pairs BLOCKEND 
        """
        # Iterate through the defaults and add them to the list
        self.to_map(p[4], self.defaults)            
        return

    def p_expression(self, p):
        """
        expression : simple_expression
        expression : compound_expression
        """
        self.move(p)
        return

    def p_simple_expression(self, p):
        """
        simple_expression : expression_statement
        """
        self.move(p, [('?', p[1])])
        return

    def p_compound_expression(self, p):
        """
        compound_expression : scoped_expression
        compound_expression : compound_expression AND scoped_expression
        compound_expression : compound_expression OR scoped_expression
        """

        self.fold_logic_expression( p, 'compount expression')
        return

    def p_scoped_expression(self, p):
        """
        scoped_expression : LPAREN expression_statement RPAREN
        scoped_expression : LPAREN compound_expression RPAREN
        """
        self.move(p, p[2])
        return


    def p_expression_statement(self, p):
        """
        expression_statement : subject_is_object
        expression_statement : subject_is_not_object
        expression_statement : subject_in_range
        expression_statement : subject_in_any_range
        expression_statement : subject_not_in_range
        expression_statement : subject_not_in_any_range
        expression_statement : subject_comparison
        """
        self.move(p)
        return

    def p_subject_comparison(self, p):
        """
        subject_comparison : subject LT rvalue
        subject_comparison : subject GT rvalue
        subject_comparison : subject LTE rvalue
        subject_comparison : subject GTE rvalue
        subject_comparison : subject EQ rvalue
        subject_comparison : subject NEQ rvalue
        """
        opcode  = p[2]
        lhs     = p[1]
        rhs     = p[3]
        match opcode:
            case '<':
                p[0]    = Symbol.Operator(LT(lhs,rhs))
            case '>':
                p[0]    = Symbol.Operator(GT(lhs,rhs))
            case '<=':
                p[0]    = Symbol.Operator(LTE(lhs,rhs))
            case '>=':
                p[0]    = Symbol.Operator(GTE(lhs,rhs))
            case '==':
                p[0]    = Symbol.Operator(EQ(lhs,rhs))
            case '!=':
                p[0]    = Symbol.Operator(NEQ(p[1], p[3]))
               
        return

    def p_subject_is_object(self, p):
        """
        subject_is_object : subject IS object
        """
        p[0]    = EQ(p[1], p[3])
        return

    def p_subject_is_not_object(self, p):
        """
        subject_is_not_object : subject IS NOT object
        """
        p[0]    = NEQ(p[1], p[4])
        return

    def p_subject_in_range(self, p):
        """
        subject_in_range : subject IN range_expression
        """
        p[0]    = IN(p[1], p[3], True)
        return

    def p_subject_in_any_range(self, p):
        """
        subject_in_any_range : subject IN ANY range_expression
        """
        p[0]    = IN(p[1], p[4], False)
        return

    def p_subject_not_in_range(self, p):
        """
        subject_not_in_range : subject NOT IN range_expression
        """
        p[0]    = NOT_IN(p[1], p[4], False)
        return

    def p_subject_not_in_any_range(self, p):
        """
        subject_not_in_any_range : subject NOT IN ANY range_expression
        """
        p[0]    = NOT_IN(p[1], p[5], True)
        return

    def p_rvalue(self, p):
        """
        rvalue : identifier
        rvalue : number
        """
        self.move(p)
        return
    
    def p_range_expression(self, p):
        """
        range_expression : array
        range_expression : range    
        range_expression : identifier
        """
        self.move(p)
        return


    def p_range(self, p):
        """
        range : RANGE LPAREN number COMMA number RPAREN
        """
        p[0]    = Symbol.Range(p[3], p[5])
        return

    def p_subject(self, p):
        """
        subject : identifier
        subject : computed_variable
        subject : functional_expression
        """
        self.move(p)
        return

    def p_computed_variable(self, p):
        """
        computed_variable : intersection_variable
        computed_variable : tuple_variable
        """
        self.move(p)
        return

    def p_functional_expression(self, p):
        """
        functional_expression : function LPAREN arglist RPAREN
        """
        func    = p[1]
        args    = p[3]
        p[0]    = Symbol.Function(func, args)
        return

    def p_function(self, p):
        """
        function : MATH_ABS
        function : MATH_MIN
        function : MATH_MAX
        function : MATH_FLOOR
        function : MATH_MEAN
        function : MATH_STD
        function : FN_NMPHTOKMPH
        """
        self.move(p)
        return

    def p_intersection_variable(self, p):
        """
        intersection_variable : intersection DOT identifier
        """
        p[0]    = Symbol.List(p[1])
        return 

    def p_intersection(self, p):
        """
        intersection : LBRACE valuelist RBRACE
        """
        p[0]    = p[2]
        return 

    def p_valuelist(self, p):
        """
        valuelist : rvalue
        valuelist : valuelist COMMA rvalue
        """
        self.fold(p, 3)
        return 

    def p_tuple_variable(self, p):
        """
        tuple_variable : tuple DOT identifier
        """
        parts   = p[1]
        p[0]    = Symbol.Variable( f'({parts[0]},{parts[1]}).{p[3]}' )
        return 

    def p_tuple(self, p):
        """
        tuple : LPAREN rvalue COMMA rvalue RPAREN
        """
        lvalue  = p[2]
        rvalue  = p[4]
        p[0]    = (lvalue, rvalue)
        return 

    def p_object(self, p):
        """
        object : identifier
        object : EMPTY
        """

        if p[1] == 'empty':
            p[0]    = None
        else:
            self.move(p)

        return

    def p_array(self, p):
        """
        array : LBRACE arglist RBRACE
        """
        self.move(p, p[2])
        return

    def p_arglist(self, p):
        """
        arglist : arg
        arglist : arglist COMMA arg
        """
        self.fold(p, 3)
        return

    def p_arg(self, p):
        """
        arg : computed_variable
        arg : identifier
        arg : number
        arg : STRING
        arg : EMPTY
        """
        if p[1] == 'empty':
            p[0]    = None
        else:
            self.move(p)
        return

    def p_pairs(self, p):
        """
        pairs : pair 
        pairs : pairs pair
        """
        self.fold(p, 2)
        pass


    def p_pair(self, p):
        """
        pair : key COLON value
        """
        p[0]    = (p[1], p[3])
        return

    def p_key(self, p):
        """
        key : IDENTIFIER
        """
        p[0]    = Symbol.Variable(p[1])
        return

    def p_value(self, p):
        """
        value : IDENTIFIER
        value : FLOAT
        value : INTEGER
        value : STRING
        """
        p[0]    = Symbol.Variable(p[1])
        return

    def p_identifier(self, p):
        """
        identifier : IDENTIFIER
        """
        var     = p[1]
        sep     = var.find('.')
        if sep == -1:
            var     = self.resolve(p, var)
        else:
            scope   = var[:sep] 
            rscope  = self.resolve(p, scope)
            if rscope != scope:
                var = f'{rscope}{var[sep:]}'

        p[0]    = Symbol.Variable(self.resolve(p, var))
        return

    def p_number(self, p):
        """
        number : INTEGER
        number : FLOAT
        """
        val    = p[1]

        if isinstance(val, int):
            p[0]    = Symbol.Integer(p[1])
            return
        elif isinstance(val, float):
            p[0]    = Symbol.Float(p[1])
            return
        
        if val.isdecimal():
            p[0]    = Symbol.Integer(p[1])
        elif val.replace('.', '', 1).isdigit() :
            p[0]    = Symbol.Float(p[1])

        return

    def p_line_indicator(self, p):
        """
        line_indicator : LINE INTEGER STRING
        """
        file        = p[3]
        lineno      = p[2]
        return

    def p_import(self, p):
        """
        import : IMPORT STRING
        """
        file        = p[2]
        return

    def p_error(self, p):
        if self.filename is not None:
            context = self.filename
        else:
            context = 'line'
            
        raise TypeError( f"{context}:{p.lexer.lineno} Unknown text at {p.value} [{p.type}]")
    
        
    def resolve(self, p, var):
        if len(self.definitions) == 0:
            return var
        
        token   = var
        for n in range(64):
            next    = self.definitions.get(token, None)
            if next is None:
                return token
            
            token     = next

        self.throw( p, f'Recursive definition in variable {var}' )

    def move(self, p, arg=None):
        if arg is None:
            arg = p [1]
        p[0]    = arg
        return
    
    def fold(self, p, offset):
        n   = len(p)
        match len(p):
            case 1:
                result    = []
            case 2:
                result    = [p[1]]
            case _:
                values  = p[1]
                values.append(p[offset])
                result  = values

        p[0]    = result
        return

    def fold_logic_expression(self, p, typename):
        n = len(p)
        match len(p):
            case 2:
                p[0]    = [('?', p[1])]
            case 4:
                lhs     = p[1]
                rhs     = p[3]
                if lhs is None:
                    lhs = []

                match p[2]:
                    case 'and':
                        self.append_expression( p, lhs, rhs, typename, 'AND')
                    case 'or':
                        self.append_expression( p, lhs, rhs, typename, 'OR')
                p[0]    = lhs
            case _:
                self.throw( p, f'Unexpected definition on {typename}' )
        return

    def append_expression(self, p, lhs:list, rhs, typename, operator):
        self.assert_fold_logic(p, lhs, typename, operator)
        lhs.append( (operator, rhs) )
        return

    def assert_fold_logic(self, p, expressions, typename, type):
        e       = expressions[-1]
        ltype   = e[0]

        if ltype in ['?', type]:
            return
        
        self.throw( p, f'Ambiguous logical expression using {type} in {typename}. Try using braces.' )
        return

    def to_map(self, pairmap, value):
        # Iterate through the definitions and add them to the list
        for d in value:
            name        = str(d[0])
            value       = d[1]
            if isinstance(value, SymbolType):
                value	= value.value
            elif isinstance(value, int) == True:
                value   = str(value)
            elif isinstance(value, float) == True:
                value   = str(value)
            elif isinstance(value) is not str:
                value   = str(value)
            pairmap[name] = value
        return
    
    def here(self, p):
        if self.filename is not None:
            context = self.filename
        else:
            context = 'line'
        return f'{context}:{p.lexer.lineno}'

    def throw(self, p, ex):
        raise RuntimeError( f'{self.here(p)} {ex}' )
    
    def trace(self, p):
        print(f'->{len(p)}:')
        if self.filename is not None:
            context = self.filename
        else:
            context = 'line'
        path    = []
        for i in range(1, len(p.stack)):
            value = p.stack[i].value
            if value is None:
                value   = 'None'

            path.append( str(value) )

        vars    = []
        for i in range(1, len(p)):
            vars.append(str(p[i]))

        print(f"{self.here(p)} \n  at `{' '.join(path)}`\n  expression=`{','.join(vars)}`")
        return
    
if __name__ == "__main__":
    parser = Parser()