class Node:
    def __init__(self, node):
        self.data = node
        self.next = None
def sortedIntersect(head1, head2):
    common_found = False
    while head1 is not None and head2 is not None:
        if head1.data == head2.data:
            print(head1.data, end=" ")
            common_found = True
            head1 = head1.next
            head2 = head2.next
        elif head1.data < head2.data:
            head1 = head1.next
        else:
            head2 = head2.next
    if not common_found:
        print("No common elements found")

if __name__ == "__main__":
    head1 = Node(1)
    head1.next = Node(4)
    head1.next.next = Node(6)
    head1.next.next.next = Node(9)
    head1.next.next.next.next = Node(11)

    head2 = Node(3)
    head2.next = Node(4)
    head2.next.next = Node(6)
    head2.next.next.next = Node(7)
    head2.next.next.next.next = Node(8)
    head2.next.next.next.next.next = Node(9)

    print("Common elements are:")
    sortedIntersect(head1, head2)
