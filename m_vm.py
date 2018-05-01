import cPickle as pickle
import turtle

class VirtualMachine:
    def __init__(self, filename):
        self.instr_ptr = 0
        self.instr_ptr_stack = []
        self.function_call_stack = []
        self.obj = self.load_obj(filename)
        self.quads = self.obj["quads"]
        #self.globals = self.obj["globals"]
        self.functions = self.obj["functions"]
        self.heap = {}
        self.mem = self.obj["mem"]

    def load_obj(self, filename):
        f = open(filename, "rb")
        return pickle.load(f)

    def run(self):
        #get first quad of the list
        quad = self.quads[self.instr_ptr]
        op = quad.operator
        op1 = quad.operand1
        op2 = quad.operand2
        res = quad.result
        while(op != "end" or op1 != "main"):
            if(op == "+"):
                self.mem[res] = self.mem[op1] + self.mem[op2]
            elif(op == "-"):
                self.mem[res] = self.mem[op1] - self.mem[op2]
            elif(op == "*"):
                self.mem[res] = self.mem[op1] * self.mem[op2]
            elif(op == "/"):
                self.mem[res] = self.mem[op1] / self.mem[op2]
            elif(op == "="):
                self.mem[res] = self.mem[op1]
            elif(op == ">"):
                if (self.mem[op1] > self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            elif(op == "<"):
                if (self.mem[op1] < self.mem[op2]):
                    self.mem[res] = 1
                else:
                    self.mem[res] = 0
            
            #functions operations
            if (op == "era"):
                self.function_call_stack.append(op1)
                for var in self.functions[op1][4]:
                    self.mem[var[0]] = var[1]
            if (op == "param"):
                dir = self.functions[self.function_call_stack[-1]][4][res][0]
                self.mem[dir] = self.mem[op1]
            
            # Printing function
            if (op == "print"):
                print self.mem[op1]
            
            # operators that change the instruction pointer
            if(op == "goto"):
                self.instr_ptr = res
            elif(op == "gosub"):
                self.instr_ptr_stack.append(self.instr_ptr + 1)
                self.instr_ptr = self.functions[op1][2]
            elif(op == "end"):
                self.instr_ptr = self.instr_ptr_stack.pop()
            else:
                self.instr_ptr += 1
            #Get next quad of the list
            quad = self.quads[self.instr_ptr]
            op = quad.operator
            op1 = quad.operand1
            op2 = quad.operand2
            res = quad.result
        print "Program finished"