# ------------------------------------------------------------
# andorLex.py
# ------------------------------------------------------------
import ply.lex as lex
import sys

# ========================  Define global variables ======================
globalVars = {}
localVars = {}
varType = None
lastVar = None
scope = 'global'
funcType = None
nextFuncType = False
globalFuncs = {}
lastFunc = None
funcArgs = []

if sys.version_info[0] >= 3:
    raw_input = input

reserved = {
    'global': 'GLOBAL',
  	'principal': 'MAIN',
    'si': 'IF',
    'sino': 'ELSE',
    'entero': 'INT',
    'flotante': 'FLOAT',
  	'caracter': 'CHAR',
    'texto': 'STRING',
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

def  t_ID(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FCTE(t):
    r'-?[0-9]+\.[0-9][0-9]*'
    return t

def t_ICTE(t):
    r'-?[0-9]+'
    return t

def t_SCTE(t):
	r'\".*\"'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
file = open('prueba.txt','r')
lexer.input(file.read())

start = 'PROGRAMA'

# For using empty
def p_empty(p):
    '''empty : 
    '''
    pass
# listo
def p_PROGRAMA(p):
  '''PROGRAMA : PROGRAMAZ PROGRAMAB PRINCIPAL
  '''
# listo
def p_PROGRAMAB(p):
  '''PROGRAMAB  : FUNCION PROGRAMAB
                | empty
  '''
# listo
def p_PROGRAMAZ(p):
  '''PROGRAMAZ  : GLOBALES
                | empty
  '''
# listo
def p_GLOBALES(p):
  '''GLOBALES : GLOBAL GLOBALEZ END
  '''
def p_GLOBALEZ(p):
  '''GLOBALEZ : VART GLOBALEZ
              | empty
  '''
# listo
def p_VART(p):
  '''VART : DRAW ID EQUAL NEW DRAWI LPAR RPAR
  	      | DATA_TIPOS ID addVariable
  		  | ARR ID addVariable
  '''
# listo
def p_ESTATUTO(p):
  '''ESTATUTO : EXPRE
              | CONDICION
              | CICLO
              | ACCION
              | VART
              | LLAMADA_FUNCION
              | IMPRIMIR
  '''
# listo 
def p_BLOQUE(p):
  '''BLOQUE : ESTATUTO BLOQUE
            | empty
  '''
# listo
def p_DATA_TIPOS(p):
  '''DATA_TIPOS : INT addDataType
                | BOOLEAN addDataType
                | CHAR addDataType
                | STRING addDataType
                | FLOAT addDataType
                | VOID addDataType saveVoid
  '''
# listo 
def p_ASOP(p):
  '''ASOP : PLUS
          | MINUS
  '''
# listo
def p_MDOP(p):
  '''MDOP : MULT
          | DIVI
  '''
# listo
def p_ARR(p):
  '''ARR : DATA_TIPOS LBRA ICTE RBRA
  '''
# listo
def p_LLAMADA_FUNCION(p):
  '''LLAMADA_FUNCION : ID LPAR LLAMADA_FUNCIONP RPAR
  '''
# listo
def p_LLAMADA_FUNCIONP(p):
  '''LLAMADA_FUNCIONP : EXPRE LLAMADA_FUNCIONZ LLAMADA_FUNCIONP
                      | empty
  '''
# listo
def p_LLAMADA_FUNCIONZ(p):
  '''LLAMADA_FUNCIONZ : COMMA
                      | empty
  '''
# listo
def p_PRINCIPAL(p):
  '''PRINCIPAL : MAIN LPAR RPAR changeLocalScope BLOQUE END
  '''
  print('local vars: %s' % localVars)
  print('global vars: %s' % globalVars)
  print('functions: %s' % globalFuncs)
# listo
def p_CICLO(p):
  '''CICLO  : WHILEF
            | FORZ
  '''
# check
def p_WHILEF(p):
  '''WHILEF : WHILE LPAR EXPRE RPAR BLOQUE END
  '''
# listo
def p_FORZ(p):
  '''FORZ : FOR LPAR ICTE COMMA ICTE COMMA ICTE RPAR BLOQUE END
  '''
# listo
def p_CONDICION(p):
  '''CONDICION : IF LPAR EXPRE RPAR BLOQUE CONDICIONP END
  '''
def p_CONDICIONP(p):
  '''CONDICIONP : ELSE BLOQUE
                | empty
  '''
# listo
def p_RELOP(p):
  '''RELOP  : LESSTH 
            | GREATERTH
            | SEQUAL
            | NOTEQ
            | LESSEQTH
            | GREATEREQTH
  '''
# listo
def p_EXPRE(p):
  '''EXPRE : EXT EXPREZ
  '''
def p_EXPREZ(p):
  '''EXPREZ : EQUAL EXT
            | empty
  '''
def p_EXT(p):
  '''EXT  : EXP EXT_W_RELOP
  '''
def p_EXT_W_RELOP(p):
  '''EXT_W_RELOP  : RELOP EXT
        | empty
  '''
# listo
def p_EXP(p):
  '''EXP : TERMINO EXP_W_SIGN
  '''
# listo
def p_EXP_W_SIGN(p):
  '''EXP_W_SIGN : ASOP EXP
                | empty
  '''
# listo
def p_TERMINO(p):
  '''TERMINO : FAC TERMINO_W_SIGN
  '''
# listo
def p_TERMINO_W_SIGN(p):
  '''TERMINO_W_SIGN : MDOP TERMINO
                    | empty
  '''
# listo
def p_VAR_CTE(p):
  '''VAR_CTE  : ICTE
              | FCTE
  '''
# listo  
def p_IMPRIMIR(p):
  '''IMPRIMIR : PRINT LBRA IMPRIMIRZ RBRA
  '''
# listo
def p_IMPRIMIRZ(p):
  '''IMPRIMIRZ  : EXPRE 
                | SCTE
  '''
#listo
def p_FAC(p):
  '''FAC  : LPAR EXPRE RPAR
          | VAR_CTE 
          | LBRA EXPRE RPAR
          | ID FACT
  '''
  #listo
def p_FACT(p):
  '''FACT : LBRA EXPRE RBRA
          | LPAR EXPRE RPAR
          | empty
  '''
# listo
def p_FUNCION(p): 
  '''FUNCION : changeLocalScope DEFINE DATA_TIPOS ID saveFunc VAR_FUN BLOQUE RETURN EXPRE END changeGlobalScope
  '''
  global localVars
  global funcArgs
  addFunc(lastFunc, funcType, funcArgs)
  print('local vars function: %s' % localVars)
  localVars = {}
  funcArgs = []
# listo
def p_ACCION(p): 
  '''ACCION : ID POINT DIBUJA LPAR VAR_CTE RPAR
  '''
# listo
def p_VAR_FUN(p): 
  ''' VAR_FUN : LPAR VAR_FUNP RPAR
  '''
# listo
def p_VAR_FUNP(p): 
  '''VAR_FUNP : DATA_TIPOS ID addArg VAR_FUNZ
              | empty
  '''
# listo
def p_VAR_FUNZ(p): 
  '''VAR_FUNZ : COMMA VAR_FUNP
              | empty
  '''
# listo
def p_DIBUJA(p):
  '''DIBUJA : DEFINIRPOSICION
            | DEFINIRCOLOR
            | DERECHO
            | REVERSA
            | IZQUIERDA
            | DERECHA
            | VELOCIDAD
            | BORRAR
            | MOSTRAR
            | OCULTAR
            | CIRCULO
            | DEFINIRX
            | DEFINIRY
            | ARCO
            | GROSOR
  '''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)

# ==================    PUNTOS NEURALES ======================
typesValues = {
		'entero':0,
		'flotante':1,
		'texto':2,
		'caracter':3,
        'booleano':4,
        'vacio':5,
}

def p_changeGlobalScope(p):
    '''changeGlobalScope  :   empty
    '''
    global scope
    scope = 'global'

def p_changeLocalScope(p):
    '''changeLocalScope  :   empty
    '''
    global scope
    scope = 'local'

def p_addDataType(p):
    ''' addDataType :   empty
    '''
    global varType
    global nextFuncType
    global funcType
    if nextFuncType:
        funcType = typesValues[p[-1]]
    else:
        varType = typesValues[p[-1]]
    nextFuncType = False

def p_addVariable(p):
    '''addVariable  :   
    '''
    global lastVar
    lastVar = p[-1]
    nameVar = lastVar
    addVarAndType(nameVar, varType)

def p_saveVoid(p):
    '''saveVoid :   
    '''
    global funcType
    funcType = typesValues['vacio']
    print('void func saved, func type: %s' % funcType)

def p_saveFunc(p):
    '''saveFunc :   
    '''
    global lastFunc
    lastFunc = p[-1]

def p_addArg(p):
    '''addArg   :   
    '''
    global lastVar
    global funcArgs
    lastVar = p[-1]
    varName = lastVar
    addVarAndType(varName, varType)
    funcArgs.append(localVars[varName])

import ply.yacc as yacc
parser = yacc.yacc()
import pprint
pp = pprint.PrettyPrinter(indent=4)

def addVarAndType(var, vType):
    global globalVars
    global localVars

    if scope == 'local':
        if not var in localVars.keys():
            localVars[var] = {'name':var, 'type':vType}
        else:
            print('Var already declared in local scope!')
    else:
        if not var in globalVars.keys():
            globalVars[var] = {'name':var, 'type':vType}
        else:
            print('Var already declared in global scope!')

def addFunc(name, fType, params):
    global globalFuncs
    if not name in globalFuncs.keys():
        globalFuncs[name] = {'name':name, 'type':fType, 'parameters':params}
        print('Func name: %s and type: %s' % (name, fType))
    else:
        print('Function already declared before!')

with open('prueba.txt','r') as f:
         input = f.read()
         pp.pprint(parser.parse(input))