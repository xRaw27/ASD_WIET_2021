def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def parent(i):
    return (i - 1) // 2

def max_heapify(A, n, i):
    m = i
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[m]:
        m = l
    if r < n and A[r] > A[m]:
        m = r

    if i != m:
        A[i], A[m] = A[m], A[i]
        max_heapify(A, n, m)

def build_max_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        max_heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_max_heap(A)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


arr = [10, 1, 17, 2, 12, 7]
heap_sort(arr)

print(arr)

