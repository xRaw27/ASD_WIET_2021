from random import randint

def counting_sort(A, d):
    n = len(A)
    B = [0] * n
    C = [0] * n

    for x in A:
        index = (x // (n ** d)) % n
        C[index] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        index = (A[i] // (n ** d)) % n
        C[index] -= 1
        B[C[index]] = A[i]

    for i in range(n):
        A[i] = B[i]

def linear_sort(A):
    # w tablicy A znajduje się n elementów z zakresu 0,..., n^2 - 1

    counting_sort(A, 0)
    counting_sort(A, 1)

    print(A)


# arr = [1, 4, 5, 1, 3, 5, 6, 2, 2, 3, 1]
# arr = [1, 4, 1, 2, 0, 3, 2, 1]
m = 30
arr = [randint(0, (m ** 2) - 1) for _ in range(m)]
print(arr)
linear_sort(arr)


