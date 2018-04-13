import ply.lex as lex

reserved = {
    'global': 'GLOBAL',
    'principal': 'MAIN',
    'si': 'IF',
    'sino': 'ELSE',
    'entero': 'INT',
    'flotante': 'FLOAT',
    'caracter': 'STRING',
    'booleano': 'BOOLEAN',
    'vacio': 'VOID',
    'no' : 'NOT',
    'fin': 'END',
    'imprimir' : 'PRINT',
    'defino' : 'DEFINE',
    'mientrast' : 'WHILE',
    'mientras' : 'FOR',
    'regresa' : 'RETURN',
    'verdadero' : 'TRUE',
    'falso' : 'FALSE',
    'dibujo' : 'DRAW',
    'Dibujo' : 'DRAWI',
    'nuevo' : 'NEW',
    'id' : 'ID', 
  
    # Functions
    'definirPosicion' : 'DEFINIRPOSICION',
    'definirColor' : 'DEFINIRCOLOR',
    'derecho' : 'DERECHO',
    'reversa' : 'REVERSA',
    'izquierda': 'IZQUIERDA',
    'derecha' : 'DERECHA',
    'velocidad' : 'VELOCIDAD',
    'borrar' : 'BORRAR',
    'mostrar' : 'MOSTRAR',
    'ocultar' : 'OCULTAR',
    'circulo': 'CIRCULO',
    'definirX' : 'DEFINIRX',
    'definirY' : 'DEFINIRY',
    'arco': 'ARCO',
    'grosor' : 'GROSOR'
}
# List of token names.
tokens = list(reserved.values()) + [
  'EQUAL',
  'SEQUAL',
  'LPAR',
  'RPAR',
  'LBRA',
  'RBRA',
  'AND',
  'OR',
  'LESSTH',
  'GREATERTH',
  'NOTEQ',
  'LESSEQTH',
  'GREATEREQTH',
  'PLUS',
  'MINUS',
  'MULT',
  'DIVI',
  'POINT',
  'COMMA',
  'ICTE',
  'FCTE',
  'SCTE'
]

# Regular expressions for each token
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIVI = r'/'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRA = r'\['
t_RBRA = r'\]'
t_OR = r'\|\|'
t_AND = r'&&'
t_POINT = r'\.'
t_COMMA = r'\,'
t_GREATERTH = r'\>'
t_LESSTH = r'\<'
t_GREATEREQTH = r'\>='
t_LESSEQTH = r'\<='
t_SEQUAL = r'\=='
t_NOTEQ = r'\!='
t_EQUAL = r'\='

t_ignore = " \t"

#Regular expression that returns an ID.
def  t_ID(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    tokens.append(t)
    return t
# Get all the comments that start with #.
def t_COMMENT(t):
    r'\#.*'
    pass
# Regular expression for floats.
def t_FCTE(t):
    r'-?[0-9]+\.[0-9][0-9]*'
    tokens.append(t)
    return t
# Regular expression for integers.
def t_ICTE(t):
    r'-?[0-9]+'
    tokens.append(t)
    return t
# Regular expression for string.
def t_SCTE(t):
  r'\".*\"'
# Returns a new line.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# Prints an error.
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Find Column
def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return 
    
# Build the lexer
lexer = lex.lex()
