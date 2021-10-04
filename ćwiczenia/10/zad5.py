from math import sqrt, ceil, inf


def is_connected(adj_matrix):
    def DFSVisit(u):
        visited[u] = True
        for v in range(n):
            if adj_matrix[u][v] > 0 and not visited[v]:
                DFSVisit(v)

    n = len(adj_matrix)
    visited = [False] * n
    DFSVisit(0)

    for x in visited:
        if not x: return False

    return True


def highway(A):
    n = len(A)
    adj_matrix = [[0] * n for _ in range(n)]
    edges_list = []

    for u in range(n):
        for v in range(u + 1, n):
            dist = ceil(sqrt((A[u][0] - A[v][0]) ** 2 + (A[u][1] - A[v][1]) ** 2))
            edges_list.append((dist, u, v))

    edges_list.sort()
    result = inf
    first = 0
    last = -1
    while True:
        if not is_connected(adj_matrix):
            last += 1
            if last == len(edges_list): break

            edge_weight, u, v = edges_list[last]
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
        else:
            result = min(edges_list[last][0] - edges_list[first][0], result)
            edge_weight, u, v = edges_list[first]
            adj_matrix[u][v] = 0
            adj_matrix[v][u] = 0
            first += 1

    return result
