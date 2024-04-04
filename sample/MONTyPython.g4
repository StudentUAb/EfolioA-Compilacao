grammar MONTyPython;

// Tokens adicionais para tipos e palavras-chave
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
LIST_TYPE: 'list';
FOR: 'for';
WHILE: 'while';
IF: 'if';
ELSE: 'else';
LBRACE: '{';
RBRACE: '}';
PRINT: 'print';

// Definições léxicas
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';
SEMI: ';';
WHITESPACE: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;

// Definições sintáticas
program: (statement)+;

statement: varDeclaration
         | assignment
         | forLoop
         | whileLoop
         | ifStatement
         | functionDeclaration
         | printStatement;

varDeclaration: (INT_TYPE | FLOAT_TYPE) ID (ASSIGN expression)? SEMI;

assignment: ID ASSIGN expression SEMI;

expression: expression (PLUS | MINUS) expression
          | expression (STAR | SLASH) expression
          | INT
          | FLOAT
          | ID
          | LPAREN expression RPAREN
          | LBRACK expression? RBRACK;
          

forLoop: FOR LPAREN assignment expression SEMI expression RPAREN LBRACE (statement)* RBRACE;

whileLoop: WHILE LPAREN expression RPAREN LBRACE (statement)* RBRACE;

ifStatement: IF LPAREN expression RPAREN LBRACE (statement)* RBRACE (ELSE LBRACE (statement)* RBRACE)?;

functionDeclaration: (INT_TYPE | FLOAT_TYPE | LIST_TYPE) ID LPAREN params? RPAREN LBRACE (statement)* RBRACE;

params: param (COMMA param)*;
param: (INT_TYPE | FLOAT_TYPE) ID;

printStatement: PRINT LPAREN expression RPAREN SEMI;

