from random import randint

def partition(A, p, r):
    x = randint(p, r)
    A[x], A[r] = A[r], A[x]

    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)

        if q - p < r - q:
            quick_sort(A, p, q - 1)
            p = q + 1
        else:
            quick_sort(A, q + 1, r)
            r = q - 1

