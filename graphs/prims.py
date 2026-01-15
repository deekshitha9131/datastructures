#Start from any node, then repeatedly add the cheapest edge that connects the growing tree to a new vertex
import sys

def prim_mst(graph):
    V = len(graph)
    selected = [False]*V
    key = [sys.maxsize]*V
    parent = [-1]*V
    key[0] = 0
    for _ in range(V):
        min_val = sys.maxsize
        u = -1
        for v in range(V):
            if not selected[v] and key[v] < min_val:
                min_val = key[v]
                u = v

        selected[u] = True
        for v in range(V):
            if graph[u][v] > 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge \t Weight")
    for i in range(1, V):
        print(f"{parent[i] }- {i}\t{graph[i][parent[i]]}")

graph = [
    [0,2,0,6,0],
    [2,0,3,8,5],
    [0,3,0,0,7],
    [6,8,0,0,9],
    [0,5,7,9,0]
]
prim_mst(graph)