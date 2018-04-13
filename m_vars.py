#current calling function
current_call = ""

label_stack = []

assign_list = []

return_dir_stack = []
return_var_stack = []
func_parsing = False

arr_dim = []
arr_dim_str = ""
arr_current_dim = 0
arr_dim_stack = []
arr_m_list = []
arr_r = 1
arr_indices = []
arr_parsing = False

unresolved_vars = {}

operand_stack = []

operator_stack = []
last_operator = None

ptr_counter = 0

temp_counter = 0

global_dir = 0
constant_dir = 0
local_dir = 0
temp_dir = 0
stack_dir = 0
special_dir = 0

signature = []

f_param_list = []

param_counter = 0

param_types = []

quads = []

g_offset = 0
c_offset = 0
l_offset = 0
t_offset = 55000

def clear_stacks():
    global operator_stack, operand_stack, last_operator
    del(operator_stack[:])
    del(operand_stack[:])
    last_operator = None

def reset_call():
    global param_counter, param_types, signature
    param_counter = 0
    param_types = []
    signature = []