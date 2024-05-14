 def Them(self, heso, somu):
        # Tạo một nút mới cho số hạng mới
        new_node = Node(heso, somu)

        # Nếu danh sách liên kết rỗng
        if self.head is None:
            self.head = new_node
            return

        # Nếu số mũ của nút mới lớn hơn số mũ của nút đầu tiên
        if new_node.somu > self.head.somu:
            new_node.ke_tiep = self.head
            self.head = new_node
            return

        # Duyệt qua danh sách liên kết để tìm vị trí chèn
        current = self.head
        while current.ke_tiep is not None and current.ke_tiep.somu >= new_node.somu:
            current = current.ke_tiep

        # Chèn nút mới vào vị trí thích hợp
        new_node.ke_tiep = current.ke_tiep
        current.ke_tiep = new_node

# Tạo một đa thức rỗng
dathuc = DaThuc()