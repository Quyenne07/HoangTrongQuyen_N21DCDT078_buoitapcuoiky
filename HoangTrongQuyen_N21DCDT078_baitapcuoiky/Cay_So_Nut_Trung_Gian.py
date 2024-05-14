class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, p):
        if p is None:
            return 0
        count = 0
        if p.left:
            if p.left.left or p.left.right:
                count += self.SoNutTrungGian(p.left)
            else:
                count += 1
        if p.right:
            if p.right.left or p.right.right:
                count += self.SoNutTrungGian(p.right)
            else:
                count += 1
        return count

# Tạo một cây nhị phân để test
cay = BinaryTree()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
cay.root.right.left = Node(6)

# Gọi phương thức SoNutTrungGian() và in kết quả
print("Số nút trung gian của cây là:", cay.SoNutTrungGian(cay.root))