class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.ke_tiep = None

class DaThuc:
    def __init__(self):
        self.head = None

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

    def RutGon(self):
        # Tạo một danh sách liên kết mới để lưu đa thức đã rút gọn
        new_head = None
        current = self.head

        while current is not None:
            # Tìm các số hạng có cùng số mũ
            somu = current.somu
            tong_heso = current.heso
            temp = current.ke_tiep

            while temp is not None and temp.somu == somu:
                tong_heso += temp.heso
                temp = temp.ke_tiep

            # Tạo nút mới cho số hạng đã gộp
            if tong_heso != 0:
                new_node = Node(tong_heso, somu)

                # Chèn nút mới vào danh sách liên kết mới
                if new_head is None:
                    new_head = new_node
                else:
                    ptr = new_head
                    if new_node.somu > ptr.somu:
                        new_node.ke_tiep = ptr
                        new_head = new_node
                    else:
                        while ptr.ke_tiep is not None and ptr.ke_tiep.somu >= new_node.somu:
                            ptr = ptr.ke_tiep
                        new_node.ke_tiep = ptr.ke_tiep
                        ptr.ke_tiep = new_node

            # Di chuyển đến số hạng tiếp theo
            current = temp

        # Gán lại đầu danh sách liên kết cho self.head
        self.head = new_head

    def Cong(self, dathuc2):
        # Tạo một đa thức mới để lưu kết quả
        ket_qua = DaThuc()

        # Con trỏ duyệt qua đa thức dathuc1
        ptr1 = self.head
        # Con trỏ duyệt qua đa thức dathuc2
        ptr2 = dathuc2.head

        # Cộng hai đa thức và thêm vào kết quả
        while ptr1 is not None and ptr2 is not None:
            if ptr1.somu > ptr2.somu:
                ket_qua.Them(ptr1.heso, ptr1.somu)
                ptr1 = ptr1.ke_tiep
            elif ptr1.somu < ptr2.somu:
                ket_qua.Them(ptr2.heso, ptr2.somu)
                ptr2 = ptr2.ke_tiep
            else:
                tong_heso = ptr1.heso + ptr2.heso
                ket_qua.Them(tong_heso, ptr1.somu)
                ptr1 = ptr1.ke_tiep
                ptr2 = ptr2.ke_tiep

        # Thêm các số hạng còn lại của đa thức dathuc1 vào kết quả
        while ptr1 is not None:
            ket_qua.Them(ptr1.heso, ptr1.somu)
            ptr1 = ptr1.ke_tiep

        # Thêm các số hạng còn lại của đa thức dathuc2 vào kết quả
        while ptr2 is not None:
            ket_qua.Them(ptr2.heso, ptr2.somu)
            ptr2 = ptr2.ke_tiep

        # Rút gọn đa thức kết quả
        ket_qua.RutGon()

        return ket_qua

    def InDaThuc(self):
        current = self.head
        is_first = True
        while current is not None:
            if is_first:
                print(f"{current.heso}x^{current.somu}", end="")
                is_first = False
            else:
                print(f" + {current.heso}x^{current.somu}", end="")
            current = current.ke_tiep

# Tạo hai đa thức
dathuc1 = DaThuc()
dathuc1.Them(2, 3)  # 2x^3
dathuc1.Them(-1, 2)  # -x^2
dathuc1.Them(4, 1)  # 4x

dathuc2 = DaThuc()
dathuc2.Them(1, 3)  # x^3
dathuc2.Them(3, 2)  # 3x^2
dathuc2.Them(-2, 1)  # -2x

# In ra hai đa thức ban đầu
print("Đa thức 1:")
dathuc1.InDaThuc()
print("\nĐa thức 2:")
dathuc2.InDaThuc()
print()  # Để xuống dòng

# Cộng hai đa thức và in ra kết quả
ket_qua = dathuc1.Cong(dathuc2)
print("Tổng hai đa thức:")
ket_qua.InDaThuc()
print()  # Để xuống dòng