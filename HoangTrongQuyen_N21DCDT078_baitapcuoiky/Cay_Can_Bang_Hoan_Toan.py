class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def CanBangHoanToan(self):
        return self._isBalanced(self.root)[0]

    def _isBalanced(self, node):
        if node is None:
            return True, 0

        left_balanced, left_height = self._isBalanced(node.left)
        right_balanced, right_height = self._isBalanced(node.right)

        if not left_balanced or not right_balanced:
            return False, max(left_height, right_height) + 1

        height_diff = abs(left_height - right_height)
        if height_diff > 1:
            return False, max(left_height, right_height) + 1

        return True, max(left_height, right_height) + 1

# Trường hợp True
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

print(tree1.CanBangHoanToan())  # Output: True

# Trường hợp False
tree2 = BinaryTree()
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(4)
tree2.root.left.left.left = Node(5)

print(tree2.CanBangHoanToan())  # Output: False