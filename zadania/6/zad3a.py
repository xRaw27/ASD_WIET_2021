def prom(A, L):
    n = len(A)

    F = [[[False] * n for _ in range(L + 1)] for _ in range(L + 1)]

    # F[x][y][i] = 0

    for x in range(L + 1):
        for y in range(L + 1):
            if x >= A[0] or y >= A[0]:
                F[x][y][0] = True



    i = 1
    while i < n:
        for x in range(L + 1):
            for y in range(L + 1):
                condition1 = condition2 = False
                if x - A[i] >= 0:
                    condition1 = F[x - A[i]][y][i - 1]
                if y - A[i] >= 0:
                    condition1 = F[x][y - A[i]][i - 1]

                F[x][y][i] = condition1 or condition2

        if not F[L][L][i]:
            break

        i += 1

    print(i)

    [print(x) for x in F]

    # for i in range(n):


# prom([4, 5, 11, 13, 18], 17)
prom([7, 4, 2, 8, 1, 4, 6, 4], 11)
