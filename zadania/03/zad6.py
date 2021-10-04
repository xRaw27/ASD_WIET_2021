def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def parent(i):
    return (i - 1) // 2

def min_heap_add(A, value):
    A.append(value)

    i = len(A) - 1
    while i > 0:
        j = parent(i)
        if A[j] > A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
        else:
            break

def max_heap_add(A, value):
    A.append(value)

    i = len(A) - 1
    while i > 0:
        j = parent(i)
        if A[j] < A[i]:
            A[i], A[j] = A[j], A[i]
            i = j
        else:
            break

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
        max_heapify(A, n, m)

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


def insert(structure, value):
    max_heap = structure[0]
    min_heap = structure[1]

    n, m = len(max_heap), len(min_heap)

    print(max_heap, min_heap)
    print(n, m)

    if n == m == 0:
        max_heap_add(max_heap, value)

    elif n == m:
        if value > max_heap[0]:
            min_heap_add(min_heap, value)
        else:
            max_heap_add(max_heap, value)

    elif n > m:
        if value < max_heap[0]:
            max_heap[0], value = value, max_heap[0]
            max_heapify(max_heap, n, 0)

        min_heap_add(min_heap, value)

    else:
        if value > min_heap[0]:
            min_heap[0], value = value, min_heap[0]
            min_heapify(min_heap, m, 0)

        max_heap_add(max_heap, value)


    print()
    print(max_heap, min_heap)

def remove_median(structure):
    max_heap = structure[0]
    min_heap = structure[1]

    n, m = len(max_heap), len(min_heap)

    if n == m == 0:
        return None

    elif n == m:
        result = (max_heap[0] + min_heap[0]) / 2

        max_heap[0], max_heap[n - 1] = max_heap[n - 1], max_heap[0]
        max_heap.pop()
        max_heapify(max_heap, n - 1, 0)

        min_heap[0], min_heap[m - 1] = min_heap[m - 1], min_heap[0]
        min_heap.pop()
        min_heapify(min_heap, m - 1, 0)

        return result

    elif n > m:
        result = max_heap[0]

        max_heap[0], max_heap[n - 1] = max_heap[n - 1], max_heap[0]
        max_heap.pop()
        max_heapify(max_heap, n - 1, 0)

        return result

    else:
        result = min_heap[0]

        min_heap[0], min_heap[m - 1] = min_heap[m - 1], min_heap[0]
        min_heap.pop()
        min_heapify(min_heap, m - 1, 0)

        return result




xd = [[], []]
insert(xd, 3)
insert(xd, 1)
insert(xd, 2)
insert(xd, 5)
insert(xd, 6)
# insert(xd, 10)
insert(xd, 4)
insert(xd, 0)
print()
print()
print()
print(remove_median(xd))
print(xd)
