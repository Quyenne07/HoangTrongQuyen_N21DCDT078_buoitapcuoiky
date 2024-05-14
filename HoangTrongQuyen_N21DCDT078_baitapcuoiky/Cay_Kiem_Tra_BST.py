class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def KiemTraBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if root.info < min_val or root.info > max_val:
        return False

    left_is_bst = KiemTraBST(root.left, min_val, root.info)
    right_is_bst = KiemTraBST(root.right, root.info, max_val)

    return left_is_bst and right_is_bst

# Ví dụ 1: Cây là BST
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print("True")
print("Cây là BST" if KiemTraBST(root) else "Cây không phải là BST")

# Ví dụ 2: Cây không phải BST
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(6)  # Nút này vi phạm tính chất của BST
root.right.left = Node(4)
root.right.right = Node(8)

print("\nFalse")
print("Cây là BST" if KiemTraBST(root) else "Cây không phải là BST")