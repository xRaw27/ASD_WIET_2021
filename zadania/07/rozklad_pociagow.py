def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def parent(i):
    return (i - 1) // 2


def min_heapify(A, n, i):
    m = i
    l = left(i)
    r = right(i)
    if l < n and A[l] < A[m]:
        m = l
    if r < n and A[r] < A[m]:
        m = r

    if i != m:
        A[i], A[m] = A[m], A[i]
        min_heapify(A, n, m)


def heap_add(A, value):
    A.append(value)

    i = len(A) - 1
    while i > 0:
        j = parent(i)
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
        else:
            break


def heap_pop(A):
    n = len(A)
    A[0], A[n - 1] = A[n - 1], A[0]
    min_heapify(A, n - 1, 0)
    A.pop()



def platforms(T, m):
    n = len(T)
    heap = []

    for x in T:
        arrival_time, departure_time = x
        while len(heap) > 0 and heap[0] <= arrival_time:
            heap_pop(heap)

        heap_add(heap, departure_time)
        print(heap)

        if len(heap) > m:
            return False

    return True


arr = [(2, 8), (5, 8), (5, 10), (7, 10), (9, 15)]
res = platforms(arr, 3)
print(res)