class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverseList(head):
    temp = head
    prev = None
    while temp is not None:
        print("Before reversing:")
        print("prev=",prev.data if prev else None)
        print("temp=",temp.data)
        print("temp.next=",temp.next.data if temp.next else None)
        nextNode = temp.next
        temp.next = prev  #reverse
        print("After reversing:")
        print("NextNode=",nextNode.data if nextNode else None)
        print("temp.next=",temp.next.data if temp.next else None)
        prev = temp
        temp = nextNode
    return prev

def printList(temp):
    while temp is not None:
        print(f"{temp.data}", end="")
        if temp.next is not None:
            print("->", end="")
        temp = temp.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = reverseList(head)
    printList(head)
