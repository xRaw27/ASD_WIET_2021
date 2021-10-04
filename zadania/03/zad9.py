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

def quick_select(A, k):
    p = 0
    r = len(A) - 1
    while True:
        q = partition(A, p, r)
        if k > q:
            p = q + 1
        elif k < q:
            r = q - 1
        else:
            return A[q]


arr = [4, 1, 16, 17, 1, 18, 9, 3, 4, 1, 0]
arr2 = arr[:]

arr2.sort()
print(arr2)

print(quick_select(arr, 8))
