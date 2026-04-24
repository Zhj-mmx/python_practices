adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end='')

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor)

print("DFS 访问顺序：")
dfs('A')



