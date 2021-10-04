from queue import PriorityQueue
from math import inf


def prim_mst(adj_list):
    n = len(adj_list)
    queue = PriorityQueue()

    w = [inf] * n
    parent = [None] * n
    visited = [False] * n

    queue.put((0, 0))
    while not queue.empty():
        u = queue.get()[1]
        print(u)

        if visited[u]:
            continue

        visited[u] = True
        for v, edge_weight in adj_list[u]:
            print("\t", v, edge_weight, w[v])
            if not visited[v] and edge_weight < w[v]:
                parent[v] = u
                w[v] = edge_weight
                queue.put((edge_weight, v))

    print(parent)


G = [[(1, 1), (2, 12)],
     [(0, 1), (2, 7), (4, 5)],
     [(0, 12), (1, 7), (4, 6), (5, 8)],
     [(4, 30), (5, 9)],
     [(1, 5), (2, 6), (3, 30), (5, 4)],
     [(2, 8), (3, 9), (4, 4)]]

prim_mst(G)
