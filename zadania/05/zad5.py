def max_min(A, k):
    n = len(A)

    F = [[0] * k for _ in range(n)]
    S = [0] * n

    S[0] = A[0]
    for i in range(1, n):
        S[i] = S[i - 1] + A[i]

    print(S)

    for i in range(n):
        F[i][0] = S[i]

    for curr_k in range(1, k):
        for i in range(n):
            best = 0
            for j in range(0, i):
                best = max(best, min(F[j][curr_k - 1], S[i] - S[j]))

            F[i][curr_k] = best

    [print(x) for x in F]


arr = [1, 4, 2, 8, 5, 2, 3, 2]
max_min(arr, 3)
