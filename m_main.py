import m_st as state
import m_quad as quad

def generate_main():
    q = quad.Quad()
    q.set_quad("goto", None, "main", None)
    state.quads.append(q)

def update_goto(index):
    state.quads[0].result = index