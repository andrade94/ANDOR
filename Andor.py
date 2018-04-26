# ------------------------------------------------------------
# andorLex.py
# ------------------------------------------------------------
import ply.yacc as yacc
import sys
# Import tokens from lexer
from m_lexer import tokens
# Import lexer to parse.
from m_lexer import lexer
# Import utility.
from m_lexer import find_column
import m_semantic as sem
import m_st as state
import m_expr as expr
import m_rd_wrt as rw
import m_if_wh as il
# ========================  Define global variables ======================

# globalVars = {}
# localVars = {}
# varType = None
# lastVar = None
# funcType = None
# nextFuncType = False
# globalFuncs = {}
# lastFunc = None
# funcArgs = []
isPrint = False
# Build the lexer
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
                | FUNCIONV PROGRAMAB
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
  '''VART : DATA_TIPOS ID VARZ addVariable
  '''

def p_VARZ(p):
  '''VARZ : LBRA ICTE RBRA
          | empty
  '''
  p[0] = p[1]
  #  DRAW ID addVariable EQUAL NEW DRAWI LPAR RPAR
# listo
def p_ESTATUTO(p):
  '''ESTATUTO : EXPRE genQuad5
              | CONDICION
              | CICLO
              | ACCION
              | VART
              | LLAMADA_FUNCION
              | IMPRIMIR
              | LEER
  '''
# listo 
def p_BLOQUE(p):
  '''BLOQUE : ESTATUTO finishBlock BLOQUE
            | empty
  '''
# listo
def p_DATA_TIPOS(p):
  '''DATA_TIPOS : INT addDataType
                | BOOLEAN addDataType
                | STRING addDataType
                | FLOAT addDataType
                | VOID addDataType
  '''
  p[0] = p[1]
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
  '''PRINCIPAL : MAIN changeScope LPAR RPAR BLOQUE END
  '''

# listo
def p_CICLO(p):
  '''CICLO  : WHILEF
  '''
# check
def p_WHILEF(p):
  '''WHILEF : WHILE LPAR saveLabel EXPRE RPAR pushLabelS BLOQUE goValidate popLabelS END
  '''
# listo
def p_CONDICION(p):
  '''CONDICION : IF LPAR EXT RPAR pushLabelS BLOQUE CONDICIONP END
  '''
def p_CONDICIONP(p):
  '''CONDICIONP : ELSE pushElse popLabelS BLOQUE popLabelS
                | popLabelS empty
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
  '''EXPREZ : EQUAL operatorPush EXT
            | empty
  '''
def p_EXT(p):
  '''EXT  : EXP EXT_W_RELOP genQuad3
  '''
  p[0] = p[1]

def p_EXT_W_RELOP(p):
  '''EXT_W_RELOP  : RELOP operatorPush EXT
        | empty
  '''
# listo
def p_EXP(p):
  '''EXP : TERMINO genQuad2 EXP_W_SIGN
  '''
  p[0] = p[1]
# listo
def p_EXP_W_SIGN(p):
  '''EXP_W_SIGN : ASOP operatorPush EXP
                | empty
  '''
# listo
def p_TERMINO(p):
  '''TERMINO : FAC genQuad1 TERMINO_W_SIGN
  '''
  p[0] = p[1]
# listo
def p_TERMINO_W_SIGN(p):
  '''TERMINO_W_SIGN : MDOP operatorPush TERMINO
                    | empty
  '''
# listo
def p_VAR_CTE(p):
  '''VAR_CTE  : ICTE addInt
              | FCTE addFloat
              | SCTE addString
              | TRUE addBooleano
              | FALSE addBooleano
  '''
  p[0] = p[1]
# listo  
def p_IMPRIMIR(p):
  '''IMPRIMIR : PRINT LPAR isOnPrint EXT generatePrint RPAR
  '''
#listo
def p_LEER(p):
  '''LEER : READ LPAR DATA_TIPOS COMMA ID generateRead RPAR
  '''
#listo
def p_FAC(p):
  '''FAC  : pushExp LPAR EXPRE RPAR popExp
          | genQuad0 VAR_CTE operandPush
          | LBRA EXPRE RPAR
          | ID operandPush FACT
  '''
  #listo
def p_FACT(p):
  '''FACT : LBRA EXT RBRA
          | LPAR PRMS RPAR
          | empty
  '''

#listo
def p_PRMS(p):
  '''PRMS   :  EXT PRMSZ
  '''

#listo
def p_PRMSZ(p):
  '''PRMSZ   :  COMMA PRMS
              | empty
  '''

# listo
def p_FUNCION(p): 
  '''FUNCION : DEFINE DATA_TIPOS ID changeScope VAR_FUN seenFunction BLOQUE RETURN EXPRE END restoreScope
  '''
  # sem.redeclaredFunction(p[3])
# listo
def p_FUNCIONV(p): 
  '''FUNCIONV : DEFINE VOID ID changeScope VAR_FUN seenFunction BLOQUE RETURN EXPRE END restoreScope
  '''

def p_ACCION(p): 
  '''ACCION : ID POINT DIBUJA LPAR VAR_CTE RPAR
  '''
# listo
def p_VAR_FUN(p): 
  '''VAR_FUN : LPAR VAR_FUNP RPAR
  '''
# listo
def p_VAR_FUNP(p): 
  '''VAR_FUNP : DATA_TIPOS ID VAR_FUNX addVariable updateSize VAR_FUNZ
              | empty
  '''

def p_VAR_FUNX(p):
  '''VAR_FUNX : LBRA RBRA
              | empty
  '''
  p[0] = p[1]
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

# Error rule for syntax errors
def p_error(p):
    if(p):
        raise NameError("Syntax error at line {0} col {1}, unexpected '{2}'".format(p.lineno, find_column(lexer.lexdata, p), p.value))
    else:
        raise NameError("Abrupt file termination")

# ==================    PUNTOS NEURALES ======================

# Scopes
def p_restoreScope(p):
    '''restoreScope  :   empty
    '''
    sem.scope = 'global'

def p_changeScope(p):
    '''changeScope  :   empty
    '''
    sem.scope = p[-1]
    sem.validate_redeclaration_function(p[-1])
# Read
def p_generateRead(p):
    '''generateRead  :   empty
    '''
    # print(p[-3],p[-1])
    rw.read_quad(p[-3], p[-1], sem.scope)
# Print
def p_generatePrint(p):
    '''generatePrint  :   empty
    '''
    # global isPrint
    # for e in state.params_list
    #   rw.print_quad(e)
    # state.params_list = []
    # isPrint = False

def p_isOnPrint(p):
  '''isOnPrint  :   empty
  '''
  global isPrint
  isPrint = True
# Data types
def p_addDataType(p):
    ''' addDataType :  empty
    '''

def p_addVariable(p):
    '''addVariable  :   empty 
    '''
    type = p[-3]
    if(p[-1] != None):
        type += "[]"
    sem.fill_symbol_table_variable(p[-2],type)
    p[0] = type

def p_addFloat(p):
    '''addFloat  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1],"flotante")

