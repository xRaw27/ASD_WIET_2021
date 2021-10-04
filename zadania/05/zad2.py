def subset_sum_problem(A, T):
    n = len(A)

    F = [[False] * n for _ in range(T + 1)]
    F[A[0]][0] = True
    F[0][0] = True

    for i in range(1, n):
        for t in range(T + 1):
            if F[t][i - 1] or (t - A[i] >= 0 and F[t - A[i]][i - 1]):
                F[t][i] = True



    [print(x) for x in F]


arr = [3, 7, 15, 8, 9, 2, 12]
subset_sum_problem(arr, 20)
