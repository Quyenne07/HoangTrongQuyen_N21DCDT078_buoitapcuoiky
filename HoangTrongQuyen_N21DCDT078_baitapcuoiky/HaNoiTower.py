class HanoiTower:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.towers = [list(range(num_disks, 0, -1)), [], []]

    def move_disks(self, n, source, destination, intermediate):
        if n == 1:
            disk = self.towers[source].pop()
            self.towers[destination].append(disk)
            print(f"Di chuyển đĩa {disk} từ tháp {source} đến tháp {destination}")
        else:
            self.move_disks(n - 1, source, intermediate, destination)
            self.move_disks(1, source, destination, intermediate)
            self.move_disks(n - 1, intermediate, destination, source)

    def solve(self):
        self.move_disks(self.num_disks, 0, 2, 1)
        print("Tháp đích:")
        print(self.towers[2])

# Sử dụng
tower = HanoiTower(3)
tower.solve()