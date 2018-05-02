# ------------------------------------------------------------
# andorLex.py
# ------------------------------------------------------------
import ply.yacc as yacc
import sys
import m_andor_f as func_parser
# Import tokens from lexer
from m_lexer import tokens
# Module to serialize objects
import cPickle as pickle
# Import lexer to parse.
from m_lexer import lexer
# Import utility.
from m_lexer import find_column
import m_semantic as sem
import m_st as state
import m_expr as expr
import m_rd_wrt as rw
import m_if_wh as il
import m_fun as func
import m_main as main
import m_vm as vm
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
  '''PROGRAMA : seenProgram PROGRAMAZ PROGRAMAB PRINCIPAL programEnd
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
  '''VARTG : DATA_TIPOS ID VARTG2
  '''
def p_VARTG2(p):
  '''VARTG2   : VARZ seenGlobalV
              | addReturnFunction changeScope VAR_FUN BLOQUE FUNCIONRN addReturnFunctionEnd restoreScope
  '''
def p_seenGlobalV(p):
  '''seenGlobalV : empty
  '''
  type = p[-3]
  d1 = 1
  if(p[-1] != None):
      type += "[]"
      d1 = p[-1]
  if(type[0] == "e" or type[0] == "f"):
      size = 4
  else:
      size = 1
  sem.fill_global_variables_table(p[-2], type, d1 * size)
  p[0] = type
# listo
def p_VARTL(p):
  '''VARTL : DATA_TIPOS ID VARZ seenLocalV updateSize
  '''
def p_seenLocalV(p):
  '''seenLocalV : empty
  '''
  type = p[-3]
  d1 = 1
  if(p[-1] != None):
      type += "[]"
      d1 = p[-1]
  if(type[0] == "e" or type[0] == "f"):
      size = 4
  else:
      size = 1
  sem.fill_local_variables_table(p[-2], type, d1 * size)
  p[0] = type

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
  '''ESTATUTO : EXPRE genQuad5
              | CONDICION
              | CICLO
              | ACCION
              | VARTL
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
def p_PRINCIPAL(p):
  '''PRINCIPAL : MAIN changeScope seenMain LPAR RPAR BLOQUE END
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
  '''VAR_CTE  : VAR_CTE2
              | SCTE addString
              | TRUE addBooleano
              | FALSE addBooleano
  '''
  p[0] = p[1]

def p_VAR_CTE2(p):
  '''VAR_CTE2   : W_SIGN addSign ICTE addInt genQuad0
                | W_SIGN addSign FCTE addFloat genQuad0
  '''
  p[0] = p[3]

def p_W_SIGN(p):
  '''W_SIGN   : PLUS
              | MINUS
              | empty
  '''
  p[0] = p[1]

def p_addSign(p):
  '''addSign   :  empty
  '''
  expr.add_operator("s" + str(p[-1]))
  p[0] = p[-1]
# listo  
def p_IMPRIMIR(p):
  '''IMPRIMIR : PRINT LPAR ARGSIMP RPAR
  '''
#listo
def p_ARGSIMP(p):
  '''ARGSIMP  : EXP generatePrint ARGSIMPX
              | SCTE generatePrint ARGSIMPX
  '''
def p_ARGSIMPX(p):
  '''ARGSIMPX : COMMA ARGSIMP
              | empty
  '''
def p_LEER(p):
  '''LEER : READ LPAR DATA_TIPOS COMMA ID generateRead RPAR
  '''
#listo
def p_FAC(p):
  '''FAC  : FACAUX
          | FACAUX2
          | CALL
          | ARRAY
          | ID operandPush
  '''
  p[0] = p[1]

def p_FACAUX(p):
  '''FACAUX : LPAR pushExp EXP RPAR popExp
  '''
  p[0] = p[3]

def p_FACAUX2(p):
  '''FACAUX2 : genQuad0 VAR_CTE operandPush
  '''
  p[0] = p[2]

def p_CALL(p):
  '''CALL : ID LPAR addCall PRMS RPAR checkSignature endCall
  '''
  p[0] = p[1]

def p_checkSignature(p):
  '''checkSignature : empty
  '''
  sem.is_signature_valid(p[-5], state.signature)
def p_addCall(p):
  '''addCall : empty
  '''
  expr.add_operator("#")
  state.return_dir_stack.append(state.temp_dir)
  func_name = p[-2]
  type = sem.func_table[func_name][0][0]  # [[primitive, dir, size, scope], dir, size]
  if(type != "vacio"):  # Function has a return value
      if(type[0] == "e" or type[0] == "f"):
          size = 4
      else:
          size = 1
      # Creates a temporal to save return value
      func.generate_era(func_name, [func_name, [type, state.temp_dir, size, 't']])
      state.temp_dir += size
  else:
      func.generate_era(func_name, None)
def p_endCall(p):
  '''endCall : empty
  '''
  state.operator_stack.pop()
  func.generate_gosub(p[-6])
  state.reset_call()
def p_addParamCall(p):
  '''addParamCall : empty
  '''
  param = state.operand_stack.pop()
  func.generate_param(param)
  state.signature.append(param[1][0])
  
def p_ARRAY(p):
  '''ARRAY : ID operandPush LBRA EXP RBRA
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
  '''PRMC   :  EXP addParamCall PRMSZ
  '''
  p[0] = p[1]

