# zakładamy że graf jest spójny

def articulation_points(adj_list):
    def DFSVisit(u):
        nonlocal time

        visited[u] = True
        d[u] = time
        low[u] = d[u]
        time += 1

        for v in adj_list[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(v)
                if low[v] >= d[u]:
                    is_articulation_point[u] = True

                low[u] = min(low[u], low[v])

            elif parent[u] != v:
                low[u] = min(low[u], d[v])


    n = len(adj_list)
    visited = [False] * n
    is_articulation_point = [False] * n
    parent = [-1] * n
    d = [-1] * n
    low = [-1] * n

    time = 1
    DFSVisit(0)

    root_children = 0
    for i in range(n):
        if parent[i] == 0: root_children += 1

    is_articulation_point[0] = False
    if root_children >= 2:
        is_articulation_point[0] = True

    print(d)
    print(low)
    print(parent)
    print(is_articulation_point)


G = [[1, 12], [0, 2, 9], [1, 3, 7], [2, 4], [3, 5, 8, 10, 11], [4, 6], [5, 7], [2, 6], [4, 9], [1, 8], [4, 11], [4, 10], [0, 13, 14, 15, 16], [12, 14], [12, 13], [12, 16], [12, 15]]
articulation_points(G)

