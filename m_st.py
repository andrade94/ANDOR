# Module that keeps the state of the parser
# Temp pool
# TODO: Add a pool for each primitive

# Conditions
params_list = []
label_stack = []
label = 0
# Operands stack
operand_stack = []
# Functions
signature = []
f_size = 0
# Param Counter
param_counter = 0
param_types = []

# Operator stack
operator_stack = []
last_operator = None

# Temp counter
temp_counter = 0

# Quad list
quads = []

def clear_stacks():
    global operator_stack, operand_stack, last_operator
    del(operator_stack[:])
    del(operand_stack[:])
    last_operator = None

def reset_param_counter():
    global param_counter
    param_counter = 0

def reset_param_types():
    global param_types
    param_types = []

def reset_call():
    reset_param_counter()
    reset_param_types()