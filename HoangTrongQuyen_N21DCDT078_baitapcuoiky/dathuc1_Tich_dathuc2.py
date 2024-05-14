class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None

class DaThuoc:
    def __init__(self):
        self.head = None

    def them_so_hang(self, he_so, so_mu):
        new_node = Node(he_so, so_mu)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ke_tiep is not None:
                current = current.ke_tiep
            current.ke_tiep = new_node

    def Tich(self, dathuc2):
        result = DaThuoc()
        current1 = self.head
        while current1 is not None:
            current2 = dathuc2.head
            while current2 is not None:
                he_so_moi = current1.he_so * current2.he_so
                so_mu_moi = current1.so_mu + current2.so_mu
                result.them_so_hang(he_so_moi, so_mu_moi)
                current2 = current2.ke_tiep
            current1 = current1.ke_tiep
        return result

# Sử dụng
dathuc1 = DaThuoc()
dathuc1.them_so_hang(2, 2)
dathuc1.them_so_hang(3, 1)
dathuc1.them_so_hang(1, 0)

dathuc2 = DaThuoc()
dathuc2.them_so_hang(1, 2)
dathuc2.them_so_hang(-2, 1)
dathuc2.them_so_hang(3, 0)

tich = dathuc1.Tich(dathuc2)

print("Đa thức 1:")
current = dathuc1.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep

print("\n\nĐa thức 2:")
current = dathuc2.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep

print("\n\nTích của hai đa thức:")
current = tich.head
while current is not None:
    print(f"{current.he_so}x^{current.so_mu}", end=" ")
    current = current.ke_tiep