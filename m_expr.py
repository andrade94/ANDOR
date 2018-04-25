import m_st as state
import m_quad as quad
        
def generate_quad(hierarchy):
    qd = quad.Quad()
    # if(hierarchy == 0 and (state.last_operator == 'u+' or state.last_operator == 'u-')):
    #     qd.set_quad(state.operator_stack.pop(), None, state.operand_stack.pop(), state.operand_stack.pop())
    #     state.temp_counter += 1
    #     state.label += 1
    if(hierarchy == 1 and (state.last_operator == '*' or state.last_operator == '/') and state.operator_stack):
        qd.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
        state.temp_counter += 1
        state.label += 1
    elif(hierarchy == 2 and (state.last_operator == '+' or state.last_operator == '-') and state.operator_stack):
        qd.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
        state.temp_counter += 1
        state.label += 1
    elif(hierarchy == 3 and (state.last_operator == '==' or state.last_operator == '<=' or state.last_operator == '>=' or state.last_operator == '<>'  or state.last_operator == '<'  or state.last_operator == '>') and state.operator_stack):
        qd.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
        state.temp_counter += 1
        state.label += 1
    elif(hierarchy == 5 and (state.last_operator == '=')):
        qd.set_quad(state.operator_stack.pop(), state.operand_stack.pop(), state.operand_stack.pop(), "t" + str(state.temp_counter))
        state.temp_counter += 1
        state.label += 1
    if(qd.operator != None):
        state.quads.append(qd)
        state.operand_stack.append(qd.result)
    else:
        del(qd)
    if(len(state.operator_stack) > 0):
        state.last_operator = state.operator_stack[-1]

def add_operand(operand):
    state.operand_stack.append(operand)

def add_operator(operator):
    state.operator_stack.append(operator)
    if(operator == '#'):
        last_operator = None
    else:
        last_operator = state.operator_stack[-1]

def push_expr():
    state.operator_stack.append('#')
    state.last_operator = None

def pop_expr():
    state.operator_stack.pop()
    if (state.operator_stack):
        state.last_operator = state.operator_stack[-1]