#listo
def p_PRMSZ(p):
  '''PRMSZ   :  COMMA PRMC
              | empty
  '''

# listo
def p_FUNCION(p): 
  '''FUNCION : DEFINE DATA_TIPOS ID seenFunction changeScope VAR_FUN BLOQUE FUNCIONRN END functionEnd restoreScope
  '''
  # sem.redeclaredFunction(p[3])
# listo
def p_FUNCIONV(p): 
  '''FUNCIONV : DEFINE VOID ID addReturnFunction changeScope VAR_FUN BLOQUE FUNCIONRV END addReturnFunctionEnd restoreScope
  '''

def p_FUNCIONRV(p):
    '''FUNCIONRV : RETURN
    '''

def p_FUNCIONRN(p):
    '''FUNCIONRN : RETURN EXP
    '''

def p_seenFunction(p):
    '''seenFunction  :   empty
    '''
    state.local_dir = 0
    sem.func_table[p[-1]].append(len(state.quads))

def p_addReturnFunction(p):
    '''addReturnFunction  :   empty
    '''
    state.local_dir = 0
    #state.return_dir_stack.append(state.temp_dir)
    sem.func_table[p[-1]].append(len(state.quads))
def p_addReturnFunctionEnd(p):
    '''addReturnFunctionEnd  :   empty
    '''
    func_name = p[-7]
    return_var = state.operand_stack.pop()
    func.generate_return(func_name, return_var)
    func.generate_end(func_name)
    sem.func_table[func_name].append(state.f_size)
    sem.func_table[func_name][0] = return_var[1]
    #state.return_dir_stack.pop()
    #state.return_var_stack.pop()
    state.f_size = 0
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
  '''PARAMS : DATA_TIPOS ID ARR2 seenLocalV updateSize
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
    sem.scope = "global"
    #addresses = state.address_stack.pop()
    #state.global_dir = addresses[0]
    #state.constant_dir = addresses[1]
    #state.local_dir = addresses[2]
    #state.temp_dir = addresses[3]

def p_changeScope(p):
    '''changeScope  :   empty
    '''
    sem.scope = p[-2]
    sem.validate_redeclaration_function(p[-2])
    #state.address_stack.append([state.global_dir, state.constant_dir, state.local_dir, state.temp_dir])
    state.temp_counter = 0
    state.temp_dir = 0
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
    if(isinstance(p[-1], str) and p[-1][0] == '"'):
      param = p[-1]
    else:
      param = state.operand_stack.pop()
    rw.print_quad(param)

# Data types
def p_addDataType(p):
    ''' addDataType :  empty
    '''
def p_addFloat(p):
    '''addFloat  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1], "flotante", 4)

def p_addInt(p):
    '''addInt  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1], "entero", 4)

def p_addString(p):
    '''addString  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1], "caracter", 1)

def p_addBooleano(p):
    '''addBooleano  :   empty 
    '''
    sem.fill_symbol_table_constant(p[-1], "booleano", 1)

