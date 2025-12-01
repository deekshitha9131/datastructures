class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def intersectPoint(head1, head2):
    while head2 is not None:
        temp = head1
        while temp is not None:
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    return None

if __name__ == "__main__":
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)
    head2.next.next.next = head1.next

    intersectionPoint = intersectPoint(head1, head2)

    if intersectionPoint is None:
        print("-1")
    else:
        print(intersectionPoint.data)