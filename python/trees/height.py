#Edges of longest path
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def height(node):
        if node is None:
            return -1
        lh = height(node.left)
        rh = height(node.right)
        return max(lh,rh)+1
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.right = Node("D")
root.right.left = Node("E")
root.right.right = Node("F")
root.right.left.left = Node("G")
root.right.right.left = Node("H")
root.right.right.right = Node("I")

print(height(root))