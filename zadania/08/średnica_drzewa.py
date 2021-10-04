from collections import deque

def BFS(adj_list, s):
    queue = deque()
    n = len(adj_list)

    visited = [False] * n
    d = [-1] * n

    d[s] = 0
    visited[s] = True
    queue.append(s)

    while len(queue) > 0:
        u = queue.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                queue.append(v)

    return d


def srednica_drzewa(adj_list):
    n = len(adj_list)
    d = BFS(adj_list, 0)

    v = 0
    for i in range(n):
        if d[i] > d[v]:
            v = i

    print(d)

    d = BFS(adj_list, v)
    return max(d)


G = [[1, 10], [0, 2, 4, 5], [1, 3], [2], [1], [1, 6, 7], [5], [5, 8, 9], [7], [7], [0]]
res = srednica_drzewa(G)
print(res)