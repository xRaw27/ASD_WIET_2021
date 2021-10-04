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

def heap_add(A, value):
    A.append(value)

    i = len(A) - 1
    while i > 0:
        j = parent(i)
        if A[j] < A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
        else:
            break




arr = [10, 1, 17, 2, 12, 7]
build_max_heap(arr)

arr2 = []
heap_add(arr2, 10)
print(arr2)
heap_add(arr2, 1)
print(arr2)
heap_add(arr2, 17)
print(arr2)
heap_add(arr2, 2)
print(arr2)
heap_add(arr2, 12)
print(arr2)
heap_add(arr2, 7)
print(arr2)
