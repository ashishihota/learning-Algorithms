
class stack(object):
    def __init(self, limit = 10):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, data):
        if len(self.stk) > self.limit:
            print("The stack is full")
        else:
            self.stk.append(data)
        print("the stack is ", self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print("the stack is empty")
            return 0
        else:
            return self.stk.pop()       

    def peek(self):
        if len(self.stk) <= 0:
            print("stack underflow")
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

our_stack = stack()
our_stack.push("1")
our_stack.push("2")
our_stack.push("4")
our_stack.push("3")
our_stack.push("4")
