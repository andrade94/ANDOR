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
		print(attributes)
		func_table[symbol] = attributes
    else: 
        raise NameError("Function redeclaration, '{0}' already exists".format(symbol))

def fill_symbol_table_variable(symbol, type): 
    #verifica si existe el scope dado
    if(var_table.get(scope) == None): 
        var_table[scope] = {}

    if(symbol == scope or var_table[scope].get(symbol) != None): 
        raise NameError("Variable redeclaration, '{0}' already exists".format(symbol))
    else: 
        var_table[scope][symbol] = [type]
    #print("{0} {1} {2} {3} {4}".format(p[-4], p[-3], p[-2], p[-1], p[0]))

def fill_symbol_table_constant(symbol, type): 
    if(var_table[constant_str].get(symbol) != None): 
        return
    else: 
        var_table[constant_str][symbol] = [type]
    #print var_table

def get_function(func_name): 
    return func_table.get(func_name)

def get_scope(): 
    return scope

def validate_redeclaration_function(validate_scope): 
    if(var_table.get(validate_scope) != None):  raise NameError('se declaro varias veces una misma funcion')

def validate_variable_is_declared(var): 
    if(var_table[scope][var] == None):  raise NameError('la variable {0} no se a declarado'.var)

# revisar este pedo
def is_declared(var):
    if(var_table[constant_str].get(var) != None):
        return True
    elif(var_table.get(scope) != None and var_table[scope].get(var) != None):
        return True
    elif(var_table[global_str].get(var) != None):
        return True
    else: 
        raise NameError("Undeclared variable '{0}'".format(var))

def get_variable(var):
    if(var_table.get(scope) != None and var_table[scope].get(var) != None):
        return [var, var_table[scope].get(var)]
    elif(var_table[constant_str].get(var) != None):
        return [var, var_table[constant_str].get(var)]
    else:
        return [var, var_table[global_str].get(var)]

def get_type(op, op1, op2): 
    #print op, op1, op2 
    if(isinstance(op1,str)): 
        type = semantic_cube[op]["caracter"][op2[1][0]]
    else: 
        type = semantic_cube[op][op1[1][0]][op2[1][0]]
    if(type != None): 
        return type
    else: 
        raise NameError("Incompatible types '{0}' and '{1}'".format(op1[1][0], op2[1][0]))

def is_signature_valid(func_name, signature):
    if(cmp(func_table.get(func_name)[1], signature) == 0):
        return True
    else:
        raise NameError("Wrong signature")