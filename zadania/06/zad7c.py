from math import inf

def bin_search(T, val):
    l = 0
    r = len(T) - 1

    while l <= r:
        m = (l + r) // 2

        if T[m] == val:
            return m

        if val > T[m]:
            l = m + 1
        else:
            r = m - 1

    return None


def longest(intervals, K):
    T = []
    for x in intervals:
        T.append(x[0])
        T.append(x[1])

    T.sort()
    P = [T[0]]
    for i in range(1, len(T)):
        if P[len(P) - 1] != T[i]:
            P.append(T[i])

    print(P)

    n = len(P)
    F = [[inf] * n for _ in range(n)]

    for x in intervals:
        F[bin_search(P, x[0])][bin_search(P, x[1])] = 1

    best = 0
    result = None
    for x in range(1, n):
        i = 0
        while i + x < n:
            j = i + x
            for k in range(i + 1, j):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])

            if F[i][j] <= K and P[j] - P[i] > best:
                best = P[j] - P[i]
                result = (P[i], P[j])

            i += 1

    [print(x) for x in F]
    return best, result


arr = [(0, 3), (12, 16), (5, 10), (3, 7), (10, 12), (2, 5), (7, 10), (1, 2), (10, 17)]
res = longest(arr, 10)
print(res)
