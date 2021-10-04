def four_vertices_cycle(adj_matrix):
    n = len(adj_matrix)
    M = [[-1] * n for _ in range(n)]


    for i in range(n):
        _in = []
        _out = []

        for j in range(n):
            if adj_matrix[j][i] == 1:
                _in.append(j)
            if adj_matrix[i][j] == 1:
                _out.append(j)

        # print(_in, _out)
        for u in _in:
            for v in _out:
                M[u][v] = i
                if M[v][u] != -1:
                    return u, M[u][v], v, M[v][u]

    return None
    # [print(x) for x in M]


G = [[0, 0, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 0, 1],
     [0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 1, 0]]

res = four_vertices_cycle(G)
print(res)