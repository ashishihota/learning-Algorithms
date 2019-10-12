
class stack(object):
    def __init__(self):
        self.stk = []     #initializing an array as a stack

    def is_empty(self):
        return self.stk == []

    def push(self, item):
        self.stk.append(data)

    def pop(self):
        if self.is_empty():
            print("the stack is empty")
        else:
            self.stk.pop()

    def size(self):
        return len(self.stk)

    def peek(self):
        if self.is_empty():
            print("the stack is empty")
        else:
            return self.stk[-1]
    def show(self):
        return self.stk