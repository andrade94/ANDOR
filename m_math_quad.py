import m_all_quad as quad
# operand_stack = []
# operator_stack = []
# last_operator = None
# temp_counter = 0
# quads = []

# ID found
def add_operand(id, type):
    quad.quad.push_operand_stack([id, type])

def add_operator(operator):
    quad.quad.push_operator_stack(operator)
    if(operator == 'x'):
        quad.quad.set_last_operator(None)
    else:
         quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1)) 

def push_expr():
    quad.quad.push_operator_stack("x")
    quad.quad.set_last_operator(None)

def pop_expr():  
    op = quad.quad.pop_operator_stack()   
        
def generate_quad(level):
    if(level == 0):
        pass
    elif(level == 1):
        if(quad.quad.get_last_operator() == '*' or quad.quad.get_last_operator() == '/'):
            quad.quad.operator = quad.quad.pop_operator_stack()   
            quad.quad.operand2 = quad.quad.pop_operand_stack()[0]
            quad.quad.operand1 = quad.quad.pop_operand_stack()[0]
            quad.quad.result = "t" + str(quad.quad.get_temp_counter())
            quad.quad.push_operand_stack([quad.quad.result, 0])
            quad.quad.quads.append(quad.quad.generate_quad()) 
            if(len(quad.quad.operator_stack) > 0):
                quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1))
            quad.quad.set_temp_counter(quad.quad.get_temp_counter()+1)
    elif(level == 2):
        if(quad.quad.get_last_operator() == '+' or quad.quad.get_last_operator() == '-'):   
            quad.quad.operator = quad.quad.pop_operator_stack()  
            quad.quad.operand2 = quad.quad.pop_operand_stack()[0]
            quad.quad.operand1 = quad.quad.pop_operand_stack()[0]
            quad.quad.result = "t" + str(quad.quad.get_temp_counter())
            quad.quad.push_operand_stack([quad.quad.result, 0])
            quad.quad.quads.append(quad.quad.generate_quad())
            if(len(quad.quad.operator_stack) > 0):
               quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1))
            quad.quad.set_temp_counter(quad.quad.get_temp_counter()+1)
    elif(level == 5):
        if(quad.quad.get_last_operator() == '='): 
            quad.quad.operator = quad.quad.pop_operator_stack() 
            quad.quad.operand1 = quad.quad.pop_operand_stack()[0]
            quad.quad.result = quad.quad.pop_operand_stack()[0]
            quad.quad.push_operand_stack([quad.quad.result, 0])
            quad.quad.quads.append(quad.quad.generate_quad())
            if(len(quad.quad.operator_stack) > 0):
                quad.quad.set_last_operator(quad.quad.get_operator_stack_index(-1))
