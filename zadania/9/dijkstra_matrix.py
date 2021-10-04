from math import inf


def dijkstra(adj_matrix, s):
    n = len(adj_matrix)
    [print(x) for x in adj_matrix]

    d = [inf] * n
    d[s] = 0
    parent = [-1] * n
    visited = [False] * n
    for _ in range(n):
        u = 0
        u_distance = inf
        for v in range(n):
            if not visited[v] and d[v] < u_distance:
                u = v
                u_distance = d[v]

        visited[u] = True

        for v in range(n):
            # print("\t", v, edge_weight, w[v])
            if not visited[v] and adj_matrix[u][v] != 0 and d[u] + adj_matrix[u][v] < d[v]:
                parent[v] = u
                d[v] = d[u] + adj_matrix[u][v]

    print()
    print(d)
    print(parent)


# G = [[0, 1, 12, 0, 0, 0],
#      [1, 0, 7, 0, 5, 0],
#      [12, 7, 0, 0, 6, 8],
#      [0, 0, 0, 0, 30, 9],
#      [0, 5, 6, 30, 0, 4],
#      [0, 0, 8, 9, 4, 0]]

G = [[0, 1, 12, 0, 0, 0],
     [0, 0, 0, 0, 5, 0],
     [0, 7, 0, 0, 6, 8],
     [0, 0, 0, 0, 0, 9],
     [0, 0, 0, 30, 0, 0],
     [0, 0, 0, 0, 4, 0]]

dijkstra(G, 0)
