import m_st as state
import m_quad as quad
import m_semantic as sem

def print_quad(printable):
    qd = quad.Quad()
    qd.set_quad("print", None, printable, None)
    # state.operand_stack.append(qd.result)
    state.quads.append(qd)
    state.temp_counter += 1

def read_quad(type, var, scope):
    if(type == sem.var_table[scope][var][0]):
        qd = quad.Quad()
        qd.set_quad("read", None, "t" + str(state.temp_counter), var)
        # state.operand_stack.append(qd.result)
        state.quads.append(qd)
        state.temp_counter += 1
    else:
        print "incompatible"