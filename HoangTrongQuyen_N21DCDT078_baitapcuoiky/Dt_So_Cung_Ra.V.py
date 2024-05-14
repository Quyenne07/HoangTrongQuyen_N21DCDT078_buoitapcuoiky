from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def SoCungRa(self, v):
        if v not in self.graph:
            return 0
        return len(self.graph[v])

# Ví dụ sử dụng
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(2, 4)
g.add_edge(4, 3)

print("Số cung đi ra khỏi đỉnh 0:", g.SoCungRa(0))  # Output: 1
print("Số cung đi ra khỏi đỉnh 1:", g.SoCungRa(1))  # Output: 1
print("Số cung đi ra khỏi đỉnh 2:", g.SoCungRa(2))  # Output: 2
print("Số cung đi ra khỏi đỉnh 3:", g.SoCungRa(3))  # Output: 1
print("Số cung đi ra khỏi đỉnh 4:", g.SoCungRa(4))  # Output: 1
print("Số cung đi ra khỏi đỉnh 5:", g.SoCungRa(5))  # Output: 0