class StackOverflowError(Exception):
    pass
class StackUnderflowError(Exception):
    pass

class Stack:
    def __init__(self,capacity=None):
        self.data = []
        self.capacity = capacity
    def size(self):
        return len(self.data)
    def is_full(self):
        if self.capacity:
            return len(self.data) == self.capacity
        return False
    def is_empty(self):
        return len(self.data) == 0
    def push(self, item):
        if self.is_full():
            raise StackOverflowError("Stack is full, cannot push new item")
        self.data.append(item)
        print(f"Pushed {item}")
    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack is empty, cannot pop item")
        return self.data.pop()
    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Stack is empty, no top element")
        return self.data[-1]
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements are(top->bottom):",self.data[::-1])

if __name__ == "__main__":
    s = Stack(capacity=3)
    try:
        s.push(10)
        s.push(15)
        s.push(20)
        # s.push(25) 
        s.display()
        print("Top:",s.peek()) 
        print("Popped element:", s.pop())
        s.push(30)
        s.push(35)
    except StackOverflowError as e:
        print(e)
    except StackUnderflowError as e:
        print(e)