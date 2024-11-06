class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    
stack = Stack()
stack.push(100)
stack.push(70)
stack.push(50)

print(stack.top()) #Fornece o último elemento adicionado.
print(stack.pop()) #Remove o útlimo elemento adicionado.
print(stack.size())
print(stack.items)