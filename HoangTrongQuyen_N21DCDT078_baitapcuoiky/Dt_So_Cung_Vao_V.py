from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for node in self.graph:
            if v in self.graph[node]:
                count += 1
        return count

# Ví dụ sử dụng
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(2, 4)
g.add_edge(4, 3)

print("Số cung đi vào đỉnh 0:", g.SoCungVao(0))  # Output: 1
print("Số cung đi vào đỉnh 1:", g.SoCungVao(1))  # Output: 1
print("Số cung đi vào đỉnh 2:", g.SoCungVao(2))  # Output: 1
print("Số cung đi vào đỉnh 3:", g.SoCungVao(3))  # Output: 2
print("Số cung đi vào đỉnh 4:", g.SoCungVao(4))  # Output: 1
print("Số cung đi vào đỉnh 5:", g.SoCungVao(5))  # Output: 0