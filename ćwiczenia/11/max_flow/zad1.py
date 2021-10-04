from collections import deque
from math import inf


def extend(adj_list, s, t):
    print(adj_list)
    n = len(adj_list)

    parent = [None] * n
    visited = [False] * n
    visited[s] = True

    d = [inf] * n
    d[s] = 0

    width = [inf] * n

    queue = deque()
    queue.append(s)

    while len(queue) > 0:
        u = queue.popleft()

        if u == t:
            break

        for v, weight in adj_list[u]:
            if not visited[v] and weight > 0:
                visited[v] = True
                queue.append(v)
                d[v] = d[u] + 1
                parent[v] = u
                width[v] = min(width[u], weight)

    print(d)
    print(parent)
    print(width)
    if parent[t] is None:
        print('\n---------------------------------------------------------------------------------------------------\n')
        return 0

    max_width = width[t]
    v = t
    while v != s:
        u = parent[v]
        print(u, v, max_width)
        for x in adj_list[u]:
            if x[0] == v:
                x[1] -= max_width
                break

        for x in adj_list[v]:
            if x[0] == u:
                x[1] += max_width
                break

        v = u

    print(adj_list)
    print('\n---------------------------------------------------------------------------------------------------\n')

    return max_width


def edmonds_karp(adj_list, s, t):
    n = len(adj_list)

    residual_network = [[] for _ in range(n)]

    for u in range(n):
        for v, weight in adj_list[u]:
            residual_network[u].append([v, weight])
            residual_network[v].append([u, weight])

    x = extend(residual_network, s, t)
    max_flow = x
    while x > 0:
        x = extend(residual_network, s, t)
        max_flow += x

    return max_flow


G = [[(1, 16), (2, 13)],
     [(3, 12)],
     [(1, 4), (4, 14)],
     [(2, 9), (5, 20)],
     [(3, 7), (5, 4)],
     [(6, 9)],
     [],
     []]

# G2 = [[(1, 1000000), (2, 1000000)],
#       [(3, 1000000), (2, 1)],
#       [(3, 1000000)],
#       []]

G3 = [[], [(0, 10)], [(1, 5)]]
res = edmonds_karp(G, 0, 5)
print(res)
