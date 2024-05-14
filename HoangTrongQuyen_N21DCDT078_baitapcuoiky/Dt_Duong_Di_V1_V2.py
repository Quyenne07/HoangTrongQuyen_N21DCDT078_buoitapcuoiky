from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def DuongDi(self, v1, v2):
        visited = set()

        def dfs(node, target):
            if node == target:
                return True
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target):
                        return True
            return False

        return dfs(v1, v2)

# Ví dụ sử dụng
# Đồ thị vô hướng
g1 = Graph(directed=False)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
print("Có đường đi từ 0 đến 4:", g1.DuongDi(0, 4))  # True
print("Có đường đi từ 4 đến 0:", g1.DuongDi(4, 0))  # True
print("Có đường đi từ 0 đến 5:", g1.DuongDi(0, 5))  # False

# Đồ thị có hướng
g2 = Graph(directed=True)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
print("Có đường đi từ 0 đến 4:", g2.DuongDi(0, 4))  # True
print("Có đường đi từ 4 đến 0:", g2.DuongDi(4, 0))  # False
print("Có đường đi từ 0 đến 5:", g2.DuongDi(0, 5))  # False