def p_blockFinish(p):
    '''finishBlock  :   empty
    '''
    # expr.clear_stacks()
    pass
# Function functions

def p_updateSize(p):
    '''updateSize  :   empty
    '''
    d1 = 1
    if(p[-2] != None):
      d1 = p[-2]
    type = p[-1]
    if(type[0] == "e" or type[0] == "f"):
        state.f_size += 4 * d1
    else:
        state.f_size += 1 * d1

def p_seenMain(p):
    '''seenMain   :   empty
    '''
    main.update_goto(len(state.quads) + 1)

def p_seenProgram(p):
    '''seenProgram  :   empty
    '''
    main.generate_main()

def p_programEnd(p):
    '''programEnd  :   empty
    '''
    func.generate_end("main")

def p_functionEnd(p):
    '''functionEnd  :   empty
    '''
    func.generate_end(p[-7])
    sem.func_table[p[-7]].append(state.f_size)
    state.f_size = 0

# conditions
def p_pushLabelS(p):
    '''pushLabelS  :   empty
    '''
    state.label_stack.append(len(state.quads))
    il.generate_if_goto_f(state.operand_stack.pop())

def p_popLabelS(p):
    '''popLabelS  :   empty
    '''
    il.put_label_to_goto_f(state.label_stack.pop())

def p_pushElse(p):
    '''pushElse  :   empty
    '''
    temp = state.label_stack.pop()
    state.label_stack.append(len(state.quads))
    state.label_stack.append(temp)
    il.generate_else_goto()

# Loops
def p_saveLabel(p):
	'''saveLabel  :  empty
  '''
	state.label_stack.append(len(state.quads)-1)
	
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
    expr.generate_quad(0)

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

f_parser = func_parser.parser
parser = yacc.yacc()
import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('prueba.txt','r') as f:
    input = f.read()
    preparsing = f_parser.parse(input, 0, 0)
    result = parser.parse(input, 0, 0)
    var_table = sem.var_table
    func_table = sem.func_table
    # for idx, quad in enumerate(state.quads):
        # print idx + 1, (quad.operator, quad.operand1, quad.operand2, quad.result)
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
    # print(state.quads)

def add_offset(lst, g_offset, c_offset, l_offset):
    if(lst[3] == 'g'):
        lst[1] += + g_offset
    elif(lst[3] == 'c'):
        lst[1] += c_offset
    else:
        lst[1] += l_offset

# Adds offset to global, local and constant variables
for okey in sem.var_table:
    for ikey in sem.var_table[okey].items():
        add_offset(ikey[1], state.g_offset, state.c_offset + state.global_dir, state.l_offset)

# Counts global and constant variables to pass the starting stack address to the VM
stack_dir = 0
for var in sem.var_table[sem.global_str].items():
    stack_dir += var[1][2]
for var in sem.var_table[sem.constant_str].items():
    stack_dir += var[1][2]

for func_name in sem.func_table:
    if(sem.var_table[func_name] != None):
        sem.func_table[func_name].append(sorted(map(lambda x: [x[1][1], x[0]], sem.var_table[func_name].items())))

# Changes variables to memory addresses and adds temporal offset
for idx, quad in enumerate(state.quads):
    quad.transform(state.t_offset)
    #quad.add_offset(0, state.global_dir, 9000, 43000)
    print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

#for e in sem.var_table[sem.constant_str].items():
#    e[1][1] += state.global_dir
#    for idx, quad in enumerate(state.quads):
#        quad.transform()
#        #quad.add_offset(0, state.global_dir, 9000, 43000)
#        print idx, (quad.operator, quad.operand1, quad.operand2, quad.result)

# Sorting function
def swap(element):
    return element[1][1], element[0]

with open("o.af", "wb") as out:
    obj = {
        "quads": state.quads,
        "functions": sem.func_table,
        "mem": dict(map(swap, sem.var_table[sem.constant_str].items()) + map(swap, sem.var_table[sem.global_str].items()))
    }
    pickle.dump(obj, out, -1)

machine = vm.VirtualMachine("o.af", stack_dir)
machine.run()