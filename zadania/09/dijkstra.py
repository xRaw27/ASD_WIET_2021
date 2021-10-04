from queue import PriorityQueue
from math import inf


def dijkstra(adj_list, s):
    n = len(adj_list)
    queue = PriorityQueue()

    d = [inf] * n
    d[s] = 0
    parent = [None] * n
    visited = [False] * n

    queue.put((0, s))
    while not queue.empty():
        u = queue.get()[1]
        print(u)

        if visited[u]:
            continue

        visited[u] = True
        for v, edge_weight in adj_list[u]:
            # print("\t", v, edge_weight, w[v])
            if not visited[v] and d[u] + edge_weight < d[v]:
                parent[v] = u
                d[v] = d[u] + edge_weight
                queue.put((d[v], v))

    print(d)
    print(parent)


G = [[(1, 1), (2, 12)],
     [(0, 1), (2, 7), (4, 5)],
     [(0, 12), (1, 7), (4, 6), (5, 8)],
     [(4, 30), (5, 9)],
     [(1, 5), (2, 6), (3, 30), (5, 4)],
     [(2, 8), (3, 9), (4, 4)]]


dijkstra(G, 0)
