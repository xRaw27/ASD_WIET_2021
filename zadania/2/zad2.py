from random import randint, seed
from time import time

seed(123)

def inversions(arr):
    def merge(T, A, l, m, r):
        nonlocal result

        for i in range(l, m + 1):
            A[i] = T[i]

        p = l
        q = m + 1
        i = l
        while p <= m and q <= r:
            if A[p] <= T[q]:
                T[i] = A[p]
                # print(q - (m + 1))
                result += q - (m + 1)
                p += 1
            else:
                T[i] = T[q]
                q += 1
            i += 1

        while p <= m:
            T[i] = A[p]
            # print(q - (m + 1))
            result += q - (m + 1)
            p += 1
            i += 1


    def divide(T, A, l, r):
        if l == r:
            return

        m = (l + r) // 2
        divide(T, A, l, m)
        divide(T, A, m + 1, r)
        merge(T, A, l, m, r)

    result = 0
    n = len(arr)
    arr2 = [0] * n
    divide(arr, arr2, 0, n - 1)

    return result


xd = [randint(-100000, 100000) for _ in range(0, 100000)]

start = time()
print(inversions(xd))
print(time() - start)
