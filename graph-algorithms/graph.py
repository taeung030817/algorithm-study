from collections import deque


class Graph:
    """인접 리스트 기반 그래프. BFS/DFS 제공."""

    def __init__(self):
        self.adjacency = {}

    def add_edge(self, a, b, directed=False):
        self.adjacency.setdefault(a, []).append(b)
        if not directed:
            self.adjacency.setdefault(b, []).append(a)
        else:
            self.adjacency.setdefault(b, [])

    def bfs(self, start):
        """물결처럼 한 층씩 확장. 가중치 없는 그래프의 최단 경로 탐색에 사용."""
        visited = {start}
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start, visited=None, order=None):
        """끝까지 갔다가 막히면 돌아온다. 도달 가능성, 순환 감지 등에 사용."""
        if visited is None:
            visited = set()
        if order is None:
            order = []

        visited.add(start)
        order.append(start)
        for neighbor in self.adjacency.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, order)

        return order


if __name__ == "__main__":
    g = Graph()
    for a, b in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]:
        g.add_edge(a, b)

    print("BFS:", g.bfs("A"))
    print("DFS:", g.dfs("A"))
