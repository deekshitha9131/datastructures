def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x,y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(vertices, edges):
    edges.sort(key=lambda x: x[2])

    parent = []
    rank = []
    for i in range(vertices):
        parent.append(i)
        rank.append(0)
    mst = []
    e = 0
    i = 0
    while e < vertices-1 and i<len(edges):
        u,v,w = edges[i]
        i+=1
        x = find(parent, u)
        y = find(parent, v)
        if x!= y:
            mst.append((u,v,w))
            union(parent, rank, x, y)
            e += 1

    print("Edge \tWeight")
    for u, v, w in mst:
        print(f"{u} - {v}\t{w}")