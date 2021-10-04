from queue import PriorityQueue
from math import inf


def two_drivers(adj_list, s, t):
    n = len(adj_list)
    queue = PriorityQueue()

    d = [[inf, inf] for _ in range(n)]
    d[s] = [0, 0]

    parent = [[(-1, -1), (-1, -1)] for _ in range(n)]
    visited = [[False, False] for _ in range(n)]

    queue.put((0, s, 0))
    queue.put((0, s, 1))

    while not queue.empty():
        _, u, driver = queue.get()
        print(u, driver)

        if visited[u][driver]:
            continue

        visited[u][driver] = True

        for v, edge_weight in adj_list[u]:
            # print("\t", v, edge_weight, w[v])
            new_distance = d[u][driver]
            if driver == 0:
                new_distance += edge_weight

            if not visited[v][(driver + 1) % 2] and new_distance < d[v][(driver + 1) % 2]:
                parent[v][(driver + 1) % 2] = (u, driver)
                d[v][(driver + 1) % 2] = new_distance
                queue.put((new_distance, v, (driver + 1) % 2))

    print(d)
    print(parent)

    driver = 0
    if d[t][1] < d[t][0]:
        driver = 1

    path = []
    while t != -1:
        if driver == 1: path.append(("Alicja", t))
        else: path.append(("Bob", t))
        t, driver = parent[t][driver]

    path.reverse()
    print(path)


G = [[(1, 5), (5, 2)], [(0, 5), (2, 4), (4, 4), (5, 1)], [(1, 4), (3, 1), (4, 2)], [(2, 1), (4, 2)], [(1, 4), (2, 2), (3, 2), (5, 3)], [(0, 2), (1, 1), (4, 3)]]
two_drivers(G, 0, 4)

# G = [[(1, 3), (2, 5)], [(0, 3), (2, 3)], [(0, 5), (1, 3), (3, 6)], [(2, 6)]]
# two_drivers(G, 0, 3)
# G = [[(1, 5), (7, 1)], [(0, 5), (2, 5)], [(1, 5), (3, 5)], [(2, 5), (4, 5)], [(3, 5), (5, 100)], [(4, 100), (6, 1)], [(5, 1), (7, 100)], [(0, 1), (6, 100)]]
# two_drivers(G, 2, 7)
