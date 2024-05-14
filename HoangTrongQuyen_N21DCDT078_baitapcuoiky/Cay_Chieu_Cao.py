class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def ChieuCao(self, p):
        if p is None:
            return 0
        else:
            left_height = self.ChieuCao(p.left)
            right_height = self.ChieuCao(p.right)
            return max(left_height, right_height) + 1

# Tạo một cây nhị phân để test
cay = BinaryTree()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
cay.root.right.left = Node(6)

# Gọi phương thức ChieuCao() và in kết quả
print("Chiều cao của cây là:", cay.ChieuCao(cay.root))