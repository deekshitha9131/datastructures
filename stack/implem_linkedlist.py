class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head=new_node
        print(f"Pushed {data}")
    def pop(self):
        if self.is_empty():
            print("Stack is empty!! cannot pop")
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped
    def peek(self):
        if self.is_empty:
            print("Stack is empty")
            return None
        return self.head.data
    def is_empty(self):
        return self.head is None
        
    def diaplay(self):
        if self.is_empty():
            print("Satck is empty")
            return
        print("Stack elements are(top->bottom):",end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(35)
    s.diaplay()

    print("Top element is:",s.peek())
    print("Popped element is:", s.pop())
    s.diaplay()