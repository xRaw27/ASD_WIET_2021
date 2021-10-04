def best_root(adj_list):
    def DFSVisit(u):
        visited[u] = True

        for v, edge_weight in adj_list[u]:
            if not visited[v]:
                d[v] = d[u] + edge_weight
                parent[v] = u
                DFSVisit(v)

    n = len(adj_list)
    visited = [False] * n
    parent = [-1] * n
    d = [0] * n
    DFSVisit(0)

    s = 0
    for i in range(n):
        if d[i] > d[s]:
            s = i

    visited = [False] * n
    parent = [-1] * n
    d[s] = 0
    DFSVisit(s)

    t = 0
    for i in range(n):
        if d[i] > d[t]:
            t = i

    print(s, t)
    diameter = d[t]
    root = t
    while d[parent[root]] > diameter / 2:
        root = parent[root]

    if max(d[parent[root]], diameter - d[parent[root]]) < max(d[root], diameter - d[root]):
        root = parent[root]

    print(root)
    print(parent)
    print(visited)
    print(d)



G = [[(1, 7), (7, 6), (8, 4)], [(0, 7), (2, 8), (3, 6)], [(1, 8)], [(1, 6), (4, 3), (5, 5), (6, 8)], [(3, 3)], [(3, 5)], [(3, 8)], [(0, 6)], [(0, 4), (9, 2), (10, 5), (11, 3)], [(8, 2)], [(8, 5)], [(8, 3), (12, 3), (13, 1)], [(11, 3)], [(11, 1)]]
best_root(G)


