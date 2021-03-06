import m_st as state

global_str = "global"
constant_str = "constant"
scope = global_str
var_table = {scope:{}, constant_str:{}} 
func_table = {}
operation = None

semantic_cube = {
"=":{
	"entero":{
		"entero":"entero",
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
	"caracter":{
		"entero":None,
		"caracter":"caracter",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":None,
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":"booleano",
	}
},
"*":{
	"entero":{
		"entero":"entero",
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"caracter":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"flotante",
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	}
},
"+":{
	"entero":{
		"entero":"entero",
		"caracter":"caracter",
		"flotante":"flotante",
		"booleano":None,
	},
	"caracter":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"flotante",
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
},
"-":{
	"entero":{
		"entero":"entero",
		"caracter":"caracter",
		"flotante":"flotante",
		"booleano":None,
	},
	"caracter":{
		"entero":None,
		"caracter":"caracter",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"flotante",
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
},
"/":{
	"entero":{
		"entero":"flotante",
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"caracter":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"flotante",
		"caracter":None,
		"flotante":"flotante",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
},
">":{
	"entero":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":"booleano",
		"booleano":None,
	},
	"caracter":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"booleano",
		"caracter":None,
		"flotante":"booleano",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	 }, 
},
"<":{
	"entero":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":"booleano",
		"booleano":None,
	},
	"caracter":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"booleano",
		"caracter":None,
		"flotante":"booleano",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	}, 
},
">=":{
	"entero":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":"booleano",
		"booleano":None,
	},
	"caracter":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"booleano",
		"caracter":None,
		"flotante":"booleano",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
},
"<=":{
	"entero":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":"booleano",
		"booleano":None,
	},
	"caracter":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"booleano",
		"caracter":None,
		"flotante":"booleano",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":None,
	},
},
"!=":{
	"entero":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":"booleano",
		"booleano":None,
	},
	"caracter":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"booleano",
		"caracter":None,
		"flotante":"booleano",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":"booleano",
	},
},
"==":{
	"entero":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":"booleano",
		"booleano":None,
	},
	"caracter":{
		"entero":"booleano",
		"caracter":"booleano",
		"flotante":None,
		"booleano":None,
	},
	"flotante":{
		"entero":"booleano",
		"caracter":None,
		"flotante":"booleano",
		"booleano":None,
	},
	"booleano":{
		"entero":None,
		"caracter":None,
		"flotante":None,
		"booleano":"booleano",
	},
}
}

def fill_symbol_table_function(symbol, attributes): 
    if(func_table.get(symbol) == None): 
        func_table[symbol] = attributes
    else: 
        raise NameError("Function redeclaration, '{0}' already exists".format(symbol))

def fill_local_variables_table(var, type, size):
    #verifica si existe el scope dado
    if(var_table.get(scope) == None):
        var_table[scope] = {}
    if(var == scope or var_table[scope].get(var) != None):
        raise NameError("Variable redeclaration, '{0}' already exists".format(var))
    else:
        var_table[scope][var] = [type, state.local_dir, size, 'l']
        state.local_dir += size

def fill_global_variables_table(var, type, size):
    #verifica si existe el scope dado
    if(var_table.get(scope) == None):
        var_table[scope] = {}
    if(var == scope or var_table[scope].get(var) != None):
        raise NameError("Variable redeclaration, '{0}' already exists".format(var))
    else:
        var_table[scope][var] = [type, state.global_dir, size, 'g']
        state.global_dir += size

def fill_symbol_table_constant(symbol, type, size):
    if(var_table[constant_str].get(symbol) != None):
        pass
    else:
        var_table[constant_str][symbol] = [type, state.constant_dir, size, 'c']
        if(type[0] == "e" or type[0] == "f"):
            state.constant_dir += 4
        else:
            state.constant_dir += 1


def get_function(func_name):
    function = func_table.get(func_name)
    if(function != None):
        return function
    else:
        raise NameError("Undeclared function '{0}'".format(func_name))

def get_scope(): 
    return scope


def validate_redeclaration_function(validate_scope): 
    if(var_table.get(validate_scope) != None):  raise NameError('se declaro varias veces una misma funcion')

def validate_variable_is_declared(var): 
    if(var_table[scope][var] == None):  raise NameError('la variable {0} no se ha declarado'.var)

# revisar este pedo
def is_declared(var):
    if(var_table[constant_str].get(var) != None):
        return True
    elif(var_table.get(scope) != None and var_table[scope].get(var) != None):
        return True
    elif(var_table[global_str].get(var) != None):
        return True
    elif(func_table.get(var) != None):
        return True
    else: 
        raise NameError("Undeclared variable '{0}'".format(var))

def get_variable(var):
    if(var_table.get(scope) != None and var_table[scope].get(var) != None):
        return [var, var_table[scope].get(var)]
    elif(var_table[constant_str].get(var) != None):
        return [var, var_table[constant_str].get(var)]
    elif(func_table.get(var) != None):
        info = func_table[var][0][:]  # Function return value information
        info[1] = state.return_dir_stack.pop()  # Gets the last return address
        info[3] = 't'  # Changes its type to temporal
        return [var, info]
    else:
        return [var, var_table[global_str].get(var)]

def get_type(op, op1, op2): 
    #print op, op1, op2 
    if(isinstance(op1, str)):
        type = semantic_cube[op]["caracter"][op2[1][0]]
    else:
        if(op1[1] == None):
            type1 = func_table[op1[0]][0]
        else:
            type1 = op1[1][0]
        if(op2[1] == None):
            type2 = func_table[op2[0]][0]
        else:
            type2 = op2[1][0]
        type = semantic_cube[op][type1][type2]
    if(type != None): 
        return type
    else: 
        raise NameError("Incompatible types '{0}' and '{1}'".format(op1[1][0], op2[1][0]))

def is_signature_valid(func_name, signature):
    if(cmp(func_table.get(func_name)[1], signature) == 0):
        return True
    else:
        raise NameError("Wrong signature '{0}', {1}".format(func_name, signature))