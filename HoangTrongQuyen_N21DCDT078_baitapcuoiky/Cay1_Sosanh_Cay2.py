class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def SoSanh(root1, root2):
    # Trường hợp cơ sở: Cả hai cây rỗng
    if root1 is None and root2 is None:
        return True

    # Trường hợp cơ sở: Một cây rỗng, một cây không rỗng
    if root1 is None or root2 is None:
        return False

    # Kiểm tra giá trị của nút hiện tại
    if root1.info != root2.info:
        return False

    # Đệ quy so sánh cây con bên trái và bên phải
    return SoSanh(root1.left, root2.left) and SoSanh(root1.right, root2.right)

# Ví dụ sử dụng
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print(SoSanh(root1, root2))  # Output: True

root3 = Node(1)
root3.left = Node(2)
root3.right = Node(3)
root3.left.left = Node(4)

print(SoSanh(root1, root3))  # Output: False