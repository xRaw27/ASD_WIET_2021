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


def heap_get(A):
    n = len(A)
    A[0], A[n - 1] = A[n - 1], A[0]

    max_heapify(A, n - 1, 0)

    return A.pop()


def zbigniew(A):
    n = len(A)
    print(A)

    heap = []
    result = 0

    e = A[0]
    for i in range(1, n - 1):
        e -= 1
        heap_add(heap, A[i])

        while e < 1:
            if len(heap) == 0:
                print("nie da sie")
                return False

            e += heap_get(heap)
            result += 1


    print(result + 1)


# zbigniew([4, 6, 0, 0, 2, 0, 0, 5, 0, 0, 0, 0, 1])
zbigniew([3, 0, 0, 2, 0, 0])
