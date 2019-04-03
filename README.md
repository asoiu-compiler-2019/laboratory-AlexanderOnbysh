Compiler
=============
Compiler is a very small C interpreter written in Python from scratch. Project was written as a part of course
Compiler Construction.

* [example1](example_1.c)
* [example2](example_2.c)

## Setup
**Prerequsite**:<br/>
    - Install [python3.7](https://www.python.org) or later, preferably use a virtualenv.<br/>

### Running interpreter
To execute c program, run `python3 __main__.py -f <file>`.

For example, to run the [example1](example1.c):
```bash
cd Compiler
python3 __main__.py -f example1.c
```

## EBNF
```
        program                     : declarations
        declarations                : (include_library | function_declaration | declaration_list)*
        include_library             : HASH ID<'include'> LESS_THAN ID DOT ID<'h'> GREATER_THAN
        function_declaration        : type_spec ID LPAREN parameters RPAREN compound_statement
        function_body               : LBRACKET (declaration_list | statement)* RBRACKET
        parameters                  : type_spec variable (COMMA type_spec variable)*
        declaration_list            : declaration+
        declaration                 : type_spec init_declarator_list SEMICOLON
        init_declarator_list        : init_declarator (COMMA init_declarator)*
        init_declarator             : variable (ASSIGN assignment_expression)?
        statement                   : iteration_statement
                                    | selection_statement
                                    | jump_statement
                                    | compound_statement
                                    | expression_statement
        compound_statement          : LBRACKET (declaration_list | statement)* RBRACKET
        jump_statement              : RETURN expression? SEMICOLON
                                    | BREAK SEMICOLON
                                    | CONTINUE SEMICOLON
        selection_statement         : IF LPAREN expression RPAREN statement (ELSE statement)?
        iteration_statement         : WHILE LPAREN expression RPAREN statement
                                    | DO statement WHILE LPAREN expression RPAREN SEMICOLON
                                    | FOR LPAREN expression_statement expression_statement (expression)? RPAREN statement
        expression_statement        : expression* SEMICOLON
        constant_expression         : conditional_expression
        expression                  : assignment_expression (COMMA assignment_expression)*
        assignment_expression       : assignment_expression (COMMA assignment_expression)*
                                    | conditional_expression
        conditional_expression      : logical_and_expression (QUESTION_MARK expression COLON conditional_expression)?
        logical_and_expression      : logical_or_expression (LOG_AND_OP logical_or_expression)*
        logical_or_expression       : inclusive_or_expression (LOG_OR_OP inclusive_or_expression)*
        inclusive_or_expression     : exclusive_or_expression (OR_OP exclusive_or_expression)*
        exclusive_or_expression     : and_expression (XOR_OP and_expression)*
        and_expression              : equality_expression (AND_OP equality_expression)*
        equality_expression         : relational_expression ((EQ_OP | NE_OP) relational_expression)*
        relational_expression       : shift_expression ((LE_OP | LT_OP | GE_OP | GT_OP) shift_expression)*
        shift_expression            : additive_expression ((LEFT_OP | RIGHT_OP) additive_expression)*
        additive_expression         : multiplicative_expression ((ADD_OP | SUB_OP) multiplicative_expression)*
        multiplicative_expression   : cast_expression ((MUL_OP | DIV_OP | MOD_OP) cast_expression)*
        cast_expression             : LPAREN type_spec RPAREN cast_expression
                                    | unary_expression
        unary_expression            : INC_OP unary_expression
                                    | DEC_OP unary_expression
                                    | AND_OP cast_expression
                                    | ADD_OP cast_expression
                                    | SUB_OP cast_expression
                                    | LOG_NEG cast_expression
                                    | postfix_expression
        unary_expression            : primary_expression INC_OP
                                    | primary_expression DEC_OP
                                    | primary_expression LPAREN argument_expression_list? RPAREN
        argument_expression_list    : assignment_expression (COMMA assignment_expression)*
        primary_expression          : LPAREN expression RPAREN
                                    | constant
                                    | string
                                    | variable
        constant                    : INTEGER_CONST
                                    | REAL_CONST
        type_spec                   : TYPE
        variable                    : ID
        string                      : STRING
```
