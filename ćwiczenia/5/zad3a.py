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

    [print(x) for x in F]
    return F[m][n]

def lis(A):
    B = A[:]
    B.sort()

    return lcs(A, B)


res = lis([7, 1, 2, 8, 5, 6, 5, 4, 3])
print(res)

