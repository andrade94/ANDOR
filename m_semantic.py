global_s = "global"
# constant_s = "constant"
scope = global_s
var_table = {scope: {}}
lastType = None
# operation = {}
# func_table = {}

semantic_cube = {
  "=": {
      "entero": {
          "entero": "entero",
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
      "caracter": {
          "entero": "caracter",
          "caracter": "caracter",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "flotante",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": "booleano",
      }
  },
  "*": {
      "entero": {
          "entero": "entero",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "caracter": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "flotante",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      }
  },
  "+": {
      "entero": {
          "entero": "entero",
          "caracter": "caracter",
          "flotante": "flotante",
          "booleano": None,
      },
      "caracter": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "flotante",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  "-": {
      "entero": {
          "entero": "entero",
          "caracter": "caracter",
          "flotante": "flotante",
          "booleano": None,
      },
      "caracter": {
          "entero": None,
          "caracter": "caracter",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "flotante",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  "/": {
      "entero": {
          "entero": "flotante",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "caracter": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "flotante",
          "caracter": None,
          "flotante": "flotante",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  ">": {
      "entero": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": "booleano",
          "booleano": None,
      },
      "caracter": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "booleano",
          "caracter": None,
          "flotante": "booleano",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  "<": {
      "entero": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": "booleano",
          "booleano": None,
      },
      "caracter": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "booleano",
          "caracter": None,
          "flotante": "booleano",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  ">=": {
      "entero": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": "booleano",
          "booleano": None,
      },
      "caracter": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "booleano",
          "caracter": None,
          "flotante": "booleano",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  "<=": {
      "entero": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": "booleano",
          "booleano": None,
      },
      "caracter": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "booleano",
          "caracter": None,
          "flotante": "booleano",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": None,
      },
  },
  "!=": {
      "entero": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": "booleano",
          "booleano": None,
      },
      "caracter": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "booleano",
          "caracter": None,
          "flotante": "booleano",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": "booleano",
      },
  },
  "==": {
      "entero": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": "booleano",
          "booleano": None,
      },
      "caracter": {
          "entero": "booleano",
          "caracter": "booleano",
          "flotante": None,
          "booleano": None,
      },
      "flotante": {
          "entero": "booleano",
          "caracter": None,
          "flotante": "booleano",
          "booleano": None,
      },
      "booleano": {
          "entero": None,
          "caracter": None,
          "flotante": None,
          "booleano": "booleano",
      },
  }
}

def fill_typeVariable_table(var, type):
  if(var_table.get(scope) == None):
    var_table[scope] = {}
  # elif(scope != "global"):
  #   raise NameError("Function redeclared '{0}'".format(p[-1]))
  if(var == scope or var_table[scope].get(var) != None):
    raise NameError("Redeclared variable '{0}'".format(var))
  else:
    var_table[scope][var] = [type]

def redeclaredFunction(name):
  if(var_table.get(name) != None):
    raise NameError("Redeclared function '{0}'".format(name))

def redeclaredVariable(var):
  if(var == scope or var_table[scope].get(var) != None):
    raise NameError("Redeclared variable '{0}'".format(var))

def isDeclared(var):
  if(var_table[scope][var] == None):
    raise NameError("Variable:'{0}' is not declared.".format(var))
  
def getScope():
  return scope


