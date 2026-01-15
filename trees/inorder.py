class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.right = Node("D")
root.right.left = Node("E")
root.right.right = Node("F")
root.right.left.left = Node("G")
root.right.right.left = Node("H")
root.right.right.right = Node("I")

result = inorder(root)
print(result)