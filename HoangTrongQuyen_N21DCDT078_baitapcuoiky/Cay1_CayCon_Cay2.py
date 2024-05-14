class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def CayCon(root1, root2):
    # Trường hợp cơ sở: Cây con rỗng
    if root2 is None:
        return True

    # Trường hợp cơ sở: Cây lớn rỗng và cây con không rỗng
    if root1 is None:
        return False

    # Kiểm tra giá trị của nút hiện tại
    if root1.info == root2.info:
        # Nếu giá trị của nút hiện tại giống nhau, kiểm tra cây con bên trái và bên phải
        return (CayCon(root1.left, root2.left) and CayCon(root1.right, root2.right))

    # Nếu giá trị của nút hiện tại khác nhau, tìm kiếm trên cây con bên trái và bên phải
    return CayCon(root1.left, root2) or CayCon(root1.right, root2)

# Ví dụ sử dụng
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(2)
root2.left = Node(4)
root2.right = Node(5)

print(CayCon(root1, root2))  # Output: True

root3 = Node(6)
root3.left = Node(4)
root3.right = Node(5)

print(CayCon(root1, root3))  # Output: False