def p_addInt(p):
    '''addInt  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1],"entero")

def p_addString(p):
    '''addString  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1],"caracter")

def p_addBooleano(p):
    '''addBooleano  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1],"booleano")

def p_blockFinish(p):
    '''finishBlock  :   empty
    '''
    # expr.clear_stacks()
    pass
# Function functions
def p_seenFunction(p):
    '''seenFunction  :   empty
    '''
    sem.fill_symbol_table_function(p[-3],[p[-4], sem.get_signature(), sem.get_function_size()])
    sem.clear_signature()
    sem.clear_function_size

def p_updateSize(p):
    '''updateSize  :   empty
    '''
    sem.update_signature(p[-1])
    sem.update_function_size(p[-1])

# conditions
def p_pushLabelS(p):
    '''pushLabelS  :   empty
    '''
    state.label_stack.append(state.label)
    il.generate_if_goto_F(state.operand_stack.pop())

def p_popLabelS(p):
    '''popLabelS  :   empty
    '''
    il.put_label_to_goto_F(state.label_stack.pop())

def p_pushElse(p):
    '''pushElse  :   empty
    '''
    temp = state.label_stack.pop()
    state.label_stack.append(state.label)
    state.label_stack.append(temp)
    il.generate_else_goto()

# Loops
def p_saveLabel(p):
	'''saveLabel  :  empty
  '''
	state.label_stack.append(state.label)
	
def p_goValidate(p):
	'''goValidate :  empty
  '''
	temp = state.label_stack.pop()
	il.generate_loop_goto(state.label_stack.pop())
	state.label_stack.append(temp)

# Math rules
def p_operandPush(p):
    '''operandPush  :   empty   
    '''
    if(sem.is_declared(p[-1])):
      expr.add_operand(sem.get_variable(p[-1]))
    
def p_operatorPush(p):
    '''operatorPush   :   empty 
    '''
    expr.add_operator(p[-1])
    p[0] = p[-1]
    
def p_pushExp(p):
    '''pushExp   :   empty 
    '''
    expr.push_expr()
    
def p_popExp(p):
    '''popExp   :    empty 
    '''
    expr.pop_expr()
    
def p_genQuad0(p):
    '''genQuad0   :    empty 
    '''

def p_genQuad1(p):
    '''genQuad1  :    empty   
    '''
    expr.generate_quad(1)
    
def p_genQuad2(p):
    '''genQuad2  :    empty 
    '''
    expr.generate_quad(2)

def p_genQuad3(p):
    '''genQuad3  :    empty 
    '''
    expr.generate_quad(3)
    
def p_genQuad5(p):
    '''genQuad5   :    empty 
    '''
    expr.generate_quad(5)

parser = yacc.yacc()
import pprint
pp = pprint.PrettyPrinter(indent=4)

# def addVarAndType(var, vType):
#     global globalVars
#     global localVars

#     if sem.scope == 'local':
#         if not var in localVars.keys():
#             localVars[var] = {'name':var, 'type':vType}
#         else:
#             print('Var already declared in local scope!')
#     else:
#         if not var in globalVars.keys():
#             globalVars[var] = {'name':var, 'type':vType}
#         else:
#             print('Var already declared in global scope!')

# def addFunc(name, fType, params):
#     global globalFuncs
#     if not name in globalFuncs.keys():
#         globalFuncs[name] = {'name':name, 'type':fType, 'parameters':params}
#         print('Func name: %s and type: %s' % (name, fType))
#     else:
#         print('Function already declared before!')

with open('prueba.txt','r') as f:
    input = f.read()
    pp.pprint(parser.parse(input))
    var_table = sem.var_table
    func_table = sem.func_table
    for idx, quad in enumerate(state.quads):
      print idx + 1, (quad.operator, quad.operand1, quad.operand2, quad.result)
    # print "Scope\t|Id\t|Type"
    # print "--------|-------|--------"
    # for k in var_table:
    #     sys.stdout.write(k)
    #     for k1 in var_table[k]:
    #         print("\t|" + str(k1) + "\t|" + var_table[k][k1][0])
    #     print "--------|-------|--------"
    # print "--------|-------|--------"
    # for k in func_table:
    #     sys.stdout.write(k)
    #     for k1 in var_table[k]:
    #         print("\t|" + str(k1) + "\t|" + var_table[k][k1][0])
    #     print "--------|-------|--------"