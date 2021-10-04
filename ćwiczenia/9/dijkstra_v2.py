from queue import PriorityQueue
from math import inf


def dijkstra(adj_list, s):
    n = len(adj_list)
    queue = PriorityQueue()

    d = [inf] * n
    d[s] = 0
    parent = [None] * n
    visited = [False] * n

    queue.put((0, s, None))
    while not queue.empty():
        u_d, u, u_parent = queue.get()

        if visited[u]:
            continue

        visited[u] = True
        parent[u] = u_parent
        d[u] = u_d

        for v, edge_weight in adj_list[u]:
            queue.put((d[u] + edge_weight, v, u))



    print(d)
    print(parent)


G = [[(1, 1), (2, 12)],
     [(0, 1), (2, 7), (4, 5)],
     [(0, 12), (1, 7), (4, 6), (5, 8)],
     [(4, 30), (5, 9)],
     [(1, 5), (2, 6), (3, 30), (5, 4)],
     [(2, 8), (3, 9), (4, 4)]]


dijkstra(G, 0)
