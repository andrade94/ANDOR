# ------------------------------------------------------------
# andorLex.py
# ------------------------------------------------------------
import ply.yacc as yacc

# Get semantic variables
import m_semantic as sem

# Parsing state module
import m_st as state

# Get tokens from the lexer
from m_lexer import tokens
# Get the lexer
from m_lexer import lexer
from m_lexer import find_column

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
                | FUNCIONV PROGRAMAB
                | empty
  '''
# listo
def p_PROGRAMAZ(p):
  '''PROGRAMAZ  : GLOBAL GLOBALEZ END
                | empty
  '''
def p_GLOBALEZ(p):
  '''GLOBALEZ : VARTG GLOBALEZ
              | empty
  '''
def p_VARTG(p):
  '''VARTG : DATA_TIPOS ID VARZ seenVariable
  '''
def p_VARTL(p):
  '''VARTL : DATA_TIPOS ID VARZ seenVariable
  '''
def p_VARZ(p):
  '''VARZ : ARRDIM
          | empty
  '''
  p[0] = p[1]

def p_ARRDIM(p):
  '''ARRDIM : LBRA ICTE RBRA
  '''
  p[0] = p[2]
  #  DRAW ID addVariable EQUAL NEW DRAWI LPAR RPAR
# listo
def p_ESTATUTO(p):
  '''ESTATUTO : EXPRE
              | CONDICION
              | CICLO
              | ACCION
              | VARTL
              | IMPRIMIR
              | LEER
              | CALL
  '''
# listo 
def p_BLOQUE(p):
  '''BLOQUE : ESTATUTO BLOQUE
            | empty
  '''
# listo
def p_DATA_TIPOS(p):
  '''DATA_TIPOS : INT
                | BOOLEAN
                | STRING
                | FLOAT
                | VOID
  '''
  p[0] = p[1]
def p_PRINCIPAL(p):
  '''PRINCIPAL : MAIN LPAR RPAR BLOQUE END
  '''

# listo
def p_CICLO(p):
  '''CICLO  : WHILEF
  '''
# check
def p_WHILEF(p):
  '''WHILEF : WHILE LPAR EXPRE RPAR BLOQUE END
  '''
# listo
def p_CONDICION(p):
  '''CONDICION : IF LPAR EXT RPAR BLOQUE CONDICIONP END
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
  p[0] = p[1]
# listo 
def p_ASOP(p):
  '''ASOP : PLUS
          | MINUS
  '''
  p[0] = p[1]
# listo
def p_MDOP(p):
  '''MDOP : MULT
          | DIVI
  '''
  p[0] = p[1]
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
  p[0] = p[1]

def p_EXT_W_RELOP(p):
  '''EXT_W_RELOP  : RELOP EXT
        | empty
  '''
# listo
def p_EXP(p):
  '''EXP : TERMINO EXP_W_SIGN
  '''
  p[0] = p[1]
# listo
def p_EXP_W_SIGN(p):
  '''EXP_W_SIGN : ASOP EXP
                | empty
  '''
# listo
def p_TERMINO(p):
  '''TERMINO : FAC TERMINO_W_SIGN
  '''
  p[0] = p[1]
# listo
def p_TERMINO_W_SIGN(p):
  '''TERMINO_W_SIGN : MDOP TERMINO
                    | empty
  '''
# listo
def p_VAR_CTE(p):
  '''VAR_CTE  : ICTE
              | FCTE
              | SCTE
              | TRUE
              | FALSE
  '''
  p[0] = p[1]
# listo  
def p_IMPRIMIR(p):
  '''IMPRIMIR : PRINT LPAR ARGSIMP RPAR
  '''
#listo
def p_ARGSIMP(p):
  '''ARGSIMP  : EXP ARGSIMPX
              | SCTE ARGSIMPX
  '''
def p_ARGSIMPX(p):
  '''ARGSIMPX : COMMA ARGSIMP
              | empty
  '''
def p_LEER(p):
  '''LEER : READ LPAR DATA_TIPOS COMMA ID RPAR
  '''
#listo
def p_FAC(p):
  '''FAC  : FACAUX
          | FACAUX2
          | CALL
          | ARRAY
          | ID
  '''
  p[0] = p[1]

def p_FACAUX(p):
  '''FACAUX : LPAR EXP RPAR
  '''
  p[0] = p[2]

def p_FACAUX2(p):
  '''FACAUX2 : VAR_CTE
  '''
  p[0] = p[1]

def p_CALL(p):
  '''CALL : ID LPAR PRMS RPAR
  '''
  p[0] = p[1]
def p_ARRAY(p):
  '''ARRAY : ID LBRA EXP RBRA
  '''
  p[0] = p[1]
#listo
def p_PRMS(p):
  '''PRMS   :   PRMC
            |   empty
  '''
  p[0] = p[1]
#listo
def p_PRMC(p):
  '''PRMC   :  EXP PRMSZ
  '''
  p[0] = p[1]

#listo
def p_PRMSZ(p):
  '''PRMSZ   :  COMMA PRMC
              | empty
  '''

# listo
def p_FUNCION(p): 
  '''FUNCION : DEFINE DATA_TIPOS ID VAR_FUN seenFunction BLOQUE FUNCIONRN END
  '''
  # sem.redeclaredFunction(p[3])
# listo
def p_FUNCIONV(p): 
  '''FUNCIONV : DEFINE VOID ID VAR_FUN seenFunction BLOQUE FUNCIONRV END
  '''

def p_FUNCIONRV(p):
    '''FUNCIONRV : RETURN
    '''

def p_FUNCIONRN(p):
    '''FUNCIONRN : RETURN EXP
    '''
# listo
def p_VAR_FUN(p): 
  '''VAR_FUN : LPAR VAR_FUNC RPAR
  '''
def p_VAR_FUNC(p):
  '''VAR_FUNC : VAR_FUNP
              | empty
  '''
# listo
def p_VAR_FUNP(p): 
  '''VAR_FUNP : PARAMS VAR_FUNZ
  '''
def p_PARAMS(p):
  '''PARAMS : DATA_TIPOS ID ARR2 seenVariable updateSize
  '''
def p_ARR2(p):
  '''ARR2 : LBRA RBRA
          | empty
  '''
  p[0] = p[1]
# listo
def p_VAR_FUNZ(p): 
  '''VAR_FUNZ : COMMA VAR_FUNP
              | empty
  '''
# listo
def p_ACCION(p): 
  '''ACCION : ID POINT DIBUJA LPAR VAR_CTE RPAR
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
  
def p_seenFunction(p):
    '''seenFunction  :   empty
    '''
    sem.fill_symbol_table_function(p[-2], [p[-3], state.signature])
    state.signature = []

def p_updateSize(p):
    '''updateSize : '''
    state.signature.append(p[-1])

def p_seenVariable(p):
    '''seenVariable : '''
    type = p[-3]
    if(p[-1] != None):
        type += "[]"
    p[0] = type

# Error rule for syntax errors
def p_error(p):
    if(p):
        raise NameError("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(lexer.lexdata, p), p.value))
    else:
        raise NameError("Abrupt file termination")

# ==================    PUNTOS NEURALES ======================
parser = yacc.yacc(tabmodule="preparser")