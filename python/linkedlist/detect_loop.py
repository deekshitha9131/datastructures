class Node:
    def __init__(self,nextNode):
        self.data = nextNode
        self.next = None
def detect_loop(head):
    st = set()
    while head is not None:
        if head in st:
            return True
        st.add(head)
        head = head.next
    return False

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    head.next.next.next = head.next
    if detect_loop(head):
        print("Loop detected in the Linked List")
    else:
        print("NO Loop detected in the linked List")

