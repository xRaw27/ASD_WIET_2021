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

def quicksort(A):
    n = len(A)
    stack = [(0, n - 1)]

    while len(stack) > 0:
        p, r = stack.pop()
        if p < r:
            q = partition(A, p, r)
            stack.append((p, q - 1))
            stack.append((q + 1, r))


arr = [7, 2, 4, 8, 5, 1, 3]

quicksort(arr)

print(arr)
