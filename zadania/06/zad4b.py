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
    if l < n and A[l][0] > A[m][0]:
        m = l
    if r < n and A[r][0] > A[m][0]:
        m = r

    if i != m:
        A[i], A[m] = A[m], A[i]
        max_heapify(A, n, m)


def heap_add(A, value):
    A.append(value)

    i = len(A) - 1
    while i > 0:
        j = parent(i)
        if A[j][0] < A[i][0]:
            A[i], A[j] = A[j], A[i]
            i = j
        else:
            break


def heap_get(A):
    n = len(A)
    A[0], A[n - 1] = A[n - 1], A[0]

    max_heapify(A, n - 1, 0)

    return A.pop()


def zbigniew(A):
    n = len(A)
    heap = []
    jumps = [0]
    result = 0

    e = A[0]
    i = 0
    while i < n - 1:
        if e >= 1:
            e -= 1
            i += 1
            if A[i] > 0:
                heap_add(heap, (A[i], i))

        else:
            if len(heap) == 0:
                return -1

            new_e, index = heap_get(heap)
            e += new_e
            jumps.append(index)

            result += 1

    jumps.append(n - 1)
    print(jumps)
    return result + 1


res = zbigniew([4, 6, 0, 0, 2, 0, 0, 5, 0, 0, 0, 0, 1])
# res = zbigniew([3, 0.5, 0.5, 0.5, 0.5, 0])
print(res)

