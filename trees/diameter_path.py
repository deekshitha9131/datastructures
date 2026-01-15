class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter_path(root):
    if root is None:
        return []

    best_length = 0   # number of edges
    best_path = []

    def height(node):
        nonlocal best_length, best_path

        if node is None:
            return -1, []

        lh, ldown = height(node.left)
        rh, rdown = height(node.right)

        # Diameter through this node
        current_length = lh + rh + 2
        if current_length > best_length:
            best_length = current_length
            best_path = (
                ldown[::-1] + [node.data] + rdown
            )

        # Return downward path: node -> leaf
        if lh > rh:
            return lh + 1, [node.data] + ldown
        else:
            return rh + 1, [node.data] + rdown

    height(root)
    return best_path

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(6)

print(diameter_path(root))
