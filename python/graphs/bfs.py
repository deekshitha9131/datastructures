def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

graph = {
    0: [1,2],
    1: [0,3,4],
    2: [0,5],
    3: [1],
    4: [1],
    5: [2]
}
bfs(graph, 0)