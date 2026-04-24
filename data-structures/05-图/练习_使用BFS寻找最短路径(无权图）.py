from collections import deque

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


def bfs_shortest_distance(start, target):
    visited = set()
    queue = deque()

    distance = {start: 0}

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()

        if current == target:
            return distance[current]
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    return -1

print("从 A 到 D 的最短距离（经过的边数）:", bfs_shortest_distance('A', 'D'))