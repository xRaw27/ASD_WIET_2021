from math import inf

def decreasing_edges(adj_list, s):
    edges_list = []

    n = len(adj_list)
    for u in range(n):
        for v, edge_weight in adj_list[u]:
            edges_list.append((edge_weight, u, v))

    d = [inf] * n
    d[s] = 0
    parent = [-1] * n

    for edge_weight, u, v in edges_list:
        if d[u] + edge_weight < d[v]:
            d[v] = d[u] + edge_weight
            parent[v] = u

    edges_list.sort()
    edges_list.reverse()
    print(edges_list)

    print(d)
    print(parent)


G = [[(2, 60), (3, 40), (1, 50)], [(0, 50), (4, 49)], [(0, 60), (4, 30), (6, 10), (7, 19)], [(0, 40), (6, 43), (7, 42)], [(1, 49), (2, 30), (6, 45), (5, 20)], [(4, 20)], [(2, 10), (3, 43), (4, 45), (8, 15)], [(3, 42), (2, 19)], [(6, 15)]]

decreasing_edges(G, 0)
