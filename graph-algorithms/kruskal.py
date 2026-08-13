class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}

    def find(self, n):
        while self.parent[n] != n:
            self.parent[n] = self.parent[self.parent[n]]  # path compression
            n = self.parent[n]
        return n

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False  # 이미 연결됨 -> 이 간선을 추가하면 순환 생성 -> 건너뜀
        self.parent[root_a] = root_b
        return True


def kruskal(nodes, edges):
    """edges: [(cost, a, b), ...]. 싼 간선부터 고려하되 순환을 만들면 건너뛴다."""
    uf = UnionFind(nodes)
    mst = []

    for cost, a, b in sorted(edges):
        if uf.union(a, b):
            mst.append((a, b, cost))

    return mst


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D"]
    edges = [
        (1, "A", "B"),
        (3, "A", "C"),
        (4, "B", "C"),
        (2, "B", "D"),
        (5, "C", "D"),
    ]
    print(kruskal(nodes, edges))
