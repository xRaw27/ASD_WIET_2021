from random import randint, seed
from time import time


def merge(T, A, l, m, r):
    for i in range(l, m + 1):
        A[i] = T[i]

    p = l
    q = m + 1
    i = l
    while p <= m and q <= r:
        if A[p] < T[q]:
            T[i] = A[p]
            p += 1
        else:
            T[i] = T[q]
            q += 1
        i += 1

    while p <= m:
        T[i] = A[p]
        p += 1
        i += 1


def merge_sort(T, A, l, r):
    if l == r:
        return

    m = (l + r) // 2
    merge_sort(T, A, l, m)
    merge_sort(T, A, m + 1, r)
    merge(T, A, l, m, r)


def ms(T):
    n = len(T)
    A = [0] * n
    merge_sort(T, A, 0, n - 1)


def merge_sort_iterative(T):
    n = len(T)
    A = [0] * n

    # -1 - divide, else - merge
    stack = [(0, n - 1, -1)]
    while len(stack) > 0:
        l, r, m = stack.pop()

        if m == -1 and l < r:
            m = (l + r) // 2
            stack.append((l, r, m))
            stack.append((l, m, -1))
            stack.append((m + 1, r, -1))

        if m >= 0:
            merge(T, A, l, m, r)



# arr = [1, 7, 5, 3, 4, 2, 5, 1, -90, 43, 12, 3, 123, 312, 312, 31263, 13, 3, 3, 12, 163, 13, 123, 123, 12]
# # ms(arr)
# merge_sort_iterative(arr)
# print(arr)

arr = [randint(0, 100000) for _ in range(0, 100000)]
arr_copy = arr[:]
arr_copy.sort()

start = time()
ms(arr)
# merge_sort_iterative(arr)

print(time() - start)
print(arr == arr_copy)
