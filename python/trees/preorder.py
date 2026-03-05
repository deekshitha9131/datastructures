class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.right = Node("D")
root.right.left = Node("E")
root.right.right = Node("F")
root.right.left.left = Node("G")
root.right.right.left = Node("H")
root.right.right.right = Node("I")

result = preorder(root)
print(result)