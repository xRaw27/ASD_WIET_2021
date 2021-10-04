from math import inf


def bellman_ford(adj_list, s):
    n = len(adj_list)
    d = [inf] * n
    parent = [-1] * n

    d[s] = 0
    for i in range(n - 1):
        for u in range(n):
            for v, edge_weight in adj_list[u]:
                if d[u] + edge_weight < d[v]:
                    d[v] = d[u] + edge_weight
                    parent[v] = u

    print(d)
    print(parent)

    for u in range(n):
        for v, edge_weight in adj_list[u]:
            if d[u] + edge_weight < d[v]:
                print("ujemny cykl")
                return




G = [[(1, 5), (2, 6), (4, 1)], [(0, 5), (2, 2), (3, 1), (4, 3), (6, 8)], [(0, 6), (1, 2), (3, 3), (5, 4)], [(1, 1), (2, 3), (5, 3)], [(0, 1), (1, 3)], [(2, 4), (3, 3), (6, 3)], [(1, 8), (5, 3), (7, 3)], [(6, 3)]]
bellman_ford(G, 0)

