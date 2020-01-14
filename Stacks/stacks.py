class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data_val):
        if data_val not in self.stack:
            self.stack.append(data_val)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return ("Nothing in the Stack")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]


AStack = Stack()
print(AStack.remove())

AStack.add("Monday")
AStack.add("Tuesday")
AStack.add("Wednesday")
AStack.add("Thursday")
AStack.add("Friday")
print(AStack.stack)
print(AStack.remove())
print(AStack.stack)
