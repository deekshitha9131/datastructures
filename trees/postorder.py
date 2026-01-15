class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.right = Node("D")
root.right.left = Node("E")
root.right.right = Node("F")
root.right.left.left = Node("G")
root.right.right.left = Node("H")
root.right.right.right = Node("I")

result = postorder(root)
print(result)