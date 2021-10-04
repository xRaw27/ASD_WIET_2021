def matching(adj_matrix):
    n = len(adj_matrix)

    edges = [sum(x) for x in adj_matrix]

    print(edges)

    stop = False
    result = []
    counter = 0
    while not stop:
        stop = True

        for u in range(n):
            if edges[u] == 1:
                counter += 1
                stop = False

                for v in range(n):
                    if adj_matrix[u][v] == 1:
                        result.append((u, v))

                        edges[v] = 0
                        for w in range(n):
                            if adj_matrix[v][w] == 1:
                                edges[w] -= 1
                                adj_matrix[v][w] = 0
                                adj_matrix[w][v] = 0

                        break

    print(edges)
    print(adj_matrix)

    print(counter)
    print(result)


# G = [[0, 1, 0, 0, 0, 0, 0, 0],
#      [1, 0, 1, 1, 0, 0, 0, 0],
#      [0, 1, 0, 0, 0, 0, 0, 0],
#      [0, 1, 0, 0, 1, 0, 0, 0],
#      [0, 0, 0, 1, 0, 1, 0, 0],
#      [0, 0, 0, 0, 1, 0, 1, 1],
#      [0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 1, 0, 0]]

G = [[0, 1, 0, 1, 0],
     [1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0],
     [1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0]]

matching(G)
