class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNut(self, p):
        if p is None:
            return 0
        else:
            return self.SoNut(p.left) + self.SoNut(p.right) + 1

# Tạo một cây nhị phân để test
cay = BinaryTree()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

# Gọi phương thức SoNut() và in kết quả
print("Số nút của cây là:", cay.SoNut(cay.root))