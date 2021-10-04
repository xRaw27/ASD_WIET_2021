def prom(A, L):
    n = len(A)

    F = [[0] * n for _ in range(L + 1)]
    P = [[0] * n for _ in range(L + 1)]

    for x in range(A[0]):
        F[x][0] = A[0]

    result = 0
    for i in range(1, n):
        for x in range(L + 1):
            F[x][i] = F[x][i - 1] + A[i]
            P[x][i] = x

            if x - A[i] >= 0 and F[x - A[i]][i - 1] < F[x][i]:
                F[x][i] = F[x - A[i]][i - 1]
                P[x][i] = x - A[i]

        if F[L][i] > L:
            result = i - 1
            break

    [print(x) for x in F]
    print()
    [print(x) for x in P]
    up = []
    down = []
    x = L
    for i in range(result, -1, -1):
        if P[x][i] == x:
            up.append(A[i])
        else:
            down.append(A[i])
            x = P[x][i]

    print(up, down)


# prom([1, 7, 5, 11, 13, 18], 12)
# prom([7, 4, 2, 8, 1, 4, 6, 4], 11)
prom([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11)
# ([1, 8, 2], [4, 7])
