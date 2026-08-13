import heapq


def dijkstra(graph, start):
    """graph: {node: [(neighbor, cost), ...]}. 비용이 음수가 아닐 때만 정확하다."""
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_cost, node = heapq.heappop(heap)
        if current_cost > distances[node]:
            continue  # 이미 더 저렴한 경로를 찾은 상태 -> 건너뜀

        for neighbor, weight in graph.get(node, []):
            new_cost = current_cost + weight
            if new_cost < distances[neighbor]:   # relaxation
                distances[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": [],
    }
    print(dijkstra(graph, "A"))
    # {'A': 0, 'B': 3, 'C': 1, 'D': 4}
