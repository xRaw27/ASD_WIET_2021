from collections import deque
from math import inf


def BFS(adj_list, s, t):
    n = len(adj_list)
    d = [inf] * n
    visited = [False] * n
    parent = [-1] * n

    queue = deque()
    queue.append(s)
    d[s] = 0
    visited[s] = True
    while len(queue) > 0:
        u = queue.popleft()

        for v in adj_list[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                visited[v] = True
                queue.append(v)

    if d[t] == inf:
        return None

    result = []
    while t != -1:
        result.append(t)
        t = parent[t]

    result.reverse()
    print(d)
    print(parent)
    print(result)
    
    return result


G = [[5], [0, 6], [1, 6], [2, 4], [], [1, 4], [3, 5]]
BFS(G, 0, 2)
