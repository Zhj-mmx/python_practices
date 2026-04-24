import heapq # ?

graph = {
    'A': {'B': 6, 'D': 2},
    'B': {'A': 6, 'C': 1, 'E': 2},
    'C': {'B': 1, 'F': 5},
    'D': {'A': 2, 'E': 5},
    'E': {'B': 2, 'D': 5, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    previous = {node: None for node in graph} #?

    pq = [(0, start)]

    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue

            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist 
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_dist))


print("Hello,World")
