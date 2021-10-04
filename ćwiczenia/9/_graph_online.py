print("1. UNWEIGHTED\n2. WEIGHTED\n3. ADJ LIST TO MATRIX")

mode = int(input())

# [[(2, 60), (3, 40), (1, 50)], [(0, 50), (4, 49)], [(0, 60), (4, 30), (6, 10), (7, 19)], [(0, 40), (6, 43), (7, 42)], [(1, 49), (2, 30), (6, 45), (5, 20)], [(4, 20)], [(2, 10), (3, 43), (4, 45), (8, 15)], [(3, 42), (2, 19)], [(6, 15)]]
if mode == 3:
    inp = input()
    inp = inp.replace(" ", "")
    adj_list = inp.split("],[")

    n = len(adj_list)
    matrix = [[0] * n for _ in range(n)]

    for i in range(len(adj_list)):
        adj_list[i] = adj_list[i].replace("[", "").replace("]", "")
        adj_list[i] = adj_list[i].split(",")
        for j in range(len(adj_list[i])):
            adj_list[i][j] = int(adj_list[i][j].replace(")", "").replace("(", ""))

        xd = []
        for j in range(0, len(adj_list[i]), 2):
            xd.append((adj_list[i][j], adj_list[i][j + 1]))

        adj_list[i] = xd

    for u in range(n):
        for v, edge_weight in adj_list[u]:
            matrix[u][v] = edge_weight

    [print(x) for x in matrix]


else:
    print("matrix: ")
    matrix = []
    while True:
        inp = input()
        if inp == "":
            break

        inp = inp.replace("]", "").replace("[", "").replace(" ", "").replace("\t", "")
        if inp[len(inp) - 1] == ",":
            inp = inp[:len(inp) - 1]

        matrix.append([int(x) for x in inp.split(",")])

    print("G = [", end="")
    [print(x, ",", sep="") for x in matrix]
    print("]")

    n = len(matrix)
    adj_list = [[] for _ in range(n)]
    if mode == 1:
        for u in range(n):
            for v in range(n):
                if matrix[u][v] > 0:
                    adj_list[u].append(v)
    if mode == 2:
        n = len(matrix)
        adj_list = [[] for _ in range(n)]
        for u in range(n):
            for v in range(n):
                if matrix[u][v] != 0:
                    adj_list[u].append((v, matrix[u][v]))

    print()
    print("G =", adj_list)

