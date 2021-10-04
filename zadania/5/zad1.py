from math import inf

def knapsack(P, W, max_W):
    n = len(P)
    profit_sum = 0

    for x in P:
        profit_sum += x

    print(profit_sum)
    F = [[inf] * n for _ in range(profit_sum + 1)]
    F[0][0] = 0

    p = 1
    while p <= P[0]:
        F[p][0] = W[0]
        p += 1


    for i in range(1, n):
        for p in range(profit_sum + 1):
            if p - P[i] >= 0:
                F[p][i] = min(F[p][i - 1], F[p - P[i]][i - 1] + W[i])
            else:
                F[p][i] = min(F[p][i - 1], W[i])

    result = 0
    for p in range(profit_sum, -1, -1):
        if F[p][n - 1] <= max_W:
            result = p
            break

    [print(x) for x in F]

    return result, get_solution(F, P, W, result, n)


def get_solution(F, P, W, p, n):
    i = n - 1
    result = []
    while i > 0:
        if F[p][i - 1] != F[p][i]:
            result.append(i)
            p -= P[i]
        i -= 1

    if p > 0:
        result.append(0)

    return result


profit = [1, 10, 8, 4, 5, 3, 7]
weight = [100, 4, 5, 12, 9, 1, 13]
res = knapsack(profit, weight, 24)
print(res)
