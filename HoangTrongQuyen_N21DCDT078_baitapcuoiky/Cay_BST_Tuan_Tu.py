class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def BSTTuanTu(self):
        return self._isTuanTu(self.root)

    def _isTuanTu(self, node):
        if node is None:
            return True

        if node.left and node.right:
            return False

        left_exists = self._exists(node.left)
        right_exists = self._exists(node.right)

        return (left_exists and not right_exists) or (not left_exists and right_exists)

    def _exists(self, node):
        if node is None:
            return False

        if node.left or node.right:
            return True

        return self._exists(node.left) or self._exists(node.right)
    
# Tạo một cây nhị phân tìm kiếm tuần tự
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(5)
tree.root.left.left = Node(3)
tree.root.left.left.left = Node(1)

print(tree.BSTTuanTu())  # Output: True

# Tạo một cây nhị phân không phải là tìm kiếm tuần tự
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(5)
tree.root.right = Node(15)

print(tree.BSTTuanTu())  # Output: False