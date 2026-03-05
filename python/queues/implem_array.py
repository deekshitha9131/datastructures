# FIFO
# first in first out
class Queue:
    def __init__(self,capacity):
        self.queue = [None]*capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity
    def is_full(self):
        return self.size == self.capacity
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1)%self.capacity
        self.queue[self.rear]=item
        self.size +=1
        print(f"Enqueued {item}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front+1)% self.capacity
        self.size -=1
        print(f"Dequeued {item}")
        return item
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements are: ")
        for i in range(self.size):
            print(self.queue[(self.front+i)%self.capacity], end=" ")
        print()

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.display()

    q.dequeue()
    q.dequeue()