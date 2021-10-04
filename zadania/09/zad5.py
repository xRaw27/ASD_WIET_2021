from math import inf
from queue import PriorityQueue

def max_extending_path(adj_list, s, t):

    n = len(adj_list)
    visited = [False] * n
    parent = [-1] * n
    capacity = [-inf] * n
    capacity[s] = inf

    queue = PriorityQueue()

    queue.put((-capacity[s], s))

    while not queue.empty():
        u_capacity, u = queue.get()
        u_capacity *= -1

        if u == t: break
        if visited[u]: continue

        visited[u] = True
        for v, edge_weight in adj_list[u]:
            if not visited[v] and min(u_capacity, edge_weight) > capacity[v]:
                capacity[v] = min(u_capacity, edge_weight)
                parent[v] = u
                queue.put((-capacity[v], v))

    print(capacity)
    print(parent)

    path = []
    while parent[t] != -1:
        path.append(t)
        t = parent[t]
    path.append(s)
    path.reverse()
    print(path)



G = [[(1, 5), (6, 3)], [(2, 1)], [(3, 2)], [], [(3, 8)], [(3, 3), (4, 2)], [(1, 3), (2, 8), (5, 4)]]
# G = [[(1, 5), (6, 3)], [(2, 1)], [(3, 2)], [], [(3, 8)], [(3, 3), (4, 2)], [(1, 3), (2, 8)]]
max_extending_path(G, 0, 3)

# 0, 5, 0, 0, 0, 0, 3,
# 0, 0, 1, 0, 0, 0, 0,
# 0, 0, 0, 2, 0, 0, 0,
# 0, 0, 0, 0, 0, 0, 0,
# 0, 0, 0, 8, 0, 0, 0,
# 0, 0, 0, 3, 2, 0, 0,
# 0, 3, 8, 0, 0, 4, 0,
