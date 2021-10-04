def transitive_closure(adj_matrix):
    def DFSVisit(s, u):
        if s != u:
            M[s][u] = 1

        visited[u] = True
        for v in adj_list[u]:
            if not visited[v]:
                DFSVisit(s, v)

    n = len(adj_matrix)
    adj_list = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if adj_matrix[u][v] > 0:
                adj_list[u].append(v)

    M = [[0] * n for _ in range(n)]
    for u in range(n):
        visited = [False] * n
        DFSVisit(u, u)

    [print(x) for x in M]


G = [[0, 4, 5, 0, 0, 0, 0, 0],
     [0, 0, 3, 12, 0, 0, 0, 22],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 3, 0, 0, 0, 0],
     [0, 0, 0, 11, 0, 0, 0, 0],
     [55, 0, 13, 0, 0, 13, 0, 0],
     [0, 0, 0, 21, 5, 0, 0, 0]]
transitive_closure(G)
