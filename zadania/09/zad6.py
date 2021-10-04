from queue import PriorityQueue
from math import inf


def dijkstra(adj_list, s):
    n = len(adj_list)
    queue = PriorityQueue()

    d = [inf] * n
    d[2 * s] = 0
    d[2 * s + 1] = 0
    parent = [-1] * n
    visited = [False] * n

    queue.put((0, 2 * s))
    queue.put((0, 2 * s + 1))
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
    for u in range(n // 2):
        print("Wierzchołek ", u)
        print(d[2 * u], d[2 * u + 1])

    t = 2 * 2 + 1
    path = []
    while t != -1:
        if t % 2 != 0:
            path.append(("Alicja", t // 2))
        else:
            path.append(("Bob", t // 2))
        t = parent[t]

    path.reverse()
    print(path)


def two_drivers(adj_list, s, t):
    n = len(adj_list)

    adj_list_new = [[] for _ in range(2 * n)]

    for u in range(n):
        for v, weight in adj_list[u]:
            adj_list_new[2 * u].append((2 * v + 1, weight))
            adj_list_new[2 * u + 1].append((2 * v, 0))

    print(adj_list_new)
    dijkstra(adj_list_new, 0)


G = [[(1, 5), (5, 2)], [(0, 5), (2, 4), (4, 4), (5, 1)], [(1, 4), (3, 1), (4, 2)], [(2, 1), (4, 2)], [(1, 4), (2, 2), (3, 2), (5, 3)], [(0, 2), (1, 1), (4, 3)]]
two_drivers(G, 0, 3)

# G = [[(1, 3), (2, 5)], [(0, 3), (2, 3)], [(0, 5), (1, 3), (3, 6)], [(2, 6)]]
# two_drivers(G, 0, 3)
