# Diameter of a binary tree measured in number of edges

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def diameter(root):
    max_diameter = 0
    def height(node):
        nonlocal max_diameter
        if node is None:
            return -1
        lh = height(node.left)
        rh = height(node.right)
        max_diameter = max(max_diameter, lh + rh + 2)
        return max(lh,rh)+1
    height(root)
    return max_diameter

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(6)

print(diameter(root))
