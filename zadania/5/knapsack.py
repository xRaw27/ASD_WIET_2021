def get_solution(F, W, P, i, w):
    if i < 0: return []
    if i == 0:
        if w >= W[0]: return [0]
        return []

    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]

    return get_solution(F, W, P, i - 1, w)


def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0] * (MaxW + 1) for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])

    [print(x) for x in F]
    print(F[n - 1][MaxW])
    print(get_solution(F, W, P, n - 1, MaxW))


# W = [4, 2, 5, 1, 2]
# P = [4, 1, 2, 5, 3]

W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
knapsack(W, P, 24)
