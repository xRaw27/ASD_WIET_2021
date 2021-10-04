def bin_search(T, val):
    l = 0
    r = len(T) - 1

    while l <= r:
        m = (l + r) // 2

        if T[m] == val:
            return m

        if val > T[m]:
            l = m + 1
        else:
            r = m - 1

    return None


def interval(intervals, a, b):
    def DFSVisit(u):
        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(v)

    T = []
    for x in intervals:
        T.append(x[0])
        T.append(x[1])

    T.sort()
    P = [T[0]]
    for i in range(1, len(T)):
        if P[len(P) - 1] != T[i]:
            P.append(T[i])

    if bin_search(P, a) is None or bin_search(P, b) is None:
        return False

    n = len(P)
    adj_list = [[] for _ in range(n)]
    visited = [False] * n

    for x in intervals:
        v1 = bin_search(P, x[0])
        v2 = bin_search(P, x[1])
        adj_list[v1].append(v2)

    DFSVisit(bin_search(P, a))
    return visited[bin_search(P, b)]


arr = [(0, 3), (12, 16), (5, 10), (3, 7), (10, 12), (2, 5), (7, 10), (1, 2), (10, 17)]
res = interval(arr, 1, 7)
print(res)
