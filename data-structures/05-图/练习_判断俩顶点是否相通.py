from collections import deque

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def is_connected(graph, start, end):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:    
                visited.add(neighbor)
                queue.append(neighbor)
    return False
     

adj_list_broken = {
    'A': ['B', 'C'],
    'B': ['A'],         # 去 D 的桥没了
    'C': ['A', 'D'],
    'D': ['C']          # 去 B 的桥没了
}


print("桥断了后，A 和 D 连通吗？", is_connected(adj_list_broken, 'A', 'D'))

#参考答案
def is_connected_2(graph, start, end):
    visited = set()

    def dfs(node):
        if node == end:
            return True 
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False
    
    return dfs(start)
        