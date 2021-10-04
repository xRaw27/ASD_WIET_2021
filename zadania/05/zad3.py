def lcs(A, B):
    n = len(A)
    m = len(B)

    F = [[0] * (n + 1) for _ in range(m + 1)]

    # i -> A, j -> B
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                F[j][i] = F[j - 1][i - 1] + 1

            else:
                F[j][i] = max(F[j][i - 1], F[j - 1][i])


    return F[m][n]


res = lcs([1, 7, 9, 12, 19, 21], [3, 9, 11, 12, 15, 19, 50])
print(res)

a = [3, 7, 8, 2, 5, 4, 1, 3]
b = [7, 3, 8, 2, 1, 4, 5, 3]
res = lcs(a, b)
print(res)
