class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data}")
    def pop(self):
        if self.is_empty():
            print("Stack underflow! cannot pop from empty stack")
            return None
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements are(top->bottom):",self.stack[::-1])

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(15)
    s.push(20)
    s.display()

    print("Top element:", s.peek())
    print("Popped element:",s.pop())

    s.display()