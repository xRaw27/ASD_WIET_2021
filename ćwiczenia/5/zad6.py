from math import inf

def monety(A, value):
    n = len(A)

    F = [inf] * (value + 1)
    F[0] = 0

    for i in range(value + 1):
        for x in A:
            F[i] = min(F[i], F[i - x] + 1)

    print(F)


monety([1, 5, 8], 15)
