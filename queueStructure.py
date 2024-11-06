class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def first_element(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("A fila está vazia!")
            return None


    def last_element(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            print("A fila está vazia!")
            return None

    def append(self, item):
        self.queue.append(item)
    
    def remove(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("A fila está vazia!")
            return None
    
    def show_queue(self):
        return self.queue
    
queue = Queue()

queue.append("John")
queue.append("Maria")
queue.append("Michael")

print("Fila:", queue.show_queue())

# Removendo
element = queue.remove()
print("Elemento removido:", element)

# Verificando os elementos da fila
print("Primeiro elemento:", queue.first_element())
print("Último elemento:", queue.last_element())

