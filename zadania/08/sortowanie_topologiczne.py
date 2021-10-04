from collections import deque


def topological_sort(adj_list):
    def DFSVisit(u):
        nonlocal adj_list, queue
        visited[u] = True

        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)

        queue.appendleft(u)

    queue = deque()
    n = len(adj_list)
    visited = [False] * n

    for u in range(n):
        if not visited[u]:
            DFSVisit(u)

    return queue


G = [[1, 2], [2, 4], [], [], [3, 6, 5], [], [], [1], [7]]
res = topological_sort(G)
print(res)