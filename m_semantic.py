#import the funcTable to create a new one every time a scope is needed 
# import func_table as func_table                                          
#import the quad to maque the quadric more generic

global_str = "global"
constant_str = "constant"
scope = global_str
var_table = {scope:{}, constant_str:{}} 

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
                   

def fill_symbol_table_variable(symbol, type):
     #verifica si existe el scope dado
     if(var_table.get(scope) == None):
         var_table[scope] = {}

     if(symbol == scope or var_table[scope].get(symbol) != None):
         raise NameError("Variable redeclaration, '{0}' already exists".format(symbol))
     else:
         var_table[scope][symbol] = [type]

def fill_symbol_table_constant(symbol, type):
    if(var_table[constant_str].get(symbol) != None):
        return
    else:
        var_table[constant_str][symbol] = [type]
    print var_table
	
def get_scope():
	return scope  
	
def validate_redeclaration_function(validate_scope):
	if(var_table.get(validate_scope) != None): raise NameError('se declaro varias veces una misma funcion')  

def validate_variable_is_declared(var):
	if(var_table[scope][var] == None): raise NameError('la variable {0} no se a declarado'.var)
    
def is_declared(var):
    if(var_table.get(scope) == None):
        raise NameError("Undeclared variable '{0}'".format(var))
    elif(var_table[scope].get(var) == None and var_table[global_str].get(var) == None and var_table[constant_str].get(var) == None):
        raise NameError("Undeclared variable '{0}'".format(var))
    else:
        return True

def get_variable(var):
    if(var_table[scope].get(var) != None):
        return [var, var_table[scope].get(var)]
    elif(var_table[constant_str].get(var) != None):
        return [var, var_table[constant_str].get(var)]
    else:
        return [var, var_table[global_str].get(var)]
        
def get_type(op, op1, op2):
    print op, op1, op2
    type = semantic_cube[op][op1[1][0]][op2[1][0]]
    if(type != None):
        return type
    else:
        raise NameError("Incompatible types '{0}' and '{1}'".format(op1[1][0], op2[1][0]))